---
name: mk-063
description: "Converting an order target into traffic. Use when the task requires traffic required for the order target and conversion rate. Apply this method to the specified inputs and verify the deliverable"
---

# MK-063 | Converting an order target into traffic

For a regular chat, upload `packs/mk-063.md`. It includes the shared rules, this method, and required references

## Purpose

This skill delivers: **Traffic required for the order target and conversion rate**

Working backward to resource requirements is not a forecast or optimal allocation; do not decide actual spending without an affordable ceiling

## Required inputs

Provide: Required orders, comparable traffic-to-order conversion rate and number of planning days

For method questions, provide the formula, variables and an example directly; for a calculation, ask only for missing operands

## Method

1. Required traffic = required orders / comparable traffic-to-order conversion rate, which must be positive
2. Daily target = period traffic / actual planning or operating days D; retain D when unknown, rather than fixing 30
3. Check website, period and audience; label assumed conversion rates and scenario scope

## Calculations and interpretation

Required traffic = required orders / comparable conversion rate; daily traffic = required traffic / actual days D, rounded up for whole units. Conversion rate and D must be positive; preserve symbols and gaps for unknown values

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

**MK-063-A1 | 28 orders, 10% conversion, 14-day campaign**

Expected: Traffic 280, daily 20, not division by 30

## Method sources

Source file: 行銷策略實戰學程Day2-以終為始x降低成本x提升指標

Location: Costs

Source basis: extracted from course materials

Source URL: https://docs.google.com/presentation/d/1NdxlcqAKMPHqGVS5jbjSYR_UgOJSA0fS65OnTtQLEHQ/edit

English translation of source excerpt:

> Begin with the end in mind x reduce costs x improve metrics
