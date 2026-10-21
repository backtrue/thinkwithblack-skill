---
name: mk-264
description: "Shopping SKU Waste Diagnosis. Use when you need a product-level comparison of spend and sales; apply this method to the specified inputs and verify the deliverable"
---

# MK-264｜Shopping SKU Waste Diagnosis

For a regular chat, upload `packs/mk-264.md`; it includes the shared rules, this method, and required references

## Purpose

This Skill delivers: **A product-level comparison of spend and sales**

Execution steps compiled by ThinkWithBlack for this method's stated purpose, 2026-10-21; the course outline and original sources are retained below

When IDs cannot be matched one-to-one, leave them unmatched rather than guess; do not invent a match rate without complete event samples

## Required Inputs

Product-key mapping, spend, valid orders/net revenue for a common period, attribution window, refunds/costs and brand targets

## Method Steps

1. Align spend and outcomes by product key, checking duplicates, one-to-many joins and unmatched records
2. Check attribution maturity, refunds and cost scope before calculating available CPA, ROAS and contribution
3. Classify against brand targets; distinguish limited delivery, tracking gaps and actual zero sales before diagnosing waste

## Calculation and Interpretation

CPA = spend / valid orders; ROAS = comparable attributed net revenue / spend. Zero denominators or missing data remain undefined; observed association is not incrementality

## Required Output Fields

| Order | Field | How to complete |
|---:|---|---|
| 1 | SKU and match state | Use the supplied source, calculation, or explicit unknown |
| 2 | Period and attribution maturity | Use the supplied source, calculation, or explicit unknown |
| 3 | Spend and valid outcomes | Use the supplied source, calculation, or explicit unknown |
| 4 | Costs and calculations | Use the supplied source, calculation, or explicit unknown |
| 5 | Brand target | Use the supplied source, calculation, or explicit unknown |
| 6 | Problem evidence | Use the supplied source, calculation, or explicit unknown |
| 7 | Next step and revision condition | Use the supplied source, calculation, or explicit unknown |

## Verification cases

**MK-264-A1 | Spend 100, outcome data unavailable**

Expected: Unknown sales; no CPA or waste claim

**MK-264-A2 | Spend 100, two mature valid orders**

Expected: CPA 50, compared with the brand target

## Method Sources

Original file: AI × Google Ads 搜尋廣告實戰課｜五堂課程大綱

Source location: SKU

Source basis: Extended from a course outline

Original URL: https://docs.google.com/document/d/10HOKMeR1qM9_LXmc7pYGXJ6tbOMJtBuFAxcuCCAJZk4/edit

English translation of source excerpt retained in the master table:

> • Common Shopping diagnoses: no product impressions, excessive click costs, clicks without conversions, budget wasted on specific SKUs, disapproved products, or insufficient data quality

### Additional Source Locations

Source verification record for the original course material

- Source code: GO
- Original location: SKU
- Original outline evidence (English translation): • Common Shopping diagnoses: no product impressions, excessive click costs, clicks without conversions, budget wasted on specific SKUs, disapproved products, or insufficient data quality
