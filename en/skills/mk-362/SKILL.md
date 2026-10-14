---
name: mk-362
description: "AI Citation Presence Assessment. Use when work requires records of websites and pages actually cited; process the specified inputs using this method and verify the deliverable"
---

# MK-362 | AI Citation Presence Assessment

For ordinary chat, upload `packs/mk-362.md`, which includes the shared rules, this method, and required references

## Purpose

This skill delivers: **Records of websites and pages actually cited**

One answer does not establish a stable ranking; do not simulate current results when actual answers have not been obtained

## Required inputs


Available raw records: the complete question and AI answer, platform and time, citation URLs and page passages, and matching owned content

## Method Steps

1. Preserve the full question, answer, platform, and time. Open each provided citation and inspect its actual URL, main content, and supporting passage. Start with visible evidence when the user supplies full text or screenshots
2. An explicit link to an owned page supporting the associated sentence is a supported owned citation. An owned link not supporting that sentence is a mismatched citation, calling for interpretation correction or examination of a factual page issue
3. A syndicated or third-party URL is credited to that page, not the owned site. Similar wording without traceable attribution is no confirmed citation; do not infer copying, training provenance, or actual use of an idea
4. For no citation, inspect the relevant owned content: add a missing answer, substantiate unsupported claims, or improve the opening/headings/lists when the answer is hard to find. If already clear and supported, retain it rather than rewriting solely because one answer omitted it
5. Reclassify after a complete citation, redirect, or answer version arrives. Request only the cited page or full answer; another Skill is not required. Tie every proposed edit to an observed page gap

## Calculation and Interpretation

Deliver answer sentence, citation URL, supporting passage, separate citation/support states, and matching action. Citation rate applies only to the fixed question set and recorded samples; failed answer retrievals remain separate

Check example (hypothetical): an answer resembles owned copy but cites only a media republication; record a third-party citation. A complete answer later reveals an additional owned URL supporting the sentence, changing the classification to owned citation

Decision rules authored by ThinkWithBlack, 2026-10-14; original course sources remain below

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

**MK-362-C05｜One record matches opposing conditions**

Expected: mark the data as contradictory or pending classification; do not arbitrarily assign the most common category

## Method sources

Original file: SEO 106｜Check 成效診斷：從 AI 回答結果看出內容與品牌缺口

Source locator: questions

Source basis: extracted from course materials

Original URL: https://docs.google.com/presentation/d/1yJsbQNDgX4lUtExwfxXgaPvHjEwbjywvCKllchkIoOU/edit

English translation of source excerpt retained in the master sheet:

> • In what types of questions does it appear?
