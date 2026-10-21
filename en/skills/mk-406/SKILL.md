---
name: mk-406
description: "Seven-Day LINE Flow for Non-Buyers. Use when work requires a draft with conditions, messages, and exit rules; process the specified inputs using this method and verify the deliverable"
---

# MK-406 | Seven-Day LINE Flow for Non-Buyers

For ordinary chat, upload `packs/mk-406.md`, which includes the shared rules, this method, and required references

## Purpose

This skill delivers: **A draft with conditions, messages, and exit rules**

Do not send messages or create automation without approval; if a tool cannot show recipient eligibility, do not assume everyone can be messaged

## Required inputs


Available raw records: join time and promise, current purchase status, actual offers and expiry, responses, contact rules, and eligibility

## Method Steps

1. Define entry from actual join time, promised joining benefit, nonbuyer state, available products/offers, and contact eligibility. Seven days is an observation workflow, not seven mandatory messages
2. Fulfill the joining promise first. Before every message, check current state: buyers exit acquisition, opt-outs stop marketing within their scope, and expired offers lose their old promises
3. Usage questions receive instruction, explicit trust concerns receive genuine evidence, and cost/shipping concerns receive supported terms. Without a new barrier, follow existing frequency rules with a suitable next step rather than stacking coupons
4. For each node, specify trigger, task, eligible recipients, success transition, and suppression condition. Request the original consent/source record when eligibility is missing while delivering conditional drafts and the workflow
5. Replies, purchases, or complaints change the path when received, not on day seven. Seven days without purchase leaves a record of messages, answers, and unresolved gaps rather than automatically increasing discounts

## Calculation and Interpretation

Use the latest valid events to assign compatible nodes. Keep sent, received, clicked, and purchased states separate. Deliver node entry/exit conditions; a draft schedule is not a sent message

Check example (hypothetical): day one fulfills the joining promise and day three is scheduled for first-purchase information. A valid order on day two cancels the acquisition message; day three becomes relevant usage instruction or no message

Decision rules authored by ThinkWithBlack, 2026-10-14; original course sources remain below

## Required output fields

| Order | Field | How to fill it in |
|---:|---|---|
| 1 | Message task | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 2 | Audience and conditions | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 3 | Triggers / exclusions | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 4 | Body copy | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 5 | CTA | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 6 | Tracking fields | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 7 | Frequency rules | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 8 | Publication status | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |

## Method sources

Original file: 行銷策略實戰學程 Day5｜Google Ads × LINE｜線上課程用投影片

Source locator: LINE

Source basis: extracted from course materials

Original URL: https://docs.google.com/presentation/d/1RK8wiunlvJrRxgFuTcGhO5B5fRa4fbEogpZTJpF6YKc/edit

English translation of source excerpt retained in the master sheet:

> Google Ads × LINE
