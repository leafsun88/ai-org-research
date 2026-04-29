---
name: financial-modeling
description: >
  Financial model construction including DCF, LBO, comparable companies,
  and three-statement models. Use when the user asks about financial
  projections, DCF analysis, leveraged buyout modeling, revenue forecasting,
  or building a financial model for any business.
---

# Financial Modeling

## Required Inputs

- **Company/Business**: What is being modeled.
- **Model Type**: DCF, LBO, three-statement, or comparable companies.
- **Time Horizon**: Projection period (default: 5 years).
- **Purpose**: Valuation, fundraising, internal planning, or transaction.

## Execution Steps

### 1. Revenue Build

Bottom-up revenue model. Identify drivers (units × price, users × ARPU,
seats × ASP). Project each driver independently with stated assumptions.

### 2. Cost Structure

- COGS / gross margin projection with scale effects.
- OpEx by category (R&D, S&M, G&A) with % of revenue benchmarks.
- Working capital assumptions (DSO, DPO, DIO).
- CapEx and depreciation schedule.

### 3. Three-Statement Integration

Income statement → balance sheet → cash flow statement. Ensure the balance
sheet balances. Cash flow ties to the change in cash on the balance sheet.

### 4. Model-Specific Outputs

**DCF**: WACC calculation, terminal value (exit multiple + perpetuity growth),
sensitivity table on WACC × terminal growth.

**LBO**: Sources & uses, debt schedule, returns waterfall, IRR sensitivity
on entry multiple × exit multiple.

**Comps**: Peer selection criteria, trading multiples (EV/Revenue, EV/EBITDA,
P/E), regression analysis if applicable.

## Output Template

```markdown
## Financial Model: [Company]

### Key Assumptions
| Assumption | Year 1 | Year 3 | Year 5 | Source/Basis |
|---|---|---|---|---|
| Revenue growth | X% | X% | X% | [rationale] |
| Gross margin | X% | X% | X% | [rationale] |
| EBITDA margin | X% | X% | X% | [rationale] |

### Summary Financials ($M)
| Metric | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |
|---|---|---|---|---|---|
| Revenue | | | | | |
| Gross Profit | | | | | |
| EBITDA | | | | | |
| Net Income | | | | | |
| Free Cash Flow | | | | | |

### [DCF/LBO/Comps] Output
[Model-specific valuation output with sensitivity analysis]

### Key Risks to Model
- [Risk]: Impact on valuation if assumption is wrong.
```

## Quality Checks

- Every assumption has a stated source or rationale.
- Three statements are internally consistent.
- Sensitivity analysis covers at least 2 key variables.
- Model includes a bear case scenario.
