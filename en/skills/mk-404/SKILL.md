---
name: mk-404
description: "LINE Stage Tag Design. Use when work requires statuses for joining, consideration, first purchase, and repeat purchase; process the specified inputs using this method and verify the deliverable"
---

# MK-404 | LINE Stage Tag Design

For ordinary chat, upload `packs/mk-404.md`, which includes the shared rules, this method, and required references

## Purpose

This skill delivers: **Statuses for joining, consideration, first purchase, and repeat purchase**

Do not send messages or create automation without approval; if a tool cannot show recipient eligibility, do not assume everyone can be messaged

## Required inputs


Available raw records: deidentified contact keys, event occurrence and arrival times, orders/refunds, approved stage rules, and consent/opt-out scope

## Method Steps

1. List join, browse, inquiry, valid payment, refund, and unsubscribe events by the same deidentified contact key, retaining occurrence and ingestion times. Verify joins rather than merging similar names
2. Separate commercial stage, product job, and contact eligibility. A valid purchase of the same product moves first-purchase education to usage or continuation. VIP is an entitlement tag that can coexist with purchased status
3. Order events by occurrence time and valid-order state. A late-arriving older browse event does not move a buyer back to consideration. Apply the brand's refund definition without automatically reissuing a first-purchase coupon
4. Missing joins or conflicting events leave known facts plus an unresolved state; withhold identity-dependent targeting and request the conflicting order/contact key. Purchase status does not grant messaging consent
5. Update the affected field and message task after valid orders, full refunds, renewed consent, or opt-outs. Apply opt-outs to their actual channel or global scope without guessing other-channel eligibility

## Calculation and Interpretation

Deliver raw event → current stage → entitlements/eligibility → usable message task → transition event. If nonbuyer/considering/buyer share one field, specify precedence. Sleeping status follows product cycles and existing rules separately

Check example (hypothetical): a valid purchase on the 14th is followed on the 15th by a browse event that occurred on the 13th; keep purchased status. A later full refund excluded by the brand's valid-order rule triggers stage recalculation, while coupon eligibility still follows its own rules

Decision rules authored by ThinkWithBlack, 2026-10-14; original course sources remain below

## Required output fields

| Order | Field | How to fill it in |
|---:|---|---|
| 1 | Goal | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 2 | Audience | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 3 | Plan / task | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 4 | Evidence and assumptions | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 5 | Prerequisites | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 6 | Resources | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 7 | Deliverables and acceptance | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 8 | Unresolved items | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |

## Verification cases

**MK-404-A1 | One tag represents two distinct needs**

Expected: Split rules or clarify purpose instead of forcing one message

## Method sources

Original file: 行銷策略實戰學程 Day5｜Google Ads × LINE｜線上課程用投影片

Source locator: LINE

Source basis: extracted from course materials

Original URL: https://docs.google.com/presentation/d/1RK8wiunlvJrRxgFuTcGhO5B5fRa4fbEogpZTJpF6YKc/edit

English translation of source excerpt retained in the master sheet:

> Google Ads × LINE
