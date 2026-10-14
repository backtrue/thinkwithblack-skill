---
name: mk-206
description: "Hero Post Candidate Selection. Use when you need candidates with sample size and performance across multiple dimensions; apply this method to the specified inputs and verify the deliverable"
---

# MK-206｜Hero Post Candidate Selection

For a regular chat, upload `packs/mk-206.md`; it includes the shared rules, this method, and required references

## Purpose

This Skill delivers: **Candidates with sample size and performance across multiple dimensions**

Past success supports candidates and hypotheses only; shared content elements are not proven causes of success

## Required Inputs


Available raw records: Post ID records by audience and objective, with spend, impressions, clicks, mature outcomes, and usage scope

## Method Steps

1. Aggregate spend, impressions, clicks, engagement, valid orders, and order contribution by Post ID while preserving audience temperature, offer, page, and observation maturity. Do not collapse different contexts into one winner
2. Within the same task and comparable context, a sales objective prioritizes mature valid outcomes and acceptable cost. High CTR or engagement without mature sales support remains an attention or education candidate, not a sales workhorse
3. Check fragility by removing the largest order and asking whether the result changes from meeting the objective to missing it. A reversal keeps the post as a test candidate with the dependency identified, not a cross-audience winner
4. Mature, within-limit results across several intended audiences support continued use within those observed conditions. Warm-audience success alone restricts the recommendation to warm audiences
5. Expired products or offers, refund-adjusted failure, or failure in a new audience withdraw the corresponding use scope. If order mapping is missing, request outcomes by Post ID rather than substituting an arbitrary spend threshold

## Calculation and Interpretation

CTR = clicks / impressions in the same scope; cost per outcome = spend / valid outcomes. Report conversion, clicks, engagement, and replication across contexts together. Removing the largest order is a fragility check, not a statistical test

Check example (hypothetical): two posts each spend 2,000. A has one 20,000 order; B has several mature orders within the established cost limit. Keep A as a candidate and use B within its observed audience. Refunds later push B over the limit; return it to testing or withdrawal consideration

Decision rules authored by ThinkWithBlack, 2026-10-14; original course sources remain below

## Required Output Fields

| Order | Field | How to fill it |
|---:|---|---|
| 1 | Post ID | Original evidence, intermediate method result, or explicitly unknown; do not fabricate |
| 2 | Source and period | Original evidence, intermediate method result, or explicitly unknown; do not fabricate |
| 3 | Performance across four dimensions | Original evidence, intermediate method result, or explicitly unknown; do not fabricate |
| 4 | Sample limitations | Original evidence, intermediate method result, or explicitly unknown; do not fabricate |
| 5 | Suitable use | Original evidence, intermediate method result, or explicitly unknown; do not fabricate |
| 6 | Elements to retain | Original evidence, intermediate method result, or explicitly unknown; do not fabricate |
| 7 | Test arrangement | Original evidence, intermediate method result, or explicitly unknown; do not fabricate |
| 8 | Reasons for not using | Original evidence, intermediate method result, or explicitly unknown; do not fabricate |

## Method Sources

Original file: Meta廣告學程 103 如何有效放大成效

Source location: Hero

Source basis: Derived from course material

Original URL: https://docs.google.com/presentation/d/1LoV6FtBtLBi4MRoWgygvmEhgq7FwirK0Ik2_PJP6_8k/edit

English translation of source excerpt retained in the master table:

> These ads embody the Hero Post concept
