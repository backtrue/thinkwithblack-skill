---
name: mk-067
description: "Calculate break-even ROAS from revenue and non-advertising expenses. Use for questions about which product costs to include, whether production and delivery alone suffice, how to incorporate monthly company fixed costs, and whether the lowest-priced variant can represent the whole range. For method questions, deliver cost definitions, formulas, and examples directly; check costs and sales mix when calculating actual figures. A break-even question alone does not trigger scaling or pricing workflows"
---

# MK-067 | Break-even return on ad spend calculation

For a regular chat, upload `packs/mk-067.md`. It includes the shared rules, this method, and required references

## Purpose

This skill delivers: **A threshold calculated using gross margin and the specified expense basis**

Recalculability does not mean the data is complete; break-even points and cost ceilings apply only under the stated assumptions

## Required inputs

For a method question, deliver the formula and an explicitly hypothetical example directly. An actual calculation requires net revenue, non-advertising expenses, and fixed expenses not yet included for the same period and product scope. For multiple variants, use quantities and revenue/costs per variant, or totals already aggregated using the actual mix. A break-even threshold alone does not require conversion rate, actual CPA, or budget utilization

## Method

1. Confirm the period, scope, and sources of revenue and non-advertising expenses; organize variant and overall amounts using the calculation sequence below
2. Calculate pre-advertising available contribution. Subtract fixed expenses not yet included when they must also be covered, then calculate break-even ROAS
3. Retain the formula, cost basis, sales mix, and excluded expenses; provide a method explanation or actual calculation as requested

## Calculations and interpretation

If advertising is the only remaining expense to cover, break-even ROAS = 1 ÷ pre-advertising contribution margin ratio

### Execution order for a break-even calculation

This section covers the break-even formula and method questions; check costs and calculate the threshold in order

1. Fix the period, currency, and product/variant scope; first confirm whether revenue is net of discounts and refunds. For each variant, list net revenue Rᵢ, non-advertising expenses Vᵢ for the same scope, and their sources. Include the product, payment/logistics, fulfillment, and other costs the question needs covered, counting each once. Advertising expense is the ceiling being solved for; do not deduct it into Vᵢ first. If only purchase costs are supplied, deliver a partial threshold and retain the remaining expense gaps
2. Calculate Cᵢ=Rᵢ−Vᵢ, then aggregate R=ΣRᵢ and C=ΣCᵢ using the actual sales mix. Multiply unit prices and unit costs by quantities sold first; do not multiply values already totaled for the period again. Check attribution of shared order expenses first so they are not deducted for every variant. Aggregate products, categories, and the entire store within their respective consistent scopes; actual advertising ROAS must use the same revenue scope
3. When R and C are both positive and advertising is the only remaining expense, the threshold is R÷C=1÷(C÷R). Deliver variant-level and overall results, expense definitions, and sales mix first. When R is zero/negative or C is zero/negative, do not output a positive break-even threshold; explain that there is currently no positive advertising allowance or valid revenue basis. If fixed expenses also need covering, list same-scope fixed expenses F separately and check whether they are already in V. Calculate R÷(C−F) only when there is no duplicate deduction and C−F is positive. Label results excluding fixed expenses as advertising break-even for the expense scope used

The lowest selling price does not imply the lowest contribution margin ratio. Do not substitute the cheapest variant for the whole product mix or directly average variant ROAS thresholds. When sales mix is unknown, deliver variant thresholds and the overall formula. Calculate future mixes as explicitly assumed scenarios; do not treat historical mix as a guarantee of the future

Purely hypothetical teaching example: variant A has net revenue 100, non-advertising expenses 50, an allowance of 50, and a threshold of 2. Variant B has net revenue 200, non-advertising expenses 160, an allowance of 40, and a threshold of 5. Selling one of each gives an overall threshold of 300÷90=10/3, not (2+5)÷2=3.5. Lower-priced A actually has the lower threshold. If the question is only how to calculate it, these formulas and counterexample provide a complete answer; obtain actual variants, sales volumes, and expenses only when calculating for a specific store

Retain this skill's seven required output fields: input variable, value, unit and definition, source, formula, result, and limitations. Label teaching numbers as assumptions and keep unknown case values unknown. Do not omit the method answer because store-specific figures are missing

This section expands the existing reciprocal formula arithmetically. Separating non-advertising costs and fixed expenses refers to [Shopify break-even calculation and FAQ](https://www.shopify.com/uk/blog/break-even-roas-calculator). Aggregation across variants and the lowest-price counterexample are derivations for this method; they introduce no market threshold and are not presented as verbatim course content

Retain original values, units, periods, and substituted formulas. The formula is not an unconditional guarantee of results

Define gross profit, contribution margin, cost denominators, and periods explicitly; do not copy classroom example numbers as universal thresholds

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

**MK-067-C05 | A required denominator is zero**

Expected: Report that the formula is undefined; do not output a zero cost or an infinite target

**MK-067-C06 | Only some costs are supplied**

Expected: Retain the partial result and excluded items; do not call it complete profitability

## Method sources

Source file: Meta廣告學程 104 廣告的數據決策

Location: ROAS

Source basis: extracted from course materials

Source URL: https://docs.google.com/presentation/d/16FiqnSxBs-gSDxsxUBNhWdUX5vZrIWoZPGangj_f_Pk/edit

English translation of source excerpt:

> Reasonable ROAS
