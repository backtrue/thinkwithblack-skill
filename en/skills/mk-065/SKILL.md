---
name: mk-065
description: "Working backward to target cost per click. Use when the task requires cPC derived from acceptable CPA and conversion rate. Apply this method to the specified inputs and verify the deliverable"
---

# MK-065 | Working backward to target cost per click

For a regular chat, upload `packs/mk-065.md`. It includes the shared rules, this method, and required references

## Purpose

This skill delivers: **CPC derived from acceptable CPA and conversion rate**

Recalculability does not mean the data is complete; break-even points and cost ceilings apply only under the stated assumptions

## Required inputs

Raw inputs: consistent Target CPA, corresponding clicks K, valid orders P from those clicks, click definition, attribution/mature observation window and currency

## Method

1. Use the specified per-valid-order Target CPA. An approved estimate retains order value times margin times approved ad-allocation fraction, not revenue-target/order-value volume
2. Match clicks and their valid orders; purchase conversion rate is P/K. Outbound clicks, all clicks and sessions have distinct denominators. A session conversion rate cannot imply an all-click CPC allowance
3. With K positive, matched attribution and a mature window, Target CPC = Target CPA × P/K per corresponding click. For immature or unmatched outcomes, report observed counts and an unset usable rate
4. With K zero, conversion is undefined. With K positive and P zero, observed conversion and the formula value are zero but support no positive click allowance; do not recommend a platform zero bid or claim order cost zero
5. When matched actual CPC exceeds the candidate allowance, show the gap and conversion rate, then examine creative/audience/landing differences. Recompute after new valid orders, click definitions, windows or Target CPA; CPC alone does not establish the cause

## Calculations and interpretation

Hypothetical check: Target CPA 216 with 1,000 corresponding clicks and 10 valid orders gives Target CPC 2.16; 20 verified mature orders changes it to 4.32. If 1,000 denotes sessions, label the result per-session allowance rather than CPC

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

**MK-065-C05 | A required denominator is zero**

Expected: Report that the formula is undefined; do not output a zero cost or an infinite target

**MK-065-C06 | Only some costs are supplied**

Expected: Retain the partial result and excluded items; do not call it complete profitability

## Method sources

Source file: Meta廣告學程 104 廣告的數據決策

Location: CPC

Source basis: extracted from course materials

Source URL: https://docs.google.com/presentation/d/16FiqnSxBs-gSDxsxUBNhWdUX5vZrIWoZPGangj_f_Pk/edit

English translation of source excerpt:

> Cost per click (CPC)
