---
name: mk-254
description: "Product Price Consistency Check. Use when you need differences between catalog, offer, and website prices; apply this method to the specified inputs and verify the deliverable"
---

# MK-254｜Product Price Consistency Check

For a regular chat, upload `packs/mk-254.md`; it includes the shared rules, this method, and required references

## Purpose

This Skill delivers: **Differences between catalog, offer, and website prices**

When IDs cannot be matched one-to-one, leave them unmatched rather than guess; do not invent a match rate without complete event samples

## Required Inputs

Catalog platform, SKU or variant and currency; feed regular price, sale price, and effective period; current page price for the same variant, read time, promotion conditions and time zone; current price-field specifications

## Method Steps

1. Align feed and product page by SKU or variant, recording prices, currency, read time, and promotion conditions
2. Check regular price, sale price, and start or end time separately; use a common time zone to determine the effective price at read time instead of treating expired or future promotions as current
3. Compare the actual payable product price under matching page conditions and identify currency, amount, period, or variant discrepancies; leave inaccessible pages unresolved
4. Verify amount, currency, and time-field formatting against the catalog platform’s current official requirements and record the source and date; course typography with thousands separators is not a feed serialization rule
5. Deliver raw values, discrepancies, proposed corrections, and evidence per item; after an actual update, read back the feed and page, keeping unexecuted changes labeled as proposals

## Calculation and Interpretation

Use product data for specifications and prices; verify catalog fields and disapproval rules during production

## Required Output Fields

| Order | Field | How to complete |
|---:|---|---|
| 1 | SKU or variant, platform, and currency | Use the supplied source, calculation, or explicit unknown |
| 2 | Feed regular and sale prices | Use the supplied source, calculation, or explicit unknown |
| 3 | Effective period, time zone, and read time | Use the supplied source, calculation, or explicit unknown |
| 4 | Page price and promotion conditions | Use the supplied source, calculation, or explicit unknown |
| 5 | Discrepancy and effective price | Use the supplied source, calculation, or explicit unknown |
| 6 | Format specification source and date | Use the supplied source, calculation, or explicit unknown |
| 7 | Proposed value and evidence | Use the supplied source, calculation, or explicit unknown |
| 8 | Actual update and readback status | Use the supplied source, calculation, or explicit unknown |

## Verification Cases

**MK-254-A1 | A promotion expired but the feed still shows its sale price while the page shows the regular price**

Expected: Align time zone and SKU, flag the effective-period and price mismatch, and propose a correction while recording actual update and readback status

## Method Sources

Original file: Meta廣告學程 105 有轉換是業績擴大的開始

Source location: Products

Source basis: Derived from course material

Original URL: https://docs.google.com/presentation/d/1RzfmYLhPsK23uxqxWbKji2-efsbJPGFs_tMzCRX56BM/edit

English translation of source excerpt retained in the master table:

> From product planning to catalog ads and collections, improve performance through budget allocation
