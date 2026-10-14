---
name: mk-174
description: "Diagnose Cart Adds Without Purchase. Use when you need items to investigate around price, shipping, payment, and trust; apply this method to the specified inputs and verify the deliverable"
---

# MK-174｜Diagnose Cart Adds Without Purchase

For a regular chat, upload `packs/mk-174.md`; it includes the shared rules, this method, and required references

## Purpose

This Skill delivers: **Items to investigate around price, shipping, payment, and trust**

Event groups do not necessarily represent the same people dropping off at each stage; verify counting and attribution across data sources

## Required Inputs


Available raw records: cart/order keys, products, quoted shipping, failed checkout steps, payment outcomes, and customer remarks

## Method Steps

1. Join product, fee disclosure, checkout steps, payment outcome, and customer remarks by the same cart or order key. Remove paid orders, duplicate events, and cases still within their normal payment waiting period
2. If a required step prevents completion, such as a broken payment button or address submission, propose repairing and replaying that step. A discount does not resolve that obstruction in these records
3. Treat fees as a candidate cause for the affected group only when checkout works and customers explicitly reject a newly disclosed cost. Compare earlier total-price disclosure, existing shipping offers, or real bundles rather than automatically proposing sitewide free shipping
4. Match stated payment-security or delivery concerns to payment explanations or feasible delivery terms. With cart events alone, identify the unresolved checkout stage and request one failed checkout record with its payment outcome; diagnose it from the raw record
5. A newly found successful payment removes that order from the nonbuyer group and changes the task to tracking reconciliation. If customers still reject fees after a repair, move to comparing fee offers

## Calculation and Interpretation

Abandoned carts = valid carts whose observation window has elapsed minus paid carts within that group. Without a join, report separate event counts rather than a person-level dropout rate. In the barrier and next-message fields, record the matched step, action, and new record that would invalidate the action

Check example (hypothetical): a checkout reports a card-verification error, so repair payment. A later successful-payment record changes the action to investigating a missing event and excluding the buyer from nonbuyer messaging, even though shipping was also charged

Decision rules authored by ThinkWithBlack, 2026-10-14; original course sources remain below

## Required Output Fields

| Order | Field | How to fill it |
|---:|---|---|
| 1 | Behavioral conditions | Original evidence, intermediate method result, or explicitly unknown; do not fabricate |
| 2 | Period | Original evidence, intermediate method result, or explicitly unknown; do not fabricate |
| 3 | Exclusions | Original evidence, intermediate method result, or explicitly unknown; do not fabricate |
| 4 | Known behavior | Original evidence, intermediate method result, or explicitly unknown; do not fabricate |
| 5 | Barriers to validate | Original evidence, intermediate method result, or explicitly unknown; do not fabricate |
| 6 | Next-stage message | Original evidence, intermediate method result, or explicitly unknown; do not fabricate |
| 7 | Evidence | Original evidence, intermediate method result, or explicitly unknown; do not fabricate |
| 8 | Execution status | Original evidence, intermediate method result, or explicitly unknown; do not fabricate |

## Method Sources

Original file: Meta廣告學程 102 為什麼這些人不買

Source location: Shopping cart

Source basis: Derived from course material

Original URL: https://docs.google.com/presentation/d/1VZM1BFp_CiefpdHFrSRKIDim5oOKHh52w6D5RUXi-Nc/edit

English translation of source excerpt retained in the master table:

> Cart abandonment rate
