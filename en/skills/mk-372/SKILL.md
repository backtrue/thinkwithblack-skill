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

1. First organize order data with these required fields: order number, email or phone number, order date, and order total
2. Use email or phone as pivot-table rows so each member's orders can be aggregated into one row
3. Calculate R, F, and M from this organized order table; do not replace original orders with subjective member labels

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

## Method sources

Original file: 營業額提升主要關鍵（二）社群/會員經營技巧

Source locator: RFM

Source basis: extracted from course materials

Original URL: https://docs.google.com/presentation/d/1ZYpstuVAXGk9KdZt1QZm2OQ7ozpYYtfrBf0Xsy7kRx8/edit

English translation of source excerpt retained in the master sheet:

> Use RFM rules for segmentation to turn new customers (one purchase) into returning customers (more than one purchase)
