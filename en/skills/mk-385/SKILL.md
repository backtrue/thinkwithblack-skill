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

Two deidentified member snapshots, reference dates/time zones, windows, RFM values/scores, segmentation rules/versions and data refresh times

## Method steps

1. Check windows/rule versions and mark rule or coverage changes separately
2. Match snapshots using stable keys, retaining new, out-of-scope and unmatched customers
3. Deliver previous/current segments and transitions, tied to new orders, refunds or elapsed time; rule changes are not customer improvement
4. Summarize previous×current counts when requested, showing denominators and match coverage

## Calculation and interpretation

First define members, valid orders, refunds, and the period; calculate frequency using orders rather than item rows

## Required output fields

| Order | Field | How to complete |
|---:|---|---|
| 1 | Deidentified customer key | Use the supplied source, calculation, or explicit unknown |
| 2 | Before/after reference dates and time zones | Use the supplied source, calculation, or explicit unknown |
| 3 | Before/after rule versions | Use the supplied source, calculation, or explicit unknown |
| 4 | Previous RFM and segment | Use the supplied source, calculation, or explicit unknown |
| 5 | Current RFM and segment | Use the supplied source, calculation, or explicit unknown |
| 6 | Segment transition | Use the supplied source, calculation, or explicit unknown |
| 7 | Data or rule-change explanation | Use the supplied source, calculation, or explicit unknown |
| 8 | Noncomparability and open issues | Use the supplied source, calculation, or explicit unknown |

## Verification cases

**MK-385-A1 | Orders unchanged, segmentation version changes**

Expected: Label a rule change, not customer improvement

## Method sources

Original file: 營業額提升主要關鍵（二）社群/會員經營技巧

Source locator: RFM

Source basis: extracted from course materials

Original URL: https://docs.google.com/presentation/d/1ZYpstuVAXGk9KdZt1QZm2OQ7ozpYYtfrBf0Xsy7kRx8/edit

English translation of source excerpt retained in the master sheet:

> Use RFM rules for segmentation to turn new customers (one purchase) into returning customers (more than one purchase)
