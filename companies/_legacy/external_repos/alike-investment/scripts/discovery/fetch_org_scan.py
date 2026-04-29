"""
组织穿透脚本化第一版
- 基于 yfinance companyOfficers 获取管理层名单
- 用 Perplexity URL discovery 找每位高管的 biography / role / controversy 来源
- 拉取部分原文，生成逐人档案
- 更新 organization/_org_scan_report.md
"""

import re
from pathlib import Path
from datetime import datetime

import yfinance as yf

from fetch_financials import fmp_profile
from fetch_org_basic import officer_bucket, slugify
from fetch_perplexity import query_perplexity_urls, fetch_full_text
from path_utils import resolve_discovery_dir


def normalize_person_name(name: str) -> str:
    if not name:
        return ""
    cleaned = re.sub(r"^(mr|mrs|ms|dr|prof)\.?\s+", "", name.strip(), flags=re.I)
    cleaned = re.sub(r"\s+", " ", cleaned)
    return cleaned.strip()


def build_person_prompt(company: str, ticker: str, name: str, title: str) -> str:
    return f"""You are a search engine. Find real URLs about {name}, who is {title} at {company} ({ticker}).

Return ONLY a JSON array. Each item must be:
{{"url":"https://...","title":"exact title","author":"publisher or org","date":"YYYY-MM-DD","brief":"10 words max"}}

Search for:
1. Biography / career profile
2. Current role and responsibilities at {company}
3. Interview / conference / keynote / podcast appearances
4. Governance, controversy, lawsuit, board or leadership transition references

Rules:
- Only include real URLs.
- No markdown, no explanation.
- Prefer company IR, official bio, reputable interviews, conference pages, major media.
- Exclude paywalled links when possible.
- Return up to 6 strongest URLs.
"""


def select_people(officers):
    c_suite = [o for o in officers if officer_bucket(o.get("title", "")) == "c_suite"]
    vp_level = [o for o in officers if officer_bucket(o.get("title", "")) == "vp_level"]
    selected = c_suite[:8] + vp_level[:4]
    deduped = []
    seen = set()
    for officer in selected:
        name = officer.get("name", "")
        if name and name not in seen:
            seen.add(name)
            deduped.append(officer)
    return deduped, c_suite, vp_level


def fetch_person_sources(company: str, ticker: str, person: dict, output_dir: Path):
    name = normalize_person_name(person.get("name") or "Unknown")
    title = person.get("title") or "Unknown"
    urls = []
    try:
        urls = query_perplexity_urls(build_person_prompt(company, ticker, name, title))
    except Exception:
        urls = []

    person_source_dir = output_dir / "organization" / "sources" / slugify(name)
    person_source_dir.mkdir(parents=True, exist_ok=True)

    saved_sources = []
    for item in urls[:4]:
        url = item.get("url", "")
        if not url.startswith("http"):
            continue
        title_text = item.get("title") or item.get("brief") or url
        safe_name = slugify(title_text)[:60]
        source_path = person_source_dir / f"{safe_name}.md"
        if source_path.exists():
            saved_sources.append((item, source_path))
            continue
        fetched = fetch_full_text(url, timeout=25)
        if not fetched.get("success"):
            continue
        source_path.write_text(
            f"""---
type: org_person_source
person: "{name}"
title: "{title}"
date: {item.get('date', datetime.now().strftime('%Y-%m-%d'))}
url: {url}
chars: {fetched.get('chars', 0)}
credibility: S3
evidence: E2
---

# {title_text}

{fetched.get('text', '')[:6000]}
""",
            encoding="utf-8",
        )
        saved_sources.append((item, source_path))

    if not saved_sources:
        last_name = (name.split()[-1] if name else "").lower()
        local_candidates = []
        for path in sorted((output_dir / "sources" / "youtube").glob("*.md"), reverse=True):
            if last_name and last_name in path.name.lower():
                local_candidates.append(("local_youtube", path))
            if len(local_candidates) >= 2:
                break
        for path in sorted((output_dir / "sources" / "podcasts").glob("*.md"), reverse=True):
            if last_name and last_name in path.name.lower():
                local_candidates.append(("local_podcast", path))
            if len(local_candidates) >= 4:
                break
        for source_type, path in local_candidates:
            saved_sources.append((
                {"title": path.stem, "brief": source_type},
                path,
            ))
    return saved_sources


def write_person_profile(base_dir: Path, ticker: str, person: dict, saved_sources):
    name = normalize_person_name(person.get("name") or "Unknown")
    title = person.get("title") or "Unknown"
    bucket = officer_bucket(title)
    path = base_dir / "organization" / bucket / f"{slugify(name)}.md"
    age = person.get("age", "N/A")
    pay = person.get("totalPay")
    pay_str = f"${pay:,.0f}" if isinstance(pay, (int, float)) else "N/A"

    lines = [
        "---",
        f"ticker: {ticker}",
        f"person: {name}",
        f"title: {title}",
        "credibility: S4",
        "evidence: E3",
        f'date: "{datetime.now().strftime("%Y-%m-%d")}"',
        "status: auto_scan",
        "---",
        "",
        f"# {name} - {title}",
        "",
        "## Identity",
        f"- **Full Name:** {name}",
        f"- **Title:** {title}",
        f"- **Age:** {age}",
        f"- **Compensation:** {pay_str}",
        "",
        "## Auto Scan Summary",
        f"- 收集到外部资料: {len(saved_sources)} 条",
        "- 该档案由 `/collect -> org_scan` 自动生成，适合形成初步职业轨迹和外部信号。",
        "",
        "## Source Inventory",
    ]
    if saved_sources:
        for item, source_path in saved_sources:
            rel = source_path.relative_to(base_dir)
            lines.append(f"- {item.get('title', source_path.name)} -> {rel}")
    else:
        lines.append("- 暂未抓到外部资料")
    lines.extend([
        "",
        "## Next Questions",
        "- 这个人加入公司前的核心履历是什么？",
        "- 他/她当前真正负责的职能边界是什么？",
        "- 是否有离职、争议、治理异常或能力错配信号？",
    ])
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def fetch_org_scan(ticker: str, company_name: str = None):
    stock = yf.Ticker(ticker)
    info = stock.info or {}
    fp = fmp_profile(ticker) or {}
    company = company_name or fp.get("companyName") or info.get("shortName") or ticker
    output_dir = resolve_discovery_dir(ticker)
    org_dir = output_dir / "organization"
    (org_dir / "sources").mkdir(parents=True, exist_ok=True)

    officers = info.get("companyOfficers", []) or []
    if not isinstance(officers, list):
        officers = []

    selected, c_suite, vp_level = select_people(officers)
    person_paths = []
    people_with_sources = 0

    for person in selected:
        saved_sources = fetch_person_sources(company, ticker, person, output_dir)
        if saved_sources:
            people_with_sources += 1
        person_paths.append(write_person_profile(output_dir, ticker, person, saved_sources))

    report_path = org_dir / "_org_scan_report.md"
    report_lines = [
        "---",
        f"ticker: {ticker}",
        "type: org_scan_report",
        "credibility: S4",
        "evidence: E3",
        f'date: "{datetime.now().strftime("%Y-%m-%d")}"',
        "status: auto_scan",
        "---",
        "",
        f"# {company} ({ticker}) - 组织架构穿透报告",
        "",
        "## Auto Scan Coverage",
        f"- C-Suite identified: {len(c_suite)}",
        f"- VP / Extended Leadership identified: {len(vp_level)}",
        f"- People scanned: {len(selected)}",
        f"- People with external sources: {people_with_sources}",
        "",
        "## Key Observations",
        "- 该报告由 `/collect` 自动生成，已经超过基础 org map，但仍不是最终人工版组织穿透。",
        "- 当前更适合回答“关键高管有哪些、能否找到外部履历和公开资料”，不适合直接替代最终投资判断。",
        "",
        "## Generated Profiles",
    ]
    for path in person_paths:
        report_lines.append(f"- {path.relative_to(output_dir)}")
    report_lines.extend([
        "",
        "## Remaining Gaps",
        "- board / committee / proxy 细节仍不完整",
        "- departed exec 仍需要专项补充",
        "- 人脉网络、跨公司共事关系、治理异常仍建议人工复核",
    ])
    report_path.write_text("\n".join(report_lines), encoding="utf-8")

    return {
        "company": company,
        "c_suite_count": len(c_suite),
        "vp_count": len(vp_level),
        "selected_people": len(selected),
        "people_with_sources": people_with_sources,
    }


if __name__ == "__main__":
    import sys

    ticker = sys.argv[1]
    company_name = sys.argv[2] if len(sys.argv) > 2 else None
    print(fetch_org_scan(ticker, company_name))
