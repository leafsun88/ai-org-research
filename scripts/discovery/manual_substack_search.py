"""Manual/public-search Substack discovery.

This is the no-Perplexity fallback for Substack/newsletter discovery.

It does three things:
1. Build a target-specific query map from the manifest and podcast query map.
2. Search public web result pages (DuckDuckGo/Bing) for candidate URLs.
3. Optionally fetch accessible public pages and save them into the standard
   staging/vault Substack layout.

It never fabricates URLs and it never requires a paid search API key. If public
search blocks a query, pass a newline-separated URL file with --url-file and the
script will still de-dupe, score, fetch, and sync those URLs.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import shutil
import time
from datetime import datetime
from pathlib import Path
from typing import Any
from urllib.parse import parse_qs, quote_plus, unquote, urlparse

import requests

from fetch_perplexity import fetch_full_text
from target_config import (
    PROJECT_ROOT,
    build_alias_query_terms,
    get_channel,
    get_channel_queries,
    load_target,
    target_key,
    target_script_root,
    target_vault_root,
)


HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.8",
}

SEARCH_PROVIDERS = {"duckduckgo", "bing"}
PAYWALL_HINTS = {
    "subscribe to continue reading",
    "this post is for paid subscribers",
    "paid subscribers",
    "sign in to continue",
    "members only",
}


def metadata_dir(target: dict[str, Any]) -> Path:
    path = target_script_root(target) / "sources" / "substack" / "metadata"
    path.mkdir(parents=True, exist_ok=True)
    return path


def transcripts_dir(target: dict[str, Any]) -> Path:
    path = target_script_root(target) / "sources" / "substack" / "transcripts"
    path.mkdir(parents=True, exist_ok=True)
    return path


def vault_metadata_dir(target: dict[str, Any]) -> Path:
    path = target_vault_root(target) / "substack" / "metadata"
    path.mkdir(parents=True, exist_ok=True)
    return path


def vault_transcripts_dir(target: dict[str, Any]) -> Path:
    path = target_vault_root(target) / "substack" / "transcripts"
    path.mkdir(parents=True, exist_ok=True)
    return path


def clean_text(value: str) -> str:
    value = html.unescape(re.sub(r"<[^>]+>", " ", value or ""))
    return re.sub(r"\s+", " ", value).strip()


def safe_filename(value: str, fallback: str = "source") -> str:
    value = re.sub(r"[^A-Za-z0-9\s-]", "", value or "")[:80].strip()
    value = re.sub(r"\s+", "_", value).lower()
    return value or fallback


def canonical_url(url: str) -> str:
    url = html.unescape((url or "").strip())
    if url.startswith("//"):
        url = "https:" + url
    parsed = urlparse(url)
    if "duckduckgo.com" in parsed.netloc and parsed.path.startswith("/l/"):
        values = parse_qs(parsed.query).get("uddg")
        if values:
            url = unquote(values[0])
    return url.split("#", 1)[0].rstrip("/")


def domain(url: str) -> str:
    return urlparse(url).netloc.lower().removeprefix("www.")


def looks_like_substack_or_newsletter(url: str) -> bool:
    d = domain(url)
    return (
        d == "substack.com"
        or d.endswith(".substack.com")
        or "substack.com" in url
        or d.endswith(".beehiiv.com")
        or d.endswith(".ghost.io")
        or d in {"productgrowth.blog", "every.to", "notboring.co"}
    )


def parse_podcast_query_map(path: Path) -> list[str]:
    if not path.exists():
        return []
    queries: list[str] = []
    in_query_section = False
    for raw in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = raw.strip()
        if line.startswith("## "):
            in_query_section = line.lower() in {
                "## 搜索 query",
                "## search queries",
                "## podcast queries",
                "## 给 youtube / substack / web 复用的 query",
                "## queries",
            }
            continue
        if in_query_section and line.startswith("- "):
            value = line[2:].strip()
            if value and value != "N/A":
                queries.append(value)
    return unique(queries)


def read_podcast_query_map(target: dict[str, Any]) -> tuple[list[str], str]:
    candidates = [
        target_vault_root(target) / "podcasts" / "metadata" / "_podcast_query_map.md",
        target_script_root(target) / "sources" / "podcasts" / "metadata" / "_podcast_query_map.md",
    ]
    for path in candidates:
        queries = parse_podcast_query_map(path)
        if queries:
            return queries, str(path)
    return [], ""


def unique(values: list[str]) -> list[str]:
    result: list[str] = []
    seen: set[str] = set()
    for value in values:
        clean = str(value or "").strip()
        key = clean.lower()
        if clean and key not in seen:
            seen.add(key)
            result.append(clean)
    return result


def build_queries(target: dict[str, Any], max_queries: int = 0) -> tuple[list[str], str, list[str]]:
    inherited, inherited_path = read_podcast_query_map(target)
    configured = get_channel_queries(target, "substack")
    company = target.get("company_name", target_key(target))
    aliases = build_alias_query_terms(target)[:10]
    fallback = [
        f"{company} Substack",
        f"{company} founder Substack",
        f"{company} revenue ARR Substack",
        f"{company} lawsuit Substack",
    ]
    for alias in aliases:
        if alias.lower() != str(company).lower():
            fallback.append(f"{alias} Substack")
    base = unique(configured + inherited + fallback)
    expanded: list[str] = []
    for query in base:
        q = query.strip()
        if not q:
            continue
        expanded.extend([
            f"site:substack.com/p {q}",
            f"site:substack.com {q}",
            f"{q} newsletter analysis",
        ])
    expanded = unique(expanded)
    if max_queries > 0:
        expanded = expanded[:max_queries]
    return expanded, inherited_path, inherited


def write_query_map(
    target: dict[str, Any],
    queries: list[str],
    inherited_path: str,
    inherited_count: int,
) -> Path:
    path = metadata_dir(target) / "_manual_substack_query_map.md"
    lines = [
        "---",
        f"company: {json.dumps(target.get('company_name', ''))}",
        f"research_key: {target_key(target)}",
        "type: manual_substack_query_map",
        f"generated_at: {datetime.now().isoformat(timespec='seconds')}",
        "---",
        "",
        f"# Manual Substack Query Map: {target.get('company_name', target_key(target))}",
        "",
        "## Inherited Podcast Query Map",
        "",
        f"- path: {inherited_path or 'none'}",
        f"- inherited_query_count: {inherited_count}",
        "",
        "## Final Search Queries",
        "",
    ]
    lines.extend(f"- {query}" for query in queries)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def search_duckduckgo(query: str, limit: int) -> list[dict[str, Any]]:
    url = "https://duckduckgo.com/html/"
    response = requests.get(url, params={"q": query}, headers=HEADERS, timeout=20)
    response.raise_for_status()
    html_text = response.text
    matches = re.findall(
        r'<a[^>]+class="result__a"[^>]+href="([^"]+)"[^>]*>(.*?)</a>',
        html_text,
        flags=re.I | re.S,
    )
    results = []
    for href, title_html in matches[:limit]:
        results.append({
            "url": canonical_url(href),
            "title": clean_text(title_html),
            "provider": "duckduckgo",
            "query": query,
        })
    return results


def search_bing(query: str, limit: int) -> list[dict[str, Any]]:
    url = "https://www.bing.com/search"
    response = requests.get(url, params={"q": query}, headers=HEADERS, timeout=20)
    response.raise_for_status()
    html_text = response.text
    matches = re.findall(
        r'<li[^>]+class="b_algo"[^>]*>.*?<a[^>]+href="(http[^"]+)"[^>]*>(.*?)</a>',
        html_text,
        flags=re.I | re.S,
    )
    results = []
    for href, title_html in matches[:limit]:
        results.append({
            "url": canonical_url(href),
            "title": clean_text(title_html),
            "provider": "bing",
            "query": query,
        })
    return results


def search_provider(provider: str, query: str, limit: int) -> list[dict[str, Any]]:
    if provider == "duckduckgo":
        return search_duckduckgo(query, limit)
    if provider == "bing":
        return search_bing(query, limit)
    raise ValueError(f"Unknown search provider: {provider}")


def read_manual_urls(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        raise FileNotFoundError(path)
    items = []
    for line_no, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        match = re.search(r"https?://\S+", line)
        if not match:
            continue
        url = canonical_url(match.group(0).rstrip(").,;"))
        title = line.replace(match.group(0), "").strip(" \t-|,")
        items.append({
            "url": url,
            "title": title or url.rstrip("/").split("/")[-1],
            "provider": "manual_url_file",
            "query": f"{path}:{line_no}",
        })
    return items


def relevance_terms(target: dict[str, Any]) -> list[str]:
    cfg = get_channel(target, "substack")
    terms = []
    terms.extend(cfg.get("relevance_terms", []))
    terms.extend(build_alias_query_terms(target))
    terms.extend(target.get("founders", []))
    terms.extend(target.get("executives", []))
    return unique([str(term) for term in terms])


def score_candidate(item: dict[str, Any], target: dict[str, Any]) -> dict[str, Any]:
    text = " ".join([
        item.get("title", ""),
        item.get("url", ""),
    ]).lower()
    hits = []
    score = 0
    for term in relevance_terms(target):
        clean = term.strip()
        if not clean:
            continue
        if clean.lower() in text:
            hits.append(clean)
            score += 3 if len(clean.split()) > 1 else 1
    if looks_like_substack_or_newsletter(item.get("url", "")):
        score += 4
        hits.append("newsletter_domain")
    if "/p/" in item.get("url", ""):
        score += 1
    item["relevance_score"] = score
    item["relevance_hits"] = unique(hits)
    return item


def dedupe_candidates(items: list[dict[str, Any]]) -> list[dict[str, Any]]:
    seen: dict[str, dict[str, Any]] = {}
    for item in items:
        url = canonical_url(item.get("url", ""))
        if not url.startswith("http"):
            continue
        parsed = urlparse(url)
        if parsed.netloc.endswith("duckduckgo.com") or parsed.netloc.endswith("bing.com"):
            continue
        item["url"] = url
        key = url.lower().removesuffix("/")
        if key not in seen:
            seen[key] = item
            continue
        existing = seen[key]
        existing["queries"] = unique(
            existing.get("queries", [existing.get("query", "")]) + [item.get("query", "")]
        )
        existing["providers"] = unique(
            existing.get("providers", [existing.get("provider", "")]) + [item.get("provider", "")]
        )
    return list(seen.values())


def discover(
    target: dict[str, Any],
    providers: list[str],
    max_queries: int,
    results_per_query: int,
    strict_substack: bool,
    url_file: Path | None,
    no_search: bool,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], Path]:
    queries, inherited_path, inherited = build_queries(target, max_queries=max_queries)
    query_map = write_query_map(target, queries, inherited_path, len(inherited))
    statuses: list[dict[str, Any]] = []
    candidates: list[dict[str, Any]] = []

    if url_file:
        manual_items = read_manual_urls(url_file)
        candidates.extend(manual_items)
        statuses.append({
            "provider": "manual_url_file",
            "query": str(url_file),
            "status": "success",
            "returned": len(manual_items),
        })

    if not no_search:
        for i, query in enumerate(queries, 1):
            print(f"  query {i}/{len(queries)}: {query}")
            for provider in providers:
                try:
                    found = search_provider(provider, query, results_per_query)
                    if strict_substack:
                        found = [item for item in found if "substack.com" in item.get("url", "")]
                    else:
                        found = [
                            item for item in found
                            if looks_like_substack_or_newsletter(item.get("url", ""))
                            or any(term.lower() in (item.get("title", "") + item.get("url", "")).lower()
                                   for term in build_alias_query_terms(target)[:6])
                        ]
                    candidates.extend(found)
                    statuses.append({
                        "provider": provider,
                        "query": query,
                        "status": "success",
                        "returned": len(found),
                    })
                    time.sleep(0.5)
                except Exception as exc:
                    statuses.append({
                        "provider": provider,
                        "query": query,
                        "status": "failed",
                        "error": str(exc)[:300],
                        "returned": 0,
                    })
                    time.sleep(0.5)

    scored = [score_candidate(item, target) for item in dedupe_candidates(candidates)]
    scored.sort(key=lambda item: (item.get("relevance_score", 0), item.get("title", "")), reverse=True)
    return scored, statuses, query_map


def is_likely_paywalled(text: str) -> bool:
    lower = text.lower()
    return any(hint in lower for hint in PAYWALL_HINTS)


def fetch_reader_text(url: str, timeout: int = 30) -> dict[str, Any]:
    """Fetch public markdown via Jina Reader as a fallback."""
    reader_url = f"https://r.jina.ai/http://{url}"
    try:
        # Jina Reader may reject browser-like Accept headers with 403. Keep this
        # request deliberately plain so it behaves like a simple markdown fetch.
        response = requests.get(
            reader_url,
            headers={"Accept": "text/plain"},
            timeout=timeout,
        )
        if response.status_code != 200:
            return {"success": False, "error": f"reader_http_{response.status_code}", "url": url}
        text = response.text.strip()
        if len(text) < 300:
            return {"success": False, "error": "reader_content_too_short", "url": url, "text": text}
        return {
            "success": True,
            "text": text,
            "url": url,
            "chars": len(text),
            "reader_url": reader_url,
        }
    except requests.Timeout:
        return {"success": False, "error": "reader_timeout", "url": url}
    except Exception as exc:
        return {"success": False, "error": f"reader_error: {exc}", "url": url}


def save_markdown(target: dict[str, Any], item: dict[str, Any], text: str, index: int) -> Path:
    url = item.get("url", "")
    title = item.get("title") or url.rstrip("/").split("/")[-1] or f"source {index}"
    date = item.get("date") or "unknown"
    path = transcripts_dir(target) / f"{safe_filename(str(date), 'unknown')}_{safe_filename(title, f'source_{index}')}.md"
    content = f"""---
company: {json.dumps(target.get("company_name", ""))}
research_key: {target_key(target)}
type: substack
source: {json.dumps(domain(url))}
title: {json.dumps(title)}
url: {url}
date: {date}
fetched_at: {datetime.now().isoformat(timespec="seconds")}
discovery_provider: {json.dumps(item.get("provider", ""))}
relevance_score: {item.get("relevance_score", 0)}
credibility: S3-S4
evidence: E2-E3
chars: {len(text)}
---

# {title}

**Source**: {url}
**Discovery query**: {item.get("query", "")}

---

{text}
"""
    path.write_text(content, encoding="utf-8")
    return path


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def read_existing_candidates(target: dict[str, Any]) -> list[dict[str, Any]]:
    path = metadata_dir(target) / "_manual_substack_candidates.json"
    if not path.exists():
        return []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return []
    return data if isinstance(data, list) else []


def fetch_candidates(
    target: dict[str, Any],
    candidates: list[dict[str, Any]],
    min_score: int,
    skip_fetch: bool,
    max_fetch: int,
    reader_fallback: bool,
) -> list[dict[str, Any]]:
    statuses = []
    eligible = [item for item in candidates if int(item.get("relevance_score", 0)) >= min_score]
    if max_fetch > 0:
        eligible = eligible[:max_fetch]
    for i, item in enumerate(candidates, 1):
        if item not in eligible:
            statuses.append({
                "status": "indexed_low_relevance",
                "url": item.get("url", ""),
                "title": item.get("title", ""),
                "relevance_score": item.get("relevance_score", 0),
            })
            continue
        if skip_fetch:
            statuses.append({
                "status": "indexed_only",
                "url": item.get("url", ""),
                "title": item.get("title", ""),
                "relevance_score": item.get("relevance_score", 0),
            })
            continue
        print(f"  fetch {len(statuses)+1}: {item.get('title') or item.get('url')}")
        result = fetch_full_text(item.get("url", ""))
        fetch_method = "direct"
        direct_error = "" if result.get("success") else result.get("error", "unknown")
        reader_error = ""
        if (not result.get("success")) and reader_fallback:
            reader_result = fetch_reader_text(item.get("url", ""))
            if reader_result.get("success"):
                result = reader_result
                fetch_method = "jina_reader"
            else:
                reader_error = reader_result.get("error", "unknown")
        if not result.get("success"):
            statuses.append({
                "status": "fetch_failed",
                "url": item.get("url", ""),
                "title": item.get("title", ""),
                "relevance_score": item.get("relevance_score", 0),
                "error": result.get("error", "unknown"),
                "direct_error": direct_error,
                "reader_error": reader_error,
            })
            time.sleep(0.35)
            continue
        text = result.get("text", "")
        if is_likely_paywalled(text):
            statuses.append({
                "status": "indexed_paywall_or_subscriber_post",
                "url": item.get("url", ""),
                "title": item.get("title", ""),
                "relevance_score": item.get("relevance_score", 0),
                "chars": len(text),
            })
            time.sleep(0.35)
            continue
        path = save_markdown(target, item, text, i)
        statuses.append({
            "status": "success",
            "url": item.get("url", ""),
            "title": item.get("title", ""),
            "relevance_score": item.get("relevance_score", 0),
            "chars": len(text),
            "fetch_method": fetch_method,
            "reader_url": result.get("reader_url", ""),
            "path": str(path),
        })
        time.sleep(0.35)
    return statuses


def sync_to_vault(target: dict[str, Any]) -> dict[str, int]:
    counts = {"metadata": 0, "transcripts": 0}
    for src, dst, key in [
        (metadata_dir(target), vault_metadata_dir(target), "metadata"),
        (transcripts_dir(target), vault_transcripts_dir(target), "transcripts"),
    ]:
        dst.mkdir(parents=True, exist_ok=True)
        for path in src.glob("*"):
            if not path.is_file() or path.name == ".DS_Store":
                continue
            shutil.copy2(path, dst / path.name)
            counts[key] += 1
    return counts


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", required=True)
    parser.add_argument("--providers", default="duckduckgo,bing")
    parser.add_argument("--max-queries", type=int, default=12)
    parser.add_argument("--results-per-query", type=int, default=8)
    parser.add_argument("--min-score", type=int, default=4)
    parser.add_argument("--max-fetch", type=int, default=20)
    parser.add_argument("--skip-fetch", action="store_true")
    parser.add_argument("--no-reader-fallback", action="store_true")
    parser.add_argument("--strict-substack", action="store_true")
    parser.add_argument("--url-file")
    parser.add_argument("--no-search", action="store_true")
    parser.add_argument("--replace-existing", action="store_true")
    parser.add_argument("--sync-vault", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    providers = [p.strip() for p in args.providers.split(",") if p.strip()]
    invalid = [p for p in providers if p not in SEARCH_PROVIDERS]
    if invalid:
        raise SystemExit(f"Unknown providers: {', '.join(invalid)}")

    target = load_target(args.target)
    print(f"[manual-substack] {target_key(target)} ({target.get('company_name', '')})")
    candidates, search_statuses, query_map = discover(
        target=target,
        providers=providers,
        max_queries=args.max_queries,
        results_per_query=args.results_per_query,
        strict_substack=args.strict_substack,
        url_file=Path(args.url_file) if args.url_file else None,
        no_search=args.no_search,
    )

    if not args.replace_existing:
        candidates = [
            score_candidate(item, target)
            for item in dedupe_candidates(read_existing_candidates(target) + candidates)
        ]
        candidates.sort(key=lambda item: (item.get("relevance_score", 0), item.get("title", "")), reverse=True)

    meta = metadata_dir(target)
    write_json(meta / "_manual_substack_candidates.json", candidates)
    write_json(meta / f"_manual_substack_candidates_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json", candidates)
    write_json(meta / "_manual_substack_search_status.json", {
        "research_key": target_key(target),
        "company": target.get("company_name", ""),
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "query_map": str(query_map),
        "candidate_count": len(candidates),
        "statuses": search_statuses,
    })

    if args.dry_run:
        print(f"  dry-run candidates: {len(candidates)}")
        return 0

    statuses = fetch_candidates(
        target=target,
        candidates=candidates,
        min_score=args.min_score,
        skip_fetch=args.skip_fetch,
        max_fetch=args.max_fetch,
        reader_fallback=not args.no_reader_fallback,
    )
    failures = [item for item in statuses if item.get("status") != "success"]
    write_json(meta / "_manual_substack_collection_status.json", {
        "research_key": target_key(target),
        "company": target.get("company_name", ""),
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "total_candidates": len(candidates),
        "total_records": len(statuses),
        "success_records": len(statuses) - len(failures),
        "failure_records": len(failures),
        "statuses": statuses,
    })
    write_json(meta / "_manual_substack_collection_failures.json", failures)

    sync_counts = {}
    if args.sync_vault:
        sync_counts = sync_to_vault(target)

    print(
        "  done: "
        f"{len(candidates)} candidates, "
        f"{len(statuses) - len(failures)} fetched, "
        f"{len(failures)} non-fetched"
    )
    if sync_counts:
        print(f"  synced to vault: {sync_counts}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
