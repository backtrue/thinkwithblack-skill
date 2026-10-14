---
name: mk-108
description: "Gift-with-purchase threshold planning. Use when the task requires calculations of average order value, gift cost, and spending thresholds. Apply this method to the specified inputs and verify the deliverable"
---

# MK-108 | Gift-with-purchase threshold planning

For a regular chat, upload `packs/mk-108.md`. It includes the shared rules, this method, and required references

## Purpose

This skill delivers: **Calculations of average order value, gift cost, and spending thresholds**

Do not fabricate discounts, gift inventory, countdown deadlines, limited quantities, or testimonials

## Required inputs


Available raw records: paid order amounts, item costs, gift and fulfillment costs, inventory, and stacking rules

## Method Steps

1. Use order-level paid amounts, items, variable costs, genuine add-on options, gift cost/inventory, and stacking rules to construct threshold candidates from real baskets, not a fixed multiple of average order value
2. Separate orders already qualifying from orders needing additional purchases. Existing qualifiers still consume gifts; additional buying is a scenario until observed
3. Calculate total contribution change against the original baskets. Reject a scenario when added contribution cannot cover gifts for all qualifying orders, extra fulfillment, and campaign costs, even if average order value rises
4. Real complementary demand, acceptable costs, and sufficient inventory support a capped test candidate. Without uptake evidence, report the break-even add-on count and feasible options; request actual orders near the threshold rather than inventing a lift rate
5. Revise or stop when actual redemption, displaced full-price sales, or refunds make added contribution negative. Any threshold change requires recounting existing qualifiers

## Calculation and Interpretation

Added contribution = scenario net revenue minus scenario product/fulfillment variable costs, all gifts, extra campaign costs, and baseline contribution. Do not subtract a discount already reflected in revenue twice. With equal-cost gifts, additional add-on contribution times uptake must cover all gifts and extra costs

Check example (hypothetical): 40 orders already qualify and ten add-ons each contribute 60; 50 gifts cost 20 each. Added contribution is 600 − 1,000 = −400, so reject that scenario. Gifts costing eight instead produce 200, making it a test candidate; the ten assumed add-ons still need validation

Decision rules authored by ThinkWithBlack, 2026-10-14; original course sources remain below

## Required output fields

| Order | Field | How to complete |
|---:|---|---|
| 1 | Goal | Use source evidence, an intermediate method result, or an explicit unknown; do not invent information |
| 2 | Audience | Use source evidence, an intermediate method result, or an explicit unknown; do not invent information |
| 3 | Plan/task | Use source evidence, an intermediate method result, or an explicit unknown; do not invent information |
| 4 | Evidence and assumptions | Use source evidence, an intermediate method result, or an explicit unknown; do not invent information |
| 5 | Prerequisites | Use source evidence, an intermediate method result, or an explicit unknown; do not invent information |
| 6 | Resources | Use source evidence, an intermediate method result, or an explicit unknown; do not invent information |
| 7 | Deliverables and acceptance | Use source evidence, an intermediate method result, or an explicit unknown; do not invent information |
| 8 | Open issues | Use source evidence, an intermediate method result, or an explicit unknown; do not invent information |

## Verification cases

**MK-108-C05 | The budget is unknown, but materials can be organized first**

Expected: Deliver the parts of the plan that do not depend on the budget first; do not require a complete questionnaire

## Method sources

Source file: 行銷策略實戰學程Day4-佈局獲利 × 節奏變現 × 轉單收割

Location: Campaign

Source basis: extracted from course materials

Source URL: https://docs.google.com/presentation/d/1dq3xqYVUnWvUCpzZKI91yDDOzvkyG0uHy3EOsOjtItA/edit

English translation of source excerpt:

> Consider consumers with active needs each month and bring campaign traffic to the campaign page for prompt conversion
