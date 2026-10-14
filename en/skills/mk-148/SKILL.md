---
name: mk-148
description: "Purchase Concern Classification. Use when you need concerns about price, trust, use, and delivery; apply this method to the specified inputs and verify the deliverable"
---

# MK-148｜Purchase Concern Classification

For a regular chat, upload `packs/mk-148.md`; it includes the shared rules, this method, and required references

## Purpose

This Skill delivers: **Concerns about price, trust, use, and delivery**

Keep review excerpts faithful; a recommendation, collaboration plan, or reuse arrangement does not mean the other party has been contacted

## Required Inputs


Available raw records: verbatim support exchanges, the associated SKU and page, timestamps, behavior, and actual offer or fulfillment terms

## Method Steps

1. Collect verbatim support remarks with SKU, page at the time, timestamp, and behavior. One person may have several concerns; retain the actual words and stage
2. Price concerns need explicit rejection or comparison of total price or alternatives. Trust concerns concern authenticity, safety, evidence, or support; usage concerns concern size, compatibility, or operation; delivery concerns concern dates, region, or fees
3. Match the answer to the concern: disclose total price, supply genuine evidence, explain fit, or state fulfillable delivery. If a required size is unavailable or payment cannot complete, resolve that supply or technical obstruction first
4. Browse or cart events alone leave the concern unsupported by remarks. Inspect one support exchange or interaction record from that stage to distinguish causes rather than assigning a psychological label to the whole event group
5. Reclassify after a clarification or verified failure. Retain the original evidence, but change the next message to the currently actionable issue

## Calculation and Interpretation

For each case, deliver the remark, supported classification, unsupported inference, matching action, and withdrawal condition. Count unique customers or cases; multiple labels may sum to more than the number of cases

Check example (hypothetical): “Too expensive; the other store delivers tomorrow” supports tentative price and timing concerns. Context shows the product is needed tomorrow at any acceptable quoted price; prioritize next-day fulfillment rather than sending a coupon

Decision rules authored by ThinkWithBlack, 2026-10-14; original course sources remain below

## Required Output Fields

| Order | Field | How to fill it |
|---:|---|---|
| 1 | Unit of analysis | Original evidence, intermediate method result, or explicitly unknown; do not fabricate |
| 2 | Original clues | Original evidence, intermediate method result, or explicitly unknown; do not fabricate |
| 3 | Category definitions | Original evidence, intermediate method result, or explicitly unknown; do not fabricate |
| 4 | Classification result | Original evidence, intermediate method result, or explicitly unknown; do not fabricate |
| 5 | Supporting / counterevidence | Original evidence, intermediate method result, or explicitly unknown; do not fabricate |
| 6 | Unknowns | Original evidence, intermediate method result, or explicitly unknown; do not fabricate |
| 7 | Downstream use | Original evidence, intermediate method result, or explicitly unknown; do not fabricate |

## Verification Cases

**MK-148-C05｜One record meets opposing conditions**

Expected: mark contradictory or pending judgment; do not arbitrarily assign the most common category

## Method Sources

Original file: Meta廣告學程 102 為什麼這些人不買

Source location: Testimonials

Source basis: Derived from course material

Original URL: https://docs.google.com/presentation/d/1VZM1BFp_CiefpdHFrSRKIDim5oOKHh52w6D5RUXi-Nc/edit

English translation of source excerpt retained in the master table:

> Creative B1: People who viewed but did not add to cart may simply not have bought (use limited-time/limited-quantity copy) or may distrust the brand (use third-party testimonial/review copy)
