---
name: mk-378
description: "RFM Threshold Setting. Use when work requires thresholds based on purchase cycles and distributions; process the specified inputs using this method and verify the deliverable"
---

# MK-378 | RFM Threshold Setting

For ordinary chat, upload `packs/mk-378.md`, which includes the shared rules, this method, and required references

## Purpose

This skill delivers: **Thresholds based on purchase cycles and distributions**

Do not rank RFM results from different observation periods as if they shared one basis; separately verify the purpose and authorization for any list export or use

## Required inputs

Provide: de-identified customer, order, date, amount, and refund data

## Method steps

1. Set R thresholds based on the average purchase cycle; the course materials suggest ranges of 1–2 times, 2–3 times, and more than 3 times the cycle
2. Set F thresholds according to data coverage and the average repeat purchase cycle; the course materials provide no fixed value across industries
3. M thresholds may reference the free-shipping threshold, average order value, TOP 50% order value, and TOP 10% order value, then be adjusted to marketing goals
4. If the brand has not provided its average purchase cycle, free-shipping threshold, or order-value distribution, list those gaps first; do not invent five equal segments

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
