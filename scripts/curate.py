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


def _locales(cfg: dict) -> list[str]:
    return list(cfg.get("locales") or ["zh"])


def _default_locale(cfg: dict) -> str:
    return str(cfg.get("default_locale") or _locales(cfg)[0])


def _fallback_content(item: Candidate, cfg: dict) -> dict:
    summary = truncate(item.description, 150)
    return {
        locale: {"summary": summary, "insight": ""}
        for locale in _locales(cfg)
    }


def pick_fallback(
    ranked: list[Candidate], cfg: dict
) -> list[tuple[Candidate, str, dict]]:
    count = int(cfg["digest"].get("count", 10))
    owner_cap = int(cfg["digest"].get("max_per_owner", 2))
    cat_cap = int(cfg["digest"].get("max_per_category", 3))
    picked: list[tuple[Candidate, str, dict]] = []
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
            picked.append((item, cat, _fallback_content(item, cfg)))
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
    "你能分辨真实需求和自嗨工具，也敢指出一个项目适合怎么被产品化。"
    "你需要用中文和英文分别写作，两种语言都要自然，不要逐字翻译。你只输出 JSON。"
)


def build_prompt(cfg: dict, candidates: list[Candidate], target: date) -> str:
    count = int(cfg["digest"].get("count", 10))
    categories = "、".join(cfg.get("categories", []))
    return f"""下面是从 GitHub Trending、新项目搜索和 Hacker News 收集到的 {len(candidates)} 个候选项目。

读者是想创业但还没找到方向的人，以及每天关注开源社区的人。他们想知道：今天有什么值得看，以及这些项目里藏着什么机会。

请从中挑选 {count} 个最值得今天推荐的项目，并写成中英双语日报。

要求：
1. 恰好 {count} 个不同项目，repo 必须与候选列表中的 owner/name 完全一致，不得编造。
2. 优先覆盖不同方向，避免同质化（例如不要选 5 个 agent 框架）；同一 owner 最多 2 个。
3. intro 是对象，必须同时包含 zh 和 en：
   - zh：60–90 字，指出今天这批项目共同反映的一个变化、需求或机会信号，不要逐个点名；
   - en：30–50 words，表达同一个观察，但用英语原生写法，不要逐字翻译中文。
4. content 是对象，每个项目必须同时包含 zh 和 en，各自有 summary 和 insight：
   - summary：讲清「它是什么、解决谁的问题、为什么现在值得看」。中文 50–80 字，英文 25–45 words。
   - insight：一个具体的「可以怎么借」的角度：面向谁、切哪个场景、和现有方案差在哪。中文 30–60 字，英文 15–30 words。
   - 两种语言都要原生写作，英文不要照搬中文句式，也不要保留中文标点。
   - 如果项目更适合作为基础设施或趋势信号，就直接说明，不要硬编创业点子。
   - 不要写「可以做 SaaS」「前景广阔」「值得关注」这类空话，不要编造市场数据。
   - 不要用 Markdown、不要 emoji，不要复述 star 数。
5. category 只能从以下选一个（这是内部分类，不需要翻译）：{categories}。
6. 严格输出 JSON：
{{"intro": {{"zh": "...", "en": "..."}}, "items": [{{"repo": "owner/name", "category": "...", "content": {{"zh": {{"summary": "...", "insight": "..."}}, "en": {{"summary": "...", "insight": "..."}}}}}}]}}
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
        "max_tokens": int(conf.get("max_tokens", 6000)),
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


def _clean_text(value) -> str:
    text = re.sub(r"\s+", " ", str(value or "")).strip().strip('"“”')
    text = re.sub(r"^[-–—\s]+", "", text)
    return text


def _parse_content(entry: dict, cfg: dict) -> dict:
    locales = _locales(cfg)
    default = _default_locale(cfg)
    raw = entry.get("content")
    parsed: dict[str, dict] = {}

    if isinstance(raw, dict):
        for locale in locales:
            block = raw.get(locale)
            if not isinstance(block, dict):
                continue
            summary = _clean_text(block.get("summary"))
            summary = re.sub(
                r"^[^\s：:]{1,60}[/／][^\s：:]{1,80}\s*[：:—-]\s*", "", summary
            )
            if len(summary) < 12:
                continue
            insight = _clean_text(block.get("insight"))
            parsed[locale] = {
                "summary": truncate(summary, 180),
                "insight": truncate(insight, 160) if len(insight) >= 10 else "",
            }

    if not parsed:
        summary = _clean_text(entry.get("summary"))
        insight = _clean_text(entry.get("insight"))
        if len(summary) >= 12:
            parsed[default] = {
                "summary": truncate(summary, 180),
                "insight": truncate(insight, 160) if len(insight) >= 10 else "",
            }

    if not parsed:
        return {}
    if default not in parsed:
        parsed[default] = dict(next(iter(parsed.values())))
    for locale in locales:
        if locale not in parsed:
            parsed[locale] = dict(parsed[default])
    return parsed


def normalize_llm(
    cfg: dict, data: dict, ranked: list[Candidate]
) -> tuple[dict, list[tuple[Candidate, str, dict]], str]:
    count = int(cfg["digest"].get("count", 10))
    owner_cap = int(cfg["digest"].get("max_per_owner", 2))
    cat_cap = int(cfg["digest"].get("max_per_category", 4))
    allowed = list(cfg.get("categories", []))
    by_name = {c.full_name.lower(): c for c in ranked}
    owner_counts: Counter = Counter()
    cat_counts: Counter = Counter()
    picked: list[tuple[Candidate, str, dict]] = []
    deferred: list[tuple[Candidate, str, dict]] = []
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
        content = _parse_content(entry, cfg)
        if not content:
            continue
        if cat_counts[category] >= cat_cap:
            deferred.append((item, category, content))
            continue
        picked.append((item, category, content))
        chosen.add(item.full_name.lower())
        owner_counts[item.owner.lower()] += 1
        cat_counts[category] += 1
        if len(picked) >= count:
            break

    # Keep category overflow around; the pool may be thin in other directions.
    for item, category, content in deferred:
        if len(picked) >= count:
            break
        if item.full_name.lower() in chosen:
            continue
        if owner_counts[item.owner.lower()] >= owner_cap:
            continue
        picked.append((item, category, content))
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
            picked.append((item, category, _fallback_content(item, cfg)))
            chosen.add(item.full_name.lower())
            owner_counts[item.owner.lower()] += 1
            cat_counts[category] += 1

    raw_intro = data.get("intro")
    intro: dict[str, str] = {}
    if isinstance(raw_intro, dict):
        for locale in _locales(cfg):
            text = _clean_text(raw_intro.get(locale))
            if len(text) >= 10:
                intro[locale] = truncate(text, 300)
    elif isinstance(raw_intro, str):
        text = _clean_text(raw_intro)
        if len(text) >= 10:
            intro[_default_locale(cfg)] = truncate(text, 300)

    return intro, picked[:count], str(data.get("_model") or "")


def apply_overrides(cfg: dict, digest: dict, target: date) -> dict:
    """Allow a human editor to correct localized copy for one day."""
    path = DATA_DIR / "overrides" / f"{target.isoformat()}.json"
    data = read_json(path, None)
    if not isinstance(data, dict) or not data:
        return digest

    locales = _locales(cfg)
    default = _default_locale(cfg)
    if any(isinstance(data.get(locale), dict) for locale in locales):
        blocks = {loc: data[loc] for loc in locales if isinstance(data.get(loc), dict)}
    else:
        blocks = {default: data}

    by_repo = {item["repo"].lower(): item for item in digest.get("items", [])}
    for locale, block in blocks.items():
        intro = block.get("intro")
        if intro:
            if not isinstance(digest.get("intro"), dict):
                digest["intro"] = {}
            digest["intro"][locale] = truncate(
                re.sub(r"\s+", " ", str(intro)).strip(), 300
            )
        for repo, patch in (block.get("items") or {}).items():
            item = by_repo.get(repo.lower())
            if not item or not isinstance(patch, dict):
                continue
            category = str(patch.get("category") or "").strip()
            if category:
                item["category"] = category
            content = item.setdefault("content", {})
            localized = content.setdefault(locale, {})
            for key in ("summary", "insight"):
                value = str(patch.get(key) or "").strip()
                if value:
                    localized[key] = truncate(value, 180 if key == "summary" else 160)
            if not content.get(locale):
                content.pop(locale, None)

    order = {name: i for i, name in enumerate(cfg.get("categories", []))}
    digest["items"].sort(key=lambda item: order.get(item.get("category"), 99))
    if data.get("generated_by"):
        digest["generated_by"] = str(data["generated_by"])
    log(f"applied editorial overrides from {path.relative_to(DATA_DIR.parent)}")
    return digest


def build_digest(
    cfg: dict,
    picks: list[tuple[Candidate, str, dict]],
    intro: dict,
    target: date,
    generated_by: str,
    model: str,
) -> dict:
    order = {name: i for i, name in enumerate(cfg.get("categories", []))}
    picks = sorted(picks, key=lambda p: order.get(p[1], 99))
    items = []
    for item, category, content in picks:
        items.append(
            {
                "repo": item.full_name,
                "url": item.url,
                "content": content,
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
        {},
        target,
        "heuristic",
        "",
    )
