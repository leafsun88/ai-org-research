---
name: financial-model-v1
description: >
  This skill builds the initial financial model covering revenue, costs, cash flow,
  and key SaaS metrics. Use when asked to create the company's first financial model,
  build a three-statement model for a startup, or establish the baseline financial
  projections. Also consider when fundraising begins without a financial model.
  Suggest when the user is making growth commitments without modelled financials.
department: finance
agent: cfo-vp-finance
version: 1.0.0
complexity: complex
related-skills:
  - ../../../finance/fpa-analyst/fundraising-model-builder/SKILL.md
  - ../../../finance/fpa-analyst/annual-budget-builder/SKILL.md
triggers:
  - "build financial model"
  - "create financial projections"
  - "financial model"
  - "model our financials"
  - "build a forecast model"
---

# financial-model-v1

## Agent: CFO / VP Finance

L1 CFO and VP Finance (1x) reporting to the COO, responsible for unit economics, financial modelling, pricing sign-off, and pitch narration for financial audiences.

Department ethos: [ideal-finance.md](../../../../departments/finance/ideal-finance.md)
Tool policy: [allowed-tools.yaml](../../../../allowed-tools.yaml)

## Skill Description

Builds the initial financial model covering revenue projections, cost structure, cash flow, and key SaaS metrics to establish the company's baseline financial framework.

## When to Use

- When the company is pre-model and needs its first structured financial projection for fundraising or strategic planning.
- When the existing financial model is a back-of-napkin spreadsheet that cannot support investor diligence or board-level decisions.
- When a pivot or new business line requires a ground-up financial model with distinct revenue and cost assumptions.

## Workflow

1. **Revenue Architecture**: Define the revenue model structure -- subscription tiers, usage-based components, professional services, expansion revenue. Map each revenue stream to its driver (customers x ACV, seats x price, usage x rate). Deliverable: revenue model architecture document with driver definitions.
2. **Bottoms-Up Revenue Build**: Build the revenue forecast using bottoms-up assumptions: lead volume by channel, conversion rates by stage, sales cycle length, ACV by segment, net revenue retention rate. Model monthly cohorts for the first 24 months, then quarterly through month 60. Deliverable: revenue forecast with cohort-level detail.
3. **Cost Structure Modelling**: Model COGS (hosting, support, third-party APIs) to derive gross margin. Build OpEx by department (R&D, S&M, G&A) with headcount-driven and non-headcount line items. Include stock-based compensation as a separate line. Deliverable: P&L model with gross margin and operating margin.
4. **Cash Flow Construction**: Build the cash flow model accounting for billing frequency (monthly vs. annual prepay mix), collections timing (DSO assumptions), payment terms for vendors, and capex. Model the cash conversion cycle. Deliverable: cash flow statement with monthly granularity for 24 months.
5. **SaaS Metrics Dashboard**: Calculate and present ARR, MRR, net new ARR, gross churn, net revenue retention, LTV/CAC ratio, CAC payback period, burn multiple, and months of runway. Deliverable: SaaS metrics summary with definitions and calculation methodology.
6. **Scenario Framework**: Build best/base/worst scenarios by varying 3-5 key drivers (growth rate, churn, CAC, gross margin, hiring pace). Define what triggers a move between scenarios. Deliverable: scenario analysis with trigger definitions and management actions.
7. **Model Documentation**: Document all assumptions, data sources, formula logic, and known limitations. Create a model changelog for version tracking. Deliverable: assumptions register and model user guide.

## Anti-Patterns

- **Top-down-only forecasting**: Building revenue projections from TAM-down percentages without bottoms-up validation from sales capacity and pipeline data. *Why*: top-down models produce numbers that feel right but cannot be operationalized or defended in diligence.
- **Ignoring cash vs. revenue timing**: Modelling revenue recognition without a corresponding cash flow model. *Why*: GAAP revenue and cash receipts diverge significantly with annual contracts and usage billing; companies die from cash gaps, not revenue gaps.
- **Over-engineering the v1**: Building a 50-tab model with currency conversion, multi-entity consolidation, and detailed department-level budgets before the company has product-market fit. *Why*: model complexity should match business complexity; premature sophistication wastes time and obscures the key drivers.
- **Hardcoded assumptions**: Embedding assumptions directly in formulas rather than centralizing them in a clearly labelled assumptions tab. *Why*: scenario analysis becomes impossible when changing an assumption requires editing dozens of cells across multiple tabs.
- **Missing unit economics layer**: Building a P&L without a unit economics layer that connects customer-level metrics to company-level financials. *Why*: investors evaluate startups on unit economics first; a model that cannot show CAC, LTV, and payback is incomplete.

## Output

**On success**: Produces a complete v1 financial model containing the revenue forecast, P&L, cash flow statement, SaaS metrics dashboard, scenario analysis, and assumptions register. Delivered as a version-controlled spreadsheet with a model user guide.

**On failure**: Report which model components could not be built (e.g., revenue model blocked by undefined pricing), what partial model exists, and what business decisions or data collection must happen before the model can be completed. Provide a prioritized action list with owners.

## Related Skills

- [`fundraising-model-builder`](../../../finance/fpa-analyst/fundraising-model-builder/SKILL.md) -- Extends this v1 model into an investor-facing format with use-of-proceeds and dilution analysis.
- [`annual-budget-builder`](../../../finance/fpa-analyst/annual-budget-builder/SKILL.md) -- Uses this model as the foundation for departmental budget allocation.
