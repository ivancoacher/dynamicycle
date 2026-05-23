---
id: 17798068936219
title: "Getting started with the audience performance dashboard"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/17798068936219-Getting-started-with-the-audience-performance-dashboard"
section: "Customer insights"
category: "Advanced KDP & Marketing Analytics"
category_slug: "advanced-kdp-marketing-analytics"
klaviyo_updated: "2026-04-21T13:54:31Z"
language: en
---

## You will learn

Learn how to use the audience performance dashboard to analyze the performance of your audience segments and optimize them per marketing channel. The audience performance summary provides detailed information on each of your segments, their overall success per channel, and their total conversions or revenue. This information is useful for comparing which segments are performing well and which segments need to be further optimized.

[Advanced KDP](https://help.klaviyo.com/hc/en-us/articles/17655007276059) and [Marketing Analytics](https://help.klaviyo.com/hc/en-us/articles/33789259613595) are not included in Klaviyo’s standard marketing application, and a subscription is required to access the associated functionality.Head to our [billing guide](https://help.klaviyo.com/hc/en-us/articles/115000976672) to learn about how to purchase these plans.

## Navigating to the dashboard

Navigation steps to the audience performance dashboard vary based on whether you are an Advanced KDP or Marketing Analytics customer.

If you are an Advanced KDP customer, navigate to ****Advanced KDP > Intelligence > Predictive models****.

If you are a Marketing Analytics customer, navigate to ****Marketing Analytics > Predictive models****.

Only Owners, Admins, Managers, and Analysts can view this table.

## Customizing the audience performance dashboard

At the top of the dashboard, the conversion metric used in the table calculations and the time period you are viewing will be present.

### Adjusting your conversion metric

If you are using a revenue based metric (e.g., **Placed Order**), the last three columns of the table will have the total revenue by channels and per segment. If you are using a non-revenue based metric (e.g., **Active on Site**), these columns will instead be the total number of conversions by channels and per segment.

![dropdowns audience.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28720659871131)

1. To adjust your conversion metric, open the conversion metric dropdown.
2. Choose from the list below or search in the field for a metric.

![conversion metric dropdown.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28720671678491)

Once you update your metric, your entire table will refresh.

Note that adjusting your metric only adjusts it for this audience performance table and no other metrics or reports.

### Adjusting your time period

The time period you choose will determine the data that appears in the table. For example, choosing Last 7 days will only show data that occurred within the last 7 days.

1. Open the time period dropdown. It will have **Last 7 days** selected as default.

![time range.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28720659877275)

2. Choose one of the following options:

- Last 7 days
- Last 30 days
- Week-to-date
- Month-to-date
- Custom (Note that data can only be pulled from 6/21/2023 onwards and is limited to 1 year max.)

The time period will use your [account’s local timezone](https://help.klaviyo.com/hc/en-us/articles/115005232388). Additionally, segment data will only appear if the segment was created before or within the chosen time period

### Refreshing the table data

To see your latest data, you will have to refresh the dashboard manually. In the upper right corner next to the circular arrows icon, you will note the timestamp of whenever the dashboard was refreshed by anyone in your account.

![refresh data .jpg](https://klaviyo.zendesk.com/hc/article_attachments/28720671684891)

1. To refresh the dashboard, click on the circular arrows icon. Your dashboard timestamp will change to reflect this refresh update.

## Reviewing the audience performance data

The audience performance summary table will have all starred audience segments sorted alphabetically with performance information for each.

If you do not see a particular segment appearing here, you will need to navigate to ****Lists & Segments**** and click the ****star icon**** next to that particular segment.

![audience performance table main-updated.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28720671691291)

Each row will represent a specific segment and have the following information:

- ****Segment****
  Name of the specific segment, along with the date of creation below. Clicking on this name will directly take you to the segment in the **Lists & segments** section.
- ****Members****
  Total numbers of members to date within the time period chosen for the table.
- ****Size change****
  How many segment members were added or subtracted within the chosen time period.
- ****Email conversions**** (if using a non-revenue based metric)
  The total number of conversions attributed to email within the chosen time period.
- ****Email revenue**** (if using a revenue based metric)
  The total amount of revenue attributed to email within the chosen time period.
- ****SMS conversions**** (if using a non-revenue based metric)
  The total number of conversions attributed to SMS within the chosen time period.
- ****SMS revenue**** (if using a revenue based metric)
  The total amount of revenue attributed to SMS within the chosen time period.
- ****Total conversions**** (if using a non-revenue based metric)
  The total number of all conversions (both email and SMS) within the chosen time period.
- ****Total revenue**** (if using a revenue based metric)
  The total amount of revenue for all conversions (both email and SMS) within the chosen time period.

You can also sort each table by ascending or descending order by using the arrows next to each column.

![arrow sorting.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28720659887387)

Conversions (i.e., conversion and revenue columns in the audience performance dashboard) shown are based on segment membership at the time the conversation event occurred.

For example, say you have a segment of profiles that have never placed an order. When a profile places their first order, they will exit the segment. However, since the profile was in the non-purchasers segment at the time they placed their order, the revenue is attributed to the original segment at the time of the purchase (i.e., profiles that have never placed an order).

## Troubleshooting data issues

If a profile did not convert within your table’s chosen table period, their data will not appear in this table.

If a row appears blank or with a “-” icon, this means that the data is currently unavailable. This could mean that the segment was created after your chosen time period for the table and you need to adjust this or that no profiles received messages via a particular channel during the time period.

Additionally, if your entire table is blank, you need to go back and start segments to appear.

## Additional resources

[Getting started with segments](https://help.klaviyo.com/hc/en-us/articles/115005237908)

[Understanding the difference between segments and lists](https://help.klaviyo.com/hc/en-us/articles/115005061447)