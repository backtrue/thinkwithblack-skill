---
name: mk-236
description: "Search Term Observation Classification. Use when you need ambiguous items or items with insufficient data; apply this method to the specified inputs and verify the deliverable"
---

# MK-236｜Search Term Observation Classification

For a regular chat, upload `packs/mk-236.md`; it includes the shared rules, this method, and required references

## Purpose

This Skill delivers: **Ambiguous items or items with insufficient data**

If the account cannot show all terms, do not call the data complete market demand; the same term can mean different things in different service contexts

## Required Inputs

Provide: search terms, keywords, campaign performance, pages, and demand hypotheses

## Method Steps

1. Classify Search Terms as mine, exclude, observe, or content_signal; this Skill handles only observe
2. When meaning is uncertain, data is insufficient, or evidence does not yet support exclusion/increased investment, retain the original Search Term, current metrics, open questions, and the next evidence needed
3. Do not automatically add an ambiguous Search Term as a negative; explicitly label insufficient evidence as evidence_insufficient / low_confidence / needs_more_data
4. Available Search Terms may be restricted by privacy thresholds, so the observation list represents currently visible data, not the full market

## Calculation and Interpretation

Search term reports may not cover the entire market; observe when evidence is insufficient, and do not choose negative keywords from guesses alone

## Required Output Fields

| Order | Field | How to fill it |
|---:|---|---|
| 1 | Unit of analysis | Original evidence, intermediate method result, or explicitly unknown; do not fabricate |
| 2 | Original clues | Original evidence, intermediate method result, or explicitly unknown; do not fabricate |
| 3 | Category definitions | Original evidence, intermediate method result, or explicitly unknown; do not fabricate |
| 4 | Classification result | Original evidence, intermediate method result, or explicitly unknown; do not fabricate |
| 5 | Supporting / counterevidence | Original evidence, intermediate method result, or explicitly unknown; do not fabricate |
| 6 | Unknowns | Original evidence, intermediate method result, or explicitly unknown; do not fabricate |
| 7 | Downstream use | Original evidence, intermediate method result, or explicitly unknown; do not fabricate |

## Verification Cases

**MK-236-C05｜One record meets opposing conditions**

Expected: mark contradictory or pending judgment; do not arbitrarily assign the most common category

## Method Sources

Original file: Google Ads Search AI Skill｜Codex 開發交接規格

Source location: observe

Source basis: Specification reference

Original URL: https://docs.google.com/document/d/1jOD2aDqCQiEmH-aIm1ql3xpXZv4Px8gW5cT6XBaoamk/edit

English translation of source excerpt retained in the master table:

> • observe｜Keep under observation: insufficient data or uncertain meaning

### Additional Source Locations

Source verification record for the original course material

- Original location: observe
