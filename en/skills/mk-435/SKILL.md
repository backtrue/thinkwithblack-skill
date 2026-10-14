---
name: mk-435
description: "Product Revenue, Gross Margin, and Conversion Comparison. Use when work requires product investment candidates and limits on causal interpretation; process the specified inputs using this method and verify the deliverable"
---

# MK-435 | Product Revenue, Gross Margin, and Conversion Comparison

For ordinary chat, upload `packs/mk-435.md`, which includes the shared rules, this method, and required references

## Purpose

This skill delivers: **Product investment candidates and limits on causal interpretation**

Adding impressions across platforms does not yield deduplicated reach; conversions with different attribution windows cannot be added as actual sitewide orders

## Required inputs

Raw inputs: same-period SKUs, valid deduplicated views/orders, net product revenue, margin definition, full variable costs, refunds, stock and advertising task

## Method steps

1. Verify SKU, period, product/order counts and refunds; separate unit price, revenue, gross margin and order contribution. Allocate shared bundle/fulfillment costs once using actual rules
2. Calculate the course revenue × margin ratio × conversion-rate index with view/valid-purchase numerators and denominators. Missing values or zero denominators remain unknown. The index ranks comparable candidates, not spendable profit
3. Then calculate same-period/per-order available contribution and check supply, fulfillment, returns and new input costs. High-index items with nonpositive contribution, no stock or failed fulfillment are not spend candidates. Fix demonstrated landing/supply gaps first
4. Select bounded exposure/content inputs among task-matched, cost-supported and fulfillable SKUs. Separate natural historical purchases from paid results. If removing the largest valid order reverses ranking, investigate. Without incremental evidence, use capped comparisons rather than extrapolate an optimal allocation
5. Deliver index, actual costs, available contribution, supply, selection and contrary evidence. Re-rank after refunds, mix or costs change; unchanged index does not retain eligibility automatically

## Calculation and interpretation

Course index I = net product revenue × specified gross-margin ratio × valid purchases/matching views. Available contribution C = net revenue minus same-scope non-ad variable costs; show ad costs separately and deduct once

Hypothetical check: A has a higher index but contribution -20; B has a lower index, contribution 100 and fulfillable stock, supporting B. A documented duplicate return cost corrected to contribution 150 makes A eligible for reconsideration

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

**MK-435-C05｜Comparison periods differ in length or definition**

Expected: Do not directly compare totals; first list what is not comparable and what can safely be compared

## Method sources

Original file: 營業額提升主要關鍵（三）從數據來提升 ROI 的策略

Source locator: reports

Source basis: extracted from course materials

Original URL: https://docs.google.com/presentation/d/1lwpCxF1cMgaK7Gnvngw8NzytDLYD8MK-p91g8dwSytU/edit

English translation of source excerpt retained in the master sheet:

> What reports are produced
