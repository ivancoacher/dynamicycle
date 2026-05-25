---
id: "42789551068699"
title: "Getting started with Report builder (in beta)"
source_url: "https://help.klaviyo.com/hc/en-us/articles/42789551068699-Getting-started-with-Report-builder-in-beta"
section: "Intelligence (Advanced KDP & Marketing Analytics)"
category: "Advanced KDP & Marketing Analytics"
category_slug: "advanced-kdp-marketing-analytics"
klaviyo_updated: "2026-04-17T06:55:41Z"
language: "en"
---
Available to customers with ****Advanced Klaviyo Data Platform (AKDP)**** or ****Marketing Analytics (MA)**** access.

## ****Overview****

The new Report builder is the next generation of Klaviyo’s custom reporting experience. Built on Klaviyo’s ****Data Dictionary**** and a vastly more scalable infrastructure, it provides a flexible, consistent way to create and customize performance, product, and metric reports — all in one place.

With Report builder, you can:

- Build reports using ****Campaigns****, ****Flows****, ****Forms****, ****Products****, or ****Metrics (events)**** data from any integration
- Combine ****Campaigns and Flows**** data in a single marketing performance report
- Use ****multiple groupings**** and add ****up to 20 filters****
- Group by ****custom profile and event properties****
- ****Export**** data to CSV, or ****schedule**** your reports to run on a recurring basis
- Start from a ****pre-configured “quick start” template**** and easily customize the report further to your needs

Report builder is currently in beta and available to all active and trial ****Advanced Klaviyo Data Platform (AKDP)**** and ****Marketing Analytics**** customers.

## ****Key improvements from Custom Reports****

Report builder was rebuilt from the ground up to offer more flexibility, data consistency, and control.

Overall here is how Report Builder’s capabilities compare and have been improved:

|  |  |  |
| --- | --- | --- |
| ****Capability**** | ****Custom Reports**** | ****Report builder**** |
| ****Data contexts**** | Campaigns, Flows, Products, and Metrics | Campaigns, Flows, All Messages (Campaigns and Flows), Forms, Products, and Metrics |
| ****Filtering**** | 1 filter (by tag) | Up to 20 filters |
| ****Grouping**** | 1-2 grouping options | Any number of campaign and flow attribute groupings, up to 5 metric property groupings and up to 4 profile property groupings supported in a single report |
| ****Profile & event properties**** | Only supported in Metric reports | Group by any custom profile event property in any report type |
| ****Scheduling**** | Schedule a report to run weekly or monthly at a certain date-time | Schedule a report to run weekly or monthly at a certain date-time, and customize the send timezone, subject line and message |
| ****Templates**** | Standard report types and legacy prebuilt report templates library | Updated standard report types with canonical conversion metrics included  \* Modernized Report Template Library coming 2026 |
| ****Export**** | CSV only | CSV only |

## ****Capabilities by report type****

Each report type has different supported data contexts and grouping options.

|  |  |  |
| --- | --- | --- |
| ****Report Type**** | ****Custom reports**** | ****New report builder**** |
| Campaign data | - Email, SMS, Push events**Does not include WhatsApp, Omnichannel, RCS** - Group by 2 of 4 possible Message attributes - 1 Filter (by tag only) | - ALL Channel events - ALL Formats (e.g. RCS) - Group by ANY message attribute, up to 5 metric attributes, and up to 4 of any profile attribute (incl. Custom profile properties) - Filter by ANY attribute |
| Flow data | - Email, SMS, Push events**Does not include WhatsApp, Omnichannel, RCS** - Group by only 1 attribute (i.e. Flow Message) - 1 Filter (on grouping only) | - ALL Channel events - ALL Formats (e.g. RCS) - Group by ANY message attribute and 3 of ANY profile attribute (incl. Custom) - Filter by ANY attribute |
| Metric data | - Single & Multi-metric reporting are separate - Allows 1 grouping - 1 Filter (on grouping only) | - Single & Multi-metric reporting are the same - Group by ANY shared attribute - Filter by ANY attribute |
| Form data | - Only possible with the Single Metric Deep Dive report | - Now possible with a standard Forms report - Group by multiple metrics & attributes |
| Product data | - Group by either Product OR Category - 1 Filter (on grouping only) | - Multiple Group by ANY shared attribute and ANY profile attribute - Filter by ANY attribute |
| Profile data | - Only exposed in Single & Multi-metric Reporting | - Up to 2 profile attributes in ANY report |

You can now group by profile attributes (e.g., City, Current RFM Group, and your own brand-specific custom profile properties) across any of the report types — an experience not previously possible in Custom Reports.

## ****Access Report builder****

1. Navigate to ****Advanced → Marketing analytics → Report builder (Beta)****.


   ![](https://klaviyo.zendesk.com/hc/article_attachments/42789551041179)
2. The ****Reports**** page lists all your saved reports.

   From this page, you can:

- ****Create**** a new report
- ****Download**** it to CSV
- ****Schedule**** it for recurring delivery
- Run, edit, or rename a report
- View a sample 1000 rows of results from the most recent run
- Delete a report

![](https://klaviyo.zendesk.com/hc/article_attachments/42789629593883)

## ****Create a new report****

1. ****Click “Create report.”****
   This opens the ****Create a report**** drawer.
2. Give your report a ****name**** and ****description****, and choose a ****report type**** (Campaign, Flow, Form, Metric, or Product performance) or start from a ****Custom report**** to build from scratch.

![](https://klaviyo.zendesk.com/hc/article_attachments/42789629594907)

Each report type starts with a standard configuration that includes the most relevant metrics — including revenue metrics. For example, your mapped revenue metric (e.g. Placed Order) is automatically selected as the first conversion metric in the report

![](https://klaviyo.zendesk.com/hc/article_attachments/42789551046299)

## ****Configure your data****

After selecting a report type, you’ll be taken to the ****Select data**** screen.

- Use the ****Selected**** tab to see the pre-selected metrics and attributes included by default for your chosen report type.
- Switch from the default “****Selected****” tab to the “****All****” tab to explore and add additional groupings, filters, or timeframe intervals (Entire range, Daily, Weekly, Monthly).



  ![](https://klaviyo.zendesk.com/hc/article_attachments/42789551047323)
  ![](https://klaviyo.zendesk.com/hc/article_attachments/42789629599131)
- Choose from available metrics (like Opens, Clicks, Placed Orders, etc.), and how you’d like to measure that metric (Total, Uniques, Rate, Average, Revenue per Recipient, etc.) to identify the kind of data you want.
- You can add additional ****groupings**** by selecting attributes like campaign name, channel, text message format (e.g. SMS, MMS, RCS), A/B test variation, inbox provider, country, current RFM group, and more. Once you export your data to CSV, you can use these groupings to pivot your data to create unique, nested views.
- Add filters (up to 20) that allow exact values or “contains” on a given attribute to customize your report.


  ![](https://klaviyo.zendesk.com/hc/article_attachments/42789551049371)
- Adjust the ****Time frame**** (Last 7 days, Last 30 days, Year-to-date, etc.) and choose your ****Group by time interval**** (Entire period, Day, Week, Month).

![](https://klaviyo.zendesk.com/hc/article_attachments/42789551054747)

![](https://klaviyo.zendesk.com/hc/article_attachments/42789551056667)

## ****Preview and run your report****

- When you’re ready, click ****Run****.
- Report builder will process your query and display a ****1000-row sample preview**** so you can review your results before exporting.
- While your report runs, you’ll see a progress animation showing each stage (data retrieval, organization, export preparation).
- Once the report is complete, you can ****download the data as a CSV****, schedule it, or view it in the app.

![](https://klaviyo.zendesk.com/hc/article_attachments/42789629605403)

## ****Schedule or export your report****

From your report’s ****Manage report**** menu, you can:

- ****Edit**** your configuration
- ****Rename**** your report
- ****Schedule**** recurring delivery via email
  ![](https://klaviyo.zendesk.com/hc/article_attachments/42789551059483)

  When scheduling a report:
- You can automate running and sending the report to yourself. The recipient will always default to your own user email address at this time.
- Select your start date, sending time, time zone, and send frequency (weekly, monthly).
- You can customize the subject line and message.

Scheduled emails include a secure link to download the latest CSV directly from Klaviyo.

![](https://klaviyo.zendesk.com/hc/article_attachments/42789629609627)

## ****Report builder can help you answer real questions:****

- Compare ****engagement**** and ****conversion rates**** by ****channel**** across all campaigns and flows.
- Analyze ****Placed Order**** and ****Added to Cart**** metrics by ****attributed campaign****.
- View ****form submissions**** by version and region to optimize signup performance.
- Identify ****top-performing products**** by ****campaign**** or by ****RFM group****
- Group purchase behavior by ****custom profile attributes**** like membership tier or loyalty status.

## ****Next steps****

- Build and use custom reports in Report builder
- Provide product feedback via the product feedback form, our Customer Success Manager or support@klaviyo.com