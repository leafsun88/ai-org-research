# SkillsMP Modeling Recommendations

Reviewed on 2026-04-26.

## Best To Absorb Into Our Canonical Skill

1. `sartrus/modelling-team`
   - Use for architecture -> build -> challenger -> repair workflow.
   - Best ideas: scenario selector, assumption register, formula challenger, odd-dimension sensitivity grids, explicit formula reference rules.
   - Install status: keep as reviewed reference first; do not make it canonical by itself.

2. `LerianStudio/financial-modeling`
   - Use for six-phase modeling discipline: scoping, architecture, assumptions, build, validation, documentation.
   - Best ideas: anti-rationalization checklist, validation before delivery, documentation metrics.
   - Install status: safe as reference.

3. `AbsolutelySkilled/financial-modeling`
   - Use for principles and anti-patterns: assumptions explicit, scenarios over point estimates, downside stress, unit economics, cap table concepts.
   - Risk: includes `npx skills add` companion-install instructions; do not auto-run.
   - Install status: reference only unless manually installed later.

4. `virattt/dcf-valuation`
   - Use for compact DCF checklist.
   - Best ideas: 5-year FCF projection, WACC/terminal growth sensitivity, terminal value ratio sanity check, EV cross-check.
   - Install status: safe as reference.

5. `anthropics/comps-analysis`
   - Use for comps sheet structure and formula discipline.
   - Best ideas: formulas over hardcodes, statistic block, peer metrics, source comments.
   - Risk: prioritizes paid/institutional MCP sources; for our free-first workflow use SEC/Yahoo/StockAnalysis unless user provides paid data.
   - Install status: reference only.

6. `anthropics/lbo-model`
   - Use only when user asks for LBO.
   - Best ideas: template-first rule, formula color convention, debt schedule and returns checks.
   - Install status: optional later.

## Useful But Not Canonical

- `daloopa/build-model`: excellent comprehensive data pull and context JSON pattern, but depends on Daloopa citation/data workflow.
- `panaversity/financial-architect` and `idfa-ops`: useful named-range and model interaction ideas, but heavier than current workflow.
- `officecli-financial-model`: useful for generic financial workbook structure, but less public-company-specific.

## Not Recommended For Immediate Install

- Skills that require Capital IQ, Bloomberg, FactSet, Daloopa, or other paid/proprietary sources unless the user explicitly provides credentials.
- Skills that include broad shell execution, global package install, or unattended installer commands.
- Duplicate forks of the same `creating-financial-models` skill; keep one reference copy only.

## Model Samples To Generate

1. **Compact DCF + Comps**
   - Fast, source-mapped, similar to current model but denser and easier to inspect.
   - Good for quick company review.

2. **Scenario Architect Model**
   - Dashboard + Assumptions + Historical + Forecast + DCF + Sensitivity + Checks.
   - Shows Base/Bear/Bull scenario selector and clear assumption registry.

3. **Comps-Focused Model**
   - Peer metrics, valuation multiples, min/median/max statistics, implied value range.
   - Good when relative valuation matters more than the DCF.

4. **Quality Challenger Pack**
   - Not a standalone valuation model; a review workbook/checklist that audits source coverage, formula outputs, and valuation sanity checks.
   - Good as a companion to any final model.
