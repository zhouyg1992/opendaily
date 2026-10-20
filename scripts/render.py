# SPDX-License-Identifier: MIT
"""Render one Markdown file per day and keep the README index in sync."""
from __future__ import annotations

import json
import math
from datetime import date
from pathlib import Path

from util import (
    CONTENT_DIR,
    DATA_DIR,
    ROOT,
    fmt_count,
    read_json,
    weekday_cn,
    write_text,
)

START_MARK = "<!-- DIGEST:START -->"
END_MARK = "<!-- DIGEST:END -->"


def load_digests() -> list[dict]:
    folder = DATA_DIR / "digests"
    if not folder.exists():
        return []
    digests = []
    for path in sorted(folder.glob("*.json")):
        data = read_json(path, None)
        if data and data.get("date"):
            digests.append(data)
    digests.sort(key=lambda item: item["date"], reverse=True)
    return digests


def save_digest(digest: dict) -> Path:
    path = DATA_DIR / "digests" / f"{digest['date']}.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(digest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return path


def grouped_items(digest: dict, cfg: dict) -> list[tuple[str, list[dict]]]:
    order = {name: i for i, name in enumerate(cfg.get("categories", []))}
    buckets: dict[str, list[dict]] = {}
    for item in digest.get("items", []):
        buckets.setdefault(item.get("category") or "其他", []).append(item)
    return sorted(buckets.items(), key=lambda pair: order.get(pair[0], 99))


def digest_stats(digest: dict, cfg: dict) -> dict:
    groups = grouped_items(digest, cfg)
    chars = len(digest.get("intro", "")) + sum(
        len(item.get("summary", "")) for item in digest.get("items", [])
    )
    return {
        "count": len(digest.get("items", [])),
        "categories": len(groups),
        "stars_today": sum(
            int(item.get("stars_today") or 0) for item in digest.get("items", [])
        ),
        "minutes": max(3, math.ceil(chars / 450)),
    }


def render_markdown(digest: dict, cfg: dict) -> str:
    d = date.fromisoformat(digest["date"])
    stats = digest_stats(digest, cfg)
    meta_bits = [f"{stats['count']} 个项目", f"{stats['categories']} 个方向"]
    if stats["stars_today"]:
        meta_bits.append(f"当日新增 {fmt_count(stats['stars_today'])} stars")

    lines = [
        f"# 开源日报 · {d.isoformat()} {weekday_cn(d)}",
        "",
        f"> {digest.get('intro', '')}",
        "",
        " · ".join(meta_bits),
        "",
    ]
    for category, entries in grouped_items(digest, cfg):
        lines.append(f"## {category}")
        lines.append("")
        for entry in entries:
            lines.append(
                f"- **[{entry['repo']}]({entry['url']})** — {entry.get('summary', '')}"
            )
            meta = []
            if entry.get("language"):
                meta.append(f"`{entry['language']}`")
            if entry.get("stars"):
                meta.append(f"★ {fmt_count(int(entry['stars']))}")
            if entry.get("stars_today"):
                meta.append(f"当日 +{fmt_count(int(entry['stars_today']))}")
            if meta:
                lines.append("  " + " · ".join(meta))
            if entry.get("insight"):
                lines.append(f"  > 灵感：{entry['insight']}")
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("[← 返回首页](../README.md) · [全部日报](../daily/)")
    lines.append("")
    lines.append("由 GitHub Actions 自动生成。")
    lines.append("")
    return "\n".join(lines)


def write_content(digest: dict, cfg: dict) -> None:
    write_text(CONTENT_DIR / f"{digest['date']}.md", render_markdown(digest, cfg))


def build_readme_block(digests: list[dict], cfg: dict) -> str:
    if not digests:
        return "还没有生成任何一期。\n"

    latest = digests[0]
    d = date.fromisoformat(latest["date"])
    md_path = f"daily/{latest['date']}.md"
    items = latest.get("items", [])
    lines = [
        f"**[{d.strftime('%Y.%m.%d')} · {weekday_cn(d)}]({md_path})** — {latest.get('intro', '')}",
        "",
    ]
    for index, entry in enumerate(items, 1):
        insight = entry.get("insight") or entry.get("summary", "")
        lines.append(f"{index}. **[{entry['repo']}]({entry['url']})** — {insight}")
        lines.append("")
    lines.append(f"[阅读完整日报（含项目介绍和 {len(items)} 条灵感）→]({md_path})")
    lines.append("")
    return "\n".join(lines)


def update_readme(digests: list[dict], cfg: dict) -> None:
    block = f"{START_MARK}\n{build_readme_block(digests, cfg)}\n{END_MARK}"
    readme = ROOT / "README.md"
    if not readme.exists():
        readme.write_text(block + "\n", encoding="utf-8")
        return

    text = readme.read_text(encoding="utf-8")
    if START_MARK in text and END_MARK in text:
        start = text.index(START_MARK)
        end = text.index(END_MARK) + len(END_MARK)
        text = text[:start] + block + text[end:]
    else:
        text = text.rstrip() + "\n\n" + block + "\n"
    readme.write_text(text, encoding="utf-8")
