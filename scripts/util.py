# SPDX-License-Identifier: MIT
"""Shared helpers: paths, dates, HTTP, formatting."""
from __future__ import annotations

import html as html_lib
import json
import os
import re
import time
from datetime import date, datetime
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

try:
    from zoneinfo import ZoneInfo

    TZ = ZoneInfo("Asia/Shanghai")
except Exception:  # pragma: no cover - extremely rare
    TZ = None

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
CONTENT_DIR = ROOT / "daily"
UA = "OpenDailyBot/1.0 (+https://github.com/zhouyg1992/opendaily)"

WEEKDAYS = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]


def log(message: str) -> None:
    print(f"[opendaily] {message}", flush=True)


def today_local() -> date:
    if TZ is not None:
        return datetime.now(TZ).date()
    return date.today()  # pragma: no cover


def parse_date(value: str) -> date:
    return datetime.strptime(value, "%Y-%m-%d").date()


def weekday_cn(d: date) -> str:
    return WEEKDAYS[d.weekday()]


def read_json(path: Path, default):
    try:
        with path.open("r", encoding="utf-8") as fh:
            return json.load(fh)
    except (FileNotFoundError, json.JSONDecodeError):
        return default


def write_json(path: Path, payload) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        json.dump(payload, fh, ensure_ascii=False, indent=2)
        fh.write("\n")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        fh.write(text)


def strip_tags(value: str) -> str:
    value = re.sub(r"<[^>]+>", " ", value or "")
    value = html_lib.unescape(value)
    return re.sub(r"\s+", " ", value).strip()


def clean_markdown(value: str) -> str:
    """Turn a README excerpt into readable plain text."""
    value = value or ""
    value = re.sub(r"<!--.*?-->", " ", value, flags=re.S)
    value = re.sub(r"```.*?```", " ", value, flags=re.S)
    value = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", value)
    value = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", value)
    value = re.sub(r"<[^>]+>", " ", value)
    value = re.sub(r"^\s{0,3}#{1,6}\s*", "", value, flags=re.M)
    value = re.sub(r"[*_`>|]+", " ", value)
    value = html_lib.unescape(value)
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def truncate(text: str, limit: int) -> str:
    text = text or ""
    if len(text) <= limit:
        return text
    cut = text[:limit]
    for sep in ("。", "！", "？", ". ", "! ", "? ", "; ", "；", "，", ", "):
        idx = cut.rfind(sep)
        if idx > limit * 0.6:
            return cut[: idx + len(sep)].strip()
    return cut.rsplit(" ", 1)[0].strip() + "…"


def parse_count(value) -> int:
    if isinstance(value, int):
        return value
    digits = re.sub(r"[^\d]", "", str(value or ""))
    return int(digits) if digits else 0


def fmt_count(n: int) -> str:
    n = int(n or 0)
    if n >= 1_000_000:
        scaled, unit = n / 1_000_000, "m"
    elif n >= 1_000:
        scaled, unit = n / 1_000, "k"
    else:
        return str(n)
    if scaled >= 10:
        text = f"{scaled:.0f}"
    else:
        text = f"{scaled:.1f}".rstrip("0").rstrip(".")
    return text + unit


class HttpError(RuntimeError):
    pass


class HttpClient:
    """Tiny JSON/text fetcher with GitHub rate-limit awareness."""

    def __init__(self, token: str | None = None):
        self.token = token
        self.remaining: int | None = None

    def _headers(self) -> dict:
        headers = {
            "User-Agent": UA,
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        return headers

    def _track(self, headers) -> None:
        if headers is None:
            return
        remaining = headers.get("X-RateLimit-Remaining")
        if remaining is not None:
            try:
                self.remaining = int(remaining)
            except ValueError:
                pass

    def get(
        self,
        url: str,
        *,
        timeout: int = 30,
        retries: int = 2,
        accept: str | None = None,
        allow_404: bool = False,
    ) -> str | None:
        headers = self._headers()
        if accept:
            headers["Accept"] = accept
        last_error = None
        for attempt in range(retries + 1):
            request = Request(url, headers=headers)
            try:
                with urlopen(request, timeout=timeout) as resp:
                    self._track(resp.headers)
                    charset = resp.headers.get_content_charset() or "utf-8"
                    return resp.read().decode(charset, "replace")
            except HTTPError as exc:
                self._track(exc.headers)
                body = exc.read().decode("utf-8", "replace")[:300]
                if exc.code == 404 and allow_404:
                    return None
                last_error = HttpError(f"HTTP {exc.code} for {url}: {body}")
                if exc.code in (403, 429, 500, 502, 503) and attempt < retries:
                    time.sleep(2 * (attempt + 1))
                    continue
                raise last_error
            except (URLError, TimeoutError, OSError) as exc:
                last_error = HttpError(f"network error for {url}: {exc}")
                if attempt < retries:
                    time.sleep(1.5 * (attempt + 1))
                    continue
                raise last_error
        raise last_error  # pragma: no cover


class GitHub:
    def __init__(self, token: str | None):
        self.http = HttpClient(token)
        self.api = "https://api.github.com"

    @property
    def remaining(self) -> int | None:
        return self.http.remaining

    def _get(self, path: str, params: dict | None = None, allow_404: bool = False):
        url = self.api + path
        if params:
            url += "?" + urlencode(params)
        raw = self.http.get(url, allow_404=allow_404)
        if raw is None:
            return None
        try:
            return json.loads(raw)
        except json.JSONDecodeError as exc:
            raise HttpError(f"bad JSON from {url}: {exc}") from exc

    def search_repos(self, query: str, per_page: int = 25) -> list[dict]:
        data = self._get(
            "/search/repositories",
            {"q": query, "sort": "stars", "order": "desc", "per_page": per_page},
        )
        return (data or {}).get("items", [])

    def repo(self, full_name: str) -> dict | None:
        return self._get("/repos/" + full_name, allow_404=True)


def get_token() -> str | None:
    return os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN") or None


def post_json(url: str, payload: dict, *, api_key: str | None = None, timeout: int = 180) -> str:
    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    headers = {
        "User-Agent": UA,
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"
    request = Request(url, data=body, headers=headers, method="POST")
    try:
        with urlopen(request, timeout=timeout) as resp:
            return resp.read().decode("utf-8", "replace")
    except HTTPError as exc:
        detail = exc.read().decode("utf-8", "replace")[:600]
        raise HttpError(f"HTTP {exc.code} from {url}: {detail}") from exc
    except (URLError, TimeoutError, OSError) as exc:
        raise HttpError(f"network error for {url}: {exc}") from exc
