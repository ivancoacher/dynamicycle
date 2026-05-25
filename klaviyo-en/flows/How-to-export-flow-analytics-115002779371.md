---
id: "115002779371"
title: "How to export flow analytics"
source_url: "https://help.klaviyo.com/hc/en-us/articles/115002779371-How-to-export-flow-analytics"
section: "Manage flows"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-04-21T13:56:37Z"
language: "en"
---
## You will learn

Learn how to export a CSV file of analytics for all or a specific set of flows. Exporting the analytics for a certain flow allows you to easily measure and review how successful a flow is. Further, you can analyze the data on a message by message basis, examining how each SMS or email is performing. In this article, we run through how to export a flow's analytics.

Owners, Admins, and Analysts are able to export flow analytics.

## Export all flow analytics

To export the analytics for all flows:

1. Navigate to the ****Flows****tab.
2. Click the ****Options**** dropdown at the top.
3. Click ****Export analytics****.
   ![export analytics.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28717378832667)
4. When you click this option, a modal will appear with options for setting up your export. Choose from the following options:
   - ******Select time range******You can choose to export all flows that have been sent over all-time, or you can limit the time range of the export.
   - ******Select tags******
     If you are using tags to organize your flows, you can specify to only export flows that have a certain tag.
   - ******Aggregate analytics by day, week, or month******When you check this box, a dropdown will allow you to choose whether you want to aggregate your flow email analytics on a daily, weekly, or monthly level.
   - ******Include all A/B test message variations******If you're A/B testing any of your flow emails, this option allows you to view the analytics of each variation separately.

Note if you want to export the analytics for a single flow, [create a new tag](https://help.klaviyo.com/hc/en-us/articles/360025834271), and then tag the flow and export the analytics for that tag.

5. Once you are done setting up your export, click ****Export**** ****Analytics****.

## Information in the exported file

Note that your data will include archived flows that fall within your export’s time range. Additionally, your chosen time range will pull data based on your account’s [local timezone](https://help.klaviyo.com/hc/en-us/articles/115005232388).

The resulting CSV file will contain the following columns (in order):

- **Flow Name**
- **Flow Message ID**
- **Flow Message Name**
- **Flow Message Channel**
- **Status**
- **Delivered**
- **Unique Opens**
- **Open Rate**
- **Unique Clicks**
- **Click Rate**
- **Placed Order**
- **Placed Order Rate**
- **Revenue**
- **Revenue per Recipient**
- **Unsub Rate**
- **Complaint Rate**
- **Bounce Rate**
- **Tags**

The following additional columns will only appear if the option "Include all A/B email variations" is selected. Please note that messages that do not have an A/B test associated with them will contain "n/a" in these columns.

- **A/B Test Name**
- **Variant Name**
- **A/B Test Dates**
- **Winning Variant**

For exports that include A/B test variations, you may see multiple rows for the same message ID. Each row contains data for a different variation. The example below shows the data for a flow which had 2 separate A/B tests run for its first message. The first 2 rows are from the 2 variations of the first A/B test. The second 2 rows are the variations for its second test.
![Flow analytics spreadsheet that is downloaded after exporting flow analytics.](https://klaviyo.zendesk.com/hc/article_attachments/28717378828827)

If a message was live and sending before an A/B test was created for it, you will see an additional row for the main message along with the rows for each variation.

## Additional resources

Learn more about analytics and reporting:

- [Understanding flow analytics](https://help.klaviyo.com/hc/en-us/articles/115002779351)
- [Understanding available campaign analytics](https://help.klaviyo.com/hc/en-us/articles/115005258568)
- [Getting started with a custom report strategy](https://help.klaviyo.com/hc/en-us/articles/360046757411)