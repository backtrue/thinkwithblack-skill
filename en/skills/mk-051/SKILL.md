---
name: mk-051
description: "Comparing price acceptance across customer groups. Use when the task requires group-specific price distributions on a consistent basis. Apply this method to the specified inputs and verify the deliverable"
---

# MK-051 | Comparing price acceptance across customer groups

For a regular chat, upload `packs/mk-051.md`. It includes the shared rules, this method, and required references

## Purpose

This skill delivers: **Group-specific price distributions on a consistent basis**

Curve intersections, cost floors, and launch decisions are distinct tasks; a price intersection does not guarantee maximum profit

## Required inputs

Provide: Product costs, target audience, raw survey responses, or survey purpose

## Method

1. Distribute the survey to different Personas/audiences and retain each response's customer-group affiliation
2. Calculate PSM curves and intersections separately for each group to see whether price acceptance differs
3. The course material also suggests comparing survey completion rates and CTR across Personas. These measure campaign response, not price acceptance itself

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

**MK-051-C05 | A respondent's four price answers have a contradictory order**

Expected: Retain and flag the original answers; report sensitivity separately under the established cleaning rules

**MK-051-C06 | The curves do not have an intersection defined by the source**

Expected: Deliver the distributions and the reason interpretation is unavailable; do not fabricate an intersection

## Method sources

Source file: 營業額提升主要關鍵（一）縱深橫寬產品/產品線企劃策略

Location: PSM

Source basis: extracted from course materials

Source URL: https://docs.google.com/presentation/d/1lIddPByRFVZeT-TR3CSaL_lEKkpJRloL6JQBLg1fO50/edit

English translation of source excerpt:

> Van Westendorp's PSM (Price Sensitivity Measurement) fundamentally asks about the target consumer's acceptance of a price. It asks not only whether a price is expensive or cheap, but also which price is "too cheap"
