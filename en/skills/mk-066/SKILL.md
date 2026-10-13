---
name: mk-066
description: "Working backward to target cost per add-to-cart. Use when the task requires cost derived from the add-to-cart purchase rate and CPA. Apply this method to the specified inputs and verify the deliverable"
---

# MK-066 | Working backward to target cost per add-to-cart

For a regular chat, upload `packs/mk-066.md`. It includes the shared rules, this method, and required references

## Purpose

This skill delivers: **Cost derived from the add-to-cart purchase rate and CPA**

Recalculability does not mean the data is complete; break-even points and cost ceilings apply only under the stated assumptions

## Required inputs

Provide: Revenue, costs, average order value, conversion rate, fixed expenses, and target assumptions

## Method

1. A reasonable ROAS can be derived as average order value ÷ ideal CPA; the course example is 1,200 ÷ 216 = 5.56
2. Set ROAS first from the brand's gross margin and advertising affordability; do not apply a fixed ROAS threshold across brands
3. After ROAS meets the target, also check whether the budget is fully spent. High ROAS at insufficient volume does not mean the sales target has been achieved

## Calculations and interpretation

Reasonable cost per add-to-cart = Target CPA × add-to-cart-to-purchase ratio

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

**MK-066-C05 | A required denominator is zero**

Expected: Report that the formula is undefined; do not output a zero cost or an infinite target

**MK-066-C06 | Only some costs are supplied**

Expected: Retain the partial result and excluded items; do not call it complete profitability

## Method sources

Source file: Meta廣告學程 104 廣告的數據決策

Location: Add to cart

Source basis: extracted from course materials

Source URL: https://docs.google.com/presentation/d/16FiqnSxBs-gSDxsxUBNhWdUX5vZrIWoZPGangj_f_Pk/edit

English translation of source excerpt:

> Today's add-to-cart completion rate = 30%, meaning an order requires 3.3 adds to cart. Completing an order costs 450, so each add to cart carries 450 / 3.3 = NT$136
