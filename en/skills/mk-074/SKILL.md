---
name: mk-074
description: "Marketing return on investment calculation. Use when the task requires an mROI calculation with explicit definitions and cost boundaries. Apply this method to the specified inputs and verify the deliverable"
---

# MK-074 | Marketing return on investment calculation

For a regular chat, upload `packs/mk-074.md`. It includes the shared rules, this method, and required references

## Purpose

This skill delivers: **An mROI calculation with explicit definitions and cost boundaries**

Recalculability does not mean the data is complete; break-even points and cost ceilings apply only under the stated assumptions

## Required inputs

Provide: Revenue, gross margin rate or costs, marketing expense and the ROI definition for the same analysis scope

For method questions, provide the formula, variables and an example directly; for a calculation, ask only for missing operands

## Method

1. The course mROI formula: [(revenue × gross margin ratio) − marketing expense] ÷ marketing expense × 100%
2. Use the same analysis scope for revenue, gross margin ratio, and marketing expense; do not force the calculation when marketing expense is zero
3. Use mROI to assess financial accountability; it does not replace process diagnosis of traffic, conversion, average order value, and related metrics

## Calculations and interpretation

Calculate using the ROI definition specified for this case. If none is specified, present advertising ROAS alongside available cost items; do not independently call revenue divided by spend a profit ROI

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

**MK-074-C05 | A required denominator is zero**

Expected: Report that the formula is undefined; do not output a zero cost or an infinite target

**MK-074-C06 | Only some costs are supplied**

Expected: Retain the partial result and excluded items; do not call it complete profitability

## Method sources

Source file: 營業額提升主要關鍵（三）從數據來提升 ROI 的策略

Location: mROI

Source basis: extracted from course materials

Source URL: https://docs.google.com/presentation/d/1lwpCxF1cMgaK7Gnvngw8NzytDLYD8MK-p91g8dwSytU/edit

English translation of source excerpt:

> mROI =
