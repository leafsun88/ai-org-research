---
name: financial-statement-analysis
description: Analyze corporate financial statements and produce a structured write-up covering data sourcing, three-statement sanity checks, trend tables, key ratios, cash-flow quality, and red-flag detection. USE THIS SKILL whenever the user shares a financial filing, annual report, earnings release, PDF link, or pasted financial tables — even if they only ask a casual question like "分析一下这份财报", "这家公司怎么样", "帮我看看这个年报", "这只股票基本面如何", or provides a ticker alongside any financial data. Also trigger when the user asks to compare two companies' financials, or asks follow-up questions about numbers from a filing already in the conversation. Do NOT wait for the user to explicitly ask for a "framework" or "analysis template" — trigger proactively on any financial filing context. Ask before applying to banks, insurers, brokers, REITs, or property developers because ratio definitions differ for those sectors.
---

## Before anything else — handle the data source

The quality of the analysis depends entirely on whether the underlying numbers are trustworthy. Do this first, before writing a single ratio.

### If a PDF URL was provided
Attempt `web_fetch` on the URL. If the fetch succeeds and returns readable text, extract the core financial tables. If the fetch fails or returns empty/garbled content (common with exchange servers like SSE, SZSE, HKEX):
1. Note clearly: "PDF could not be fetched directly — using secondary source"
2. Search for the filing data via `web_search` using company name + year + "年度报告" + "主要财务数据"
3. Fetch a reliable secondary source (Sina Finance, 东方财富, official company IR page)
4. Clearly label every number with its source: `[年报原文]` or `[二手来源: XXX]`

**Never silently blend primary and secondary sources.** If a number came from a news article rather than the filing itself, say so.

### Tag every data point before using it

| Tag | Meaning | Rule |
|---|---|---|
| `[直接]` | Appears verbatim in the filing | Can be stated as fact |
| `[推算]` | Computed from filing numbers | Must show the formula inline |
| `[推断]` | Inferred from context, not stated | Must be flagged or dropped |
| `[二手]` | From secondary source, not filing | Must cite the source name |

`[推断]` items must never be presented as facts. Either drop them or explicitly flag: "根据上下文推断，未经年报直接披露."

---

## Step 1 — Normalize the input

- Confirm reporting scope: consolidated vs standalone, annual vs interim
- Confirm accounting standard: PRC GAAP / IFRS / US GAAP
- Confirm unit and currency — unit mismatches (万元 vs 元) are the most common arithmetic error
- Note any major M&A, disposals, or accounting policy changes that break comparability
- If source is PDF or HTML, extract core rows into a structured table before analysis

---

## Step 2 — Mandatory data extraction checklist

Collect these fields before writing any analysis. Mark `—` if genuinely missing; do not estimate.

### Income statement (3 years where available)
| Field | Tag | Notes |
|---|---|---|
| 营业收入 | [直接] | |
| 营业成本 | [直接] | |
| 毛利率 | [直接] or [推算: (rev-cogs)/rev] | |
| 归母净利润 | [直接] | **Required** |
| **扣非净利润** | [直接] | **Required — always extract both** |
| 非经常性损益合计 | [直接] | Explain gap if \|np − np_ex\| > 10% of np |
| 营业利润 | [直接] | |
| 研发/销售/管理/财务费用 | [直接] | |

### Cash flow statement
| Field | Tag | Notes |
|---|---|---|
| 经营活动现金流净额 (CFO) — **all years** | [直接] | Record trend, not just latest year |
| 资本开支 (capex) | [直接] or [推算] | For FCF |
| FCF | [推算: CFO − capex] | |
| CFO / 归母净利润 | [推算] | Quality check: sustained < 1× is a concern |

### Balance sheet
| Field | Tag |
|---|---|
| 总资产 | [直接] |
| 总负债 | [直接] |
| 归属股东净资产 | [直接] |
| 货币资金 | [直接] |
| 存货 | [直接] |
| 应收账款 | [直接] |
| 有息负债（短期借款+长期借款） | [直接] |
| 资产负债率 | [直接] or [推算: 负债/总资产] |

---

## Step 3 — Three-statement sanity checks

Run these before drawing any conclusions:

1. **Balance sheet identity**: 总资产 = 总负债 + 股东权益（含少数股东）. Flag if it doesn't balance.
2. **Net income linkage**: 期末净资产 ≈ 期初净资产 + 归母净利润 − 分红 ± OCI. Large unexplained gaps = red flag.
3. **Cash conversion**: CFO vs 归母净利润 across multiple years. Sustained CFO < net income = earnings quality concern.
4. **Production-sales-inventory check** (where volume data is disclosed): 期初库存 + 产量 ≈ 销量 + 期末库存. Residual > ~2% of production = note and explain.

If a key statement is missing or a fetch failed, explicitly state: **"三表勾稽不完整，缺少 [X 表]，以下分析基于可用数据."** Do not silently skip this check.

---

## Step 4 — Analysis order

1. Data quality and source transparency (Steps above)
2. Operating trend: revenue, gross margin, cost structure, product/segment/geography mix
3. Profit quality: 归母净利润 vs 扣非净利润 — explain any divergence in plain language
4. Cash flow quality: CFO conversion trend, FCF, working capital behavior
5. Balance sheet: leverage, liquidity, asset composition, notable items
6. Key ratios (see `references/ratios.md`)
7. Red flags: 3–7 items only, each with current value + prior-year trend + plain-language impact
8. Follow-ups: specific unanswered questions for the full filing or management

**Do not jump to conclusions if data quality is uncertain.**
**Do not use valuation language if accounting quality is unclear.**

---

## Step 5 — Write the analysis

Use the structure in `assets/report_template.md`. Key rules for each section:

**One-sentence conclusion** — what changed and why it matters. Be specific.

**Operating trend** — always distinguish volume vs price effects where data allows (e.g. "销量+39%但均价−16%"). Segment or geographic breakdown if available.

**Profit quality** — present 归母净利润 and 扣非净利润 side by side in every analysis. If they diverge >10%, identify the non-recurring items and state whether they are likely to recur. This is the most commonly omitted step — do not skip it.

**Cash flow quality** — show CFO/net income ratio for each year available. If capex is available, compute FCF. A company with rising profits but falling CFO conversion needs an explicit explanation.

**Balance sheet** — leverage trend, liquidity position, working capital cycle, any outsized single items (e.g. goodwill, large inventory, high payables days).

**Red flags** — each flag must include:
- The current value with units `[直接]` or `[推算: formula]`
- Prior-year value for comparison (direction of trend)
- One-sentence plain-language "so what"

**Follow-ups** — concrete questions that require the full filing, MD&A, or earnings call to resolve.

---

## Derived metric labeling rules

Any computed number must show its formula inline or in a note. No exceptions.

| Metric | Required label format |
|---|---|
| 净利率 | 推算：归母净利润 ÷ 营业收入 |
| 每GWh/吨均价 | 推算：收入 ÷ 销量（GWh/万吨/千升） |
| 人均创收 | 推算：营业收入 ÷ 总员工数；若总员工数本身为推算，show that formula too |
| CFO/净利润 | 推算：CFO ÷ 归母净利润 |
| 净现金 | 推算：货币资金 + 交易性金融资产 − 有息负债 |
| FCF | 推算：CFO − capex |

This labeling rule applies in ALL output formats — structured analysis, social media posts, table cells, and inline commentary.

---

## Sector flags — confirm before proceeding

For these sectors, standard ratios do not apply without modification. Confirm with the user first:
- Banks / insurance / securities brokers (debt is operating input; PB and ROE-DDM replace EV/EBITDA)
- REITs (NAV-based; FFO replaces net income)
- Property developers (pre-sales recognition; NAV and cash collection rate matter more than income)
- Early-stage pre-revenue companies (no earnings; EV/Revenue or pipeline NPV)

---

## Load extra files when relevant

- `references/ratios.md` — ratio formulas and pitfalls (read for Step 4)
- `assets/report_template.md` — structured output shell (use for Step 5)
- `assets/example_input.csv` — minimal CSV format for the compute script
- `scripts/compute_ratios.py` — run for repeatable ratio calculations on tabular data
