---
name: mk-109
description: "Check shipping-cost responsibility and low-average-order-value risks in free-shipping offers, or explain why a free-shipping formula subtracts AOV, the amount remaining per order, and the difference from a reference baseline. Check product revenue, buyer-paid shipping, and logistics expense for each offer. A purely formula-based question can be answered with symbols; do not infer an optimal threshold or conversion effect"
---

# MK-109 | Free-shipping offer check

For a regular chat, upload `packs/mk-109.md`. It includes the shared rules, this method, and required references

## Purpose

This skill delivers: **Shipping-cost responsibility and low-average-order-value risks**

Do not fabricate discounts, gift inventory, countdown deadlines, limited quantities, or testimonials

## Required inputs

Keep symbols for formula questions; calculations need product net revenue excluding shipping P, buyer shipping charge F, logistics expense L, other costs C, whether receipts include F, existing orders N and original/new offer conditions

## Method

1. Free shipping can lower the first-purchase barrier as part of a new-customer promotional bundle
2. Shipping remains a variable cost and belongs in the contribution margin calculation; free shipping does not mean zero cost
3. The course mentions using convenience-store-pickup platforms during campaigns to reduce payment-processing and shipping costs, but supplies no fixed free-shipping-threshold formula

## Calculations and interpretation

Check gross margin and stacked offers; time limits, inventory, and benefits must be real, with no promise of guaranteed results

## Required output fields

| Order | Field | How to complete |
|---:|---|---|
| 1 | Offer and conditions | Use the supplied source, calculation, or explicit unknown |
| 2 | Product net revenue P | Use the supplied source, calculation, or explicit unknown |
| 3 | Buyer shipping revenue F | Use the supplied source, calculation, or explicit unknown |
| 4 | Logistics expense L | Use the supplied source, calculation, or explicit unknown |
| 5 | Other costs C | Use the supplied source, calculation, or explicit unknown |
| 6 | Whether receipts include F | Use the supplied source, calculation, or explicit unknown |
| 7 | Original/new contribution calculation | Use the supplied source, calculation, or explicit unknown |
| 8 | Existing-order difference N×F | Use the supplied source, calculation, or explicit unknown |
| 9 | New-order contribution | Use the supplied source, calculation, or explicit unknown |
| 10 | Unknowns and missing data | Use the supplied source, calculation, or explicit unknown |

## MK-109 supplementary method: checking revenue and expenses in free-shipping offers

### Free-shipping comparisons: verify shipping revenue from buyers first; do not substitute logistics expense

Use this only when comparing shipping/free-shipping offers for the current task. The first deliverable must list knowns and unknowns: net product revenue excluding shipping P, the original shipping fee charged to the buyer F, the seller's payment to the logistics provider L, other costs C, and whether the receipts input already includes F. The seller's per-order shipping, logistics, or delivery cost can only be L. Statements such as "the buyer pays shipping", "below the free-shipping threshold", or "the seller absorbs shipping" do not supply the amount of F

If F or the receipts basis is missing, first state "The reduction in contribution from making existing orders ship free cannot currently be calculated." For the same orders that would have occurred anyway, holding product revenue, logistics expenses, and other costs constant: original contribution is P+F-L-C, new free-shipping contribution is P-L-C, and new minus original is -F. N existing orders lose N×F in receipts. L occurs in both offers and is neither an incremental cost nor its upper bound. Leave F symbolic when unknown; do not assume F=L, F≤L, or zero original net shipping revenue. Do not calculate a fixed loss, percentage decline, or break-even increase in orders from such assumptions

Even a purely hypothetical example must explicitly state "Assume additionally that the buyer originally paid shipping F = [amount], and product revenue excludes F" before substitution. Saying only "this is hypothetical" or "the customer pays shipping" is insufficient. Knowing L does not permit assuming the same F. Retain logistics expense in both old and new offers; do not write the old offer simply as product gross profit. Do not turn a hypothetical result into a currently known loss

Calculate additional orders separately as P-L-C; do not treat their partial contribution as the loss on existing orders. If receipts already include F, separate out P first; do not add F or deduct shipping twice. Identify partial contribution when costs such as payment processing or refunds are missing. After preserving unknowns, still complete segmentation and controlled-comparison design. The missing-input list must include the buyer's original shipping fee and whether receipts include shipping, not merely the order distribution

For free-shipping comparisons, follow the separate verification of revenue and expenses described above

## Verification cases

**MK-109-A1 | P=500, F=60, L=80, C=300, N=10**

Expected: Original contribution180, new120; existing orders lose600, not logistics80 substituted for shipping60

**MK-109-A2 | Only L=80 is known, F unknown**

Expected: Keep original P+F−80−C, new P−80−C and difference −F

**MK-109-A3 | Receipts560 already include F=60**

Expected: Derive P=500; do not add60 to560

## Method sources

Source file: 行銷策略實戰學程Day4-佈局獲利 × 節奏變現 × 轉單收割

Location: Campaign

Source basis: extracted from course materials

Source URL: https://docs.google.com/presentation/d/1dq3xqYVUnWvUCpzZKI91yDDOzvkyG0uHy3EOsOjtItA/edit

English translation of source excerpt:

> Consider consumers with active needs each month and bring campaign traffic to the campaign page for prompt conversion
