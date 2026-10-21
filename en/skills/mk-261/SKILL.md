---
name: mk-261
description: "Product Barcode Completeness Check. Use when you need missing identifiers such as GTIN; apply this method to the specified inputs and verify the deliverable"
---

# MK-261｜Product Barcode Completeness Check

For a regular chat, upload `packs/mk-261.md`; it includes the shared rules, this method, and required references

## Purpose

This Skill delivers: **Missing identifiers such as GTIN**

Execution steps compiled by ThinkWithBlack for this method's stated purpose, 2026-10-21; the course outline and original sources are retained below

When IDs cannot be matched one-to-one, leave them unmatched rather than guess; do not invent a match rate without complete event samples

## Required Inputs

Feed identifiers, manufacturer/package records, variants and current Merchant Center diagnostics

## Method Steps

1. Match each product/variant to original identifier records and retain unmatched items
2. Distinguish missing values, formatting issues, mismatched codes and products with no manufacturer identifier; never invent a code
3. List original values, authoritative sources and proposed corrections; check current Google identifier requirements for this product type and reread diagnostics after an applied correction

## Calculation and Interpretation

The same title does not establish the same variant; without diagnostic readback, keep the listing status unverified

## Required Output Fields

| Order | Field | How to complete |
|---:|---|---|
| 1 | Product/variant key | Use the supplied source, calculation, or explicit unknown |
| 2 | Original Feed value | Use the supplied source, calculation, or explicit unknown |
| 3 | Manufacturer evidence | Use the supplied source, calculation, or explicit unknown |
| 4 | Missing/conflicting value | Use the supplied source, calculation, or explicit unknown |
| 5 | Proposed value and basis | Use the supplied source, calculation, or explicit unknown |
| 6 | Applicable rule source | Use the supplied source, calculation, or explicit unknown |
| 7 | Readback state | Use the supplied source, calculation, or explicit unknown |

## Verification Cases

**MK-261-A1 | Two sizes have different codes**

Expected: Match by variant

**MK-261-A2 | No manufacturer code is supplied**

Expected: Record missing evidence/rule check; do not invent a GTIN

## Method Sources

Original file: AI × Google Ads 搜尋廣告實戰課｜五堂課程大綱

Source location: GTIN

Source basis: Extended from a course outline

Original URL: https://docs.google.com/document/d/10HOKMeR1qM9_LXmc7pYGXJ6tbOMJtBuFAxcuCCAJZk4/edit

English translation of source excerpt retained in the master table:

> • Core Product Feed fields: Title, Description, Image, Price, Availability, Brand, GTIN, Google Product Category, Product Type, Custom Label, and others

### Additional Source Locations

Source verification record for the original course material

- Source code: GO
- Original location: GTIN
- Original outline evidence (English translation): • Core Product Feed fields: Title, Description, Image, Price, Availability, Brand, GTIN, Google Product Category, Product Type, Custom Label, and others
