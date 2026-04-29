"""Book discovery for company/founder coverage."""

from __future__ import annotations

from datetime import datetime
from typing import Any
from urllib.parse import quote_plus

import requests

from .common import PublicCompanyTarget, write_json, write_markdown, write_probe_report


HEADERS = {"User-Agent": "AIOrgResearchBot/1.0"}


def _query_openlibrary(query: str, limit: int = 5) -> list[dict[str, Any]]:
    url = f"https://openlibrary.org/search.json?q={quote_plus(query)}&limit={limit}"
    response = requests.get(url, headers=HEADERS, timeout=6)
    response.raise_for_status()
    data = response.json()
    results = []
    for doc in data.get("docs", [])[:limit]:
        results.append(
            {
                "title": doc.get("title"),
                "author": ", ".join(doc.get("author_name", [])[:3]),
                "first_publish_year": doc.get("first_publish_year"),
                "source": "openlibrary",
                "source_url": f"https://openlibrary.org{doc.get('key')}" if doc.get("key") else url,
            }
        )
    return results


def _query_google_books(query: str, limit: int = 5) -> list[dict[str, Any]]:
    url = f"https://www.googleapis.com/books/v1/volumes?q={quote_plus(query)}&maxResults={limit}"
    response = requests.get(url, headers=HEADERS, timeout=6)
    response.raise_for_status()
    data = response.json()
    results = []
    for item in data.get("items", [])[:limit]:
        info = item.get("volumeInfo", {})
        results.append(
            {
                "title": info.get("title"),
                "subtitle": info.get("subtitle"),
                "author": ", ".join(info.get("authors", [])[:3]),
                "published_date": info.get("publishedDate"),
                "description": info.get("description", ""),
                "source": "google_books",
                "source_url": info.get("infoLink"),
            }
        )
    return results


def _relevant(book: dict[str, Any], terms: list[str]) -> bool:
    haystack = " ".join(str(book.get(key, "")) for key in ["title", "subtitle", "author", "description"]).lower()
    return any(term.lower() in haystack for term in terms if term)


def collect_books(target: PublicCompanyTarget, limit_per_query: int = 3, max_queries: int = 6) -> dict[str, Any]:
    processed_dir = target.public_company_root / "processed" / "books"
    company_terms = [target.company_name, target.ticker, *target.aliases]
    founders = target.config.get("founders", []) or []
    executives = target.config.get("executives", []) or []
    queries = [
        f'"{target.company_name}" company book',
        f'"{target.company_name}" biography',
        f'"{target.company_name}" founder',
        *[f'"{name}" "{target.company_name}" book' for name in founders[:4]],
        *[f'"{name}" "{target.company_name}" interview book' for name in executives[:3]],
    ]
    queries = queries[:max_queries]
    books: list[dict[str, Any]] = []
    query_log: list[dict[str, Any]] = []
    for query in queries:
        row = {"query": query, "sources": []}
        for source_name, fn in [("openlibrary", _query_openlibrary), ("google_books", _query_google_books)]:
            try:
                found = fn(query, limit_per_query)
                row["sources"].append({"source": source_name, "count": len(found)})
                for item in found:
                    item["query"] = query
                books.extend(found)
            except Exception as exc:  # noqa: BLE001
                row["sources"].append({"source": source_name, "error": str(exc)})
        query_log.append(row)

    deduped: list[dict[str, Any]] = []
    seen: set[tuple[str, str]] = set()
    relevance_terms = [target.company_name, target.ticker, "SanDisk", "Sandisk", *founders, *executives]
    for book in books:
        key = (str(book.get("title", "")).lower(), str(book.get("author", "")).lower())
        if key in seen or not book.get("title"):
            continue
        seen.add(key)
        if _relevant(book, relevance_terms):
            deduped.append(book)

    payload = {
        "company": target.company_name,
        "ticker": target.ticker,
        "status": "ok" if deduped else "none_found",
        "books": deduped,
        "raw_candidates": books,
        "query_log": query_log,
        "updated_at": datetime.now().isoformat(timespec="seconds"),
    }
    write_json(processed_dir / "company_books.json", payload)
    lines = [f"# {target.company_name} Books", ""]
    if deduped:
        for book in deduped:
            title = book.get("title", "Untitled")
            author = book.get("author") or "unknown author"
            source = book.get("source_url") or ""
            lines.append(f"- {title} — {author} ({book.get('source')}) {source}")
    else:
        lines.append("none found / query log retained in `company_books.json`")
    lines.extend(["", "## Query Log"])
    lines.extend(f"- {row['query']}" for row in query_log)
    write_markdown(processed_dir / "company_books.md", lines)
    status = {"status": payload["status"], "items": deduped, "gaps": [] if deduped else [{"reason": "no_high_confidence_company_books_found"}]}
    write_probe_report(target, "books", status)
    return status
