---
name: mk-042
description: "Diagnosing an overly early call to action. Use when the task requires locations that request a purchase or inquiry too early. Apply this method to the specified inputs and verify the deliverable"
---

# MK-042 | Diagnosing an overly early call to action

For a regular chat, upload `packs/mk-042.md`. It includes the shared rules, this method, and required references

## Purpose

This skill delivers: **Locations that request a purchase or inquiry too early**

Task stages are analytical categories, not a claim that every customer follows the same path

## Required inputs

Provide: The product or service, customers' own words, existing pages, and actions the company can support

## Method

1. Check the match between current intent and the CTA: informational users should not be forced to buy immediately, and transactional users should not be kept circling through educational content
2. Judge whether the next step is too early by asking "Would the customer actually want to take this action now?"
3. Leave uncertain cases pending validation; do not attribute low conversion directly to the CTA

## Calculations and interpretation

Search phrases and paths are planning hypotheses; check them against real search terms and evidence of how pages support the need

## Required output fields

| Order | Field | How to complete |
|---:|---|---|
| 1 | Object/location | Use source evidence, an intermediate method result, or an explicit unknown; do not invent information |
| 2 | Conditions for adoption | Use source evidence, an intermediate method result, or an explicit unknown; do not invent information |
| 3 | Actual evidence | Use source evidence, an intermediate method result, or an explicit unknown; do not invent information |
| 4 | Check status | Use source evidence, an intermediate method result, or an explicit unknown; do not invent information |
| 5 | Difference/candidate cause | Use source evidence, an intermediate method result, or an explicit unknown; do not invent information |
| 6 | Next task | Use source evidence, an intermediate method result, or an explicit unknown; do not invent information |
| 7 | Limitations | Use source evidence, an intermediate method result, or an explicit unknown; do not invent information |

## Verification cases

**MK-042-C05 | The data meets the existing conditions**

Expected: Report usable or maintain; do not manufacture a need for changes

**MK-042-C06 | The tool returns an error**

Expected: Report that the data was not obtained; do not classify it as a business anomaly

## Method sources

Source file: Google Ads 第一堂｜看懂需求，才知道廣告怎麼接

Location: Jumping ahead too quickly

Source basis: extracted from course materials

Source URL: https://docs.google.com/presentation/d/15ZOg0pX_xikpdA3FwGEoCSVgWortvCnxSe4hz4ugizg/edit

English translation of source excerpt:

> The instructor demonstrates a small-company attendance system in full, then deliberately checks whether "book a demo" jumps too far ahead
