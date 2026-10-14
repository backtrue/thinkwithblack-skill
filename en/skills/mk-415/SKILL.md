---
name: mk-415
description: "Cross-Channel Message Schedule. Use when work requires frequency, audiences, channels, and recipient permissions; process the specified inputs using this method and verify the deliverable"
---

# MK-415 | Cross-Channel Message Schedule

For ordinary chat, upload `packs/mk-415.md`, which includes the shared rules, this method, and required references

## Purpose

This skill delivers: **Frequency, audiences, channels, and recipient permissions**

Do not send messages or create automation without approval; if a tool cannot show recipient eligibility, do not assume everyone can be messaged

## Required inputs


Available raw records: channel lists and usable identity joins, consent/opt-out scope, sent/replied/completed records, offers, deadlines, and existing contact rules

## Method Steps

1. Match campaign lists across channels with usable deidentified identity keys. List actual consent/opt-out scope, sent/replied/completed states, offers, and deadlines. Unmatched identities remain unresolved rather than guessed from names
2. Completion of the same task, such as buying the first-order bundle, cancels remaining acquisition messages for that task across channels. For incomplete tasks, follow existing frequency and cross-channel rules; prior receipt does not prohibit all follow-up
3. Resolve incompatible offers and eligibility first. Prioritize necessary service and existing commitments by actual urgency and deadlines, then schedule marketing in available slots. If two campaigns lack priority, ask only which objective takes precedence rather than inventing a universal interval
4. A channel-specific opt-out removes that scope; an explicit global refusal removes global marketing. Missing eligibility on another channel leaves a draft rather than treating no opt-out as consent
5. Re-evaluate schedules before each planned send using new purchases, replies, expiry, and eligibility. Remove resolved needs and route new service problems to service while retaining contact history

## Calculation and Interpretation

Deliver channel, task, trigger, timing basis, and cancellation condition for each identifiable group. Deduplicate only linked identities and report unknown intersections separately

Check example (hypothetical): a Monday LINE acquisition message is followed by a planned Wednesday email for the same offer. A confirmed Tuesday purchase cancels Wednesday's promotion. A read receipt without purchase instead leaves follow-up governed by the existing contact rule

Decision rules authored by ThinkWithBlack, 2026-10-14; original course sources remain below

## Required output fields

| Order | Field | How to fill it in |
|---:|---|---|
| 1 | Date / stage | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 2 | Task | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 3 | Deliverable | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 4 | Prerequisites | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 5 | Responsible role | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 6 | Resources | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 7 | Conflict | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 8 | Status | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |

## Validation cases

**MK-415-C05｜Two campaigns use the same limited resource on the same day**

Expected: flag the resource conflict and adjustable options; do not assume unlimited resources

## Method sources

Original file: 營業額提升主要關鍵（二）社群/會員經營技巧

Source locator: LINE

Source basis: extracted from course materials

Original URL: https://docs.google.com/presentation/d/1ZYpstuVAXGk9KdZt1QZm2OQ7ozpYYtfrBf0Xsy7kRx8/edit

English translation of source excerpt retained in the master sheet:

> SMS, eDM, LINE, groups
