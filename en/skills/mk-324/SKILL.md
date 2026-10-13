---
name: mk-324
description: "Article Opening Answer Check. Use when work requires missing questions, audience, answers, and decision guidance; process the specified inputs using this method and verify the deliverable"
---

# MK-324 | Article Opening Answer Check

For ordinary chat, upload `packs/mk-324.md`, which includes the shared rules, this method, and required references

## Purpose

This skill delivers: **Missing questions, audience, answers, and decision guidance**

General content rewriting differs from Speak Human TW language review; do not automatically apply its review documents without an explicit trigger

## Required inputs

Provide: the full article, reader questions, sources, and actual experience or evidence

## Method steps

1. Check whether the first 200 characters directly explain the question the article answers, who it is for, what answer it provides, and what readers can decide afterward
2. The introduction states the task of the whole article, rather than warming up or giving a generic overview of trends
3. If readers must scroll further to learn what the article solves, mark the introduction for improvement

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

**MK-324-C05｜Data meets the existing conditions**

Expected: Report that it is usable or should be maintained; do not invent a need for changes

**MK-324-C06｜Tool returns an error**

Expected: Report that the data was not obtained; do not classify it as a business anomaly

## Method sources

Original file: SEO104_AI可引用文章檢查表

Source locator: checks

Source basis: extracted from course materials

Original URL: https://docs.google.com/presentation/d/1hmaWbUWe-BsaRUVA9IpGrLUt7wQ8wdIVHe4W_Sg4uP4/edit

English translation of source excerpt retained in the master sheet:

> The task of 104: check whether an article has the conditions needed for AI citation
