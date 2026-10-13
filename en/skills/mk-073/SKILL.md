---
name: mk-073
description: "When revenue declines or misses a target, use consistently defined data to decompose traffic, conversion-rate, and average-order-value differences and decide what to check first, the next action, and review conditions. Ask for missing data first and reassess after corrections"
---

# MK-073 | Revenue-gap decomposition

For a regular chat, upload `packs/mk-073.md`. It includes the shared rules, this method, and required references

Method revision: 2026-10-12 | Decision Model prototype

## Purpose

Answer one decision: **For this revenue decline or target shortfall, should we first examine traffic, conversion, or average order value?**

Deliver a decomposition of traffic, conversion-rate, and average-order-value gaps, then state the priority for investigation, supporting basis, next step, and review conditions. Use the user's stated comparison period or target directly

## Required data and follow-up questions

First organize the fields below from the information already supplied. Calculate what can be calculated and ask only for what is missing

| Required data | Purpose |
|---|---|
| Comparison period and current period, or target and actual | Identify the two sets of numbers to compare; keep target figures labeled as assumptions |
| Net revenue for both periods | Calculate the revenue difference and check currency, discounts, refunds, shipping, and transaction-status treatment |
| Transaction count for both periods | Calculate average order value = net revenue ÷ transaction count |
| Traffic and its unit for both periods | Calculate conversion rate = transaction count ÷ traffic; consistently use store visits or visiting groups in physical stores and one consistent traffic definition for websites |
| Operating days, time slots, and data sources | Establish comparable scope and make findings traceable to the original table or attachment |

If consistently defined conversion rates, average order values, and traffic are already available, decompose directly and reconcile with net revenue. Costs, fixed expenses, and gross margin are needed only when the user separately asks about profitability; complete the revenue decision when the current question has sufficient data

Continue according to the missing inputs:

- Revenue only: calculate the total difference first, then ask for transactions and traffic in both periods. Reuse the traffic unit if supplied; ask for the unit only if it is missing
- Revenue and transaction counts available: first calculate average order value and transaction changes. If both periods have more than 0 transactions, calculate the combined transaction change=(N1−N0)×A0 and the average-order-value difference=N1×(A1−A0), where N is transaction count; reconcile their sum to the revenue difference. Then obtain both periods' traffic and units to split the transaction change into traffic and conversion components
- Current period only: ask which period or target to compare against first
- Different period lengths or operating hours: first select dates and hours that can be aligned. Totals, daily averages, and operating-day differences may be listed first; rank priorities once the comparison scope is fixed
- Inconsistent definitions: identify the specific differing field and request alignment of that field; reuse the background already supplied
- General method question without numbers: deliver the decision table below and a minimal record template: "date/operating hours, traffic and unit, transaction count, net revenue, stockout/non-purchase/return and exchange records". Explain which figures are needed to select a branch

## Method

1. **Decompose revenue**: fix the period and definitions of traffic, transactions, and net revenue first, then calculate traffic × conversion rate × average order value. Distinguish unit price from average order value according to transaction contents; use the per-transaction average when purchases include multiple items
2. **Locate the gap**: compare target and actual or actuals from two periods, decompose amounts in the fixed order below, then choose a decision branch. If consistently defined impressions and clicks are available, further decompose impressions × click-through rate = clicks. When clicks are used as traffic, the conversion-rate denominator must also be clicks. Calculate website sessions and store visitors using their respective definitions
3. **Connect to a decision**: deliver the priority for investigation, supporting evidence, candidate causes to check, next step, and review conditions. When new data changes the premises, update the calculations and branch and revise the original action accordingly

## Calculations and interpretation

Let 0 represent the comparison period or target and 1 the current period or actual. T=traffic, C=conversion rate, A=average order value, R=net revenue. First verify R=T×C×A for both sets

Use the fixed order "traffic → conversion rate → average order value", replacing one variable at a time:

| Difference | Formula |
|---|---|
| Traffic difference | (T1 − T0) × C0 × A0 |
| Conversion-rate difference | T1 × (C1 − C0) × A0 |
| Average-order-value difference | T1 × C1 × (A1 − A0) |
| Total difference | Sum of the three components = R1 − R0 |

Preserve positive and negative signs. Compare negative differences by monetary amount and list positive differences separately as offsets. When several variables change together, this fixed order determines how interactions are allocated. The priority is a starting point for investigation; causes still require supporting records

Retain original values, units, periods, sources, and substituted formulas together. Enter conversion rates as decimals and present them as percentages if useful. Preserve precision during calculation and round only at the end. If the sum does not reconcile, first investigate periods, refunds, transaction status, traffic denominators, and rounding in the inputs; resolve these before selecting a branch

With a zero denominator, mark the corresponding ratio incalculable and retain confirmed revenue and transaction facts. For example, with positive traffic and zero transactions, conversion rate is 0 but average order value is undefined; examine non-conversion records first. If every variable in an individual difference formula is known, list that component first. Mark components involving undefined average order value incalculable, report the total revenue difference separately, and leave the complete three-part decomposition pending inputs. With zero traffic, verify operating and traffic records first, then decompose the three amounts once usable data is available

## Decision branches

Resolve required-data gaps, zero denominators, and inconsistent definitions first, then check the comparison baseline for this question. If data is comparable and there is no revenue gap, prioritize "maintain the current approach" and list positive and negative offsets. Rank traffic, conversion, or average-order-value investigations only when a revenue gap exists. If two or more components are negative, rank them under "multiple declines" first, then connect each to its investigation action. When the user corrects data, recheck starting from the affected inputs

| Evidence condition | Current decision | What to investigate next | When to review or revise the decision |
|---|---|---|---|
| Traffic falls while conversion rate and average order value are stable or rising | Check the traffic gap first | Compare operating days, time slots, channels, or impressions/clicks using existing records; locate the gap in a verifiable segment | Recalculate the three differences after segment data is supplied or the next comparable period |
| Conversion rate falls while traffic and average order value are stable or rising | Check the conversion gap first | Examine stockouts, non-purchase inquiries, service interactions, or checkout records; compare the same products, time slots, or channels | Once records support a cause, propose the corresponding improvement; recalculate conversion rate and revenue in the next comparable period |
| Average order value falls while traffic and conversion rate are stable or rising | Check the average-order-value gap first | Compare items per transaction, category mix, discounts, and refunds to locate the differences | Confirm product or order segments after the data is complete, then recalculate average order value and revenue |
| Two or more components have negative differences | Investigate in descending order of negative monetary impact | Check records for the largest negative component first and list other negatives and positive offsets; list equal amounts together and prioritize by available evidence | Update the investigation order when new data changes the amount ranking |
| Only revenue and transaction counts are known; traffic is unknown | Interpret transactions and average order value first, then select the traffic or conversion branch after obtaining traffic | Request store-visitor or website-traffic data and units for the same periods | Decompose all three differences again after traffic is supplied |
| Periods, denominators, refund treatment, or other definitions differ, or the formula does not reconcile | Align the data first | Identify mismatched fields, differences, and required original records | Rank investigations only after definitions align and the sum can be verified |
| No revenue gap exists against the baseline for this question | Maintain the current approach and review the next comparable period | List changes and offsets; if the user has specified a target, check against that target as well | Reassess when a new gap appears or the user supplies a new target |
| The user supplies or corrects data | Reselect the branch from updated data | Update affected ratios, all three amounts, the priority, and actions; identify the datum that changed the decision | Continue with the corrected data and review conditions |

Express candidate causes as verification actions, such as "compare stockout dates with non-purchase records". Link proposed adjustments to specific verified evidence and actions within the user's control. Preserve the distinct evidence status of a manager's impressions, a decline in one ratio, and an amount ranking

## Required output fields

Begin with a paragraph stating "what to check first, the basis, what to do next, and when to review", then retain the seven fields below in a table. With insufficient data, deliver calculable parts and necessary follow-up questions first. For method-only questions, deliver the decision table and recording method

| Order | Field | How to complete |
|---:|---|---|
| 1 | Input variable | Revenue, traffic, transaction count, conversion rate, and average order value used for this question |
| 2 | Value | Original or calculated values; label unknowns explicitly |
| 3 | Unit and definition | Period, currency, traffic denominator, and transaction/refund definitions |
| 4 | Source | Original table, attachment, user-supplied numbers, or explicitly labeled target assumptions |
| 5 | Formula | Substituted values, three differences, and total reconciliation; identify missing inputs for fields that cannot be calculated |
| 6 | Result | Selected branch, priority, next step, and review conditions |
| 7 | Limitations | Specific missing inputs or definition differences affecting this branch decision; when complete, write "Data for calculation and branch selection is complete". Put unverified causes and target assumptions in the next steps |

When using the known-customer-group supplement, integrate group differences into the same deliverable and identify which group's records to examine first. Select a traffic, conversion, or average-order-value branch only after obtaining traffic and transaction data for that group

## MK-073 supplementary method: revenue differences for known customer groups

If mutually exclusive, collectively exhaustive groups and consistently defined period data are supplied, prioritize actual net revenue. Otherwise, estimate each group's revenue as order count × average order value using the same period and order-status definitions. Group revenue difference = current-period group revenue − comparison-period group revenue. The sum of group differences should equal the total revenue difference. If it does not, investigate period, grouping, refund, or definition differences first rather than forcing reconciliation

This is an arithmetic decomposition of known groups. It does not explain why groups changed or prove advertising caused the changes. Order count is not customer count; analysis of customer numbers or first/repeat purchases additionally requires deduplicated customer IDs and a first-order definition. Preserve and resolve differences in classification, refunds/allowances, currency, or order-status definitions first

### Supplementary acceptance cases
**MK-073-C07 | Revenue differences between new and returning customers**
Case data: in the comparison period, new customers placed 100 orders with average order value 1,200 monetary units; returning customers placed 80 orders at 1,800. In the current period, new customers placed 140 orders at 1,100; returning customers placed 45 at 1,700. Perform this arithmetic decomposition only if periods, currency, order status, and group definitions match and new/returning groups are mutually exclusive and collectively exhaustive
Expected: Comparison-period revenue: new customers 120,000 monetary units, returning customers 144,000, total 264,000. Current-period figures: 154,000, 76,500, total 230,500. The new-customer group changes by +34,000 and the returning-customer group by −67,500, totaling −33,500 and matching the overall difference. Treat counts as orders, not people; do not infer customer counts, explain causes, or claim advertising causality

### Supplementary method sources
- [Shopify Customers reports](https://help.shopify.com/en/manual/reports-and-analytics/shopify-reports/report-types/default-reports/customers-reports): used to check definitions of first purchases, returning customers, customer cohorts, and report scope
- The group-difference formula is ThinkWithBlack's arithmetic decomposition of the categorized data supplied by the user; it is not claimed to be a universal attribution formula defined by Shopify

## Verification cases

The following are fictional practice data. Unless a case states otherwise, both periods use the same operating periods and traffic/transaction definitions; amounts are net revenue in New Taiwan dollars

| Case | Comparison period → current period | Expected decision and checks |
|---|---|---|
| D01 Traffic | 1,000 visitors / 100 transactions / 100,000 → 800 visitors / 80 transactions / 80,000 | Traffic difference −20,000, others 0; examine traffic segments first |
| D02 Conversion | 1,000 visitors / 100 transactions / 100,000 → 1,000 visitors / 80 transactions / 80,000 | Conversion rate 10% → 8%, difference −20,000; examine non-purchase, stockout, and service records first |
| D03 Average order value | 1,000 visitors / 100 transactions / 100,000 → 1,000 visitors / 100 transactions / 80,000 | Average order value 1,000 → 800, difference −20,000; examine category mix, items, discounts, and refunds first |
| D04 Multiple declines | 1,000 visitors / 100 transactions / 100,000 → 800 visitors / 64 transactions / 57,600 | The three differences are −20,000, −16,000, and −6,400, totaling −42,400; examine traffic first and list conversion and average order value separately |
| D05 Missing traffic | 100 transactions / 100,000 → 80 transactions / 80,000 | Average order value is unchanged and transactions fall; ask for traffic and units before distinguishing traffic from conversion |
| D06 Inconsistent definitions | 30 days of store visits → 20 days of visiting groups | Align the period and traffic definition first |
| D07 Zero denominator | Current period: 100 visitors / 0 transactions / 0 revenue | Conversion rate is 0 and average order value is undefined; examine non-conversion records first and retain calculable parts |
| D08 Corrected data | D02 current-period traffic is corrected to 800 visitors; everything else is unchanged | Conversion rate returns to 10%; switch to checking traffic first and replace the previous conversion-first action |
| D09 No gap | Both periods: 1,000 visitors / 100 transactions / 100,000, with no higher target | All three differences are 0; maintain and review the next comparable period |
| D10 Positive offset | 1,000 visitors / 100 transactions / 100,000 → 800 visitors / 80 transactions / 104,000 | Traffic −20,000, conversion 0, average order value +24,000; total +4,000. There is no gap for this question; list the offset |
| D11 Revenue only | 100,000 → 80,000 | Deliver the difference of −20,000 first, then ask for transactions and traffic in both periods |
| D12 Target supplied | Target: 1,000 visitors / 100 transactions / 100,000; actual: 800 visitors / 80 transactions / 80,000 | Difference −20,000; label target assumptions and examine traffic and the target's basis first |

Use MK-073-C07 to verify known-customer-group differences. If profitability is separately requested but only partial costs are supplied, list known costs, missing items, and calculable results, then revisit the index to select methods for the user's new task

## Method sources

Source file: 營業額提升主要關鍵（三）從數據來提升 ROI 的策略

Location: Five metrics

Source basis: extracted from course materials

Source URL: https://docs.google.com/presentation/d/1lwpCxF1cMgaK7Gnvngw8NzytDLYD8MK-p91g8dwSytU/edit

English translation of source excerpt:

> Five metrics

### Decision design for this revision

ThinkWithBlack developed "Required data and follow-up questions", "Decision branches", the investigation ranking of the three differences, review conditions, and D01–D12 cases for this free-edition Decision Model prototype. The fixed-order difference formulas are an arithmetic expansion of R=T×C×A by replacing variables one at a time. The original course's five-metric method is preserved in the sources above
