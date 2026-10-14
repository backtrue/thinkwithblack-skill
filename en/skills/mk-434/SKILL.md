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

Raw inputs: campaign type and first-acquisition date, customer cohort, matched observation duration with valid orders/sessions/net revenue, full costs, offers and dimension scopes

## Method steps

1. Distinguish later value of first-acquisition campaign types from sessions in a current campaign. Keep First user campaign and Session campaign separate and preserve the requested purpose
2. Build comparable first-acquisition cohorts and observe equal durations from equal starting points, with matched refund/cancellation maturity. For younger cohorts compare only completed common windows
3. List customers, valid orders, net revenue, sessions, all campaign costs and available contribution. Separate contribution per acquired customer from value per session and include ad/discount/gift costs
4. Retain or boundedly repeat types meeting the target in comparable mature cohorts. Change types when demand exists but landing/incentive costs need fixing. Reduce/stop mature cost failures and observe immature cohorts. Without a suitable control, differences support candidates rather than attribute all repeat purchases to the campaign
5. Deliver cohorts, windows, costs and choice. Update when refunds/repeats/costs are completed; build a new comparison for changed purpose, offers or customer mix rather than impose old averages

## Calculation and interpretation

Period contribution is cohort net revenue minus variable product/fulfillment costs and campaign costs not already deducted. Per-customer value is same-scope contribution/deduplicated cohort customers. Window revenue is not complete lifetime value

Hypothetical check: A contributes 200 from ten new customers; B contributes 180 from six, giving 20/30 per customer and supporting B. Adding B's omitted gift cost of 120 lowers its value to 10; switch priority to A

Dimension reference: [Google Analytics traffic-source scopes](https://support.google.com/analytics/answer/11080067?hl=en)

Decision rules authored by ThinkWithBlack on 2026-10-14; original course sources are retained below

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
