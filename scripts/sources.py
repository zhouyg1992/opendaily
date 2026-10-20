# SPDX-License-Identifier: MIT
"""Collect candidate repositories from GitHub Trending, GitHub Search and Hacker News."""
from __future__ import annotations

import json
import math
import re
import time
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
from datetime import date, timedelta
from urllib.parse import quote

from util import (
    DATA_DIR,
    GitHub,
    HttpClient,
    clean_markdown,
    log,
    parse_count,
    strip_tags,
    truncate,
)

TRENDING_URL = "https://github.com/trending"
ARTICLE_RE = re.compile(r'<article class="Box-row">(.*?)</article>', re.S)
H2_RE = re.compile(r"<h2[^>]*>(.*?)</h2>", re.S)
REPO_HREF_RE = re.compile(r'href="/([^"/\s]+/[^"/\s]+)"')
DESC_RE = re.compile(r'<p[^>]*class="[^"]*col-9[^"]*"[^>]*>(.*?)</p>', re.S)
LANG_RE = re.compile(r'itemprop="programmingLanguage">([^<]+)<')
TODAY_RE = re.compile(r"([\d,]+)\s+stars today")

RESERVED_OWNERS = {
    "about",
    "apps",
    "collections",
    "contact",
    "customer-stories",
    "events",
    "explore",
    "features",
    "issues",
    "join",
    "login",
    "marketplace",
    "new",
    "notifications",
    "orgs",
    "pricing",
    "readme",
    "search",
    "security",
    "settings",
    "site",
    "sponsors",
    "topics",
    "trending",
    "users",
}

CACHE_DIR = DATA_DIR / ".cache" / "repos"


@dataclass
class Candidate:
    full_name: str
    description: str = ""
    language: str = ""
    stars: int = 0
    forks: int = 0
    stars_today: int = 0
    topics: list[str] = field(default_factory=list)
    created_at: str = ""
    pushed_at: str = ""
    hn_points: int = 0
    sources: list[str] = field(default_factory=list)
    archived: bool = False
    fork: bool = False
    readme: str = ""
    score: float = 0.0

    def __post_init__(self) -> None:
        self.full_name = self.full_name.strip()
        if "/" not in self.full_name:
            raise ValueError(f"bad repo name: {self.full_name!r}")
        self.owner, self.name = self.full_name.split("/", 1)

    @property
    def url(self) -> str:
        return f"https://github.com/{self.full_name}"


def _extract_count(article: str, kind: str) -> int:
    match = re.search(
        rf'href="/[^"]+/{kind}"[^>]*>.*?</svg>\s*([\d,]+)', article, re.S
    )
    return parse_count(match.group(1)) if match else 0


def parse_trending(html_text: str, language: str | None) -> list[Candidate]:
    out: list[Candidate] = []
    for block in ARTICLE_RE.findall(html_text):
        h2 = H2_RE.search(block)
        if not h2:
            continue
        repo_match = None
        for href in REPO_HREF_RE.findall(h2.group(1)):
            owner = href.split("/", 1)[0]
            if owner.lower() in RESERVED_OWNERS or href.count("/") != 1:
                continue
            repo_match = href
            break
        if not repo_match:
            continue

        desc_match = DESC_RE.search(block)
        desc = strip_tags(desc_match.group(1)) if desc_match else ""
        lang_match = LANG_RE.search(block)
        today_match = TODAY_RE.search(block)

        out.append(
            Candidate(
                full_name=repo_match,
                description=truncate(desc, 400),
                language=(lang_match.group(1).strip() if lang_match else language or ""),
                stars=_extract_count(block, "stargazers"),
                forks=_extract_count(block, "forks"),
                stars_today=parse_count(today_match.group(1)) if today_match else 0,
                sources=["trending"],
            )
        )
    return out


def fetch_trending(cfg: dict) -> list[Candidate]:
    conf = cfg["sources"]["trending"]
    if not conf.get("enabled", True):
        return []
    client = HttpClient()
    since = conf.get("since", "daily")
    urls = [(f"{TRENDING_URL}?since={since}", None)]
    for lang in conf.get("languages", []):
        urls.append((f"{TRENDING_URL}/{quote(lang)}?since={since}", lang))

    seen: dict[str, Candidate] = {}
    for url, lang in urls:
        try:
            body = client.get(
                url, accept="text/html,application/xhtml+xml", timeout=40
            )
            items = parse_trending(body or "", lang)
            for item in items:
                if item.full_name.lower() not in seen:
                    seen[item.full_name.lower()] = item
            log(f"trending{'/' + lang if lang else ''}: {len(items)} repos")
        except Exception as exc:  # noqa: BLE001 - one flaky page must not kill the run
            log(f"trending{'/' + lang if lang else ''} failed: {exc}")
        time.sleep(0.4)
    return list(seen.values())


def fetch_search(cfg: dict, gh: GitHub, target: date) -> list[Candidate]:
    conf = cfg["sources"]["search"]
    if not conf.get("enabled", True):
        return []
    min_stars = int(conf.get("min_stars", 100))
    values = {
        "since_14d": (target - timedelta(days=14)).isoformat(),
        "since_30d": (target - timedelta(days=30)).isoformat(),
        "since_180d": (target - timedelta(days=180)).isoformat(),
        "min_stars": min_stars,
        "min_stars_5x": min_stars * 5,
    }
    out: list[Candidate] = []
    for template in conf.get("queries", []):
        query = template.format(**values)
        try:
            items = gh.search_repos(query, per_page=int(conf.get("per_page", 25)))
            log(f"search `{query}`: {len(items)} repos")
        except Exception as exc:  # noqa: BLE001
            log(f"search `{query}` failed: {exc}")
            continue
        for item in items:
            full_name = item.get("full_name", "")
            if not full_name:
                continue
            out.append(
                Candidate(
                    full_name=full_name,
                    description=truncate(strip_tags(item.get("description") or ""), 400),
                    language=item.get("language") or "",
                    stars=int(item.get("stargazers_count") or 0),
                    forks=int(item.get("forks_count") or 0),
                    topics=list(item.get("topics") or []),
                    created_at=item.get("created_at") or "",
                    pushed_at=item.get("pushed_at") or "",
                    archived=bool(item.get("archived")),
                    fork=bool(item.get("fork")),
                    sources=["search"],
                )
            )
    return out


def fetch_hn(cfg: dict) -> list[Candidate]:
    conf = cfg["sources"]["hn"]
    if not conf.get("enabled", True):
        return []
    since = int(time.time()) - int(conf.get("lookback_days", 7)) * 86400
    min_points = int(conf.get("min_points", 60))
    url = (
        "https://hn.algolia.com/api/v1/search"
        f"?tags=story&numericFilters=points%3E{min_points},created_at_i%3E{since}"
        "&hitsPerPage=100"
    )
    try:
        body = HttpClient().get(url, timeout=30)
        hits = json.loads(body or "{}").get("hits", [])
    except Exception as exc:  # noqa: BLE001
        log(f"hacker news failed: {exc}")
        return []

    out: list[Candidate] = []
    seen: set[str] = set()
    for hit in hits:
        link = (hit.get("url") or "").strip()
        match = re.match(r"https?://(?:www\.)?github\.com/([^/?#]+)/([^/?#]+)", link)
        if not match:
            continue
        owner, repo = match.group(1), match.group(2)
        if owner.lower() in RESERVED_OWNERS or repo.endswith(".git"):
            continue
        full_name = f"{owner}/{repo}"
        if full_name.lower() in seen:
            continue
        seen.add(full_name.lower())
        out.append(
            Candidate(
                full_name=full_name,
                description=truncate(hit.get("title") or "", 300),
                hn_points=int(hit.get("points") or 0),
                sources=["hn"],
            )
        )
    log(f"hacker news: {len(out)} github repos")
    return out


def merge(candidates: list[Candidate]) -> list[Candidate]:
    merged: dict[str, Candidate] = {}
    for item in candidates:
        key = item.full_name.lower()
        current = merged.get(key)
        if current is None:
            merged[key] = item
            continue
        current.stars = max(current.stars, item.stars)
        current.forks = max(current.forks, item.forks)
        current.stars_today = max(current.stars_today, item.stars_today)
        current.hn_points = max(current.hn_points, item.hn_points)
        if len(item.description) > len(current.description):
            current.description = item.description
        current.description = current.description or item.description
        current.language = current.language or item.language
        current.created_at = current.created_at or item.created_at
        current.pushed_at = current.pushed_at or item.pushed_at
        current.archived = current.archived or item.archived
        current.fork = current.fork or item.fork
        for topic in item.topics:
            if topic and topic not in current.topics:
                current.topics.append(topic)
        for source in item.sources:
            if source not in current.sources:
                current.sources.append(source)
    return list(merged.values())


def prelim_score(item: Candidate) -> float:
    score = min(math.log10(max(item.stars, 1)) * 10, 45)
    score += min(item.stars_today / 50, 20)
    score += min(item.hn_points / 20, 10)
    if item.stars == 0:
        score += 10  # unknown yet, give HN-only entries a chance to be resolved
    return score


def _cache_path(full_name: str):
    return CACHE_DIR / (full_name.lower().replace("/", "__") + ".json")


def fetch_repo_meta(gh: GitHub, full_name: str) -> dict | None:
    path = _cache_path(full_name)
    try:
        if path.exists() and time.time() - path.stat().st_mtime < 86400:
            return json.loads(path.read_text(encoding="utf-8"))
    except Exception:  # noqa: BLE001
        pass
    try:
        meta = gh.repo(full_name)
    except Exception as exc:  # noqa: BLE001
        log(f"repo meta {full_name} failed: {exc}")
        return None
    if meta:
        try:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps(meta, ensure_ascii=False), encoding="utf-8")
        except Exception:  # noqa: BLE001
            pass
    return meta


def apply_meta(item: Candidate, meta: dict) -> None:
    item.description = truncate(strip_tags(meta.get("description") or item.description), 400)
    item.language = meta.get("language") or item.language
    item.stars = int(meta.get("stargazers_count") or item.stars)
    item.forks = int(meta.get("forks_count") or item.forks)
    item.topics = list(meta.get("topics") or item.topics)
    item.created_at = meta.get("created_at") or item.created_at
    item.pushed_at = meta.get("pushed_at") or item.pushed_at
    item.archived = bool(meta.get("archived"))
    item.fork = bool(meta.get("fork"))


def fetch_readme(full_name: str, limit: int = 12000) -> str:
    client = HttpClient()
    for name in ("README.md", "readme.md", "README.rst"):
        url = f"https://raw.githubusercontent.com/{full_name}/HEAD/{name}"
        try:
            body = client.get(
                url,
                timeout=20,
                retries=0,
                accept="text/plain, text/markdown, */*",
                allow_404=True,
            )
            if body:
                return truncate(clean_markdown(body), limit)
        except Exception:  # noqa: BLE001
            continue
    return ""


def enrich(
    gh: GitHub, candidates: list[Candidate], limit: int, readme_chars: int
) -> list[Candidate]:
    """Fill in created_at/topics and README excerpts for the most promising repos."""
    shortlist = sorted(candidates, key=prelim_score, reverse=True)[:limit]
    meta_needed = [c for c in shortlist if not c.created_at or c.stars == 0]
    if meta_needed:
        log(f"enriching metadata for {len(meta_needed)} repos")
        for item in meta_needed:
            meta = fetch_repo_meta(gh, item.full_name)
            if meta:
                apply_meta(item, meta)

    log(f"fetching README excerpts for {len(shortlist)} repos")
    with ThreadPoolExecutor(max_workers=5) as pool:
        readmes = list(pool.map(lambda c: fetch_readme(c.full_name), shortlist))
    for item, readme in zip(shortlist, readmes):
        item.readme = truncate(readme, readme_chars)
    return shortlist


def resolve_unknown(gh: GitHub, candidates: list[Candidate]) -> list[Candidate]:
    """Repos that only reached us through Hacker News have no star count yet."""
    pending = [c for c in candidates if c.stars == 0 and c.hn_points > 0]
    if not pending:
        return candidates
    log(f"resolving {len(pending)} repos surfaced only by Hacker News")
    for item in pending[:8]:
        meta = fetch_repo_meta(gh, item.full_name)
        if meta:
            apply_meta(item, meta)
    return candidates


def collect(cfg: dict, gh: GitHub, target: date) -> list[Candidate]:
    raw: list[Candidate] = []
    raw += fetch_trending(cfg)
    raw += fetch_search(cfg, gh, target)
    raw += fetch_hn(cfg)
    candidates = merge(raw)
    log(f"candidate pool: {len(candidates)} unique repos")
    return candidates
