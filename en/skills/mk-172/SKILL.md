---
name: mk-172
description: "Remarketing Funnel Inventory. Use when you need segments for browsing, adding to cart, and purchasing; apply this method to the specified inputs and verify the deliverable"
---

# MK-172｜Remarketing Funnel Inventory

For a regular chat, upload `packs/mk-172.md`; it includes the shared rules, this method, and required references

## Purpose

This Skill delivers: **Segments for browsing, adding to cart, and purchasing**

Event groups do not necessarily represent the same people dropping off at each stage; verify counting and attribution across data sources

## Required Inputs

Raw ViewContent, AddToCart, and Purchase counts from the same source and common period; event-versus-person definitions, deduplication, and attribution conditions; page or customer-service evidence for subsequent concern hypotheses

## Method Steps

1. Record raw VC, ATC, and Purchase counts, source, and common period; verify compatible event or person counting definitions and identify incompatible fields before calculation
2. Calculate VC-to-ATC = ATC / VC and ATC-to-Purchase = Purchase / ATC; report numerators, denominators, and percentages; a zero denominator is not calculable, while a zero numerator with a positive denominator is 0%
3. Ratios of event totals describe relative event volumes, not sequential drop-off among the same people; person-level drop-off requires linked observations for the same cohort with consistent event order
4. Use differences to guide page, service, and creative investigation; list observable gaps and hypotheses without asserting psychological causes

## Calculation and Interpretation

VC-to-ATC ratio = ATC / VC; ATC-to-Purchase ratio = Purchase / ATC, expressed as percentages. A zero denominator is not 0%; when totals do not represent a linked cohort, neither a ratio nor one minus that ratio is a person-level conversion or drop-off rate

## Required Output Fields

| Order | Field | How to complete |
|---:|---|---|
| 1 | Source, common period, and counting or attribution definitions | Use the supplied source, calculation, or explicit unknown |
| 2 | Raw VC, ATC, and Purchase counts | Use the supplied source, calculation, or explicit unknown |
| 3 | Numerator, denominator, and formula for each ratio | Use the supplied source, calculation, or explicit unknown |
| 4 | Ratio or reason it cannot be calculated | Use the supplied source, calculation, or explicit unknown |
| 5 | Observed difference and definition limits | Use the supplied source, calculation, or explicit unknown |
| 6 | Hypotheses and required evidence | Use the supplied source, calculation, or explicit unknown |

## Verification cases

**MK-172-A1 | VC = 100, ATC = 20, Purchase = 0**

Expected: The ratios are 20% and 0%; these are event-volume ratios and do not establish that the same 20 visitors all failed to purchase

**MK-172-A2 | VC = 0, ATC = 0, Purchase = 0**

Expected: Both denominators are zero, so both ratios are not calculable

## Method Sources

Original file: Meta廣告學程 102 為什麼這些人不買

Source location: Shopping cart

Source basis: Derived from course material

Original URL: https://docs.google.com/presentation/d/1VZM1BFp_CiefpdHFrSRKIDim5oOKHh52w6D5RUXi-Nc/edit

English translation of source excerpt retained in the master table:

> Cart abandonment rate
