---
name: mk-048
description: "Price-perception distribution analysis. Use when the task requires a calculation table for four cumulative-proportion curves. Apply this method to the specified inputs and verify the deliverable"
---

# MK-048 | Price-perception distribution analysis

For a regular chat, upload `packs/mk-048.md`. It includes the shared rules, this method, and required references

## Purpose

This skill delivers: **A calculation table for four cumulative-proportion curves**

Curve intersections, cost floors, and launch decisions are distinct tasks; a price intersection does not guarantee maximum profit

## Required inputs

Provide the target group, four original answers, product/quantity and currency, sampling and cleaning rules. For existing curves, include the price grid, cumulative direction, and denominator. Explain the method with explicit assumptions when appropriate; costs are needed only for business-feasibility assessment

## Method

1. Organize the responses to each of the four questions into a price distribution/line: too cheap, somewhat expensive, good value, and too expensive
2. Compare all four lines on the same price axis to prepare for interpreting PMC, PME, OPP, and IPP
3. Do not replace intersections with averages first; PSM centers on the intersections of different price-perception curves

## Calculations and interpretation

At a common price p, use the same N responses with all four answers valid: the too-cheap proportion is the count with too-cheap threshold >= p divided by N; bargain/cheap uses the same direction. The somewhat-expensive proportion is the count with somewhat-expensive threshold <= p divided by N; too-expensive uses the same direction. All four curves share the price grid and denominator. Retain missing answers, inconsistent price ordering, and cleaning rules; do not discard answers to force an intersection

A discrete grid brackets a crossing interval. Report an estimated crossing only with a stated interpolation method. Report absent crossings or overlapping intervals rather than inventing a unique precise value. PMC crosses too-cheap with somewhat-expensive; PME crosses bargain/cheap with too-expensive; OPP crosses too-cheap with too-expensive; IPP crosses bargain/cheap with somewhat-expensive. These describe this sample's price perceptions; check costs and actual purchases separately

## Required output fields

| Order | Field | How to complete |
|---:|---|---|
| 1 | Price point | Use source evidence, an intermediate method result, or an explicit unknown; do not invent information |
| 2 | Valid response count | Use source evidence, an intermediate method result, or an explicit unknown; do not invent information |
| 3 | Cumulative proportion for each question | Use source evidence, an intermediate method result, or an explicit unknown; do not invent information |
| 4 | Intersection definition | Use source evidence, an intermediate method result, or an explicit unknown; do not invent information |
| 5 | Interpretable result | Use source evidence, an intermediate method result, or an explicit unknown; do not invent information |
| 6 | Excluded/unprocessed count | Use source evidence, an intermediate method result, or an explicit unknown; do not invent information |
| 7 | Limitations | Use source evidence, an intermediate method result, or an explicit unknown; do not invent information |

## Verification cases

**MK-048-A1 | At a price, two of four valid respondents have too-cheap thresholds >= p**

Expected: The too-cheap proportion is 2/4 = 50%; use the same denominator and each curve's direction for the other questions

**MK-048-A2 | No crossing appears on the discrete grid**

Expected: Report the absent intersection and interpretable range; do not use an average price as a crossing

## Method sources

Source file: 營業額提升主要關鍵（一）縱深橫寬產品/產品線企劃策略

Location: PSM

Source basis: extracted from course materials

Source URL: https://docs.google.com/presentation/d/1lIddPByRFVZeT-TR3CSaL_lEKkpJRloL6JQBLg1fO50/edit

English translation of source excerpt:

> Van Westendorp's PSM (Price Sensitivity Measurement) fundamentally asks about the target consumer's acceptance of a price. It asks not only whether a price is expensive or cheap, but also which price is "too cheap"
