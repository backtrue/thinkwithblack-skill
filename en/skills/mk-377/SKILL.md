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

Provide: de-identified customer, order, date, amount, and refund data

## Method steps

1. To assess spending capacity per purchase, use AVERAGE to calculate each member's average order amount
2. Do not conflate average order value with cumulative spending as one M measure; the course materials assign these calculations different purposes
3. Average order value can inform subsequent M tiers and pricing for campaign bundles

## Calculation and interpretation

First define members, valid orders, refunds, and the period; calculate frequency using orders rather than item rows

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

## Validation cases

**MK-377-C05｜The original specification gives no segment weights or cost ratios**

Expected: list the necessary decisions; do not invent “industry-standard” values

## Method sources

Original file: 營業額提升主要關鍵（二）社群/會員經營技巧

Source locator: RFM

Source basis: extracted from course materials

Original URL: https://docs.google.com/presentation/d/1ZYpstuVAXGk9KdZt1QZm2OQ7ozpYYtfrBf0Xsy7kRx8/edit

English translation of source excerpt retained in the master sheet:

> Use RFM rules for segmentation to turn new customers (one purchase) into returning customers (more than one purchase)
