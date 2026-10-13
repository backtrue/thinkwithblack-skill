---
name: mk-049
description: "Interpreting the acceptable price range. Use when the task requires explanation of intersections, the reasonable price range, and their limitations. Apply this method to the specified inputs and verify the deliverable"
---

# MK-049 | Interpreting the acceptable price range

For a regular chat, upload `packs/mk-049.md`. It includes the shared rules, this method, and required references

## Purpose

This skill delivers: **Explanation of intersections, the reasonable price range, and their limitations**

Curve intersections, cost floors, and launch decisions are distinct tasks; a price intersection does not guarantee maximum profit

## Required inputs

Provide: Product costs, target audience, raw survey responses, or survey purpose

## Method

1. PMC, the minimum reasonable price, is the intersection of "too cheap" and "somewhat expensive"; prices below it may raise quality concerns
2. PME, the maximum reasonable price, is the intersection of "good value" and "too expensive"; prices above it may exceed the target group's perceived value
3. Treat PMC–PME as the reasonable price range, then assess it alongside costs and the contribution margin ratio rather than relying only on the survey

## Calculations and interpretation

Check sampling, valid responses, and the ordering of price questions; willingness to pay is neither actual purchasing nor a profit guarantee

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

**MK-049-C05 | A respondent's four price answers have a contradictory order**

Expected: Retain and flag the original answers; report sensitivity separately under the established cleaning rules

**MK-049-C06 | The curves do not have an intersection defined by the source**

Expected: Deliver the distributions and the reason interpretation is unavailable; do not fabricate an intersection

## Method sources

Source file: 營業額提升主要關鍵（一）縱深橫寬產品/產品線企劃策略

Location: PSM

Source basis: extracted from course materials

Source URL: https://docs.google.com/presentation/d/1lIddPByRFVZeT-TR3CSaL_lEKkpJRloL6JQBLg1fO50/edit

English translation of source excerpt:

> Van Westendorp's PSM (Price Sensitivity Measurement) fundamentally asks about the target consumer's acceptance of a price. It asks not only whether a price is expensive or cheap, but also which price is "too cheap"
