---
name: mk-035
description: "Generating natural customer search phrases. Use when the task requires candidate search phrases that preserve the original meaning. Apply this method to the specified inputs and verify the deliverable"
---

# MK-035 | Generating natural customer search phrases

For a regular chat, upload `packs/mk-035.md`. It includes the shared rules, this method, and required references

## Purpose

This skill delivers: **Candidate search phrases that preserve the original meaning**

Task stages are analytical categories, not a claim that every customer follows the same path

## Required inputs

Provide: The product or service, customers' own words, existing pages, and actions the company can support

## Method

1. For each event, write natural-language search phrases the customer might actually type into Google
2. Do not use brand copy or assume the person has already decided to buy
3. Treat search phrases as candidates and validate them later with actual search terms, customer-service data, or similar evidence

## Calculations and interpretation

Search phrases and paths are planning hypotheses; check them against real search terms and evidence of how pages support the need

## Required output fields

| Order | Field | How to complete |
|---:|---|---|
| 1 | Customer wording and source | Use the supplied source, calculation, or explicit unknown |
| 2 | Event and job | Use the supplied source, calculation, or explicit unknown |
| 3 | Actual candidate search phrase | Use the supplied source, calculation, or explicit unknown |
| 4 | Wording and intent rationale | Use the supplied source, calculation, or explicit unknown |
| 5 | Observed or hypothesized | Use the supplied source, calculation, or explicit unknown |
| 6 | Destination page and action | Use the supplied source, calculation, or explicit unknown |
| 7 | Validation data | Use the supplied source, calculation, or explicit unknown |

## Verification cases

**MK-035-C05 | An ad promotes a service that the page does not explain**

Expected: Record a verifiable promise gap; do not immediately conclude it caused all abandonment

**MK-035-C06 | No verbatim customer statements are available**

Expected: Produce only a need map awaiting validation, not a claimed finding from actual research

## Method sources

Source file: Google Ads 第一堂｜看懂需求，才知道廣告怎麼接

Location: Trigger event

Source basis: extracted from course materials

Source URL: https://docs.google.com/presentation/d/15ZOg0pX_xikpdA3FwGEoCSVgWortvCnxSe4hz4ugizg/edit

English translation of source excerpt:

> Identify need-trigger events
