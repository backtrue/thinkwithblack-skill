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

Provide: de-identified customer, order, date, amount, and refund data

## Method steps

1. Align Recency ranges with the average purchase cycle and use NES (New Customer, Existing Customer, Sleeping Customer) for the initial classification
2. The course materials suggest R ranges of 1–2 times, 2–3 times, and more than 3 times the purchase cycle
3. Do not determine dormancy solely from fixed 30 / 60 / 90-day cutoffs; first establish the brand's average purchase cycle

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
