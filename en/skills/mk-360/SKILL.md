---
name: mk-360
description: "AI Search Question Prioritization. Use when work requires question selection based on business relevance and representativeness; process the specified inputs using this method and verify the deliverable"
---

# MK-360 | AI Search Question Prioritization

For ordinary chat, upload `packs/mk-360.md`, which includes the shared rules, this method, and required references

## Purpose

This skill delivers: **Question selection based on business relevance and representativeness**

One answer does not establish a stable ranking; do not simulate current results when actual answers have not been obtained

## Required inputs

Provide: actual AI answers, queries, dates, platforms, and cited URLs

## Method steps

1. Select the most important 10 questions for live testing, prioritizing needs and business contexts in which the brand wants to be understood / recommended
2. Retain both low-intent and high-intent questions to see at which stage the brand is absent
3. Avoid test bias by not selecting only questions most likely to mention the brand

## Calculation and interpretation

Retain questions, dates, platforms, and actual answers; one result does not represent answers shown to all users

## Required output fields

| Order | Field | How to fill it in |
|---:|---|---|
| 1 | Candidate | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 2 | Eligibility | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 3 | Relevant evidence | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 4 | Task fit | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 5 | Limitations / resources | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 6 | Priority | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 7 | Tradeoff rationale | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 8 | Missing items | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |

## Validation cases

**MK-360-C05｜Only two valid candidates exist**

Expected: deliver the two items and their limitations; do not invent other candidates to meet a quota

## Method sources

Original file: SEO 106｜Check 成效診斷：從 AI 回答結果看出內容與品牌缺口

Source locator: questions

Source basis: extracted from course materials

Original URL: https://docs.google.com/presentation/d/1yJsbQNDgX4lUtExwfxXgaPvHjEwbjywvCKllchkIoOU/edit

English translation of source excerpt retained in the master sheet:

> • In what types of questions does it appear?
