---
name: mk-059
description: "Per-product contribution margin calculation. Use when the task requires the amount remaining after specified variable expenses. Apply this method to the specified inputs and verify the deliverable"
---

# MK-059 | Per-product contribution margin calculation

For a regular chat, upload `packs/mk-059.md`. It includes the shared rules, this method, and required references

## Purpose

This skill delivers: **The amount remaining after specified variable expenses**

Recalculability does not mean the data is complete; break-even points and cost ceilings apply only under the stated assumptions

## Required inputs

Provide: Unit net revenue, variable costs on the same unit basis and calculation scope

For method questions, provide the formula, variables and an example directly; for a calculation, ask only for missing operands

## Method

1. Calculate a product's contribution margin amount by subtracting its variable costs from revenue first
2. Variable costs must include actual items such as purchasing/production, payment processing and logistics, revenue shares, taxes, and advertising incurred with sales
3. Flag missing cost items as incomplete; do not pass off selling price minus purchase cost as the full contribution margin

## Calculations and interpretation

Per-product contribution margin = net revenue per unit − variable costs for that unit

Retain original values, units, periods, and substituted formulas. The formula is not an unconditional guarantee of results

Define gross profit, contribution margin, cost denominators, and periods explicitly; do not copy classroom example numbers as universal thresholds

## Required output fields

| Order | Field | How to complete |
|---:|---|---|
| 1 | Input variable | Use source evidence, an intermediate method result, or an explicit unknown; do not invent information |
| 2 | Value | Use source evidence, an intermediate method result, or an explicit unknown; do not invent information |
| 3 | Unit and definition | Use source evidence, an intermediate method result, or an explicit unknown; do not invent information |
| 4 | Source | Use source evidence, an intermediate method result, or an explicit unknown; do not invent information |
| 5 | Formula | Use source evidence, an intermediate method result, or an explicit unknown; do not invent information |
| 6 | Result | Use source evidence, an intermediate method result, or an explicit unknown; do not invent information |
| 7 | Limitations | Use source evidence, an intermediate method result, or an explicit unknown; do not invent information |

## MK-059 supplementary method: contribution per eligible visitor

When comparing offers or comparable groups, first calculate each valid order's contribution using the same period and cost basis, then sum the group's contribution and divide by all eligible visitors in that group. Keep zero-order visitors in the denominator. If groups are defined by customer, use deduplicated customer counts; do not replace customers with order counts. If a visitor/customer has multiple orders, sum their in-scope orders using an attribution rule fixed in advance

Contribution per eligible visitor = total contribution from the group's valid orders ÷ all eligible visitors in the group. Revenue per visitor and contribution per visitor are different. When costs are incomplete, report only partial contribution; do not call revenue per visitor profit. Do not output contribution per visitor when the denominator is zero or missing

State the aggregation level and denominator, whether zero-order visitors are included, whether customers are deduplicated, and the completeness of costs
Do not define additional purchases/incrementality solely as new customers; new versus existing customer status is not causal evidence. Comparing offer effects also requires a valid control or comparable baseline and sufficient observation time. Otherwise, report only an arithmetic scenario or observed difference

### Revenue, discount, and refund basis: deduct each item only once

Establish the basis of the revenue input before writing the per-order contribution formula. If it is already net of discounts, do not deduct discounts again; if refunds have already reduced revenue, do not deduct them again. If the input is before discounts, subtract actual discounts once. If refunds are not yet reflected, subtract refunds that have occurred for the same order scope and observation period. If cost or refund data has not matured, report provisional/partial contribution rather than final profit

When "revenue" or "receipts" does not specify the treatment of discounts and refunds, do not choose a definition yourself. Provide two conditional formulas and identify the missing fields. Until the basis is confirmed, do not call one result complete contribution or profit

### Supplementary acceptance cases
**MK-059-C07 | The per-visitor denominator and boundaries of additional purchases**
Case data: Group A has 100 eligible visitors and total order contribution of 1,000 monetary units; Group B has 100 eligible visitors and total order contribution of 800 monetary units. Both denominators include eligible visitors who did not order
Expected: Group A's contribution per visitor is 10 monetary units and Group B's is 8. Output the formula, denominator, and cost completeness. Without a visitor denominator, do not infer contribution per visitor. When assessing additional purchases, do not consider only new-customer counts or treat an arithmetic difference as causal proof

### Supplementary method sources
- [Oracle Commerce experiment goals](https://docs.oracle.com/en/cloud/saas/cx-commerce/21a/ccexp/configure-goals.html): Revenue per Visitor uses the number of participants in the group as its denominator. This supplementary method replaces the numerator with the order contribution calculated by this skill; it does not call Oracle's revenue metric a profit metric
- [Shopify Profit reports](https://help.shopify.com/en/manual/reports-and-analytics/shopify-reports/report-types/default-reports/profit-reports): used to check the definitions of net sales, costs, gross profit, discounts, and refunds
- The contribution-per-visitor formula is a supplementary step written by ThinkWithBlack from the per-order contribution method; it is not claimed to be quoted verbatim from the sources above

### Free-shipping comparisons: verify shipping revenue from buyers first; do not substitute logistics expense

Use this only when comparing shipping/free-shipping offers for the current task. The first deliverable must list knowns and unknowns: net product revenue excluding shipping P, the original shipping fee charged to the buyer F, the seller's payment to the logistics provider L, other costs C, and whether the receipts input already includes F. The seller's per-order shipping, logistics, or delivery cost can only be L. Statements such as "the buyer pays shipping", "below the free-shipping threshold", or "the seller absorbs shipping" do not supply the amount of F

If F or the receipts basis is missing, first state "The reduction in contribution from making existing orders ship free cannot currently be calculated." For the same orders that would have occurred anyway, holding product revenue, logistics expenses, and other costs constant: original contribution is P+F-L-C, new free-shipping contribution is P-L-C, and new minus original is -F. N existing orders lose N×F in receipts. L occurs in both offers and is neither an incremental cost nor its upper bound. Leave F symbolic when unknown; do not assume F=L, F≤L, or zero original net shipping revenue. Do not calculate a fixed loss, percentage decline, or break-even increase in orders from such assumptions

Even a purely hypothetical example must explicitly state "Assume additionally that the buyer originally paid shipping F = [amount], and product revenue excludes F" before substitution. Saying only "this is hypothetical" or "the customer pays shipping" is insufficient. Knowing L does not permit assuming the same F. Retain logistics expense in both old and new offers; do not write the old offer simply as product gross profit. Do not turn a hypothetical result into a currently known loss

Calculate additional orders separately as P-L-C; do not treat their partial contribution as the loss on existing orders. If receipts already include F, separate out P first; do not add F or deduct shipping twice. Identify partial contribution when costs such as payment processing or refunds are missing. After preserving unknowns, still complete segmentation and controlled-comparison design. The missing-input list must include the buyer's original shipping fee and whether receipts include shipping, not merely the order distribution

For free-shipping comparisons, follow the separate verification of revenue and expenses described above

## Verification cases

**MK-059-C05 | A required denominator is zero**

Expected: Report that the formula is undefined; do not output a zero cost or an infinite target

**MK-059-C06 | Only some costs are supplied**

Expected: Retain the partial result and excluded items; do not call it complete profitability

## Method sources

Source file: 行銷策略實戰學程Day2-以終為始x降低成本x提升指標

Location: Costs

Source basis: extracted from course materials

Source URL: https://docs.google.com/presentation/d/1NdxlcqAKMPHqGVS5jbjSYR_UgOJSA0fS65OnTtQLEHQ/edit

English translation of source excerpt:

> Begin with the end in mind x reduce costs x improve metrics
