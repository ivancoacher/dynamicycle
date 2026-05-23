<h1>How to build a product performance report</h1>

## You will learn

Learn more about the product performance report, where to find it in Klaviyo, and how to customize it to better serve your brand. The product performance report lets you analyze product performance across key funnel metrics like browse, checkout, and purchase. Klaviyo helps you get started by providing a pre-built report. Customize it to your needs by honing in on individual products or focusing on high-level trends among collections and categories.

The product performance report helps you answer questions like:

- What are my best selling products, month over month?
- What does my conversion funnel look like across product categories?
- Do some products see a higher drop-off rate between browse-to-checkout or checkout-to-purchase?
- How has browsing and checkout activity shifted over the last 90 days, by category, as we’ve refreshed collections for a new season?

To access the product performance report, your account must have either a standard ecommerce integration (e.g., Shopify, BigCommerce, etc.) or a custom integration that incorporates product events like **Checkout Started**, **Ordered Product**, etc.

## Before you begin

For Shopify stores, based on your customer privacy settings in Shopify, Klaviyo may not track onsite events for visitors to your Shopify store in the EU, EEA, UK and Switzerland, unless they have provided consent. Thus, if you include an onsite tracking metric (such as **Viewed Product**) in your report, your report will not account for non-consented individuals.

## Build your report

1. To view the product performance report, click on ****Analytics**** > ****Custom Reports****.
2. Then, either browse our library of prebuilt reports or click ****Create from scratch****.

![In analytics, inside the custom reports section](https://klaviyo.zendesk.com/hc/article_attachments/28720759602459)

3. Under **Report Type**, select ****Product Performance Report**** from the dropdown, and give your report a name.

![In the new report section, choosing a report type from the dropdown](https://klaviyo.zendesk.com/hc/article_attachments/28720759604251)

You will then be able to customize your report to best serve your business.

4. First, select the metrics you want to report on. By default, **Viewed Product**, **Ordered Product**, and **Checkout Started** are applied. You can eliminate any of these metrics from your report by clicking the ****X**** to the right of that metric; however, you cannot add metrics that are not product-specific.

![In a Product Performance Report, options to customize it by choosing from metrics like opens, clicks, checkout started, placed order, etc](https://klaviyo.zendesk.com/hc/article_attachments/28720771442971)

5. Next, decide how you want these metrics to be calculated. There are two different dropdowns that customize this for you, as defined below.

- ******Total**, **unique**, or **value******
  You can report on the total number of instances of an event (**Total**) or the unique number of profiles that performed that event (**Unique**). If the metric you select has a monetary value associated with it (e.g., **Placed Order**), you can also report on the value of the events (**Value**).
- ******SUM** or **AVG******
  You can choose one of two aggregations: **SUM** or **AVG**. **SUM** shows you the total of all events for your selected metric. For example, if there are two $15 **Placed Order** events within the time span you select, the **VALUE SUM** will be $30 and the **TOTAL SUM** will be 2. **AVG** shows the average of events that occurred for your metric. For example, if there are two $15 **Placed Order** events within the time span you select, the **AVG** will be $15.

6. You can also add a modifier to group and filter your report by specific values. This allows you to build a more tailored report around your selected metric, specific to your business needs.

- ****Group By****
  By default, your report will be grouped by product name. You can choose to keep the product name (specific product) or switch to **Product Category** (or the specific product collection) from the associated dropdown.

  ![Inside a Product Performance Report, you can add an filter to group by like product name](https://klaviyo.zendesk.com/hc/article_attachments/28720759593755)

  Reports will only include events filtered by a profile property starting after that property was created. Even if a property was retroactively applied, if it didn’t exist on profiles at the time the event takes place, then it won't appear in the report. Learn how [properties function and influence your data](https://klaviyo.zendesk.com/hc/en-us/articles/115005074627).
- ****Filter values****
  Along with your grouping, you can add filters to make your report even more specific and only display certain instances of an event. For example, if you group by **Product Name**, then you can select ****+ Add Filter**** and type in the names of your choice to be shown in your report.

7. Finally, customize the time range of your report so that it only shows the data you care about. To adjust the timeframe, choose your selected time range and grouping from the associated dropdowns.

![Inside the Product Performance Report, customize the timeframe it pulls for date range and how it's grouped](https://klaviyo.zendesk.com/hc/article_attachments/28720759589147)

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

1. Once you have customized your product performance report to your liking, click ****Run Report****. This will process your report and save it in your account.

Note that **message ID** and **experiment variation** are different properties used in UTM tracking. **Message ID** refers to the ID number of the message, while **experiment variation** refers to the ID associated with a specific A/B test version. Currently, only **message ID** will appear in report downloads. However, both **message ID** and **experiment variation** will appear in your Google Analytics data.

![A product performance report example with the Run Report button below](https://klaviyo.zendesk.com/hc/article_attachments/28720771453211)

While it may take some time to generate your results, you will see a robust summary of your report populate as soon as your data is ready for analysis. Your report will automatically be saved, so you may proceed with other marketing activities and return to your report from within the Analytics tab at any time.

When your report is complete and populated with results, the configuration box will automatically collapse so that you can identify performance trends and opportunities. A timestamp of when the report was last run will appear above your results.
2. To export the report results for further analysis, click ****Export****.

![After a Custom Report has run, click the Export button in the top right to download and export results](https://klaviyo.zendesk.com/hc/article_attachments/28720759595291)

### Schedule your report

You also have the option to schedule a report to auto-run at a specific date and time and be notified via email when your results are ready. This way, you can set up your reports to automatically run and pull data for your review instead of manually exporting them.

[Learn how to schedule and automate your custom reports](https://help.klaviyo.com/hc/en-us/articles/4407838420123).

## Update report results

Reports do not automatically refresh with data; rather, you need to manually re-run your report to pull fresh data.

1. To see when a report was last updated, look at the **Last Run** timestamp from either the ****Analytics**** tab or from within the report itself.
2. To update your report to display the latest data, reopen it and click ****Run Report**** to refresh your results.
3. If you need to see historical report results from previous runs, go to ****Custom Reports**** and click ****More****.4. Then choose ****View History**** from the dropdown menu. This will show all historical runs for your report of interest.

![On the Custom Reports list page, clicking on the More dropdown will expose the View History option](https://klaviyo.zendesk.com/hc/article_attachments/28720759626139)

5. To export the results of a historic run of your report, select ****Export****.

![To download all historically run reports, click export to the right of a given report](https://klaviyo.zendesk.com/hc/article_attachments/28720759592091)

## Clone and rename reports

If you have an existing report that you would like to copy, use the clone option.

1. Go to ****Custom Reports**** and find the report that you want to clone.
2. To the right of the report, click ****More****.
3. Then choose ****Clone Report**** from the dropdown menu.
![On the Custom Reports list page, clicking on the dropdown for More and choosing Clone Report](https://klaviyo.zendesk.com/hc/article_attachments/28720759608987)
Once you clone your report, you will see a new report appear at the top of your **Custom Reports** list named "Copy of **your original report name**.

![Example of a copy of your original custom report appearing in Custom Repports list](https://klaviyo.zendesk.com/hc/article_attachments/28720759614363)

Note that cloned reports do not include scheduling preferences from the original report. If you would like to schedule your copied report to deliver to you on a regular cadence, you will need to [adjust that separately](https://help.klaviyo.com/hc/en-us/articles/4407838420123).

4. If you would also like to rename your cloned report, navigate to the right of the report and click ****More****, then choose ****Edit Name**** from the dropdown menu.

![On the Custom Reports list page, clicking on the dropdown for More and choosing edit name](https://klaviyo.zendesk.com/hc/article_attachments/28720759616795)

5. Rename your report in the modal that appears. Once you have renamed your report, click ****Save****.

![Edit Name modal with field to rename report and to click Save when done](https://klaviyo.zendesk.com/hc/article_attachments/28720771463451)

## Additional resources

- [How to build and use custom reports in Klaviyo](https://klaviyo.zendesk.com/hc/en-us/articles/360047725651)
- [Getting started with reporting](https://klaviyo.zendesk.com/hc/en-us/articles/360047399472)
- [Getting started with a custom reporting strategy](https://klaviyo.zendesk.com/hc/en-us/articles/360046757411)
