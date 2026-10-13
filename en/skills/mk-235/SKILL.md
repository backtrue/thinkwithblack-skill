---
name: mk-235
description: "Judge whether Google Search/Shopping search terms should be excluded. Use for low-click, apparently relevant terms and organizing negative keyword candidates. Assess intent, data volume, and the destination page directly; retain observation status when evidence is insufficient"
---

# MK-235｜Search Term Exclusion Review

For a regular chat, upload `packs/mk-235.md`; it includes the shared rules, this method, and required references

## Purpose

This Skill delivers: **Negative keyword candidates with explicit reasons**

If the account cannot show all terms, do not call the data complete market demand; the same term can mean different things in different service contexts

## Required Inputs

Provide: search terms, keywords, campaign performance, pages, and demand hypotheses

## Method Steps

1. Identify irrelevant, misunderstood, low-quality, or impossible-to-convert search terms for exclusion review
2. Clearly unrelated needs may justify negative keywords or stopping waste
3. Do not automatically exclude a term because conversions are temporarily zero; first verify intent, data volume, and the page's response so content/product opportunities are not mistaken for noise

## Calculation and Interpretation

Search term reports may not cover the entire market; observe when evidence is insufficient, and do not choose negative keywords from guesses alone

## Required Output Fields

| Order | Field | How to fill it |
|---:|---|---|
| 1 | Search term | Original evidence, intermediate method result, or explicitly unknown; do not fabricate |
| 2 | Original keyword and group | Original evidence, intermediate method result, or explicitly unknown; do not fabricate |
| 3 | Cost / result | Original evidence, intermediate method result, or explicitly unknown; do not fabricate |
| 4 | Intent fit | Original evidence, intermediate method result, or explicitly unknown; do not fabricate |
| 5 | Problem type | Original evidence, intermediate method result, or explicitly unknown; do not fabricate |
| 6 | Recommended action | Original evidence, intermediate method result, or explicitly unknown; do not fabricate |
| 7 | Affected scope | Original evidence, intermediate method result, or explicitly unknown; do not fabricate |
| 8 | Review | Original evidence, intermediate method result, or explicitly unknown; do not fabricate |

## Activation Conditions and Full Question Scope

Use MK-235 directly when the user asks whether actual search terms should be excluded, how to organize low-click but apparently relevant Shopping terms, or how to judge negative keyword candidates. Do not require proof of irrelevance before starting; this Skill checks intent, data volume, and pages to produce candidates or observation decisions

[Q026 original question](https://www.reddit.com/r/PPC/comments/1sos37a/search_terms_for_google_shopping_ads/) (English translation of the source excerpt): “Shopping search terms usually have fewer than 10 clicks per month and all appear relevant; CPC/CPA is rising and traffic seems less likely to buy. How should the terms be organized and exclusions chosen?” Cost and impressions of traffic quality are background here; the complete task is term organization and exclusion judgment. Use this Skill directly without requiring routing across methods

This Skill's existing intent, data-volume, page checks, and observation under insufficient evidence are sufficient for this task. Do not add independent methods merely for reading data, shared rules, or observation steps. Classify the task as multi-Skill only when another distinct and necessary method deliverable exists

For method questions, first provide the complete decision steps and organization fields; case-specific decisions for each term require actual terms, products/pages, periods, and available performance. Do not fabricate an exclusion list without concrete rows. Low clicks, zero conversions, rising CPC/CPA, or subjective impressions of buyer intent alone do not justify exclusion; retain all terms when all demand fits, without a fixed deletion count or threshold

Standalone CPC/CPA causes, Shopping learning periods/bids/budgets, Feed changes, or match-type definitions are outside this Skill's search-term judgment. If also requested, retain the full question and separately check methods and platform sources. Q014 includes learning-period optimization, so the complete question remains a capability gap; being able to handle its negative keyword portion does not establish that this Skill solves the whole question

## Method Sources

Original file: 行銷策略實戰學程 Day5｜Google Ads × LINE｜線上課程用投影片

Source location: Search terms

Source basis: Derived from course material

Original URL: https://docs.google.com/presentation/d/1RK8wiunlvJrRxgFuTcGhO5B5fRa4fbEogpZTJpF6YKc/edit

English translation of source excerpt retained in the master table:

> Search volume does not represent a single kind of value; search terms reflect different stages of the customer's purchase journey
