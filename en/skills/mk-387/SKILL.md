---
name: mk-387
description: "Member Segmentation Completeness Check. Use when work requires checks for missing, overlapping, and incorrect segments; process the specified inputs using this method and verify the deliverable"
---

# MK-387 | Member Segmentation Completeness Check

For ordinary chat, upload `packs/mk-387.md`, which includes the shared rules, this method, and required references

## Purpose

This skill delivers: **Checks for missing, overlapping, and incorrect segments**

Do not rank RFM results from different observation periods as if they shared one basis; separately verify the purpose and authorization for any list export or use

## Required inputs

Valid source orders/deidentified keys, current RFM values/scores, same-version score bands/group mappings, window/reference date and list production date

## Method steps

1. Check whether every member has the order numbers, identifier, dates, and amounts needed to calculate R, F, and M
2. Check whether every RFM score maps to an established Total Score segment
3. Check whether monthly lists are current, avoiding this month's CRM execution based on old segments
4. The original course materials provide no additional completeness score; list missing fields and affected segments when data is missing, rather than inventing scores

## Calculation and interpretation

First define members, valid orders, refunds, and the period; calculate frequency using orders rather than item rows

## Required output fields

| Order | Field | How to fill it in |
|---:|---|---|
| 1 | Subject / location | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 2 | Conditions for use | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 3 | Actual evidence | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 4 | Check status | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 5 | Differences / possible causes | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 6 | Next task | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 7 | Limitations | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |

## Verification cases

**MK-387-A1 | Orders exist but mapping version missing**

Expected: Check data completeness while leaving segment mapping unverified

## Method sources

Original file: 營業額提升主要關鍵（二）社群/會員經營技巧

Source locator: RFM

Source basis: extracted from course materials

Original URL: https://docs.google.com/presentation/d/1ZYpstuVAXGk9KdZt1QZm2OQ7ozpYYtfrBf0Xsy7kRx8/edit

English translation of source excerpt retained in the master sheet:

> Use RFM rules for segmentation to turn new customers (one purchase) into returning customers (more than one purchase)
