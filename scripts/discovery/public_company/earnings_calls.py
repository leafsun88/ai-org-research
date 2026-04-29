"""IR earnings-call metadata and presentation collection."""

from __future__ import annotations

import re
import shutil
import subprocess
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any
from urllib.parse import urljoin

import requests

from .common import PublicCompanyTarget, relative_to_project, safe_filename, write_json, write_markdown, write_probe_report


HEADERS = {"User-Agent": "AIOrgResearchBot/1.0"}
UNRELATED_PRESENTATION_TERMS = [
    "disruptor in education",
    "schools we serve",
    "virtual public education",
    "enrollment",
    "effective teachers",
]


@dataclass
class _FetchedResponse:
    content: bytes
    url: str
    headers: dict[str, str]

    @property
    def text(self) -> str:
        return self.content.decode("utf-8", errors="ignore")

    def raise_for_status(self) -> None:
        return None


def _get(url: str, timeout: int = 8) -> requests.Response | _FetchedResponse:
    try:
        response = requests.get(url, headers=HEADERS, timeout=timeout)
        response.raise_for_status()
        return response
    except Exception:
        if not shutil.which("curl"):
            raise
        result = subprocess.run(
            [
                "curl",
                "--http1.1",
                "-L",
                "--fail",
                "--max-time",
                str(max(timeout + 20, 30)),
                "-A",
                HEADERS["User-Agent"],
                "-sS",
                url,
            ],
            capture_output=True,
            check=False,
            timeout=max(timeout + 35, 45),
        )
        if result.returncode != 0:
            raise RuntimeError(result.stderr.decode("utf-8", errors="ignore") or f"curl failed for {url}")
        content_type = "application/pdf" if result.stdout[:4] == b"%PDF" else "text/html"
        return _FetchedResponse(result.stdout, url, {"content-type": content_type})


def _links(html: str, base_url: str) -> list[dict[str, str]]:
    results: list[dict[str, str]] = []
    for match in re.finditer(r'(?is)<a\b[^>]*href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', html):
        href = urljoin(base_url, match.group(1))
        label = re.sub(r"(?is)<.*?>", " ", match.group(2))
        label = re.sub(r"\s+", " ", label).strip()
        if href not in {item["url"] for item in results}:
            results.append({"url": href, "label": label})
    for match in re.finditer(r'(?i)(https?://[^"\']+|/static-files/[A-Za-z0-9-]+)', html):
        href = urljoin(base_url, match.group(1))
        if href not in {item["url"] for item in results}:
            results.append({"url": href, "label": ""})
    return results


def _html_to_text(raw: str) -> str:
    text = re.sub(r"(?is)<(script|style).*?>.*?</\1>", " ", raw)
    text = re.sub(r"(?is)<br\s*/?>", "\n", text)
    text = re.sub(r"(?is)</(p|div|h1|h2|h3|li)\s*>", "\n", text)
    text = re.sub(r"(?is)<.*?>", " ", text)
    text = text.replace("&amp;", "&").replace("&nbsp;", " ").replace("&#39;", "'")
    text = re.sub(r"[ \t\r\f\v]+", " ", text)
    text = re.sub(r"\n\s+", "\n", text)
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def _artifact_text_sample(path: Path, content_type: str, limit: int = 12000) -> str:
    if "pdf" in content_type.lower() or path.suffix.lower() == ".pdf":
        if shutil.which("pdftotext"):
            result = subprocess.run(["pdftotext", str(path), "-"], text=True, capture_output=True, timeout=15, check=False)
            return result.stdout[:limit]
        return ""
    return path.read_text(encoding="utf-8", errors="ignore")[:limit]


def _content_identity_check(target: PublicCompanyTarget, path: Path, content_type: str) -> dict[str, Any]:
    text = _artifact_text_sample(path, content_type)
    text_l = text.lower()
    aliases = [target.company_name, target.ticker, *target.aliases]
    alias_hits = sorted({alias for alias in aliases if alias and alias.lower() in text_l})
    forbidden_hits = [term for term in UNRELATED_PRESENTATION_TERMS if term in text_l]
    passed = len(text.strip()) >= 500 and bool(alias_hits) and not forbidden_hits
    return {
        "passed": passed,
        "alias_hits": alias_hits,
        "forbidden_hits": forbidden_hits,
        "text_chars_checked": len(text),
        "sample": re.sub(r"\s+", " ", text[:500]).strip(),
    }


def _fetch_stockanalysis_transcripts(target: PublicCompanyTarget, max_transcripts: int = 3) -> list[dict[str, Any]]:
    ticker = target.ticker.lower()
    index_url = f"https://stockanalysis.com/stocks/{ticker}/transcripts/"
    response = _get(index_url, timeout=12)
    raw_dir = target.public_company_root / "raw_filings" / "earnings_calls"
    processed_dir = target.public_company_root / "processed" / "earnings_calls"
    index_path = raw_dir / "stockanalysis_transcripts_index.html"
    index_path.write_bytes(response.content)
    links = []
    seen: set[str] = set()
    for link in _links(response.text, index_url):
        if f"/stocks/{ticker}/transcripts/" not in link["url"]:
            continue
        if link["url"].rstrip("/") == index_url.rstrip("/"):
            continue
        if "earnings call" not in link.get("label", "").lower():
            continue
        if link["url"] in seen:
            continue
        seen.add(link["url"])
        links.append(link)

    transcripts: list[dict[str, Any]] = []
    for link in links[:max_transcripts]:
        page = _get(link["url"], timeout=15)
        label = safe_filename(link.get("label") or Path(link["url"].rstrip("/")).name)
        html_path = raw_dir / f"{label}_transcript_source.html"
        md_path = processed_dir / f"{label}_transcript.md"
        html_path.write_bytes(page.content)
        text = _html_to_text(page.text)
        start_match = re.search(r"(?is)(full transcript\s+ai summary\s+)?operator\b", text)
        if start_match:
            text = text[start_match.start() :]
        write_markdown(
            md_path,
            [
                "---",
                f"company: {target.company_name}",
                f"ticker: {target.ticker}",
                f"source_url: {link['url']}",
                "source_type: third_party_transcript_fallback",
                "provider: StockAnalysis",
                "---",
                "",
                f"# {link.get('label') or target.company_name + ' transcript'}",
                "",
                text,
            ],
        )
        transcripts.append(
            {
                "label": link.get("label"),
                "source_url": link["url"],
                "raw_html_path": relative_to_project(html_path),
                "processed_path": relative_to_project(md_path),
                "characters": len(text),
                "source_type": "third_party_transcript_fallback",
            }
        )
    return transcripts


def fetch_earnings_calls(target: PublicCompanyTarget, max_downloads: int = 4) -> dict[str, Any]:
    root = target.public_company_root
    raw_dir = root / "raw_filings" / "earnings_calls"
    processed_dir = root / "processed" / "earnings_calls"
    ir_url = (target.ir_url or "").rstrip("/")
    status: dict[str, Any] = {"status": "partial", "items": [], "gaps": []}
    if not ir_url:
        status["gaps"].append({"reason": "ir_url_missing"})
        write_probe_report(target, "earnings_calls_ir", status)
        return status

    pages = [
        ("events", f"{ir_url}/news-events/events"),
        ("presentations", f"{ir_url}/news-events/presentations"),
        ("press_releases", f"{ir_url}/news-releases"),
    ]
    all_links: list[dict[str, Any]] = []
    for page_name, url in pages:
        try:
            response = _get(url, timeout=6)
            local_html = raw_dir / f"{page_name}.html"
            local_html.write_bytes(response.content)
            status["items"].append({"type": "ir_page", "name": page_name, "url": url, "path": relative_to_project(local_html)})
            for link in _links(response.text, url):
                link["page"] = page_name
                all_links.append(link)
        except Exception as exc:  # noqa: BLE001
            status["gaps"].append({"page": page_name, "url": url, "reason": str(exc)})

    for seed in (target.config.get("public_company") or {}).get("earnings_presentations", []):
        url = seed.get("url")
        if not url:
            continue
        if not any(link.get("url") == url for link in all_links):
            all_links.append({"url": url, "label": seed.get("label", ""), "page": "config_seed"})

    interesting = []
    for link in all_links:
        haystack = f"{link.get('label', '')} {link.get('url', '')}".lower()
        if any(term in haystack for term in ["earnings", "quarter", "fiscal", "webcast", "static-files", "media-server", "presentation", "financial-results"]):
            interesting.append(link)

    downloaded = []
    for idx, link in enumerate(interesting[:max_downloads]):
        url = link["url"]
        if "static-files" not in url and not url.lower().endswith(".pdf"):
            continue
        try:
            response = _get(url, timeout=30)
            content_type = response.headers.get("content-type", "")
            suffix = ".pdf" if "pdf" in content_type or response.content[:4] == b"%PDF" else ".bin"
            label = link.get("label") or f"presentation_{idx + 1}"
            path = raw_dir / f"{safe_filename(label)}{suffix}"
            path.write_bytes(response.content)
            content_validation = _content_identity_check(target, path, content_type)
            row = {
                **link,
                "path": relative_to_project(path),
                "content_type": content_type,
                "bytes": len(response.content),
                "content_validation": content_validation,
            }
            if not content_validation["passed"]:
                rejected_dir = raw_dir / "rejected"
                rejected_dir.mkdir(parents=True, exist_ok=True)
                rejected_path = rejected_dir / path.name
                path.replace(rejected_path)
                row["rejected_path"] = relative_to_project(rejected_path)
                status["gaps"].append({"url": url, "reason": "content_identity_failed", "validation": content_validation})
                continue
            downloaded.append(row)
            status["items"].append({"type": "presentation", **row})
        except Exception as exc:  # noqa: BLE001
            status["gaps"].append({"url": url, "reason": f"download_failed: {exc}"})

    metadata = {
        "company": target.company_name,
        "ticker": target.ticker,
        "ir_url": ir_url,
        "official_transcript_status": "not_published_on_ir",
        "fallback_transcript_sources": [
            "https://stockanalysis.com/stocks/{ticker}/transcripts/".format(ticker=target.ticker.lower()),
            "Motley Fool earnings-call transcripts",
            "Seeking Alpha earnings-call transcripts",
            "Investing.com earnings-call transcripts",
            "ROIC.ai transcripts",
        ],
        "links": interesting,
        "downloaded_presentations": downloaded,
        "downloaded_transcripts": [],
        "updated_at": datetime.now().isoformat(timespec="seconds"),
    }
    try:
        metadata["downloaded_transcripts"] = _fetch_stockanalysis_transcripts(target)
        for item in metadata["downloaded_transcripts"]:
            status["items"].append({"type": "third_party_transcript", **item})
    except Exception as exc:  # noqa: BLE001
        status["gaps"].append({"reason": "third_party_transcript_fetch_failed", "source": metadata["fallback_transcript_sources"][0], "error": str(exc)})
    write_json(raw_dir / "earnings_call_metadata.json", metadata)
    lines = [
        f"# {target.company_name} Earnings Calls",
        "",
        "- Official IR pages were used for metadata, presentation files, webcast links, and press-release links.",
        "- Official transcript text was not found on IR in this pass; transcript sources below are fallback only.",
        "",
        "## Presentations",
    ]
    if downloaded:
        lines.extend(f"- [{item.get('label') or item['url']}]({item['url']}) -> `{item['path']}`" for item in downloaded)
    else:
        lines.append("- none downloaded")
    lines.extend(["", "## Transcript Fallbacks"])
    lines.extend(f"- {source}" for source in metadata["fallback_transcript_sources"])
    lines.extend(["", "## Downloaded Third-Party Transcripts"])
    if metadata["downloaded_transcripts"]:
        lines.extend(f"- [{item['label']}]({item['source_url']}) -> `{item['processed_path']}`" for item in metadata["downloaded_transcripts"])
    else:
        lines.append("- none downloaded")
    write_markdown(processed_dir / "earnings_calls_index.md", lines)
    status["status"] = "ok" if any(item.get("type") in {"presentation", "third_party_transcript"} for item in status["items"]) else "partial"
    if not downloaded:
        status["gaps"].append({"reason": "no_presentation_downloaded"})
    write_probe_report(target, "earnings_calls_ir", status)
    return status
