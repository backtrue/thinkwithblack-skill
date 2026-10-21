---
name: mk-383
description: "Days to First Repeat Purchase Calculation. Use when work requires the interval between the first and second valid purchases; process the specified inputs using this method and verify the deliverable"
---

# MK-383 | Days to First Repeat Purchase Calculation

For ordinary chat, upload `packs/mk-383.md`, which includes the shared rules, this method, and required references

## Purpose

This skill delivers: **The interval between the first and second valid purchases**

Do not rank RFM results from different observation periods as if they shared one basis; separately verify the purpose and authorization for any list export or use

## Required inputs

Raw inputs: anonymized customer keys, valid deduplicated orders/dates, history coverage, cancellation/refund rules, timezone, reference date; cohort is all completed first-repeat customers or an explicitly specified F=2 group

## Method steps

1. Apply validity/deduplication and sort orders per customer. Verify sufficient history to identify the first purchase. Partial history gives the first two observed orders with a coverage gap, not a true first-repeat claim
2. For first-repeat timing, include customers with at least two valid orders, including three-or-more purchasers. Restrict to F=2 only when explicitly requested and label that cohort
3. Take the first two valid orders per eligible customer; interval is second purchase date minus first. Use the specified day definition and timezone. Two distinct valid same-day orders can yield zero; duplicated orders cannot create a repeat
4. Mean first-repeat days is total eligible intervals/eligible customer count; median/distribution may be separate. Customers without a second purchase remain unobserved, not zero or included in the completed-repeat mean. No eligible customers gives an undefined mean
5. Deliver cohort, first two orders, intervals, sample count and incomplete/uncovered records. A third order does not remove a completed first repeat. Added history, second orders or cancellation corrections trigger recomputation. Compare matched cohorts/mature windows; a shorter mean alone is not a campaign effect

## Calculation and interpretation

Hypothetical complete valid history: A purchases January 1, 11 and 21, giving first-repeat interval 10 days. B purchases January 1 and 31, giving 30 days. The all-completed-repeat mean is (10+30)/2=20; only an explicitly requested F=2 cohort yields 30, not the all-repeat mean

Decision rules authored by ThinkWithBlack on 2026-10-14; original course sources are retained below

## Required output fields

| Order | Field | How to fill it in |
|---:|---|---|
| 1 | Variable | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 2 | Definition | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 3 | Source / unit | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 4 | Formula | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 5 | Input value | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 6 | Result | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 7 | Missing items / limitations | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |

## Verification cases

**MK-383-A1 | Three purchases, first-to-second gap ten days**

Expected: Include in all first-repeat customers unless exact F = 2 is requested

## Method sources

Original file: 營業額提升主要關鍵（二）社群/會員經營技巧

Source locator: RFM

Source basis: extracted from course materials

Original URL: https://docs.google.com/presentation/d/1ZYpstuVAXGk9KdZt1QZm2OQ7ozpYYtfrBf0Xsy7kRx8/edit

English translation of source excerpt retained in the master sheet:

> Use RFM rules for segmentation to turn new customers (one purchase) into returning customers (more than one purchase)
