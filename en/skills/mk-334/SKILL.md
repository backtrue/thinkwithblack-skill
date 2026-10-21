---
name: mk-334
description: "Source Check for Important Claims. Use when work requires a mapping of claims to sources that actually support them; process the specified inputs using this method and verify the deliverable"
---

# MK-334 | Source Check for Important Claims

For ordinary chat, upload `packs/mk-334.md`, which includes the shared rules, this method, and required references

## Purpose

This skill delivers: **A mapping of claims to sources that actually support them**

General content rewriting differs from Speak Human TW language review; do not automatically apply its review documents without an explicit trigger

## Required inputs

Provide: the full article, reader questions, sources, and actual experience or evidence

## Method steps

1. For important judgments, prioritize official documentation, research reports, papers, books, news, expert interviews, government data, or platform announcements
2. Citations must directly support the core judgment; do not merely append a list of sources to the article
3. Start by checking whether each article has at least 1–3 genuinely relevant sources; the goal is support for claims, not a source count

## Calculation and interpretation

Check only presence and clarity; do not invent experts, experience, or data, or guarantee AI citations

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

**MK-334-C05｜Data meets the existing conditions**

Expected: Report that it is usable or should be maintained; do not invent a need for changes

**MK-334-C06｜Tool returns an error**

Expected: Report that the data was not obtained; do not classify it as a business anomaly

## Method sources

Original file: SEO104_AI可引用文章檢查表

Source locator: checks

Source basis: extracted from course materials

Original URL: https://docs.google.com/presentation/d/1hmaWbUWe-BsaRUVA9IpGrLUt7wQ8wdIVHe4W_Sg4uP4/edit

English translation of source excerpt retained in the master sheet:

> The task of 104: check whether an article has the conditions needed for AI citation
