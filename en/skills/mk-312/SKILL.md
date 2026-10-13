---
name: mk-312
description: "Use website pages and GSC query/page performance to decide whether existing pages should be kept, improved, consolidated, or supplemented with new pages, and plan main entry pages and relevant internal links"
---

# MK-312｜Decide Whether to Keep, Improve, or Add Pages

For a regular chat, upload `packs/mk-312.md`; it includes the shared rules, this method, and required references

## Purpose

This Skill delivers: **Recommendations to avoid rework and duplicate pages**

Permission in robots or the existence of a sitemap does not guarantee indexing; do not combine site technical status and content quality into a single conclusion

## Required Inputs

Provide: website pages, HTML, existing content, audiences, and search demand

## Method Steps

1. For each question, determine whether an existing page already answers it, can be improved, or a new page is needed
2. If an existing page has the same topic/intent, prioritize improving it rather than creating a page for every long-tail question
3. Add a page only when existing pages have different tasks and cannot reasonably meet the need; explain the break caused by the missing page

## Calculation and Interpretation

Actually crawl/read content and site structure; check current rules and markup, without promising rankings or citations

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

## MK-312 Supplement: Main Entry Pages, GSC Performance, and Consolidation Decisions

This supplement extends existing-page decisions to topic-cluster organization; it is not a new quotation from the original course. When the user specifies a topic or treatment, inventory its existing URLs by reading the sitemap first, then cross-checking actual pages, internal links, and available GSC page/query data. Use the sitemap to discover URLs; it is not a complete site inventory or proof of indexing status

For GSC comparisons, hold the property, search type, filters, and equal-length nonoverlapping periods constant. First use the page dimension to find pages with rising/falling impressions or clicks, then inspect page × query data for candidate pages to understand the demand each serves. Record periods, dimensions, filters, row completeness, and tool limitations. If only some rows are returned, limits are insufficient, or data is unavailable, mark the inventory partial; missing rows are not zero. Differences between periods are observations and do not alone prove that page content or internal links caused the change

For each page, verify actual content, primary task, search intent, case/clinical evidence, service information, and current inbound/outbound pages. Separate different needs within a topic by their main destination URLs; general explanations, cost assessment, cases, and booking can use different pages. Sharing a keyword or declining impressions alone does not establish duplication or a need to consolidate

Classify each page as keep, improve, consolidation candidate, or add. List consolidation candidates only when search intent and core answers substantially overlap, one page can fully serve the need, and source pages have no cases or professional information requiring independent preservation. For each candidate, list the recommended destination URL, source pages, unique content to retain, canonical/redirect decisions to confirm, and internal links to update. Do not directly recommend deleting or redirecting pages before checking their URLs and content. Keep separate pages with clear roles when distinct treatment contexts or decision questions still have independent value

When internal link planning is needed, use the internal-link planning method to add a link map: source URL, target URL, link context, anchor text describing the next page's task, and the reader's next step. Link only when the destination continues the current need; do not interlink the whole site or promise that links themselves increase rankings or traffic

Deliver a decision table with one row per page, including at least URL, page role/intent, GSC comparison periods and page×query differences, keep/improve/consolidate/add decision, supporting evidence and unknowns, consolidation destination or improvement direction, recommended internal links, and follow-up metrics. Website editing, merging, canonical changes, or redirects still require separate explicit authorization before execution

## Verification Cases

**MK-312-C05｜One record meets opposing conditions**

Expected: mark contradictory or pending judgment; do not arbitrarily assign the most common category

## Method Sources

Original file: SEO 102-全站意圖佈局：從搜尋意圖到關鍵節點頁策略

Source location: Pages

Source basis: Derived from course material

Original URL: https://docs.google.com/presentation/d/1-Axcm6vxQIgjymV4Jv0X8x0mO_SGp3_0gVAZ1KI_ILk/edit

English translation of source excerpt retained in the master table:

> Different pages address different search needs
