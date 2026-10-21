---
name: mk-137
description: "Write Traditional Chinese Facebook ads from three confirmed comparison-aware USPs. Base line one on the Persona’s buying motivation rather than a fixed pain-point formula. Deliver three tones with 14–15 Traditional Chinese characters in line one and 7–8 in the complete CTA"
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

1. Analyze the product information, base copy, or photos to identify supported features, the Persona’s buying motivation, and plausible situations. Determine why this person wants to buy, what they hope to gain, or what concerns affect the choice before selecting an angle. Prefer supplied customer statements, reviews, or interviews; use a reasonable hypothesis when evidence is missing
2. Propose exactly three comparison-aware USPs and invite confirmation, additions, or revisions. Stop and wait for the user's reply before writing the ads
3. After USP confirmation, start line one from the Persona’s buying motivation. Use question wording to evoke a relevant situation or desired experience, choosing a pain point, aspiration, self-identity, or purchase concern according to that motivation. Do not default to pain points or add fear merely to attract attention. Line one must contain exactly 14 or 15 Traditional Chinese characters, with no punctuation, question mark, spaces, digits, Latin letters, or emoji. Check every character and rewrite until all three tones comply
4. Line two is exactly a complete 7–8-character Traditional Chinese CTA followed by the fixed separator, arrow, and short URL. Every word before that separator belongs to the CTA and counts toward the same limit. Do not add introductory wording or offer prefixes, exclude a prefix, or validate only the final phrase. Allow no punctuation, spaces, digits, Latin letters, or emoji in the complete CTA. Check all three tones and rewrite any failure before delivery
5. Line three describes the consumer's potential emotions or feelings after using the product. Lines two and three each have a maximum of 40 characters
6. Deliver exactly three lines for each of the active, friendly, and professional tones together. Make the consumer the subject of every sentence, use gentle and natural language, avoid excessive exclamation marks, and write all ad variants in Traditional Chinese

Format, with the tone label outside the three body lines:

```text
[Active / Friendly / Professional]
Question based on buying motivation in exactly 14–15 Traditional Chinese characters
Complete 7–8-character Traditional Chinese CTA 👉 [short URL]
The consumer's potential feelings after use
```

The complete text before the fixed separator and arrow is the CTA. Count all of it as 7–8 Traditional Chinese characters, including any supplied prefix. Exclude only the fixed separator space, arrow, and URL. Keep the complete second line and third line within 40 characters each

Actual character validation: count each Chinese character as one Unicode character, rather than bytes, display width, or UTF-16 code units. Submit all three complete active, friendly, and professional drafts to the checker after writing. Validate 14–15 Chinese characters in line one, 7–8 in the complete CTA before the arrow including all prefix text, and at most 40 characters in each of lines two and three. If a tone is missing or duplicated, or any draft fails, rewrite and resubmit all three complete drafts. Deliver only after every draft passes, using the exact validated text. Any edits require another validation

## Calculation and Interpretation

Check the connection: Persona’s buying motivation → situation or desired experience evoked by line one → how a confirmed USP supports this choice. Age, gender, or a busy lifestyle describes the audience but does not establish a reason to buy. Separate supplied motivation evidence from reasonable hypotheses, then check whether the opening addresses the reason for this purchase

Pain points, aspirations, self-identity, and purchase concerns can all provide an opening angle. A specific problem may support a pain-point opening; a desire to reward oneself may support aspiration or self-identity; a shopper already comparing ingredients may respond to a purchase concern. Select according to buying motivation and USP support, rather than judging copy by whether its tone is gentle or forceful

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
| 5 | Format check | Line one: exactly 14–15 Traditional Chinese characters, no punctuation; Complete CTA before the arrow: exactly 7–8 Traditional Chinese characters with every prefix included; lines two and three: at most 40 characters each; consumer subjects throughout; connection between buying motivation, the opening situation, and the confirmed USP |
| 6 | Pending facts | Specific factual or URL gaps affecting the copy |
| 7 | Subsequent use | A/B testing by the user |

Keep execution checks in work records; deliver the USP drafts or all three complete ad variants according to the current stage

## Verification Cases

- Before USP confirmation: propose three comparison-aware USP drafts and wait for confirmation, additions, or revisions
- After USP confirmation without separate Persona approval: infer a plausible consumer situation and deliver all three tones
- Length and characters: line one contains exactly 14 or 15 Traditional Chinese characters without punctuation; the entire CTA before the arrow contains exactly 7 or 8 Traditional Chinese characters; every prefix counts toward this same limit; rewrite any failing variant
- Subject and emotion: use consumer subjects and post-use feelings, gentle Traditional Chinese wording, and restrained exclamation marks
- Missing short URL: retain a placeholder and do not invent offers or facts
- Aspiration or self-identity: when the Persona wants to reward themselves or develop a self-care habit, evoke that motivation and connect it to a confirmed USP; do not force a pain or fear angle
- Problem or purchase concern: use a pain point for a specific problem, or a purchase concern when an interested shopper is comparing ingredients; check the motivation–opening–USP connection in each case
- Demographics without motivation evidence: do not infer a purchase reason directly from age, gender, or a busy lifestyle; use a reasonable hypothesis and retain USP confirmation without a separate Persona approval gate

## Confirmation and Revision

Wait for confirmation after presenting the three USPs. When the user revises facts, USPs, or direction, revise the affected content using the original material

## Method Sources

The original GPT instructions supplied by the user on 2026-10-18, followed by explicit changes requiring 14–15 Traditional Chinese characters in line one and 7–8 Traditional Chinese characters in the entire CTA before the arrow, including any prefix

On 2026-10-21, the user clarified that line one starts with the Persona’s buying motivation, choosing pain points, aspirations, self-identity, or purchase concerns accordingly and checking the connection to the opening situation and confirmed USPs

Supplementary course: Meta Advertising Course 101 — Let AI Help You Create Ads

Course URL: https://docs.google.com/presentation/d/19GaScd4rGE8V4iqPfemeK8-QAwbSIeOKGpB5OwwTMlo/edit
