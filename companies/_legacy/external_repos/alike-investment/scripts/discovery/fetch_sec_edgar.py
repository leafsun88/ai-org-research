"""
SEC EDGAR Filing Fetcher
- 完全免费，无需API key
- 获取10-K (年报), 10-Q (季报), 8-K (重大事件)
- 解析HTML filing为纯文本
- 保存到 {TICKER}/sources/earnings/
"""

import re
import os
from typing import Optional
import sys
import json
import time
import requests
from pathlib import Path
from datetime import datetime
from html.parser import HTMLParser

DB_DIR = Path(os.environ.get('ALIKE_DB_DIR', str(Path(__file__).parent.parent)))
HEADERS = {'User-Agent': 'InvestmentResearchBot research@example.com'}

# ── CIK lookup cache ──
_CIK_CACHE = {}


def _load_cik_map():
    """Load SEC ticker → CIK mapping."""
    global _CIK_CACHE
    if _CIK_CACHE:
        return _CIK_CACHE
    try:
        r = requests.get('https://www.sec.gov/files/company_tickers.json',
                         headers=HEADERS, timeout=30)
        if r.status_code == 200:
            for item in r.json().values():
                _CIK_CACHE[item['ticker'].upper()] = str(item['cik_str']).zfill(10)
    except Exception as e:
        print(f"  Warning: could not load CIK map: {e}")
    return _CIK_CACHE


def get_cik(ticker: str) -> Optional[str]:
    """Get CIK for a ticker symbol."""
    cik_map = _load_cik_map()
    return cik_map.get(ticker.upper())


def get_filings_index(ticker: str):
    """Get all filings for a company from EDGAR."""
    cik = get_cik(ticker)
    if not cik:
        print(f"  ✗ Could not find CIK for {ticker}")
        return None

    url = f'https://data.sec.gov/submissions/CIK{cik}.json'
    r = requests.get(url, headers=HEADERS, timeout=15)
    if r.status_code != 200:
        print(f"  ✗ EDGAR submissions error: {r.status_code}")
        return None

    return r.json()


class HTMLTextExtractor(HTMLParser):
    """Extract readable text from HTML, stripping tags."""

    def __init__(self):
        super().__init__()
        self.result = []
        self.skip_tags = {'script', 'style', 'head', 'meta', 'link'}
        self._skip_depth = 0

    def handle_starttag(self, tag, attrs):
        if tag.lower() in self.skip_tags:
            self._skip_depth += 1
        if tag.lower() in ('p', 'br', 'div', 'tr', 'li', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
            self.result.append('\n')

    def handle_endtag(self, tag):
        if tag.lower() in self.skip_tags:
            self._skip_depth = max(0, self._skip_depth - 1)
        if tag.lower() in ('p', 'div', 'tr', 'table', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
            self.result.append('\n')

    def handle_data(self, data):
        if self._skip_depth == 0:
            self.result.append(data)

    def get_text(self):
        text = ''.join(self.result)
        # Clean up excessive whitespace
        text = re.sub(r'[ \t]+', ' ', text)
        text = re.sub(r'\n\s*\n\s*\n+', '\n\n', text)
        return text.strip()


def extract_text_from_html(html_content: str) -> str:
    """Extract readable text from SEC HTML filing."""
    parser = HTMLTextExtractor()
    parser.feed(html_content)
    return parser.get_text()


def download_filing(ticker: str, accession: str, primary_doc: str, cik: str) -> Optional[str]:
    """Download a specific SEC filing and return text content."""
    acc_clean = accession.replace('-', '')
    cik_int = str(int(cik))
    url = f'https://www.sec.gov/Archives/edgar/data/{cik_int}/{acc_clean}/{primary_doc}'

    try:
        r = requests.get(url, headers=HEADERS, timeout=60)
        if r.status_code == 200:
            if primary_doc.endswith('.htm') or primary_doc.endswith('.html'):
                return extract_text_from_html(r.text)
            else:
                return r.text
        else:
            print(f"    Download failed: {r.status_code}")
    except Exception as e:
        print(f"    Download error: {e}")
    return None


def fetch_sec_filings(ticker: str, filing_types=None, max_per_type=100, download_text=True):
    """
    Fetch SEC filings for a company.

    Args:
        ticker: Stock ticker symbol
        filing_types: List of filing types to fetch (default: ['10-K', '10-Q', '8-K'])
        max_per_type: Max filings to fetch per type
        download_text: Whether to download and parse the actual filing text

    Returns:
        Dict with filing metadata and optionally full text
    """
    if filing_types is None:
        filing_types = ['10-K', '10-Q']

    print(f"[SEC EDGAR] Fetching filings for {ticker}...")

    data = get_filings_index(ticker)
    if not data:
        return {"success": False, "error": "Could not fetch filings index"}

    company_name = data.get('name', ticker)
    cik = get_cik(ticker)
    recent = data.get('filings', {}).get('recent', {})
    forms = list(recent.get('form', []))
    dates = list(recent.get('filingDate', []))
    accessions = list(recent.get('accessionNumber', []))
    primary_docs = list(recent.get('primaryDocument', []))
    descriptions = list(recent.get('primaryDocDescription', []))

    # Load additional filing pages (for companies with many filings)
    extra_files = data.get('filings', {}).get('files', [])
    for ef in extra_files:
        try:
            ef_url = f'https://data.sec.gov/submissions/{ef["name"]}'
            r = requests.get(ef_url, headers=HEADERS, timeout=15)
            if r.status_code == 200:
                ef_data = r.json()
                forms.extend(ef_data.get('form', []))
                dates.extend(ef_data.get('filingDate', []))
                accessions.extend(ef_data.get('accessionNumber', []))
                primary_docs.extend(ef_data.get('primaryDocument', []))
                descriptions.extend(ef_data.get('primaryDocDescription', []))
            time.sleep(0.2)
        except Exception as e:
            print(f"  Warning: could not load extra filings page {ef.get('name')}: {e}")

    print(f"  Total filings in index: {len(forms)}")

    results = {
        "success": True,
        "company": company_name,
        "cik": cik,
        "filings": {},
    }

    company_dir = DB_DIR / ticker / "sources" / "earnings"
    company_dir.mkdir(parents=True, exist_ok=True)

    for ftype in filing_types:
        count = 0
        results["filings"][ftype] = []

        for i in range(len(forms)):
            if forms[i] != ftype or count >= max_per_type:
                continue

            filing_info = {
                "date": dates[i],
                "accession": accessions[i],
                "document": primary_docs[i],
                "description": descriptions[i] if i < len(descriptions) else "",
            }

            if download_text:
                print(f"  Downloading {ftype} ({dates[i]})...")
                text = download_filing(ticker, accessions[i], primary_docs[i], cik)
                if text:
                    # Truncate very long filings (10-K can be 500K+ chars)
                    # Keep first 100K chars which covers most of the important sections
                    if len(text) > 150000:
                        text = text[:150000] + f"\n\n[... truncated, full filing: {len(text)} chars ...]"

                    filing_info["text_length"] = len(text)

                    # Save as markdown
                    filename = f"{dates[i]}_{ftype}.md"
                    acc_clean = accessions[i].replace('-', '')
                    cik_int = str(int(cik))
                    doc_url = f"https://www.sec.gov/Archives/edgar/data/{cik_int}/{acc_clean}/{primary_docs[i]}"

                    md_content = f"""---
ticker: {ticker}
type: sec_filing
form: {ftype}
date: {dates[i]}
accession: {accessions[i]}
url: {doc_url}
text_length: {len(text)}
---

# {ticker} {ftype} - {dates[i]}

## Filing Info
- **Company**: {company_name}
- **Form**: {ftype}
- **Filed**: {dates[i]}
- **SEC URL**: {doc_url}

## Full Text

{text}
"""
                    filepath = company_dir / filename
                    filepath.write_text(md_content, encoding='utf-8')
                    print(f"    ✓ {filename} ({len(text):,} chars)")
                    filing_info["saved_to"] = str(filepath)
                else:
                    print(f"    ✗ Failed to download")

                time.sleep(0.5)  # SEC rate limiting: 10 requests/sec

            results["filings"][ftype].append(filing_info)
            count += 1

    # Summary
    total = sum(len(v) for v in results["filings"].values())
    print(f"  Done: {total} filings processed")

    return results


def fetch_10k_sections(ticker: str, years=2):
    """Fetch just 10-K filings (annual reports) - the most valuable for analysis."""
    return fetch_sec_filings(ticker, filing_types=['10-K'], max_per_type=years)


def fetch_quarterly_filings(ticker: str, quarters=4):
    """Fetch recent 10-Q filings."""
    return fetch_sec_filings(ticker, filing_types=['10-Q'], max_per_type=quarters)


def fetch_material_events(ticker: str, count=5):
    """Fetch recent 8-K filings (material events like earnings, M&A, etc.)."""
    return fetch_sec_filings(ticker, filing_types=['8-K'], max_per_type=count)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python fetch_sec_edgar.py TICKER [10-K|10-Q|8-K] [max_count]")
        print("Example: python fetch_sec_edgar.py APP 10-K 2")
        sys.exit(1)

    ticker = sys.argv[1]
    ftype = sys.argv[2] if len(sys.argv) > 2 else None
    max_count = int(sys.argv[3]) if len(sys.argv) > 3 else 100

    if ftype:
        results = fetch_sec_filings(ticker, filing_types=[ftype], max_per_type=max_count)
    else:
        results = fetch_sec_filings(ticker, max_per_type=max_count)

    if results["success"]:
        for ft, filings in results["filings"].items():
            print(f"\n{ft}: {len(filings)} filings")
            for f in filings:
                print(f"  {f['date']} | {f.get('text_length', '?')} chars")
