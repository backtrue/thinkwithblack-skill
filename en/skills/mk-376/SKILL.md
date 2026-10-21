---
name: mk-376
description: "Member Cumulative Spend Calculation. Use when work requires purchase amounts with clear refund and period definitions; process the specified inputs using this method and verify the deliverable"
---

# MK-376 | Member Cumulative Spend Calculation

For ordinary chat, upload `packs/mk-376.md`, which includes the shared rules, this method, and required references

## Purpose

This skill delivers: **Purchase amounts with clear refund and period definitions**

Do not rank RFM results from different observation periods as if they shared one basis; separately verify the purpose and authorization for any list export or use

## Required inputs

Raw inputs: anonymized customer keys, valid deduplicated orders, dates, receipts/refunds; total or average M definition, order validity rules, observation period and currency

## Method steps

1. Fix M as cumulative net consumption or average order value in the specified period, without mixing definitions across members. Specify period, order dates and refund allocation; unknown rules retain raw values and pending definitions
2. Deduplicate customer/order keys, apply case-defined cancellation/refund validity and sum period net amounts. Retain receipts, refunds and inclusion per order; product rows are not orders
3. Cumulative M is total valid-order net amounts; average M is that total/valid-order count. Average is undefined with zero orders; confirmed no valid transactions yields cumulative zero, while missing sources mean unavailable data
4. Label historical receipts as historical net consumption, not complete customer lifetime value. Contribution requires specified costs; future LTV needs a horizon, retention/purchase and cost model. Without that model leave LTV unestimated
5. Deliver period, definition, included details and result per member. Recompute and update dependent scores/groups after refunds, added orders, coverage or M-definition changes rather than reuse a different-definition ranking

## Calculation and interpretation

Hypothetical check: two valid orders net 100 and 200 give cumulative M 300 and average M 150. A further refund 50 on the second order, with both still valid under the case rule, changes them to 250 and 125. Full-refund order inclusion follows the case validity rule

Decision rules authored by ThinkWithBlack on 2026-10-14; original course sources are retained below

## Required output fields

| Order | Field | How to fill it in |
|---:|---|---|
| 1 | Variable | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 2 | Definition | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 3 | Source / unit | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 4 | Formula | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 5 | Input value | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 6 | Result | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 7 | Missing items / limitations | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |

## Verification cases

**MK-376-A1 | Valid orders 100 and 200, second refunded 50 but remains valid**

Expected: Total 250, mean 125, with the refund rule retained

## Method sources

Original file: 營業額提升主要關鍵（二）社群/會員經營技巧

Source locator: RFM

Source basis: extracted from course materials

Original URL: https://docs.google.com/presentation/d/1ZYpstuVAXGk9KdZt1QZm2OQ7ozpYYtfrBf0Xsy7kRx8/edit

English translation of source excerpt retained in the master sheet:

> Use RFM rules for segmentation to turn new customers (one purchase) into returning customers (more than one purchase)
