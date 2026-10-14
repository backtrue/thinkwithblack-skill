---
name: mk-187
description: "Remarketing Repeated-Reach Check. Use when you need risks from audience overlap and excessive messaging; apply this method to the specified inputs and verify the deliverable"
---

# MK-187｜Remarketing Repeated-Reach Check

For a regular chat, upload `packs/mk-187.md`; it includes the shared rules, this method, and required references

## Purpose

This Skill delivers: **Risks from audience overlap and excessive messaging**

Event groups do not necessarily represent the same people dropping off at each stage; verify counting and attribution across data sources

## Required Inputs


Available raw records: audience inclusion/exclusion rules, valid purchase times, creative and exposure records, and available deidentified audience intersections

## Method Steps

1. For the same period, list audience inclusion/exclusion rules, valid purchase times, creatives, and available impressions/reach. Calculate person-level overlap only from usable deidentified intersection records; similar names do not establish overlap
2. If buyers still receive nonbuyer offers, repair list updates or exclusions. If the same person receives incompatible prices or ineligible offers, reconcile eligibility and promises before reducing every group's budget
3. Increasing repeated exposure plus declining response or mature conversions under comparable audience, creative, and time conditions supports a fatigue candidate. Compare a creative replacement or reduced repetition. Rising Frequency alone calls for checking response, not automatic pausing
4. Checkout failure, offer expiry, or audience changes redirect the action and withdraw a simple fatigue diagnosis. Without intersection data, inspect rule conflicts and actual exclusions rather than claiming to know who saw duplicates
5. Re-evaluate audience matching after purchase or eligibility updates. Withdraw an exposure-count-only reduction when repeated recipients still meet the cost objective

## Calculation and Interpretation

Frequency = impressions / reach within the same scope. Reach from different scopes cannot be added as unique people. Deliver the affected group, rule change, and original creative-comparison baseline; do not add a universal frequency cap

Check example (hypothetical): Frequency rises from two to four while mature acquisition cost stays within target, so maintain initially. A record then shows a buyer receiving a first-purchase-only ad; repair purchaser exclusion rather than reducing frequency everywhere

Decision rules authored by ThinkWithBlack, 2026-10-14; original course sources remain below

## Required Output Fields

| Order | Field | How to fill it |
|---:|---|---|
| 1 | Subject / location | Original evidence, intermediate method result, or explicitly unknown; do not fabricate |
| 2 | Conditions for use | Original evidence, intermediate method result, or explicitly unknown; do not fabricate |
| 3 | Actual evidence | Original evidence, intermediate method result, or explicitly unknown; do not fabricate |
| 4 | Check status | Original evidence, intermediate method result, or explicitly unknown; do not fabricate |
| 5 | Differences / possible causes | Original evidence, intermediate method result, or explicitly unknown; do not fabricate |
| 6 | Next task | Original evidence, intermediate method result, or explicitly unknown; do not fabricate |
| 7 | Limitations | Original evidence, intermediate method result, or explicitly unknown; do not fabricate |

## Verification Cases

**MK-187-C05｜Data meets existing conditions**

Expected: report usable or keep as is; do not invent a need for changes

**MK-187-C06｜The tool returns an error**

Expected: report data not obtained; do not classify the tool error as a business anomaly

## Method Sources

Original file: Meta廣告學程 102 為什麼這些人不買

Source location: Shopping cart

Source basis: Derived from course material

Original URL: https://docs.google.com/presentation/d/1VZM1BFp_CiefpdHFrSRKIDim5oOKHh52w6D5RUXi-Nc/edit

English translation of source excerpt retained in the master table:

> Cart abandonment rate
