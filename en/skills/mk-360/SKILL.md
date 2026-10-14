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


Available raw records: original customer/search/lost-sale questions with sources and dates, known frequency, and business objectives

## Method Steps

1. Build the question pool from real support, search, and won/lost-sale questions, preserving wording, date, and source. Remove brand-leading phrasing; retain brand names only when necessary to the original task
2. Group by the decision the person needs to make. Merge paraphrases with the same answer and choice, while separating understanding, comparison, suitability, and purchase tasks rather than keeping only easy recommendation prompts
3. Prioritize material conditions where a wrong answer causes a real wrong choice, then fill up to ten questions using documented frequency, business objectives, and uncovered tasks. Ties without evidence remain tied or use source order, not invented popularity scores
4. State why each question merits testing and which choice a wrong answer affects. Deliver fewer than ten when fewer independent real questions exist. Brand-desired questions without customer records remain separately labeled candidates
5. Replace redundant or lower-priority questions when new remarks reveal an important uncovered task. Version the set and distinguish retained from new questions in later comparisons. Expected model success must not determine selection

## Calculation and Interpretation

Deliver original question, source, decision task, selection/rejection reason, and replacement condition. Report counts and periods only when known; unknown frequency is not zero. Select questions before reading this round's AI answers

Check example (hypothetical): three of ten questions paraphrase the same product recommendation. A real compatibility question affecting whether the product works replaces a duplicate, even if it is less likely to mention the brand

Decision rules authored by ThinkWithBlack, 2026-10-14; original course sources remain below

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
