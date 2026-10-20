"""OpenDaily entrypoint: collect, curate, render, persist."""
from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import date

from curate import (
    apply_overrides,
    categorize,
    curate,
    filter_candidates,
    shortlist_for_llm,
)
from render import load_digests, save_digest, update_readme, write_content
from sources import collect, enrich, resolve_unknown
from util import (
    DATA_DIR,
    ROOT,
    GitHub,
    get_token,
    log,
    parse_date,
    read_json,
    today_local,
    write_json,
)


def load_config() -> dict:
    with (ROOT / "config.json").open("r", encoding="utf-8") as fh:
        return json.load(fh)


def load_seen() -> dict[str, str]:
    return read_json(DATA_DIR / "seen.json", {})


def blocked_repos(seen: dict[str, str], target: date, cooldown: int) -> set[str]:
    blocked = set()
    for name, value in seen.items():
        try:
            last = parse_date(value)
        except ValueError:
            continue
        gap = abs((target - last).days)
        if gap < cooldown and last != target:
            blocked.add(name.lower())
    return blocked


def update_seen(seen: dict[str, str], digest: dict, cooldown: int) -> None:
    today = digest["date"]
    for item in digest["items"]:
        seen[item["repo"]] = today
    # keep the file small: drop entries not used for a long time
    cutoff = date.fromisoformat(today).toordinal() - max(cooldown * 3, 180)
    pruned = {}
    for name, value in seen.items():
        try:
            if date.fromisoformat(value).toordinal() >= cutoff:
                pruned[name] = value
        except ValueError:
            continue
    seen = pruned
    write_json(DATA_DIR / "seen.json", dict(sorted(seen.items())))


def rebuild(cfg: dict) -> None:
    digests = load_digests()
    if not digests:
        log("nothing to rebuild: no digests found")
        return
    for digest in digests:
        digest = apply_overrides(cfg, digest, parse_date(digest["date"]))
        save_digest(digest)
        write_content(digest, cfg)
    digests = load_digests()
    update_readme(digests, cfg)
    log(f"rebuilt {len(digests)} digest(s), latest {digests[0]['date']}")


def run_day(cfg: dict, target: date, force: bool) -> None:
    existing = DATA_DIR / "digests" / f"{target.isoformat()}.json"
    if existing.exists() and not force:
        log(f"{target.isoformat()} already generated; use --force to regenerate")
        rebuild(cfg)
        return

    cooldown = int(cfg["digest"].get("cooldown_days", 60))
    seen = load_seen()
    blocked = blocked_repos(seen, target, cooldown)

    token = get_token()
    gh = GitHub(token)
    if token is None:
        log("no GITHUB_TOKEN: using the unauthenticated 60 req/h limit")
    candidates = collect(cfg, gh, target)
    if not candidates:
        raise RuntimeError("all sources failed or returned nothing")
    candidates = resolve_unknown(gh, candidates)

    llm_conf = cfg.get("llm", {})
    readme_chars = int(llm_conf.get("readme_chars", 1200))

    filtered = filter_candidates(cfg, candidates, target, blocked)
    if not filtered:
        raise RuntimeError("no usable candidates left after filtering")
    shortlist = shortlist_for_llm(filtered, cfg, target)
    category_count = len({categorize(c) for c in shortlist})
    log(f"shortlist: {len(shortlist)} repos across {category_count} categories")
    shortlist = enrich(gh, shortlist, limit=len(shortlist), readme_chars=readme_chars)

    digest = curate(cfg, shortlist, target)
    digest = apply_overrides(cfg, digest, target)
    if len(digest["items"]) < int(cfg["digest"].get("count", 10)):
        log(
            f"warning: only {len(digest['items'])} items selected "
            f"(wanted {cfg['digest'].get('count', 10)})"
        )

    path = save_digest(digest)
    write_content(digest, cfg)
    update_seen(seen, digest, cooldown)

    digests = load_digests()
    update_readme(digests, cfg)

    log(f"wrote {path.relative_to(ROOT)} with {len(digest['items'])} items")
    for index, item in enumerate(digest["items"], 1):
        log(f"  {index:02d}. {item['repo']} [{item['category']}]")


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate the daily open-source digest")
    parser.add_argument("--date", help="digest date in YYYY-MM-DD (Asia/Shanghai)")
    parser.add_argument("--force", action="store_true", help="regenerate an existing day")
    parser.add_argument(
        "--rebuild", action="store_true", help="re-render the site from saved digests"
    )
    args = parser.parse_args()

    cfg = load_config()

    if args.rebuild:
        rebuild(cfg)
        return 0

    raw_date = args.date or os.environ.get("DIGEST_DATE") or ""
    if raw_date:
        try:
            target = parse_date(raw_date)
        except ValueError:
            log(f"invalid date: {raw_date}")
            return 2
    else:
        target = today_local()

    force = args.force or os.environ.get("FORCE", "").lower() in ("1", "true", "yes")

    log(f"digest date: {target.isoformat()} (Asia/Shanghai)")
    try:
        run_day(cfg, target, force)
    except Exception as exc:  # noqa: BLE001 - surface a clean CI failure
        log(f"ERROR: {exc}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
