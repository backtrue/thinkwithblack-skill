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


Available raw records: valid orders, observation coverage, product cycles, order-value distributions, approved rules, and intended group actions

## Method Steps

1. Read existing brand segmentation rules, valid-order/refund definitions, observation dates, and each member's observable start. Apply approved thresholds first and flag unsuitable data separately rather than silently changing policy
2. Without thresholds, calculate raw R, F, and M before proposing boundaries tied to product cycles and list actions. Candidate R boundaries come from observed purchase intervals or known usage cycles. Separate short-history and long-cycle products; an uncompleted interval at the data cutoff is not infinite
3. Compare F across equal observable tenure. Members without a second-purchase opportunity remain not yet assessable. M uses valid net order value; expensive benefits additionally require contribution and benefit costs, not high revenue alone
4. Connect every candidate group to an action such as due replenishment, overdue investigation, or loyalty care. Merge groups receiving the same action; do not impose quintiles or invented score weights without a task
5. Inspect records on both sides of boundaries, specify inclusive/exclusive endpoints, and assign each member exactly once. Recalculate after cycle, refund, or window changes. Without a cycle, deliver distributions and unresolved products rather than asking the user to identify sleepers

## Calculation and Interpretation

R = reference date minus last valid purchase date; F = distinct valid orders in the window; M = net value of valid orders in the window. Course cycle multiples and basket distributions are candidate inputs. Separate proposed thresholds from approved rules and list members whose actions change

Check example (hypothetical): a known 60-day cycle supports candidate rules R≤60 not overdue and R>60 investigate; R=61 triggers investigation. Correcting the purchase to a double quantity lasting 120 days changes it to not overdue and removes overdue-winback messaging

Decision rules authored by ThinkWithBlack, 2026-10-14; original course sources remain below

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
