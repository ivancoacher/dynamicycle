---
id: "360046234772"
title: "How to build a multi-metric report"
source_url: "https://help.klaviyo.com/hc/en-us/articles/360046234772-How-to-build-a-multi-metric-report"
section: "Build and use custom reports"
category: "Analytics"
category_slug: "analytics-audience"
klaviyo_updated: "2026-04-21T13:54:48Z"
language: "en"
---
## You will learn

Learn more about the multi-metric report and how to customize it to suit your business and marketing performance needs in one, unified report. You can customize this report to account for your desired timeframe, properties, and groupings.

The multi-metric Report helps you answer questions like:

- What do my key business KPIs over the last quarter look like?
- What do my key business metrics look like over the last month, attributed only to email campaigns?
- How are men versus women converting from cart to purchase, and who is spending more per order on average?

In this guide, you will learn more about what the multi-metric report offers and where to find it in Klaviyo.

## Build your report

1. To create a new multi-metric report, navigate to the ****Analytics >**** ****Custom Reports****.
2. Then, either browse our library of prebuilt reports or click ****Create from scratch****.

![Custom reports section inside of the Analytics tab](https://klaviyo.zendesk.com/hc/article_attachments/28713337634331)

3. Under **Report Type**, select ****Multi-Metric Report**** from the dropdown, and give your report a name.

![New repot with report type dropdown open and report name field to enter name of report](https://klaviyo.zendesk.com/hc/article_attachments/28713337640219)

4. You will be able to configure your report by selecting up to 10 different Metrics to report on. You can select any standard metric available in your account as well as select calculated metrics like certain rates (e.g., **Open Rate**). To add an additional metric, select ****+ Add Metric****.

![Inside a report, customize it by choosing from metrics like opens, clicks, checkout started, placed order, etc. by using +Add Metric button](https://klaviyo.zendesk.com/hc/article_attachments/28713331949211)

5. Next, decide how you want to analyze these metrics. All standard metrics support two different dropdowns to customize your analysis. Choose one of the values from the applicable dropdown menu.

- ****Total, Unique, or Value****
  You can report on the total number of instances of an event (TOTAL) or the unique number of profiles that performed that event (UNIQUE). If the metric you select has a monetary value associated with it (e.g., Placed Order), you can also report on the value of the events (VALUE).
- ****SUM or AVG****
  You can choose one of two aggregations: SUM or AVG. SUM shows you the total of all events for your selected metric. For example, if there are two Placed Order events within the timespan you select, both with a $15 value, the VALUE SUM will be $30 and the TOTAL SUM will be 2. AVG shows the average of events that occurred for your metric. For example, if there are two Placed Order events within the timespan you select, both with a value of $15, the average will be $15.

6. You can also add a modifier to group by specific values. This allows you to build a more tailored report around your selected metrics, specific to your business needs. Choose an additional grouping by clicking ****+Add Group By**** and select your property of ****Product Name.****

- ****Add Group By****
  This option allows you to group values within your report by a specific property. You can then add a filter on top of this to make your grouping even more precise. You can group your reports by both email attribution and profile property data. Grouping and filtering by [metric event properties](https://developers.klaviyo.com/en/v1-2/docs/introduction-to-klaviyos-data-model) are not possible in this report, as the different metrics you select will all have different related detailed event data. Also, reports only include events filtered by a profile property starting after that property was created. Even if a property was retroactively applied, if it didn’t exist on profiles at the time the event takes place then it won't appear in the report.

  For example, you can group a multi-metric report to see a breakdown of how your revenue changes for a given month across flows and campaigns. Alternatively, group by **Product Name** to see how this differs by product. To do so, select ****+Add Group By**** and select your property of ****Product Name****.

  ![Inside a report, add filter to group by like product name by using +Add Filter button](https://klaviyo.zendesk.com/hc/article_attachments/28713337622171)

  For more information on properties you can use for grouping, head to our [Guide to Properties](https://klaviyo.zendesk.com/hc/en-us/articles/115005074627).

7. You can also add a modifier to filter your report by specific values. Choose an additional grouping by clicking ****+ Add Filter**** to set this up****.****

- ****Add Filter****
  Instead of grouping your report by specific attribution or profile properties, you can instead choose to limit your results by filtering what data is included. For example, if you only want to report on performance for a specific gender, you can add this as a filter.

  If you want to be more exclusive, and limit to activity that meets several different criteria, you can add subsequent filters. These will all appear separated by the AND connector. At this time, it is not possible to report on a cross-section of filters separated by the or connector. For example, you can report on all orders placed by those whose **Gender equals Female** AND whose **Country equals United States**. However, you cannot view activity only for those whose **Gender equals Female** OR whose **Country equals United States**. This is true for event data sent in an array like **Collections** as well.

  For more information on the distinction between AND and OR, head to our [AND vs. OR Guide](https://klaviyo.zendesk.com/hc/en-us/articles/360036534631).

8. Finally, customize the time range of your report so that it only shows the data you care about. To adjust the timeframe, choose your selected time range and grouping from the associated dropdowns.

![Inside a report, customize the timeframe by choosing from the dropdowns for time period and grouping by](https://klaviyo.zendesk.com/hc/article_attachments/28713331933467)

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

1. After you configure a new report, the next step is to click ****Run Report**** to generate your results. A results summary will appear for you to review, and you can choose to export these results for further analysis.

![Example of a multi-metric report with name, configured metrics, and timeframe chosen, with button for Run Report below](https://klaviyo.zendesk.com/hc/article_attachments/28713331940123)

While it may take some time to generate your results, you will see a robust summary of your report populate as soon as your data is ready for analysis. If you don’t want to wait, we will notify you with an in-app notification and email when your results are ready.

All of your previously run reports will be automatically saved in your Custom Analytics page. It is not possible to save a partially configured report, but every report will be automatically saved after the first time it is run. When you navigate into an existing report, a timestamp of when the report was last run will appear above your results along with an Export button.
2. To export the results of your report for further analysis, simply click ****Export****.

![After a Custom Report has run, click the Export button in the top right to download and export results](https://klaviyo.zendesk.com/hc/article_attachments/28713337628315)

### Schedule your report

You also have the option to schedule a report to auto-run at a specific date and time and be notified via email when your results are ready. This way, you can set up your reports to automatically run and pull data for your review instead of manually exporting them.

Head to our guide on [How to Schedule Custom Reports](https://help.klaviyo.com/hc/en-us/articles/4407838420123) and learn how to set this up for your reports.

## Update report results

Reports do not automatically refresh with data over time if you are using a relative timeframe such as **Last 30 Days**.

1. To see when report results were last generated for a given report, look at the **Last Run** timestamp from either the Analytics tab or from within the report itself.
2. If you want to update your report results to pull in fresh data, navigate into the report and click ****Run Report**** again.
3. In the event that you need to see historical report results from previous runs, go to ****Custom Reports**** and click ****More****.4. Then choose ****View History**** from the dropdown menu.

![On the Custom Analytics list page, clicking on the More dropdown to the right of the analytics name will expose the View History option](https://klaviyo.zendesk.com/hc/article_attachments/39543071632667)

This will show all historical runs for your report of interest.
5. To download the historical results of your report, select ****Export****.

![To download all historically run reports, click export to the right of a given report](https://klaviyo.zendesk.com/hc/article_attachments/28713337630235)

## Clone and rename reports

If you have an existing report that you would like to copy, use the clone option.

1. To clone a report, go to ****Custom Reports**** and find the report that you want to clone.
2. To the right of the report, click ****More****.3. Then choose ****Clone Report**** from the dropdown menu.
![Report inside custom reports list, with More dropdown open and clone report chosen](https://klaviyo.zendesk.com/hc/article_attachments/28713331980827)
Once you clone your report, you will see a new report appear at the top of your **Custom Reports** list named "Copy of **your original report name**.

![Example of a cloned report that appears at top of your custom reports list with 'Copy' and name of report](https://klaviyo.zendesk.com/hc/article_attachments/28713337651611)

Note that cloned reports do not include scheduling preferences from the original report. If you would like to schedule your copied report to deliver to you on a regular cadence, head to our guide on [How to Schedule Custom Reports](https://help.klaviyo.com/hc/en-us/articles/4407838420123).
4. If you would also like to rename your cloned report, navigate to the right of the report and click ****More****, then choose ****Edit Name**** from the dropdown menu.

![Copy report inside custom reports list, with More dropdown open and Edit Name chosen](https://klaviyo.zendesk.com/hc/article_attachments/28713331999003)

5. Rename your report in the modal that appears.
6. Once you have renamed your report, click ****Save****.

![Edit report name modal with field for report name and Save button below](https://klaviyo.zendesk.com/hc/article_attachments/28713337664795)

## Additional resources

- [Understanding custom reports in Klaviyo](https://klaviyo.zendesk.com/hc/en-us/articles/360047725651)
- [How to build a single metric deep dive report](https://klaviyo.zendesk.com/hc/en-us/articles/360046242952)
- [Getting started with reporting](https://klaviyo.zendesk.com/hc/en-us/articles/360047399472)
- [How to build a custom report strategy](https://klaviyo.zendesk.com/hc/en-us/articles/360046757411)