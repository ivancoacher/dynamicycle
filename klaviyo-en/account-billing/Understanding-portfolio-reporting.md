---
id: 25185047957275
title: "Understanding portfolio reporting"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/25185047957275-Understanding-portfolio-reporting"
section: "Portfolio"
category: "Account & billing"
category_slug: "account-billing"
klaviyo_updated: "2026-04-21T13:54:35Z"
language: en
---

## You will learn

Learn about the reporting tools and functionality for portfolios. These features enable you to easily aggregate and analyze your data across multiple accounts (such as if you have different brands or use separate accounts for different regions).

With portfolio reporting, you can:

- Get a comprehensive look at your performance across accounts.
- Compare accounts in a single view and currency.
- Understand what drives conversions and revenue for each account.

## Before you begin

As part of the [portfolio setup process](https://help.klaviyo.com/hc/en-us/articles/24656917054747), you must select and map your metrics.

Portfolio metrics aggregate similar metrics across your accounts and create one metric for reporting at the portfolio level. For example, you may have multiple metrics that are associated with revenue across your portfolio that you want pulled together into one metric.

Portfolio metrics are based on either:

- Monetary value, also referred to as revenue
- Event count, also referred to as conversions

The information in the **Home** tab varies based on which type of metric is selected.

Until you create a portfolio-level metric, you won’t see any data in your portfolio **Home** tab.

****How to add metrics in a portfolio****

Tips for creating your metric:

- Name your portfolio metric in a way that represents all the metrics associated with it (e.g., “Orders” or “Placed Orders” for metrics that deal with customers making a purchase).
- Choose aggregated metrics that have similar data associated with them (e.g., create a single portfolio metric for all **Placed Order** events).
  - The type affects whether the report shows the number of conversions (if **Event count** is selected) or by revenue (if **Monetary value** is selected).
    1. Next to each account, pick what account-level metric you want to map to this portfolio metric (e.g., **Placed Order**).
    2. If you don’t want to add any metric for a specific account, toggle the **Include in metric?** to ****Exclude****.
  - For instance, you may need to exclude an account for a portfolio metric because that account does not support a given metric.

  To create a metric:

  1. Navigate to the ****Home**** tab in the portfolio.
  2. In the **Portfolio metric** dropdown, select ****Create new metric****.
  3. Under **Metric name**, input what you want the metric to be called in the portfolio (e.g., **Order value**).
     ![Naming the portfolio metric](https://klaviyo.zendesk.com/hc/article_attachments/28713374810267)
  4. Under **Type**, choose the type of metric (e.g., **Monetary Value** for placed orders).

1. Select ****Save and exit****.
2. Repeat steps 3-8 for all the metrics you want to view in the portfolio.
3. Once you’ve created your desired portfolio metrics, click ****View reporting**** or navigate back to the ****Home**** page to view the report.

## Customize your portfolio report

On the **Home** tab, you’ll see your filters and options for viewing your accounts’ performance:

- ****Timeframe****
  The time period that the report pulls in information from your linked accounts. The default is 7 days, but you can also view it as week-to-date, month-to-date, last 30 days, or a custom timeframe.
- ****Accounts****
  The linked accounts you want to view in the report. The default pulls in data from all linked accounts.
- ****Portfolio metric****
  The metric you want to examine in the report (such as **Active on Site** or **Placed Order**). The default is the first metric you created in the portfolio.
- ****Currency****
  The currency used in the report. If your individual accounts use varying currencies, Klaviyo converts them to the currency you select for this report. This only applies to the portfolio report; adjusting this setting does not change the currency in any linked account. The default is your portfolio currency.
  - Note: the currency dropdown only appears for a portfolio metric when that metric is mapped to accounts that have 2 or more different currencies.

### Refresh the report

The report updates when you either:

- Navigate to the ****Home**** tab.
- Manually click the refresh button on the right side.

![Home tab, with the refresh button and timestamp highlighted](https://klaviyo.zendesk.com/hc/article_attachments/28713374813083)

You can also see the last time the report updated on the right.

## Understand the **Top performers** report

The **Top Performer** report shows the top 3 accounts across your portfolio for 3 key performance indicators (KPIs). This overview also shows how the portfolio and top accounts are trending compared to the previous period.

- A green arrow indicates a positive trend (e.g., increased revenue).
- A red arrow indicates a negative trend (e.g., fewer conversions).

  What’s displayed in this report varies based on whether the selected metric is based on revenue (i.e., monetary value) or conversions (i.e., event count).
- Revenue-based
  - Total revenue
  - Average order value (AOV)
  - Conversion rate
- Conversion-based metrics show:
  - Total revenue
  - Email click rate
  - Conversion rate

![top performers.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28713385799067)

You can customize which aggregate metrics you want to view in your Top Performers report by swapping or deleting the metric cards.

## Understand the **Accounts performance** report

The **Accounts performance report** enables you to understand your marketing performance for each account as well as across accounts.

Depending on what metric you’ve selected in your filters, you’ll see either attributed conversions or revenue.

- The number of conversions shows for any metric assigned the **Event count** type.
- The revenue amount shows for any metric assigned the **Monetary value** type.

The table below shows examples of conversion- and revenue-based metrics. Note that since you can name the metrics shown in a portfolio, the names of your metrics may be different.

|  |  |
| --- | --- |
| ****Conversion-based metrics examples**** | ****Revenue-based metrics examples**** |
| Active on site | Placed order |
| Review submitted | Started checkout |

Want to jump ahead? Skip to the section on [revenue-based metrics](#h_01HWNMT8YD420NMCAMDQAFE8D7) or on [exporting portfolio reports](#h_01HWNMT8YEJYHXRSR83GKYTSPC).

### Conversion-based metrics (i.e., **Event count** type)

#### **Account performance** overview

At the top, you’ll see a graph with 2 tabs:

- ****Attributed conversions****
  Shows the conversions attributed to campaigns and flows.
  ![Graph showing attributed conversions for campaigns versus flows](https://klaviyo.zendesk.com/hc/article_attachments/28713385766427)
- ****Channel mix****
  Shows the conversions attributed to email, SMS, and mobile push.
  ![Graph showing attributed conversions for email and SMS](https://klaviyo.zendesk.com/hc/article_attachments/28713385771675)

  In the upper right, you can pick how you want to view this information:
- Conversion count from highest to lowest, or lowest to highest
- Account name in alphabetical or reverse alphabetical order

![Options for sorting conversions](https://klaviyo.zendesk.com/hc/article_attachments/28713385777435)

#### Performance breakdown for conversion-based metrics

Under the graph, you can see the **Performance breakdown** section. This includes a table with more details about each account’s campaign and flow performance.

By default, you’ll see a table listing:

- Total conversions
- Conversions from campaigns
- Conversions from flows

![performance breakdown.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28713385804059)

In this view, there is a search bar, where you can search for a specific account, and 2 dropdowns to filter your view.

#### View attributed conversions for a specific channel (left dropdown)

Selecting the left dropdown provides the options to sort by of:

- **Attributed conversions**
- **Campaigns performance**
- **Flows performance**

  Choosing either **Campaigns performance** or **Flows performance** changes the right dropdown so that you can:
- Choose a channel (email, SMS, or push)
- View campaign or flow performance for that channel, including:
  - Recipients
  - Open rate and unique opens (available for email and mobile push)
  - Click rate and unique clicks (available for email and SMS)
  - Conversion rate and number of conversions

![pb conversions 2.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28713374851995)

#### Compare attributed conversions across all channels (right dropdown)

Selecting only the right dropdown (i.e., if you leave the left dropdown as **Attributed conversions**) allows you to select:

- **Campaigns & flows**
- **Campaigns**
- **Flows**

  Choosing either **Campaigns** or **Flows** shows you the following for each account’s campaigns or flows:
- Total conversions
- Email conversions
- SMS conversions
- Push conversions

![Example of choosing Campaigns in the right dropdown to view each channel's contribution to conversions](https://klaviyo.zendesk.com/hc/article_attachments/28713374829339)

### Revenue-based metrics (i.e., **Monetary value** type)

#### **Account performance** overview

At the top, you’ll see a graph with 2 tabs:

- ****Attributed revenue****
  Shows the revenue attributed to campaigns and flows.
  ![Graph showing attributed revenue for campaigns versus flows](https://klaviyo.zendesk.com/hc/article_attachments/28713385784987)
- ****Channel mix****
  Shows the revenue attributed to email, SMS, and mobile push.
  ![Graph showing attributed revenue by channel](https://klaviyo.zendesk.com/hc/article_attachments/28713374822939)

  In the upper right, you can pick how you want to view this information:
- Revenue from highest to lowest, or lowest to highest
- Account name in alphabetical or reverse alphabetical order

![Options for sorting attributed revenue](https://klaviyo.zendesk.com/hc/article_attachments/28713374835867)

#### Performance breakdown for revenue-based metrics

Under the graph, you can see a table with more details about each account’s campaign and flow performance.

By default, you’ll see a table listing:

- Total revenue
- Revenue from campaigns
- Revenue from flows
- Average order value

![performance breakdown.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28713385804059)

In this view, there is a search bar, where you can search for a specific account, and 2 dropdowns to filter your view.

#### View attributed conversions for a specific channel (left dropdown)

Selecting the left dropdown provides the options of:

- **Attributed revenue**
- **Campaigns performance**
- **Flows performance**.

  Choosing either **Campaigns performance** or **Flows performance** changes the right dropdown so that you can:
- Choose a channel (email, SMS, or push)
- View campaign or flow performance for that channel:
  - Recipients
  - Open rate and unique opens (available for email and mobile push)
  - Click rate and unique clicks (available for email and SMS)
  - Conversion rate and revenue amount

![pb conversions 2.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28713374851995)

#### Compare attributed revenue across all channels (right dropdown)

Selecting only the right dropdown (i.e., if you leave the left dropdown as **Attributed revenue**) allows you to select:

- **Campaigns & flows**
- **Campaigns**
- **Flows**

  Choosing either **Campaigns** or **Flows** shows you the following for each account’s campaigns or flows:
- Total revenue
- Email revenue
- SMS revenue
- Push revenue

## Export portfolio reports

To export analytics from the **Accounts performance** report:

1. Navigate to the ****Home**** tab.
2. Click ****Export as CSV****.
   ![Home tab, highlighting the Export as CSV button](https://klaviyo.zendesk.com/hc/article_attachments/28713385793179)
3. Select one of the following options for how you want to view all campaigns performance, flows performance, and attributed conversions/revenue:
   1. ****Accounts performance overview****
      This report exports your data grouped by account.
   2. ****All campaigns and flows by account****
      This report exports your data broken down by the active or sent individual campaigns and flows for each account.
4. The report may take a few minutes to download. If it takes more than 1 minute, you’ll receive an email when it’s ready.
5. In the ****Home**** tab, select ****Recent report downloads****.
   Note that this button only appears once your first report is ready to be downloaded. If it doesn’t show, check back later.

![Home tab, showing the Recent report downloads button](https://klaviyo.zendesk.com/hc/article_attachments/28713385791003)

## Understand campaign or flow performance data

Review and compare how specific campaigns or flows are contributing to success per account, and compare aggregated performance without having to log into individual accounts.

![](https://klaviyo.zendesk.com/hc/article_attachments/29691051900443)

Click on ****Campaigns**** or ****Flows**** from the left navigation. You can also select a specific campaign or flow from ****Home > Performance breakdown**** to navigate to these sections. However, you must have your **Performance breakdown** chart filters set to **Attributed revenue** or **Campaign performance** with **Campaigns** or **Flows** chosen, as shown in the example below.

![clickable path.jpg](https://klaviyo.zendesk.com/hc/article_attachments/29691051906331)

### Customize your view

At the top of your dashboard, you’ll see your filters and options for viewing your accounts’ performance:

- ****Accounts****
  The linked accounts you want to view in the dashboard. The default pulls in data from all linked accounts.
- ****Timeframe****
  The time period that the report pulls in information from your linked accounts. The default is 7 days, but you can also view it as week-to-date, month-to-date, last 30 days, or a custom timeframe.
- ****Portfolio metric****
  The metric you want to examine in the report (such as **Active on site** or **Placed order**). The default is the first metric you created in the portfolio.
- ****Channel****
  The marketing channel (email, SMS, or push) you sent the campaign
- ****Currency****
  The currency used in the dashboard. If your individual accounts use varying currencies, Klaviyo converts them to the currency you select for this report. This only applies to the portfolio report; adjusting this setting does not change the currency in any linked account. The default is your portfolio currency.

### Review the table

The table below will display different columns with information about each campaign per account. These include:

- ****Campaign****
  The name of the campaign or flow, including information on the type or name of segment(s) it was sent to.
- ****Account****
  Name of the account where the campaign was sent from.
- ****Channel****
  Whether the campaign was an email, SMS, or push message. If your flow is a combination of multiple channels, you will see those reflected here.
- ****Status****
  All campaigns that have been sent or in the processing of sending.
- ****Send date****
  When the particular campaign was sent.
- ****Open rate**** (available for email and push)
  The rate at which your customers open your emails or push messages. This is the number of individuals opening your email divided by the number of recipients. This column will also show the unique open count below the rate.
- ****Click rate**** (available for email and SMS)
  The rate and which your customers clicked your emails or SMS messages. This is the percentage of people who clicked a link in your message out of the people who received it. This column will also show the unique click count below the rate.
- ****Conversions****
  The number of people that converted attributed to this campaign or flow. This column will also show the unique conversions count below the rate.
- ****Revenue****
  If you used a revenue-based metric (e.g., **Added to cart**), you will see a column denoting the amount of money made on that campaign or flow.

### Additional dashboard actions

#### Sort the dashboard

Hover over until you see the arrow icon and click next to any column to sort the table by ascending or descending order.

![](https://klaviyo.zendesk.com/hc/article_attachments/29691051910555)

#### Copy an account ID

You can also copy a particular account’s ID to your clipboard if you want to review performance in more detail. Click on the ****3 dot menu**** next to a specific campaign or flow.

![](https://klaviyo.zendesk.com/hc/article_attachments/29691051919515)

#### Export your data

Review and compare your accounts and their campaign or flow performance by exporting the raw data. Click on ****Export CSV**** to download this information. Keep in mind that your export will reflect whatever table options you have selected.

![](https://klaviyo.zendesk.com/hc/article_attachments/29691013883803)