---
name: mk-339
description: "Weak Paragraph Prioritization. Use when work requires passages most worth revising first, with supporting reasons; process the specified inputs using this method and verify the deliverable"
---

# MK-339 | Weak Paragraph Prioritization

For ordinary chat, upload `packs/mk-339.md`, which includes the shared rules, this method, and required references

## Purpose

This skill delivers: **Passages most worth revising first, with supporting reasons**

General content rewriting differs from Speak Human TW language review; do not automatically apply its review documents without an explicit trigger

## Required inputs

Raw inputs: full article, core reader question, original sources for material claims, existing sections/dependencies and available editing resources

## Method steps

1. Read the core answer and evidence first. Wrong answers, source contradictions or unsupported material claims are mandatory first fixes. Pair the claim with its actual source and identify the conclusion it fails to support
2. After the core answer holds, identify missing applicability, exceptions, comparison criteria or next actions that would lead readers to choose incorrectly. State the missing information and the decision it enables, rather than just a low score
3. Next prioritize unclear or unextractable structure, then wording/headings/format. Fix upstream conclusions before dependent sections. Within a tier, prioritize core-task impact and repairs supported by available evidence
4. Choose feasible items within resources and provide original text, gap, evidence needed, specific edit and affected sections. Deliver two valid issues when only two exist. When tool scores differ, retain the actual priority evidence
5. Reorder affected items when evidence or the core answer changes and remove resolved items. A source overturning a claim requires withdrawing that claim and dependent advice before the planned formatting edit

## Calculation and interpretation

Order fixes by wrong core answer/unsupported material evidence, decision-changing omissions, comprehension/structure, then wording/format. Within a tier consider dependencies and feasible resources. A score difference is not an improvement outcome

Hypothetical check: an H2 rewrite initially leads, but the core comparison reverses its cited finding. Fix the conclusion and dependent recommendation first; after verifying the conclusion, return to remaining H2 and other gaps

Decision rules authored by ThinkWithBlack on 2026-10-14; original course sources are retained below

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

**MK-339-C05｜Only two valid candidates exist**

Expected: deliver the two items and their limitations; do not invent other candidates to meet a quota

## Method sources

Original file: SEO104_AI可引用文章檢查表

Source locator: checks

Source basis: extracted from course materials

Original URL: https://docs.google.com/presentation/d/1hmaWbUWe-BsaRUVA9IpGrLUt7wQ8wdIVHe4W_Sg4uP4/edit

English translation of source excerpt retained in the master sheet:

> The task of 104: check whether an article has the conditions needed for AI citation
