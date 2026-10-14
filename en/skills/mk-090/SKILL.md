---
name: mk-090
description: "Product-profitability prioritization. Use when the task requires a comparison of revenue, gross margin, and conversion performance. Apply this method to the specified inputs and verify the deliverable"
---

# MK-090 | Product-profitability prioritization

For a regular chat, upload `packs/mk-090.md`. It includes the shared rules, this method, and required references

## Purpose

This skill delivers: **A comparison of revenue, gross margin, and conversion performance**

Products occurring in the same transaction do not establish psychological motives; a product pairing does not automatically prove cross-selling effectiveness

## Required inputs


Available raw records: same-period product revenue, view and purchase units, costs, available inventory, and the investment objective

## Method Steps

1. Align SKU, period, refund treatment, margin, and view/purchase counting units. Item purchases divided by item views can calculate the course metric but is not a visitor conversion probability
2. Calculate the course index for historical candidate ranking, then inspect inventory, fulfillment, actual buyer jobs, and acquisition costs. An unavailable high-index item is not a current lead product
3. For the same task, compare supported additional-volume scenarios times contribution per order minus added promotion costs. A lower-index product can take priority if its achievable total contribution is higher and meets the objective
4. If ranking depends on one large order or very few views, remove the influential record and recalculate; a reversal restricts it to a test candidate. Without added-demand evidence, deliver historical ranking and a bounded test rather than assuming doubled traffic doubles sales
5. Re-rank after refunds, costs, stock, or buyer-task changes. Request actual product and fulfillment costs for the candidate; price is not margin

## Calculation and Interpretation

Course item conversion rate = purchased items / viewed items. Profit index = item revenue × margin rate × item conversion rate; use decimal rates and do not divide by zero. Separately calculate supported additional orders × net revenue less variable costs per order − added promotion costs, without double-counting discounts

Check example (hypothetical): A has the higher historical index but no stock, so it is not the current lead. B's scenario of 20 units at 100 contribution minus 500 promotion cost yields 1,500. Capacity falling to three units yields −200 and withdraws that investment scenario

Decision rules authored by ThinkWithBlack, 2026-10-14; original course sources remain below

## Required output fields

| Order | Field | How to complete |
|---:|---|---|
| 1 | Product/role | Use source evidence, an intermediate method result, or an explicit unknown; do not invent information |
| 2 | Need clues | Use source evidence, an intermediate method result, or an explicit unknown; do not invent information |
| 3 | Sales and gross margin | Use source evidence, an intermediate method result, or an explicit unknown; do not invent information |
| 4 | Pairing or follow-on relationship | Use source evidence, an intermediate method result, or an explicit unknown; do not invent information |
| 5 | Supply constraints | Use source evidence, an intermediate method result, or an explicit unknown; do not invent information |
| 6 | Candidate approach | Use source evidence, an intermediate method result, or an explicit unknown; do not invent information |
| 7 | Reason | Use source evidence, an intermediate method result, or an explicit unknown; do not invent information |

## Method sources

Source file: 營業額提升主要關鍵（三）從數據來提升 ROI 的策略

Location: Earnings index

Source basis: extracted from course materials

Source URL: https://docs.google.com/presentation/d/1lwpCxF1cMgaK7Gnvngw8NzytDLYD8MK-p91g8dwSytU/edit

English translation of source excerpt:

> Earnings index
