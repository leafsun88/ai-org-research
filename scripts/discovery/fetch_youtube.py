"""
Phase 3: YouTube采集
- 先继承 podcast 阶段的 query map，补齐 YouTube 搜索宇宙
- Search provider: RapidAPI Metadata Search -> yt-dlp fallback
- Transcript provider: RapidAPI Transcript3 -> youtube-transcript-api -> yt-dlp subtitle fallback
- 保存 transcript 到 _staging/sources/youtube/transcripts/
- 保存 segments、candidate、status 到 _staging/sources/youtube/metadata/
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime
from pathlib import Path
from typing import Any

try:
    from target_config import (
        build_alias_query_terms,
        get_channel,
        get_channel_queries,
        load_target,
        target_script_root,
        target_key,
        target_vault_root,
        unique_strings,
    )
except ImportError:
    load_target = None
    target_script_root = None

    def target_key(target: dict[str, Any]) -> str:
        return target.get("research_key") or target.get("ticker")

    def unique_strings(values: list[str]) -> list[str]:
        result: list[str] = []
        seen: set[str] = set()
        for value in values:
            clean = str(value).strip()
            key = clean.lower()
            if clean and key not in seen:
                seen.add(key)
                result.append(clean)
        return result

    def build_alias_query_terms(target: dict[str, Any], include_people: bool = True) -> list[str]:
        terms = [target.get("company_name", ""), target.get("ticker", ""), target.get("research_key", "")]
        terms.extend(target.get("aliases", []))
        if include_people:
            terms.extend(target.get("founders", []))
            terms.extend(target.get("executives", []))
        return unique_strings(terms)

    def get_channel(target: dict[str, Any], channel: str) -> dict[str, Any]:
        return target.get("channels", {}).get(channel, {})

    def get_channel_queries(target: dict[str, Any], channel: str) -> list[str]:
        return unique_strings([str(q) for q in get_channel(target, channel).get("queries", [])])

    def target_vault_root(target: dict[str, Any]) -> Path:
        slug = target.get("slug") or str(target.get("company_name", "target")).lower()
        return Path.cwd() / "companies" / slug / "vault"


def load_project_env() -> None:
    """Load local .env without adding python-dotenv as a dependency."""
    for env_path in [
        Path.cwd() / ".env",
        Path(__file__).resolve().parents[2] / ".env",
        Path(__file__).resolve().parents[1] / ".env",
    ]:
        if not env_path.exists():
            continue
        try:
            for raw_line in env_path.read_text(encoding="utf-8").splitlines():
                line = raw_line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                key, value = line.split("=", 1)
                key = key.strip()
                value = value.strip().strip('"').strip("'")
                if key and key not in os.environ:
                    os.environ[key] = value
        except Exception:
            pass


load_project_env()


DB_DIR = Path(os.environ.get("ALIKE_DB_DIR", str(Path(__file__).parent.parent)))
_TARGET_CACHE: dict[str, dict[str, Any] | None] = {}
YT_DLP = os.environ.get("YT_DLP_PATH", "/Users/leafsun/Library/Python/3.9/bin/yt-dlp")
YT_DLP_COOKIES_FROM_BROWSER = os.environ.get("YTDLP_COOKIES_FROM_BROWSER")
YT_DLP_COOKIES_FILE = os.environ.get("YTDLP_COOKIES_FILE")
YT_DLP_EXTRACTOR_ARGS = os.environ.get("YTDLP_EXTRACTOR_ARGS")
YT_DLP_USER_AGENT = os.environ.get(
    "YTDLP_USER_AGENT",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
)
YT_DLP_SLEEP_REQUESTS = os.environ.get("YTDLP_SLEEP_REQUESTS", "1")
YT_DLP_SUBTITLE_TIMEOUT = int(os.environ.get("YTDLP_SUBTITLE_TIMEOUT", "25"))

RAPIDAPI_KEY = os.environ.get("RAPIDAPI_KEY", "").strip()
RAPIDAPI_KEY_HEADER = "x-rapidapi-" + "key"
RAPIDAPI_HOST_HEADER = "x-rapidapi-" + "host"
RAPIDAPI_SEARCH_HOST = os.environ.get(
    "YOUTUBE_RAPIDAPI_SEARCH_HOST",
    "youtube-transcript-metadata-search.p.rapidapi.com",
)
RAPIDAPI_TRANSCRIPT_HOST = os.environ.get(
    "YOUTUBE_RAPIDAPI_TRANSCRIPT_HOST",
    "youtube-transcript3.p.rapidapi.com",
)
RAPIDAPI_TIMEOUT = int(os.environ.get("RAPIDAPI_TIMEOUT", "25"))
RAPIDAPI_USER_AGENT = os.environ.get("RAPIDAPI_USER_AGENT", "curl/8.7.1")

SUPPORTED_SEARCH_PROVIDERS = {"rapidapi_metadata_search", "yt_dlp_search"}
SUPPORTED_TRANSCRIPT_PROVIDERS = {
    "rapidapi_transcript3",
    "youtube_transcript_api",
    "yt_dlp_subtitle",
}
DEFAULT_SEARCH_PROVIDER_ORDER = ["rapidapi_metadata_search", "yt_dlp_search"]
DEFAULT_TRANSCRIPT_PROVIDER_ORDER = [
    "rapidapi_transcript3",
    "youtube_transcript_api",
    "yt_dlp_subtitle",
]
LOW_CONFIDENCE_QUERY_STOPWORDS = {
    "interview",
    "podcast",
    "founder",
    "ceo",
    "talk",
    "keynote",
    "demo",
    "product",
    "company",
    "deep",
    "dive",
    "organization",
    "workflow",
    "community",
    "with",
    "about",
    "from",
    "the",
    "and",
    "for",
}
NOISY_RELEVANCE_TERMS = LOW_CONFIDENCE_QUERY_STOPWORDS | {
    "ai",
    "mj",
    "app",
    "apps",
    "tool",
    "tools",
    "model",
    "models",
    "video",
    "videos",
    "image",
    "images",
    "generation",
    "creative",
    "coding",
    "agent",
    "agents",
    "builder",
    "startup",
    "startups",
    "software",
    "discord",
    "community",
    "rooms",
    "style",
    "reference",
    "prompt",
    "prompts",
}

try:
    from youtube_transcript_api import YouTubeTranscriptApi
except ImportError:
    YouTubeTranscriptApi = None


def now_iso() -> str:
    return datetime.now().isoformat(timespec="seconds")


def maybe_load_target(ticker: str, target: dict[str, Any] | None = None) -> dict[str, Any] | None:
    if target:
        return target
    if ticker in _TARGET_CACHE:
        return _TARGET_CACHE[ticker]
    if load_target:
        try:
            _TARGET_CACHE[ticker] = load_target(ticker)
            return _TARGET_CACHE[ticker]
        except Exception:
            pass
    _TARGET_CACHE[ticker] = None
    return None


def staging_root_for_ticker(ticker: str, target: dict[str, Any] | None = None) -> Path:
    loaded = maybe_load_target(ticker, target)
    if loaded and target_script_root:
        return target_script_root(loaded)
    return DB_DIR / ticker


def youtube_output_dir(ticker: str, target: dict[str, Any] | None = None) -> Path:
    output_dir = staging_root_for_ticker(ticker, target) / "sources" / "youtube"
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir


def youtube_metadata_dir(ticker: str, target: dict[str, Any] | None = None) -> Path:
    output_dir = youtube_output_dir(ticker, target) / "metadata"
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir


def youtube_transcripts_dir(ticker: str, target: dict[str, Any] | None = None) -> Path:
    output_dir = youtube_output_dir(ticker, target) / "transcripts"
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir


def parse_provider_order(
    value: str | list[str] | None,
    default: list[str],
    supported: set[str],
) -> list[str]:
    """Parse provider order from CLI/config, preserving order and dropping unknowns."""
    if value is None or value == "":
        raw_values = list(default)
    elif isinstance(value, list):
        raw_values = value
    else:
        raw_values = [part.strip() for part in str(value).split(",")]

    result: list[str] = []
    seen: set[str] = set()
    for provider in raw_values:
        clean = str(provider).strip()
        if clean in supported and clean not in seen:
            seen.add(clean)
            result.append(clean)

    return result or [provider for provider in default if provider in supported]


def normalize_date(value: Any) -> str:
    if value is None:
        return ""
    text = str(value).strip()
    if not text or text == "NA":
        return ""
    if len(text) == 8 and text.isdigit():
        return f"{text[:4]}-{text[4:6]}-{text[6:8]}"
    match = re.match(r"(\d{4}-\d{2}-\d{2})", text)
    if match:
        return match.group(1)
    match = re.match(r"(\d{4})/(\d{2})/(\d{2})", text)
    if match:
        return f"{match.group(1)}-{match.group(2)}-{match.group(3)}"
    return text


def parse_seconds(value: Any) -> float:
    if value in (None, "", "NA"):
        return 0.0
    if isinstance(value, (int, float)):
        return float(value)
    text = str(value).strip()
    if not text:
        return 0.0
    try:
        return float(text)
    except ValueError:
        pass
    if ":" in text:
        try:
            parts = [float(part) for part in text.split(":")]
            seconds = 0.0
            for part in parts:
                seconds = seconds * 60 + part
            return seconds
        except ValueError:
            return 0.0
    return 0.0


def safe_filename(value: str, max_len: int = 70) -> str:
    safe = re.sub(r"[^\w\s\-\u4e00-\u9fff]", "", value or "youtube-video")
    safe = re.sub(r"\s+", "-", safe.strip())
    return (safe[:max_len].strip("-") or "youtube-video")


def _frontmatter_extra(target: dict[str, Any] | None = None) -> str:
    if not target:
        return ""
    return (
        f"company: {json.dumps(target.get('company_name', ''), ensure_ascii=False)}\n"
        f"research_key: {target_key(target)}\n"
        "credibility: S2-S3\n"
        "evidence: E2\n"
    )


def clean_vtt(vtt_text: str) -> str:
    """Convert VTT subtitle to clean text, removing duplicates and timestamps."""
    lines = vtt_text.split("\n")
    text_lines = []
    seen = set()

    for line in lines:
        if line.startswith("WEBVTT") or line.startswith("Kind:") or line.startswith("Language:"):
            continue
        if "-->" in line:
            continue
        if not line.strip():
            continue
        if line.strip().startswith("align:") or line.strip().startswith("position:"):
            continue

        clean = re.sub(r"<[^>]+>", "", line).strip()
        if not clean:
            continue

        if clean not in seen:
            seen.add(clean)
            text_lines.append(clean)

    return " ".join(text_lines)


def build_common_yt_dlp_args() -> list[str]:
    """Build yt-dlp args that help with YouTube's stricter anti-bot checks."""
    args = ["--user-agent", YT_DLP_USER_AGENT]

    if YT_DLP_COOKIES_FROM_BROWSER:
        args.extend(["--cookies-from-browser", YT_DLP_COOKIES_FROM_BROWSER])
    elif YT_DLP_COOKIES_FILE:
        args.extend(["--cookies", YT_DLP_COOKIES_FILE])

    if YT_DLP_EXTRACTOR_ARGS:
        args.extend(["--extractor-args", YT_DLP_EXTRACTOR_ARGS])

    return args


def fetch_transcript_via_api(video_id: str) -> str | None:
    """Fallback transcript fetcher using youtube-transcript-api."""
    if not YouTubeTranscriptApi:
        return None

    try:
        api = YouTubeTranscriptApi()
        for lang in (["en"], ["en-US"], ["zh-Hans", "zh-CN", "zh"], None):
            try:
                transcript = api.fetch(video_id, languages=lang) if lang else api.fetch(video_id)
                text = " ".join(entry.text for entry in transcript.snippets).strip()
                if len(text) > 100:
                    return text
            except Exception:
                continue
    except Exception:
        return None

    return None


def search_youtube(query: str, max_results: int = 10) -> list[dict[str, Any]]:
    """Search YouTube using yt-dlp, return normalized candidate metadata."""
    cmd = [
        YT_DLP,
        f"ytsearch{max_results}:{query}",
        "--flat-playlist",
        "--print",
        "%(id)s\t%(title)s\t%(channel)s\t%(upload_date)s\t%(duration)s",
    ]
    cmd.extend(build_common_yt_dlp_args())
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        videos: list[dict[str, Any]] = []
        for line in result.stdout.strip().split("\n"):
            if not line.strip():
                continue
            parts = line.split("\t")
            if len(parts) >= 5:
                video_id = parts[0]
                videos.append(
                    {
                        "id": video_id,
                        "video_id": video_id,
                        "title": parts[1],
                        "channel": parts[2],
                        "channelName": parts[2],
                        "date": normalize_date(parts[3]),
                        "publishDate": normalize_date(parts[3]),
                        "duration": parse_seconds(parts[4]),
                        "url": f"https://www.youtube.com/watch?v={video_id}",
                        "match_count": 0,
                        "timestamps": [],
                        "ai_summary": "",
                        "source_query": query,
                        "source_queries": [query],
                        "search_provider": "yt_dlp_search",
                        "search_providers": ["yt_dlp_search"],
                    }
                )
        return videos
    except Exception as exc:
        print(f"  搜索失败: {exc}")
        return []


def download_subtitle_via_yt_dlp(video_id: str, lang: str = "en") -> tuple[str | None, str]:
    """Download subtitle for a video using yt-dlp only. Returns clean text and language."""
    with tempfile.TemporaryDirectory() as tmpdir:
        out_template = os.path.join(tmpdir, f"sub_{video_id}")

        for sub_flag in ["--write-auto-sub", "--write-sub"]:
            cmd = [
                YT_DLP,
                sub_flag,
                "--skip-download",
                "--sub-lang",
                lang,
                "--sleep-requests",
                YT_DLP_SLEEP_REQUESTS,
                "-o",
                out_template,
                f"https://www.youtube.com/watch?v={video_id}",
            ]
            cmd.extend(build_common_yt_dlp_args())
            try:
                subprocess.run(cmd, capture_output=True, text=True, timeout=YT_DLP_SUBTITLE_TIMEOUT)
            except subprocess.TimeoutExpired:
                continue

            for path in Path(tmpdir).glob(f"sub_{video_id}*.vtt"):
                clean_text = clean_vtt(path.read_text(encoding="utf-8", errors="ignore"))
                if len(clean_text) > 100:
                    return clean_text, lang

            for path in Path(tmpdir).glob(f"sub_{video_id}*.srt"):
                srt_text = path.read_text(encoding="utf-8", errors="ignore")
                clean = re.sub(
                    r"\d+\n\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}\n",
                    "",
                    srt_text,
                )
                clean = re.sub(r"<[^>]+>", "", clean)
                clean = " ".join(clean.split())
                if len(clean) > 100:
                    return clean, lang

        if lang == "en":
            return download_subtitle_via_yt_dlp(video_id, lang="zh-Hans")

    return None, ""


def download_subtitle(video_id: str, lang: str = "en") -> str | None:
    """Backward-compatible wrapper: yt-dlp subtitle, then youtube-transcript-api."""
    text, _language = download_subtitle_via_yt_dlp(video_id, lang=lang)
    if text:
        return text
    return fetch_transcript_via_api(video_id)


def rapidapi_get(host: str, path: str, params: dict[str, Any]) -> dict[str, Any]:
    if not RAPIDAPI_KEY:
        return {
            "ok": False,
            "status": "skipped_missing_key",
            "reason": "RAPIDAPI_KEY is not set",
            "stop_provider": False,
        }

    query = urllib.parse.urlencode({k: v for k, v in params.items() if v not in (None, "")})
    url = f"https://{host}{path}"
    if query:
        url = f"{url}?{query}"

    request = urllib.request.Request(
        url,
        headers={
            RAPIDAPI_KEY_HEADER: RAPIDAPI_KEY,
            RAPIDAPI_HOST_HEADER: host,
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": RAPIDAPI_USER_AGENT,
        },
        method="GET",
    )
    try:
        with urllib.request.urlopen(request, timeout=RAPIDAPI_TIMEOUT) as response:
            body = response.read().decode("utf-8", errors="replace")
            return {
                "ok": True,
                "status": "success",
                "status_code": response.status,
                "data": json.loads(body) if body.strip() else {},
            }
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        if exc.code in (401, 403):
            reason = "rapidapi_auth_error"
            stop_provider = True
        elif exc.code == 429:
            reason = "rapidapi_quota_or_rate_limit"
            stop_provider = True
        else:
            reason = "rapidapi_http_error"
            stop_provider = False
        return {
            "ok": False,
            "status": reason,
            "status_code": exc.code,
            "body_preview": body[:500],
            "stop_provider": stop_provider,
        }
    except Exception as exc:
        return {
            "ok": False,
            "status": "rapidapi_request_error",
            "reason": str(exc),
            "stop_provider": False,
        }


def _payload_items(payload: Any, preferred_key: str) -> list[Any]:
    if isinstance(payload, list):
        return payload
    if not isinstance(payload, dict):
        return []
    for key in (preferred_key, "results", "data", "items"):
        value = payload.get(key)
        if isinstance(value, list):
            return value
        if isinstance(value, dict):
            for nested_key in (preferred_key, "results", "items"):
                nested = value.get(nested_key)
                if isinstance(nested, list):
                    return nested
    return []


def _normalize_timestamp(value: Any) -> dict[str, Any]:
    if isinstance(value, str):
        return {"transcript": value, "context": "", "time": None, "formattedTime": ""}
    if not isinstance(value, dict):
        return {}
    return {
        "time": value.get("time"),
        "formattedTime": value.get("formattedTime") or value.get("formatted_time") or "",
        "transcript": value.get("transcript") or value.get("text") or "",
        "context": value.get("context") or "",
    }


def normalize_rapidapi_search_response(payload: Any, source_query: str) -> list[dict[str, Any]]:
    """Normalize YouTube Transcript & Metadata Search response into candidate rows."""
    candidates: list[dict[str, Any]] = []
    for item in _payload_items(payload, "results"):
        if not isinstance(item, dict):
            continue
        video_id = item.get("videoId") or item.get("video_id") or ""
        raw_id = item.get("id") or ""
        if not video_id and re.fullmatch(r"[A-Za-z0-9_-]{8,20}", str(raw_id)):
            video_id = str(raw_id)
        if not video_id:
            continue

        timestamps = [
            ts for ts in (_normalize_timestamp(ts) for ts in item.get("timestamps", []) or []) if ts
        ]
        match_count_raw = item.get("matchCount", item.get("match_count", len(timestamps)))
        try:
            match_count = int(match_count_raw)
        except (TypeError, ValueError):
            match_count = len(timestamps)

        title = item.get("title") or item.get("name") or f"YouTube video {video_id}"
        channel = item.get("channelName") or item.get("channel") or item.get("channelTitle") or ""
        date_str = normalize_date(item.get("publishDate") or item.get("publishedAt") or item.get("date"))
        duration = parse_seconds(item.get("durationSeconds") or item.get("duration") or item.get("lengthSeconds"))

        candidates.append(
            {
                "id": video_id,
                "video_id": video_id,
                "raw_id": raw_id,
                "title": title,
                "channel": channel,
                "channelName": channel,
                "date": date_str,
                "publishDate": date_str,
                "duration": duration,
                "url": item.get("url") or f"https://www.youtube.com/watch?v={video_id}",
                "match_count": match_count,
                "ai_summary": item.get("aiSummary") or item.get("summary") or "",
                "timestamps": timestamps,
                "source_query": source_query,
                "source_queries": [source_query],
                "search_provider": "rapidapi_metadata_search",
                "search_providers": ["rapidapi_metadata_search"],
            }
        )
    return candidates


def normalize_rapidapi_transcript_response(payload: Any) -> tuple[str, list[dict[str, Any]], str]:
    """Normalize Youtube Transcript API response into text, segment rows, and language."""
    segments: list[dict[str, Any]] = []
    language = ""
    for item in _payload_items(payload, "transcript"):
        if isinstance(item, str):
            text = item.strip()
            if text:
                segments.append({"text": text, "duration": None, "offset": None, "lang": ""})
            continue
        if not isinstance(item, dict):
            continue
        text = str(item.get("text") or item.get("transcript") or "").strip()
        if not text:
            continue
        lang = str(item.get("lang") or item.get("language") or "").strip()
        if lang and not language:
            language = lang
        segments.append(
            {
                "text": text,
                "duration": parse_seconds(item.get("duration")),
                "offset": parse_seconds(item.get("offset") or item.get("start") or item.get("time")),
                "lang": lang,
            }
        )

    text = " ".join(segment["text"] for segment in segments).strip()
    return text, segments, language


def rapidapi_metadata_search(query: str, cfg: dict[str, Any]) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    status = {
        "record_type": "provider_call",
        "provider": "rapidapi_metadata_search",
        "query": query,
        "host": RAPIDAPI_SEARCH_HOST,
        "generated_at": now_iso(),
    }
    params = {
        "q": query,
        "category": cfg.get("category", "Technology"),
        "sortBy": cfg.get("sort_by", cfg.get("sortBy", "relevance")),
        "duration": cfg.get("duration", "any"),
        "fuzzy": cfg.get("fuzzy", 1),
        "mode": cfg.get("mode", "fuzzy"),
    }
    if cfg.get("video"):
        params["video"] = cfg.get("video")

    response = rapidapi_get(RAPIDAPI_SEARCH_HOST, "/api/search", params)
    status.update({key: value for key, value in response.items() if key != "data"})
    if not response.get("ok"):
        return [], status

    candidates = normalize_rapidapi_search_response(response.get("data", {}), query)
    status["status"] = "success" if candidates else "no_results"
    status["results"] = len(candidates)
    return candidates, status


def rapidapi_transcript3(video_id: str, url: str = "") -> tuple[dict[str, Any] | None, list[dict[str, Any]]]:
    attempts: list[dict[str, Any]] = []
    if not RAPIDAPI_KEY:
        attempts.append(
            {
                "provider": "rapidapi_transcript3",
                "status": "skipped_missing_key",
                "reason": "RAPIDAPI_KEY is not set",
                "stop_provider": False,
                "generated_at": now_iso(),
            }
        )
        return None, attempts

    for param_name, param_value in (("videoId", video_id), ("url", url)):
        if not param_value:
            continue
        response = rapidapi_get(RAPIDAPI_TRANSCRIPT_HOST, "/api/transcript", {param_name: param_value})
        attempt = {
            "provider": "rapidapi_transcript3",
            "param": param_name,
            "host": RAPIDAPI_TRANSCRIPT_HOST,
            "generated_at": now_iso(),
        }
        attempt.update({key: value for key, value in response.items() if key != "data"})
        attempts.append(attempt)
        if not response.get("ok"):
            if response.get("stop_provider"):
                break
            continue

        text, segments, language = normalize_rapidapi_transcript_response(response.get("data", {}))
        if len(text) > 100:
            return (
                {
                    "text": text,
                    "segments": segments,
                    "language": language,
                    "transcript_provider": "rapidapi",
                    "transcript_method": "rapidapi_transcript3",
                },
                attempts,
            )
        attempts[-1]["status"] = "empty_or_short_transcript"
        attempts[-1]["chars"] = len(text)
        if param_name == "videoId":
            # A 200 response with an empty transcript is a content miss, not a transport miss.
            # Retrying the same video through the URL endpoint usually burns another RapidAPI
            # request without improving recall, so keep URL fallback for request-level failures.
            break

    return None, attempts


def fetch_transcript_with_providers(
    video_id: str,
    video_url: str,
    provider_order: list[str],
    disabled_providers: set[str] | None = None,
) -> tuple[dict[str, Any] | None, list[dict[str, Any]]]:
    disabled_providers = disabled_providers if disabled_providers is not None else set()
    attempts: list[dict[str, Any]] = []

    for provider in provider_order:
        if provider in disabled_providers:
            attempts.append(
                {
                    "provider": provider,
                    "status": "skipped_provider_disabled",
                    "generated_at": now_iso(),
                }
            )
            continue

        if provider == "rapidapi_transcript3":
            result, provider_attempts = rapidapi_transcript3(video_id, video_url)
            attempts.extend(provider_attempts)
            if any(attempt.get("stop_provider") for attempt in provider_attempts):
                disabled_providers.add(provider)
            if result:
                return result, attempts

        elif provider == "youtube_transcript_api":
            text = fetch_transcript_via_api(video_id)
            attempt = {
                "provider": provider,
                "status": "success" if text else "no_transcript",
                "generated_at": now_iso(),
                "chars": len(text) if text else 0,
            }
            attempts.append(attempt)
            if text:
                return (
                    {
                        "text": text,
                        "segments": [],
                        "language": "",
                        "transcript_provider": "youtube_transcript_api",
                        "transcript_method": "youtube_transcript_api",
                    },
                    attempts,
                )

        elif provider == "yt_dlp_subtitle":
            text, language = download_subtitle_via_yt_dlp(video_id)
            attempt = {
                "provider": provider,
                "status": "success" if text else "no_subtitle",
                "generated_at": now_iso(),
                "chars": len(text) if text else 0,
            }
            attempts.append(attempt)
            if text:
                return (
                    {
                        "text": text,
                        "segments": [],
                        "language": language,
                        "transcript_provider": "yt_dlp",
                        "transcript_method": "yt_dlp_subtitle",
                    },
                    attempts,
                )

    return None, attempts


def read_podcast_query_map(ticker: str, target: dict[str, Any] | None = None) -> tuple[list[str], str]:
    staging_root = staging_root_for_ticker(ticker, target)
    candidates = [
        staging_root / "sources" / "podcasts" / "metadata" / "_podcast_query_map.md",
        DB_DIR / ticker / "_podcast_query_map.md",
        DB_DIR / ticker / "sources" / "podcasts" / "_podcast_query_map.md",
    ]
    if target:
        vault = target_vault_root(target)
        candidates.extend(
            [
                vault / "podcasts" / "_podcast_query_map.md",
                vault / "podcasts" / "metadata" / "_podcast_query_map.md",
            ]
        )

    for path in candidates:
        if not path.exists():
            continue
        queries: list[str] = []
        in_query_section = False
        for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
            stripped = line.strip()
            if stripped.startswith("## "):
                in_query_section = any(token in stripped.lower() for token in ["query", "搜索"])
                continue
            if in_query_section and stripped.startswith("- "):
                value = stripped[2:].strip()
                if value:
                    queries.append(value)
        if not queries:
            for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
                stripped = line.strip()
                if stripped.startswith("- "):
                    value = stripped[2:].strip()
                    if value:
                        queries.append(value)
        return unique_strings(queries), str(path)

    return [], ""


def default_queries(ticker: str, company_name: str) -> list[str]:
    return [
        f"{company_name} CEO interview",
        f"{company_name} founder interview",
        f"{company_name} product demo interview",
        f"{company_name} organization AI workflow",
        f"{ticker} company deep dive",
    ]


def build_youtube_queries(
    ticker: str,
    company_name: str,
    configured_queries: list[str] | None,
    target: dict[str, Any] | None,
    max_queries: int | None,
) -> tuple[list[str], str, list[str]]:
    inherited_queries, inherited_path = read_podcast_query_map(ticker, target)
    seed_queries = list(inherited_queries)
    seed_queries.extend(configured_queries or [])
    if target:
        seed_queries.extend(
            [
                f"{term} interview"
                for term in build_alias_query_terms(target, include_people=True)
                if len(str(term).strip()) > 2
            ]
        )
    if not seed_queries:
        seed_queries = default_queries(ticker, company_name)

    all_queries = unique_strings(seed_queries)
    if max_queries and max_queries > 0:
        all_queries = all_queries[:max_queries]
    return all_queries, inherited_path, inherited_queries


def write_youtube_query_map(
    ticker: str,
    company_name: str,
    queries: list[str],
    inherited_path: str,
    inherited_queries: list[str],
    search_provider_order: list[str],
    transcript_provider_order: list[str],
    cfg: dict[str, Any],
    target: dict[str, Any] | None,
) -> Path:
    output_dir = youtube_metadata_dir(ticker, target)
    path = output_dir / "_youtube_query_map.md"
    content = f"""---
ticker: {ticker}
type: youtube_query_map
company: {json.dumps(company_name, ensure_ascii=False)}
generated_at: {now_iso()}
---

# YouTube Query Map

## Source
- inherited_podcast_query_map: {inherited_path or "none"}
- inherited_query_count: {len(inherited_queries)}

## Provider Plan
- search_provider_order: {", ".join(search_provider_order)}
- transcript_provider_order: {", ".join(transcript_provider_order)}
- rapidapi_search_host: {RAPIDAPI_SEARCH_HOST}
- rapidapi_transcript_host: {RAPIDAPI_TRANSCRIPT_HOST}
- rapidapi_key_present: {bool(RAPIDAPI_KEY)}
- category: {cfg.get("category", "Technology")}
- sort_by: {cfg.get("sort_by", cfg.get("sortBy", "relevance"))}
- duration: {cfg.get("duration", "any")}
- mode: {cfg.get("mode", "fuzzy")}
- fuzzy: {cfg.get("fuzzy", 1)}
- min_duration_min: {cfg.get("min_duration_min", 0)}
- pre_download_relevance: {cfg.get("pre_download_relevance", True if target else False)}
- relevance_min_score: {cfg.get("relevance_min_score", 3)}

## 搜索 Query
"""
    for query in queries:
        content += f"- {query}\n"
    if target:
        content += "\n## Target Terms\n"
        for term in build_alias_query_terms(target, include_people=True):
            content += f"- {term}\n"
        content += "\n## Pre-Download Relevance Terms\n"
        for term in build_relevance_required_terms(target, company_name, ticker, cfg):
            content += f"- {term}\n"

    path.write_text(content, encoding="utf-8")
    return path


def search_youtube_candidates(
    query: str,
    max_results: int,
    provider_order: list[str],
    cfg: dict[str, Any],
    disabled_providers: set[str],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    statuses: list[dict[str, Any]] = []
    for provider in provider_order:
        if provider in disabled_providers:
            statuses.append(
            {
                "record_type": "provider_call",
                "provider": provider,
                "query": query,
                "status": "skipped_provider_disabled",
                "generated_at": now_iso(),
                }
            )
            continue

        if provider == "rapidapi_metadata_search":
            candidates, status = rapidapi_metadata_search(query, cfg)
            if candidates:
                candidates, rejected = filter_low_confidence_rapidapi_candidates(candidates)
                status["filtered_low_confidence"] = len(rejected)
                if rejected:
                    statuses.extend(rejected)
            statuses.append(status)
            if status.get("stop_provider"):
                disabled_providers.add(provider)
            if candidates:
                return candidates[:max_results], statuses

        elif provider == "yt_dlp_search":
            candidates = search_youtube(query, max_results=max_results)
            statuses.append(
                {
                    "record_type": "provider_call",
                    "provider": provider,
                    "query": query,
                    "status": "success" if candidates else "no_results",
                    "results": len(candidates),
                    "generated_at": now_iso(),
                }
            )
            if candidates:
                return candidates[:max_results], statuses

    return [], statuses


def candidate_text(candidate: dict[str, Any]) -> str:
    timestamp_text = " ".join(
        f"{ts.get('transcript', '')} {ts.get('context', '')}" for ts in candidate.get("timestamps", [])
    )
    return " ".join(
        [
            str(candidate.get("title", "")),
            str(candidate.get("channel", "")),
            str(candidate.get("ai_summary", "")),
            timestamp_text,
        ]
    ).lower()


def normalize_match_text(value: str) -> str:
    return re.sub(r"\s+", " ", str(value or "").lower()).strip()


def term_matches_text(term: str, text: str) -> bool:
    clean = normalize_match_text(term)
    if not clean:
        return False
    normalized_text = normalize_match_text(text)
    if not normalized_text:
        return False
    if " " in clean or "." in clean or "-" in clean:
        return clean in normalized_text
    if len(clean) < 3:
        return False
    return re.search(rf"(?<![a-z0-9]){re.escape(clean)}(?![a-z0-9])", normalized_text) is not None


def build_relevance_required_terms(
    target: dict[str, Any] | None,
    company_name: str,
    ticker: str,
    cfg: dict[str, Any],
) -> list[str]:
    raw_terms: list[str] = [company_name, ticker]
    if target:
        if cfg.get("relevance_terms"):
            raw_terms.extend(target.get("founders", []) or [])
            raw_terms.extend(target.get("executives", []) or [])
            raw_terms.extend(cfg.get("relevance_terms", []) or [])
        else:
            raw_terms.extend(build_alias_query_terms(target, include_people=True))
    else:
        raw_terms.extend(cfg.get("relevance_terms", []) or [])

    terms: list[str] = []
    seen: set[str] = set()
    for term in raw_terms:
        clean = normalize_match_text(str(term))
        if not clean:
            continue
        if clean in NOISY_RELEVANCE_TERMS:
            continue
        if len(clean) < 3:
            continue
        if clean not in seen:
            seen.add(clean)
            terms.append(str(term).strip())
    return terms


def query_signal_terms(query: str) -> list[str]:
    return [
        term
        for term in re.split(r"\W+", str(query).lower())
        if len(term) >= 4 and term not in LOW_CONFIDENCE_QUERY_STOPWORDS
    ]


def candidate_metadata_relevance(
    candidate: dict[str, Any],
    required_terms: list[str] | None = None,
    query_terms: list[str] | None = None,
    exclude_terms: list[str] | None = None,
    min_score: float = 3,
) -> dict[str, Any]:
    """Score whether a candidate's metadata/snippets truly match the target."""
    text = candidate_text(candidate)
    required_terms = required_terms or []
    query_terms = query_terms or candidate.get("source_queries", []) or []
    exclude_terms = exclude_terms or []

    term_hits: list[str] = []
    query_hits: list[str] = []
    excluded_hits: list[str] = []
    score = 0.0

    for term in required_terms:
        if term_matches_text(str(term), text):
            term_hits.append(str(term))
            score += 4 if " " in str(term).strip() else 3

    seen_query_terms: set[str] = set()
    for query in query_terms:
        for term in query_signal_terms(str(query)):
            if term in seen_query_terms:
                continue
            seen_query_terms.add(term)
            if term_matches_text(term, text):
                query_hits.append(term)
                score += 1

    for term in exclude_terms:
        if term_matches_text(str(term), text):
            excluded_hits.append(str(term))
            score -= 5

    try:
        match_count = int(candidate.get("match_count") or 0)
    except (TypeError, ValueError):
        match_count = 0
    score += min(match_count, 5) * 0.5
    score += min(len(candidate.get("timestamps", []) or []), 3) * 0.25

    if excluded_hits:
        reason = "exclude_term_hit"
        is_relevant = False
    elif required_terms and not term_hits:
        reason = "no_required_term_hit"
        is_relevant = False
    else:
        reason = "score_pass" if score >= min_score else "score_below_threshold"
        is_relevant = score >= min_score

    return {
        "is_relevant": is_relevant,
        "score": score,
        "term_hits": term_hits,
        "query_hits": query_hits,
        "excluded_hits": excluded_hits,
        "reason": reason,
    }


def candidate_has_match_evidence(candidate: dict[str, Any]) -> bool:
    """Keep RapidAPI candidates only when the response has real match evidence.

    RapidAPI fuzzy search can return generic videos with matchCount=0. Pulling
    transcripts for those burns quota without improving recall, so require
    either explicit matchCount/timestamps or a title/channel/summary/context hit
    on non-generic query terms.
    """
    try:
        match_count = int(candidate.get("match_count") or 0)
    except (TypeError, ValueError):
        match_count = 0
    if match_count > 0:
        return True
    text = candidate_text(candidate)
    for query in candidate.get("source_queries", []) or [candidate.get("source_query", "")]:
        if any(term in text for term in query_signal_terms(str(query))):
            return True
    return False


def filter_low_confidence_rapidapi_candidates(
    candidates: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    kept: list[dict[str, Any]] = []
    rejected: list[dict[str, Any]] = []
    for candidate in candidates:
        if candidate_has_match_evidence(candidate):
            kept.append(candidate)
            continue
        rejected.append(
            {
                "provider": "rapidapi_metadata_search",
                "record_type": "rejected_candidate",
                "video_id": candidate.get("video_id") or candidate.get("id"),
                "title": candidate.get("title", ""),
                "query": candidate.get("source_query", ""),
                "status": "filtered_low_confidence_rapidapi",
                "match_count": candidate.get("match_count", 0),
                "generated_at": now_iso(),
            }
        )
    return kept, rejected


def score_candidate(candidate: dict[str, Any], focus_terms: list[str]) -> float:
    text = candidate_text(candidate)
    score = float(candidate.get("match_count", 0)) * 3
    score += min(len(candidate.get("timestamps", []) or []), 8)
    if candidate.get("duration", 0) >= 600:
        score += 2
    if candidate.get("date"):
        score += 0.5

    for query in candidate.get("source_queries", []):
        terms = [term for term in re.split(r"\W+", str(query).lower()) if len(term) >= 4]
        if any(term in text for term in terms):
            score += 1.5

    for term in focus_terms:
        clean = str(term).strip().lower()
        if clean and clean in text:
            score += 5

    return score


def dedupe_and_rank_candidates(
    candidates: list[dict[str, Any]],
    focus_terms: list[str],
    min_duration_min: float = 0,
    relevance_required_terms: list[str] | None = None,
    exclude_terms: list[str] | None = None,
    pre_download_relevance: bool = False,
    min_relevance_score: float = 3,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    by_id: dict[str, dict[str, Any]] = {}
    filtered: list[dict[str, Any]] = []
    min_seconds = float(min_duration_min or 0) * 60
    relevance_required_terms = relevance_required_terms or []
    exclude_terms = exclude_terms or []

    for candidate in candidates:
        duration = parse_seconds(candidate.get("duration"))
        if min_seconds and duration and duration < min_seconds:
            filtered.append(
                {
                    "id": candidate.get("id"),
                    "title": candidate.get("title"),
                    "duration": duration,
                    "status": "filtered_short_duration",
                }
            )
            continue

        video_id = candidate.get("video_id") or candidate.get("id")
        if not video_id:
            continue
        candidate["duration"] = duration

        if video_id not in by_id:
            by_id[video_id] = dict(candidate)
            by_id[video_id]["source_queries"] = list(candidate.get("source_queries", []))
            by_id[video_id]["search_providers"] = list(candidate.get("search_providers", []))
            continue

        existing = by_id[video_id]
        existing["source_queries"] = unique_strings(
            existing.get("source_queries", []) + candidate.get("source_queries", [])
        )
        existing["search_providers"] = unique_strings(
            existing.get("search_providers", []) + candidate.get("search_providers", [])
        )
        existing["match_count"] = int(existing.get("match_count", 0)) + int(candidate.get("match_count", 0))
        existing["timestamps"] = (existing.get("timestamps", []) or []) + (candidate.get("timestamps", []) or [])
        if len(str(candidate.get("ai_summary", ""))) > len(str(existing.get("ai_summary", ""))):
            existing["ai_summary"] = candidate.get("ai_summary", "")

    ranked = list(by_id.values())
    relevance_checked: list[dict[str, Any]] = []
    for candidate in ranked:
        metadata_relevance = candidate_metadata_relevance(
            candidate,
            required_terms=relevance_required_terms,
            query_terms=candidate.get("source_queries", []),
            exclude_terms=exclude_terms,
            min_score=min_relevance_score,
        )
        candidate["metadata_relevance"] = metadata_relevance
        if pre_download_relevance and relevance_required_terms and not metadata_relevance.get("is_relevant"):
            filtered.append(
                {
                    "record_type": "rejected_candidate",
                    "id": candidate.get("id"),
                    "video_id": candidate.get("video_id") or candidate.get("id"),
                    "title": candidate.get("title"),
                    "channel": candidate.get("channel"),
                    "duration": candidate.get("duration", 0),
                    "status": "filtered_metadata_relevance",
                    "source_queries": candidate.get("source_queries", []),
                    "search_providers": candidate.get("search_providers", []),
                    "metadata_relevance": metadata_relevance,
                    "generated_at": now_iso(),
                }
            )
            continue

        candidate["relevance_score"] = score_candidate(candidate, focus_terms) + float(
            metadata_relevance.get("score", 0)
        )
        if candidate.get("search_providers"):
            candidate["search_provider"] = candidate["search_providers"][0]
        relevance_checked.append(candidate)

    relevance_checked.sort(
        key=lambda row: (row.get("relevance_score", 0), row.get("duration", 0)),
        reverse=True,
    )
    return relevance_checked, filtered


def write_youtube_search_status(
    ticker: str,
    queries: list[str],
    statuses: list[dict[str, Any]],
    search_provider_order: list[str],
) -> None:
    output_dir = youtube_metadata_dir(ticker)
    rapidapi_search_calls = sum(
        1
        for row in statuses
        if row.get("provider") == "rapidapi_metadata_search"
        and row.get("record_type") != "rejected_candidate"
        and row.get("status") not in {"skipped_missing_key", "skipped_provider_disabled"}
    )
    payload = {
        "ticker": ticker,
        "generated_at": now_iso(),
        "queries": queries,
        "search_provider_order": search_provider_order,
        "rapidapi_key_present": bool(RAPIDAPI_KEY),
        "api_request_counts": {
            "rapidapi_metadata_search_calls": rapidapi_search_calls,
        },
        "statuses": statuses,
    }
    (output_dir / "_youtube_search_status.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def write_youtube_candidates(ticker: str, candidates: list[dict[str, Any]]) -> None:
    output_dir = youtube_metadata_dir(ticker)
    (output_dir / "_youtube_candidates.json").write_text(
        json.dumps(candidates, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def write_youtube_rejected_candidates(ticker: str, rejected: list[dict[str, Any]]) -> None:
    output_dir = youtube_metadata_dir(ticker)
    (output_dir / "_youtube_rejected_candidates.json").write_text(
        json.dumps(rejected, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def write_youtube_dry_run_plan(
    ticker: str,
    queries: list[str],
    search_provider_order: list[str],
    transcript_provider_order: list[str],
    query_map_path: Path,
) -> None:
    output_dir = youtube_metadata_dir(ticker)
    payload = {
        "ticker": ticker,
        "generated_at": now_iso(),
        "dry_run": True,
        "query_map": str(query_map_path),
        "queries": queries,
        "search_provider_order": search_provider_order,
        "transcript_provider_order": transcript_provider_order,
        "rapidapi_key_present": bool(RAPIDAPI_KEY),
        "note": "dry-run does not call RapidAPI, yt-dlp, or overwrite collection status",
    }
    (output_dir / "_youtube_dry_run_plan.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def write_youtube_status(
    ticker: str,
    results: list[dict[str, Any]],
    queries: list[str],
    search_provider_order: list[str] | None = None,
    transcript_provider_order: list[str] | None = None,
    dry_run: bool = False,
) -> None:
    output_dir = youtube_metadata_dir(ticker)
    failures = [row for row in results if not row.get("chars")]
    rapidapi_transcript_calls = 0
    for row in results:
        for attempt in row.get("provider_attempts", []) or []:
            if attempt.get("provider") != "rapidapi_transcript3":
                continue
            if attempt.get("status") in {"skipped_missing_key", "skipped_provider_disabled"}:
                continue
            rapidapi_transcript_calls += 1
    status = {
        "ticker": ticker,
        "generated_at": now_iso(),
        "dry_run": dry_run,
        "queries": queries,
        "search_provider_order": search_provider_order or [],
        "transcript_provider_order": transcript_provider_order or [],
        "rapidapi_key_present": bool(RAPIDAPI_KEY),
        "total_records": len(results),
        "success_records": len(results) - len(failures),
        "failure_records": len(failures),
        "total_chars": sum(row.get("chars", 0) for row in results),
        "api_request_counts": {
            "rapidapi_transcript3_calls": rapidapi_transcript_calls,
        },
        "statuses": results,
    }
    (output_dir / "_youtube_collection_status.json").write_text(
        json.dumps(status, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    (output_dir / "_youtube_collection_failures.json").write_text(
        json.dumps(failures, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def existing_youtube_transcript(ticker: str, video_id: str) -> str:
    output_dirs = [youtube_transcripts_dir(ticker), youtube_output_dir(ticker)]
    needle = f"https://www.youtube.com/watch?v={video_id}"
    for output_dir in output_dirs:
        if not output_dir.exists():
            continue
        for path in output_dir.glob("*.md"):
            try:
                if needle in path.read_text(encoding="utf-8", errors="ignore")[:2500]:
                    return str(path)
            except Exception:
                continue
    return ""


def save_youtube_transcript(
    ticker: str,
    video_id: str,
    title: str,
    channel: str,
    date_str: str,
    transcript: str,
    language: str = "",
    target: dict[str, Any] | None = None,
    transcript_provider: str = "",
    transcript_method: str = "",
    search_provider: str = "",
    search_providers: list[str] | None = None,
    source_queries: list[str] | None = None,
    segments: list[dict[str, Any]] | None = None,
    provider_attempts: list[dict[str, Any]] | None = None,
) -> Path:
    """Save a YouTube transcript as markdown and write a segments sidecar when available."""
    sources_dir = youtube_transcripts_dir(ticker, target)
    metadata_dir = youtube_metadata_dir(ticker, target)
    date_str = normalize_date(date_str) or datetime.now().strftime("%Y-%m-%d")
    filename = f"{date_str}_{safe_filename(title, 55)}.md"
    filepath = sources_dir / filename
    segments_file = metadata_dir / filepath.with_suffix(".segments.json").name
    url = f"https://www.youtube.com/watch?v={video_id}"
    source_queries = source_queries or []
    search_providers = search_providers or ([search_provider] if search_provider else [])
    segments = segments or []

    if segments:
        segments_payload = {
            "ticker": ticker,
            "video_id": video_id,
            "url": url,
            "title": title,
            "channel": channel,
            "source_queries": source_queries,
            "transcript_provider": transcript_provider,
            "transcript_method": transcript_method,
            "fetched_at": now_iso(),
            "segments": segments,
        }
        segments_file.write_text(
            json.dumps(segments_payload, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
    else:
        segments_file = Path("")

    fetched_at = now_iso()
    content = f"""---
ticker: {ticker}
type: youtube
title: {json.dumps(title, ensure_ascii=False)}
channel: {json.dumps(channel, ensure_ascii=False)}
date: {date_str}
url: {url}
{_frontmatter_extra(target)}source: youtube
video_id: {video_id}
transcript_provider: {transcript_provider}
transcript_method: {transcript_method}
search_provider: {search_provider}
search_providers: {json.dumps(search_providers, ensure_ascii=False)}
source_queries: {json.dumps(source_queries, ensure_ascii=False)}
language: {language or "unknown"}
chars: {len(transcript)}
segments_file: {segments_file.name if segments_file else ""}
fetched_at: {fetched_at}
---

# {title}

## 视频信息
- **频道**: {channel}
- **日期**: {date_str}
- **链接**: {url}
- **搜索词**: {", ".join(source_queries)}
- **Transcript provider**: {transcript_provider} / {transcript_method}

## 转录全文

{transcript}
"""

    filepath.write_text(content, encoding="utf-8")

    if provider_attempts:
        attempts_file = metadata_dir / filepath.with_suffix(".providers.json").name
        attempts_file.write_text(
            json.dumps(
                {
                    "video_id": video_id,
                    "title": title,
                    "provider_attempts": provider_attempts,
                    "fetched_at": fetched_at,
                },
                ensure_ascii=False,
                indent=2,
            ),
            encoding="utf-8",
        )
    return filepath


def fetch_youtube_for_company(
    ticker: str,
    company_name: str,
    max_videos: int = 15,
    queries: list[str] | None = None,
    query_max_results: int | None = None,
    target: dict[str, Any] | None = None,
    dry_run: bool = False,
    search_provider_order: str | list[str] | None = None,
    transcript_provider_order: str | list[str] | None = None,
    max_queries: int | None = None,
) -> list[dict[str, Any]]:
    """Full pipeline: query map -> candidate search -> transcript fetch -> markdown."""
    print(f"[YouTube] Researching {ticker} ({company_name})...")
    channel_cfg = get_channel(target, "youtube") if target else {}
    search_order = parse_provider_order(
        search_provider_order if search_provider_order is not None else channel_cfg.get("search_provider_order"),
        DEFAULT_SEARCH_PROVIDER_ORDER,
        SUPPORTED_SEARCH_PROVIDERS,
    )
    transcript_order = parse_provider_order(
        transcript_provider_order
        if transcript_provider_order is not None
        else channel_cfg.get("transcript_provider_order"),
        DEFAULT_TRANSCRIPT_PROVIDER_ORDER,
        SUPPORTED_TRANSCRIPT_PROVIDERS,
    )
    if query_max_results is None:
        query_max_results = int(channel_cfg.get("max_candidates_per_query", channel_cfg.get("query_max_results", 5)))
    min_duration_min = float(channel_cfg.get("min_duration_min", 0) or 0)
    pre_download_relevance = bool(channel_cfg.get("pre_download_relevance", True if target else False))
    min_relevance_score = float(channel_cfg.get("relevance_min_score", 3) or 3)

    final_queries, inherited_path, inherited_queries = build_youtube_queries(
        ticker,
        company_name,
        queries,
        target,
        max_queries,
    )
    query_map_path = write_youtube_query_map(
        ticker,
        company_name,
        final_queries,
        inherited_path,
        inherited_queries,
        search_order,
        transcript_order,
        channel_cfg,
        target,
    )
    print(f"  Query map: {query_map_path}")
    print(f"  Search providers: {', '.join(search_order)}")
    print(f"  Transcript providers: {', '.join(transcript_order)}")
    print(f"  Pre-download relevance: {pre_download_relevance}")

    if dry_run:
        print("  Dry run: 不调用 RapidAPI / yt-dlp，只写 query map 和 dry-run plan，不覆盖真实 collection status。")
        write_youtube_dry_run_plan(ticker, final_queries, search_order, transcript_order, query_map_path)
        return []

    all_candidates: list[dict[str, Any]] = []
    search_statuses: list[dict[str, Any]] = []
    disabled_search_providers: set[str] = set()

    for query in final_queries:
        print(f"  搜索: {query}")
        candidates, statuses = search_youtube_candidates(
            query,
            max_results=query_max_results,
            provider_order=search_order,
            cfg=channel_cfg,
            disabled_providers=disabled_search_providers,
        )
        search_statuses.extend(statuses)
        all_candidates.extend(candidates)
        print(f"    找到 {len(candidates)} 个候选")

    focus_terms = build_alias_query_terms(target, include_people=True) if target else [company_name, ticker]
    relevance_required_terms = build_relevance_required_terms(target, company_name, ticker, channel_cfg)
    exclude_terms = (target or {}).get("exclude_terms", []) if target else []
    ranked_candidates, filtered = dedupe_and_rank_candidates(
        all_candidates,
        focus_terms=focus_terms,
        min_duration_min=min_duration_min,
        relevance_required_terms=relevance_required_terms,
        exclude_terms=exclude_terms,
        pre_download_relevance=pre_download_relevance,
        min_relevance_score=min_relevance_score,
    )
    for row in filtered:
        search_statuses.append(row)

    write_youtube_search_status(ticker, final_queries, search_statuses, search_order)
    write_youtube_candidates(ticker, ranked_candidates)
    write_youtube_rejected_candidates(ticker, filtered)

    selected_videos = ranked_candidates[:max_videos]
    print(
        f"\n  共 {len(ranked_candidates)} 个通过 relevance 的独立候选，"
        f"过滤 {len(filtered)} 个，选前 {len(selected_videos)} 个提取 transcript..."
    )

    results: list[dict[str, Any]] = []
    disabled_transcript_providers: set[str] = set()
    for index, video in enumerate(selected_videos):
        video_id = video["video_id"]
        title = video.get("title", f"Video_{video_id}")
        channel = video.get("channel", "Unknown")
        date_str = video.get("date", "")
        url = video.get("url") or f"https://www.youtube.com/watch?v={video_id}"

        print(f"  [{index + 1}/{len(selected_videos)}] {title[:60]}...")

        existing_path = existing_youtube_transcript(ticker, video_id)
        if existing_path:
            print("    ⏭ existing transcript")
            results.append(
                {
                    "id": video_id,
                    "video_id": video_id,
                    "title": title,
                    "chars": Path(existing_path).stat().st_size,
                    "file": existing_path,
                    "status": "existing_success",
                    "source_queries": video.get("source_queries", []),
                    "search_provider": video.get("search_provider", ""),
                }
            )
            write_youtube_status(
                ticker,
                results,
                final_queries,
                search_provider_order=search_order,
                transcript_provider_order=transcript_order,
            )
            continue

        transcript_result, provider_attempts = fetch_transcript_with_providers(
            video_id,
            url,
            transcript_order,
            disabled_providers=disabled_transcript_providers,
        )
        if transcript_result:
            transcript = transcript_result["text"]
            filepath = save_youtube_transcript(
                ticker,
                video_id,
                title,
                channel,
                date_str,
                transcript,
                language=transcript_result.get("language", ""),
                target=target,
                transcript_provider=transcript_result.get("transcript_provider", ""),
                transcript_method=transcript_result.get("transcript_method", ""),
                search_provider=video.get("search_provider", ""),
                search_providers=video.get("search_providers", []),
                source_queries=video.get("source_queries", []),
                segments=transcript_result.get("segments", []),
                provider_attempts=provider_attempts,
            )
            print(f"    ✓ {len(transcript):,} chars → {filepath.name}")
            results.append(
                {
                    "id": video_id,
                    "video_id": video_id,
                    "title": title,
                    "chars": len(transcript),
                    "file": str(filepath),
                    "status": "success",
                    "transcript_method": transcript_result.get("transcript_method", ""),
                    "transcript_provider": transcript_result.get("transcript_provider", ""),
                    "search_provider": video.get("search_provider", ""),
                    "source_queries": video.get("source_queries", []),
                    "provider_attempts": provider_attempts,
                }
            )
        else:
            print("    ✗ 无完整 transcript")
            results.append(
                {
                    "id": video_id,
                    "video_id": video_id,
                    "title": title,
                    "status": "no_transcript",
                    "error": "all_transcript_providers_failed",
                    "search_provider": video.get("search_provider", ""),
                    "source_queries": video.get("source_queries", []),
                    "provider_attempts": provider_attempts,
                }
            )

        write_youtube_status(
            ticker,
            results,
            final_queries,
            search_provider_order=search_order,
            transcript_provider_order=transcript_order,
        )

    success = sum(1 for row in results if row.get("chars"))
    total_chars = sum(row.get("chars", 0) for row in results)
    print(f"\n  完成: {success}/{len(selected_videos)} 成功, 共 {total_chars:,} 字符")
    write_youtube_status(
        ticker,
        results,
        final_queries,
        search_provider_order=search_order,
        transcript_provider_order=transcript_order,
    )
    return results


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("ticker", nargs="?")
    parser.add_argument("company_name", nargs="?")
    parser.add_argument("--target", dest="target_name")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--max-queries", type=int)
    parser.add_argument("--max-videos", type=int)
    parser.add_argument("--query-max-results", type=int)
    parser.add_argument("--search-provider-order")
    parser.add_argument("--transcript-provider-order")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.target_name:
        if not load_target:
            raise RuntimeError("target_config.py is required for --target")
        target = load_target(args.target_name)
        key = target_key(target)
        channel_cfg = get_channel(target, "youtube")
        fetch_youtube_for_company(
            key,
            target.get("company_name", key),
            max_videos=args.max_videos if args.max_videos is not None else int(channel_cfg.get("max_videos", 15)),
            queries=get_channel_queries(target, "youtube"),
            query_max_results=args.query_max_results,
            target=target,
            dry_run=args.dry_run,
            search_provider_order=args.search_provider_order,
            transcript_provider_order=args.transcript_provider_order,
            max_queries=args.max_queries,
        )
    else:
        if not args.ticker:
            print("Usage: python fetch_youtube.py TICKER [COMPANY_NAME]")
            print("   or: python fetch_youtube.py --target TARGET_KEY")
            sys.exit(1)
        ticker = args.ticker
        company_name = args.company_name if args.company_name else ticker
        fetch_youtube_for_company(
            ticker,
            company_name,
            max_videos=args.max_videos if args.max_videos is not None else 15,
            query_max_results=args.query_max_results if args.query_max_results is not None else 5,
            dry_run=args.dry_run,
            search_provider_order=args.search_provider_order,
            transcript_provider_order=args.transcript_provider_order,
            max_queries=args.max_queries,
        )


if __name__ == "__main__":
    main()
