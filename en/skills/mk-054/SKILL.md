---
name: mk-054
description: "Ranking selling points from surveys. Use when the task requires a ranking of the features consumers value. Apply this method to the specified inputs and verify the deliverable"
---

# MK-054 | Ranking selling points from surveys

For a regular chat, upload `packs/mk-054.md`. It includes the shared rules, this method, and required references

## Purpose

This skill delivers: **A ranking of the features consumers value**

Without raw survey responses, produce only a questionnaire or analysis plan; do not fabricate answers

## Required inputs

Provide the target group, selling points/pain points/features and their sources, questions and single/multiple-choice rules, raw answers, and sampling source. With only a survey objective, deliver questions and an analysis template first

## Method

1. For a survey-based warm-up campaign, list the consumer pain points and product features the brand currently believes may matter and let respondents vote/select
2. Rank pain points and selling points using actual survey results to prioritize sales-page section 2 and sections 4–6
3. Survey results are preference evidence for this sample; do not treat the brand's original guesses as consumer findings

## Calculations and interpretation

Deduplicate and count using each question's valid-response rules. Option share = valid respondents selecting the option / valid respondents for that question. Multiple-choice shares may total above 100%; keep single-choice, multiple-choice, and ranking questions separate. Retain ties, missing/excluded answers, sampling differences, and option order; sample preference is not a population share

## Required output fields

| Order | Field | How to complete |
|---:|---|---|
| 1 | Question/option and source | Use the supplied source, calculation, or explicit unknown |
| 2 | Response format | Use the supplied source, calculation, or explicit unknown |
| 3 | Valid respondent count | Use the supplied source, calculation, or explicit unknown |
| 4 | Selections/share/rank | Use the supplied source, calculation, or explicit unknown |
| 5 | Ties, missing and excluded answers | Use the supplied source, calculation, or explicit unknown |
| 6 | Supported content priorities | Use the supplied source, calculation, or explicit unknown |
| 7 | Sampling limits and next step | Use the supplied source, calculation, or explicit unknown |

## Verification cases

**MK-054-A1 | Ten valid respondents select A seven times and B six times in a multiple-choice question**

Expected: Report 70% and 60%; a 130% total is valid on this basis

**MK-054-A2 | Options exist but responses do not**

Expected: Deliver questions and calculation fields; leave observed rankings unfilled

## Method sources

Source file: 行銷策略實戰學程Day4-佈局獲利 × 節奏變現 × 轉單收割

Location: Survey

Source basis: extracted from course materials

Source URL: https://docs.google.com/presentation/d/1dq3xqYVUnWvUCpzZKI91yDDOzvkyG0uHy3EOsOjtItA/edit

English translation of source excerpt:

> Collect first-party data through surveys
