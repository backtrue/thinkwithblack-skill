---
name: mk-432
description: "New-Customer Conversion Source Analysis. Use when work requires source comparisons against first-purchase rates; process the specified inputs using this method and verify the deliverable"
---

# MK-432 | New-Customer Conversion Source Analysis

For ordinary chat, upload `packs/mk-432.md`, which includes the shared rules, this method, and required references

## Purpose

This skill delivers: **Source comparisons against first-purchase rates**

Adding impressions across platforms does not yield deduplicated reach; conversions with different attribution windows cannot be added as actual sitewide orders

## Required inputs


Available raw records: deidentified first-visit cohorts and sources, visit/purchase timestamps, order history, refunds, and acquisition and order costs

## Method Steps

1. Define whether new means first visit, first purchase, or first brand contact. Separate purchase on the first visit from a first purchase on a later return using deidentified user keys, first-visit source/time, purchase time, and valid orders
2. Compare sources within first-visit cohorts of equal observation length, retaining nonbuyers in the denominator. Session-source summaries support source performance reporting, not a cohort's long-term value
3. High conversion with low order contribution or high acquisition cost does not justify priority. Compare valid order contribution and acquisition cost per original new visitor, then consider scale, supply, and the cost objective
4. Observed contribution after acquisition cost meeting the objective, with capacity for added demand, supports a capped expansion test. Keep immature cohorts under observation; mature loss-making cohorts support reduction candidates. Existing attribution describes observed results; additional-budget effects need a subsequent comparable test
5. Rebuild the cohort and outcomes after first-visit attribution, refunds, or purchase-history corrections, withdrawing rankings that no longer qualify. Request missing cohort/order fields instead of dividing unrelated report totals

## Calculation and Interpretation

Same-cohort first-purchase rate = first buyers within the window / original new visitors. Contribution per new visitor = cohort net order revenue minus product and variable fulfillment costs, divided by original new visitors; then subtract acquisition cost per person on the same basis. Do not calculate with a zero denominator

Check example (hypothetical): A and B each bring 100 new visitors. A has ten buyers, 2,000 contribution, and 3,000 acquisition cost; B has five buyers, 2,500 contribution, and 1,000 cost. A's higher conversion does not give it priority. Refunds reducing B's contribution to 500 withdraw B's positive-contribution expansion candidate

Decision rules authored by ThinkWithBlack, 2026-10-14; original course sources remain below

## Required output fields

| Order | Field | How to fill it in |
|---:|---|---|
| 1 | Business action | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 2 | Event / field | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 3 | Source | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 4 | Period and level | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 5 | Denominator / currency | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 6 | Formula or naming | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 7 | Result | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 8 | Items to fix | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |

## Method sources

Original file: 營業額提升主要關鍵（三）從數據來提升 ROI 的策略

Source locator: reports

Source basis: extracted from course materials

Original URL: https://docs.google.com/presentation/d/1lwpCxF1cMgaK7Gnvngw8NzytDLYD8MK-p91g8dwSytU/edit

English translation of source excerpt retained in the master sheet:

> What reports are produced
