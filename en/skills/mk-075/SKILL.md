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

Provide: Revenue, costs, average order value, conversion rate, fixed expenses, and target assumptions

## Method

1. The course's three cost formulas are: traffic acquisition cost=(Meta Amount Spent + Google Ads spend) ÷ (Meta Clicks/Outbound Click + Google clicks); lead acquisition cost=advertising spend ÷ first-time buyers; order acquisition cost=advertising spend ÷ total buyers
2. Before use, confirm consistent periods, currencies, click definitions, and denominators across sources
3. Mark the result incalculable if the denominator is zero or sources are missing; do not force cross-platform figures together

## Calculations and interpretation

Check the numerator, denominator, population, period, currency, attribution, and deduplication for each metric

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
