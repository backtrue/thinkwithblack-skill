---
name: mk-372
description: "Member Order Data Organization. Use when work requires correct relationships between customers with multiple orders and order details; process the specified inputs using this method and verify the deliverable"
---

# MK-372 | Member Order Data Organization

For ordinary chat, upload `packs/mk-372.md`, which includes the shared rules, this method, and required references

## Purpose

This skill delivers: **Correct relationships between customers with multiple orders and order details**

Do not rank RFM results from different observation periods as if they shared one basis; separately verify the purpose and authorization for any list export or use

## Required inputs

Provide: de-identified customer, order, date, amount, and refund data

## Method steps

1. Use stable deidentified customer keys, unique order keys, valid dates, amounts/statuses; identify order-level versus item-level input
2. Build one row per customer/order key, preserving item keys and their order relationship separately; count repeated order totals once and aggregate item amounts according to their definition
3. Flag missing keys, conflicting totals or customer ownership rather than merging by guesswork; use the cleaned valid-order table for RFM

## Calculation and interpretation

First define members, valid orders, refunds, and the period; calculate frequency using orders rather than item rows

## Required output fields

| Order | Field | How to fill it in |
|---:|---|---|
| 1 | Customer key | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 2 | Observation coverage | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 3 | Last valid purchase | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 4 | R | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 5 | F | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 6 | M | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 7 | Applied segmentation rules | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 8 | Segment | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 9 | Limitations | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |

## Verification cases

**MK-372-A1 | One order, two item rows each repeating total 100**

Expected: Order table total remains 100; preserve the two item relationships

## Method sources

Original file: 營業額提升主要關鍵（二）社群/會員經營技巧

Source locator: RFM

Source basis: extracted from course materials

Original URL: https://docs.google.com/presentation/d/1ZYpstuVAXGk9KdZt1QZm2OQ7ozpYYtfrBf0Xsy7kRx8/edit

English translation of source excerpt retained in the master sheet:

> Use RFM rules for segmentation to turn new customers (one purchase) into returning customers (more than one purchase)
