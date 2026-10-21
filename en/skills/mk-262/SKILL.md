---
name: mk-262
description: "Product Custom Label Design. Use when you need labels for margin, price tier, campaign, and product line; apply this method to the specified inputs and verify the deliverable"
---

# MK-262｜Product Custom Label Design

For a regular chat, upload `packs/mk-262.md`; it includes the shared rules, this method, and required references

## Purpose

This Skill delivers: **Labels for margin, price tier, campaign, and product line**

Execution steps compiled by ThinkWithBlack for this method's stated purpose, 2026-10-21; the course outline and original sources are retained below

When IDs cannot be matched one-to-one, leave them unmatched rather than guess; do not invent a match rate without complete event samples

## Required Inputs

SKUs, costs/margin definition, price, campaigns/product lines, existing labels and project-specific bands

## Method Steps

1. Identify the management decision for each dimension: margin, price band, campaign or product line
2. Define names, allowed values, inclusive/exclusive boundaries, sources and refresh timing; leave missing business cutoffs open
3. Apply rules per SKU and report missing or multiple matches; deliver the dictionary and mapping, checking current Merchant Center specifications before producing import fields

## Calculation and Interpretation

Fix currency/cost definitions; bands must not overlap and must explicitly handle unclassified products

## Required Output Fields

| Order | Field | How to complete |
|---:|---|---|
| 1 | Dimension and purpose | Use the supplied source, calculation, or explicit unknown |
| 2 | Field and allowed values | Use the supplied source, calculation, or explicit unknown |
| 3 | Bands and sources | Use the supplied source, calculation, or explicit unknown |
| 4 | SKU mapping | Use the supplied source, calculation, or explicit unknown |
| 5 | Missing/conflicting values | Use the supplied source, calculation, or explicit unknown |
| 6 | Refresh timing | Use the supplied source, calculation, or explicit unknown |

## Verification Cases

**MK-262-A1 | 100 matches both ≤100 and ≥100**

Expected: Resolve the boundary before assigning

**MK-262-A2 | Cost is unknown**

Expected: Leave margin label pending; price is not margin

## Method Sources

Original file: AI × Google Ads 搜尋廣告實戰課｜五堂課程大綱

Source location: Custom Label

Source basis: Extended from a course outline

Original URL: https://docs.google.com/document/d/10HOKMeR1qM9_LXmc7pYGXJ6tbOMJtBuFAxcuCCAJZk4/edit

English translation of source excerpt retained in the master table:

> • Core Product Feed fields: Title, Description, Image, Price, Availability, Brand, GTIN, Google Product Category, Product Type, Custom Label, and others

### Additional Source Locations

Source verification record for the original course material

- Source code: GO
- Original location: Custom Label
- Original outline evidence (English translation): • Core Product Feed fields: Title, Description, Image, Price, Availability, Brand, GTIN, Google Product Category, Product Type, Custom Label, and others
