---
name: mk-363
description: "AI Brand Mention Assessment. Use when work requires whether the brand is mentioned and the surrounding context; process the specified inputs using this method and verify the deliverable"
---

# MK-363 | AI Brand Mention Assessment

For ordinary chat, upload `packs/mk-363.md`, which includes the shared rules, this method, and required references

## Purpose

This skill delivers: **Whether the brand is mentioned and the surrounding context**

One answer does not establish a stable ranking; do not simulate current results when actual answers have not been obtained

## Required inputs

Provide: actual AI answers, queries, dates, platforms, and cited URLs

## Method steps

1. The mention check determines whether AI mentions the brand in its answer
2. When content is cited without mentioning the brand, prioritize weak content-to-brand entity linkage as a diagnostic clue
3. Add author experience, brand cases, internal links, About pages, and service pages to make the content an asset demonstrating brand expertise

## Calculation and interpretation

Retain questions, dates, platforms, and actual answers; one result does not represent answers shown to all users

## Required output fields

| Order | Field | How to fill it in |
|---:|---|---|
| 1 | Unit of analysis | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 2 | Original clues | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 3 | Category definitions | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 4 | Classification results | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 5 | Support / counterexamples | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 6 | Unknowns | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 7 | Downstream use | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |

## Validation cases

**MK-363-C05｜One record matches opposing conditions**

Expected: mark the data as contradictory or pending classification; do not arbitrarily assign the most common category

## Method sources

Original file: SEO 106｜Check 成效診斷：從 AI 回答結果看出內容與品牌缺口

Source locator: questions

Source basis: extracted from course materials

Original URL: https://docs.google.com/presentation/d/1yJsbQNDgX4lUtExwfxXgaPvHjEwbjywvCKllchkIoOU/edit

English translation of source excerpt retained in the master sheet:

> • In what types of questions does it appear?
