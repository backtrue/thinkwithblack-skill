---
name: mk-071
description: "Average order value and conversion-rate sensitivity analysis. Use when the task requires revenue and profit changes under different assumptions. Apply this method to the specified inputs and verify the deliverable"
---

# MK-071 | Average order value and conversion-rate sensitivity analysis

For a regular chat, upload `packs/mk-071.md`. It includes the shared rules, this method, and required references

## Purpose

This skill delivers: **Revenue and profit changes under different assumptions**

Working backward to resource requirements is not a forecast or optimal allocation; do not decide actual spending without an affordable ceiling

## Required inputs

Provide: Revenue, costs, average order value, conversion rate, fixed expenses, and target assumptions

## Method

1. Calculate scenarios using revenue = traffic × conversion rate × average order value
2. Hold two variables constant and separately test how changes in average order value, conversion rate, or traffic affect orders and revenue
3. Use the break-even target to judge which lever deserves attention first; an increase in a single metric does not automatically improve profit

## Calculations and interpretation

Scenario revenue = consistently defined traffic × conversion rate × average order value; calculate scenario contribution separately by deducting each cost

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

**MK-071-C05 | A required denominator is zero**

Expected: Report that the formula is undefined; do not output a zero cost or an infinite target

**MK-071-C06 | Only some costs are supplied**

Expected: Retain the partial result and excluded items; do not call it complete profitability

## Method sources

Source file: 行銷策略實戰學程Day2-以終為始x降低成本x提升指標

Location: Costs

Source basis: extracted from course materials

Source URL: https://docs.google.com/presentation/d/1NdxlcqAKMPHqGVS5jbjSYR_UgOJSA0fS65OnTtQLEHQ/edit

English translation of source excerpt:

> Begin with the end in mind x reduce costs x improve metrics
