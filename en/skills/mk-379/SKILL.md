---
name: mk-379
description: "RFM Score Calculation. Use when work requires recalculable scores and their original basis; process the specified inputs using this method and verify the deliverable"
---

# MK-379 | RFM Score Calculation

For ordinary chat, upload `packs/mk-379.md`, which includes the shared rules, this method, and required references

## Purpose

This skill delivers: **Recalculable scores and their original basis**

Do not rank RFM results from different observation periods as if they shared one basis; separately verify the purpose and authorization for any list export or use

## Required inputs

Raw inputs: customer/valid-order/refund data, reference date and full window; approved R/F/M scoring intervals with inclusive boundaries, direction, total/average M and rule version, plus code mapping when labels are needed

## Method steps

1. Calculate raw R as days from last valid purchase to the reference date, F as deduplicated valid orders in the specified window, and M as approved net total or average. Retain dates, window, validity and details
2. Apply approved intervals per axis and require exactly one match. Overlaps are rule conflicts and gaps are unmapped, not nearest-score assignments. Without a valid purchase R is undefined and follows approved no-purchase rules
3. The course three-digit code concatenates 1–5 scores in R/F/M order: 5,4,3 becomes 543. Total Score is a classification code, not sum 12 or weighted value. Other score ranges require approved encoding and mapping
4. Deliver raw RFM, matched intervals, three scores, code and rule version per member. Labels require the same-version approved map; without one retain computed scores/code rather than guess loyalty or dormancy
5. Recompute affected scores/groups after orders, refunds, reference dates, boundaries or M definitions change, retaining previous values. Different windows/versions are not direct evidence of member improvement or decline

## Calculation and interpretation

Fillable five-tier intervals (supply approved increasing cut points/version before use; an existing brand table takes precedence)

| Score | R days (lower is more recent) | F valid orders | M approved amount |
|---:|---|---|---|
| 1 | R ≥ r4 | F < f1 | M < m1 |
| 2 | r3 ≤ R < r4 | f1 ≤ F < f2 | m1 ≤ M < m2 |
| 3 | r2 ≤ R < r3 | f2 ≤ F < f3 | m2 ≤ M < m3 |
| 4 | r1 ≤ R < r2 | f3 ≤ F < f4 | m3 ≤ M < m4 |
| 5 | 0 ≤ R < r1 | F ≥ f4 | M ≥ m4 |

Cut points increase within each axis and retain units. F here applies to valid purchasers; zero purchases follow separate approved rules. Without cut points, deliver raw values and an unset table, not universal thresholds

Hypothetical approved cut points: R 30 with r1=31,r2=61,r3=91,r4=121 scores 5; F 4 with f1=2,f2=3,f3=4,f4=5 scores 4; M 250 with m1=100,m2=200,m3=300,m4=400 scores 3; code 543. Changing r1 to 30 places R=30 in 30 ≤ R < 61, score 4, giving code 443

Source: [Original course slides 30–33: intervals and Total Score](https://docs.google.com/presentation/d/1ZYpstuVAXGk9KdZt1QZm2OQ7ozpYYtfrBf0Xsy7kRx8/edit#slide=id.g2b001449a48_0_178)

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

**MK-379-A1 | An R value matches two bands**

Expected: Report overlap rather than choose the higher score

## Method sources

Original file: 營業額提升主要關鍵（二）社群/會員經營技巧

Source locator: RFM

Source basis: extracted from course materials

Original URL: https://docs.google.com/presentation/d/1ZYpstuVAXGk9KdZt1QZm2OQ7ozpYYtfrBf0Xsy7kRx8/edit

English translation of source excerpt retained in the master sheet:

> Use RFM rules for segmentation to turn new customers (one purchase) into returning customers (more than one purchase)
