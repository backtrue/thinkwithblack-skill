---
name: mk-066
description: "Working backward to target cost per add-to-cart. Use when the task requires cost derived from the add-to-cart purchase rate and CPA. Apply this method to the specified inputs and verify the deliverable"
---

# MK-066 | Working backward to target cost per add-to-cart

For a regular chat, upload `packs/mk-066.md`. It includes the shared rules, this method, and required references

## Purpose

This skill delivers: **Cost derived from the add-to-cart purchase rate and CPA**

Recalculability does not mean the data is complete; break-even points and cost ceilings apply only under the stated assumptions

## Required inputs

Raw inputs: per-valid-order Target CPA, matched add-to-carts A and resulting valid purchases P, event/person/order units, matching method, mature window and actual add-to-cart spend

## Method

1. Fix Target CPA and valid-order definition; specify whether cost concerns events, cart users or deduplicated cart flows. Match subsequent valid purchases to those carts rather than divide unrelated purchase and cart events
2. For a matched cohort/window, cart-to-purchase ratio is P/A. If the ratio counts people but Target CPA counts orders with multiple orders per person, obtain consistent order/flow units first. Unmatched or immature outcomes leave the usable ratio pending
3. With A positive and consistent units, target add-to-cart cost = Target CPA × P/A. Compare matched spend/A in the same unit. Values outside the defined feasible ratio require duplicate/unit checks rather than clamping to 100%
4. With A zero, the ratio is undefined. With A positive and P zero, observed ratio/formula value zero supports no positive cart allowance; retain actual spend and do not call purchase cost zero
5. Actual matched cart cost above target identifies cost/completion gaps. Use checkout/payment evidence to choose landing repair or acquisition changes. Recompute and withdraw obsolete judgments after purchases, refunds, matching or Target CPA changes

## Calculations and interpretation

Hypothetical check: Target CPA 216 with 100 deduplicated cart flows and 25 valid orders gives target cart cost 54. Confirming 50 mature orders changes it to 108. Retain ratio, currency and units with the calculation; this task delivers add-to-cart cost

Decision rules authored by ThinkWithBlack on 2026-10-14; original course sources are retained below

## Required output fields

| Order | Field | How to complete |
|---:|---|---|
| 1 | Input variable | Use source evidence, an intermediate method result, or an explicit unknown; do not invent information |
| 2 | Value | Use source evidence, an intermediate method result, or an explicit unknown; do not invent information |
| 3 | Unit and definition | Use source evidence, an intermediate method result, or an explicit unknown; do not invent information |
| 4 | Source | Use source evidence, an intermediate method result, or an explicit unknown; do not invent information |
| 5 | Formula | Use source evidence, an intermediate method result, or an explicit unknown; do not invent information |
| 6 | Result | Use source evidence, an intermediate method result, or an explicit unknown; do not invent information |
| 7 | Limitations | Use source evidence, an intermediate method result, or an explicit unknown; do not invent information |

## Verification cases

**MK-066-C05 | A required denominator is zero**

Expected: Report that the formula is undefined; do not output a zero cost or an infinite target

**MK-066-C06 | Only some costs are supplied**

Expected: Retain the partial result and excluded items; do not call it complete profitability

## Method sources

Source file: Meta廣告學程 104 廣告的數據決策

Location: Add to cart

Source basis: extracted from course materials

Source URL: https://docs.google.com/presentation/d/16FiqnSxBs-gSDxsxUBNhWdUX5vZrIWoZPGangj_f_Pk/edit

English translation of source excerpt:

> Today's add-to-cart completion rate = 30%, meaning an order requires 3.3 adds to cart. Completing an order costs 450, so each add to cart carries 450 / 3.3 = NT$136
