---
name: mk-257
description: "Product Category Mapping. Use when you need mappings between internal and platform categories; apply this method to the specified inputs and verify the deliverable"
---

# MK-257｜Product Category Mapping

For a regular chat, upload `packs/mk-257.md`; it includes the shared rules, this method, and required references

## Purpose

This Skill delivers: **Mappings between internal and platform categories**

When IDs cannot be matched one-to-one, leave them unmatched rather than guess; do not invent a match rate without complete event samples

## Required Inputs

Provide: product Feed, actual website information, SKU performance, and disapproval messages

## Method Steps

1. Use google_product_category / fb_product_category and product_type to describe product categories
2. product_type can use breadcrumb levels, for example “Home > Womenswear > Dresses > Ankle-length dresses”
3. Categories must match the actual product and support later collection/catalog ad filtering; do not classify arbitrarily just to fill fields

## Calculation and Interpretation

Use product data for specifications and prices; verify catalog fields and disapproval rules during production

## Required Output Fields

| Order | Field | How to fill it |
|---:|---|---|
| 1 | Source subject | Original evidence, intermediate method result, or explicitly unknown; do not fabricate |
| 2 | Target subject | Original evidence, intermediate method result, or explicitly unknown; do not fabricate |
| 3 | Task to address | Original evidence, intermediate method result, or explicitly unknown; do not fabricate |
| 4 | Evidence of fit | Original evidence, intermediate method result, or explicitly unknown; do not fabricate |
| 5 | Applicable conditions | Original evidence, intermediate method result, or explicitly unknown; do not fabricate |
| 6 | Unmapped items / conflicts | Original evidence, intermediate method result, or explicitly unknown; do not fabricate |
| 7 | Next step | Original evidence, intermediate method result, or explicitly unknown; do not fabricate |

## Verification Cases

**MK-257-C05｜One subject has two different uses**

Expected: list uses and conditions separately rather than force a single match

## Method Sources

Original file: Meta廣告學程 105 有轉換是業績擴大的開始

Source location: Products

Source basis: Derived from course material

Original URL: https://docs.google.com/presentation/d/1RzfmYLhPsK23uxqxWbKji2-efsbJPGFs_tMzCRX56BM/edit

English translation of source excerpt retained in the master table:

> From product planning to catalog ads and collections, improve performance through budget allocation
