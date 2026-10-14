---
name: mk-384
description: "New, Existing, and Dormant Member Segmentation. Use when work requires NES groups with clear periods and statuses; process the specified inputs using this method and verify the deliverable"
---

# MK-384 | New, Existing, and Dormant Member Segmentation

For ordinary chat, upload `packs/mk-384.md`, which includes the shared rules, this method, and required references

## Purpose

This skill delivers: **NES groups with clear periods and statuses**

Do not rank RFM results from different observation periods as if they shared one basis; separately verify the purpose and authorization for any list export or use

## Required inputs


Available raw records: member/order keys, valid orders and refunds, first/last purchase, observable tenure, product cycles, and approved NES rules

## Method Steps

1. Organize valid orders, refunds, first/last purchase, observable start, and product cycle by deidentified member key. Preserve approved NES definitions and thresholds separately from this task's investigation labels
2. Keep never-buyers separate. One valid purchase supports a first-buyer stage; multiple purchases support an existing-buyer stage. Sleeping status depends separately on elapsed time and the applicable cycle; one purchase alone does not mean sleeping
3. Investigate overdue status only after an evidenced repurchase/service window with complete coverage. Separate not-yet-due from insufficient-history cases. Apply product-specific cycles instead of flattening different categories into a store average
4. Without brand thresholds, deliver raw classifications and proposed rules, checking supply, complaints, and later purchases before coupons. If an approved label conflicts with product timing, retain the official label and separately revise the proposed action
5. Update labels and next steps after new orders, refunds invalidating a first purchase, or completed history. Request the last valid purchase or product cycle rather than asking the user to classify the member

## Calculation and Interpretation

Count distinct valid orders. R = reference date minus last valid purchase; never-buyers do not receive R=0. For one NES field, specify how sleeping overrides new/existing, while retaining purchase stage and cycle status separately

Check example (hypothetical): one purchase 35 days ago with a normal 60-day cycle is first-buyer and not due. Changing elapsed time to 90 days with complete records makes it overdue for investigation, starting with the reason for no repeat purchase

Decision rules authored by ThinkWithBlack, 2026-10-14; original course sources remain below

## Required output fields

| Order | Field | How to fill it in |
|---:|---|---|
| 1 | Unit of analysis | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 2 | Original clues | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 3 | Category definitions | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 4 | Classification results | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 5 | Support / counterexamples | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 6 | Unknowns | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 7 | Downstream use | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |

## Validation cases

**MK-384-C05｜One record matches opposing conditions**

Expected: mark the data as contradictory or pending classification; do not arbitrarily assign the most common category

## Method sources

Original file: 營業額提升主要關鍵（二）社群/會員經營技巧

Source locator: RFM

Source basis: extracted from course materials

Original URL: https://docs.google.com/presentation/d/1ZYpstuVAXGk9KdZt1QZm2OQ7ozpYYtfrBf0Xsy7kRx8/edit

English translation of source excerpt retained in the master sheet:

> Use RFM rules for segmentation to turn new customers (one purchase) into returning customers (more than one purchase)
