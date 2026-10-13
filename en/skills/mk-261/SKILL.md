---
name: mk-261
description: "Product Barcode Completeness Check. Use when you need missing identifiers such as GTIN; apply this method to the specified inputs and verify the deliverable"
---

# MK-261｜Product Barcode Completeness Check

For a regular chat, upload `packs/mk-261.md`; it includes the shared rules, this method, and required references

## Purpose

This Skill delivers: **Missing identifiers such as GTIN**

Preserve the original task name and delivery scope. This method was developed from the master-table task and approved entry requirements, not claimed as new rules quoted verbatim from the course. The original source is a course outline, and the detailed method still requires approval/review. Do not infer unauthorized product behavior, business thresholds, or platform capabilities from this draft

When IDs cannot be matched one-to-one, leave them unmatched rather than guess; do not invent a match rate without complete event samples

## Required Inputs

Provide: product Feed, actual website information, SKU performance, and disapproval messages

## Method Steps

1. Start with Merchant Center / Product Feed and actual product data, handling only “Product Barcode Completeness Check”
2. The outline explicitly supports Title, Description, Image, Price, Availability, Brand, GTIN, Google Product Category, Product Type, Custom Label, Product Group, Shopping Search Terms, and disapproval/data-quality diagnosis
3. When delivering “Missing identifiers such as GTIN,” trace the result to the actual Feed, SKU performance, search terms, or disapproval messages; if data is missing, list only the missing items
4. Merchant Center field requirements, disapproval rules, and Shopping capabilities change; check current Google official information before actual execution, and do not invent fixed rules absent from the outline

## Calculation and Interpretation

Use product data for specifications and prices; verify catalog fields and disapproval rules during production

## Required Output Fields

| Order | Field | How to fill it |
|---:|---|---|
| 1 | Subject / location | Original evidence, intermediate method result, or explicitly unknown; do not fabricate |
| 2 | Conditions for use | Original evidence, intermediate method result, or explicitly unknown; do not fabricate |
| 3 | Actual evidence | Original evidence, intermediate method result, or explicitly unknown; do not fabricate |
| 4 | Check status | Original evidence, intermediate method result, or explicitly unknown; do not fabricate |
| 5 | Differences / possible causes | Original evidence, intermediate method result, or explicitly unknown; do not fabricate |
| 6 | Next task | Original evidence, intermediate method result, or explicitly unknown; do not fabricate |
| 7 | Limitations | Original evidence, intermediate method result, or explicitly unknown; do not fabricate |

## Verification Cases

**MK-261-C05｜Data meets existing conditions**

Expected: report usable or keep as is; do not invent a need for changes

**MK-261-C06｜The tool returns an error**

Expected: report data not obtained; do not classify the tool error as a business anomaly

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
