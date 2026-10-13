---
name: mk-064
description: "Customer acquisition cost ceiling calculation. Use when the task requires an estimate based on average order value, gross margin, and the affordable allocation. Apply this method to the specified inputs and verify the deliverable"
---

# MK-064 | Customer acquisition cost ceiling calculation

For a regular chat, upload `packs/mk-064.md`. It includes the shared rules, this method, and required references

## Purpose

This skill delivers: **An estimate based on average order value, gross margin, and the affordable allocation**

Recalculability does not mean the data is complete; break-even points and cost ceilings apply only under the stated assumptions

## Required inputs

Provide: Revenue, costs, average order value, conversion rate, fixed expenses, and target assumptions

## Method

1. The course formula for ideal CPA is: target revenue / average order value × gross margin ratio × 30%. For example, with an average order value of 1,200 and a gross margin ratio of 60%, ideal CPA is 216
2. The 30% is the course's benchmark for allocating advertising expenses, not an accounting rule for every brand. Confirm it against the brand's actual profit and loss and goals before formal use
3. Only after CPA fits the cost constraints should budget utilization and scaling be assessed; do not look at a single CPA alone

## Calculations and interpretation

An already specified Target CPA takes priority. Only when a simplified estimate is approved for this case, Target CPA = average order value × gross margin ratio × acceptable advertising-cost allocation

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

**MK-064-C05 | A required denominator is zero**

Expected: Report that the formula is undefined; do not output a zero cost or an infinite target

**MK-064-C06 | Only some costs are supplied**

Expected: Retain the partial result and excluded items; do not call it complete profitability

## Method sources

Source file: Meta廣告學程 104 廣告的數據決策

Location: CPA

Source basis: extracted from course materials

Source URL: https://docs.google.com/presentation/d/16FiqnSxBs-gSDxsxUBNhWdUX5vZrIWoZPGangj_f_Pk/edit

English translation of source excerpt:

> Reasonable CPA
