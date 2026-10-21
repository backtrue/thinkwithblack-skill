---
name: mk-391
description: "Replenishment Reminder Timing Plan. Use when work requires reminder hypotheses based on usage and historical cycles; process the specified inputs using this method and verify the deliverable"
---

# MK-391 | Replenishment Reminder Timing Plan

For ordinary chat, upload `packs/mk-391.md`, which includes the shared rules, this method, and required references

## Purpose

This skill delivers: **Reminder hypotheses based on usage and historical cycles**

Customer segmentation and actual eligibility to receive marketing messages are separate matters

## Required inputs


Available raw records: last valid order, product quantity, actual start and usage, remaining stock, later replenishment, delivery time, and contact eligibility

## Method Steps

1. Inspect last valid purchase, whether the product is consumable, usable quantity, actual start date, usage rate, and later replenishment. Purchase date is not automatically the usage start
2. Known quantity, rate, and start date support an estimated depletion date and a reminder adjusted for actual delivery preparation. Product-specific historical intervals support a repurchase-window candidate, not an exact depletion date
3. Do not apply replenishment to a durable product or ended use. Match a genuine compatible consumable or service when that is the next need. Exclude people who replenished, have remaining stock, or cannot be contacted
4. If usage is missing, request existing package quantity and one usage or remaining-stock record rather than a complete questionnaire. If still unknown, deliver a cycle condition rather than a fabricated calendar date
5. Recalculate from updated stock after replenishment, remaining-quantity, or usage changes. Cancel the schedule for refunded, undelivered orders and adjust promises for supply delays

## Calculation and Interpretation

Usable days = usable quantity / actual daily usage. Estimated depletion = actual start date + usable days; subtract known delivery preparation for the reminder. Zero or intermittent usage requires separate treatment, not forced division. Deliver evidence, timing, and cancellation/rescheduling conditions

Check example (hypothetical): 300 mL used from day one at 10 mL/day lasts about 30 days. On day ten, a record shows 250 mL remaining and 5 mL/day usage; estimate another 50 days from that date and postpone the original reminder

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

**MK-391-A1 | Replenishment cycle is only assumed**

Expected: Label assumption/evidence needed, not a definite depletion date

## Method sources

Original file: 營業額提升主要關鍵（二）社群/會員經營技巧

Source locator: members

Source basis: extracted from course materials

Original URL: https://docs.google.com/presentation/d/1ZYpstuVAXGk9KdZt1QZm2OQ7ozpYYtfrBf0Xsy7kRx8/edit

English translation of source excerpt retained in the master sheet:

> Social / member management and mobile marketing thinking
