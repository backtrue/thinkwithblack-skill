---
name: mk-075
description: "Cost-metric definition review. Use when the task requires a check for mixed use of leads, people, and orders. Apply this method to the specified inputs and verify the deliverable"
---

# MK-075 | Cost-metric definition review

For a regular chat, upload `packs/mk-075.md`. It includes the shared rules, this method, and required references

## Purpose

This skill delivers: **A check for mixed use of leads, people, and orders**

Recalculability does not mean the data is complete; break-even points and cost ceilings apply only under the stated assumptions

## Required inputs

Raw inputs: requested metric, expense scope, clicks, valid deduplicated leads, valid orders, buyers/new-customer keys, period, currency, attribution and validity definitions

## Method

1. Name the outcome as clicks, leads, orders, buyers or new customers and map each to a source field. First purchasers are not leads and buyer counts are not order counts; correct existing mislabeled formulas and denominators
2. Click cost uses matching spend/clicks; lead cost matching spend/valid deduplicated leads; order cost matching spend/valid deduplicated orders. Buyer cost and new-customer CAC use their respective counts, with CAC expenses scoped as specified
3. Before combining sources verify period, currency, click definitions and expenses. Mixing outbound and incompatible all-click counts is not one CPC. Deduplicate overlapping platform-attributed purchases using valid order keys or report platform values separately
4. Zero denominators mean report spend and zero outcomes with undefined cost. Missing sources/partial costs retain partial values and missing items. Without validity rules report raw fields rather than infer sale, cancellation or new-customer definitions
5. Deliver numerator, denominator, population, period, currency, deduplication and result for each metric. Recompute relevant values after orders, refunds, identity coverage or attribution corrections, retaining prior values and change sources

## Calculations and interpretation

Hypothetical check with approved common spend 600: 300 matching clicks, 20 valid leads, 6 valid orders, 5 buyers and 3 new customers yield 2/click, 30/lead, 100/order, 120/buyer and 200/new customer. Different outcome definitions cannot be compared as deterioration in the same task

Decision rules authored by ThinkWithBlack on 2026-10-14; original course sources are retained below

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

**MK-075-C05 | A required denominator is zero**

Expected: Report that the formula is undefined; do not output a zero cost or an infinite target

**MK-075-C06 | Only some costs are supplied**

Expected: Retain the partial result and excluded items; do not call it complete profitability

## Method sources

Source file: LookerStudio教學

Location: Formulas for each metric

Source basis: extracted from course materials

Source URL: https://docs.google.com/presentation/d/15dCCATrfSb0jHMhvfvp-15aQ5CvYW9xafHYPGm_pm3o/edit

English translation of source excerpt:

> Formulas for each metric
