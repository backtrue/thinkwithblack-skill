---
name: mk-326
description: "Answer-First Paragraph Check. Use when work requires locations where answers are buried too deeply or not given directly; process the specified inputs using this method and verify the deliverable"
---

# MK-326 | Answer-First Paragraph Check

For ordinary chat, upload `packs/mk-326.md`, which includes the shared rules, this method, and required references

## Purpose

This skill delivers: **Locations where answers are buried too deeply or not given directly**

General content rewriting differs from Speak Human TW language review; do not automatically apply its review documents without an explicit trigger

## Required inputs

Provide: the full article, reader questions, sources, and actual experience or evidence

## Method steps

1. Directly answer the question in the first 2–4 sentences below each H2, then add background, reasons, examples, and differences
2. Answer-First means placing the answer first, rather than removing context
3. If the answer appears only in the latter half of the paragraph, mark it as insufficiently front-loaded

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

**MK-326-C05｜Data meets the existing conditions**

Expected: Report that it is usable or should be maintained; do not invent a need for changes

**MK-326-C06｜Tool returns an error**

Expected: Report that the data was not obtained; do not classify it as a business anomaly

## Method sources

Original file: SEO104_AI可引用文章檢查表

Source locator: checks

Source basis: extracted from course materials

Original URL: https://docs.google.com/presentation/d/1hmaWbUWe-BsaRUVA9IpGrLUt7wQ8wdIVHe4W_Sg4uP4/edit

English translation of source excerpt retained in the master sheet:

> The task of 104: check whether an article has the conditions needed for AI citation
