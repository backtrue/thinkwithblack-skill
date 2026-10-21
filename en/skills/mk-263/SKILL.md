---
name: mk-263
description: "Shopping Product Group Planning. Use when you need groups based on product data and business strategy; apply this method to the specified inputs and verify the deliverable"
---

# MK-263｜Shopping Product Group Planning

For a regular chat, upload `packs/mk-263.md`; it includes the shared rules, this method, and required references

## Purpose

This Skill delivers: **Groups based on product data and business strategy**

Execution steps compiled by ThinkWithBlack for this method's stated purpose, 2026-10-21; the course outline and original sources are retained below

When IDs cannot be matched one-to-one, leave them unmatched rather than guess; do not invent a match rate without complete event samples

## Required Inputs

Product Feed, available attributes/labels, current product groups, management goal and exclusions

## Method Steps

1. Choose grouping keys for the management purpose, such as product-line control, and verify they exist
2. Write inclusion/exclusion rules and map SKUs, reporting unclassified and overlapping items
3. Check coverage and justified exclusions, then deliver the group tree/mapping; verify supported subdivision fields against the current interface

## Calculation and Interpretation

Separate grouping purpose from bidding/exclusion decisions; do not stop products using invented thresholds

## Required Output Fields

| Order | Field | How to complete |
|---:|---|---|
| 1 | Group and parent | Use the supplied source, calculation, or explicit unknown |
| 2 | Management purpose | Use the supplied source, calculation, or explicit unknown |
| 3 | Attribute rules | Use the supplied source, calculation, or explicit unknown |
| 4 | SKU list | Use the supplied source, calculation, or explicit unknown |
| 5 | Exclusions and remainder | Use the supplied source, calculation, or explicit unknown |
| 6 | Overlap check | Use the supplied source, calculation, or explicit unknown |
| 7 | Proposed action | Use the supplied source, calculation, or explicit unknown |

## Verification cases

**MK-263-A1 | A SKU lacks product line**

Expected: Keep it as unclassified

**MK-263-A2 | A SKU matches two exclusive groups**

Expected: Flag conflicting rules

## Method Sources

Original file: AI × Google Ads 搜尋廣告實戰課｜五堂課程大綱

Source location: Product Group

Source basis: Extended from a course outline

Original URL: https://docs.google.com/document/d/10HOKMeR1qM9_LXmc7pYGXJ6tbOMJtBuFAxcuCCAJZk4/edit

English translation of source excerpt retained in the master table:

> • Product Group and Custom Label: how to manage groups by product line, margin, price tier, campaign, or business strategy

### Additional Source Locations

Source verification record for the original course material

- Source code: GO
- Original location: Product Group
- Original outline evidence (English translation): • Product Group and Custom Label: how to manage groups by product line, margin, price tier, campaign, or business strategy
