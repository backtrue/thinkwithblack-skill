---
name: mk-070
description: "Additional volume required after a price cut. Use when the task requires extra sales volume needed to maintain contribution. Apply this method to the specified inputs and verify the deliverable"
---

# MK-070 | Additional volume required after a price cut

For a regular chat, upload `packs/mk-070.md`. It includes the shared rules, this method, and required references

## Purpose

This skill delivers: **Extra sales volume needed to maintain contribution**

Recalculability does not mean the data is complete; break-even points and cost ceilings apply only under the stated assumptions

## Required inputs

Provide: Original order count and original/new contribution per order, or their prices and costs; corresponding conversion rates only when traffic is to be derived

For method questions, provide the formula, variables and an example directly; for a calculation, ask only for missing operands

## Method

1. A price cut directly lowers average order value, so recalculate the contribution margin ratio and break-even requirements using the new price first
2. Then work backward to the extra traffic/conversions needed to maintain or increase revenue. An experience-based course example says a 20% discount may require approximately 40% more traffic; this is an example, not a fixed formula
3. If average order value falls without sufficient additional traffic or conversions, the price-cut business model does not hold. A 25% contribution margin ratio is the course's floor benchmark

## Calculations and interpretation

Orders required to maintain original contribution = original orders × original contribution per order / new contribution per order, rounded up for whole orders. Apply this requirement only when new contribution is positive. With zero or negative new contribution, more such orders cannot recover an originally positive contribution; do not report negative orders or a finite break-even volume. If original total contribution is also nonpositive, show both results and confirm the target

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

**MK-070-A1 | Original 100 orders at contribution 20, new contribution 10**

Expected: Requires 200 orders

**MK-070-A2 | New contribution zero or −5**

Expected: Cannot recover original positive contribution through more such orders; no finite positive or negative order requirement

## Method sources

Source file: 營業額提升主要關鍵（三）從數據來提升 ROI 的策略

Location: Price reduction

Source basis: extracted from course materials

Source URL: https://docs.google.com/presentation/d/1lwpCxF1cMgaK7Gnvngw8NzytDLYD8MK-p91g8dwSytU/edit

English translation of source excerpt:

> Reduce prices to achieve a large increase in sales volume
