---
name: mk-398
description: "Member Campaign Repeat Purchase Review. Use when work requires repeat purchase results and confounding factors for the same group; process the specified inputs using this method and verify the deliverable"
---

# MK-398 | Member Campaign Repeat Purchase Review

For ordinary chat, upload `packs/mk-398.md`, which includes the shared rules, this method, and required references

## Purpose

This skill delivers: **Repeat purchase results and confounding factors for the same group**

Customer segmentation and actual eligibility to receive marketing messages are separate matters

## Required inputs


Available raw records: the original eligible-list snapshot, campaign objective and horizon, delivery records, linked orders/refunds, and campaign costs

## Method Steps

1. Freeze the initial deidentified eligible list, segment, objective, and observation window. Store actual deliveries/contacts and later orders separately; later segment moves do not change the original denominator
2. Count the original list, contact-eligible list, delivered list, and buyers separately. Label every denominator; moving to another membership tier does not remove an outcome from this campaign
3. Judge reuse against the original KPI and net contribution. Meeting the objective at acceptable cost supports reuse. Eligibility or delivery failure calls for list/delivery repair; delivered messages without a relevant need call for a different task or stopping the offer
4. Estimate incremental impact only with a comparable control. Otherwise report observed cohort outcomes without crediting all natural repeat purchases to the campaign. Request the original list snapshot rather than substituting today's segment size
5. Replace recommendations after refunds, recovered orders, or deduplication change KPIs or cost. Build the next campaign's list from new states without rewriting this history

## Calculation and Interpretation

Original-cohort repeat rate = original members with valid repeat purchases / original members. A delivered-recipient rate uses a separate delivered denominator. Deduct benefit, fulfillment, messaging, and campaign costs without deducting discounts already in net revenue twice; deduplicate cross-channel orders

Check example (hypothetical): 20 of 100 original members buy again and move tiers; the rate remains 20/100 = 20%, not 20/80 = 25%. Five full refunds with no other valid repeat order change it to 15%; reassess against the original objective

Decision rules authored by ThinkWithBlack, 2026-10-14; original course sources remain below

## Required output fields

| Order | Field | How to fill it in |
|---:|---|---|
| 1 | Original hypothesis / task | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 2 | Baseline | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 3 | Actual action | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 4 | Subsequent evidence | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 5 | Interpretation | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 6 | Confounding factors | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 7 | Version / replacement | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 8 | Next round | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |

## Validation cases

**MK-398-C05｜Approved but not actually executed**

Expected: keep the task pending execution; do not evaluate before-and-after effects

## Method sources

Original file: 營業額提升主要關鍵（二）社群/會員經營技巧

Source locator: members

Source basis: extracted from course materials

Original URL: https://docs.google.com/presentation/d/1ZYpstuVAXGk9KdZt1QZm2OQ7ozpYYtfrBf0Xsy7kRx8/edit

English translation of source excerpt retained in the master sheet:

> Social / member management and mobile marketing thinking
