---
id: 360047022912
title: "How to build a campaign performance report"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360047022912-How-to-build-a-campaign-performance-report"
section: "Build and use custom reports"
category: "Analytics"
category_slug: "analytics-audience"
klaviyo_updated: "2026-04-21T13:54:49Z"
language: en
---

## You will learn

Learn more about the campaign performance report, where to find it in Klaviyo, and how to customize it to better serve your business. The campaign performance report lets you deep dive into campaign-specific engagement and conversion data. This reports helps you get up and running quickly by providing a pre-made report that includes all standard engagement and deliverability metrics neatly grouped by campaign name. Tailor it to your needs by customizing the metrics you want to analyze and focusing that analysis using tags and time range filters.

The campaign performance report can help you answer questions like:

- How have my product launch campaigns performed over the last year?
- What does my conversion funnel look like for campaigns sent over the last 90 days compared across different conversion metrics, including attributed site visits, checkouts, and purchases?

## Build your report

1. Navigate to ****Analytics********> Custom Reports****.
2. Then, either browse our library of prebuilt reports or click ****Create from scratch****.

![View of Custom Reports list page with buttons at top left to create own report or button at top right to go into the Reports Library](https://klaviyo.zendesk.com/hc/article_attachments/28711698975515)

3. Under **Report Type**, select ****Campaign Performance Report**** from the dropdown.
4. Give your report a name.

![Inside a new Custom created report with option to choose type of report on left and ability to name on right](https://klaviyo.zendesk.com/hc/article_attachments/28711698957723)

### Customizing your report

From there, customize your report to best serve your business needs. By default, the report is pre-populated with the standard deliverability and engagement metrics related to your channels in Klaviyo. If you employ both SMS and email, you will see both SMS and email metrics appear.

![View of the campaign performance with filters chosen and SMS and email chosen as channesl by default](https://klaviyo.zendesk.com/hc/article_attachments/28711698986395)

1. Choose what metrics you want to analyze in your report, adding to or removing from the automated selection. If any pre-populated metric is irrelevant to your needs, remove it by clicking the ****X**** to the right of the metric’s name.
For example, to view only SMS performance, you will need to remove all email metrics. To re-add any of these defaults, simply click within the gray box and reselect them from the dropdown.

You may also add up to 10 conversion metrics in addition to the pre-populated set that comes with the report. This includes both standard conversion metrics (e.g., **Placed Order**) and conversion rates (e.g., **Placed Order Rate**) that are attributable to your messaging.

Note that **SMS ROI, SMS Usage, and SMS Spend** is only available starting on October 1, 2025. **SMS ROI and SMS Spend** are only available for non-contracted SMS customers, contracted SMS customers will see 0's for all theseflow metrics for all time periods periods. SMS ROI Is computed using attributed revenue from the [mapped revenue metric](https://klaviyo.zendesk.com/hc/en-us/articles/25829057055899).

2. Select ****+ Add Conversion Metric**** to add these parameters to your analysis.

![Inside a Campaign Flow Report showing the ability to add additional Conversion Metrics like Placed Order](https://klaviyo.zendesk.com/hc/article_attachments/28711677526811)

3. Once you have customized your report and added your desired conversion metric, the next step is to decide how you want to analyze those conversion metrics. With the exception of rates, all conversion metrics support two different dropdowns to customize your analysis:

- ******Total**********,**** ******Unique**********, or**** ******Value******
  You can report on the total number of instances of an event (**Total**) or the unique number of profiles that performed that event (**Unique**). If the metric you select has a monetary value associated with it (e.g., **Placed Order**), you can also report on the value of the events (**Value**).
- ******SUM****** ****or**** ******AVG******
  You can choose one of two aggregations: **SUM** or **AVG**. **SUM** shows you the total of all events for your selected metric. For example, if there are two $15 **Placed Order** events within the time span you select, the **VALUE SUM** will be $30 and the **TOTAL SUM** will be 2. **AVG** shows the average of events that occurred for your metric. For example, if there are two $15 **Placed Order** events within the time span you select, the average will be $15.

  4. You also have the option to see performance data grouped by specific list or segment. You can add this modifier to group and filter your report by specific values. For guidance and best practices on segments, refer to our [resource](https://help.klaviyo.com/hc/en-us/articles/115005237908-Getting-started-with-segments#segment-ideas9) for segment ideas.

  ![View of the segment and list reporting checkbox options](https://klaviyo.zendesk.com/hc/article_attachments/28711699023003)

  Segment-level data is only available from July 1, 2022 onwards, so any campaign performance report that groups by “list/segment” before this date will produce an error. You will need to either remove the affected “list/segment” group or adjust your timeframe to start on or after July 1, 2022 to successfully run the report.

  5. You will have a few options for organizing your list or segment data. These options include:
- ****Grouping by list or segment****
  By checking the box for ****List/Segment**** will create a report that aggregates segment-level metrics across all campaigns.
  Each row in your report will show data per segment (i.e., Campaign ID) and per campaign send (i.e., Campaign ID and Campaign Name), with additional corresponding report metrics.
  ![](https://klaviyo.zendesk.com/hc/article_attachments/35315307780379)
- ****Grouping by inbox provider****
  By checking the box for ****Inbox provider**** will create a report that aggregates campaign performance by inbox provider. Note that only deliverability metrics will be shown and revenue will not be attributed to inbox providers.
  Each row in your report will show data per inbox provider with additional corresponding deliverability metrics.
  ![](https://klaviyo.zendesk.com/hc/article_attachments/35315307787931)
- ****Grouping by campaign and list or segment****
  By checking the boxes for both ****Campaign**** and ****List/Segment**** this will create a report that breaks down metrics by segment per campaign. Each row in your data report will show per segment and per campaign send, with additional corresponding report metrics.
  ![](https://klaviyo.zendesk.com/hc/article_attachments/35315327669403)
- ****Grouping by campaign and inbox provider****
  By checking the boxes for both ****Campaign**** and ****Inbox provider**** will create a report that breaks down metrics by inbox provider per campaign. Each row in your data report will show per inbox provider and per campaign send, with additional deliverability metrics.
  ![](https://klaviyo.zendesk.com/hc/article_attachments/35315327675035)
- ****Grouping by campaign variations****
  By checking the boxes for both ****Campaign (Including Variations)**** this will create a report that breaks down metrics by using the campaign variant. This option is useful if you are sending multiple campaign variations and would like to see which one is more successful down to the segment level. Pairing this with another group (e.g., **Inbox provider** or **List and segment**) will behave similar to the **Campaign** option, but provide data the variation level.
  Note that campaigns without variations will show “N/A” under the variant column.
  ![](https://klaviyo.zendesk.com/hc/article_attachments/35315307808027)

  Choosing **Campaign** and **Campaign (including variations)** either together, as well as choosing all three options, will not produce data results.

  The campaign performance report supports filtering by [tags](https://klaviyo.zendesk.com/hc/en-us/articles/360025834271). For example, if you only want to view data from your product announcement campaigns, select that tag from the **Filter by Tags** dropdown menu. You may select multiple tags at once, separated by the AND connector.

  ![Inside a Campaign Performance Report, you can add additional filter tags by choosing your tags from a dropdown](https://klaviyo.zendesk.com/hc/article_attachments/28711677537691)

  6. Finally, customize the time range of your report so that it only shows the data you care about. To adjust the timeframe, choose your selected time range and grouping from the associated dropdowns. If you have not specified a specific grouping, your data will instead be sorted into two rows: one for email and one for SMS.

  Note that, if you opt to include [A/B email variations](https://klaviyo.zendesk.com/hc/en-us/articles/115005228148), you will not be able to group the report by time and vice versa.

  ![Inside the Campaign Performance Report, you can customize the timeframe it pulls for date range and how it's grouped](https://klaviyo.zendesk.com/hc/article_attachments/28711677532827)

  You can adjust the time range to:
- **Today**
- **Last 24 Hours**
- **Yesterday**
- **This Week**
- **Last 7 Days**
- **Last Week**
- **This Month**
- **Last 30 Days**
- **Last Month**
- **This Year**
- **Last 90 Days**
- **Last 365 Days**
- **Last Year**
- **Custom**

  You can also group the data by:
- **Daily**
- **Weekly**
- **Monthly**
- **Yearly**

Note that timestamp data within your reports, including exported reports, will display in your [account's local time](https://help.klaviyo.com/hc/en-us/articles/115005232388) from your settings. Additionally, if you are using custom date ranges, the maximum time range is 2 years. If you attempt to create a report with over 2 worth of data, an error will appear.

## Run and export your report

Once you have customized your campaign performance report to include all of your desired engagement, deliverability, and conversion metrics — as well as timeframes, groupings, and filters — you are ready to run your report.

Note that **message ID** and **experiment variation** are different properties used in UTM tracking. **Message ID** refers to the overarching ID number of the message, while **experiment variation** refers to the ID associated with a specific A/B test version. Currently, only **message ID** will appear in report downloads. However, both **message ID** and **experiment variation** will appear in your Google Analytics data.

1. Click ****Save & Run Report****. This will process your report and save it in your account.

While it may take some time to populate your results, when it is complete you will see a robust summary of your report. Your new report and its results will automatically be saved, so you may navigate away and return to your report from within the Analytics tab at any time.

![An example of Results Preview inside the Campaign Performance Report after it has run and returned a preview of some results](https://klaviyo.zendesk.com/hc/article_attachments/28711698980251)

When your report is complete, you will see it populated with results and the configuration box will automatically collapse so you can focus on identifying performance trends and opportunities. A timestamp of when the report was last run will appear above your results.

2. If you wish to export the results of your report for further analysis, click ****Export****.

## Schedule your reports

You also have the option to schedule a report to auto-run at a specific date and time and be notified via email when your results are ready. This way, you can set up your reports to automatically run and pull data for your review instead of manually exporting them.

[Learn how to schedule reports to automatically send to your inbox](https://help.klaviyo.com/hc/en-us/articles/4407838420123).

## Update report results

Reports do not automatically refresh; rather, you will need to manually re-run the report to pull updated data. To see when a report was last updated, look at the **Last Run** timestamp from either the Analytics tab or from within the report itself.

1. Reopen your report and click ****Run Report****.
2. In the event that you need to see historical report results from previous runs, go to ****Custom Reports**** and click ****More**** and then choose ****View History**** from the dropdown menu.

![On the Custom Analytics list page, clicking on the More dropdown to the right of the analytics name will expose the View History option](https://klaviyo.zendesk.com/hc/article_attachments/28711677598747)

This will show all historical runs for your report of interest.
3. To download the historical results of your report, select ****Export****.

![After a Custom Report has run, click the Export button in the top right to download and export results](https://klaviyo.zendesk.com/hc/article_attachments/28711698968987)

## Clone and rename reports

If you have an existing report that you would like to copy, use the clone option.

1. Go to ****Custom Reports**** and find the report that you want to clone.
2. To the right of the report, click ****More**** and then choose ****Clone Report**** from the dropdown menu.
Once you clone your report, you will see a new report appear at the top of your **Custom Reports** list named "Copy of **your original report name**.

![On the Custom Reports list page, the button labeled more to the right of a report will open a dropdown when clicked and shown Clone Report](https://klaviyo.zendesk.com/hc/article_attachments/28711677580955)

![On the main Custom Reports list page, an example of a cloned report which will appear at the top of the list](https://klaviyo.zendesk.com/hc/article_attachments/28711699033499)

Note that cloned reports do not include scheduling preferences from the original report. If you would like to schedule your copied report to deliver to you on a regular cadence, head to our guide on [How to Schedule Custom Reports](https://help.klaviyo.com/hc/en-us/articles/4407838420123).

3. If you would also like to rename your cloned report, navigate to the right of the report and click ****More****, then choose ****Edit Name**** from the dropdown menu.

![On the Custom Reports list page, the button labeled more to the right of a report will open a dropdown when clicked and shown Rename Report ](https://klaviyo.zendesk.com/hc/article_attachments/28711699037979)

4. Rename your report in the modal that appears. Once you have renamed your report, click ****Save****.

![When Rename Report is chosen from the More dropdown on the custom reports pages, a modal will appear to allow you to rename report](https://klaviyo.zendesk.com/hc/article_attachments/28711677595035)

## Additional resources

- [Understanding custom reports in Klaviyo](https://klaviyo.zendesk.com/hc/en-us/articles/360047725651)
- [Getting started with reporting](https://klaviyo.zendesk.com/hc/en-us/articles/360047399472)
- [How to build a flow performance report](https://klaviyo.zendesk.com/hc/en-us/articles/360047044892)