<h1>Understanding cohort analysis in Advanced KDP and Marketing Analytics</h1>

## You will learn

Learn about Klaviyo’s cohort analysis, including how to define a cohort and understand the data presented. The cohort analysis allows you to analyze the behavior of groups of profiles over time.

## Before you begin

[Advanced KDP](https://help.klaviyo.com/hc/en-us/articles/17655007276059) and [Marketing Analytics](https://help.klaviyo.com/hc/en-us/articles/33789259613595) are not included in Klaviyo’s standard marketing application, and a subscription is required to access the associated functionality.Head to our [billing guide](https://help.klaviyo.com/hc/en-us/articles/115000976672) to learn about how to purchase these plans.

## What is a cohort report?

A cohort report is a type of analysis that allows you to take a group of profiles with common characteristics (i.e., a cohort) and analyze their behavior over time. This allows you to identify trends and patterns in engagement, conversions, and other key metrics across their lifecycle.

## Create a cohort report

Take the following navigation steps to access the cohort report:

1. Select ****Advanced KDP**** or ****Marketing Analytics**** on the left-hand navigation in Klaviyo.
2. Select the ****Customer insights**** group.
3. On the **Customer insights** page, select the ****Cohort analysis**** tab.
4. Select an existing cohort analysis, or click ****Create cohort report**** to create your first analysis.
   ![prebuilt reports.jpg](https://klaviyo.zendesk.com/hc/article_attachments/33880690808475)

   Cohort analysis also includes 4 pre-built reports you can use to quickly start analyzing cohort performance. These include:
5. ****SMS consent to first order****
   Profiles who consented to SMS marketing before making their first purchase.
6. ****Repeat purchasers****
   Profiles who made repeat purchases month over month.
7. ****Post-purchase****
   Profiles who made at least 1 more purchase within a year after their first purchase.
8. ****Email consent to first order****
   Profiles who consented to email marketing before making their first purchase.

To create a cohort report from scratch, you’ll first need to define the cohort you want to analyze behavior over time for, as well as the behavior you want to measure. After selecting ****Create cohort report****, set the following information:

- ****Report name****
  Create a name for your cohort report.
- ****Description****
  An optional field to add a description for your cohort report.
- ****Cohorting event****
  This event defines what causes a user to enter the cohort and acts as a starting point for tracking user behavior over time. For example, setting **Placed Order** as the cohorting event will cause profiles to enter the cohort when they place their first order, and track their performance over time from that moment.
- ****Instance****
  This field defines which instance of the cohorting event should cause a profile to first enter the cohort being analyzed. The values for this field can be:
  - ****First in all event history****
    The first occurrence of this event over all time
  - ****First within the time period****
    The first occurrence of this event within a specific time period you define.
- ****Cohorting event filters****
  Set filters to limit the cohorting event to specific cases.
  - ****Cohorting event property****
    The event data you can use to filter the cohorting event to specific events. For example, if you set **Placed Order** as the cohorting event, you can use this field to filter the event so only purchases of specific products cause a profile to enter the cohort.
  - ****Cohorting report property relationship****
    The operator that defines the relationship between the cohorting event property and the value you define (e.g., is equal to, does not equal, starts with, etc.).
- ****Reporting event****
  This event defines the performance metric that will be measured over time for the cohort. For example, setting **Placed Order** as the reporting event will cause the report to track placed orders over time for the cohort.
- ****Reporting event filters****
  Set filters to limit the reporting event to specific cases.
  - ****Reporting event property****
    The event data you can use to filter the reporting event to specific events. For example, if you set **Placed Order** as the reporting event, you can use this field to filter the event so only purchases of specific products are measured over time.
  - ****Reporting property relationship****
    The operator that defines the relationship between the reporting event property and the value you define (e.g., is equal to, does not equal, starts with, etc.)

![](https://klaviyo.zendesk.com/hc/article_attachments/33799581899803)

## Using Klaviyo’s cohort report

The first column of your graph shows the dates for each cohort. Klaviyo will always display the last 12 calendar months (in this case February 2024 - January 2025).

![](https://klaviyo.zendesk.com/hc/article_attachments/33878700505243)

The second column, titled **Size**, displays the total number of profiles that engaged in this specific metric activity. In the example above, this cohort report shows the total number of profiles that performed a **Placed Order** event. You’ll notice that the report has blue highlights. The higher the value of each cohort, the darker the color will be. This helps you quickly identify the strongest and weakest performance of these cohorts over time for your given metric.

![size.jpg](https://klaviyo.zendesk.com/hc/article_attachments/33878848964635)

The third column, titled **0 mos,** shows the measure of the reporting event for the same month as the cohorting event. The subsequent numbered columns (labeled **1 mos** - **11 mos**) show the measure of the reporting event for each subsequent month.

![Untitled 2.jpg](https://klaviyo.zendesk.com/hc/article_attachments/33878724603291)

Additionally, you have access to the following settings to adjust the analysis.

![](https://klaviyo.zendesk.com/hc/article_attachments/33799581901851)

- ****Date range****
  The date range for which the reporting event will be measured.
- ****Time interval****
  The time interval between columns and rows in the cohort report (i.e., month or week).
- ****Measurement****
  The measurement for the reporting event being measured over time. This can be:
  - ****Conversions****
    The count of conversions based on the reporting event. You can view this as an average per profile, or as a total count.
  - ****Profiles****
    The number of profiles that performed the reporting event. You can view this number as a count, or as a percent of the original cohort.
  - ****Conversion value****
    The value of the conversions that occurred due to the reporting event. You can view this as the average value per profile, or as a total sum of all conversions.

    If using average as the measurement, the calculation is total count divided by the cohort size.
- ****View by****
  Define whether you’d like to see averages, totals, or percent represented in the cohort report. The available options vary based on the selected measurement. If using **Total**, there will be an additional row at the top of the cohort report that shows the sum of the values in the columns below.
- ****Trend on hover****
  Define the data that you’d like to see when hovering over a cell in the report. This can help you understand the value of a particular axis. Based on your selection, the axis in focus can be:
  - ****Horizontal****
    Hovering over a cell in the cohort report will highlight the row and show information about the reporting event analytics for the specific cohort in the row.
    ![horizontal hover.jpg](https://klaviyo.zendesk.com/hc/article_attachments/33800577699867)
  - ****Vertical****
    Hovering over a cell in the cohort report will highlight the column and show information about the reporting event analytics “after X months”.
    ![vertical hover.jpg](https://klaviyo.zendesk.com/hc/article_attachments/33800577704859)
  - ****Diagonal****
    Hovering over a cell in the cohort report will highlight the diagonal path and show information about the reporting event analytics for a specific calendar month or week.

![diagonal hover.jpg](https://klaviyo.zendesk.com/hc/article_attachments/33800586417435)

Klaviyo also uses color to represent the value of the measurement. Higher values have darker colors, while smaller values have lighter colors. This helps to make trends and changes in measured values easily identifiable.

## Understanding cohort report data

A cohort report can provide a number of different insights based on how you read it.

To demonstrate how to read the data in a cohort report, we’ll use the following report as an example:

![](https://klaviyo.zendesk.com/hc/article_attachments/33799581904027)

This cohort report requires customers to make a purchase to enter a cohort (i.e., the cohorting event) and tracks **Placed Order** events over time (i.e., the reporting event). It measures the count of conversions each month over the last 12 months.

The cohorting event itself is excluded from the month/week 0 column by default. To see the value associated with the cohorting event, select a revenue measurement (i.e., **Conversion value** or **Lifetime value**) and it will appear as an additional gray column next to **Size**.

### Reading the cohort report horizontally

By reading a cohort report horizontally, you can gain insights about behavior patterns over time for specific cohorts.

In the example, the first column in the cohort report (i.e., **Size**) shows the total number of customers that have made a first purchase in 2024. Each column after that shows the number of additional conversions that have occurred over time for each calendar month. As you read the report horizontally, you gain insights about repeat purchase rate over time.

![](https://klaviyo.zendesk.com/hc/article_attachments/33799572509339)

You can see that the sum of the cohorts has a total of 90,000 profiles across all months in 2024. The next column shows that after 0 months (i.e., the same calendar month as the first purchase causing profiles to enter the cohort), there were 62,000 conversions from this initial cohort. After 1 more month (i.e., the next column), this number increases to 75,000 conversions.

From this, you can learn that after an initial purchase, most repeat purchasers tend to make their next purchase the month after their initial purchase.

Note that when reading the **Total** row for cohort report, the number of cohorts included in the sum decreases with each column.

### Reading the cohort report vertically

By reading a cohort report vertically, you can learn how different cohorts perform at the same relative point in time (e.g., the repeat purchase rate 3 months after a first purchase for each cohort). This allows you to learn whether profile behavior changes over time across different cohorts.

In the example cohort report, you can see that as you go down the column, conversions increase. Looking at the 1 month column, you can see that the number of conversions increases for newer cohorts. This may indicate that towards the end of 2024, there may have been an event (e.g., new product launch or a marketing campaign) that drove this increase. Specifically, the August 2024 cohort saw a spike in the number of conversions (i.e., 18,000 conversions from 11,000 the previous month) compared to the July 2024 cohort at the same time (i.e., 5,000 conversions from 3,000 the previous month).

![](https://klaviyo.zendesk.com/hc/article_attachments/33799572511003)

### Reading the cohort report diagonally

By reading a cohort report diagonally, you can track performance across cohorts at the same absolute point in time, or at different lifecycle stages (e.g., the repeat purchase rate in a specific month).

![](https://klaviyo.zendesk.com/hc/article_attachments/33799572512667)

Look at the example cohort report starting from the **0 month** column for the October 2024 cohort. As you go up-right diagonally from this starting point, you can see the number of conversions in October 2024 for each cohort. During this time, each of the cohorts is at a different point in their lifecycle.

In this case, there is an increase in conversions for most cohorts compared to the previous month. This indicates that there may have been an event in October 2024 that caused an increase in conversions for most cohorts. Perhaps October is when customers begin their holiday shopping. Conversely, if there was a consistent decrease in conversions for most cohorts compared to the previous month, this may indicate there are external factors (e.g., a downturn in the economy) that affected all profiles at the same time.
