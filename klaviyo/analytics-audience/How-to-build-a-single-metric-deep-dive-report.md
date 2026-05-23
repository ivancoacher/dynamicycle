---
id: 360046242952
title: "How to build a single metric deep dive report"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360046242952-How-to-build-a-single-metric-deep-dive-report"
section: "Build and use custom reports"
category: "Analytics"
category_slug: "analytics-audience"
klaviyo_updated: "2026-04-21T13:54:48Z"
language: en
---

## You will learn

Learn how to use the single metric deep dive report to get metric data for either a broad overview of activities or to understand trends by key event or [profile properties](https://klaviyo.zendesk.com/hc/en-us/articles/115005074627). You can choose any metric in your account to build a report around and can further customize it by selecting different timeframes, properties, and groupings.

The single metric report can you help you answer questions like:

- What was my revenue breakdown by product collection over the last year?
- How has my checkout value changed over the last 90 days?
- How has order volume compared across different loyalty tiers over the last quarter?

In this guide, you will learn more about what the Single Metric Deep Dive Report entails, where to find it in Klaviyo, and how to configure it to meet your reporting goals.

## Build your report

1. To create a new Single Metric Deep Dive Report, navigate to the ****Analytics**** ****>**** ****Custom Reports****.
2. Then, either browse our library of prebuilt reports or click ****Create from scratch****.

![Inside of the analytics tab showing the custom reports section](https://klaviyo.zendesk.com/hc/article_attachments/28722596039707)

3. Under **Report Type**, select ****Single Metric Deep Dive Report**** from the dropdown, and give your report a name.

![Inside a new report with options for report type in dropdown and field for report name to the left](https://klaviyo.zendesk.com/hc/article_attachments/28722596047771)

4. Then, choose a metric to report on. From the designated dropdown, you can select any standard metric available in your account including select calculated metrics, like rates (e.g.,**Open Rate**). In the example below, **Placed Order** is the selected metric.

![Inside a metric report with option at top to choose property to report on and grouping to sort by below](https://klaviyo.zendesk.com/hc/article_attachments/28722596024603)

5. Next, decide how you want to analyze the metric. All standard metrics support two different dropdowns to customize your analysis:

- ******Total**, **Unique**, or **Value******
  You can report on the total number of instances of an event (**TOTAL**) or the unique number of profiles that performed that event (**UNIQUE**). If the metric you select has a monetary value associated with it (e.g., **Placed Order**), you can also report on the value of the events (**VALUE**).
- ******SUM** or **AVG******
  You can choose one of two aggregations: SUM or AVG. SUM shows you the total of all events for your selected metric. For example, if there are two Placed Order events within the timespan you select, both with a $15 value, the VALUE SUM will be $30 and the TOTAL SUM will be 2. AVG shows the average of events that occurred for your metric. For example, if there are two **Placed Order** events within the timespan you select, both with a value of $15, the average will be $15.

6. Finally, you can add a modifier to group and filter your report by specific values. This allows you to build a more tailored report around your selected metrics, specific to your business needs.

- ****Add a grouping****

  You can group values within your report by a specific property. You can then add a filter on top of this to make your grouping even more precise. Klaviyo lets you group your reports by both event data and profile property data. Note that reports only include events filtered by a profile property starting after that property was created. Even if a property was retroactively applied, if it didn’t exist on profiles at the time the event takes place then it won't appear in the report.

  For example, you can group your **Placed Order** report data **Collection**, to compare how different collections perform. To do so, select ****+Add Group By**** and select your property for **Collection**. Then, you can then optionally select ****+ Add Filter**** and restrict your report to only look at a subset of values. In the image below, we’ve limited our **Placed Order** report to only show us data for two key collections: Klaviyo T-Shirts and Women’s items.

  ![Inside a metric report with option at top to choose property and grouping to sort by below with examples women's shirt grouping](https://klaviyo.zendesk.com/hc/article_attachments/28722596029083)

  For more information on properties that you can use for grouping, head to our [Guide to Properties](https://klaviyo.zendesk.com/hc/en-us/articles/115005074627).
- ****Add a filter****
  Instead of grouping your report by specific attribution or profile properties, you can instead choose to limit your results by filtering what data is included. For example, if you only want to report on performance for a specific gender, select ****+ Add Filter**** to set this up.

  If you want to be more exclusive, and limit to activity that meets several different criteria, you can add subsequent filters. These will all appear separated by the AND connector. At this time, it is not possible to report on a cross-section of filters separated by the OR connector. For example, you can report on all orders placed by those whose **Gender equals Female** AND whose **City equals Boston**. However, you cannot view activity only for those whose **Gender equals Female** OR whose **Country equals Boston**. This is true for event data sent in an array like **Collections** as well.

  ![](https://klaviyo.zendesk.com/hc/article_attachments/39543381539611)

  For more information on the distinction between AND and OR, head to our [AND vs. OR Guide](https://klaviyo.zendesk.com/hc/en-us/articles/360036534631).

### Customize by timeframe

By customizing the time range of your report, you can restrict the report so that it only shows the data you care about.

1. To adjust the timeframe, choose your selected time range and grouping from the associated dropdowns.

![Inside a Custom report, you can customize by a timeframe dropdown for range and grouping of dates](https://klaviyo.zendesk.com/hc/article_attachments/28722596027419)

You can adjust the time range to:

- Today
- Last 24 Hours
- Yesterday
- This Week
- Last 7 Days
- Last Week
- This Month
- Last 30 Days
- Last Month
- This Year
- Last 90 Days
- Last 365 Days
- Last Year
- Custom

You can also group the data by:

- Daily
- Weekly
- Monthly
- Yearly

Note that timestamp data within your reports, including exported reports, will display in your [account's local time](https://help.klaviyo.com/hc/en-us/articles/115005232388) from your settings. Additionally, if you are using custom date ranges, the maximum time range is 2 years. If you attempt to create a report with over 2 worth of data, an error will appear.

## Run and export your report

1. After configuring your report, click ****Run Report**** to generate your results. A results summary will appear for you to review, and you can choose to export these results for further analysis.

![Inside report with single metric report type, example report name, placed order metric, and timeframe of last year and run report button below](https://klaviyo.zendesk.com/hc/article_attachments/28722596051227)

While it may take some time to generate your results, you will see a robust summary of your report populate as soon as your data is ready for analysis. If you don’t want to wait, we will notify you with an in-app notification and email when your results are ready.

All of your previously run reports will be automatically saved in your Custom Analytics page. It is not possible to save a partially configured report, but every report will be automatically saved after the first time it is run. When you navigate into an existing report, a timestamp of when the report was last run will appear above your results along with an Export button.

2. To export the results of your report for further analysis, click  ****Export,**** as shown in the top right in the example below.

![New run single metric report with results below and export button in upper right](https://klaviyo.zendesk.com/hc/article_attachments/28722596053147)

### Schedule your report

You also have the option to schedule a report to auto-run at a specific date and time and be notified via email when your results are ready. This way, you can set up your reports to automatically run and pull data for your review instead of manually exporting them.

Head to our guide on [How to Schedule Custom Reports](https://help.klaviyo.com/hc/en-us/articles/4407838420123) and learn how to set this up for your reports.

## Update report results

Reports do not automatically refresh with data over time if you are using a relative timeframe such as **Last 30 Days**. To see when report results were last generated for a given report, look at the **Last Run** timestamp from either the Analytics tab or from within the report itself.

1. If you want to update your report results to pull in fresh data, navigate into the report and click ****Run Report**** again.
2. In the event that you need to see historical report results from previous runs, go to ****Custom Reports.****3. Click ****More**** and then choose ****View History**** from the dropdown menu.

![On the Custom Analytics list page, clicking on the More dropdown to the right of the analytics name will expose the View History option](https://klaviyo.zendesk.com/hc/article_attachments/28722557630875)

This will show all historical runs for your report of interest.
4. To download the historical results of your report, select ****Export****.

![Inside a custom report history, there will be listing of all reports ever run with the ability to export again by clicking on export the right of a report.](https://klaviyo.zendesk.com/hc/article_attachments/28722596035739)

## Clone and rename reports

If you have an existing report that you would like to copy, use the clone option.

1. To clone a report, go to ****Custom Reports**** and find the report that you want to clone.
2. To the right of the report, click ****More****.3. Then choose ****Clone Report**** from the dropdown menu.
![Inside reports view with more dropdown opened from top menu and clone report chosen](https://klaviyo.zendesk.com/hc/article_attachments/28722557648667)
Once you clone your report, you will see a new report appear at the top of your **Custom Reports** list named "Copy of your original report name."

![Example inside Custom reports with copy of your report highlighted at top of list below](https://klaviyo.zendesk.com/hc/article_attachments/28722596060571)

Note that cloned reports do not include scheduling preferences from the original report. If you would like to schedule your copied report to deliver to you on a regular cadence, head to our guide on [How to Schedule Custom Reports](https://help.klaviyo.com/hc/en-us/articles/4407838420123).
4. If you would also like to rename your cloned report, navigate to the right of the report and click ****More****.5. Then choose ****Edit Name**** from the dropdown menu.

![Inside reports view with more dropdown opened from top menu and edit name chosen](https://klaviyo.zendesk.com/hc/article_attachments/28722596063899)

6. Rename your report in the modal that appears. Once you have renamed your report, click ****Save****.

![Edit report name modal with name of your report in dropdown and Save button below](https://klaviyo.zendesk.com/hc/article_attachments/28722596068251)

## Additional resources

- [About custom reports in Klaviyo](https://klaviyo.zendesk.com/hc/en-us/articles/360047725651)
- [Getting started with reporting](https://klaviyo.zendesk.com/hc/en-us/articles/360047399472)
- [How to build a multi-metric report](https://klaviyo.zendesk.com/hc/en-us/articles/360046234772)
- [Guide to building a custom report strategy](https://klaviyo.zendesk.com/hc/en-us/articles/360046757411)