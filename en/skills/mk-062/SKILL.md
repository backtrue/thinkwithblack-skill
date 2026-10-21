---
name: mk-062
description: "Converting a revenue target into order volume. Use when the task requires orders required for the target revenue and average order value. Apply this method to the specified inputs and verify the deliverable"
---

# MK-062 | Converting a revenue target into order volume

For a regular chat, upload `packs/mk-062.md`. It includes the shared rules, this method, and required references

## Purpose

This skill delivers: **Orders required for the target revenue and average order value**

Working backward to resource requirements is not a forecast or optimal allocation; do not decide actual spending without an affordable ceiling

## Required inputs

Provide: Target or break-even revenue, comparable average order value and planning period

For method questions, provide the formula, variables and an example directly; for a calculation, ask only for missing operands

## Method

1. Break-even order volume = break-even revenue ÷ average order value
2. Use the same logic to divide target revenue by expected average order value and obtain the required order count
3. Use an average order value consistent with the target products/overall business in this task; avoid mixing new and existing customers

## Calculations and interpretation

Required orders = target revenue / comparable AOV, rounded up for whole orders. AOV must be positive; retain revenue scope, currency and period without adding margin/cost prerequisites

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

**MK-062-A1 | Target1000, AOV300**

Expected: Four whole orders required

**MK-062-A2 | AOV zero or unknown**

Expected: No finite order requirement; retain invalid/missing input

## Method sources

Source file: 行銷策略實戰學程Day2-以終為始x降低成本x提升指標

Location: Costs

Source basis: extracted from course materials

Source URL: https://docs.google.com/presentation/d/1NdxlcqAKMPHqGVS5jbjSYR_UgOJSA0fS65OnTtQLEHQ/edit

English translation of source excerpt:

> Begin with the end in mind x reduce costs x improve metrics
