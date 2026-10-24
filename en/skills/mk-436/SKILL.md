---
name: mk-436
description: "Plan website or app funnel nodes, actions, events, and value, including ads, LINE, phone calls, and forms leading to valid inquiries across multiple clinics. Preserve source, period, unit, and deduplication rules; distinguish early actions from business outcomes"
---

# MK-436 | Website Funnel Event Plan

For ordinary chat, upload `packs/mk-436.md`, which includes the shared rules, this method, and required references

## Purpose

This skill delivers: **Definitions of nodes, actions, events, and value**

Adding impressions across platforms does not yield deduplicated reach; conversions with different attribution windows cannot be added as actual sitewide orders

Use this method when multiple clinics record ads, LINE, phone calls, and forms separately and need to connect clicks, friend additions, and valid inquiries. Keep clinic, treatment, source, and period separate. Record LINE button clicks, friend additions, and valid inquiries as different actions, and use approved identity and deduplication rules. When linkage evidence is unavailable, preserve the separate counts and required fields

## Required inputs

Provide: Actual website/app flow, business goals, actions/pages to observe, available order/event identifiers and current tracking; planned flow when implementation has not begun

## Method steps

1. First map the flow from source / medium through on-site behavior to goals and value, then choose the nodes that require event tracking
2. Answer the core questions: where users come from, what events they trigger, what goals they complete, and how much value they create
3. Events need not all be recorded by GA; they may include campaign actions or other verifiable behavior. Do not track events merely for tracking when they serve no business decision

## Calculation and interpretation

Verify data sources, dates, currencies, denominators, and attribution; sums across platforms do not equal unique reach or incremental impact

## Required output fields

| Order | Field | How to fill it in |
|---:|---|---|
| 1 | Goal | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 2 | Audience | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 3 | Plan / task | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 4 | Evidence and assumptions | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 5 | Prerequisites | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 6 | Resources | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 7 | Deliverables and acceptance | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |
| 8 | Unresolved items | Original evidence, intermediate method results, or an explicit unknown; do not fabricate |

## MK-436 supplementary method: define a consistent set of funnel units before calculating completion rates

When planning product views, add-to-cart, checkout starts, and payments, first list each node's trigger action, data source, counting unit, linking ID, deduplication method, period, and payment status. Event trigger counts, distinct sessions, distinct checkouts, and paid order counts are different units; a refresh or duplicate event does not represent an additional customer or checkout

Before calculating a completion rate, demonstrate that the numerator and denominator use the same unit, cohort, and compatible observation periods, and that paid units are a subset of the checkout-start units in that cohort. For example, when deduplicating by checkout ID, first fix the cohort of started checkout IDs, then verify which IDs actually paid within the specified observation window; count distinct checkout IDs in both numerator and denominator. If using sessions or customers, first confirm consistent linking and deduplication definitions; do not directly substitute paid order counts

Before using checkout-start event counts and paid order counts for a checkout completion or funnel conversion rate, confirm compatible deduplication units, cohort periods, and payment assignment. Until verified, state “Checkout completion rate cannot currently be calculated”; do not calculate or display completion / conversion rates from these two types of counts, including as warnings, counterexamples, quotations, or comparisons. Describe the definition gap in words instead. This restriction permits listing raw counts separately, showing changes on each count's own consistent basis, or reporting verifiable aggregate differences using order-to-event reconciliation; it does not support a conclusion that checkout completion declined or a particular field caused abandonment

Hypothetical examples must follow the same stopping rule. To demonstrate completion rate, explicitly define the denominator as one cohort of distinct checkout IDs and the numerator as those IDs that paid within the specified window. If only counts with different units are available, retain only examples on a consistent basis and the evidence still needed; do not display or calculate ratios mixing count types

Even with missing data, complete the table defining nodes, actions, events, and value. List how events and orders will be reconciled using linking IDs, how duplicate events will be handled, how payment / refund statuses and completions across weeks will be assigned, and which differences to check weekly. A tracking plan does not establish that events are installed, triggered successfully, or verified, and does not predetermine actual causes of abandonment

Funnel comparisons use the same units, periods, and definition of the paid subset

## Verification cases

**MK-436-A1 | Checkout clicked but payment incomplete**

Expected: Separate checkout-start from purchase-success with trigger evidence

## Method sources

Original file: 營業額提升主要關鍵（三）從數據來提升 ROI 的策略

Source locator: reports

Source basis: extracted from course materials

Original URL: https://docs.google.com/presentation/d/1lwpCxF1cMgaK7Gnvngw8NzytDLYD8MK-p91g8dwSytU/edit

English translation of source excerpt retained in the master sheet:

> What reports are produced
