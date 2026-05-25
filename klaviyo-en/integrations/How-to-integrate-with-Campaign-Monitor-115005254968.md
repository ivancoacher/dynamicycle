---
id: "115005254968"
title: "How to integrate with Campaign Monitor"
source_url: "https://help.klaviyo.com/hc/en-us/articles/115005254968-How-to-integrate-with-Campaign-Monitor"
section: "Migrate from an email service provider"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:24Z"
language: "en"
---
## You will learn

Learn how to integrate Campaign Monitor with Klaviyo in order to sync your Campaign Monitor lists and contacts and track Campaign Monitor analytics in Klaviyo.

Klaviyo syncs the following data from Campaign Monitor:

- Campaign Monitor contacts
- Received, clicked, and open metrics from Campaign Monitor
- Campaign Monitor lists (some or all, depending on your preferences)

## Add the Campaign Monitor integration

1. First, you'll need to locate your API key in your Campaign Monitor account. From the **Account Settings** page in your Campaign Monitor account, click ****API Keys****.
2. Click ****Show API Key**** and copy the value.
   ![Manage API Key page in Campaign Monitor with API Key and Client ID blurred out](https://klaviyo.zendesk.com/hc/article_attachments/28715962541211)
3. In your Klaviyo account, select the ****Integrations**** tab, then click ****Explore apps.****
4. Search for **Campaign Monitor**, then click the card.
5. Click ****Install****.
6. On the next page, add your Campaign Monitor API key and click ****Connect to Campaign Monitor****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28715962550683)
7. On the next page, you can configure the following integration settings under **Advanced**:
   - ****Collect open and click data for Campaign Monitor campaigns****
     Selecting this setting will sync open and click data from your Campaign Monitor campaigns.
   - ****Create Klaviyo lists from Campaign Monitor lists****
     Selecting this setting will create corresponding Klaviyo lists from your Campaign Monitor lists.
   - ****Only create Klaviyo lists for specific Campaign Monitor lists****
     Selecting this setting will allow you to specify which Campaign Monitor lists should be used to create corresponding Klaviyo lists. You will be prompted to add a comma separated list of Campaign Monitor list IDs. Please note that, even if you select this setting, all Campaign Monitor contacts who have received, opened, or clicked an email will sync to Klaviyo.
     ![](https://klaviyo.zendesk.com/hc/article_attachments/32010057312027)
8. Click ****Complete setup**** when you're done.

Once you've completed setup, data will begin to sync to Klaviyo within a few minutes. Klaviyo runs a historical sync as well as set up periodic syncs to pull in new data. Klaviyo receives historical engagement data from Campaign Monitor from the last 90 days. New data syncs to Klaviyo every hour.

## Campaign Monitor data in Klaviyo

As your integration syncs, you should start to see data populate from your Campaign Monitor campaigns.

Once the Campaign Monitor integration is present on your **Enabled Integrations** list and has a green border next to it, your integration is fully synced.

To view your Campaign Monitor data in Klaviyo, click the ****Analytics**** dropdown and select ****Metrics****. Here, you can filter by **Campaign Monitor**.

Click the ****Received Email (Campaign Monitor)**** metric.

![Metrics tab in Klaviyo showing Campaign Monitor metrics list](https://klaviyo.zendesk.com/hc/article_attachments/28715969163291)

## Best practices

To ensure that you maintain good deliverability, you should only send your first few email campaigns to an engaged segment of your list(s) from Campaign Monitor. Since you'll have open and click data from Campaign Monitor, you'll be able to use this to segment your list. You should also include open and click data from Klaviyo, as this will add engaged users that interact with your Klaviyo emails going forward. Last, be sure to add conditions that limit your sends to customers who have been added to your main list. This will ensure that your emails are targeting customers that have opted into receiving messages (by joining your list).

Build your engaged segment by using the conditions below. The open and click conditions below are scoped to 30 days. If you send emails less often, you can loosen these timeframes to 60 or even 90 days. Be sure to monitor your deliverability whenever increasing your engagement window. If you find your open and click rates decreasing, then tighten your engagement criteria by lowering the timeframe back to 30 days.

To create the segment:

- Name: Engaged segment
- If someone is in or not in a list > Person is > in Email List
- AND What some has done (or not done) > Opened Email (Campaign Monitor) > at least once > in the last > 30 > days
- OR What some has done (or not done) > Clicked Email (Campaign Monitor) > at least once > in the last > 30 > days
- OR What some has done (or not done) > Opened Email (Klaviyo) > at least once > in the last > 30 > days
- OR What some has done (or not done) > Clicked Email (Klaviyo) > at least once > in the last > 30 > days
- OR If someone is in or not in a list > Person is > in Email List > and was added in the last > 7 > days

![Klaviyo segment builder with engaged segment definition for Campaign Monitor, Create segment button with blue background](https://klaviyo.zendesk.com/hc/article_attachments/28715969152539)

## Outcome

You've now integrated Campaign Monitor with Klaviyo in order to track analytics and sync lists and contacts to Klaviyo.

## Additional Resources

- [How to migrate from another email service provider to Klaviyo](https://klaviyo.zendesk.com/hc/en-us/articles/115005082767)
- [Getting started with segments](https://help.klaviyo.com/hc/en-us/articles/115005237908)