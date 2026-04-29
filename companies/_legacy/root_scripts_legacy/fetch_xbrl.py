"""
SEC EDGAR XBRL 财务数据提取器
================================
从SEC EDGAR companyfacts API获取完整历史财务数据。
比yfinance更长的时间序列，更多指标，季度+年度全覆盖。

输出: {TICKER}/financials_detailed.md
"""

import sys
import json
import requests
from pathlib import Path
from datetime import datetime
from collections import defaultdict

DB_DIR = Path(__file__).parent.parent
HEADERS = {'User-Agent': 'InvestmentResearch research@example.com'}

# ── CIK lookup ──
_CIK_CACHE = {}

def _load_cik_map():
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

def get_cik(ticker: str):
    cik_map = _load_cik_map()
    return cik_map.get(ticker.upper())


# ── XBRL Data Extraction ──

def fetch_company_facts(ticker: str):
    """Fetch all XBRL facts from SEC EDGAR."""
    cik = get_cik(ticker)
    if not cik:
        print(f"  ✗ Could not find CIK for {ticker}")
        return None

    url = f'https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json'
    r = requests.get(url, headers=HEADERS, timeout=30)
    if r.status_code != 200:
        print(f"  ✗ EDGAR XBRL error: {r.status_code}")
        return None

    return r.json()


def extract_quarterly_values(facts: dict, concept: str) -> dict:
    """
    Extract quarterly-only values for a concept.
    Returns dict: {'2025Q3': value, '2025Q2': value, ...}

    XBRL quirk: 10-Q filings report cumulative YTD numbers.
    We need to find the single-quarter entries (with CY frame like CY2025Q3)
    or calculate them from cumulative data.
    """
    gaap = facts.get('facts', {}).get('us-gaap', {})
    concept_data = gaap.get(concept, {})
    units = concept_data.get('units', {})

    result = {}

    for unit_type, datapoints in units.items():
        if unit_type not in ('USD', 'USD/shares', 'shares', 'pure'):
            continue

        for dp in datapoints:
            frame = dp.get('frame', '')
            form = dp.get('form', '')
            fp = dp.get('fp', '')
            start = dp.get('start', '')
            end = dp.get('end', '')
            val = dp.get('val')

            if val is None:
                continue

            # Method 1: Use CY frame (e.g., CY2025Q3) - these are single quarter values
            if frame and 'Q' in frame and frame.startswith('CY'):
                # e.g., CY2025Q3 -> 2025Q3
                q_label = frame[2:]  # Remove 'CY' prefix
                result[q_label] = val

            # Method 2: For annual (10-K), use CY frame
            elif frame and frame.startswith('CY') and 'Q' not in frame and form == '10-K':
                # e.g., CY2025 -> 2025
                y_label = frame[2:]
                result[y_label] = val

    return result


def extract_instant_values(facts: dict, concept: str) -> dict:
    """
    Extract point-in-time balance sheet values.
    Returns dict: {'2025Q4': value, '2025Q3': value, ...}
    """
    gaap = facts.get('facts', {}).get('us-gaap', {})
    concept_data = gaap.get(concept, {})
    units = concept_data.get('units', {})

    result = {}

    for unit_type, datapoints in units.items():
        if unit_type not in ('USD', 'shares'):
            continue

        for dp in datapoints:
            form = dp.get('form', '')
            end = dp.get('end', '')
            fp = dp.get('fp', '')
            val = dp.get('val')

            if val is None or form not in ('10-K', '10-Q'):
                continue

            # Parse end date to quarter label
            try:
                dt = datetime.strptime(end, '%Y-%m-%d')
                q = (dt.month - 1) // 3 + 1
                if form == '10-K':
                    # Annual filing - label as Q4
                    q_label = f"{dt.year}Q4"
                    y_label = str(dt.year)
                    result[y_label] = val
                    result[q_label] = val
                else:
                    q_label = f"{dt.year}Q{q}"
                    result[q_label] = val
            except ValueError:
                continue

    return result


def fmt_val(v, unit='money'):
    """Format a value for display."""
    if v is None:
        return "N/A"

    if unit == 'pct':
        return f"{v:.1f}%"
    elif unit == 'ratio':
        return f"{v:.2f}"
    elif unit == 'eps':
        return f"${v:.2f}"
    elif unit == 'shares':
        v = float(v)
        if abs(v) >= 1e9:
            return f"{v/1e9:.2f}B"
        if abs(v) >= 1e6:
            return f"{v/1e6:.0f}M"
        return f"{v:,.0f}"
    else:  # money
        v = float(v)
        sign = "-" if v < 0 else ""
        av = abs(v)
        if av >= 1e12:
            return f"{sign}${av/1e12:.2f}T"
        if av >= 1e9:
            return f"{sign}${av/1e9:.2f}B"
        if av >= 1e6:
            return f"{sign}${av/1e6:.0f}M"
        if av >= 1e3:
            return f"{sign}${av/1e3:.0f}K"
        return f"{sign}${av:.0f}"


def calc_pct(num, denom):
    if num is None or denom is None or denom == 0:
        return None
    return num / denom * 100


def calc_yoy(current, previous):
    if current is None or previous is None or previous == 0:
        return None
    return (current - previous) / abs(previous) * 100


def build_detailed_financials(ticker: str, facts: dict) -> str:
    """Build comprehensive financials markdown from XBRL data."""

    entity_name = facts.get('entityName', ticker)

    # ── Extract all data ──
    # Income statement (flow metrics - need quarterly extraction)
    revenue = extract_quarterly_values(facts, 'RevenueFromContractWithCustomerExcludingAssessedTax')
    if not revenue:
        revenue = extract_quarterly_values(facts, 'Revenues')

    cost_of_rev = extract_quarterly_values(facts, 'CostOfRevenue')
    operating_income = extract_quarterly_values(facts, 'OperatingIncomeLoss')
    net_income = extract_quarterly_values(facts, 'NetIncomeLoss')
    rd_expense = extract_quarterly_values(facts, 'ResearchAndDevelopmentExpense')
    sga_expense = extract_quarterly_values(facts, 'SellingGeneralAndAdministrativeExpense')
    if not sga_expense:
        sga_expense = extract_quarterly_values(facts, 'SellingAndMarketingExpense')
    interest_expense = extract_quarterly_values(facts, 'InterestExpense')
    tax_expense = extract_quarterly_values(facts, 'IncomeTaxExpenseBenefit')
    dda = extract_quarterly_values(facts, 'DepreciationDepletionAndAmortization')
    sbc = extract_quarterly_values(facts, 'AllocatedShareBasedCompensationExpense')
    eps_diluted = extract_quarterly_values(facts, 'EarningsPerShareDiluted')
    eps_basic = extract_quarterly_values(facts, 'EarningsPerShareBasic')
    shares_diluted = extract_quarterly_values(facts, 'WeightedAverageNumberOfDilutedSharesOutstanding')
    total_expenses = extract_quarterly_values(facts, 'CostsAndExpenses')
    amortization_intangibles = extract_quarterly_values(facts, 'AmortizationOfIntangibleAssets')

    # Balance sheet (instant/point-in-time)
    cash = extract_instant_values(facts, 'CashAndCashEquivalentsAtCarryingValue')
    total_assets = extract_instant_values(facts, 'Assets')
    current_assets = extract_instant_values(facts, 'AssetsCurrent')
    accounts_recv = extract_instant_values(facts, 'AccountsReceivableNetCurrent')
    goodwill = extract_instant_values(facts, 'Goodwill')
    intangibles = extract_instant_values(facts, 'GoodwillAndOtherIntangibleAssets')
    equity = extract_instant_values(facts, 'StockholdersEquity')
    total_liabilities = extract_instant_values(facts, 'Liabilities')
    if not total_liabilities:
        total_liabilities = extract_instant_values(facts, 'LiabilitiesCurrent')
    long_term_debt = extract_instant_values(facts, 'LongTermDebt')
    if not long_term_debt:
        long_term_debt = extract_instant_values(facts, 'LongTermDebtNoncurrent')
    current_liabilities = extract_instant_values(facts, 'LiabilitiesCurrent')
    retained_earnings = extract_instant_values(facts, 'RetainedEarningsAccumulatedDeficit')
    shares_outstanding = extract_instant_values(facts, 'CommonStockSharesOutstanding')
    contract_liability = extract_instant_values(facts, 'ContractWithCustomerLiabilityCurrent')
    accrued_liab = extract_instant_values(facts, 'AccruedLiabilitiesCurrent')
    ppe = extract_instant_values(facts, 'PropertyPlantAndEquipmentNet')

    # Cash flow (flow metrics)
    operating_cf = extract_quarterly_values(facts, 'NetCashProvidedByUsedInOperatingActivities')
    capex = extract_quarterly_values(facts, 'PaymentsToAcquirePropertyPlantAndEquipment')
    buybacks = extract_quarterly_values(facts, 'PaymentsForRepurchaseOfCommonStock')
    if not buybacks:
        buybacks = extract_quarterly_values(facts, 'PaymentsForRepurchaseOfEquity')
    debt_repay = extract_quarterly_values(facts, 'RepaymentsOfDebt')
    if not debt_repay:
        debt_repay = extract_quarterly_values(facts, 'RepaymentsOfLongTermDebt')
    debt_issue = extract_quarterly_values(facts, 'ProceedsFromIssuanceOfLongTermDebt')

    # ── Build markdown ──
    lines = []
    lines.append("---")
    lines.append(f"ticker: {ticker}")
    lines.append(f"company: {entity_name}")
    lines.append(f"last_updated: {datetime.now().strftime('%Y-%m-%d')}")
    lines.append("data_source: SEC EDGAR XBRL (companyfacts API)")
    lines.append("---")
    lines.append("")
    lines.append(f"# {entity_name} ({ticker}) — 详细财务数据")
    lines.append("")

    # ── ANNUAL TABLE ──
    annual_keys = sorted([k for k in revenue.keys() if 'Q' not in k], reverse=True)

    if annual_keys:
        lines.append("## 年度损益表 (完整历史)")
        headers = ["指标"] + annual_keys
        lines.append("| " + " | ".join(headers) + " |")
        lines.append("| " + " | ".join(["---"] * len(headers)) + " |")

        def annual_row(name, data, unit='money'):
            row = [f"**{name}**"]
            for k in annual_keys:
                row.append(fmt_val(data.get(k), unit))
            lines.append("| " + " | ".join(row) + " |")

        def annual_derived_row(name, numerator, denominator, unit='pct'):
            row = [f"**{name}**"]
            for k in annual_keys:
                val = calc_pct(numerator.get(k), denominator.get(k))
                row.append(fmt_val(val, unit) if val is not None else "N/A")
            lines.append("| " + " | ".join(row) + " |")

        def annual_yoy_row(name, data):
            row = [f"**{name}**"]
            for i, k in enumerate(annual_keys):
                prev_year = str(int(k) - 1) if k.isdigit() else None
                if prev_year and prev_year in data and data.get(k):
                    yoy = calc_yoy(data[k], data[prev_year])
                    row.append(f"{yoy:+.1f}%" if yoy is not None else "N/A")
                else:
                    row.append("N/A")
            lines.append("| " + " | ".join(row) + " |")

        annual_row("营收", revenue)
        annual_yoy_row("营收YoY", revenue)
        annual_row("营业成本", cost_of_rev)

        # Gross profit (calculated)
        gross_profit = {}
        for k in annual_keys:
            if revenue.get(k) and cost_of_rev.get(k):
                gross_profit[k] = revenue[k] - cost_of_rev[k]
        annual_row("毛利润", gross_profit)
        annual_derived_row("毛利率", gross_profit, revenue)

        annual_row("研发费用", rd_expense)
        annual_derived_row("研发占营收%", rd_expense, revenue)
        annual_row("销售管理费", sga_expense)
        annual_row("运营总支出", total_expenses)
        annual_row("营业利润", operating_income)
        annual_derived_row("营业利润率", operating_income, revenue)
        annual_row("利息支出", interest_expense)
        annual_row("所得税", tax_expense)
        annual_row("净利润", net_income)
        annual_derived_row("净利润率", net_income, revenue)
        annual_row("折旧摊销(D&A)", dda)
        annual_row("无形资产摊销", amortization_intangibles)
        annual_row("股权激励(SBC)", sbc)
        annual_derived_row("SBC占营收%", sbc, revenue)

        # EBITDA (calculated)
        ebitda = {}
        for k in annual_keys:
            if operating_income.get(k) is not None and dda.get(k) is not None:
                ebitda[k] = operating_income[k] + dda[k]
        annual_row("EBITDA (计算)", ebitda)
        annual_derived_row("EBITDA利润率", ebitda, revenue)

        annual_row("稀释EPS", eps_diluted, 'eps')
        annual_row("基本EPS", eps_basic, 'eps')
        annual_row("稀释股数", shares_diluted, 'shares')
        lines.append("")

    # ── QUARTERLY INCOME TABLE ──
    quarterly_keys = sorted([k for k in revenue.keys() if 'Q' in k], reverse=True)

    if quarterly_keys:
        lines.append(f"## 季度损益表 ({len(quarterly_keys)}个季度完整历史)")
        headers = ["指标"] + quarterly_keys
        lines.append("| " + " | ".join(headers) + " |")
        lines.append("| " + " | ".join(["---"] * len(headers)) + " |")

        def q_row(name, data, unit='money'):
            row = [f"**{name}**"]
            for k in quarterly_keys:
                row.append(fmt_val(data.get(k), unit))
            lines.append("| " + " | ".join(row) + " |")

        def q_derived_row(name, numerator, denominator, unit='pct'):
            row = [f"**{name}**"]
            for k in quarterly_keys:
                val = calc_pct(numerator.get(k), denominator.get(k))
                row.append(fmt_val(val, unit) if val is not None else "N/A")
            lines.append("| " + " | ".join(row) + " |")

        def q_yoy_row(name, data):
            row = [f"**{name}**"]
            for k in quarterly_keys:
                # Find same quarter last year
                try:
                    year = int(k[:4])
                    q = k[4:]
                    prev = f"{year-1}{q}"
                    if prev in data and data.get(k):
                        yoy = calc_yoy(data[k], data[prev])
                        row.append(f"{yoy:+.1f}%" if yoy is not None else "N/A")
                    else:
                        row.append("N/A")
                except:
                    row.append("N/A")
            lines.append("| " + " | ".join(row) + " |")

        q_row("营收", revenue)
        q_yoy_row("营收YoY", revenue)
        q_row("营业成本", cost_of_rev)

        # Gross profit quarterly
        gp_q = {}
        for k in quarterly_keys:
            if revenue.get(k) and cost_of_rev.get(k):
                gp_q[k] = revenue[k] - cost_of_rev[k]
        q_row("毛利润", gp_q)
        q_derived_row("毛利率", gp_q, revenue)

        q_row("研发费用", rd_expense)
        q_derived_row("研发占营收%", rd_expense, revenue)
        q_row("营业利润", operating_income)
        q_derived_row("营业利润率", operating_income, revenue)
        q_row("净利润", net_income)
        q_derived_row("净利润率", net_income, revenue)
        q_row("D&A", dda)
        q_row("SBC", sbc)
        q_derived_row("SBC占营收%", sbc, revenue)
        q_row("所得税", tax_expense)

        # Effective tax rate
        pretax = {}
        for k in quarterly_keys:
            if net_income.get(k) is not None and tax_expense.get(k) is not None:
                pretax[k] = net_income[k] + tax_expense[k]
        q_derived_row("有效税率", tax_expense, pretax)

        q_row("稀释EPS", eps_diluted, 'eps')
        q_row("稀释股数", shares_diluted, 'shares')
        lines.append("")

    # ── QUARTERLY BALANCE SHEET ──
    bs_quarterly_keys = sorted([k for k in cash.keys() if 'Q' in k], reverse=True)

    if bs_quarterly_keys:
        lines.append(f"## 季度资产负债表 ({len(bs_quarterly_keys)}个季度)")
        headers = ["指标"] + bs_quarterly_keys
        lines.append("| " + " | ".join(headers) + " |")
        lines.append("| " + " | ".join(["---"] * len(headers)) + " |")

        def bs_row(name, data, unit='money'):
            row = [f"**{name}**"]
            for k in bs_quarterly_keys:
                row.append(fmt_val(data.get(k), unit))
            lines.append("| " + " | ".join(row) + " |")

        bs_row("现金", cash)
        bs_row("应收账款", accounts_recv)
        bs_row("流动资产", current_assets)
        bs_row("商誉", goodwill)
        bs_row("商誉+无形", intangibles)
        bs_row("PP&E", ppe)
        bs_row("总资产", total_assets)
        bs_row("流动负债", current_liabilities)
        bs_row("应计负债", accrued_liab)
        bs_row("合同负债(递延收入)", contract_liability)
        bs_row("长期债务", long_term_debt)
        bs_row("股东权益", equity)
        bs_row("留存收益", retained_earnings)
        bs_row("流通股", shares_outstanding, 'shares')

        # Derived metrics
        row = ["**净现金/净负债**"]
        for k in bs_quarterly_keys:
            c = cash.get(k, 0) or 0
            d = long_term_debt.get(k, 0) or 0
            row.append(fmt_val(c - d) if (cash.get(k) or long_term_debt.get(k)) else "N/A")
        lines.append("| " + " | ".join(row) + " |")

        row = ["**有形账面价值**"]
        for k in bs_quarterly_keys:
            e = equity.get(k)
            gi = intangibles.get(k, 0) or 0
            row.append(fmt_val(e - gi) if e is not None else "N/A")
        lines.append("| " + " | ".join(row) + " |")

        # DSO (Days Sales Outstanding)
        row = ["**DSO (天)**"]
        for k in bs_quarterly_keys:
            ar = accounts_recv.get(k)
            rev = revenue.get(k)
            if ar and rev and rev > 0:
                dso = ar / rev * 90  # Quarterly revenue * 90 days
                row.append(f"{dso:.0f}")
            else:
                row.append("N/A")
        lines.append("| " + " | ".join(row) + " |")

        lines.append("")

    # ── CASH FLOW (Annual + per-quarter if available) ──
    cf_annual = sorted([k for k in operating_cf.keys() if 'Q' not in k], reverse=True)
    if cf_annual:
        lines.append("## 年度现金流")
        headers = ["指标"] + cf_annual
        lines.append("| " + " | ".join(headers) + " |")
        lines.append("| " + " | ".join(["---"] * len(headers)) + " |")

        def cf_row(name, data, unit='money'):
            row = [f"**{name}**"]
            for k in cf_annual:
                row.append(fmt_val(data.get(k), unit))
            lines.append("| " + " | ".join(row) + " |")

        cf_row("经营性现金流", operating_cf)
        cf_row("资本开支", capex)

        # FCF
        fcf = {}
        for k in cf_annual:
            ocf = operating_cf.get(k)
            cx = capex.get(k, 0) or 0
            if ocf is not None:
                fcf[k] = ocf - cx  # capex is reported as positive payment
        cf_row("自由现金流", fcf)

        # FCF margin
        row = ["**FCF利润率**"]
        for k in cf_annual:
            f = fcf.get(k)
            r = revenue.get(k)
            if f and r and r > 0:
                row.append(f"{f/r*100:.1f}%")
            else:
                row.append("N/A")
        lines.append("| " + " | ".join(row) + " |")

        cf_row("股票回购", buybacks)
        cf_row("偿还债务", debt_repay)
        cf_row("发行债务", debt_issue)
        cf_row("SBC", sbc)
        lines.append("")

    # ── KEY RATIOS (Derived, quarterly) ──
    if quarterly_keys and bs_quarterly_keys:
        lines.append("## 季度关键比率")
        # Use union of quarterly keys
        all_q = sorted(set(quarterly_keys) & set(bs_quarterly_keys), reverse=True)
        if all_q:
            headers = ["指标"] + all_q
            lines.append("| " + " | ".join(headers) + " |")
            lines.append("| " + " | ".join(["---"] * len(headers)) + " |")

            # Gross margin
            row = ["**毛利率**"]
            for k in all_q:
                gp = gp_q.get(k) if 'gp_q' in dir() else None
                r = revenue.get(k)
                if gp and r and r > 0:
                    row.append(f"{gp/r*100:.1f}%")
                elif revenue.get(k) and cost_of_rev.get(k):
                    gm = (revenue[k] - cost_of_rev[k]) / revenue[k] * 100
                    row.append(f"{gm:.1f}%")
                else:
                    row.append("N/A")
            lines.append("| " + " | ".join(row) + " |")

            # Operating margin
            row = ["**营业利润率**"]
            for k in all_q:
                oi = operating_income.get(k)
                r = revenue.get(k)
                row.append(f"{oi/r*100:.1f}%" if oi and r and r > 0 else "N/A")
            lines.append("| " + " | ".join(row) + " |")

            # Net margin
            row = ["**净利润率**"]
            for k in all_q:
                ni = net_income.get(k)
                r = revenue.get(k)
                row.append(f"{ni/r*100:.1f}%" if ni and r and r > 0 else "N/A")
            lines.append("| " + " | ".join(row) + " |")

            # SBC as % of revenue
            row = ["**SBC占营收%**"]
            for k in all_q:
                s = sbc.get(k)
                r = revenue.get(k)
                row.append(f"{s/r*100:.1f}%" if s and r and r > 0 else "N/A")
            lines.append("| " + " | ".join(row) + " |")

            # R&D intensity
            row = ["**研发强度**"]
            for k in all_q:
                rd = rd_expense.get(k)
                r = revenue.get(k)
                row.append(f"{rd/r*100:.1f}%" if rd and r and r > 0 else "N/A")
            lines.append("| " + " | ".join(row) + " |")

            # Debt to equity
            row = ["**负债权益比**"]
            for k in all_q:
                d = long_term_debt.get(k)
                e = equity.get(k)
                row.append(f"{d/e:.1f}x" if d and e and e > 0 else "N/A")
            lines.append("| " + " | ".join(row) + " |")

            # Revenue per share
            row = ["**每股营收**"]
            for k in all_q:
                r = revenue.get(k)
                s = shares_diluted.get(k) or shares_outstanding.get(k)
                row.append(f"${r/s:.2f}" if r and s and s > 0 else "N/A")
            lines.append("| " + " | ".join(row) + " |")

            lines.append("")

    lines.append("---")
    lines.append(f"*数据来源: SEC EDGAR XBRL (companyfacts API)*")
    lines.append(f"*提取时间: {datetime.now().strftime('%Y-%m-%d %H:%M')}*")

    return "\n".join(lines)


def fetch_xbrl_financials(ticker: str):
    """Main entry: fetch XBRL data and generate detailed financials markdown."""
    print(f"[XBRL] Fetching detailed financials for {ticker}...")

    facts = fetch_company_facts(ticker)
    if not facts:
        return False

    entity_name = facts.get('entityName', ticker)
    gaap = facts.get('facts', {}).get('us-gaap', {})
    print(f"  Company: {entity_name}")
    print(f"  Available concepts: {len(gaap)}")

    md = build_detailed_financials(ticker, facts)

    company_dir = DB_DIR / ticker
    company_dir.mkdir(parents=True, exist_ok=True)

    output_path = company_dir / "financials_detailed.md"
    output_path.write_text(md, encoding='utf-8')

    line_count = md.count('\n')
    print(f"  ✓ financials_detailed.md ({line_count} lines, {len(md):,} chars)")

    # Also save raw facts as JSON for future use
    raw_path = company_dir / "_xbrl_facts.json"
    with open(raw_path, 'w') as f:
        json.dump(facts, f)
    print(f"  ✓ _xbrl_facts.json ({len(json.dumps(facts)):,} chars)")

    return True


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python fetch_xbrl.py TICKER")
        sys.exit(1)

    ticker = sys.argv[1]
    fetch_xbrl_financials(ticker)
