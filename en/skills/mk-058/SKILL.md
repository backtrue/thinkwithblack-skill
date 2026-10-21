---
name: mk-058
description: "Classifying fixed and variable costs. Use when the task requires a comparison of fixed expenses and per-order variable expenses. Apply this method to the specified inputs and verify the deliverable"
---

# MK-058 | Classifying fixed and variable costs

For a regular chat, upload `packs/mk-058.md`. It includes the shared rules, this method, and required references

## Purpose

This skill delivers: **A comparison of fixed expenses and per-order variable expenses**

Recalculability does not mean the data is complete; break-even points and cost ceilings apply only under the stated assumptions

## Required inputs

Cost items, amounts, period and charging basis; for method questions, provide classification principles and examples directly

## Method

1. Fixed costs occur regardless of sales, such as rent, permanent staff, utilities, and some fixed marketing expenses
2. Variable costs arise from sales, such as production/purchasing, temporary labor, payment processing, logistics, digital-advertising CPA, channel revenue shares, and taxes/tax provisions
3. Classify costs using the brand's actual accounting. Do not put all advertising costs into the same category; the course material demonstrates both fixed marketing expenses and digital-ad costs that vary with orders

## Calculations and interpretation

Classify fixed, variable or mixed costs according to how they vary with sales in this case, preserving charging basis and period; use supplied split rules for mixed costs and retain unknowns

## Required output fields

| Order | Field | How to complete |
|---:|---|---|
| 1 | Cost item | Use the supplied source, calculation, or explicit unknown |
| 2 | Amount/period | Use the supplied source, calculation, or explicit unknown |
| 3 | Charging basis | Use the supplied source, calculation, or explicit unknown |
| 4 | Fixed, variable or mixed | Use the supplied source, calculation, or explicit unknown |
| 5 | Classification evidence | Use the supplied source, calculation, or explicit unknown |
| 6 | Mixed-cost split | Use the supplied source, calculation, or explicit unknown |
| 7 | Unknowns/gaps | Use the supplied source, calculation, or explicit unknown |

## Verification cases

**MK-058-A1 | Monthly rent10000, payment fee2% of orders**

Expected: Classify fixed and variable with charging basis

**MK-058-A2 | Utilities include base and usage charges without a split**

Expected: Mark mixed and request split, not all fixed

## Method sources

Source file: 行銷策略實戰學程Day2-以終為始x降低成本x提升指標

Location: Costs

Source basis: extracted from course materials

Source URL: https://docs.google.com/presentation/d/1NdxlcqAKMPHqGVS5jbjSYR_UgOJSA0fS65OnTtQLEHQ/edit

English translation of source excerpt:

> Begin with the end in mind x reduce costs x improve metrics
