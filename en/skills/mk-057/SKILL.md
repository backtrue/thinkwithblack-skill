---
name: mk-057
description: "Organizing recommendation-intent feedback. Use when the task requires a summary of recommendation intent and improvement feedback. Apply this method to the specified inputs and verify the deliverable"
---

# MK-057 | Organizing recommendation-intent feedback

For a regular chat, upload `packs/mk-057.md`. It includes the shared rules, this method, and required references

## Purpose

This skill delivers: **A summary of recommendation intent and improvement feedback**

Without raw survey responses, produce only a questionnaire or analysis plan; do not fabricate answers

## Required inputs

Provide: Recommendation question, scale, actual responses and collection period; question design needs only the product/service and respondents. Invitation candidates additionally need deidentified member keys, contact eligibility and campaign conditions

## Method

1. Keep the member-care email's central question focused on NPS/recommendation intent; do not expand it into a long questionnaire
2. Identify Promoters/high-recommendation-intent respondents as candidates for later member-event invitations
3. Recommendation intent indicates an attitude only; do not treat it as an actual referral or sale

## Calculations and interpretation

Standard NPS uses a 0–10 recommendation scale: 9–10 promoters, 7–8 passives, 0–6 detractors. NPS = (promoters − detractors) / valid responses × 100. Report missing/out-of-range exclusions; no calculation with zero valid responses. For other scales, report the original distribution. A high score is not an actual referral; verify contact eligibility for invitations

Source: [Bain: Measuring Your Net Promoter Score](https://www.netpromotersystem.com/about/measuring-your-net-promoter-score/)

## Required output fields

| Order | Field | How to complete |
|---:|---|---|
| 1 | Recommendation question and scale | Use the supplied source, calculation, or explicit unknown |
| 2 | Valid response count and exclusions | Use the supplied source, calculation, or explicit unknown |
| 3 | Promoter, passive and detractor counts | Use the supplied source, calculation, or explicit unknown |
| 4 | NPS calculation and result | Use the supplied source, calculation, or explicit unknown |
| 5 | Deidentified high-intent candidate keys | Use the supplied source, calculation, or explicit unknown |
| 6 | Contact eligibility and invitation tasks | Use the supplied source, calculation, or explicit unknown |

## Verification cases

**MK-057-A1 | 10 valid responses: 6 promoters, 2 passives, 2 detractors**

Expected: NPS = (6−2)/10×100 = 40; passives remain in the denominator

**MK-057-A2 | Responses use 1–5 or are all missing**

Expected: Do not convert to standard NPS; report original distribution or zero valid responses

## Method sources

Source file: 營業額提升主要關鍵（二）社群/會員經營技巧

Location: NPS

Source basis: extracted from course materials

Source URL: https://docs.google.com/presentation/d/1ZYpstuVAXGk9KdZt1QZm2OQ7ozpYYtfrBf0Xsy7kRx8/edit

English translation of source excerpt:

> The member-care email asks only the "NPS question" and also identifies a list of Promoters to serve as the basis for member-event invitations
