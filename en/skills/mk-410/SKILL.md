---
name: mk-410
description: "Friend Lifetime Value Estimate. Use when work requires estimates with explicit periods, gross margins, and scenario assumptions; process the specified inputs using this method and verify the deliverable"
---

# MK-410 | Friend Lifetime Value Estimate

For ordinary chat, upload `packs/mk-410.md`, which includes the shared rules, this method, and required references

## Purpose

This skill delivers: **Estimates with explicit periods, gross margins, and scenario assumptions**

Do not send messages or create automation without approval; if a tool cannot show recipient eligibility, do not assume everyone can be messaged

## Required inputs


Available raw records: the original contact cohort including nonbuyers, linked orders and costs, acquisition spend, observation horizon, and messaging costs

## Method Steps

1. Fix acquisition cohort, source, and horizon, retaining all original contacts including nonbuyers, unsubscribers, and blockers. Join valid orders, product/fulfillment costs, acquisition spend, and operating costs to that same cohort
2. The course shortcut, annual purchases × average order value × margin, estimates margin per buyer if based only on buyers. CPF decisions require contribution per original contact, not the buyer-only value
3. Compare mature contribution per contact after operating costs with acquisition cost and the brand's retained-profit requirement. Coverage supports a candidate within that horizon; failure calls for cost/offer revision or stopping consideration
4. Short-term data yields realized value plus a separately labeled future scenario. Without separating organic purchases from incremental contact effects, total contribution is not the return on added acquisition spend. Request cohort/order mapping rather than asking the customer to calculate LTV
5. Recalculate affordable CPF after refunds, omitted nonbuyers, operating costs, or retention assumptions change. Replace extrapolation with newly mature longer-horizon results and do not rank unequal horizons together

## Calculation and Interpretation

Period contribution per contact = (all cohort net order revenue − product/variable fulfillment costs − operating costs not already included) / original contacts. Observed break-even CPF equals that value, less any required retained profit per person. Deduct acquisition expense separately once; no ratio with zero contacts

Check example (hypothetical): ten of 100 contacts contribute 500 each; operating costs are 1,000, yielding 40 per original contact. CPF of 60 is not recovered in this period. Later mature orders add 3,000 with no extra costs, yielding 70 per contact and changing the coverage decision for the longer horizon

Decision rules authored by ThinkWithBlack, 2026-10-14; original course sources remain below

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

**MK-410-A1 | Two sends have different observation windows**

Expected: Align windows before ranking immature outcomes

## Method sources

Original file: 行銷策略實戰學程 Day5｜Google Ads × LINE｜線上課程用投影片

Source locator: LINE

Source basis: extracted from course materials

Original URL: https://docs.google.com/presentation/d/1RK8wiunlvJrRxgFuTcGhO5B5fRa4fbEogpZTJpF6YKc/edit

English translation of source excerpt retained in the master sheet:

> Google Ads × LINE
