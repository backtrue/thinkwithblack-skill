---
name: mk-232
description: "Search Term Source Data Health Check. Use when you need dates, fields, and data gaps; apply this method to the specified inputs and verify the deliverable"
---

# MK-232｜Search Term Source Data Health Check

For a regular chat, upload `packs/mk-232.md`; it includes the shared rules, this method, and required references

## Purpose

This Skill delivers: **Dates, fields, and data gaps**

If the account cannot show all terms, do not call the data complete market demand; the same term can mean different things in different service contexts

## Required Inputs

Original Search Terms report with export source and timestamp, covered period, time zone, currency, filters and visible-row coverage, field definitions, and available tracking or conversion mappings

## Method Steps

1. Verify that rows are actual customer Search Terms and retain the original file, export timestamp, and source; keep Keywords and generated ideas separate
2. Check period, time zone, currency, filters, aggregation level, and coverage; identify missing dates, mixed periods, truncation, and hidden portions
3. Check types and definitions for queries, associated ads or keywords, clicks, cost, and available conversions; distinguish zero, blank, untracked, and hidden values; inspect actual row dimensions before treating repeated query text as duplication
4. Verify the mapping from tracked conversions to business outcomes; without that bridge, retain language and relevance analysis and leave business value unconfirmed
5. Deliver a field-health table, supported analysis scope, and missing-data requests; preserve raw values and record any cleaning rules

## Calculation and Interpretation

Search term reports may not cover the entire market; observe when evidence is insufficient, and do not choose negative keywords from guesses alone

## Required Output Fields

| Order | Field | How to complete |
|---:|---|---|
| 1 | Source, export time, and covered period | Use the supplied source, calculation, or explicit unknown |
| 2 | Time zone, currency, filters, and coverage | Use the supplied source, calculation, or explicit unknown |
| 3 | Field name, type, and definition | Use the supplied source, calculation, or explicit unknown |
| 4 | Missing, zero, untracked, or hidden status | Use the supplied source, calculation, or explicit unknown |
| 5 | Duplicate and aggregation checks | Use the supplied source, calculation, or explicit unknown |
| 6 | Tracking-to-business-outcome mapping | Use the supplied source, calculation, or explicit unknown |
| 7 | Supported analysis and missing data | Use the supplied source, calculation, or explicit unknown |
| 8 | Raw values, cleaning rules, and effects | Use the supplied source, calculation, or explicit unknown |

## Verification Cases

**MK-232-A1 | A report has queries and clicks but no dates or conversion field**

Expected: Mark the period unknown and conversions unavailable; organize demand language, but do not compare period performance or fill the absent conversion column with zeros

## Method Sources

Original file: 行銷策略實戰學程 Day5｜Google Ads × LINE｜線上課程用投影片

Source location: Search terms

Source basis: Derived from course material

Original URL: https://docs.google.com/presentation/d/1RK8wiunlvJrRxgFuTcGhO5B5fRa4fbEogpZTJpF6YKc/edit

English translation of source excerpt retained in the master table:

> Search volume does not represent a single kind of value; search terms reflect different stages of the customer's purchase journey
