---
name: mk-434
description: "Campaign Type Traffic Value Comparison. Use when work requires traffic, revenue, and limitations across campaigns; process the specified inputs using this method and verify the deliverable"
---

# MK-434 | Campaign Type Traffic Value Comparison

For ordinary chat, upload `packs/mk-434.md`, which includes the shared rules, this method, and required references

## Purpose

This skill delivers: **Traffic, revenue, and limitations across campaigns**

Adding impressions across platforms does not yield deduplicated reach; conversions with different attribution windows cannot be added as actual sitewide orders

## Required inputs

Provide: GA4, GSC, advertising, and sales exports, metric definitions, and costs

## Method steps

1. Use the campaign that first acquired the user as the dimension and read new users, total revenue, and sessions
2. Calculate each campaign's value per session to compare the value of traffic brought in by different campaigns
3. Preserve campaign results over time for future comparisons of campaign types; do not replace long-term campaign value records with one ROAS result

## Calculation and interpretation

Verify data sources, dates, currencies, denominators, and attribution; sums across platforms do not equal unique reach or incremental impact

## Required output fields

| Order | Field | How to fill it in |
|---:|---|---|
| 1 | Comparison item | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 2 | Subject / version A | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 3 | Subject / version B | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 4 | Definition / basis | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 5 | Comparability | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 6 | Difference | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 7 | Source | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 8 | Limitations | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |

## Validation cases

**MK-434-C05｜Comparison periods differ in length or definition**

Expected: Do not directly compare totals; first list what is not comparable and what can safely be compared

## Method sources

Original file: 營業額提升主要關鍵（三）從數據來提升 ROI 的策略

Source locator: reports

Source basis: extracted from course materials

Original URL: https://docs.google.com/presentation/d/1lwpCxF1cMgaK7Gnvngw8NzytDLYD8MK-p91g8dwSytU/edit

English translation of source excerpt retained in the master sheet:

> What reports are produced
