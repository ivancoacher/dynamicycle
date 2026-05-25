---
id: "360054361092"
title: "How to export campaign analytics"
source_url: "https://help.klaviyo.com/hc/en-us/articles/360054361092-How-to-export-campaign-analytics"
section: "Analyze email results"
category: "Analytics"
category_slug: "analytics-audience"
klaviyo_updated: "2026-04-21T13:56:54Z"
language: "en"
---
## You will learn

Learn how to export a campaign's analytics. Exporting the analytics for your campaigns helps you to review and measure the performance of your campaigns. It also makes it easy to analyze the data of an individual message to see whether an SMS or email was successful.

## Export campaign analytics

1. Navigate to the ****Campaigns**** tab.
2. Click the ****menu**** next to **View library**
3. Select ****Export Analytics****. ****![Export campaign analytics option](https://klaviyo.zendesk.com/hc/article_attachments/33677391470619)****
4. Complete all the fields in the export modal.
5. Click ****Export Analytics****.

## Access past exports

To view and re-download exports from the last 30 days:

1. Click your company name in the bottom-left corner of Klaviyo.
2. Click ****Settings****.
3. Click ****Other****.
4. Click ****Downloads****.
5. Review recent downloads from your account.

## Information in the exported CSV

For any campaign, the resulting CSV file will contain the following columns (in order):

- Campaign Name
- Tags
- Subject
- List
- Send Time
- Send Weekday
- Total Recipients
- Unique Placed Orders
- Placed Order Rate
- Revenue
- Unique Opens
- Open Rate
- Total Opens
- Unique Clicks
- Click Rate
- Total Clicks
- Unsubscribes
- Spam Complaints
- Spam Complaint Rate
- Successful Deliveries
- Bounces
- Bounce Rate
- Campaign ID
- Campaign Channel

For SMS campaigns, note that the columns relating to opens will always be at 0, as SMS opens are not tracked in Klaviyo. In addition, the column named "Subject" will show you a clip of the actual text message, as there is no subject line.

## A/B testing analytics

For exports that include A/B test variations, you will see multiple rows for the same campaign ID. Each row contains data for a different variation.

For example, if you had a campaign that tested 2 variations, you will see 3 rows for this message:

1. The first variation sent to the test group.
2. The second variation sent to the test group.
3. The winning variation sent to the rest of the recipients.

You can tell the difference between variations sent to the test group and the winning variation based on the send time.

For tests that used the option to personalize variations, you may see more rows since there isn't a single winning variations for this option.

## Additional resources

- Find out more about [campaign analytics](https://klaviyo.zendesk.com/hc/en-us/articles/115005258568)
- Learn [how to export flow analytics](https://help.klaviyo.com/hc/en-us/articles/115002779371)