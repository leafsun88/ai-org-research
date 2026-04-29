"""
Founder / CEO voice 自动采集
- 读取 yfinance / FMP 获取 CEO 信息
- 汇总 insider 交易
- 复用 Perplexity URL discovery 获取管理层访谈 / 官方发言 URL
- 生成 discovery/sources/founder_voice.md
"""

import re
from pathlib import Path
from datetime import datetime

import yfinance as yf

from fetch_financials import fmp_profile
from fetch_perplexity import query_perplexity_urls, fetch_full_text
from path_utils import resolve_discovery_dir


def slugify(text: str) -> str:
    text = re.sub(r"[^\w\s-]", "", text).strip().lower()
    return re.sub(r"[-\s]+", "_", text) or "unknown"


def normalize_person_name(name: str) -> str:
    if not name:
        return ""
    cleaned = re.sub(r"^(mr|mrs|ms|dr|prof)\.?\s+", "", name.strip(), flags=re.I)
    cleaned = re.sub(r"\s+", " ", cleaned)
    return cleaned.strip()


def resolve_ceo(stock, fp):
    info = stock.info or {}
    officers = info.get("companyOfficers", []) or []
    for officer in officers:
        title = (officer.get("title") or "").lower()
        if "chief executive officer" in title or title == "ceo" or "ceo" in title:
            return officer.get("name") or fp.get("ceo") or "CEO"
    return fp.get("ceo") or "CEO"


def build_prompt(ticker: str, company: str, ceo: str) -> str:
    return f"""You are a search engine. Find real URLs about the public voice of {ceo}, the CEO/founder of {company} ({ticker}).

Return ONLY a JSON array. Each item must be:
{{"url":"https://...","title":"exact title","author":"speaker or publisher","date":"YYYY-MM-DD","brief":"10 words max"}}

Search for:
1. CEO interviews in 2024-2026
2. Conference appearances / keynote talks
3. Official blog / shareholder letter / earnings commentary quoting {ceo}
4. Long-form podcast appearances by {ceo}
5. Recent coverage of insider trading or stock sales by {ceo}

Rules:
- Only include real URLs.
- No markdown, no explanation.
- Prefer free and directly accessible sources.
- Exclude paywalled URLs when possible.
- Return up to 8 strongest URLs.
"""


def collect_local_voice(output_dir: Path, ceo: str):
    normalized = normalize_person_name(ceo)
    last_name = (normalized.split()[-1] if normalized else "").lower()
    youtube_dir = output_dir / "sources" / "youtube"
    podcast_dir = output_dir / "sources" / "podcasts"
    youtube_hits = []
    podcast_hits = []

    for path in sorted(youtube_dir.glob("*.md"), reverse=True):
        name = path.name.lower()
        if last_name and last_name in name:
            youtube_hits.append(path)
        elif len(youtube_hits) < 5:
            youtube_hits.append(path)
        if len(youtube_hits) >= 5:
            break

    for path in sorted(podcast_dir.glob("*.md"), reverse=True):
        name = path.name.lower()
        if last_name and last_name in name:
            podcast_hits.append(path)
        elif len(podcast_hits) < 5:
            podcast_hits.append(path)
        if len(podcast_hits) >= 5:
            break

    return youtube_hits, podcast_hits


def collect_web_voice(company: str, ticker: str, ceo: str, output_dir: Path):
    founder_dir = output_dir / "sources" / "founder"
    founder_dir.mkdir(parents=True, exist_ok=True)
    urls = []
    try:
        urls = query_perplexity_urls(build_prompt(ticker, company, ceo))
    except Exception:
        urls = []

    saved = []
    for item in urls[:8]:
        url = item.get("url", "")
        if not url.startswith("http"):
            continue
        title = item.get("title") or item.get("brief") or url
        safe = slugify(title)[:60]
        out = founder_dir / f"{safe}.md"
        if out.exists():
            saved.append((item, out))
            continue
        result = fetch_full_text(url, timeout=30)
        if not result.get("success"):
            continue
        out.write_text(
            f"""---
type: founder_source
title: "{title}"
author: "{item.get('author', '')}"
date: {item.get('date', datetime.now().strftime('%Y-%m-%d'))}
url: {url}
chars: {result.get('chars', 0)}
credibility: S3
evidence: E2
---

# {title}

{result.get('text', '')}
""",
            encoding="utf-8",
        )
        saved.append((item, out))
    return saved


def summarize_insider(stock):
    lines = []
    try:
        txns = stock.insider_transactions
        if txns is not None and not txns.empty:
            for _, row in txns.head(10).iterrows():
                date = row.get("Start Date", "N/A")
                if hasattr(date, "strftime"):
                    date = date.strftime("%Y-%m-%d")
                insider = row.get("Insider", "N/A")
                position = row.get("Position", "N/A")
                text = str(row.get("Text", ""))
                txn_type = "卖出" if "Sale" in text else "买入" if "Purchase" in text else text[:20]
                shares = row.get("Shares", "N/A")
                value = row.get("Value", "N/A")
                lines.append(f"| {date} | {insider} | {position} | {txn_type} | {shares} | {value} |")
    except Exception:
        pass
    return lines


def fetch_founder_voice(ticker: str, company_name: str = None):
    stock = yf.Ticker(ticker)
    fp = fmp_profile(ticker) or {}
    info = stock.info or {}
    company = company_name or fp.get("companyName") or info.get("shortName") or ticker
    ceo = normalize_person_name(resolve_ceo(stock, fp))
    output_dir = resolve_discovery_dir(ticker)
    founder_voice_path = output_dir / "sources" / "founder_voice.md"
    founder_voice_path.parent.mkdir(parents=True, exist_ok=True)

    youtube_hits, podcast_hits = collect_local_voice(output_dir, ceo)
    web_hits = collect_web_voice(company, ticker, ceo, output_dir)
    insider_rows = summarize_insider(stock)

    lines = [
        "---",
        f"ticker: {ticker}",
        "type: founder_voice",
        "status: auto_basic",
        "credibility: S3",
        "evidence: E2",
        f"generated: {datetime.now().strftime('%Y-%m-%d')}",
        f'ceo: "{ceo}"',
        "---",
        "",
        f"# {company} ({ticker}) — Founder / CEO Voice",
        "",
        "## Identity",
        f"- **CEO / Founder Lead**: {ceo}",
        f"- **Company**: {company}",
        f"- **Source basis**: yfinance/FMP + local transcripts + web founder sources",
        "",
        "## Source Inventory",
        f"- **YouTube voice sources**: {len(youtube_hits)}",
        f"- **Podcast voice sources**: {len(podcast_hits)}",
        f"- **Web founder sources**: {len(web_hits)}",
        "",
        "## Recent Public Voice Sources",
    ]
    for path in youtube_hits:
        lines.append(f"- [YouTube] {path.name}")
    for path in podcast_hits:
        lines.append(f"- [Podcast] {path.name}")
    seen_web = set()
    for item, path in web_hits:
        label = item.get("title") or item.get("brief") or path.stem
        key = (label, path.name)
        if key in seen_web:
            continue
        seen_web.add(key)
        lines.append(f"- [Web] {label} -> {path.name}")

    lines.extend([
        "",
        "## Insider Activity Snapshot",
    ])
    if insider_rows:
        lines.extend([
            "| 日期 | 内部人 | 职位 | 类型 | 股数 | 金额 |",
            "|------|--------|------|------|------|------|",
        ])
        lines.extend(insider_rows)
    else:
        lines.append("- 未获取到近期 insider 交易摘要")

    lines.extend([
        "",
        "## Key Questions",
        "- CEO 最近最常谈的战略主题是什么？",
        "- 是否出现 AI / 产品 / 组织设计方向变化？",
        "- 公开表达与 insider 行为是否一致？",
        "",
        "## Notes",
        "- 该文件由 `/collect` 自动生成，属于 founder voice 的基础版本。",
        "- 若要形成高质量 D1 认知判断，仍建议继续运行 `/founder` 做更深的手工/半手工搜索。",
    ])
    founder_voice_path.write_text("\n".join(lines), encoding="utf-8")

    return {
        "company": company,
        "ceo": ceo,
        "youtube_hits": len(youtube_hits),
        "podcast_hits": len(podcast_hits),
        "web_hits": len(web_hits),
        "insider_rows": len(insider_rows),
    }


if __name__ == "__main__":
    import sys

    ticker = sys.argv[1]
    company_name = sys.argv[2] if len(sys.argv) > 2 else None
    print(fetch_founder_voice(ticker, company_name))
