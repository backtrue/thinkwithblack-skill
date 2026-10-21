---
name: mk-382
description: "Second-Purchase Member Identification. Use when work requires F2 attainment and member groups; process the specified inputs using this method and verify the deliverable"
---

# MK-382 | Second-Purchase Member Identification

For ordinary chat, upload `packs/mk-382.md`, which includes the shared rules, this method, and required references

## Purpose

This skill delivers: **F2 attainment and member groups**

Do not rank RFM results from different observation periods as if they shared one basis; separately verify the purpose and authorization for any list export or use

## Required inputs

Deidentified customer key, unique order key, valid dates, cancellation/refund rules, history coverage and observation window

## Method steps

1. Fix history/window, apply valid-order rules and deduplicate by customer/order key before counting item rows
2. F = distinct valid order keys per customer; deliver F = 2, not COUNT of item rows
3. Check first/second dates; F = 2 is not loyalty, and customers with three or more orders are outside this exact-two group

## Calculation and interpretation

First define members, valid orders, refunds, and the period; calculate frequency using orders rather than item rows

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

## Verification cases

**MK-382-A1 | Two orders with two rows each, no third order**

Expected: F = 2, not four; customers with a third order are not exact-two

## Method sources

Original file: 營業額提升主要關鍵（二）社群/會員經營技巧

Source locator: RFM

Source basis: extracted from course materials

Original URL: https://docs.google.com/presentation/d/1ZYpstuVAXGk9KdZt1QZm2OQ7ozpYYtfrBf0Xsy7kRx8/edit

English translation of source excerpt retained in the master sheet:

> Use RFM rules for segmentation to turn new customers (one purchase) into returning customers (more than one purchase)
