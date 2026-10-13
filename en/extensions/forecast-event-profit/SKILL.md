---
name: forecast-event-profit
description: "Use historical campaigns and a recent baseline to estimate promotional CPM, conversion rate, and average order value, building ad-budget, revenue, and contribution-profit scenarios with backtesting. Use for campaign forecasting such as Black Friday and modeling instruction; use the existing sensitivity method for sensitivity comparisons involving only supplied values"
---

# Campaign Budget and Profit Forecasting

For ordinary chat, upload `packs/forecast-event-profit.md`, which includes the shared rules, this method, and required references

## Required inputs

Upload impressions, ad spend, outbound clicks, sessions, paid orders, net revenue, and costs for historical campaigns, their pre-campaign baselines, and a recent baseline, including periods, products / offers, and currency. Also provide candidate budgets, target profit, inventory / fulfillment capacity, and an affordable ceiling; teaching questions may start with tables using explicit assumptions

Use the course materials' costs, break-even, and traffic × conversion rate × average order value as the core, adding historical comparisons, drivers, backtesting, and updates from actual results. See [sources.md](references/sources.md) for sources and how this method derives from them

## Deliver an outcome that fits the question first

For questions about modeling, directly provide fillable worksheet fields, formulas, value-selection methods, example sources, and interpretation; label demonstration numbers as assumptions. Leave data-specific blanks only when asked to calculate actual amounts for the store. Retain the user's period, revenue, and profit requirements

## 1. Fix the definitions and basis

For each data item, record the source, extraction date, campaign window, comparison window, platform, market, currency, objective, product / offer, attribution, and refund maturity time. Align windows by campaign-relative day, weekday, and length; record differences individually rather than treating conditions as identical

Divide aggregated numerators by denominators instead of averaging daily rates: CPM＝ad spend÷impressions×1000; outbound click-through rate＝outbound clicks÷impressions; arrival factor＝corresponding sessions÷outbound clicks; CVR＝corresponding paid orders÷sessions; AOV＝net revenue from the same order cohort÷order count. The arrival factor may exceed 1 because of session definitions; first verify tracking and observation windows

For zero or missing denominators, record the reason instead of entering 0. If platform-reported purchases and on-site orders use different definitions, model them separately; allocate cross-channel revenue from deduplicated orders rather than summing all revenue each platform attributes to itself

## 2. Estimate future metrics

First list the recent comparable baseline, then create “that year's campaign value÷that year's pre-campaign baseline” multipliers for each comparable historical campaign, retaining original numerators, denominators, and event year. Calculate them separately for CPM, CVR, and AOV; do not use multipliers when the baseline is zero

Apply all three multipliers from one year together to the three recent baselines to form one historical-analogy estimate. List historical combinations separately; do not independently select the lowest CPM, highest CVR, and highest AOV to assemble an apparently real best year. With only one comparable history, provide one analogy and separately stated stress assumptions, rather than calling them a statistical interval or assigning scenario probabilities

With multiple historical sets, select the main scenario using comparability conditions recorded in advance, showing the other complete combinations as a range of results. If data is sparse and no clear priority conditions exist, list them side by side rather than choosing inputs backward from desired profit. This is a backtestable historical-analogy baseline; list assumptions and evidence separately for additional budget or changes in audience or auction structure

Calculate CVR separately for necessary channels or new / returning customer groups, then weight it by estimated traffic; provide traffic-share scenarios if future shares are unknown. If products or offers changed, recalculate AOV from discounted net revenue of representative order bundles and estimated order shares, and separately calculate variable costs for each bundle. Support shares with history or known orders; mark unknown shares as assumptions. Bundle shares must sum to 1; do not use the average of item prices as average order value. Do not apply historical offer multipliers again to offer effects already recalculated

Without comparable history, deliver assumption sensitivity, locations to obtain data, and update methods. If citing market data, retain its period, market, and sample and account for differences in interpretation; do not call it a forecast for this store. Determine whether CPM rises from the estimates, rather than inheriting the question's premise

## 3. Check historical forecasting ability

With multiple historical periods, hold out a later period chronologically and estimate it using the exact same rules and only earlier data and pre-campaign baselines available at the time. Retain the forecast creation date or availability time; future actual results must not enter multiplier selection, bundle weights, or baselines

For revenue backtests, also lock the planned budget, outbound click-through rate, and arrival factor in advance. If recalculating afterward using actual ad spend, list that separately as a conditional comparison at actual investment and retain the original forecast. Calculate errors separately for the two results

Compare both “carry the recent baseline forward” and the historical analogy, providing forecasts, actuals, signed errors, and absolute errors for CPM, CVR, AOV, and revenue in each period. When actuals are 0, omit percentage errors but retain absolute errors. Also provide CVR differences in percentage points to avoid confusing relative changes with percentage points

If there is only one campaign and no earlier campaign for training, record that no holdout backtest exists; an in-sample fit is not validation. If the analogy does not outperform the baseline, deliver the comparison and use the better-supported baseline or parallel scenarios without claiming forecast improvement

## 4. Connect forecasts to budget and profit

Use the full chain for every scenario: impressions＝budget÷CPM×1000; outbound clicks＝impressions×outbound click-through rate; sessions＝clicks×arrival factor; orders＝sessions×CVR; revenue＝orders×AOV. Without click-through rate or arrival factor, CPM cannot directly yield sales; list the missing inputs, or use the clicks＝budget÷CPC branch when CPC on the same basis is available

Division is undefined when CPM / CPC is zero; stop that branch. When CVR is zero, forward-calculated orders are zero; leave undefined AOV fillable instead of replacing it with zero. ROAS is undefined when ad spend is zero; provide revenue and expense details directly. For negative budget, CPM / CPC, click-through rate, arrival factor, or CVR, recheck data and definitions first. For negative net revenue, separately check refund assignment; do not use it as an ordinary positive AOV for reverse target calculations. Spreadsheets must not use IFERROR(...,0) to turn missing inputs or undefined formulas into zero

Contribution per order＝net revenue−remaining variable costs for products, payments, logistics, packaging, channels, and similar items. When ad spend is listed separately, other variable costs exclude it; count each discount, refund, tax, and shipping charge once according to its definition

Campaign contribution＝sum of contributions from all order groups−ad spend; only after deducting the period's fixed costs may it be called profit for this cost scope. Revenue÷ad spend is ROAS; define investment and returns before presenting ROI, and do not label ROAS as ROI

When listing break-even ROAS, specify included costs. With pre-ad contribution margin ratio m, ad spend B, and other fixed costs F, and m and B both greater than 0: the threshold covering only ad spend＝1÷m; the threshold including the period's fixed costs＝(F+B)÷(m×B). Use the supplied cost definitions; compare other cost assumptions in separate scenarios while keeping the original question's result on its original basis

With fixed ad budget B, other fixed costs F, pre-ad contribution margin ratio m, and target profit P, required revenue＝(F+B+P)÷m, where m must exceed 0. Then use AOV and CVR to work backward to orders and sessions and compare with the forward forecast. Explain which metric creates the gap; do not treat the target as a forecast

Reverse calculations for a positive revenue target require positive AOV and CVR; if either is zero, record that current conditions cannot meet the target; for missing values, obtain their sources. Round actual whole-order targets upward, recalculate required sessions from that integer, and round sessions upward as well. List expected values separately from integer execution targets

Compare candidate budgets within the user's affordable range, showing each input set and profit; do not label a linear extrapolation at fixed efficiency as the optimal budget. Retain scaling assumptions for candidates outside historical spending ranges. Interpret results alongside inventory, fulfillment capacity, and the maximum affordable loss; if limits are missing, provide conditional choices

## 5. Delivery and updates

Deliver a workbook or equivalent copyable tables: historical raw data, definitions and assumptions, estimates and backtests, and budget / revenue / profit scenarios. Every result must trace back to a formula and source. In ordinary chat, provide copyable tables users can place in Excel or Google Sheets

When asked about others' practices, actually read the original comments, provide their self-reported workflows and direct links, and distinguish cases with public spreadsheets from descriptions alone. See sources.md for the two Q044 sources

Finish with budget decisions possible now, missing data, and corresponding cells. When the user uploads actual results on the same basis again, update the remaining-period forecast while retaining the prior version and reasons for changes; mark immature refund or attribution values as provisional. After delivery, wait for the next question
