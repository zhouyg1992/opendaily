# SPDX-License-Identifier: MIT
"""Render daily Markdown files and README blocks for every configured locale."""
from __future__ import annotations

import calendar
import json
from datetime import date
from pathlib import Path

from util import (
    CONTENT_DIR,
    DATA_DIR,
    ROOT,
    read_json,
    weekday_cn,
    write_text,
)

START_MARK = "<!-- DIGEST:START -->"
END_MARK = "<!-- DIGEST:END -->"
I18N_DIR = ROOT / "i18n"


def locales(cfg: dict) -> list[str]:
    return list(cfg.get("locales") or ["zh"])


def default_locale(cfg: dict) -> str:
    return str(cfg.get("default_locale") or locales(cfg)[0])


def readme_name(locale: str) -> str:
    return "README.md" if locale == "zh" else f"README.{locale}.md"


def load_i18n(locale: str) -> dict:
    return read_json(I18N_DIR / f"{locale}.json", {})


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


def _one_line(value: str) -> str:
    return " ".join(str(value or "").split())


def _weekday(day: date, i18n: dict) -> str:
    weekdays = i18n.get("weekdays") or []
    if 0 <= day.weekday() < len(weekdays):
        return weekdays[day.weekday()]
    return weekday_cn(day)


def _date_short(day: date, locale: str, i18n: dict) -> str:
    weekday = _weekday(day, i18n)
    if locale.startswith("zh"):
        return f"{day.year}.{day.month:02d}.{day.day:02d} · {weekday}"
    return f"{calendar.month_abbr[day.month]} {day.day}, {day.year} · {weekday}"


def _date_daily(day: date, locale: str, i18n: dict) -> str:
    if locale.startswith("zh"):
        return f"{day.isoformat()} {_weekday(day, i18n)}"
    return _date_short(day, locale, i18n)


def _category_label(category: str, i18n: dict) -> str:
    return (i18n.get("categories") or {}).get(category, category)


def _localized_intro(digest: dict, cfg: dict, locale: str) -> str:
    raw = digest.get("intro")
    if isinstance(raw, dict):
        return _one_line(raw.get(locale) or "")
    if isinstance(raw, str) and locale == default_locale(cfg):
        return _one_line(raw)
    return ""


def _localized_entry(entry: dict, cfg: dict, locale: str) -> tuple[str, str]:
    content = entry.get("content")
    default = default_locale(cfg)
    if isinstance(content, dict):
        block = content.get(locale) or content.get(default) or {}
        summary = _one_line(block.get("summary"))
        insight = _one_line(block.get("insight"))
        if summary:
            return summary, insight
    if locale == default:
        return _one_line(entry.get("summary")), _one_line(entry.get("insight"))
    return "", ""


def _digest_body(digest: dict, cfg: dict, locale: str) -> list[str]:
    i18n = load_i18n(locale)
    lines: list[str] = []

    intro = _localized_intro(digest, cfg, locale)
    if intro:
        lines.append(f"> {intro}")
        lines.append("")

    for category, entries in grouped_items(digest, cfg):
        lines.append(f"### {_category_label(_one_line(category), i18n)}")
        lines.append("")
        for entry in entries:
            summary, insight = _localized_entry(entry, cfg, locale)
            if not summary:
                continue
            lines.append(f"* **[{entry['repo']}]({entry['url']})** — {summary}")
            if insight:
                lines.append("")
                lines.append(
                    f"  > {i18n.get('insight', 'Insight')}"
                    f"{i18n.get('insight_sep', ': ')}{insight}"
                )
            lines.append("")
    return lines


def render_markdown(digest: dict, cfg: dict, locale: str) -> str:
    day = date.fromisoformat(digest["date"])
    i18n = load_i18n(locale)
    lines = [
        f"# {i18n.get('digest_title', 'OpenDaily')} · {_date_daily(day, locale, i18n)}",
        "",
    ]
    lines += _digest_body(digest, cfg, locale)
    lines += [
        "---",
        "",
        f"[← {i18n.get('back_home', 'Back')}](../../{readme_name(locale)})"
        f" · [{i18n.get('all_issues', 'All issues')}](../)",
        "",
        i18n.get("generated_by", ""),
        "",
    ]
    return "\n".join(lines)


def write_content(digest: dict, cfg: dict, locale: str) -> None:
    write_text(
        CONTENT_DIR / locale / f"{digest['date']}.md",
        render_markdown(digest, cfg, locale),
    )


def build_readme_block(digests: list[dict], cfg: dict, locale: str) -> str:
    i18n = load_i18n(locale)
    if not digests:
        return f"{i18n.get('empty', 'No issues yet.')}\n"

    latest = digests[0]
    day = date.fromisoformat(latest["date"])
    md_path = f"daily/{locale}/{latest['date']}.md"
    lines = [f"## [{_date_short(day, locale, i18n)}]({md_path})", ""]
    lines += _digest_body(latest, cfg, locale)
    lines += [
        f"[{i18n.get('this_markdown', 'Markdown')}]({md_path})",
        "",
        f"### {i18n.get('archive', 'Archive')}",
        "",
    ]

    years: dict[int, dict[int, list[date]]] = {}
    for digest in digests:
        item_day = date.fromisoformat(digest["date"])
        years.setdefault(item_day.year, {}).setdefault(item_day.month, []).append(item_day)
    for year, months in years.items():
        year_label = f"{year} 年" if locale.startswith("zh") else str(year)
        lines.append(f"#### {year_label}")
        lines.append("")
        for month, days in months.items():
            links = " · ".join(
                f"[{item.day}](daily/{locale}/{item.isoformat()}.md)" for item in days
            )
            month_label = (
                f"{month} 月"
                if locale.startswith("zh")
                else calendar.month_abbr[month]
            )
            lines.append(f"**{month_label}**：{links}")
            lines.append("")
    return "\n".join(lines)


def update_readme(digests: list[dict], cfg: dict, locale: str) -> None:
    block = f"{START_MARK}\n{build_readme_block(digests, cfg, locale)}\n{END_MARK}"
    readme = ROOT / readme_name(locale)
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
