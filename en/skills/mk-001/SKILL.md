---
name: mk-001
description: "Extract citable product facts and missing information from product pages, specifications and instructions. Use for “What can we say based on these materials?” Delivers a sourced fact table, focusing on facts before choosing selling points"
---

# MK-001 | Product fact inventory

For a regular chat, upload `packs/mk-001.md`. It includes the shared rules, this method, and required references

## Purpose

This skill delivers: **A citable product fact table and missing-input list**

Having a product page does not mean its effects have been independently verified; identify brand statements as brand-supplied claims

## Required inputs

Provide: Product specifications, competitor differences, verifiable evidence, and intended customers

## Method

1. First make the product itself visible to the AI: prioritize product-page content. If the tool cannot read the webpage directly, follow the course material by using product images or a product-page PDF
2. Confirm that the AI has correctly identified what the product is before proceeding to USP and Persona work. Correct misidentification first instead of immediately generating copy
3. Separate product facts from the brand's subjective views. The brand may add features it considers important, but do not treat features that were not supplied as facts

## Calculations and interpretation

Use only verifiable product differences. Mark claims lacking evidence as needing support; do not generate fabricated evidence

## Required output fields

| Order | Field | How to complete |
|---:|---|---|
| 1 | Item | Use source evidence, an intermediate method result, or an explicit unknown; do not invent information |
| 2 | Original statement | Use source evidence, an intermediate method result, or an explicit unknown; do not invent information |
| 3 | Applicable product/conditions | Use source evidence, an intermediate method result, or an explicit unknown; do not invent information |
| 4 | Source location | Use source evidence, an intermediate method result, or an explicit unknown; do not invent information |
| 5 | Evidence status | Use source evidence, an intermediate method result, or an explicit unknown; do not invent information |
| 6 | Wording usable in this task | Use source evidence, an intermediate method result, or an explicit unknown; do not invent information |
| 7 | Missing inputs | Use source evidence, an intermediate method result, or an explicit unknown; do not invent information |

## Verification cases

**MK-001-C05 | The source lists both a regular price and a promotional price**

Expected: Preserve each price's period and conditions; do not arbitrarily treat one as the permanent selling price

**MK-001-C06 | The only supplied claim is "best in the industry"**

Expected: List it as an unverified claim, not an objective ranking

## Method sources

Source file: Meta廣告學程 101 讓AI幫你投出廣告

Location: USP

Source basis: extracted from course materials

Source URL: https://docs.google.com/presentation/d/19GaScd4rGE8V4iqPfemeK8-QAwbSIeOKGpB5OwwTMlo/edit

English translation of source excerpt:

> Help identify the product's USP (Unique Selling Proposition). This is also your first opportunity to communicate with the AI. It is good if it identifies the point, but if it does not get what you mean, make sure to tell it your thinking
