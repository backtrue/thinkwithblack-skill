---
name: mk-364
description: "AI Brand Description Accuracy Check. Use when work requires checks against original brand information; process the specified inputs using this method and verify the deliverable"
---

# MK-364 | AI Brand Description Accuracy Check

For ordinary chat, upload `packs/mk-364.md`, which includes the shared rules, this method, and required references

## Purpose

This skill delivers: **Checks against original brand information**

One answer does not establish a stable ranking; do not simulate current results when actual answers have not been obtained

## Required inputs

Provide: actual AI answers, queries, dates, platforms, and cited URLs

## Method steps

1. The description check goes beyond the presence of a brand name to verify AI's description of brand type, services, positioning, and differentiation
2. For vague descriptions, return to 105 to check identity signals; for incorrect descriptions, prioritize external context and brand descriptions
3. Do not immediately attribute AI errors to hallucination; first check whether the brand's own and third-party signals are confused

## Calculation and interpretation

Retain questions, dates, platforms, and actual answers; one result does not represent answers shown to all users

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

**MK-364-C05｜Data meets the existing conditions**

Expected: Report that it is usable or should be maintained; do not invent a need for changes

**MK-364-C06｜Tool returns an error**

Expected: Report that the data was not obtained; do not classify it as a business anomaly

## Method sources

Original file: SEO 106｜Check 成效診斷：從 AI 回答結果看出內容與品牌缺口

Source locator: questions

Source basis: extracted from course materials

Original URL: https://docs.google.com/presentation/d/1yJsbQNDgX4lUtExwfxXgaPvHjEwbjywvCKllchkIoOU/edit

English translation of source excerpt retained in the master sheet:

> • In what types of questions does it appear?
