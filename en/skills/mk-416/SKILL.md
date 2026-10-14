---
name: mk-416
description: "Unsubscribe and Inactivity Suppression Check. Use when work requires recipients and conditions for stopping messages; process the specified inputs using this method and verify the deliverable"
---

# MK-416 | Unsubscribe and Inactivity Suppression Check

For ordinary chat, upload `packs/mk-416.md`, which includes the shared rules, this method, and required references

## Purpose

This skill delivers: **Recipients and conditions for stopping messages**

Do not send messages or create automation without approval; if a tool cannot show recipient eligibility, do not assume everyone can be messaged

## Required inputs

Raw inputs: current unsubscribe/block/contact eligibility, delivery/bounces, observable clicks/replies/purchases, open-data visibility, approved inactivity window/frequency and current platform settings

## Method steps

1. Read current unsubscribe, block and contact eligibility first. Stop the relevant marketing contact for unsubscribed/blocked/ineligible records; missing eligibility stays unknown rather than inferred from purchases/friend counts. Retain history and state sources
2. Separate delivered, undelivered and unknown delivery, then actual clicks/replies/valid purchases from opens alone. Failed delivery is not disinterest; zero opens with clicks/purchases supports an active candidate
3. Retain applicable contact for eligible delivered records with valid interaction in the approved window. For eligible, confirmed-delivered records without observable interaction throughout the complete window, apply existing rules for reduced frequency, bounded preference confirmation or stopping. Without a set window/frequency, provide states and pending fields rather than invented days
4. Delivery failures call for repair/stop-address status, not another promotion to test interest. Protected or unknown open visibility cannot stand alone; use directly observable behavior and actual platform states
5. Deliver group conditions, raw behavior, retain/reduce/stop and review fields. New unsubscribes stop contact; new interaction can revise inactivity but cannot undo an unsubscribe. Renewed eligibility needs a new valid eligibility record and confirmed current state

## Calculation and interpretation

Inactivity means no observable valid interaction across the approved, fully covered window; retain delivery and behavior visibility. Apple Mail Privacy Protection prevents senders from seeing whether mail was opened, so zero opens alone does not establish inactivity ([Apple User Guide: Mail Privacy Protection](https://support.apple.com/en-ca/guide/iphone/iphf084865c7/ios))

Hypothetical check: a member has zero opens but link clicks, a valid purchase and current eligibility, supporting applicable contact. A new unsubscribe changes the action to stop; later clicks alone do not restore eligibility

Decision rules authored by ThinkWithBlack on 2026-10-14; original course sources are retained below

## Required output fields

| Order | Field | How to fill it in |
|---:|---|---|
| 1 | Subject / location | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 2 | Conditions for use | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 3 | Actual evidence | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 4 | Check status | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 5 | Differences / possible causes | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 6 | Next task | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 7 | Limitations | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |

## Validation cases

**MK-416-C05｜Data meets the existing conditions**

Expected: Report that it is usable or should be maintained; do not invent a need for changes

**MK-416-C06｜Tool returns an error**

Expected: Report that the data was not obtained; do not classify it as a business anomaly

## Method sources

Original file: 營業額提升主要關鍵（二）社群/會員經營技巧

Source locator: email opens

Source basis: extracted from course materials

Original URL: https://docs.google.com/presentation/d/1ZYpstuVAXGk9KdZt1QZm2OQ7ozpYYtfrBf0Xsy7kRx8/edit

English translation of source excerpt retained in the master sheet:

> Sender + email subject + preview text: affect open rate
