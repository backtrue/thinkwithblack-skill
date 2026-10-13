---
name: mk-255
description: "Product Stock Status Check. Use when you need availability and data update issues; apply this method to the specified inputs and verify the deliverable"
---

# MK-255｜Product Stock Status Check

For a regular chat, upload `packs/mk-255.md`; it includes the shared rules, this method, and required references

## Purpose

This Skill delivers: **Availability and data update issues**

When IDs cannot be matched one-to-one, leave them unmatched rather than guess; do not invent a match rate without complete event samples

## Required Inputs

Provide: product Feed, actual website information, SKU performance, and disapproval messages

## Method Steps

1. availability must reflect the actual selling status, such as in stock, available for order, preorder, out of stock, or discontinued
2. Products with frequent stock changes are not suited to long-term maintenance through a one-off manual file alone
3. If the catalog shows an item as purchasable while the website is out of stock, fix data updates before advertising

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

**MK-255-C05｜Data meets existing conditions**

Expected: report usable or keep as is; do not invent a need for changes

**MK-255-C06｜The tool returns an error**

Expected: report data not obtained; do not classify the tool error as a business anomaly

## Method Sources

Original file: Meta廣告學程 105 有轉換是業績擴大的開始

Source location: Products

Source basis: Derived from course material

Original URL: https://docs.google.com/presentation/d/1RzfmYLhPsK23uxqxWbKji2-efsbJPGFs_tMzCRX56BM/edit

English translation of source excerpt retained in the master table:

> From product planning to catalog ads and collections, improve performance through budget allocation
