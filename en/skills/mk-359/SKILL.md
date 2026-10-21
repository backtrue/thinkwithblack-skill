---
name: mk-359
description: "Non-Branded Test Question Design. Use when work requires need-based questions without directly inserting the brand; process the specified inputs using this method and verify the deliverable"
---

# MK-359 | Non-Branded Test Question Design

For ordinary chat, upload `packs/mk-359.md`, which includes the shared rules, this method, and required references

## Purpose

This skill delivers: **Need-based questions without directly inserting the brand**

One answer does not establish a stable ranking; do not simulate current results when actual answers have not been obtained

## Required inputs

Provide: Customer needs and original questions, category or solution, test market and purpose, brand terms to exclude; AI answers are recorded after testing

## Method steps

1. Non-branded questions omit the brand name and ask about needs, comparisons, contexts, recommendations, or decisions
2. Check whether AI includes the brand among answer candidates when users do not yet know the brand
3. Retain brand-name questions for identity checks, but do not treat them as the main evidence of GEO performance

## Calculation and interpretation

Retain questions, dates, platforms, and actual answers; one result does not represent answers shown to all users

## Required output fields

| Order | Field | How to complete |
|---:|---|---|
| 1 | Non-branded test question | Use the supplied source, calculation, or explicit unknown |
| 2 | Need and source | Use the supplied source, calculation, or explicit unknown |
| 3 | Question type and intent | Use the supplied source, calculation, or explicit unknown |
| 4 | Brand-term exclusion check | Use the supplied source, calculation, or explicit unknown |
| 5 | Priority | Use the supplied source, calculation, or explicit unknown |
| 6 | Test conditions and not-yet-tested status | Use the supplied source, calculation, or explicit unknown |

## Verification cases

**MK-359-A1 | Customer question contains a brand**

Expected: Preserve the need in a non-branded version and record the exclusion check

## Method sources

Original file: SEO 106｜Check 成效診斷：從 AI 回答結果看出內容與品牌缺口

Source locator: questions

Source basis: extracted from course materials

Original URL: https://docs.google.com/presentation/d/1yJsbQNDgX4lUtExwfxXgaPvHjEwbjywvCKllchkIoOU/edit

English translation of source excerpt retained in the master sheet:

> • In what types of questions does it appear?
