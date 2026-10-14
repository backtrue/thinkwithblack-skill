---
name: mk-042
description: "Diagnosing an overly early call to action. Use when the task requires locations that request a purchase or inquiry too early. Apply this method to the specified inputs and verify the deliverable"
---

# MK-042 | Diagnosing an overly early call to action

For a regular chat, upload `packs/mk-042.md`. It includes the shared rules, this method, and required references

## Purpose

This skill delivers: **Locations that request a purchase or inquiry too early**

Task stages are analytical categories, not a claim that every customer follows the same path

## Required inputs


Available raw records: the visitor question, entry page, CTA wording, interaction journey, and actual checkout or form results

## Method Steps

1. Link the visitor's question, entry page, CTA promise, and result after clicking. Diagnose the current task rather than treating informational or transactional wording as a permanent stage
2. Add an answer required before acting, such as installation eligibility or size compatibility, while keeping a purchase route for ready buyers. Keep direct checkout when specifications are already resolved
3. If the CTA is understood and desired but the button, form, or payment fails, repair the flow. If remarks connect rejection to total price or delivery, examine those terms instead of adding educational pages
4. Low conversion alone leaves the cause unresolved. Inspect one actual CTA journey and its page content rather than asking the customer to diagnose intent mismatch
5. Withdraw a diagnosis contradicted by new behavior or remarks. If added information leaves a payment obstruction, move to payment repair instead of adding more articles

## Calculation and Interpretation

In the destination-task and next-step fields, identify missing answer, ready to act, interaction failure, or unacceptable terms, with its location. Any rate must use observable visitors on that same path

Check example (hypothetical): a visitor asks about outdoor use, but the page demands purchase without answering; add supported weather-resistance conditions. A recording later shows the answer was read and the purchase button failed; repair the button and withdraw the premature-CTA diagnosis

Decision rules authored by ThinkWithBlack, 2026-10-14; original course sources remain below

## Required output fields

| Order | Field | How to complete |
|---:|---|---|
| 1 | Object/location | Use source evidence, an intermediate method result, or an explicit unknown; do not invent information |
| 2 | Conditions for adoption | Use source evidence, an intermediate method result, or an explicit unknown; do not invent information |
| 3 | Actual evidence | Use source evidence, an intermediate method result, or an explicit unknown; do not invent information |
| 4 | Check status | Use source evidence, an intermediate method result, or an explicit unknown; do not invent information |
| 5 | Difference/candidate cause | Use source evidence, an intermediate method result, or an explicit unknown; do not invent information |
| 6 | Next task | Use source evidence, an intermediate method result, or an explicit unknown; do not invent information |
| 7 | Limitations | Use source evidence, an intermediate method result, or an explicit unknown; do not invent information |

## Verification cases

**MK-042-C05 | The data meets the existing conditions**

Expected: Report usable or maintain; do not manufacture a need for changes

**MK-042-C06 | The tool returns an error**

Expected: Report that the data was not obtained; do not classify it as a business anomaly

## Method sources

Source file: Google Ads 第一堂｜看懂需求，才知道廣告怎麼接

Location: Jumping ahead too quickly

Source basis: extracted from course materials

Source URL: https://docs.google.com/presentation/d/15ZOg0pX_xikpdA3FwGEoCSVgWortvCnxSe4hz4ugizg/edit

English translation of source excerpt:

> The instructor demonstrates a small-company attendance system in full, then deliberately checks whether "book a demo" jumps too far ahead
