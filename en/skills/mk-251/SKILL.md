---
name: mk-251
description: "Product ID Mapping Check. Use when you need mappings across product, variant, and tracking event IDs; apply this method to the specified inputs and verify the deliverable"
---

# MK-251｜Product ID Mapping Check

For a regular chat, upload `packs/mk-251.md`; it includes the shared rules, this method, and required references

## Purpose

This Skill delivers: **Mappings across product, variant, and tracking event IDs**

When IDs cannot be matched one-to-one, leave them unmatched rather than guess; do not invent a match rate without complete event samples

## Required Inputs

Feed product/variant IDs, actual ViewContent/AddToCart/Purchase event samples and product identifiers, website SKU mapping and relevant event times

## Method Steps

1. Catalog product id must match content_id in Pixel/SDK events; the course generally recommends SKU as a common standard
2. Check whether content_id in ViewContent, AddToCart, and Purchase maps to a catalog product
3. If it does not, fix the event or Feed mapping first; do not guess products from similar names

## Calculation and Interpretation

Use product data for specifications and prices; verify catalog fields and disapproval rules during production

## Required Output Fields

| Order | Field | How to fill it |
|---:|---|---|
| 1 | Product / variant | Original evidence, intermediate method result, or explicitly unknown; do not fabricate |
| 2 | IDs from each source | Original evidence, intermediate method result, or explicitly unknown; do not fabricate |
| 3 | Field | Original evidence, intermediate method result, or explicitly unknown; do not fabricate |
| 4 | Feed value | Original evidence, intermediate method result, or explicitly unknown; do not fabricate |
| 5 | Website value | Original evidence, intermediate method result, or explicitly unknown; do not fabricate |
| 6 | Update time | Original evidence, intermediate method result, or explicitly unknown; do not fabricate |
| 7 | Issue classification | Original evidence, intermediate method result, or explicitly unknown; do not fabricate |
| 8 | Correction location | Original evidence, intermediate method result, or explicitly unknown; do not fabricate |
| 9 | Status | Original evidence, intermediate method result, or explicitly unknown; do not fabricate |

## Verification cases

**MK-251-A1 | Feed exists but event samples do not**

Expected: Record missing event evidence without claiming a matching pass

## Method Sources

Original file: Meta廣告學程 105 有轉換是業績擴大的開始

Source location: Products

Source basis: Derived from course material

Original URL: https://docs.google.com/presentation/d/1RzfmYLhPsK23uxqxWbKji2-efsbJPGFs_tMzCRX56BM/edit

English translation of source excerpt retained in the master table:

> From product planning to catalog ads and collections, improve performance through budget allocation
