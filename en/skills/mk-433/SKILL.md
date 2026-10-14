---
name: mk-433
description: "Landing Page Traffic Value Comparison. Use when work requires revenue and session comparisons on a consistent basis; process the specified inputs using this method and verify the deliverable"
---

# MK-433 | Landing Page Traffic Value Comparison

For ordinary chat, upload `packs/mk-433.md`, which includes the shared rules, this method, and required references

## Purpose

This skill delivers: **Revenue and session comparisons on a consistent basis**

Adding impressions across platforms does not yield deduplicated reach; conversions with different attribution windows cannot be added as actual sitewide orders

## Required inputs

Raw inputs: landing-page breakdowns by source/medium, new/returning visitor and period, sessions, valid orders, net revenue, costs and content, with report dimensions/attribution

## Method steps

1. Fix property, landing-page definition, time, device/region and refund maturity. Keep revenue/session numerators and denominators and distinguish user, session and event scopes. Deliver valid partial comparisons rather than mix scopes
2. Compare source and new/returning strata first. When page mixes differ, report within-stratum results. Use common session weights only when a shared mix is supplied; otherwise show strata without invented representative weights
3. Check matched demand, usable CTA and purchasing. Fix demonstrated landing gaps behind low value. Concentrated members/branded traffic behind high value do not establish that buying more new-visitor traffic will work
4. Comparable valid outcomes and costs support bounded traffic candidates. Sparse large orders, immature refunds or missing critical costs call for observation. If removing the largest order reverses ranking, deliver sensitivity and the order to check rather than one definitive winner
5. Deliver page comparisons, comparable strata, action and next evidence. Recompute when mix, valid orders, page or costs change. Evaluate new inputs against incremental contribution and full costs, preserving the distinction between observation and causal evidence

## Calculation and interpretation

Session value is same-scope net revenue/sessions. Aggregate numerators and denominators instead of daily ratios. A common-mix comparison is the sum of common weights times stratum values

Hypothetical check with matched demand, usable pages and affordable costs: A has new/returning values 2/10 and session counts 10/90; B has values 3/8 and counts 90/10. Aggregate values are A=9.2 and B=3.5, but B is the new-visitor candidate. For the same returning-user task, A becomes the candidate

Scope reference: [Google Analytics traffic-source scopes](https://support.google.com/analytics/answer/11080067?hl=en)

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

**MK-433-C05｜Comparison periods differ in length or definition**

Expected: Do not directly compare totals; first list what is not comparable and what can safely be compared

## Method sources

Original file: 營業額提升主要關鍵（三）從數據來提升 ROI 的策略

Source locator: reports

Source basis: extracted from course materials

Original URL: https://docs.google.com/presentation/d/1lwpCxF1cMgaK7Gnvngw8NzytDLYD8MK-p91g8dwSytU/edit

English translation of source excerpt retained in the master sheet:

> What reports are produced
