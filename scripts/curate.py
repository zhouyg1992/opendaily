# SPDX-License-Identifier: MIT
"""Filter, score and curate the daily ten."""
from __future__ import annotations

import json
import math
import os
import re
from collections import Counter
from datetime import date, datetime

from sources import Candidate
from util import DATA_DIR, HttpError, log, post_json, read_json, truncate

AI_TOPICS = {
    "ai",
    "agents",
    "ai-agents",
    "agent",
    "llm",
    "llms",
    "mcp",
    "rag",
    "gpt",
    "claude",
    "chatbot",
    "generative-ai",
}

CATEGORY_RULES = [
    (
        "AI / Agent 工具",
        r"\b(agent|agents|llm|gpt|claude|chatbot|copilot|mcp|rag|prompt|assistant|ai)\b",
    ),
    (
        "AI 基础设施 / 模型",
        r"\b(inference|model|training|fine-?tun|diffusion|embedding|vector|transformer|cuda|gpu|quantiz|serving|llama|qwen)\b",
    ),
    (
        "开发工具 / CLI",
        r"\b(cli|terminal|editor|ide|compiler|parser|debug|sdk|framework|git|vim|neovim|devtool|toolchain)\b",
    ),
    (
        "前端 / 设计",
        r"\b(frontend|react|vue|svelte|css|design|ui|component|tailwind|animation|browser|figma|canvas)\b",
    ),
    (
        "数据 / 基础设施",
        r"\b(database|sql|storage|postgres|sqlite|redis|kafka|docker|kubernetes|k8s|deploy|infra|terraform|serverless|monitoring|etl|analytics|query)\b",
    ),
    (
        "安全 / 隐私",
        r"\b(security|auth|encrypt|privacy|vulnerab|malware|firewall|secret|sandbox)\b",
    ),
    (
        "Skill / 垂直工具",
        r"\b(skill|skills|plugin|plugins|extension|addon|pcb|eda|midi|thermal|3d|game|audio|video|image|download|downloader)\b|网盘|下载",
    ),
]


def age_days(created_at: str, target: date) -> int | None:
    if not created_at:
        return None
    try:
        return (target - date.fromisoformat(created_at[:10])).days
    except ValueError:
        return None


def compile_patterns(cfg: dict) -> list[re.Pattern]:
    patterns = cfg.get("filters", {}).get("exclude_patterns", [])
    return [re.compile(p, re.I) for p in patterns]


def categorize(item: Candidate) -> str:
    haystack = " ".join(
        [item.description or "", item.full_name, " ".join(item.topics)]
    ).lower()
    for category, pattern in CATEGORY_RULES:
        if re.search(pattern, haystack):
            return category
    return "学习资源 / 其他"


def keyword_boost(item: Candidate) -> float:
    topics = {t.lower() for t in item.topics}
    return 2.0 if topics & AI_TOPICS else 0.0


def score(item: Candidate, target: date) -> float:
    value = min(math.log10(max(item.stars, 1)) * 6, 30)
    value += min(item.stars_today / 40, 15)
    value += min(item.hn_points / 30, 5)
    age = age_days(item.created_at, target)
    if age is not None:
        if age <= 7:
            value += 8
        elif age <= 30:
            value += 6
        elif age <= 90:
            value += 3
        elif age <= 365:
            value += 1
    value += keyword_boost(item)
    return round(value, 2)


def filter_candidates(
    cfg: dict,
    candidates: list[Candidate],
    target: date,
    blocked: set[str],
) -> list[Candidate]:
    min_stars = int(cfg["digest"].get("min_stars", 200))
    max_idle = int(cfg["filters"].get("max_idle_days", 365))
    patterns = compile_patterns(cfg)
    reasons: Counter = Counter()
    kept: list[Candidate] = []

    for item in candidates:
        name = item.full_name.lower()
        if name in blocked:
            reasons["已推荐过"] += 1
            continue
        if item.archived or item.fork:
            reasons["归档/fork"] += 1
            continue
        if item.stars < min_stars and item.stars_today < max(100, min_stars // 2):
            reasons["star 太少"] += 1
            continue
        if len(item.description) < 10:
            reasons["没有简介"] += 1
            continue
        haystack = f"{item.full_name} {item.description}".lower()
        if any(p.search(haystack) for p in patterns):
            reasons["清单/教程类"] += 1
            continue
        if item.pushed_at and item.stars_today == 0:
            try:
                idle = (target - date.fromisoformat(item.pushed_at[:10])).days
                if idle > max_idle:
                    reasons["长期未更新"] += 1
                    continue
            except ValueError:
                pass
        kept.append(item)

    if reasons:
        detail = "，".join(f"{k} {v}" for k, v in reasons.most_common())
        log(f"filtered out {sum(reasons.values())} repos ({detail})")
    return kept


def pick_fallback(
    ranked: list[Candidate], cfg: dict
) -> list[tuple[Candidate, str, str, str]]:
    count = int(cfg["digest"].get("count", 10))
    owner_cap = int(cfg["digest"].get("max_per_owner", 2))
    cat_cap = int(cfg["digest"].get("max_per_category", 3))
    picked: list[tuple[Candidate, str, str, str]] = []
    chosen: set[str] = set()

    for cap in (cat_cap, cat_cap + 1, 99):
        owner_counts: Counter = Counter()
        cat_counts: Counter = Counter()
        for item in picked:
            owner_counts[item[0].owner.lower()] += 1
            cat_counts[item[1]] += 1
        for item in ranked:
            if len(picked) >= count:
                break
            if item.full_name.lower() in chosen:
                continue
            if owner_counts[item.owner.lower()] >= owner_cap:
                continue
            cat = categorize(item)
            if cat_counts[cat] >= cap:
                continue
            picked.append((item, cat, truncate(item.description, 150), ""))
            chosen.add(item.full_name.lower())
            owner_counts[item.owner.lower()] += 1
            cat_counts[cat] += 1
    return picked[:count]


def _candidate_block(candidates: list[Candidate], target: date) -> str:
    blocks = []
    for index, item in enumerate(candidates, 1):
        age = age_days(item.created_at, target)
        age_text = f"{age} 天前创建" if age is not None else "创建时间未知"
        stats = [f"★{item.stars:,}"]
        if item.stars_today:
            stats.append(f"今日 +{item.stars_today:,}")
        if item.hn_points:
            stats.append(f"HN {item.hn_points} 分")
        head = " | ".join(
            [
                f"[{index}] {item.full_name}",
                "，".join(stats),
                item.language or "语言未知",
                age_text,
            ]
        )
        lines = [head, f"简介：{item.description or '（无）'}"]
        if item.topics:
            lines.append("Topics：" + ", ".join(item.topics[:10]))
        if item.readme:
            lines.append("README 摘录：" + truncate(item.readme, 700))
        blocks.append("\n".join(lines))
    return "\n\n".join(blocks)


SYSTEM_PROMPT = (
    "你是一位懂工程、也懂产品的开源项目侦察员，为正在找方向的创业者和关注开源社区的人写每日日报。"
    "你能分辨真实需求和自嗨工具，也敢指出一个项目适合怎么被产品化。你只输出 JSON。"
)


def build_prompt(cfg: dict, candidates: list[Candidate], target: date) -> str:
    count = int(cfg["digest"].get("count", 10))
    categories = "、".join(cfg.get("categories", []))
    return f"""下面是从 GitHub Trending、新项目搜索和 Hacker News 收集到的 {len(candidates)} 个候选项目。

读者是想创业但还没找到方向的人，以及每天关注开源社区的人。他们想知道：今天有什么值得看，以及这些项目里藏着什么机会。

请从中挑选 {count} 个最值得今天推荐的项目，并写成日报。

要求：
1. 恰好 {count} 个不同项目，repo 必须与候选列表中的 owner/name 完全一致，不得编造。
2. 优先覆盖不同方向，避免同质化（例如不要选 5 个 agent 框架）；同一 owner 最多 2 个。
3. intro：60–90 字，指出今天这批项目共同反映的一个变化、需求或机会信号，不要逐个点名，也不要写成空泛的行业套话。
4. summary：50–80 字中文，讲清「它是什么、解决谁的问题、为什么现在值得看」。
   - 具体、可验证，不要空泛吹捧（如「功能强大」「值得关注」）；
   - 不要以「这是一个」开头，不要复述 star 数，不要用 Markdown、不要 emoji；
   - 不要照抄英文简介的句式。
5. insight：30–60 字，给一个具体的「可以怎么借」的角度：面向谁、切哪个场景、和现有方案差在哪。
   - 如果它更适合作为基础设施或趋势信号，就直接说明，不要硬编创业点子；
   - 不要写「可以做 SaaS」「前景广阔」「值得关注」这类空话，不要编造市场数据；
   - 不要重复 summary 的内容。
6. category 只能从以下选一个：{categories}。
7. 严格输出 JSON：
{{"intro": "...", "items": [{{"repo": "owner/name", "category": "...", "summary": "...", "insight": "..."}}]}}
不要输出 JSON 以外的任何内容。

候选项目：
{_candidate_block(candidates, target)}
"""


def _extract_json(text: str) -> dict:
    cleaned = text.strip()
    cleaned = re.sub(r"^```(?:json)?\s*", "", cleaned)
    cleaned = re.sub(r"\s*```$", "", cleaned)
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        start, end = cleaned.find("{"), cleaned.rfind("}")
        if start >= 0 and end > start:
            return json.loads(cleaned[start : end + 1])
        raise


def call_llm(cfg: dict, prompt: str) -> dict | None:
    api_key = os.environ.get("LLM_API_KEY")
    if not api_key:
        return None
    conf = cfg.get("llm", {})
    base = (os.environ.get("LLM_BASE_URL") or conf.get("base_url") or "").rstrip("/")
    if not base:
        return None
    model = os.environ.get("LLM_MODEL") or conf.get("model") or "deepseek-chat"
    url = base + "/chat/completions"
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
        "temperature": float(conf.get("temperature", 0.6)),
        "max_tokens": int(conf.get("max_tokens", 3200)),
        "response_format": {"type": "json_object"},
    }
    timeout = int(conf.get("timeout", 180))
    log(f"asking {model} to curate...")
    try:
        raw = post_json(url, payload, api_key=api_key, timeout=timeout)
    except HttpError as exc:
        log(f"LLM request failed ({exc}); retrying once without JSON mode")
        payload.pop("response_format", None)
        try:
            raw = post_json(url, payload, api_key=api_key, timeout=timeout)
        except HttpError as exc2:
            log(f"LLM request failed again: {exc2}")
            return None
    try:
        response = json.loads(raw)
        content = response["choices"][0]["message"]["content"]
        data = _extract_json(content)
        data["_model"] = response.get("model") or model
        return data
    except (KeyError, IndexError, json.JSONDecodeError, TypeError) as exc:
        log(f"could not parse LLM output: {exc}")
        return None


def normalize_llm(
    cfg: dict, data: dict, ranked: list[Candidate]
) -> tuple[str, list[tuple[Candidate, str, str, str]], str]:
    count = int(cfg["digest"].get("count", 10))
    owner_cap = int(cfg["digest"].get("max_per_owner", 2))
    cat_cap = int(cfg["digest"].get("max_per_category", 4))
    allowed = list(cfg.get("categories", []))
    by_name = {c.full_name.lower(): c for c in ranked}
    owner_counts: Counter = Counter()
    cat_counts: Counter = Counter()
    picked: list[tuple[Candidate, str, str, str]] = []
    deferred: list[tuple[Candidate, str, str, str]] = []
    chosen: set[str] = set()

    for entry in data.get("items", []):
        if not isinstance(entry, dict):
            continue
        repo = str(entry.get("repo", "")).strip()
        repo = re.sub(r"^https?://(?:www\.)?github\.com/", "", repo).strip("/")
        item = by_name.get(repo.lower())
        if not item or item.full_name.lower() in chosen:
            continue
        if owner_counts[item.owner.lower()] >= owner_cap:
            continue
        category = str(entry.get("category", "")).strip()
        if category not in allowed:
            category = categorize(item)
        summary = str(entry.get("summary", "")).strip()
        summary = re.sub(r"^[-–—\s]+", "", summary).strip('"“”')
        summary = re.sub(r"^[^\s：:]{1,60}[/／][^\s：:]{1,80}\s*[：:—-]\s*", "", summary)
        summary = re.sub(r"\s+", " ", summary)
        if len(summary) < 12:
            summary = truncate(item.description, 150)
        summary = truncate(summary, 180)
        insight = str(entry.get("insight", "")).strip()
        insight = re.sub(r"^[-–—\s]+", "", insight).strip('"“”')
        insight = re.sub(r"\s+", " ", insight)
        insight = truncate(insight, 160)
        if len(insight) < 10:
            insight = ""
        if cat_counts[category] >= cat_cap:
            deferred.append((item, category, summary, insight))
            continue
        picked.append((item, category, summary, insight))
        chosen.add(item.full_name.lower())
        owner_counts[item.owner.lower()] += 1
        cat_counts[category] += 1
        if len(picked) >= count:
            break

    # The LLM may over-index on one category; keep the best extras around
    # instead of silently dropping them when the pool is otherwise thin.
    for item, category, summary, insight in deferred:
        if len(picked) >= count:
            break
        if item.full_name.lower() in chosen:
            continue
        if owner_counts[item.owner.lower()] >= owner_cap:
            continue
        picked.append((item, category, summary, insight))
        chosen.add(item.full_name.lower())
        owner_counts[item.owner.lower()] += 1
        cat_counts[category] += 1

    if len(picked) < count:
        for item in ranked:
            if len(picked) >= count:
                break
            if item.full_name.lower() in chosen:
                continue
            if owner_counts[item.owner.lower()] >= owner_cap:
                continue
            category = categorize(item)
            if cat_counts[category] >= cat_cap:
                continue
            picked.append((item, category, truncate(item.description, 150), ""))
            chosen.add(item.full_name.lower())
            owner_counts[item.owner.lower()] += 1
            cat_counts[category] += 1

    intro = re.sub(r"\s+", " ", str(data.get("intro", ""))).strip()
    if len(intro) < 10:
        intro = ""
    return intro, picked[:count], str(data.get("_model") or "")


def apply_overrides(cfg: dict, digest: dict, target: date) -> dict:
    """Allow a human editor to correct categories, summaries or insights for one day."""
    path = DATA_DIR / "overrides" / f"{target.isoformat()}.json"
    data = read_json(path, None)
    if not data:
        return digest
    by_repo = {item["repo"].lower(): item for item in digest.get("items", [])}
    for repo, patch in (data.get("items") or {}).items():
        item = by_repo.get(repo.lower())
        if not item or not isinstance(patch, dict):
            continue
        for key in ("summary", "insight", "category"):
            value = str(patch.get(key) or "").strip()
            if not value:
                continue
            if key == "category":
                item[key] = value
            else:
                item[key] = truncate(value, 180 if key == "summary" else 160)
    order = {name: i for i, name in enumerate(cfg.get("categories", []))}
    digest["items"].sort(key=lambda item: order.get(item.get("category"), 99))
    intro = str(data.get("intro") or "").strip()
    if intro:
        digest["intro"] = intro
    if data.get("generated_by"):
        digest["generated_by"] = str(data["generated_by"])
    log(f"applied editorial overrides from {path.relative_to(DATA_DIR.parent)}")
    return digest


def build_digest(
    cfg: dict,
    picks: list[tuple[Candidate, str, str, str]],
    intro: str,
    target: date,
    generated_by: str,
    model: str,
) -> dict:
    order = {name: i for i, name in enumerate(cfg.get("categories", []))}
    picks = sorted(picks, key=lambda p: order.get(p[1], 99))
    items = []
    for item, category, summary, insight in picks:
        items.append(
            {
                "repo": item.full_name,
                "url": item.url,
                "summary": summary,
                "insight": insight,
                "description": item.description,
                "category": category,
                "language": item.language,
                "stars": item.stars,
                "stars_today": item.stars_today,
                "topics": item.topics[:10],
                "sources": item.sources,
                "score": item.score,
            }
        )
    if not intro:
        intro = "今天从候选池里挑了十个项目：有已经在解决真实需求的工具，也有值得早点关注的信号。"
    return {
        "date": target.isoformat(),
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "intro": intro,
        "generated_by": generated_by,
        "model": model,
        "items": items,
    }


def shortlist_for_llm(
    candidates: list[Candidate], cfg: dict, target: date
) -> list[Candidate]:
    """Pick a category-diverse shortlist instead of just the top star counts."""
    limit = int(cfg.get("llm", {}).get("max_candidates", 24))
    per_category = int(cfg.get("llm", {}).get("shortlist_per_category", 4))
    order = {name: i for i, name in enumerate(cfg.get("categories", []))}
    buckets: dict[str, list[Candidate]] = {}
    for item in candidates:
        item.score = score(item, target)
        buckets.setdefault(categorize(item), []).append(item)
    for bucket in buckets.values():
        bucket.sort(key=lambda c: c.score, reverse=True)

    picked: list[Candidate] = []
    chosen: set[str] = set()
    cat_counts: Counter = Counter()
    for cap in (per_category, per_category + 2, limit):
        while len(picked) < limit:
            progressed = False
            for category in sorted(buckets, key=lambda c: order.get(c, 99)):
                if len(picked) >= limit:
                    break
                if cat_counts[category] >= cap:
                    continue
                bucket = buckets[category]
                while bucket and bucket[0].full_name.lower() in chosen:
                    bucket.pop(0)
                if not bucket:
                    continue
                item = bucket.pop(0)
                picked.append(item)
                chosen.add(item.full_name.lower())
                cat_counts[category] += 1
                progressed = True
            if not progressed:
                break
        if len(picked) >= limit:
            break
    return picked


def curate(cfg: dict, candidates: list[Candidate], target: date) -> dict:
    candidates = [c for c in candidates if c.stars > 0 and not c.archived and not c.fork]
    if not candidates:
        raise RuntimeError("no usable candidates left after filtering")

    for item in candidates:
        item.score = score(item, target)
    ranked = sorted(candidates, key=lambda c: c.score, reverse=True)
    log(
        "top candidates: "
        + ", ".join(f"{c.full_name}({c.score:.0f})" for c in ranked[:5])
    )

    max_candidates = int(cfg.get("llm", {}).get("max_candidates", 24))
    pool = ranked[:max_candidates]
    prompt = build_prompt(cfg, pool, target)
    data = call_llm(cfg, prompt)
    if data:
        intro, picks, model = normalize_llm(cfg, data, ranked)
        if len(picks) >= min(8, int(cfg["digest"].get("count", 10))):
            log(f"LLM picked {len(picks)} repos")
            return build_digest(cfg, picks, intro, target, "llm", model)
        log(f"LLM output only yielded {len(picks)} valid repos, falling back")

    picks = pick_fallback(ranked, cfg)
    log(f"heuristic picked {len(picks)} repos")
    return build_digest(
        cfg,
        picks,
        "",
        target,
        "heuristic",
        "",
    )
