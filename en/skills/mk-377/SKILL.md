---
name: mk-377
description: "Member Average Order Value Calculation. Use when work requires average order value compared with amount and frequency; process the specified inputs using this method and verify the deliverable"
---

# MK-377 | Member Average Order Value Calculation

For ordinary chat, upload `packs/mk-377.md`, which includes the shared rules, this method, and required references

## Purpose

This skill delivers: **Average order value compared with amount and frequency**

Do not rank RFM results from different observation periods as if they shared one basis; separately verify the purpose and authorization for any list export or use

## Required inputs

Deidentified customer/order/item keys, revenue-field definition, refund/cancellation rules, observation window and currency

## Method steps

1. Create one net-amount row per valid order, counting repeated order totals once and applying agreed refunds
2. Customer AOV = total valid-order net revenue / distinct valid orders, not AVERAGE of raw item rows
3. Show total, count and average separately; zero orders means undefined average, and missing data differs from confirmed zero transactions

## Calculation and interpretation

Deduplicate repeated order totals; if only item amounts exist, aggregate by order first. Do not mix these representations

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

**MK-377-A1 | Order A total 100 repeated twice, B total 300 once**

Expected: Two-order AOV 200, not row average 166.67

## Method sources

Original file: 營業額提升主要關鍵（二）社群/會員經營技巧

Source locator: RFM

Source basis: extracted from course materials

Original URL: https://docs.google.com/presentation/d/1ZYpstuVAXGk9KdZt1QZm2OQ7ozpYYtfrBf0Xsy7kRx8/edit

English translation of source excerpt retained in the master sheet:

> Use RFM rules for segmentation to turn new customers (one purchase) into returning customers (more than one purchase)
