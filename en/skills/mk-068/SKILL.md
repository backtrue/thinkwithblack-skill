---
name: mk-068
description: "Marketing-spend allocation ceiling. Use for financial models, available marketing budgets, and profit-reinvestment decisions under e-commerce net-profit targets, including tax-inclusive prices, per-order and company expenses, competitor price ranges, reinvestment denominators, and periods. Deliver a recalculable model and conditional budget. Handle pure break-even ROAS or scaling an existing Meta campaign according to that specific request"
---

# MK-068 | Marketing-spend allocation ceiling

For a regular chat, upload `packs/mk-068.md`. It includes the shared rules, this method, and required references

## Purpose

This skill delivers: **An available-budget table under cost constraints**

Working backward to resource requirements is not a forecast or optimal allocation; do not decide actual spending without an affordable ceiling

## Required inputs

Use inputs for the work requested; substitute or derive values already supplied

- Spending ceiling: pre-marketing available contribution, fixed expenses not yet deducted, and approved target profit for the same period and accounting basis. Derive contribution from revenue and corresponding costs only when it is not already known
- Order and traffic requirements: after establishing or deriving the revenue target, use average order value and conversion rate. Reuse directly supplied order or traffic requirements with their basis and source
- Net-profit model: revenue, per-order and company expenses, the target profit definition, and applicable tax assumptions; use sections A–C below to complete fields that affect the result
- Profit reinvestment: also obtain the profit base, percentage denominator and period, existing budget, payment timing, and affordable amount; compare candidates under sections D–E

For a formula or method question, first deliver the formula and an explicitly hypothetical example. Request missing branch-specific values only for an actual calculation

## Method

1. Identify whether the task asks for a spending ceiling, order and traffic requirements, or net-profit/reinvestment assessment; fix the period, cost basis, and target
2. For a spending ceiling alone, substitute directly into the formula below and check double-counted costs and feasibility. Work backward using average order value and conversion rate only when order or traffic requirements are requested
3. Use sections A–C for net-profit modeling and then D–E for profit reinvestment. Deliver the results relevant to the task; assess budget allocation against the target and affordable ceiling, without equating lower unit acquisition costs with budget cuts

## Calculations and interpretation

Available marketing spend = available contribution − fixed expenses to cover this period − approved target profit. Calculate on the established financial basis for this case. If contribution already includes marketing expense, restore the pre-marketing basis first to avoid deducting it twice

The following supplements apply to net-profit models or profit-reinvestment questions. For a ceiling calculation using an already established basis, substitute directly and retain the seven original output fields

### A. Fix the question and calculation basis

Retain every price, currency, tax-rate assumption, cost, target net margin, competitor statement, supplier quote, and supplementary question. First distinguish a request for modeling methods or conditional recommendations from one to decide exact prices and budgets for an actual store. For method questions, deliver formulas, calculations using known values, and a fillable table directly

Record each input's source, period, per-item/per-order/per-month basis, tax-inclusive or tax-exclusive basis, and assumed or actual status. Do not deduct discounts or refunds twice when using net revenue. Separate shipping paid by buyers from logistics expense. Exclude collected sales tax from revenue. Determine input-tax deductibility from the actual entity and transaction; retain branches when unknown rather than selecting a country's tax system yourself

Confirm separate denominators for platform monthly fees, per-order fees, percentage fees, and advertising acquisition costs. Dividing fixed expenses by orders is an allocation assumption; do not place the entire monthly fee into every item and then deduct it again at company level. Record advertising expense in only one place in the model, clearly distinguishing media spend from total marketing spend

### B. Build a complete profit-and-loss model

Build the table by product/order mix and month:

| Variable | Definition |
|---|---|
| R | Net revenue excluding tax for the same period, summed as quantity × net price using the actual mix |
| V | Non-advertising variable expenses: product, packaging, fulfillment, payment processing, channel fees, returns, etc., summed using their respective cost drivers |
| A | Marketing spend for the period, separating and then totaling media, creative, and other applicable items |
| F | Fixed/step costs for the period not already included elsewhere |
| D, I, T | Depreciation, interest, and income tax not already counted |
| N | Net profit after tax = R−V−A−F−D−I−T |

If the task defines net profit differently, preserve that definition and state the differences. When income tax or company expenses are missing, deliver the difference after listed expenses and the fields still to fill; do not call it complete after-tax net profit. Calculate N/R only when R>0. For zero revenue, report amounts and expenses rather than hiding the problem with a zero ratio

The target net margin m constrains N≥mR. Once the basis is confirmed as consistent and other expenses and T are temporarily fixed, the marketing ceiling is R−V−F−D−I−T−mR. A negative ceiling means this revenue/cost combination cannot reach the target even without advertising; do not set it to zero and claim the target is achievable. If income tax changes with profit or expense deductions, recalculate jointly using confirmed tax rules and retain whether the target is feasible

Work backward to a selling price only when explicit assumptions hold. For example, with per-item non-percentage cost c, all other costs allocated and unchanged by price, and target margin m<1, the required tax-exclusive price is c/(1−m). With an additional revenue-based fee k, it is c/(1−m−k), requiring a positive denominator. Mixed tax-inclusive fee bases require returning to the original cost definitions; do not treat all fees as percentages of tax-exclusive revenue. The derived price is a cost boundary, not evidence of willingness to pay or future sales volume

### C. Compare market, supply, and volume conditions together

Compare quotes using the same specifications, quantities, delivery terms, and tax basis. The first supplier's quote is not the entire market's cost. Retain the competitor price range supplied by the user. If a derived price exceeds that range, mark the implied value/willingness to pay as a hypothesis to validate instead of directly ordering a price increase

Compare price, supplier, packaging, logistics, bundle, and advertising-efficiency scenarios the user can implement, including complete revenue and costs for each. Price changes affect volume and price-based fees; additional advertising does not imply unchanged efficiency. Without history, state assumptions explicitly; do not assign arbitrary probabilities or call a scenario optimal

When greater volume lowers unit costs, also check MOQ, quality, full-batch payments, inventory, and fulfillment constraints. Record purchases of unsold inventory, loan principal, and capital expenditure separately from the period's profit and loss, and connect them to the cash table. Use mature, consistently defined actual before-and-after data to update original assumptions while preserving the forecast version

### D. Convert reinvestment percentages back to amounts

For every percentage, retain the numerator, denominator, period, expenses already deducted, and whether the existing budget is included. A competitor's self-reported percentage is not a direct decision rule

- Current-period marketing spend / current-period net revenue is a revenue share, not a profit-reinvestment rate
- If a proportion q of realized profit P from the prior period is allocated to the next period, the candidate amount is qP. Establish first whether this is the next period's total budget or an increment; for an increment, add the existing budget A0. An allocation from the prior period does not change that period's realized profit. Record marketing expense in the next period's profit and loss when incurred; the allocation is not new revenue in that period
- If total current-period marketing spend A equals q times current-period profit after deducting A, assume other costs and the income-tax amount are fixed and the pre-A balance is B. Then A=q(B−A), giving qB/(1+q), which differs from qB. If taxes, revenue, or costs vary with A, solve the scenario jointly again rather than applying the simplified formula

When P≤0, there is no positive profit base to allocate. Continued investment requires explicit startup capital or another funding source and an affordable loss; do not fabricate positive profit. A zero denominator makes the ratio undefined, though budget amounts with sources can still be compared

### E. Choose the reinvestment amount

Check each candidate amount against three requirements:

1. Profit and loss: recalculate with the new budget and its volume/efficiency scenarios, preserving the target net profit or an explicit growth-period loss plan. Do not silently replace a 10–25% target with an initial-loss strategy
2. Cash: list opening available funds, receipts, supplier payments, taxes, wages, inventory purchases, loan principal, capital expenditures, and the budget by payment timing. Each period's closing balance must meet the user's reserve requirement; count each outflow only once. Positive net profit does not equal available cash, and unrealized expected profit is not current funding
3. Incremental benefit: assess whether expected contribution from additional orders, after additional marketing and step costs, supports the offer. Total organic sales, platform attribution, and historical average ROAS do not directly prove incremental contribution. Without evidence, deliver a test candidate with a time limit, spending and loss ceilings, result definitions, and stopping conditions

Choose an evidence-supported amount that meets all conditions, then divide it by the explicitly defined positive profit base to obtain a percentage. Spending the full ceiling is not required. If no candidate is feasible, offer no reinvestment, cost/pricing adjustment, or the missing inputs. If a reserve, actual spending ceiling, or precise amount is needed but absent, deliver a conditional decision with parameters to fill; do not invent fixed 35%, 70%, or 20% increases or observation periods

### F. Deliverables and completion check

Deliver one integrated result: recalculation of original figures; reusable monthly profit-and-loss and cash fields/formulas; a target-scenario table; market and cost gaps; correct definitions of each percentage; candidate budget selection; and update/stopping conditions. Label numbers as original, derived, assumed, or unknown, and map every original question to a deliverable

A method question can be completed with a full model and conditional demonstration. If the original question requires actual store amounts, experience, or measured results, obtain the corresponding data and results. Record skill executability, method acceptance, and actual resolution of the original question separately

### G. Sources and scope of adoption

The core is the profit-backward-planning, cost, and break-even methods on pages 3, 7, 25, 27, and 38–49 of [Practical Marketing Strategy Course Day 2](https://docs.google.com/presentation/d/1NdxlcqAKMPHqGVS5jbjSYR_UgOJSA0fS65OnTtQLEHQ/edit). All 104 pages were read on 2026-10-08, revision AacEra95twlfAw. Model actual case costs rather than applying classroom healthy ratios, three times fixed costs, or an assumption that reaching break-even makes further spending safe

MIT-licensed supplements adopt driver-based models, scenarios, payment/receipt timing, and actual-data updates from [financial-analyst](https://github.com/alirezarezvani/claude-skills/blob/19392f7a08264ed00486a251f5b2098321771f94/finance/skills/financial-analyst/SKILL.md) and [forecasting-best-practices](https://github.com/alirezarezvani/claude-skills/blob/19392f7a08264ed00486a251f5b2098321771f94/finance/skills/financial-analyst/references/forecasting-best-practices.md). They do not adopt upstream fixed probabilities, error targets, or SaaS thresholds. Reinvestment denominators, cross-period treatment, and algebraic branches are rules integrated to meet this method's deliverable requirements

Official cross-checks: [business.gov.au budget creation](https://business.gov.au/finance/financial-tools-and-templates/create-a-budget) supports the distinction among budgets, forecasts, and actuals; [cash-flow management](https://business.gov.au/guide/guide-to-managing-cash-flow) supports cash checks for payments, inventory, and updates

#### MIT license

MIT License

Copyright (c) 2025 Alireza Rezvani

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Required output fields

| Order | Field | How to complete |
|---:|---|---|
| 1 | Input variable | Use source evidence, an intermediate method result, or an explicit unknown; do not invent information |
| 2 | Value | Use source evidence, an intermediate method result, or an explicit unknown; do not invent information |
| 3 | Unit and definition | Use source evidence, an intermediate method result, or an explicit unknown; do not invent information |
| 4 | Source | Use source evidence, an intermediate method result, or an explicit unknown; do not invent information |
| 5 | Formula | Use source evidence, an intermediate method result, or an explicit unknown; do not invent information |
| 6 | Result | Use source evidence, an intermediate method result, or an explicit unknown; do not invent information |
| 7 | Limitations | Use source evidence, an intermediate method result, or an explicit unknown; do not invent information |

## Verification cases

**MK-068-C05 | A required denominator is zero**

Expected: Report that the formula is undefined; do not output a zero cost or an infinite target

**MK-068-C06 | Only some costs are supplied**

Expected: Retain the partial result and excluded items; do not call it complete profitability

## Method sources

Source file: 行銷策略實戰學程Day2-以終為始x降低成本x提升指標

Location: Costs

Source basis: extracted from course materials

Source URL: https://docs.google.com/presentation/d/1NdxlcqAKMPHqGVS5jbjSYR_UgOJSA0fS65OnTtQLEHQ/edit

English translation of source excerpt:

> Begin with the end in mind x reduce costs x improve metrics
