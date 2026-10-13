---
name: mk-385
description: "Member Status Transition Analysis. Use when work requires changes in groups between periods; process the specified inputs using this method and verify the deliverable"
---

# MK-385 | Member Status Transition Analysis

For ordinary chat, upload `packs/mk-385.md`, which includes the shared rules, this method, and required references

## Purpose

This skill delivers: **Changes in groups between periods**

Do not rank RFM results from different observation periods as if they shared one basis; separately verify the purpose and authorization for any list export or use

## Required inputs

Provide: de-identified customer, order, date, amount, and refund data

## Method steps

1. CRM is dynamic; new purchases and each campaign can move members into different customer tiers
2. Retrieve current lists and recalculate segments every month to observe member movement
3. Set separate KPIs for each CRM campaign to observe goal attainment and member movement
4. The original course materials do not define a full state-transition probability model; track actual segment changes without estimating transition rates yourself

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
