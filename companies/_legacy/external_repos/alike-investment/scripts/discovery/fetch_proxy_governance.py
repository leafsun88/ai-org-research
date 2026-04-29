"""
Proxy / Governance 自动采集
- 拉取最新 DEF 14A proxy filing
- 生成 governance_summary.md
- 将 board / compensation / shareholder rights 风险正式接入 /collect
"""

import sys
import re
from pathlib import Path
from datetime import datetime

import yfinance as yf

sys.path.insert(0, str(Path(__file__).parent))

from fetch_financials import fmp_profile
from fetch_sec_edgar import fetch_sec_filings
from path_utils import resolve_discovery_dir


def fmt_risk(value):
    if value is None:
        return "N/A"
    return f"{value}/10"


def slugify(text: str) -> str:
    text = re.sub(r"[^\w\s-]", "", text).strip().lower()
    return re.sub(r"[-\s]+", "_", text) or "unknown"


def parse_board_nominees(text: str):
    patterns = [
        r"To elect (.+?) to serve as directors",
        r"Election of Directors:\s*(.+)",
    ]
    names = []
    for pattern in patterns:
        matches = re.findall(pattern, text, flags=re.I | re.S)
        for match in matches:
            cleaned = re.sub(r"\s+", " ", match).strip().rstrip(".")
            cleaned = cleaned.split(";")[0]
            cleaned = cleaned.split(" for ")[0]
            cleaned = cleaned.replace(" and ", ", ")
            for part in cleaned.split(","):
                candidate = part.strip(" ;")
                if not re.fullmatch(r"[A-Z][A-Za-z\.\-'\s]{2,60}", candidate):
                    continue
                if len(candidate.split()) < 2:
                    continue
                if candidate not in names:
                    names.append(candidate)
    return names


def parse_independence(text: str):
    match = re.search(
        r"except for (.+?), each of our director nominees has no material relationship",
        text,
        flags=re.I | re.S,
    )
    if not match:
        return []
    cleaned = re.sub(r"\s+", " ", match.group(1)).replace(" and ", ", ")
    return [name.strip(" ;,.") for name in cleaned.split(",") if name.strip()]


def parse_lead_independent_director(text: str):
    match = re.search(r"elected ([A-Z][A-Za-z\.\s]+?) to succeed .*? as the Lead Independent Director", text)
    if match:
        return match.group(1).strip()
    match = re.search(r"([A-Z][A-Za-z\.\s]+)\s*\(Lead Independent Director\)", text)
    return match.group(1).strip() if match else None


def parse_committee_mentions(text: str):
    committee_lines = []
    for match in re.findall(r"Members:\s*([A-Za-z0-9,\.\-\s\(\)]+)", text):
        line = re.sub(r"\s+", " ", match).strip()
        if line and line not in committee_lines:
            committee_lines.append(line)
    return committee_lines[:6]


def write_board_profiles(board_dir: Path, nominees, independent_names, lead_director):
    independent_set = {name.lower() for name in independent_names}
    created = 0
    for name in nominees:
        path = board_dir / f"{slugify(name)}.md"
        independence = "independent" if name.lower() in independent_set else "non-independent / management-affiliated"
        role_note = "Lead Independent Director" if lead_director and name.lower() == lead_director.lower() else "Director nominee"
        path.write_text(
            f"""---
person: "{name}"
type: board_profile
credibility: S5
evidence: E4
date: "{datetime.now().strftime('%Y-%m-%d')}"
status: auto_basic
---

# {name}

## Board Status
- **Role**: {role_note}
- **Independence**: {independence}

## Notes
- 该档案由 DEF 14A 自动生成，属于 board 静态信息第一版。
- 若需要完整职业轨迹、委员会历史、外部董事席位和治理判断，建议后续继续深挖。
""",
            encoding="utf-8",
        )
        created += 1
    return created


def fetch_proxy_governance(ticker: str, company_name: str = None):
    stock = yf.Ticker(ticker)
    info = stock.info or {}
    fp = fmp_profile(ticker) or {}
    company = company_name or fp.get("companyName") or info.get("shortName") or ticker

    output_dir = resolve_discovery_dir(ticker) / "organization"
    proxy_dir = output_dir / "proxy"
    board_dir = output_dir / "board"
    proxy_dir.mkdir(parents=True, exist_ok=True)
    board_dir.mkdir(parents=True, exist_ok=True)

    result = fetch_sec_filings(ticker, filing_types=["DEF 14A"], max_per_type=1)
    proxy_count = len(result.get("filings", {}).get("DEF 14A", []))
    proxy_saved = None
    proxy_text = ""
    if proxy_count:
        filing = result["filings"]["DEF 14A"][0]
        proxy_saved = filing.get("saved_to")
        if proxy_saved and Path(proxy_saved).exists():
            proxy_text = Path(proxy_saved).read_text(encoding="utf-8", errors="ignore")
            target = proxy_dir / Path(proxy_saved).name
            target.write_text(proxy_text, encoding="utf-8")
            proxy_saved = str(target)

    nominees = parse_board_nominees(proxy_text)
    independent_names = parse_independence(proxy_text)
    lead_director = parse_lead_independent_director(proxy_text)
    committee_mentions = parse_committee_mentions(proxy_text)
    board_profiles_created = write_board_profiles(board_dir, nominees, independent_names, lead_director) if nominees else 0

    governance_summary_path = output_dir / "governance_summary.md"
    board_files = list(board_dir.glob("*.md"))

    lines = [
        "---",
        f"ticker: {ticker}",
        "type: governance_summary",
        "credibility: S4",
        "evidence: E3",
        f'date: "{datetime.now().strftime("%Y-%m-%d")}"',
        "status: auto_basic",
        "---",
        "",
        f"# {company} ({ticker}) — Governance Summary",
        "",
        "## Proxy Coverage",
        f"- **Latest DEF 14A pulled**: {'yes' if proxy_saved else 'no'}",
        f"- **Saved proxy path**: {proxy_saved or 'N/A'}",
        f"- **Existing board profiles**: {len(board_files)}",
        f"- **Board nominees parsed**: {len(nominees)}",
        f"- **Lead Independent Director**: {lead_director or 'N/A'}",
        "",
        "## Governance Risk Snapshot (Yahoo Finance)",
        "| Metric | Value |",
        "|--------|-------|",
        f"| Overall Risk | {fmt_risk(info.get('overallRisk'))} |",
        f"| Audit Risk | {fmt_risk(info.get('auditRisk'))} |",
        f"| Board Risk | {fmt_risk(info.get('boardRisk'))} |",
        f"| Compensation Risk | {fmt_risk(info.get('compensationRisk'))} |",
        f"| Shareholder Rights Risk | {fmt_risk(info.get('shareHolderRightsRisk'))} |",
        "",
        "## Board Nominees",
    ]
    if nominees:
        for name in nominees:
            independence = "independent" if name.lower() in {n.lower() for n in independent_names} else "management / non-independent"
            lines.append(f"- {name} ({independence})")
    else:
        lines.append("- 未自动解析到董事候选人")
    lines.extend([
        "",
        "## Committee Signals",
    ])
    if committee_mentions:
        for line in committee_mentions:
            lines.append(f"- {line}")
    else:
        lines.append("- 未自动解析到明确 committee member 列表")
    lines.extend([
        "",
        "## Notes",
        "- 该文件由 `/collect` 自动生成，用来把 proxy / governance 正式接入组织静态。",
        "- 当前版本的重点是把 DEF 14A 和治理风险显式落盘，不等同于完整 board deep dive。",
        "- 若 board profiles 仍为空，建议继续补充 `/org-scan` 或后续 board 专项脚本。",
    ])
    governance_summary_path.write_text("\n".join(lines), encoding="utf-8")

    return {
        "company": company,
        "proxy_count": proxy_count,
        "proxy_saved": bool(proxy_saved),
        "board_profiles": len(board_files),
        "board_profiles_created": board_profiles_created,
        "board_nominees": len(nominees),
        "governance_summary": str(governance_summary_path),
    }


if __name__ == "__main__":
    import sys

    ticker = sys.argv[1]
    company_name = sys.argv[2] if len(sys.argv) > 2 else None
    print(fetch_proxy_governance(ticker, company_name))
