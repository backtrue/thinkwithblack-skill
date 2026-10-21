---
name: mk-381
description: "One-Time Purchaser Identification. Use when work requires F1 members and traceable sources; process the specified inputs using this method and verify the deliverable"
---

# MK-381 | One-Time Purchaser Identification

For ordinary chat, upload `packs/mk-381.md`, which includes the shared rules, this method, and required references

## Purpose

This skill delivers: **F1 members and traceable sources**

Do not rank RFM results from different observation periods as if they shared one basis; separately verify the purpose and authorization for any list export or use

## Required inputs

Deidentified customer key, unique order key, valid dates, cancellation/refund rules, history coverage and observation window

## Method steps

1. Fix history/window, apply valid-order rules and deduplicate by customer/order key before counting item rows
2. F = distinct valid order keys per customer; deliver F = 1, not COUNT of item rows
3. Retain order keys and period; partial history is not lifetime frequency

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

**MK-381-A1 | One purchase with three item rows**

Expected: Still F1

## Method sources

Original file: 營業額提升主要關鍵（二）社群/會員經營技巧

Source locator: RFM

Source basis: extracted from course materials

Original URL: https://docs.google.com/presentation/d/1ZYpstuVAXGk9KdZt1QZm2OQ7ozpYYtfrBf0Xsy7kRx8/edit

English translation of source excerpt retained in the master sheet:

> Use RFM rules for segmentation to turn new customers (one purchase) into returning customers (more than one purchase)
