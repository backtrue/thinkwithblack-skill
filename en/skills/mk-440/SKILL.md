---
name: mk-440
description: "Cross-Platform Impression Definition Check. Use when work requires impressions that can be summed without treating them as unique reach; process the specified inputs using this method and verify the deliverable"
---

# MK-440 | Cross-Platform Impression Definition Check

For ordinary chat, upload `packs/mk-440.md`, which includes the shared rules, this method, and required references

## Purpose

This skill delivers: **Impressions that can be summed without treating them as unique reach**

Adding impressions across platforms does not yield deduplicated reach; conversions with different attribution windows cannot be added as actual sitewide orders

## Required inputs

Provide: GA4, GSC, advertising, and sales exports, metric definitions, and costs

## Method steps

1. The course materials' total-impressions formula is Impressions(GSC)+Impressions(FAD)+Google Ads impressions
2. Before summing, confirm consistent periods and definitions across the three sources; clearly label this as summed cross-platform impressions, rather than deduplicated people reached
3. If any source is missing, report partial impressions only, rather than complete total impressions

## Calculation and interpretation

Verify data sources, dates, currencies, denominators, and attribution; sums across platforms do not equal unique reach or incremental impact

## Required output fields

| Order | Field | How to fill it in |
|---:|---|---|
| 1 | Subject / location | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 2 | Conditions for use | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 3 | Actual evidence | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 4 | Check status | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 5 | Differences / possible causes | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 6 | Next task | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 7 | Limitations | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |

## Validation cases

**MK-440-C05｜Data meets the existing conditions**

Expected: Report that it is usable or should be maintained; do not invent a need for changes

**MK-440-C06｜Tool returns an error**

Expected: Report that the data was not obtained; do not classify it as a business anomaly

## Method sources

Original file: LookerStudio教學

Source locator: total impressions

Source basis: extracted from course materials

Original URL: https://docs.google.com/presentation/d/15dCCATrfSb0jHMhvfvp-15aQ5CvYW9xafHYPGm_pm3o/edit

English translation of source excerpt retained in the master sheet:

> What if the three costs and total-impression figures cannot be produced?
