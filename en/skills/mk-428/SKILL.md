---
name: mk-428
description: "UTM URL Generation and Check. Use when work requires trackable URLs and parameter errors; process the specified inputs using this method and verify the deliverable"
---

# MK-428 | UTM URL Generation and Check

For ordinary chat, upload `packs/mk-428.md`, which includes the shared rules, this method, and required references

## Purpose

This skill delivers: **Trackable URLs and parameter errors**

Adding impressions across platforms does not yield deduplicated reach; conversions with different attribution windows cannot be added as actual sitewide orders

## Required inputs

Provide: Complete destination URL, approved source/medium/campaign values, content/term when needed, existing tracking parameters and query/fragment to preserve

## Method steps

1. Parse path, existing query and fragment, preserving non-UTM parameters
2. Add approved source/medium/campaign and optional values with URL encoding; resolve conflicting existing UTM values rather than append duplicate keys
3. Reassemble query before fragment, decode/read back values and check preserved parameters/fragment
4. Deliver complete URL/parameter table; mark expected analytics reception only after actual testing/readback

## Calculation and interpretation

Preserve approved value casing and encode special characters; URL correctness and GA4 reception are separate checks

Source: [Google Analytics: Custom URLs](https://support.google.com/analytics/answer/10917952?hl=en)

## Required output fields

| Order | Field | How to complete |
|---:|---|---|
| 1 | Complete original URL | Use the supplied source, calculation, or explicit unknown |
| 2 | Approved UTM values | Use the supplied source, calculation, or explicit unknown |
| 3 | Existing parameters/conflicts | Use the supplied source, calculation, or explicit unknown |
| 4 | Complete generated URL | Use the supplied source, calculation, or explicit unknown |
| 5 | Decoded readback | Use the supplied source, calculation, or explicit unknown |
| 6 | Original query/fragment check | Use the supplied source, calculation, or explicit unknown |
| 7 | Actual test state | Use the supplied source, calculation, or explicit unknown |

## Verification cases

**MK-428-A1 | URL has ?sku=1#details and campaign contains a space**

Expected: Preserve sku/fragment; add encoded UTM query before fragment and decode-check

## Method sources

Original file: 營業額提升主要關鍵（三）從數據來提升 ROI 的策略

Source locator: reports

Source basis: extracted from course materials

Original URL: https://docs.google.com/presentation/d/1lwpCxF1cMgaK7Gnvngw8NzytDLYD8MK-p91g8dwSytU/edit

English translation of source excerpt retained in the master sheet:

> What reports are produced
