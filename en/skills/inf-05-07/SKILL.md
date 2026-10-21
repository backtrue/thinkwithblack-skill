---
name: inf-05-07
description: "Calculate the repeat-purchase interval, mean, and median for a specified cohort using customer identifiers and valid order dates. Use for questions about the average days between first and second orders across five years of records or how to calculate this in a spreadsheet; perform the measurement directly"
---

# INF-05-07 | Repeat-purchase interval calculation

For a regular chat, upload `packs/inf-05-07.md`. It includes the shared rules, this method, and required references

## Purpose

This skill delivers: **Repeat-purchase interval**

This document specifies the data requirements and method. It does not establish that any account is connected or has been read. Identify any missing capability, authorization, or data explicitly; do not assume platform capabilities or completion

## Required inputs

Required data: an order table (CSV or spreadsheet) containing customer identifiers, unique order IDs, valid payment timestamps, and cancellation/refund/test statuses, and state the historical coverage and time zone

## Method

1. Check the data's historical coverage, customer key, order uniqueness, and valid-order rules
2. Group valid orders by customer and sort them; select only each customer's first and second valid orders
3. Calculate the interval between the first two orders, then calculate the mean using the number of eligible customers as the denominator, following the supplementary formulas below
4. Deliver the valid sample size, mean and median, counts of customers without a repeat purchase and with unknown histories, preserving the data period and calculation basis

## Calculations and interpretation

Original permission mode: read. Execute dependencies only when needed for this task; connecting every platform in advance is not required

## Required output fields

| Order | Field | How to complete |
|---:|---|---|
| 1 | Cohort | Use source evidence, an intermediate method result, or an explicit unknown; do not invent information |
| 2 | Interval definition | Use source evidence, an intermediate method result, or an explicit unknown; do not invent information |
| 3 | Valid sample | Use source evidence, an intermediate method result, or an explicit unknown; do not invent information |
| 4 | Mean/median | Use source evidence, an intermediate method result, or an explicit unknown; do not invent information |
| 5 | Customers without a repeat purchase | Use source evidence, an intermediate method result, or an explicit unknown; do not invent information |
| 6 | Observation period | Use source evidence, an intermediate method result, or an explicit unknown; do not invent information |

## Activation conditions and full question scope

Use this skill directly when the user wants to calculate repeat-purchase intervals, the mean interval between the first and second valid orders, or asks whether an app or spreadsheet can produce that number. The [Q028 original question and author's clarification](https://www.reddit.com/r/shopify/comments/18optr5/how_do_you_find_average_time_between_orders/) specify five years of customer and order records. An app and a spreadsheet are alternative approaches; a spreadsheet method is sufficient, and both are not required

Clean and calculate from the data obtained for this task

Preserve the original population: all customers whose first and second valid orders can be verified (F2+). Include customers with three or more purchases, but count only the first-to-second interval once per customer. A population of customers with exactly two orders applies only when the user explicitly requests it. The first order observed in a five-year window is not necessarily a customer's lifetime first purchase. Check complete history, customer keys, unique orders, valid payment timestamps, time zones, and cancellation/refund/test rules first. Report unknown histories separately; deduplicate line items by order before calculation. Distinct valid orders on the same day may have a zero-day interval

### Spreadsheet implementation example

This example implements the method's cohorts, intervals, and mean in spreadsheet cells. Preserve the raw data. On another sheet, arrange valid orders with confirmed complete history and stable customer keys, one row per order: A customer key, B numeric valid payment date or time, C unique order key. Normalize the case and data type of customer keys and exclude blank or missing keys; use a consistent time zone and day-count definition. Sort the entire table in ascending order by A, then B, then C before entering formulas. Re-sort and refill formulas whenever the data changes

Column D is the order sequence within each customer: enter `=1` in D2 and `=IF(A3=A2,D2+1,1)` in D3, then fill D3 down to the final record

Column E calculates the first-to-second interval in days only on the second order: leave E2 blank, enter `=IF(D3=2,B3-B2,"")` in E3, and fill E3 down to the final record. Do not enter 0 for third or later orders or customers with only one order; retain genuine zero-day intervals between two same-day orders. If B includes times, the result is days with a fractional component. Convert all dates to calendar dates in the same time zone first only when using calendar days

For example, if the data ends at row 1000, the valid customer count is `=COUNT(E2:E1000)` and the mean is `=IF(COUNT(E2:E1000)=0,"No valid second-purchase sample",AVERAGE(E2:E1000))`. Replace 1000 with the actual final row so no rows are omitted. The denominator of the mean is valid customers, not orders. Count customers without a repeat purchase separately from those with only one valid order; do not treat blank interval rows as the number of customers without a repeat purchase

[Microsoft IF](https://support.microsoft.com/en-us/excel/functions/if-function) explains conditional output; [Microsoft AVERAGE](https://support.microsoft.com/en-us/excel/functions/average-function) explains that text and blanks are ignored while numeric zeros are retained. These formulas implement the method's calculations; they do not confirm a native Shopify report or an app capability

When raw data is missing, deliver the cohort, interval, formulas, observation window, and missing inputs; leave the valid sample, mean/median, and number without a repeat purchase unknown. If the question is solely about app selection or native features, verify those capabilities separately. Email is usage context; measurement does not automatically generate welcome messages, fixed contact dates, or causal claims about results

### Median and verification

Using the valid first-to-second intervals in column E, calculate median with `=IF(COUNT(E2:E1000)=0,"No valid repeat-purchase sample",MEDIAN(E2:E1000))`. Replace 1000 with the actual last row, retain genuine zero-day intervals and exclude blanks

Check: intervals 0, 10 and 50 give count 3, mean 20 and median 10; no valid intervals produce the no-sample message for both mean and median

## Method sources

Source file: marketing_skill_master_v1_4.xlsx／前置技能目錄
Location: INF-05-07
Source basis: V1 infrastructure planning / approved entry specification
English translation of source excerpt:
> Calculate mean/median days to repeat purchase
