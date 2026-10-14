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


Available raw records: the complete question and AI answer, official brand names and aliases, actual cited pages, and product/service conditions

## Method Steps

1. Read the full question and answer, matching official names, clear aliases, and context to the actual brand. A namesake, citation URL, or author byline does not automatically count as a recommendation in the answer body
2. Separate body mention, recommendation/comparison inclusion, and owned-site citation. A complete answer to a generic definition question does not automatically fail because it omits a brand
3. If a relevant choice question omits the brand, first check whether the brand meets the requested conditions. If not, do not assert it should be recommended. If it does, inspect selected alternatives, cited pages, and visible selection criteria; unknown causes remain unknown
4. Repair a genuinely missing or wrong brand name, author/company identity, or product relationship on the cited page. If those are already clear, withdraw a weak-entity-link diagnosis and examine task fit or other visible differences
5. Reassess after new answers, full citations, renaming, or suitability changes. Request the page distinguishing unclear identity from unsuitable offering rather than blindly adding About sections, internal links, and cases

## Calculation and Interpretation

Deliver answer excerpt, mention/recommendation/citation states, relevance to the requested need, observed gap, matching edit, and withdrawal condition. One absent mention describes that observation, not platform-wide visibility

Check example (hypothetical): an AI answer cites an owned definition page without naming the brand. The question asks what waterproof ratings mean and the page clearly identifies the brand, so retain the content. If the question instead asks for regional service providers and the page gives the wrong service area, repair that fact

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

**MK-363-C05｜One record matches opposing conditions**

Expected: mark the data as contradictory or pending classification; do not arbitrarily assign the most common category

## Method sources

Original file: SEO 106｜Check 成效診斷：從 AI 回答結果看出內容與品牌缺口

Source locator: questions

Source basis: extracted from course materials

Original URL: https://docs.google.com/presentation/d/1yJsbQNDgX4lUtExwfxXgaPvHjEwbjywvCKllchkIoOU/edit

English translation of source excerpt retained in the master sheet:

> • In what types of questions does it appear?
