---
name: mk-409
description: "Friend Quality Tracking. Use when work requires comparisons of interaction, first purchases, repeat purchases, and blocks; process the specified inputs using this method and verify the deliverable"
---

# MK-409 | Friend Quality Tracking

For ordinary chat, upload `packs/mk-409.md`, which includes the shared rules, this method, and required references

## Purpose

This skill delivers: **Comparisons of interaction, first purchases, repeat purchases, and blocks**

Do not send messages or create automation without approval; if a tool cannot show recipient eligibility, do not assume everyone can be messaged

## Required inputs


Available raw records: original acquisition cohorts and sources, costs, contact/block status, linked orders/refunds, and equal observation horizons

## Method Steps

1. Freeze all original contacts by source and join date, linking acquisition cost, contact/block status, and valid orders. Compare equal observation horizons and retain nonbuyers
2. Check whether the source supplies the intended audience and serviceable need, then compare first purchase, repeat purchase, retention, and contribution per original contact. Engagement describes response or demand clues, not sales or economics
3. A low CPF with worse contribution after acquisition cost is not high quality. A more expensive source meeting the recovery objective with serviceable contacts supports reuse, subject to the cost of acquiring additional contacts
4. Mark cohorts not yet reaching their purchase cycle as immature rather than rejecting them. Without source/order joins, report confirmed joins and cost and request the mapping needed for contribution
5. Recalculate after refunds, omitted nonbuyers, expired incentives, or block updates. Uncontactable people remain in historical cost denominators; report the future usable list separately rather than improving quality by deleting people

## Calculation and Interpretation

CPF = source acquisition cost / original new contacts. Net contribution per contact = cohort net order revenue less product, fulfillment, operating, and acquisition costs / original contacts. Other objectives require their own qualified-outcome definition and cost; do not mix objectives in one ranking

Check example (hypothetical): A and B each acquire 100 contacts. A costs 1,000 and contributes 500 before acquisition; B costs 2,000 and contributes 3,000. Net values are −5 and +10 per person, favoring B. Refunds reducing B's pre-acquisition contribution to 1,000 withdraw the positive-value reuse candidate

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

**MK-409-C05｜Approved but not actually executed**

Expected: keep the task pending execution; do not evaluate before-and-after effects

## Method sources

Original file: 行銷策略實戰學程 Day5｜Google Ads × LINE｜線上課程用投影片

Source locator: LINE

Source basis: extracted from course materials

Original URL: https://docs.google.com/presentation/d/1RK8wiunlvJrRxgFuTcGhO5B5fRa4fbEogpZTJpF6YKc/edit

English translation of source excerpt retained in the master sheet:

> Google Ads × LINE
