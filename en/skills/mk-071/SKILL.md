---
name: mk-071
description: "Average order value and conversion-rate sensitivity analysis. Use when the task requires revenue and profit changes under different assumptions. Apply this method to the specified inputs and verify the deliverable"
---

# MK-071 | Average order value and conversion-rate sensitivity analysis

For a regular chat, upload `packs/mk-071.md`. It includes the shared rules, this method, and required references

## Purpose

This skill delivers: **Revenue and profit changes under different assumptions**

Working backward to resource requirements is not a forecast or optimal allocation; do not decide actual spending without an affordable ceiling

## Required inputs


Available raw records: same-period revenue, orders, traffic denominator, average order value, costs, target, capacity, and proposed actions

## Method Steps

1. Align revenue, valid orders, traffic denominator, and average order value in one period, then rebuild the baseline. A visit-based denominator needs a visit-based order rate, not a user conversion rate from another report
2. Solve each lever's required value while holding others fixed, then attach actual actions, costs, preparation time, supply, and evidence for the assumed change. The smallest algebraic change is not necessarily the easiest action
3. Exclude scenarios exceeding fulfillment, supported conversion ranges, or preparation deadlines. For equal target outcomes, prefer the option with lower cost and shorter time if the other has no known compensating benefit
4. Compare contribution and feasibility against the user's objective without invented weights. If one missing cost determines a trade-off, request that cost while delivering the known calculations and eliminated options
5. Recalculate linked variables when an offer reduces contribution or a larger basket reduces conversion. Replace the original preferred lever when new conditions invalidate it

## Calculation and Interpretation

Revenue R = traffic T × order rate C × average order value A. Required C = target R / (T × A), with analogous solutions for other variables; do not solve with a zero denominator. Contribution = orders × net revenue less variable costs per order − additional acquisition and implementation costs, compared with fixed costs or the objective

Check example (hypothetical): 1,000 visits × 2% × 1,000 = 20,000. Reaching 30,000 could use a 1,500 basket scenario. If the bundle reduces conversion to 1%, revenue becomes 15,000; withdraw the recommendation that a larger basket alone reaches the target

Decision rules authored by ThinkWithBlack, 2026-10-14; original course sources remain below

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

**MK-071-C05 | A required denominator is zero**

Expected: Report that the formula is undefined; do not output a zero cost or an infinite target

**MK-071-C06 | Only some costs are supplied**

Expected: Retain the partial result and excluded items; do not call it complete profitability

## Method sources

Source file: 行銷策略實戰學程Day2-以終為始x降低成本x提升指標

Location: Costs

Source basis: extracted from course materials

Source URL: https://docs.google.com/presentation/d/1NdxlcqAKMPHqGVS5jbjSYR_UgOJSA0fS65OnTtQLEHQ/edit

English translation of source excerpt:

> Begin with the end in mind x reduce costs x improve metrics
