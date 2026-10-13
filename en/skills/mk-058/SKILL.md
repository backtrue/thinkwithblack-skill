---
name: mk-058
description: "Classifying fixed and variable costs. Use when the task requires a comparison of fixed expenses and per-order variable expenses. Apply this method to the specified inputs and verify the deliverable"
---

# MK-058 | Classifying fixed and variable costs

For a regular chat, upload `packs/mk-058.md`. It includes the shared rules, this method, and required references

## Purpose

This skill delivers: **A comparison of fixed expenses and per-order variable expenses**

Recalculability does not mean the data is complete; break-even points and cost ceilings apply only under the stated assumptions

## Required inputs

Provide: Revenue, costs, average order value, conversion rate, fixed expenses, and target assumptions

## Method

1. Fixed costs occur regardless of sales, such as rent, permanent staff, utilities, and some fixed marketing expenses
2. Variable costs arise from sales, such as production/purchasing, temporary labor, payment processing, logistics, digital-advertising CPA, channel revenue shares, and taxes/tax provisions
3. Classify costs using the brand's actual accounting. Do not put all advertising costs into the same category; the course material demonstrates both fixed marketing expenses and digital-ad costs that vary with orders

## Calculations and interpretation

Separate fixed costs from costs that vary with order volume. Split mixed costs using the breakdown supplied for this case; do not guess unknown splits

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

**MK-058-C05 | A required denominator is zero**

Expected: Report that the formula is undefined; do not output a zero cost or an infinite target

**MK-058-C06 | Only some costs are supplied**

Expected: Retain the partial result and excluded items; do not call it complete profitability

## Method sources

Source file: 行銷策略實戰學程Day2-以終為始x降低成本x提升指標

Location: Costs

Source basis: extracted from course materials

Source URL: https://docs.google.com/presentation/d/1NdxlcqAKMPHqGVS5jbjSYR_UgOJSA0fS65OnTtQLEHQ/edit

English translation of source excerpt:

> Begin with the end in mind x reduce costs x improve metrics
