"""Run the installed officecli-financial-model skill on SNDK data.

This runner intentionally uses officecli commands to build the workbook so the
installed skill's workflow is exercised in a fresh experiment folder.
"""

from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path("/Users/leafsun/Desktop/AI Org研究")
RUN_ROOT = PROJECT_ROOT / "experiments" / "skillsmp_officecli_financial_model" / "run_sndk_officecli"
PUBLIC_COMPANY_ROOT = PROJECT_ROOT / "companies" / "sandisk" / "vault" / "public_company"
MODEL_PATH = RUN_ROOT / "sndk_officecli_financial_model.xlsx"


SHEETS = [
    "Dashboard",
    "Assumptions",
    "Income Statement",
    "Balance Sheet",
    "Cash Flow",
    "DCF Valuation",
    "Sensitivity",
    "Error Checks",
    "Sources",
]


PERIODS = ["2023A", "2024A", "2025A", "Y1", "Y2", "Y3", "Y4", "Y5"]


def run(args: list[str], *, input_text: str | None = None, check: bool = True) -> subprocess.CompletedProcess[str]:
    command = [shutil.which("officecli") or str(Path.home() / ".local" / "bin" / "officecli"), *args]
    result = subprocess.run(command, input=input_text, text=True, capture_output=True)
    if check and result.returncode != 0:
        raise RuntimeError(f"Command failed: {' '.join(command)}\nSTDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}")
    return result


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def number(value: Any, default: float = 0.0) -> float:
    if value in {None, ""}:
        return default
    if isinstance(value, str):
        value = value.replace(",", "").replace("$", "").replace("%", "")
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def ratio(numerator: Any, denominator: Any, default: float = 0.0) -> float:
    denominator_f = number(denominator)
    if denominator_f == 0:
        return default
    return number(numerator) / denominator_f


def cell(col: int, row: int) -> str:
    letters = ""
    while col:
        col, remainder = divmod(col - 1, 26)
        letters = chr(65 + remainder) + letters
    return f"{letters}{row}"


def set_op(sheet: str, address: str, props: dict[str, Any]) -> dict[str, Any]:
    return {"command": "set", "path": f"/{sheet}/{address}", "props": {k: str(v) for k, v in props.items() if v is not None}}


def sheet_op(sheet: str, props: dict[str, Any]) -> dict[str, Any]:
    return {"command": "set", "path": f"/{sheet}", "props": {k: str(v) for k, v in props.items() if v is not None}}


def batch(ops: list[dict[str, Any]]) -> None:
    for start in range(0, len(ops), 18):
        payload = json.dumps(ops[start : start + 18], ensure_ascii=False)
        run(["batch", str(MODEL_PATH)], input_text=payload)


def build_context() -> dict[str, Any]:
    annual = load_json(PUBLIC_COMPANY_ROOT / "data" / "statements" / "annual_statements.json")["periods"]
    valuation = load_json(PUBLIC_COMPANY_ROOT / "data" / "valuation" / "valuation_snapshot.json")
    latest = annual[-1]
    actuals = annual[-3:]
    return {
        "annual": actuals,
        "valuation": valuation,
        "latest": latest,
        "company": "Sandisk",
        "ticker": "SNDK",
    }


def create_workbook() -> None:
    RUN_ROOT.mkdir(parents=True, exist_ok=True)
    if MODEL_PATH.exists():
        MODEL_PATH.unlink()
    run(["create", str(MODEL_PATH)])
    run(["open", str(MODEL_PATH)])
    for sheet in SHEETS:
        run(["add", str(MODEL_PATH), "/", "--type", "sheet", "--prop", f"name={sheet}"])
    run(["remove", str(MODEL_PATH), "/Sheet1"], check=False)


def populate_assumptions(ctx: dict[str, Any]) -> None:
    latest = ctx["latest"]
    actuals = ctx["annual"]
    valuation = ctx["valuation"]
    ops: list[dict[str, Any]] = []
    for idx, period in enumerate(PERIODS, start=2):
        ops.append(set_op("Assumptions", cell(idx, 1), {"value": period, "bold": "true", "fill": "1F3864", "font.color": "FFFFFF"}))
    ops.append(set_op("Assumptions", "A1", {"value": "SNDK Financial Model Assumptions", "bold": "true", "fill": "1F3864", "font.color": "FFFFFF"}))
    rows = {
        2: ("Revenue Growth", [None, ratio(actuals[1]["revenue"], actuals[0]["revenue"]) - 1, ratio(actuals[2]["revenue"], actuals[1]["revenue"]) - 1, 0.05, 0.05, 0.05, 0.05, 0.05], "0.0%"),
        3: ("Revenue", [row.get("revenue") for row in actuals] + [None] * 5, "$#,##0"),
        4: ("Gross Margin", [ratio(row.get("gross_profit"), row.get("revenue")) for row in actuals] + [0.30, 0.32, 0.34, 0.35, 0.36], "0.0%"),
        5: ("Operating Margin", [ratio(row.get("operating_income"), row.get("revenue")) for row in actuals] + [0.12, 0.14, 0.16, 0.17, 0.18], "0.0%"),
        6: ("Tax Rate", [0.21] * 8, "0.0%"),
        7: ("D&A % Revenue", [0.04] * 8, "0.0%"),
        8: ("Capex % Revenue", [ratio(abs(row.get("capital_expenditures", 0)), row.get("revenue")) for row in actuals] + [0.08, 0.08, 0.075, 0.07, 0.07], "0.0%"),
        9: ("NWC % Revenue", [0.02] * 8, "0.0%"),
        10: ("Cash", [row.get("cash") for row in actuals] + [None] * 5, "$#,##0"),
        11: ("Debt", [row.get("debt", latest.get("debt", 0)) for row in actuals] + [latest.get("debt", 0)] * 5, "$#,##0"),
        12: ("Diluted Shares", [row.get("shares_outstanding", latest.get("shares_outstanding")) for row in actuals] + [valuation.get("shares_outstanding", latest.get("shares_outstanding"))] * 5, "#,##0"),
        13: ("Equity", [row.get("stockholders_equity", 0) for row in actuals] + [None] * 5, "$#,##0"),
        15: ("Risk-free Rate", [None, None, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04], "0.0%"),
        16: ("Equity Risk Premium", [None, None, 0.055, 0.055, 0.055, 0.055, 0.055, 0.055], "0.0%"),
        17: ("Beta", [None, None, 1.25, 1.25, 1.25, 1.25, 1.25, 1.25], "0.0x"),
        18: ("Pre-tax Cost of Debt", [None, None, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06], "0.0%"),
        19: ("Target Debt Weight", [None, None, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15], "0.0%"),
        20: ("Terminal Growth", [None, None, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03], "0.0%"),
        21: ("WACC", [None, None, None, None, None, None, None, None], "0.0%"),
    }
    for row_idx, (label, values, fmt) in rows.items():
        ops.append(set_op("Assumptions", f"A{row_idx}", {"value": label, "bold": "true" if row_idx in {2, 15} else "false"}))
        for col_idx, value in enumerate(values, start=2):
            props: dict[str, Any] = {"format": fmt, "font.color": "0000FF"}
            if row_idx == 21 and col_idx >= 4:
                props["formula"] = f"=Assumptions!{cell(col_idx, 19)}*(Assumptions!{cell(col_idx, 18)}*(1-Assumptions!{cell(col_idx, 6)}))+(1-Assumptions!{cell(col_idx, 19)})*(Assumptions!{cell(col_idx, 15)}+Assumptions!{cell(col_idx, 17)}*Assumptions!{cell(col_idx, 16)})"
                props["font.color"] = "000000"
            else:
                props["value"] = "" if value is None else value
            ops.append(set_op("Assumptions", cell(col_idx, row_idx), props))
    ops.append(set_op("Assumptions", "A24", {"value": "Source", "bold": "true", "fill": "1F3864", "font.color": "FFFFFF"}))
    ops.append(set_op("Assumptions", "B24", {"value": "SNDK public_company vault; SEC companyfacts-derived statements; public market fallback", "fill": "F2F2F2"}))
    batch(ops)


def populate_statement_sheets() -> None:
    ops: list[dict[str, Any]] = []
    for sheet in ["Income Statement", "Balance Sheet", "Cash Flow", "DCF Valuation", "Sensitivity", "Error Checks", "Dashboard", "Sources"]:
        ops.append(sheet_op(sheet, {"freeze": "B2"}))
        ops.append(set_op(sheet, "A1", {"value": sheet, "bold": "true", "fill": "1F3864", "font.color": "FFFFFF"}))
        for idx, period in enumerate(PERIODS, start=2):
            ops.append(set_op(sheet, cell(idx, 1), {"value": period, "bold": "true", "fill": "1F3864", "font.color": "FFFFFF"}))
    batch(ops)

    is_rows = {
        3: "Revenue",
        4: "Gross Profit",
        5: "Operating Income",
        6: "Tax Expense",
        7: "Net Income",
    }
    ops = [set_op("Income Statement", f"A{r}", {"value": label, "bold": "true" if r == 7 else "false"}) for r, label in is_rows.items()]
    for col in range(2, 10):
        previous_revenue = cell(col - 1, 3)
        period_cell = cell(col, 1)
        revenue_formula = f"=Assumptions!{cell(col, 3)}" if col <= 4 else f"='{ 'Income Statement' }'!{previous_revenue}*(1+Assumptions!{cell(col, 2)})"
        formulas = {
            3: revenue_formula,
            4: f"='{ 'Income Statement' }'!{cell(col, 3)}*Assumptions!{cell(col, 4)}",
            5: f"='{ 'Income Statement' }'!{cell(col, 3)}*Assumptions!{cell(col, 5)}",
            6: f"=MAX(0,'{ 'Income Statement' }'!{cell(col, 5)}*Assumptions!{cell(col, 6)})",
            7: f"='{ 'Income Statement' }'!{cell(col, 5)}-'{ 'Income Statement' }'!{cell(col, 6)}",
        }
        for row, formula in formulas.items():
            ops.append(set_op("Income Statement", cell(col, row), {"formula": formula, "font.color": "000000", "format": "$#,##0;($#,##0);-"}))
        ops.append(set_op("Income Statement", period_cell, {"value": PERIODS[col - 2], "bold": "true", "fill": "1F3864", "font.color": "FFFFFF"}))
    batch(ops)

    cf_rows = {
        3: "Net Income",
        4: "D&A",
        5: "Capex",
        6: "Change in NWC",
        8: "Free Cash Flow",
        10: "Beginning Cash",
        11: "Ending Cash",
        12: "Cash Reconciliation",
    }
    ops = [set_op("Cash Flow", f"A{r}", {"value": label, "bold": "true" if r in {8, 11, 12} else "false"}) for r, label in cf_rows.items()]
    for col in range(2, 10):
        formulas = {
            3: f"='Income Statement'!{cell(col, 7)}",
            4: f"='Income Statement'!{cell(col, 3)}*Assumptions!{cell(col, 7)}",
            5: f"=-'Income Statement'!{cell(col, 3)}*Assumptions!{cell(col, 8)}",
            6: f"=-'Income Statement'!{cell(col, 3)}*Assumptions!{cell(col, 9)}",
            8: f"='Cash Flow'!{cell(col, 3)}+'Cash Flow'!{cell(col, 4)}+'Cash Flow'!{cell(col, 5)}+'Cash Flow'!{cell(col, 6)}",
            10: f"=Assumptions!{cell(col, 10)}" if col <= 4 else f"='Cash Flow'!{cell(col - 1, 11)}",
            11: f"=Assumptions!{cell(col, 10)}" if col <= 4 else f"='Cash Flow'!{cell(col, 10)}+'Cash Flow'!{cell(col, 8)}",
        }
        for row, formula in formulas.items():
            fmt = "$#,##0;($#,##0);-" if row != 12 else "General"
            ops.append(set_op("Cash Flow", cell(col, row), {"formula": formula, "font.color": "000000", "format": fmt}))
    batch(ops)

    bs_rows = {
        3: "Cash",
        4: "Debt",
        5: "Stockholders Equity",
        6: "Operating Assets Plug",
        7: "Total Assets",
        8: "Balance Check",
    }
    ops = [set_op("Balance Sheet", f"A{r}", {"value": label, "bold": "true" if r in {7, 8} else "false"}) for r, label in bs_rows.items()]
    for col in range(2, 10):
        formulas = {
            3: f"='Cash Flow'!{cell(col, 11)}",
            4: f"=Assumptions!{cell(col, 11)}",
            5: f"=Assumptions!{cell(col, 13)}" if col <= 4 else f"='Balance Sheet'!{cell(col - 1, 5)}+'Income Statement'!{cell(col, 7)}",
            6: f"='Balance Sheet'!{cell(col, 4)}+'Balance Sheet'!{cell(col, 5)}-'Balance Sheet'!{cell(col, 3)}",
            7: f"='Balance Sheet'!{cell(col, 3)}+'Balance Sheet'!{cell(col, 6)}",
            8: f"='Balance Sheet'!{cell(col, 7)}-'Balance Sheet'!{cell(col, 4)}-'Balance Sheet'!{cell(col, 5)}",
        }
        for row, formula in formulas.items():
            fmt = "$#,##0;($#,##0);-" if row != 8 else "0"
            ops.append(set_op("Balance Sheet", cell(col, row), {"formula": formula, "font.color": "000000", "format": fmt}))
    batch(ops)

    ops = []
    for col in range(2, 10):
        ops.append(set_op("Cash Flow", cell(col, 12), {"formula": f"='Cash Flow'!{cell(col, 11)}='Balance Sheet'!{cell(col, 3)}", "font.color": "000000"}))
    batch(ops)


def populate_dcf_and_checks() -> None:
    ops: list[dict[str, Any]] = []
    labels = {
        3: "Free Cash Flow",
        4: "Discount Factor",
        5: "PV FCF",
        7: "Terminal Value",
        8: "PV Terminal Value",
        10: "Enterprise Value",
        11: "Equity Value",
        12: "Implied Price",
        13: "Terminal Value Share",
    }
    for row, label in labels.items():
        ops.append(set_op("DCF Valuation", f"A{row}", {"value": label, "bold": "true" if row in {10, 11, 12} else "false"}))
    for idx, source_col in enumerate(range(5, 10), start=2):
        year = idx - 1
        ops.append(set_op("DCF Valuation", cell(idx, 1), {"value": f"Y{year}", "bold": "true", "fill": "1F3864", "font.color": "FFFFFF"}))
        ops.append(set_op("DCF Valuation", cell(idx, 3), {"formula": f"='Cash Flow'!{cell(source_col, 8)}", "font.color": "008000", "format": "$#,##0;($#,##0);-"}))
        ops.append(set_op("DCF Valuation", cell(idx, 4), {"formula": f"=1/(1+Assumptions!{cell(source_col, 21)})^{year}", "font.color": "000000", "format": "0.000x"}))
        ops.append(set_op("DCF Valuation", cell(idx, 5), {"formula": f"='DCF Valuation'!{cell(idx, 3)}*'DCF Valuation'!{cell(idx, 4)}", "font.color": "000000", "format": "$#,##0;($#,##0);-"}))
    for col_idx in range(7, 10):
        ops.append(set_op("DCF Valuation", cell(col_idx, 1), {"value": ""}))
    ops.append(set_op("DCF Valuation", "B7", {"formula": "='DCF Valuation'!F3*(1+Assumptions!I20)/(Assumptions!I21-Assumptions!I20)", "font.color": "000000", "format": "$#,##0;($#,##0);-"}))
    ops.append(set_op("DCF Valuation", "B8", {"formula": "='DCF Valuation'!B7*'DCF Valuation'!F4", "font.color": "000000", "format": "$#,##0;($#,##0);-"}))
    ops.append(set_op("DCF Valuation", "B10", {"formula": "=SUM('DCF Valuation'!B5:F5)+'DCF Valuation'!B8", "font.color": "000000", "format": "$#,##0;($#,##0);-"}))
    ops.append(set_op("DCF Valuation", "B11", {"formula": "='DCF Valuation'!B10+'Balance Sheet'!D3-'Balance Sheet'!D4", "font.color": "000000", "format": "$#,##0;($#,##0);-"}))
    ops.append(set_op("DCF Valuation", "B12", {"formula": "='DCF Valuation'!B11/Assumptions!D12", "font.color": "000000", "format": "$#,##0.00;($#,##0.00);-"}))
    ops.append(set_op("DCF Valuation", "B13", {"formula": "='DCF Valuation'!B8/'DCF Valuation'!B10", "font.color": "000000", "format": "0.0%"}))
    batch(ops)

    ops = [
        set_op("Sensitivity", "A3", {"value": "WACC \\ TGR", "bold": "true", "fill": "1F3864", "font.color": "FFFFFF"}),
    ]
    for col_idx in range(2, 10):
        ops.append(set_op("Sensitivity", cell(col_idx, 1), {"value": ""}))
    terminal_growths = [0.02, 0.025, 0.03, 0.035, 0.04]
    waccs = [0.08, 0.09, 0.10, 0.11, 0.12]
    for idx, tg in enumerate(terminal_growths, start=2):
        ops.append(set_op("Sensitivity", cell(idx, 3), {"value": tg, "format": "0.0%", "bold": "true", "fill": "1F3864", "font.color": "FFFFFF"}))
    for row_idx, wacc in enumerate(waccs, start=4):
        ops.append(set_op("Sensitivity", cell(1, row_idx), {"value": wacc, "format": "0.0%", "bold": "true", "fill": "1F3864", "font.color": "FFFFFF"}))
        for col_idx in range(2, 7):
            col_letter_cell = cell(col_idx, 3)
            row_wacc_cell = cell(1, row_idx)
            pv_terms = []
            for offset, source_col in enumerate(range(5, 10), start=1):
                pv_terms.append(f"'Cash Flow'!{cell(source_col, 8)}/(1+$A{row_idx})^{offset}")
            formula = (
                f"=(SUM({','.join(pv_terms)})+"
                f"('Cash Flow'!I8*(1+{col_letter_cell})/($A{row_idx}-{col_letter_cell}))/(1+$A{row_idx})^5"
                f"+'Balance Sheet'!D3-'Balance Sheet'!D4)/Assumptions!D12"
            )
            ops.append(set_op("Sensitivity", cell(col_idx, row_idx), {"formula": formula, "font.color": "000000", "format": "$#,##0.00;($#,##0.00);-"}))
    batch(ops)

    ops = []
    ops.extend(
        [
            set_op("Error Checks", "A2", {"value": "Check", "bold": "true", "fill": "1F3864", "font.color": "FFFFFF"}),
            set_op("Error Checks", "A3", {"value": "Balance Sheet Balances", "bold": "true"}),
            set_op("Error Checks", "A4", {"value": "Cash Reconciles", "bold": "true"}),
        ]
    )
    for col_idx in range(2, 10):
        ops.append(set_op("Error Checks", cell(col_idx, 1), {"value": ""}))
    for idx, period in enumerate(PERIODS, start=2):
        ops.append(set_op("Error Checks", cell(idx, 2), {"value": period, "bold": "true", "fill": "1F3864", "font.color": "FFFFFF"}))
        ops.append(set_op("Error Checks", cell(idx, 3), {"formula": f"='Balance Sheet'!{cell(idx, 8)}=0", "font.color": "000000"}))
        ops.append(set_op("Error Checks", cell(idx, 4), {"formula": f"='Cash Flow'!{cell(idx, 12)}", "font.color": "000000"}))
    local_status_refs = ",".join(cell(col_idx, row_idx) for row_idx in [3, 4] for col_idx in range(2, 10))
    ops.extend(
        [
            set_op("Error Checks", "A7", {"value": "Overall Status", "bold": "true"}),
            set_op("Error Checks", "B7", {"formula": f'=IF(AND({local_status_refs}),"ALL CLEAR","ERRORS FOUND")', "font.color": "000000"}),
        ]
    )
    batch(ops)


def populate_dashboard_and_sources(ctx: dict[str, Any]) -> None:
    ops: list[dict[str, Any]] = []
    rows = [
        ("Company", ctx["company"], "target config"),
        ("Ticker", ctx["ticker"], "target config"),
        ("Latest Revenue", "='Income Statement'!D3", "Income Statement"),
        ("Latest Net Income", "='Income Statement'!D7", "Income Statement"),
        ("Y5 Revenue", "='Income Statement'!I3", "Income Statement"),
        ("DCF Enterprise Value", "='DCF Valuation'!B10", "DCF Valuation"),
        ("DCF Equity Value", "='DCF Valuation'!B11", "DCF Valuation"),
        ("DCF Implied Price", "='DCF Valuation'!B12", "DCF Valuation"),
        ("Terminal Value Share", "='DCF Valuation'!B13", "DCF Valuation"),
        ("Model Status", "PENDING QA", "Error Checks"),
    ]
    ops.append(set_op("Dashboard", "A1", {"value": "SNDK OfficeCLI Financial Model", "bold": "true", "fill": "70AD47", "font.color": "FFFFFF"}))
    ops.append(set_op("Dashboard", "B1", {"value": "Value", "bold": "true", "fill": "70AD47", "font.color": "FFFFFF"}))
    ops.append(set_op("Dashboard", "C1", {"value": "Source", "bold": "true", "fill": "70AD47", "font.color": "FFFFFF"}))
    for col_idx in range(4, 10):
        ops.append(set_op("Dashboard", cell(col_idx, 1), {"value": ""}))
    for idx, (label, value_or_formula, source) in enumerate(rows, start=2):
        ops.append(set_op("Dashboard", f"A{idx}", {"value": label, "bold": "true" if idx in {2, 3, 11} else "false"}))
        if isinstance(value_or_formula, str) and value_or_formula.startswith("="):
            if "Status" in label:
                fmt = "General"
            elif "Share" in label:
                fmt = "0.0%"
            elif "Price" in label:
                fmt = "$#,##0.00;($#,##0.00);-"
            else:
                fmt = "$#,##0;($#,##0);-"
            ops.append(set_op("Dashboard", f"B{idx}", {"formula": value_or_formula, "font.color": "008000", "format": fmt}))
        else:
            ops.append(set_op("Dashboard", f"B{idx}", {"value": value_or_formula}))
        ops.append(set_op("Dashboard", f"C{idx}", {"value": source}))
    source_rows = [
        ("Financial statement inputs", "companies/sandisk/vault/public_company/data/statements/annual_statements.json"),
        ("Market data inputs", "companies/sandisk/vault/public_company/data/valuation/valuation_snapshot.json"),
        ("Installed skill", "experiments/skillsmp_officecli_financial_model/installed_skills/officecli-financial-model"),
        ("OfficeCLI version", "officecli --version output recorded by run log"),
        ("Run folder", str(RUN_ROOT)),
    ]
    ops.append(set_op("Sources", "A1", {"value": "Source Map", "bold": "true", "fill": "70AD47", "font.color": "FFFFFF"}))
    ops.append(set_op("Sources", "B1", {"value": "Location", "bold": "true", "fill": "70AD47", "font.color": "FFFFFF"}))
    for col_idx in range(3, 10):
        ops.append(set_op("Sources", cell(col_idx, 1), {"value": ""}))
    for idx, (field, source) in enumerate(source_rows, start=2):
        ops.append(set_op("Sources", f"A{idx}", {"value": field, "bold": "true"}))
        ops.append(set_op("Sources", f"B{idx}", {"value": source}))
    batch(ops)


def finish_and_validate() -> dict[str, Any]:
    run(["set", str(MODEL_PATH), "/", "--prop", "calc.fullCalcOnLoad=true", "--prop", "calc.iterate=true"], check=False)
    run(["close", str(MODEL_PATH)], check=False)
    initial_validate = run(["validate", str(MODEL_PATH)], check=False)
    checks = run(["get", str(MODEL_PATH), "/Error Checks/B7", "--json"], check=False)
    status_text = "ERRORS FOUND"
    try:
        checks_payload = json.loads(checks.stdout)
        if checks_payload.get("data", {}).get("text") == "ALL CLEAR" and initial_validate.returncode == 0:
            status_text = "ALL CLEAR"
    except json.JSONDecodeError:
        status_text = "ERRORS FOUND"
    run(
        [
            "set",
            str(MODEL_PATH),
            "/Dashboard/B11",
            "--prop",
            f"value={status_text}",
            "--prop",
            f"font.color={'008000' if status_text == 'ALL CLEAR' else 'C00000'}",
        ],
        check=False,
    )
    run(["close", str(MODEL_PATH)], check=False)
    validate = run(["validate", str(MODEL_PATH)], check=False)
    html = run(["view", str(MODEL_PATH), "html"], check=False)
    preview_path = RUN_ROOT / "preview.html"
    html_stdout = html.stdout.strip()
    if html_stdout and Path(html_stdout).exists():
        shutil.copyfile(html_stdout, preview_path)
    else:
        preview_path.write_text(html.stdout, encoding="utf-8")
    text_view = run(["view", str(MODEL_PATH), "text"], check=False)
    (RUN_ROOT / "text_view.txt").write_text(text_view.stdout, encoding="utf-8")
    validation_passed = validate.returncode == 0 and "Validation passed" in validate.stdout
    return {
        "model_path": str(MODEL_PATH),
        "preview_path": str(preview_path),
        "text_view_path": str(RUN_ROOT / "text_view.txt"),
        "validation_status": "pass" if validation_passed else "fail",
        "validate_returncode": validate.returncode,
        "validate_stdout": validate.stdout,
        "validate_stderr": validate.stderr,
    }


def main() -> None:
    ctx = build_context()
    create_workbook()
    populate_assumptions(ctx)
    populate_statement_sheets()
    populate_dcf_and_checks()
    populate_dashboard_and_sources(ctx)
    result = finish_and_validate()
    result["skill"] = "officecli-financial-model"
    result["skill_source"] = "https://github.com/iOfficeAI/AionUi/tree/main/src/process/resources/skills/officecli-financial-model"
    result["stars"] = 22496
    (RUN_ROOT / "run_result.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
