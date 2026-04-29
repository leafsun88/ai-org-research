"""Source and skill discovery preflight for public-company collection."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any

from .common import PROJECT_ROOT, PublicCompanyTarget, relative_to_project, write_json, write_markdown, write_probe_report


SKILL_ROOTS = [
    PROJECT_ROOT / "学习" / "skills",
    Path.home() / ".codex" / "skills",
]

EXTERNAL_SKILL_DIRECTORIES = [
    {
        "name": "SkillsMP marketplace",
        "url": "https://skillsmp.com/zh",
        "use": "Large third-party SKILL.md marketplace with REST search and optional MCP server; inspect source and license before installing.",
    },
    {
        "name": "OpenAI skills catalog",
        "url": "https://github.com/openai/skills",
        "use": "First external place to check for Codex-compatible skills and examples.",
    },
    {
        "name": "The Skills Directory",
        "url": "https://theskills.directory/codex-skills",
        "use": "Searchable third-party directory for Codex SKILL.md examples.",
    },
    {
        "name": "skills.sh",
        "url": "https://skills.sh/",
        "use": "Third-party agent-skill index; use only after license/source review.",
    },
]

MARKET_GUIDES = {
    "US": [
        {
            "name": "SEC EDGAR APIs",
            "url": "https://www.sec.gov/search-filings/edgar-application-programming-interfaces",
            "use": "Canonical submissions and XBRL companyfacts source for US filings and facts.",
        },
        {
            "name": "SEC daily companyfacts bulk archive",
            "url": "https://www.sec.gov/Archives/edgar/daily-index/xbrl/companyfacts.zip",
            "use": "Bulk fallback when many issuers are collected.",
        },
    ],
    "HK": [
        {
            "name": "HKEXnews title search",
            "url": "https://www.hkexnews.hk/homelcicontentsearch.html",
            "use": "Listed company announcements, annual reports, prospectuses, and circulars.",
        },
        {
            "name": "HKEX investor FAQ",
            "url": "https://www.hkex.com.hk/global/exchange/faq/getting-started?sc_lang=en",
            "use": "Practical guidance for locating listed-company announcements and reports.",
        },
    ],
    "CN": [
        {
            "name": "CNINFO disclosure list",
            "url": "https://www.cninfo.com.cn/new/commonUrl?url=disclosure%2Flist%2Fnotice",
            "use": "Official A-share disclosure portal for periodic reports and announcements.",
        },
        {
            "name": "AKShare stock financial report documentation",
            "url": "https://akshare.akfamily.xyz/data/stock/stock.html",
            "use": "Free API wrappers for A-share financial statements and market data.",
        },
    ],
}

DATA_CATEGORY_GUIDES = [
    {
        "category": "market_data_and_peer_multiples",
        "sources": [
            {
                "name": "Yahoo chart JSON",
                "url": "https://query1.finance.yahoo.com/v8/finance/chart/{ticker}",
                "use": "Unauthenticated price history and last-price fallback.",
            },
            {
                "name": "StockAnalysis statistics pages",
                "url": "https://stockanalysis.com/stocks/{ticker}/statistics/",
                "use": "Public fallback for market cap, share count, and peer multiples; treat as medium confidence.",
            },
        ],
    },
    {
        "category": "semi_public_and_investor_views",
        "sources": [
            {
                "name": "local collect skill",
                "url": "local:ai-org-collect",
                "use": "Reuse query-map channels for podcasts, YouTube, Substack, official, jobs, social, and longform.",
            }
        ],
    },
    {
        "category": "institutional_holders",
        "sources": [
            {
                "name": "Nasdaq institutional holdings API",
                "url": "https://api.nasdaq.com/api/company/{ticker}/institutional-holdings",
                "use": "Free public holder table; retry and curl/http1 fallback because TLS/API availability can be unstable.",
            },
            {
                "name": "Holdings Channel by-stock 13F aggregate",
                "url": "https://www.holdingschannel.com/bystock/?symbol={ticker}",
                "use": "Free 13F aggregate fallback when Nasdaq API fails.",
            },
            {
                "name": "Paid holder APIs",
                "url": "user_required:paid_api_key",
                "use": "Ask the user for a paid API only after official/free/fallback sources fail or coverage is insufficient.",
            },
        ],
    },
]


def _read_frontmatter_description(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    lines = text.splitlines()
    description = ""
    name = path.parent.name
    if lines[:1] == ["---"]:
        for line in lines[1:40]:
            if line == "---":
                break
            if line.startswith("name:"):
                name = line.split(":", 1)[1].strip()
            if line.startswith("description:"):
                description = line.split(":", 1)[1].strip()
    return {"name": name, "description": description}


def _discover_local_skills(target: PublicCompanyTarget) -> list[dict[str, Any]]:
    terms = {
        "collect",
        "financial",
        "model",
        "public",
        "company",
        "xlsx",
        "spreadsheet",
        "social",
        "search",
        target.slug.lower(),
        target.ticker.lower(),
    }
    results: list[dict[str, Any]] = []
    seen: set[Path] = set()
    for root in SKILL_ROOTS:
        if not root.exists():
            continue
        for skill_file in root.rglob("SKILL.md"):
            if skill_file in seen:
                continue
            seen.add(skill_file)
            meta = _read_frontmatter_description(skill_file)
            haystack = f"{meta['name']} {meta['description']} {skill_file.parent.name}".lower()
            if any(term in haystack for term in terms):
                results.append(
                    {
                        **meta,
                        "path": str(skill_file),
                        "relative_path": relative_to_project(skill_file) if str(skill_file).startswith(str(PROJECT_ROOT)) else str(skill_file),
                    }
                )
    return sorted(results, key=lambda item: item["path"])


def discover_source_strategy(target: PublicCompanyTarget) -> dict[str, Any]:
    market = "CN" if target.market in {"A", "CN"} else target.market
    local_skills = _discover_local_skills(target)
    strategy = {
        "company": target.company_name,
        "ticker": target.ticker,
        "market": target.market,
        "status": "ok",
        "principle": "Before scraping data or source text, first discover existing skills, official APIs, public extraction guides, and source-specific caveats; record why each chosen source is used.",
        "local_skills": local_skills,
        "external_skill_directories": EXTERNAL_SKILL_DIRECTORIES,
        "market_guides": MARKET_GUIDES.get(market, []),
        "data_category_guides": DATA_CATEGORY_GUIDES,
        "required_next_step": "Use official or well-documented sources first; if a source lacks documentation or reproducible extraction rules, write an extraction gap instead of inventing data.",
        "updated_at": datetime.now().isoformat(timespec="seconds"),
    }
    root = target.public_company_root / "metadata"
    write_json(root / "source_strategy.json", strategy)
    skill_lines = [f"- {item['name']}: `{item['path']}`" for item in local_skills] or ["- none"]
    guide_lines = [f"- {item['name']}: {item['url']} ({item['use']})" for item in strategy["market_guides"]] or ["- none"]
    directory_lines = [f"- {item['name']}: {item['url']}" for item in EXTERNAL_SKILL_DIRECTORIES]
    write_markdown(
        root / "source_strategy.md",
        [
            f"# {target.company_name} Source Strategy",
            "",
            f"- Status: {strategy['status']}",
            f"- Principle: {strategy['principle']}",
            "",
            "## Local Skills",
            *skill_lines,
            "",
            "## External Skill Directories",
            *directory_lines,
            "",
            "## Market Guides",
            *guide_lines,
        ],
    )
    write_probe_report(target, "source_strategy", {"status": "ok", "items": local_skills, "gaps": []})
    return strategy
