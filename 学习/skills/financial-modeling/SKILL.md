---
name: financial-modeling
description: Build a source-mapped public-company DCF and comps workbook from collected statements, market data, valuation, peers, and capital signals.
---

# Financial Modeling

Use this skill when the user asks for上市公司建模, DCF, comps, valuation workbook, financial model, or model validation.

## Inputs

Read from:

- `companies/{slug}/vault/public_company/data/statements/annual_statements.json`
- `companies/{slug}/vault/public_company/data/statements/quarterly_statements.json`
- `companies/{slug}/vault/public_company/data/market_data/price_history.csv`
- `companies/{slug}/vault/public_company/data/valuation/valuation_snapshot.json`
- `companies/{slug}/vault/public_company/data/valuation/peer_valuation.json`
- `companies/{slug}/vault/public_company/data/capital_signals/`
- `public_company.peer_tickers` in `config/company_targets.json`

## Command

```bash
python3 scripts/discovery/build_financial_model.py SNDK --json
```

When invoked through `public-company-collect`, the model is rebuilt inside the quality loop after every data repair:

```bash
python3 scripts/discovery/collect_public_company.py SNDK --quality-loop --max-quality-iterations 3 --json
```

## Outputs

Write:

- `models/{YYYY-MM-DD}/financial_model.xlsx`
- `models/{YYYY-MM-DD}/model_inputs.json`
- `models/{YYYY-MM-DD}/model_summary.md`
- `models/{YYYY-MM-DD}/model_validation.json`
- `metadata/model_quality_audit.json`
- `metadata/model_quality_audit.md`

Workbook sheets:

- `Summary`
- `Historical Statements`
- `Operating Metrics`
- `Forecast`
- `DCF`
- `Comps`
- `Sensitivity`
- `Capital Signals`
- `Source Map`
- `Assumptions`

## Modeling Rules

- Start with an explicit model architecture before writing workbook cells: purpose, required outputs, tabs, data flow, assumption register, scenario plan, and validation checks.
- Build a complete DCF and comps shell even when some data is missing.
- Use configured `peer_tickers`; do not invent peers.
- Mark WACC, terminal growth, margin, growth, D&A, capex, and NWC assumptions as `auto_default` unless the user supplies them.
- Keep inputs, calculations, outputs, checks, and source map logically separate. Do not bury hardcoded assumptions inside formulas or calculated sections.
- The workbook must be a living Excel model, not a static values dump. `Forecast`, `DCF`, `Sensitivity`, and ideally `Summary` must contain linked formulas that reference assumptions and source sheets. Deterministic JSON outputs are useful for audit, but they do not replace workbook formulas.
- Include at least Base/Bear/Bull scenario support when enough assumptions exist. A single-point forecast is allowed only as a draft and must be labeled as such.
- For public-company quarterly models, target 8-16 historical quarters when available. If the issuer history is shorter or source coverage is incomplete, record that as coverage context instead of padding with invented data.
- Every key output should map back to a source file, API, or filing in `Source Map`.
- Missing data must be preserved as a validation gap, not filled with fake numbers.
- Before finalizing, open the workbook with `openpyxl` and scan for obvious `#REF!`, `#DIV/0!`, and `#VALUE!` tokens.
- Also compute deterministic DCF outputs in JSON. Use this as an independent check against workbook formulas, not as a substitute for formulas.

## Modeling Reference Pattern

The current workflow incorporates lessons from SkillsMP modeling skills, especially Daloopa `build-model`, Lerian `financial-modeling`, AbsolutelySkilled `financial-modeling`, Virattt `dcf-valuation`, and Sartrus `modelling-team`.

Use this pattern when improving the model:

1. Architect: write the model blueprint first, including tab layout, formulas, assumptions, scenario selector, and checks.
2. Build: generate the workbook and `model_inputs.json` from the blueprint and collected data.
3. Challenge: audit the workbook against the blueprint; check formula links, scenario wiring, visible values, source coverage, and output reasonableness.
4. Repair: if the challenger finds a material issue, rebuild the workbook and rerun validation.

Important borrowed checks:

- DCF terminal value should usually be 50-80% of enterprise value for mature companies; warn if it is above 90% or below 40% without an explicit reason.
- Cross-check DCF enterprise value against current/reported enterprise value and peer-implied multiples; large differences should become warnings, not hidden.
- WACC should be componentized: risk-free rate, equity risk premium, beta, cost of debt, tax rate, and target capital structure.
- Editable assumptions should be visually distinct from formulas and outputs.
- Scenario analysis changes multiple related assumptions together. Sensitivity analysis changes one or two drivers across a matrix.

## Validation Gate

`model_validation.json` may only be `pass` when all model-quality checks pass. Otherwise use `needs_review`. Keep model quality separate from data quality: write workbook/model checks to `model_validation.json` and `metadata/model_quality_audit.*`; do not overwrite `metadata/data_quality_audit.*`, which belongs to source/data collection.

Required checks:

- workbook exists and has the required sheets;
- no obvious formula-error tokens;
- workbook contains enough linked formulas to qualify as a model, not just static outputs. As a baseline, require formulas across `Forecast`, `DCF`, and `Sensitivity`; a workbook with zero or only cosmetic formulas must be `needs_review`;
- annual statements include revenue, gross profit, operating income, net income, operating cash flow, capex, cash, debt, assets, liabilities, equity, and shares;
- historical annual statements preserve all available SEC companyfacts annual income-statement years, up to at least three years when available;
- at least one quarterly period includes revenue plus operating income or net income;
- market cap has medium/high confidence from a quote/share-count source, not weighted-average diluted shares;
- comps include real multiples for at least one configured peer;
- deterministic DCF outputs were calculated and stored in `model_inputs.json`.
- workbook display sheets expose visible numeric outputs for operating metrics, forecast, DCF, and sensitivities; do not rely on formula caches that may render blank in spreadsheet viewers.
- assumptions are documented with source, confidence, and whether they are user-supplied, filing-derived, market-derived, or `auto_default`;
- DCF terminal value ratio, EV cross-check, and peer multiple cross-check are present as warnings or passes.

Auto-default assumptions must be called out as a warning. A workbook with only auto-default assumptions is a draft model, not decision-ready.

## Quality Loop Contract

The model builder is not the final authority by itself. The collector must rerun modeling after each repaired data source and then rerun the full audit.

- If required statement fields improve, regenerate workbook, inputs, summary, and validation.
- If market cap confidence or peer multiples improve, regenerate comps and DCF summary.
- If validation still has gaps, keep `status: needs_review`; do not suppress gaps to make the workbook pass.
- Key displayed outputs such as operating metrics, forecast values, DCF values, and sensitivities must display visible numeric values even when no local spreadsheet recalculation engine is available.
- A formula-less workbook can be retained as a static analysis pack, but it must fail the model validation gate with `workbook_formula_links` and be repaired before the overall workflow is called complete.
- Only a clean `model_validation.json` plus clean `data_quality_audit.json` can end the loop with `pass`.

## Verification

Run:

```bash
python3 -m unittest scripts.discovery.test_public_company_collection
python3 scripts/discovery/build_financial_model.py SNDK --json
```

Then read `model_validation.json`. Treat `status: needs_review` as acceptable only when the gaps are explicitly listed and no fatal workbook errors exist.
