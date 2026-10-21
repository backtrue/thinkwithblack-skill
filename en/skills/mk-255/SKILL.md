---
name: mk-255
description: "Product Stock Status Check. Use when you need availability and data update issues; apply this method to the specified inputs and verify the deliverable"
---

# MK-255｜Product Stock Status Check

For a regular chat, upload `packs/mk-255.md`; it includes the shared rules, this method, and required references

## Purpose

This Skill delivers: **Availability and data update issues**

When IDs cannot be matched one-to-one, leave them unmatched rather than guess; do not invent a match rate without complete event samples

## Required Inputs

Catalog platform, SKU or variant, feed availability and update time; actual page or inventory availability and observation time; update cadence, mechanism, and failure records; current accepted availability values

## Method Steps

1. Read feed and page or inventory source by SKU or variant, preserving both states and their respective timestamps
2. Check accepted values and meanings against the actual catalog platform’s current official specification, recording its source and date; do not copy another platform’s or a historical course’s enum list
3. Distinguish true availability mismatches, wrong variant mapping, and lag; use source-change and last successful feed-update times to investigate cadence, scheduling, or failures rather than treating observations from different times as simultaneous contradictions
4. Propose update and maintenance work for discrepancies such as feed availability versus source stockouts, identifying the authoritative source and owner; after an actual update, read back both states and timestamps

## Calculation and Interpretation

Use product data for specifications and prices; verify catalog fields and disapproval rules during production

## Required Output Fields

| Order | Field | How to complete |
|---:|---|---|
| 1 | SKU or variant and catalog platform | Use the supplied source, calculation, or explicit unknown |
| 2 | Feed status and update time | Use the supplied source, calculation, or explicit unknown |
| 3 | Page or inventory status and observation time | Use the supplied source, calculation, or explicit unknown |
| 4 | Platform accepted values and official basis | Use the supplied source, calculation, or explicit unknown |
| 5 | Mismatch, lag, and missing evidence | Use the supplied source, calculation, or explicit unknown |
| 6 | Update mechanism, cadence, and failure records | Use the supplied source, calculation, or explicit unknown |
| 7 | Proposed correction and owner | Use the supplied source, calculation, or explicit unknown |
| 8 | Post-update readback states and timestamps | Use the supplied source, calculation, or explicit unknown |

## Verification Cases

**MK-255-A1 | Yesterday’s feed says available; the product became unavailable this morning and sync logs are absent**

Expected: Record both observation times and possible lag, request update logs, and do not assert a confirmed synchronization failure

## Method Sources

Original file: Meta廣告學程 105 有轉換是業績擴大的開始

Source location: Products

Source basis: Derived from course material

Original URL: https://docs.google.com/presentation/d/1RzfmYLhPsK23uxqxWbKji2-efsbJPGFs_tMzCRX56BM/edit

English translation of source excerpt retained in the master table:

> From product planning to catalog ads and collections, improve performance through budget allocation
