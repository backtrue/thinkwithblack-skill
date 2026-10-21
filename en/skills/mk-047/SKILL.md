---
name: mk-047
description: "Price-survey response review. Use when the task requires a list of missing values, contradictory responses, and outliers. Apply this method to the specified inputs and verify the deliverable"
---

# MK-047 | Price-survey response review

For a regular chat, upload `packs/mk-047.md`. It includes the shared rules, this method, and required references

## Purpose

This skill delivers: **A list of missing values, contradictory responses, and outliers**

Curve intersections, cost floors, and launch decisions are distinct tasks; a price intersection does not guarantee maximum profit

## Required inputs

Provide: Wording of the four PSM questions, currency and response format, raw answers, deidentified response keys, sampling and segments; supplied costs or market prices are range references only

## Method

1. First check that all four PSM questions concern price acceptance and that their directions have not been reversed
2. Price levels must span a reasonable range from cost to the high end of comparable competitors. A range that is too narrow distorts interpretation of intersections
3. Retain the original customer group/Persona for each response so audiences can later be compared. Flag missing or clearly invalid answers first; do not fill in values yourself

## Calculations and interpretation

Check sampling, valid responses, and the ordering of price questions; willingness to pay is neither actual purchasing nor a profit guarantee

## Required output fields

| Order | Field | How to complete |
|---:|---|---|
| 1 | Anonymous response key and four original prices | Use the supplied source, calculation, or explicit unknown |
| 2 | Question meaning and currency | Use the supplied source, calculation, or explicit unknown |
| 3 | Missing, inconsistent or unusual response | Use the supplied source, calculation, or explicit unknown |
| 4 | Keep/exclude rule and reason | Use the supplied source, calculation, or explicit unknown |
| 5 | Segment | Use the supplied source, calculation, or explicit unknown |
| 6 | Valid count after cleaning | Use the supplied source, calculation, or explicit unknown |
| 7 | Open issues and preserved original values | Use the supplied source, calculation, or explicit unknown |

## Verification cases

**MK-047-A1 | One of four prices is missing**

Expected: Preserve original values, flag the gap and apply stated validity rules without imputation

## Method sources

Source file: 營業額提升主要關鍵（一）縱深橫寬產品/產品線企劃策略

Location: PSM

Source basis: extracted from course materials

Source URL: https://docs.google.com/presentation/d/1lIddPByRFVZeT-TR3CSaL_lEKkpJRloL6JQBLg1fO50/edit

English translation of source excerpt:

> Van Westendorp's PSM (Price Sensitivity Measurement) fundamentally asks about the target consumer's acceptance of a price. It asks not only whether a price is expensive or cheap, but also which price is "too cheap"
