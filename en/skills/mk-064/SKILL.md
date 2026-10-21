---
name: mk-064
description: "Customer acquisition cost ceiling calculation. Use when the task requires an estimate based on average order value, gross margin, and the affordable allocation. Apply this method to the specified inputs and verify the deliverable"
---

# MK-064 | Customer acquisition cost ceiling calculation

For a regular chat, upload `packs/mk-064.md`. It includes the shared rules, this method, and required references

## Purpose

This skill delivers: **An estimate based on average order value, gross margin, and the affordable allocation**

Recalculability does not mean the data is complete; break-even points and cost ceilings apply only under the stated assumptions

## Required inputs

Raw inputs: specified Target CPA and valid-order definition; an approved simplified estimate requires average order value, gross-margin rate, ad-allocation fraction and covered cost items with period/currency

## Method

1. Use the case-specified Target CPA with source, cost scope and valid-order definition. Otherwise find approved estimating assumptions; 30% is a teaching example, not a default
2. For an approved simplified estimate, Target CPA equals average order value times gross-margin rate times acceptable ad-allocation fraction. Revenue target divided by average order value is target order volume, not part of per-order CPA
3. Identify costs already deducted in the margin and the portion being allocated, counting ad costs once. Product margin alone gives a partial estimate with actual missing costs; full affordability needs the approved profit calculation rather than treating margin as net profit
4. Check nonnegative amounts, fractions from 0 to 1 and consistent definitions; repair invalid input. Zero/negative available contribution provides no positive ad allowance rather than a profitable zero-cost recommendation. Retain an explicitly approved zero Target CPA as the stated goal
5. Deliver inputs, units, source, substitution and result. Recompute with changed order value, costs or approved allocation. New-customer CAC uses its own customer count and specified expenses, not a renamed order CPA

## Calculations and interpretation

Hypothetical approved estimate: average order value 1,200, margin 60% and allocation 30% give Target CPA = 1,200 × 0.60 × 0.30 = 216 per valid order. An approved 20% allocation gives 144. Without a fraction, report order margin 720 and an unset allocation rather than filling 30%

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

**MK-064-A1 | Explicit approved Target CPA=0**

Expected: Retain the stated target; no denominator-zero rejection

**MK-064-A2 | Only AOV1200 and margin60%, no allocation ratio**

Expected: Retain margin720 and the missing ratio, without defaulting to30%

## Method sources

Source file: Meta廣告學程 104 廣告的數據決策

Location: CPA

Source basis: extracted from course materials

Source URL: https://docs.google.com/presentation/d/16FiqnSxBs-gSDxsxUBNhWdUX5vZrIWoZPGangj_f_Pk/edit

English translation of source excerpt:

> Reasonable CPA
