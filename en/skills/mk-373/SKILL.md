---
name: mk-373
description: "Member Identifier Consistency Check. Use when work requires duplicate customers and unmatched items; process the specified inputs using this method and verify the deliverable"
---

# MK-373 | Member Identifier Consistency Check

For ordinary chat, upload `packs/mk-373.md`, which includes the shared rules, this method, and required references

## Purpose

This skill delivers: **Duplicate customers and unmatched items**

Do not rank RFM results from different observation periods as if they shared one basis; separately verify the purpose and authorization for any list export or use

## Required inputs

Deidentified customer/order keys and source systems, supplied approved key mappings, duplicate/unmatched records; raw emails or phone numbers are not required

## Method steps

1. Fix the deidentified customer key and check missing/duplicate keys and orders assigned to multiple customers
2. Merge only using confirmed source-system mappings; similar names or purchase behavior do not establish identity
3. Deliver original/mapped keys, merge evidence and unmatched records; preserve unmapped identities without requesting raw contact data

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

**MK-373-A1 | Two anonymized keys buy the same product, no mapping**

Expected: Keep separate and unresolved, without merging

## Method sources

Original file: 營業額提升主要關鍵（二）社群/會員經營技巧

Source locator: RFM

Source basis: extracted from course materials

Original URL: https://docs.google.com/presentation/d/1ZYpstuVAXGk9KdZt1QZm2OQ7ozpYYtfrBf0Xsy7kRx8/edit

English translation of source excerpt retained in the master sheet:

> Use RFM rules for segmentation to turn new customers (one purchase) into returning customers (more than one purchase)
