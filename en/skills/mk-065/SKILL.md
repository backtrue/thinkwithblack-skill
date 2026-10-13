---
name: mk-065
description: "Working backward to target cost per click. Use when the task requires cPC derived from acceptable CPA and conversion rate. Apply this method to the specified inputs and verify the deliverable"
---

# MK-065 | Working backward to target cost per click

For a regular chat, upload `packs/mk-065.md`. It includes the shared rules, this method, and required references

## Purpose

This skill delivers: **CPC derived from acceptable CPA and conversion rate**

Recalculability does not mean the data is complete; break-even points and cost ceilings apply only under the stated assumptions

## Required inputs

Provide: Revenue, costs, average order value, conversion rate, fixed expenses, and target assumptions

## Method

1. The course formula for ideal CPC is: ideal CPA × conversion rate, namely target revenue / average order value × gross margin ratio × 30% × conversion rate
2. Use actual conversion data from the same funnel and period; do not force a precise CPC calculation without a reliable conversion rate
3. If CPC is too high, return to diagnosing CTR, audiences/creative, and the pricing model; do not treat CPC alone as the root cause

## Calculations and interpretation

Target CPC = Target CPA × purchase conversion rate per corresponding click

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

**MK-065-C05 | A required denominator is zero**

Expected: Report that the formula is undefined; do not output a zero cost or an infinite target

**MK-065-C06 | Only some costs are supplied**

Expected: Retain the partial result and excluded items; do not call it complete profitability

## Method sources

Source file: Meta廣告學程 104 廣告的數據決策

Location: CPC

Source basis: extracted from course materials

Source URL: https://docs.google.com/presentation/d/16FiqnSxBs-gSDxsxUBNhWdUX5vZrIWoZPGangj_f_Pk/edit

English translation of source excerpt:

> Cost per click (CPC)
