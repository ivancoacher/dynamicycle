---
id: "4416803987739"
title: "How to configure custom reports to track Apple Mail Privacy Protection (MPP) opens"
source_url: "https://help.klaviyo.com/hc/en-us/articles/4416803987739-How-to-configure-custom-reports-to-track-Apple-Mail-Privacy-Protection-MPP-opens"
section: "Custom reports best practices"
category: "Analytics"
category_slug: "analytics-audience"
klaviyo_updated: "2026-04-21T13:55:01Z"
language: "en"
---
## You will learn

Learn how to track and analyze artificially inflated Apple Mail opens in Klaviyo custom reports.

With the release of iOS15, macOS Monterey, iPadOS 15, and WatchOS 8 in September 2021, Apple also released their new feature Mail Privacy Protection (MPP). Apple Mail users can choose to opt into MPP while using Apple Mail. MPP changes how Klaviyo receives open rate data for your emails by pre-fetching our tracking pixel, and thus causing some Klaviyo analytics to show potentially higher email opens.

For your subscribers that have specifically opted into MPP, any email delivered to their device using the Apple Mail app will see open rates affected (e.g., connecting a Gmail account to Apple Mail that has opted into MPP would still fall under affected opens). Anything email open showing as an “Apple Privacy Open” comes from a subscriber using a device with MPP enabled, whether or not they have opened the email. We have no way of distinguishing between a true human open and an automated open when MPP is enabled.

Note that the Apple privacy open properties are available for opens occurring on or after November 20, 2021. Open events before this date may not be included in your Apple Mail data.

To review these opens separately, you will need to build a custom report that includes one of the Apple privacy open properties.

You can also adjust your [email conversion settings](https://help.klaviyo.com/hc/en-us/articles/11118357030555) in your account to track MPP opens by default.

## Configuring your custom report

In order to detect MPP related opens, you will need to add a property to your Single Metric, Campaign, or Flow Performance Reports.

1. Navigate to ****Analytics********> Custom Reports****.
2. You have the option to either choose a pre-built report or create your own report from scratch. With either option, you can add the Apple opens related metrics.

Note that the **Total Apple Privacy Opens** and **Unique Apple Privacy Opens** properties are not available on the product performance or multi-metric reports.

![Screen_Shot_2022-01-25_at_1.44.53_AM.png](https://klaviyo.zendesk.com/hc/article_attachments/28705637710235)

### Campaign or flow performance reports

1. From inside an existing report or a new campaign or flow performance report, click on the ****Standard Campaign Metrics**** field to expose the dropdown.
2. From here, you can choose to add either **Total Apple Privacy Opens**, **Unique Privacy Opens**, or both properties.

This is how the two properties differ:

- ******Total Apple Privacy Opens******
  The cumulative number of all MPP device opens. This includes potential multiple opens by the same subscriber.
- ******Unique Apple Privacy Opens******
  The unique number of all MPP device opens. This includes all first opens on MPP devices, but will not include if a subscriber opens the email manually thereafter.

Once you have chosen your properties, you will see these appear in your report builder view.

3. If you have no more changes to make to your report, click ****Save & Run Report****.

### Single metric reports

1. From inside an existing report or a new Single Metric report, click on the ****Group or Filter**** field to expose the dropdown.

Note that the **Apple Privacy Open** property is only available on the **Opened Email** metric in a report.

![Screen_Shot_2022-01-25_at_2.28.33_AM.png](https://klaviyo.zendesk.com/hc/article_attachments/28705637715227)

2. Here, you have the option to search or find the property for **Apple Privacy Open**. Once you have added this new property, make sure that the where Apple Privacy Open equals is shown as **True**, **False**, or both.

![Screen_Shot_2022-01-25_at_2.31.45_AM.png](https://klaviyo.zendesk.com/hc/article_attachments/28705664535323)

3. If you have no more changes to make to your report, click ****Save & Run Report****.

## Reviewing and exporting your data

Once you have added your Apple open properties, you can either preview, schedule, or export your raw data.

When you preview your report, the data will appear below the report, as shown in the example below.

![preview_ios_data.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28705637719067)

If you choose to [schedule your report](https://help.klaviyo.com/hc/en-us/articles/4407838420123) for later review or export it as a CSV, your CSV file will contain new columns for the attributed Apple opens.

It’s important to note that in your report exports, we cannot distinguish between a subscriber open versus an MPP open. Anything email open showing as an “Apple Privacy Open” comes from a subscriber using a device with MPP enabled, whether or not they have opened the email. We have no way of distinguishing between a true human open and an automated open when MPP is enabled.

In your Campaign or Flow Performance Report, you will see the applicable columns labeled “Total Apple Privacy Opens” or “Unique Apple Privacy Opens.” These columns will include the total or unique number of emails that were opened on devices using MPP.

![Screen_Shot_2022-01-25_at_3.05.50_AM.png](https://klaviyo.zendesk.com/hc/article_attachments/28705664539291)

In the Single Metric Report, you will see a column labeled “Apple Privacy Open" in your data export, as shown below. If **Apple Privacy Open** is "True", it means the message was opened on a device with MPP.

![Screen_Shot_2022-01-25_at_2.13.48_PM.png](https://klaviyo.zendesk.com/hc/article_attachments/28705637723931)