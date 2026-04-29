"""
基础组织结构采集
- 从 yfinance / FMP profile 提取管理层信息
- 自动生成 organization/overview/org_structure.md
- 自动生成 organization/_org_scan_report.md
- 为 C-Suite / VP 生成基础档案
"""

import re
from pathlib import Path
from datetime import datetime

import yfinance as yf

from fetch_financials import fmp_profile
from path_utils import resolve_discovery_dir


def slugify(text: str) -> str:
    text = re.sub(r"[^\w\s-]", "", text).strip().lower()
    return re.sub(r"[-\s]+", "_", text) or "unknown"


def officer_bucket(title: str) -> str:
    t = (title or "").lower()
    if any(k in t for k in ["chief", "ceo", "cfo", "cto", "coo", "president", "chairman", "general counsel"]):
        return "c_suite"
    if "board" in t or "director" in t:
        return "board"
    if "vp" in t or "vice president" in t or "svp" in t:
        return "vp_level"
    return "c_suite"


def write_person_file(base_dir: Path, ticker: str, person: dict):
    name = person.get("name") or "Unknown"
    title = person.get("title") or "Unknown"
    bucket = officer_bucket(title)
    path = base_dir / bucket / f"{slugify(name)}.md"
    age = person.get("age", "N/A")
    pay = person.get("totalPay")
    pay_str = f"${pay:,.0f}" if isinstance(pay, (int, float)) else "N/A"

    path.write_text(
        f"""---
ticker: {ticker}
person: {name}
title: {title}
credibility: S4
evidence: E2
date: "{datetime.now().strftime('%Y-%m-%d')}"
status: auto_basic
---

# {name} - {title}

## Identity
- **Full Name:** {name}
- **Title:** {title}
- **Age:** {age}
- **Compensation:** {pay_str}

## Source
- yfinance companyOfficers

## Notes
- 该档案由 `/collect` 自动生成，属于基础组织静态信息。
- 如需完整职业轨迹、人脉网络、争议和离职背景，请继续运行 `/org-scan`。
""",
        encoding="utf-8",
    )


def fetch_org_basic(ticker: str, company_name: str = None):
    stock = yf.Ticker(ticker)
    info = stock.info or {}
    fp = fmp_profile(ticker) or {}

    company = company_name or fp.get("companyName") or info.get("shortName") or ticker
    base_dir = resolve_discovery_dir(ticker) / "organization"
    overview_dir = base_dir / "overview"
    for folder in ["c_suite", "vp_level", "board", "departed", "overview"]:
        (base_dir / folder).mkdir(parents=True, exist_ok=True)

    officers = info.get("companyOfficers", []) or []
    if not isinstance(officers, list):
        officers = []

    for officer in officers[:25]:
        write_person_file(base_dir, ticker, officer)

    c_suite = [o for o in officers if officer_bucket(o.get("title", "")) == "c_suite"]
    vp_level = [o for o in officers if officer_bucket(o.get("title", "")) == "vp_level"]

    founded = fp.get("ipoDate", "N/A")
    exchange = info.get("fullExchangeName", fp.get("exchangeFullName", "N/A"))
    sector = info.get("sectorDisp", fp.get("sector", "N/A"))
    industry = info.get("industryDisp", fp.get("industry", "N/A"))
    hq = ", ".join(filter(None, [info.get("city", fp.get("city", "")), info.get("state", fp.get("state", "")), fp.get("country", info.get("country", ""))])) or "N/A"
    employees = info.get("fullTimeEmployees") or fp.get("fullTimeEmployees") or "N/A"

    org_structure = [
        "---",
        f"ticker: {ticker}",
        f"company: {company}",
        "type: org_structure",
        "credibility: S4",
        "evidence: E2",
        f'date: "{datetime.now().strftime("%Y-%m-%d")}"',
        "status: auto_basic",
        "sources:",
        "  - yfinance companyOfficers",
        "  - FMP company profile",
        "---",
        "",
        f"# {company} ({ticker}) - Organization Structure",
        "",
        "## Company Overview",
        f"- **Exchange:** {exchange}",
        f"- **Sector:** {sector}",
        f"- **Industry:** {industry}",
        f"- **HQ:** {hq}",
        f"- **Employees:** {employees:,}" if isinstance(employees, int) else f"- **Employees:** {employees}",
        f"- **IPO / reference date:** {founded}",
        "",
        f"## C-Suite Executive Team ({len(c_suite)} members)",
        "",
        "| Name | Title | Age | Compensation |",
        "|------|-------|-----|--------------|",
    ]
    for officer in c_suite:
        age = officer.get("age", "N/A")
        pay = officer.get("totalPay")
        pay_str = f"${pay:,.0f}" if isinstance(pay, (int, float)) else "N/A"
        org_structure.append(f"| **{officer.get('name', 'N/A')}** | {officer.get('title', 'N/A')} | {age} | {pay_str} |")
    org_structure.extend([
        "",
        f"## VP / Extended Leadership ({len(vp_level)} members)",
        "",
        "| Name | Title | Age |",
        "|------|-------|-----|",
    ])
    for officer in vp_level:
        org_structure.append(f"| **{officer.get('name', 'N/A')}** | {officer.get('title', 'N/A')} | {officer.get('age', 'N/A')} |")
    org_structure.extend([
        "",
        "## Observations",
        "- 该文档由 `/collect` 自动生成，反映基础组织静态结构，不等同于完整组织穿透。",
        "- 如需 board、departed exec、跨公司职业轨迹、治理异常与关键人才网络，请继续运行 `/org-scan`。",
    ])
    (overview_dir / "org_structure.md").write_text("\n".join(org_structure), encoding="utf-8")

    report_lines = [
        "---",
        f"ticker: {ticker}",
        "type: org_scan_report",
        "credibility: S4",
        "evidence: E2",
        f'date: "{datetime.now().strftime("%Y-%m-%d")}"',
        "status: auto_basic",
        "---",
        "",
        f"# {company} ({ticker}) - 组织架构穿透报告",
        "",
        "## 自动生成结论",
        f"- 已识别 C-Suite: {len(c_suite)} 人",
        f"- 已识别 VP / Extended Leadership: {len(vp_level)} 人",
        f"- 数据来源以 yfinance/FMP 为主，适合形成初始 org map",
        "",
        "## 当前局限",
        "- 尚未系统补齐 board / committee / departed exec",
        "- 尚未补齐每位高管的职业轨迹、人脉网络、争议与治理信号",
        "- 若要进入高质量 D1-D7 评分，仍建议运行 `/org-scan` 深挖",
    ]
    (base_dir / "_org_scan_report.md").write_text("\n".join(report_lines), encoding="utf-8")

    return {
        "company": company,
        "c_suite_count": len(c_suite),
        "vp_count": len(vp_level),
        "officer_count": len(officers),
    }


if __name__ == "__main__":
    import sys

    ticker = sys.argv[1]
    company_name = sys.argv[2] if len(sys.argv) > 2 else None
    print(fetch_org_basic(ticker, company_name))
