---
id: 17797889315355
title: "Getting started with the recency, frequency, and monetary (RFM) analysis report"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/17797889315355-Getting-started-with-the-recency-frequency-and-monetary-RFM-analysis-report"
section: "Customer insights"
category: "Advanced KDP & Marketing Analytics"
category_slug: "advanced-kdp-marketing-analytics"
klaviyo_updated: "2026-04-21T13:54:31Z"
language: en
---

## You will learn

Learn how to use the recency, frequency, and monetary values (RFM) report to gather deeper insights into your customers’ purchasing behaviors. The RFM report provides data on how recently a customer made a purchase, how frequently they purchase overall, and how much they generally spend on individual transactions. Klaviyo then brings this data together to determine what customer group (e.g., Loyal customers) a profile most aligns with. These insights are helpful as they can optimize your marketing strategies, including how you personalize messages, how you encourage repeat purchases, how frequently you message and when, etc. Additionally, for those customers or segments who may be at risk, you can use these insights to drive winback campaigns and reduce churn.

[Advanced KDP](https://help.klaviyo.com/hc/en-us/articles/17655007276059) and [Marketing Analytics](https://help.klaviyo.com/hc/en-us/articles/33789259613595) are not included in Klaviyo’s standard marketing application, and a subscription is required to access the associated functionality.Head to our [billing guide](https://help.klaviyo.com/hc/en-us/articles/115000976672) to learn about how to purchase these plans.

## Before you begin

Your report needs to:

- Have at least 500 customers who have placed an order.

  This does not refer to total profiles, but rather the number of people who have actually made an order with your business. Note that if this section is on a profile but is blank, Klaviyo doesn’t have enough data on that individual to make a prediction.
- You have an ecommerce integration (e.g., Shopify, BigCommerce, Magento, etc.) or use the Klaviyo API to send placed orders.
- You have at least 180 days of order history and have orders within the last 30 days.
- You have at least some customers who have placed 3 or more orders.

Only Owners, Admins, Managers, and Analysts can access this report. Additionally, if you have created a [new custom metric](https://help.klaviyo.com/hc/en-us/articles/22311085738395/), it may take up to 48 hours for this change to be reflected in your report.

## Recent report updates (as of 5/2/2024)

As of May 2, 2024, the RFM report is rolling out new‌ properties and settings. Please review the information below for [existing](https://klaviyo.zendesk.com/hc/en-us/articles/18193920339483#h_01HWWHY499J0M3QFMVG16Z3ZWY) and [new](https://klaviyo.zendesk.com/hc/en-us/articles/18193920339483#h_01HWWJ5KRZPD5X16RWRMN70BWQ) customers using Advanced KDP.

### Existing customers using Klaviyo Advanced KDP

#### Profile properties changes

The RFM report will have 3 new properties. Beginning on May 2nd, 2024 Klaviyo introduced the new properties noted in the table below. Then on May 21st, Klaviyo automatically updated your segments to use these new properties and remove the old property values.

| ****Old property**** | ****New property**** | ****What does it measure?**** | ****Additional considerations**** |
| --- | --- | --- | --- |
| **$current\_month\_rfm\_group** | **Current RFM group** | The RFM group the profile currently belongs to. |  |
| **$previous\_month\_rfm\_group** | **Previous RFM group** | The most recent **different** RFM group, the profile belonged to prior to their current RFM group. | Until a profile’s RFM group changes, their **Previous RFM group** will show as **Unknown******.**** |
| N/A | **RFM group last changed** | Timestamp of when the profile transitioned from **Previous RFM group** to **Current RFM group**. This will only appear when a profile changes its RFM group. |  |

#### When profile properties refresh

Additionally, RFM properties are refreshed every night instead of the 1st of the month. This means that Klaviyo will check for updates every 24 hours, and if these RFM properties have changed on a profile, you will see these changes reflected. However, if you update your RFM settings, the profile property changes will be reflected within 2 hours.

Keep in mind that the RFM dashboard updates immediately while the changes on a profile record update with a delay. Thus, you may see differences in numbers per RFM group in the dashboard that are not yet reflected in your profiles.

### New customers using Advanced KDP

New customers just getting onboarded to Advanced KDP on or after May 2, 2024 date do not need to worry about transitioning to the new profile properties, as these will already be standard.

Additionally, keep in mind that you may see the **Unknown** status for **Previous RFM group** when onboarding or when updating your RFM model while the model calculates **Current RFM group** and detects the prior state.

## Navigating to the report

Navigate to ****Advanced KDP > Intelligence > Customer insights > RFM analysis********.**** Alternatively, if you are a Marketing Analytics customer, navigate to ****Marketing Analytics**** > ****Customer insights**** > ****RFM analysis****.

Here you will see a default report set to a start date of 30 days prior to the current day and the end date as the current day.

Every night or 24 hours, the system automatically updates the **Current RFM group**, **Previous RFM group**, and **RFM group last changed** properties.

Keep in mind that the RFM dashboard updates immediately while the changes on a profile record update every 24 hours. Thus, you may see differences in numbers per RFM group in the dashboard that are not yet reflected in your profiles.

### Compare distribution of customers card

The **Compare distribution of customers** card breaks down:

- Your RFM groups
- Shows which customers were added or removed from each group.
- Shows the percentage change of each group during a specific time frame.

This card is useful for seeing how customers are allocated between different groups and if your current marketing efforts are making an impact.

Learn more about how [Klaviyo calculates your percentiles, scores, and customer groups](https://help.klaviyo.com/hc/en-us/articles/17797937793179).

### Customers tab

The **Customers** tab displays your customer groups by date in a bar chart format. On the left side is the Klaviyo-determined customer group with a blue bar representing the start date and a green bar representing the end date of your report’s time range. Here, you can compare how your customer groups are changing across a certain period.

![compare distribution-updated.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28711730698651)

By hovering over any of the bars in the chart, you can review:

- The start and end dates
- The number of profiles that fit that customer group.
- The percentage this group represents out of all groups.

![hover, customers tab.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28711701728923)

### Added or dropped tab

The **Added or dropped** tab displays bar charts for each customer group and any changes that have occurred between your report’s start and end dates. You can review the number of profiles added (teal portion of each bar) or dropped (red portion of each bar) from each customer group. This chart is useful in reviewing the total additions and subtractions to each customer group and where you should concentrate your marketing efforts.

![compare distribution of customers tab.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28711701722651)

By hovering over any of the bars in the chart, you can review the total number of dropped and added profiles to each customer group.

![added or dropped, hover.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28711701724059)

### Percentage change tab

The **Percentage change** tab shows data for each customer group by the start and end dates of your report. This table shows the total number of profiles per group, the percentage this represents out of all groups, as well as the percentage changes (positive or negative) of profiles dropped or added for each group.

This table is static and does not allow sorting or filtering.

![compare distribution tab.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28711701726875)

## Group change over time card

The **Group change over time** card provides a visual representation of your customer groups and the potential movements of customers between these groups from your start to end dates.

- The left side of your card is all customer groups at your report’s start date.
- The right side of your card is all customer groups at your end date.
- The lines in between these dates visualize customers' movements, and whether they stay in the same group, or move to a different one due to their purchasing behavior.

This card is useful in deciphering if there are patterns across these customer paths, especially where customers may be dropping off in their purchases over time. For example, if many of your Loyal customers have been primarily moving down to lower groupings and not up to Champions, this may signal a need to re-engage these profiles before they possibly churn.

Learn more about how [Klaviyo calculates your percentiles, scores, and customer groups](https://help.klaviyo.com/hc/en-us/articles/17797937793179).

The **Never purchased** group is only viewable for the start date on the left side. This is because all customers shown in the chart will have made at least one purchase by the end date. Customers who never made a purchase before the end date will not be reflected in this chart at all.

![group change over time card-updated.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28711730712859)

As shown below, by hovering over any of the group names, you can view the customer paths and the number of total profile movements into or out of each group.

![hover over, movements, groups.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28711701734555)

Additionally, by hovering over any of the specific paths or lines in the middle of the chart, you can review the number of profiles moving from one group to another.

## Median performance card

The **Median performance** card provides a view of median performance per customer group. By clicking between the ******Start date****** and ******End date****** tabs on this card, you can see the median performance by each date and key metrics (i.e., **Days since purchase**, **Purchase order number**, and **Placed order revenue**).

Learn more about how [Klaviyo calculates your percentiles, scores, and customer groups](https://help.klaviyo.com/hc/en-us/articles/17797937793179).

Knowing the median performance data can help you understand the middle point of all of your data and the central tendencies of your customer behaviors, especially if you have outliers or non-uniform data. For example, if you have disparate high-value, frequent purchases and some lower-value, infrequent customer purchases, it may be helpful to see the middle intersection of when most orders generally occur and their value.

This table is static and does not allow sorting or filtering.

![Screenshot 2024-10-07 at 12.55.04 PM.png](https://klaviyo.zendesk.com/hc/article_attachments/31276857610395)

## Customizing the report

By default, your RFM report sets the start date as 30 days prior to the current day and the end date as the current day. It also automatically determines your RFM scores [using thresholds](https://help.klaviyo.com/hc/en-us/articles/17797937793179) unique to your account. However, you can adjust these items and tailor your report to fit your specific RFM-tracking needs.

Learn more about how [Klaviyo calculates your percentiles, scores, and customer groups](https://help.klaviyo.com/hc/en-us/articles/17797937793179).

### Choosing a start and end date

At the top of your report, choose your start and end dates from the calendar picker. You can choose any dates, as long as the start date precedes the end date. Updating the date(s) will trigger an automatic recalculation of all data and groups.

![calendar view picker.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28711730717979)

### Choosing a different conversion metric

By default, your RFM report will use the most frequently used the **Placed order** statistic for your account to calculate initial RFM scores. Most companies will only have one **Placed order** statistic, but some will have multiple (e.g., if you have more than one integration). You can adjust this to another value-based metric from your ecommerce integration.

1. To change your metric, at the top of your report click ****Advanced settings****. From here, you will see the **RFM Details** menu.

![RFM details menu.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28711730721691)

2. In the **Conversion Metric** section, open the ****Select an option**** dropdown.

3. Choose a different conversion metric from the list below.

Updating the metric will trigger a recalculation of all data and groups. You can also utilize [custom metrics](Custom%20metrics) within the RFM report, read more about [strategically using these](https://help.klaviyo.com/hc/en-us/articles/18194102384539#h_01JBYHZ18494EV5Y93DZ1D2237).

![Conversion metric dropdown choose.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28711701746715)

4. (Recommended but optional) Click ****Preview**** to review your changes before you save. It is recommended to preview your changes to ensure that the new conversion metric provides the data you expect. You will see the banner shown below when you are in preview mode.

![preview menu banner.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28711701748891)

5. Once you are satisfied with your updates, click ****Save****.

### Adjusting your RFM values

You may find that you want to adjust the RFM values derived from your data to look at specific types of customers. For example, you may want your report to look at higher all-time customer spending. Adjusting to a higher score or percentile under your **Monetary definition** would produce a report of higher-spending customers over time.

You have 2 options for adjusting your RFM values:

- ****Change your RFM scores using percentiles****
  Changing your RFM scores using percentiles provides precise control over the specific percentages that generate your scores and customer grouping. For example, you may want to look at only customers who buy very frequently, so you could set your frequency minimum percentile as 75%. This gives only those customers in the top 75th percentile a 3 score in your report and skew it to only focus on those very frequent buyers.

  Note that recency percentages are not available due to the need for the number of average days between order to establish thresholds. For these definitions, use a numeric score instead, as defined below.
- ****Change your RFM scores using values****
  Changing your RFM scores using values allows you to control the Klaviyo scoring that leads to your customer groupings. Since you know your customers best, customizing your scores can help you better align with their specific behaviors. For example, you can set a frequency value of 4 purchases to be assigned your high score. This means that anyone who purchases 4 or more items receive a 3 value automatically. This is helpful if you wanted to focus on very frequent shoppers in your report. However, as noted above, for precise control over percentages and data, it may be more advantageous to use the RMF percentiles toggle to define your customer groups.

### Changing your RFM percentiles

1. At the top of your report, click ****Advanced settings****.
2. Choose which definition to adjust (**Recency definitions**, **Frequency definitions**, or **Monetary value definitions**). Click open the applicable menu, as shown in the example below.

![RFM value settings open-updated.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28711730730395)

3. Click on the toggle for ****Score based on percentiles****.

4. From here, adjust either your highest or average scores by filling in your new percentages in the field(s).

Note that values must be from 1 to 100 and should not include any special characters, including the “%” character.

In the example below, using 66% for minimum all-time spend moves all customers who fall within this higher percentile to receive a 3 value automatically. This is helpful if you want to focus on higher-spending customers over time.

![percentage field changed.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28711701753499)

5. (Recommended but optional) click ****Preview**** to review your changes before you save. It is recommended to preview your changes to ensure that the new percentiles provide the data you expect. You will see the banner shown below when you are in preview mode.

![preview menu banner.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28711701748891)

6. Once you are satisfied with your updates, click ****Save****.

### Changing your RFM scores

1. At the top of your report, click ****Advanced settings****.
2. Then choose which definition you would like to adjust (**Recency definitions**, **Frequency definitions**, or **Monetary value definitions**). Click open the applicable menu, as shown in the example below.

![RFM value settings open-updated.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28711730730395)

3. From here, adjust either your highest or average scores by filling in your new values in the field(s).

If you are updating the **Monetary value** definitions you should should values that represent monetary or currency values (e.g., 250 represents $250 USD for my account).

In the example below, using a value of $250 for minimum all-time spend makes it so that only customers who spend at least $250 are scored as your “best” customers (with a value of 3).

Note that these must be whole numbers and no special currency characters can be used. It is recommended to also use the same currency values as your account is set to, as it will not convert values here.

![monetary defintion settings_UPDATED.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28711730735515)

4. (Recommended but optional) Click ****Preview**** to review your changes before you save. It is recommended to preview your changes to ensure that the new percentiles provide the data you expect. You will see the banner shown below when you are in preview mode.

![preview menu banner.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28711701748891)

## Troubleshooting errors

### Edits to RFM settings

If you receive an error message like the one shown below, you may have attempted to save your RFM settings with an incompatible value or special characters. Values should:

- Be numeric values
- Be whole numbers
- Not conflict with one another (e.g., average all-time spend is higher than minimum all-time spend)
- Not include special characters

![error banner .jpg](https://klaviyo.zendesk.com/hc/article_attachments/28711701757467)

### Empty card or report

There may be times where Klaviyo cannot immediately retrieve your data. If this happens, you will see an error notification as shown below. As noted, refresh the entire report page to reload this card(s).

Your data is still loading if you receive a message that it is “Applying changes” with a green progress bar. This is not a data error, so there is no need to refresh the page. Your data will load momentarily in your cards.

![rfm empty report error.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28711730739867)

## Viewing the RFM statistics for an individual profile

In addition to the insights provided in the main RFM report, you can also review the RFM data and groupings for individual profiles.

To do this, you will use the **RFM Analysis** card on each profile.

1. If you are going through the **Profiles** section, navigate to ****Audiences > Profiles > Metrics and insights****. If you are in the segment builder, navigate to ****Audiences > Lists & Segments**** and find a segment. Click on a ****profile**** and head to ****Metrics and insights****.
2. Find the **RFM analysis** card below the **Predictive analytics** card.

As shown in the example below, this card will contain:

- The profile’s current RFM group (Note that RFM groups are based on the daily values that are updated daily).
- The profile’s previous RFM group for comparison.
- The timestamp of the RFM group last changed, or when a profile moved from **Previous RFM group** to **Current RFM group**. This will only appear when a profile changes its RFM group.
- Data related to the number of conversions and potential revenue. (Note that these will be revenue-based metrics derived from your RFM data such as **Placed Order, Ordered Product, Fulfilled Order,** etc.).

![](https://klaviyo.zendesk.com/hc/article_attachments/28711730743579)