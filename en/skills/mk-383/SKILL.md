---
name: mk-383
description: "Days to First Repeat Purchase Calculation. Use when work requires the interval between the first and second valid purchases; process the specified inputs using this method and verify the deliverable"
---

# MK-383 | Days to First Repeat Purchase Calculation

For ordinary chat, upload `packs/mk-383.md`, which includes the shared rules, this method, and required references

## Purpose

This skill delivers: **The interval between the first and second valid purchases**

Do not rank RFM results from different observation periods as if they shared one basis; separately verify the purpose and authorization for any list export or use

## Required inputs

Provide: de-identified customer, order, date, amount, and refund data

## Method steps

1. First filter members with 2 purchases
2. Calculate the days between each member's first and second purchases
3. Calculate the average of these intervals as the baseline for days to first repeat purchase
4. The course materials' Check is to keep reducing days to first repeat purchase; do not assign an arbitrary interval to people without a second purchase

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

**MK-383-C05｜The original specification gives no segment weights or cost ratios**

Expected: list the necessary decisions; do not invent “industry-standard” values

## Method sources

Original file: 營業額提升主要關鍵（二）社群/會員經營技巧

Source locator: RFM

Source basis: extracted from course materials

Original URL: https://docs.google.com/presentation/d/1ZYpstuVAXGk9KdZt1QZm2OQ7ozpYYtfrBf0Xsy7kRx8/edit

English translation of source excerpt retained in the master sheet:

> Use RFM rules for segmentation to turn new customers (one purchase) into returning customers (more than one purchase)
