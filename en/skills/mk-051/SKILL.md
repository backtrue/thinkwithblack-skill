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


Available raw records: raw four-question price responses, respondent groups, product and question wording, offers, recruitment records, and cleaning rules

## Method Steps

1. Align product descriptions, quantities, the four price questions, currency, exposed offers, and sampling periods. Preserve each response's original group and identify overlap rather than treating the same person as two independent respondents
2. Flag missing answers and contradictory price ordering under the established cleaning rule. If no rule exists, retain and flag the originals and compare results with and without contradictions; do not silently delete records to obtain intersections
3. Use the same price grid and curve calculations for every group. Overlapping intervals, missing intersections, or rankings reversed by removing a few responses do not support stable price separation
4. Differences that persist under comparable product terms and cleaning sensitivity support price or offer test candidates, followed by cost and actual purchase checks. CTR and completion rates describe recruitment response, not price acceptance
5. Different offers or quantities invalidate a group-price explanation; rebuild comparable groups. Request the original four questions and product description rather than asking the customer to interpret curves

## Calculation and Interpretation

At price p, the too-cheap curve is the share of valid four-question respondents whose too-cheap threshold is at least p; bargain uses the same direction. Expensive is the share whose expensive threshold is at most p; too-expensive uses that direction. PMC is the intersection of too-cheap and expensive; PME is the intersection of bargain and too-expensive. Discrete grids bracket crossings; do not invent exact intersections when none exist

Check example (hypothetical): A's interval is 800–1,000 and B's is 900–1,100. Retain the overlap and compare costs rather than automatically charging B more. Discovering that B saw a two-pack changes the finding to different product conditions and withdraws the group-price conclusion

Decision rules authored by ThinkWithBlack, 2026-10-14; original course sources remain below

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
