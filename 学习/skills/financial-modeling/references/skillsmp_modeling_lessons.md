# SkillsMP Modeling Lessons

Sources reviewed on 2026-04-26:

- SkillsMP marketplace: https://skillsmp.com/zh
- SkillsMP MCP server package: `skillsmp-mcp-server`
- Daloopa `build-model`: https://github.com/daloopa/investing/tree/main/.claude/skills/build-model
- LerianStudio `financial-modeling`: https://github.com/LerianStudio/ring/tree/main/.archive/finance-team/skills/financial-modeling
- AbsolutelySkilled `financial-modeling`: https://github.com/AbsolutelySkilled/AbsolutelySkilled/tree/main/skills/financial-modeling
- Virattt `dcf-valuation`: https://github.com/virattt/dexter/tree/main/src/skills/dcf
- Sartrus `modelling-team`: https://github.com/sartrus/modelling-team-skill/tree/main/skills/modelling-team

Useful patterns to keep:

- Save a full context JSON before building the workbook. It should include company metadata, historical periods, projected periods, income statement, balance sheet, cash flow, segment data, KPIs, market data, peers, assumptions, DCF outputs, and source references.
- Treat modeling as architecture -> build -> challenge -> repair. The challenger should inspect workbook structure, formula logic, scenario wiring, source coverage, and output reasonableness before the model can pass.
- Separate assumptions, calculations, outputs, source map, and validation checks. Never hide hardcoded assumptions in formulas.
- Use Base/Bear/Bull scenarios when enough assumptions exist. Scenario analysis should change coherent groups of assumptions; sensitivity tables should vary one or two drivers.
- Document WACC by component: risk-free rate, equity risk premium, beta, cost of debt, tax rate, and capital structure.
- DCF sanity checks should include terminal value share of total enterprise value, DCF EV vs current/reported EV, and DCF-implied multiple vs peer multiples.
- For public-company history, target 8-16 quarters when the issuer has enough available history. If not, record the reason as coverage context.
- Editable assumptions should be visually distinct from formulas and outputs in the workbook.

Rejected or deferred patterns:

- Do not depend on paid data vendors such as Daloopa or Capital IQ unless the user supplies credentials.
- Do not adopt a community skill wholesale without reviewing its source and license.
- Do not rely on Excel formula caches when building through `openpyxl`; write deterministic model outputs into JSON and visible workbook cells, or use a recalculating spreadsheet runtime in a future upgrade.
