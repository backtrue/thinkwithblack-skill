---
name: mk-374
description: "Member Purchase Recency Calculation. Use when work requires time since the most recent purchase as of a specified reference date; process the specified inputs using this method and verify the deliverable"
---

# MK-374 | Member Purchase Recency Calculation

For ordinary chat, upload `packs/mk-374.md`, which includes the shared rules, this method, and required references

## Purpose

This skill delivers: **Time since the most recent purchase as of a specified reference date**

Do not rank RFM results from different observation periods as if they shared one basis; separately verify the purpose and authorization for any list export or use

## Required inputs

Deidentified customer keys, valid order keys/timestamps, order/refund rules, explicit reference date, time zone and day-count definition

## Method steps

1. Fix the reference date, time zone and day-count definition; select valid deduplicated orders up to that date
2. Take each customer’s latest valid purchase and calculate the interval to the reference date
3. R is undefined without a valid purchase; flag future orders, unknown time zones and gaps rather than silently using today

## Calculation and interpretation

R = specified reference date − latest valid purchase date, using the agreed calendar-day or elapsed-time definition in one time zone; without the date, deliver the formula and missing field

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

**MK-374-A1 | Reference Oct 21, latest purchase Oct 1, same-zone calendar days**

Expected: R = 20; absent reference date remains unknown, not execution date

## Method sources

Original file: 營業額提升主要關鍵（二）社群/會員經營技巧

Source locator: RFM

Source basis: extracted from course materials

Original URL: https://docs.google.com/presentation/d/1ZYpstuVAXGk9KdZt1QZm2OQ7ozpYYtfrBf0Xsy7kRx8/edit

English translation of source excerpt retained in the master sheet:

> Use RFM rules for segmentation to turn new customers (one purchase) into returning customers (more than one purchase)
