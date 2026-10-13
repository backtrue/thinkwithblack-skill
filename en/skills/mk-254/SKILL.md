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

Provide: product Feed, actual website information, SKU performance, and disapproval messages

## Method Steps

1. A Feed can contain both price for the original price and sale_price for the promotional price
2. Match catalog prices to actual product page/campaign prices so the ad and landing page do not differ
3. Follow the platform's Feed price format requirements; the course example is “1,000 TWD / 800 TWD”

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

**MK-254-C05｜Data meets existing conditions**

Expected: report usable or keep as is; do not invent a need for changes

**MK-254-C06｜The tool returns an error**

Expected: report data not obtained; do not classify the tool error as a business anomaly

## Method Sources

Original file: Meta廣告學程 105 有轉換是業績擴大的開始

Source location: Products

Source basis: Derived from course material

Original URL: https://docs.google.com/presentation/d/1RzfmYLhPsK23uxqxWbKji2-efsbJPGFs_tMzCRX56BM/edit

English translation of source excerpt retained in the master table:

> From product planning to catalog ads and collections, improve performance through budget allocation
