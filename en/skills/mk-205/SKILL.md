---
name: mk-205
description: "Aggregate Performance for the Same Post. Use when you need post-level performance across ads; apply this method to the specified inputs and verify the deliverable"
---

# MK-205｜Aggregate Performance for the Same Post

For a regular chat, upload `packs/mk-205.md`; it includes the shared rules, this method, and required references

## Purpose

This Skill delivers: **Post-level performance across ads**

Past success supports candidates and hypotheses only; shared content elements are not proven causes of success

## Required Inputs

Post ID-to-ad mapping, same-period spend, impressions and consistently defined click/engagement/conversion counts, task and attribution window

## Method Steps

1. Match ad rows by Post ID, remove repeated exports and fix period, click/engagement definitions, task and attribution window
2. Sum additive, mutually exclusive comparable rows for cost, impressions, clicks and valid outcomes, then recompute rates from summed numerators/denominators; do not sum or average row CTRs
3. Keep acquisition/re-engagement and traffic/sales tasks separate; overlapping conversion attribution is not deduplicated real orders
4. Deliver raw totals, formulas and results, leaving zero-denominator rates undefined

## Calculation and Interpretation

CTR = consistently defined clicks / total impressions; CPC = total spend / corresponding clicks; cost per sale = comparable spend / corresponding valid sales. Preserve click type and percentage units for CTR

## Required Output Fields

| Order | Field | How to complete |
|---:|---|---|
| 1 | Post ID/source ad rows | Use the supplied source, calculation, or explicit unknown |
| 2 | Task, period and attribution window | Use the supplied source, calculation, or explicit unknown |
| 3 | Spend/impression totals | Use the supplied source, calculation, or explicit unknown |
| 4 | Click, engagement and sale counts | Use the supplied source, calculation, or explicit unknown |
| 5 | Numerators/denominators/formulas | Use the supplied source, calculation, or explicit unknown |
| 6 | Recomputed results | Use the supplied source, calculation, or explicit unknown |
| 7 | Duplicates/noncomparable rows | Use the supplied source, calculation, or explicit unknown |
| 8 | Interpretation | Use the supplied source, calculation, or explicit unknown |

## Verification cases

**MK-205-A1 | Comparable rows: 100 impressions/10 clicks and 900 impressions/9 clicks**

Expected: CTR = 19/1000 = 1.9%, not row-average5.5%

**MK-205-A2 | Rows use different click definitions**

Expected: Calculate separately, not one combined CTR

## Method Sources

Original file: Meta廣告學程 103 如何有效放大成效

Source location: Hero

Source basis: Derived from course material

Original URL: https://docs.google.com/presentation/d/1LoV6FtBtLBi4MRoWgygvmEhgq7FwirK0Ik2_PJP6_8k/edit

English translation of source excerpt retained in the master table:

> These ads embody the Hero Post concept
