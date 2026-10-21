---
name: mk-256
description: "Product Image and Link Check. Use when you need matching images and destination pages to products; apply this method to the specified inputs and verify the deliverable"
---

# MK-256｜Product Image and Link Check

For a regular chat, upload `packs/mk-256.md`; it includes the shared rules, this method, and required references

## Purpose

This Skill delivers: **Matching images and destination pages to products**

When IDs cannot be matched one-to-one, leave them unmatched rather than guess; do not invent a match rate without complete event samples

## Required Inputs

Catalog platform and link, image_link, and additional_image_link values by SKU or variant; product pages and authoritative product images; current read results and relevant official image and link specifications

## Method Steps

1. Preserve original link, image_link, and additional_image_link values by SKU or variant; read the URLs and final redirect destinations, recording response status and time
2. Verify the landing product and variant and inspect whether accessible images depict that product rather than another color or model; a downloadable image is not proof of a content match
3. Check format, dimensions, additional-image limits, and URL requirements against the actual platform’s current official specifications, recording sources and dates; leave missing access or specification evidence pending
4. Deliver access and matching results for each URL plus corrected URLs or missing-image requests; after an actual replacement, read back the page and image rather than treating a proposed URL as verified

## Calculation and Interpretation

Use product data for specifications and prices; verify catalog fields and disapproval rules during production

## Required Output Fields

| Order | Field | How to complete |
|---:|---|---|
| 1 | SKU or variant and original URL field | Use the supplied source, calculation, or explicit unknown |
| 2 | Response status, final URL, and read time | Use the supplied source, calculation, or explicit unknown |
| 3 | Actual page or image content | Use the supplied source, calculation, or explicit unknown |
| 4 | Product or variant match result | Use the supplied source, calculation, or explicit unknown |
| 5 | Specification source, date, and check result | Use the supplied source, calculation, or explicit unknown |
| 6 | Corrected URL or missing-image request | Use the supplied source, calculation, or explicit unknown |
| 7 | Post-change readback and unresolved items | Use the supplied source, calculation, or explicit unknown |

## Verification Cases

**MK-256-A1 | An image URL opens, but a blue SKU displays a red product**

Expected: Pass access and fail variant matching; request the correct blue image and read it back after an actual replacement

## Method Sources

Original file: Meta廣告學程 105 有轉換是業績擴大的開始

Source location: Products

Source basis: Derived from course material

Original URL: https://docs.google.com/presentation/d/1RzfmYLhPsK23uxqxWbKji2-efsbJPGFs_tMzCRX56BM/edit

English translation of source excerpt retained in the master table:

> From product planning to catalog ads and collections, improve performance through budget allocation
