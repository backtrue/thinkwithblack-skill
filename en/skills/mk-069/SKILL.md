---
name: mk-069
description: "Post-discount profit calculation. Use when the task requires joint calculation of discounts, gifts, and logistics. Apply this method to the specified inputs and verify the deliverable"
---

# MK-069 | Post-discount profit calculation

For a regular chat, upload `packs/mk-069.md`. It includes the shared rules, this method, and required references

## Purpose

This skill delivers: **Joint calculation of discounts, gifts, and logistics**

Recalculability does not mean the data is complete; break-even points and cost ceilings apply only under the stated assumptions

## Required inputs

Provide: Discount/gift offer, discounted net revenue, order variable costs, additional promotional and fulfillment costs, and the brand contribution floor

For method questions, provide the formula, variables and an example directly; for a calculation, ask only for missing operands

## Method

1. Recalculate revenue, variable costs, and the contribution margin ratio after discounting to check whether the brand's acceptable floor is breached
2. Discounts are not evaluated on revenue alone. If the contribution margin ratio is below the course's 25% benchmark, prioritize cost reduction, higher average order value, or pricing/bundle adjustments
3. Include costs from gifts, free shipping, and discounts, not merely the percentage off the list price

## Calculations and interpretation

Post-discount contribution per order = discounted net revenue − order variable costs − additional promotional fulfillment costs

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

**MK-069-C05 | A required denominator is zero**

Expected: Report that the formula is undefined; do not output a zero cost or an infinite target

**MK-069-C06 | Only some costs are supplied**

Expected: Retain the partial result and excluded items; do not call it complete profitability

## Method sources

Source file: 行銷策略實戰學程Day2-以終為始x降低成本x提升指標

Location: Costs

Source basis: extracted from course materials

Source URL: https://docs.google.com/presentation/d/1NdxlcqAKMPHqGVS5jbjSYR_UgOJSA0fS65OnTtQLEHQ/edit

English translation of source excerpt:

> Begin with the end in mind x reduce costs x improve metrics
