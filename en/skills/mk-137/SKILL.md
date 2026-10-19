---
name: mk-137
description: "Write Traditional Chinese Facebook ads with three confirmed comparison-aware USPs and active, friendly, and professional variants. Require 14–15 Traditional Chinese characters without punctuation in line one and 7–8 Traditional Chinese characters in the CTA"
---

# MK-137 | Three-Line Ad Copy

For a regular chat, upload `packs/mk-137.md`; it includes the shared rules, this method, and required references

## Purpose

Help users write Traditional Chinese Facebook ads. Confirm three USPs that imply a comparison with competitors, then deliver active, friendly, and professional variants together for A/B testing

## Required Inputs

Start with at least one of product information, base copy, or photos. Use supplied facts to fill gaps with suggested directions; keep unverified product, competitor, offer, and outcome claims pending confirmation

Propose exactly three USP drafts and let the user confirm, supplement, or revise them. Write the ads after the user confirms all three USPs. Infer a hypothetical consumer and situation from product information; a separate Persona confirmation is not required

Preserve a supplied short URL. Use [short URL] as a placeholder when none is supplied

## Method Steps

1. Analyze the product information, base copy, or photos and identify supported features and plausible consumer situations
2. Propose exactly three comparison-aware USPs and invite confirmation, additions, or revisions. Stop and wait for the user's reply before writing the ads
3. After USP confirmation, line one must contain exactly 14 or 15 Traditional Chinese characters. Use only those characters, with no punctuation, question mark, spaces, digits, Latin letters, or emoji. Express a consumer-situation question through wording. Check every character and rewrite until all three tones comply
4. Line two contains a clear CTA and short URL. The CTA wording must contain exactly 7 or 8 Traditional Chinese characters and no punctuation, spaces, digits, Latin letters, or emoji. Check it separately for all three tones and rewrite any failure before delivery. The complete message before the arrow, including introductory wording and CTA, must total 10–15 characters; introductory wording, arrow, and URL are excluded from the CTA's own count
5. Line three describes the consumer's potential emotions or feelings after using the product. Lines two and three each have a maximum of 40 characters
6. Deliver exactly three lines for each of the active, friendly, and professional tones together. Make the consumer the subject of every sentence, use gentle and natural language, avoid excessive exclamation marks, and write all ad variants in Traditional Chinese

Format, with the tone label outside the three body lines:

```text
[Active / Friendly / Professional]
Consumer-situation question in exactly 14–15 Traditional Chinese characters
Introductory wording and a 7–8-character Traditional Chinese CTA 👉 [short URL]
The consumer's potential feelings after use
```

The introduction and CTA together must contain 10–15 characters before the arrow. The entire second line, including introduction, CTA, arrow, and URL, must remain within 40 characters

Actual character validation: count each Chinese character as one Unicode character, rather than bytes, display width, or UTF-16 code units. Submit all three complete active, friendly, and professional drafts to the checker after writing. Validate 14–15 Chinese characters in line one, 7–8 in the CTA, 10–15 characters in the full message before the arrow, and at most 40 characters in each of lines two and three. If a tone is missing or duplicated, or any draft fails, rewrite and resubmit all three complete drafts. Deliver only after every draft passes, using the exact validated text. Any edits require another validation

## Calculation and Interpretation

Make the consumer the subject; products, brands, and components are objects the consumer uses or chooses. Describe feelings in line three rather than listing features or specifications

Keep the same confirmed USPs and facts across tones. Use supported differences or explicitly pending directions for competitor comparisons; do not invent competitor weaknesses, discounts, deadlines, prices, or outcomes

Preserve the short URL exactly. If the complete second line cannot fit 40 characters, request a shorter URL

## Required Output Fields

At the USP stage, deliver three comparison-aware drafts and a confirmation request. After confirmation, deliver the complete active, friendly, and professional variants together

| Order | Field | Requirement |
|---:|---|---|
| 1 | Version | USP draft or the three confirmed-USP ad variants |
| 2 | Task / angle | Three USPs and the active, friendly, and professional tones |
| 3 | Complete copy | Exactly three lines per variant, all three variants together |
| 4 | Factual sources | Supplied information, base copy, photos, and confirmed USPs |
| 5 | Format check | Line one: exactly 14–15 Traditional Chinese characters, no punctuation; CTA: exactly 7–8 Traditional Chinese characters; message before arrow: 10–15 characters total; lines two and three: at most 40 characters each; consumer subjects throughout |
| 6 | Pending facts | Specific factual or URL gaps affecting the copy |
| 7 | Subsequent use | A/B testing by the user |

Keep execution checks in work records; deliver the USP drafts or all three complete ad variants according to the current stage

## Verification Cases

- Before USP confirmation: propose three comparison-aware USP drafts and wait for confirmation, additions, or revisions
- After USP confirmation without separate Persona approval: infer a plausible consumer situation and deliver all three tones
- Length and characters: line one contains exactly 14 or 15 Traditional Chinese characters without punctuation; the CTA itself contains exactly 7 or 8 Traditional Chinese characters; count it separately from the 10–15-character message before the arrow; rewrite any failing variant
- Subject and emotion: use consumer subjects and post-use feelings, gentle Traditional Chinese wording, and restrained exclamation marks
- Missing short URL: retain a placeholder and do not invent offers or facts

## Confirmation and Revision

Wait for confirmation after presenting the three USPs. When the user revises facts, USPs, or direction, revise the affected content using the original material

## Method Sources

The original GPT instructions supplied by the user on 2026-10-18, followed by explicit changes requiring 14–15 Traditional Chinese characters in line one and 7–8 Traditional Chinese characters in the CTA

Supplementary course: Meta Advertising Course 101 — Let AI Help You Create Ads

Course URL: https://docs.google.com/presentation/d/19GaScd4rGE8V4iqPfemeK8-QAwbSIeOKGpB5OwwTMlo/edit
