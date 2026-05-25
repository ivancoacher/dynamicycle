---
id: "39406849361691"
title: "Getting started with Cloudbeds"
source_url: "https://help.klaviyo.com/hc/en-us/articles/39406849361691-Getting-started-with-Cloudbeds"
section: "Cloudbeds"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:55Z"
language: "en"
---
Learn how to integrate Klaviyo with Cloudbeds, a reservation management platform. Klaviyo syncs guests, email subscribers, and reservations from Cloudbeds, which allow you to personalize your messaging to guests.

Klaviyo’s Cloudbeds integration supports ****Cloudbeds Group Accounts****. If you manage multiple properties under a group account, Klaviyo can sync data across all of them.

If you add new properties to your Cloudbeds group account after the initial setup, simply reinstall your Cloudbeds integration in Klaviyo. This ensures we can sync all historical data from your newly added properties.

## Integrate Klaviyo with Cloudbeds

To set up the integration in Klaviyo:

1. Log in to Klaviyo.
2. Select the ****Integrations**** tab.
3. Click ****Explore apps****.
4. Search for **Cloudbeds** in the app marketplace and select the card.
5. Click ****Install****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/40629116516507)
6. Click ****Connect to Cloudbeds****.
7. Review the permissions in Klaviyo and click ****Allow****.
   ![Screenshot 2026-01-28 at 4.54.27 PM.png](https://klaviyo.zendesk.com/hc/article_attachments/46000898762651)
8. In Cloudbeds, select the properties you’d like to connect with Klaviyo and click ****Continue.****
9. Grant access to the Klaviyo integration in Cloudbeds and click ****Allow Access.****
10. On the next page, check the box **Sync your Cloudbeds email subscribers to Klaviyo** if you’d like to do so.
    ![](https://klaviyo.zendesk.com/hc/article_attachments/41127125448219)
11. If you selected the setting above, select a list from the dropdown to add Cloudbeds email subscribers to. Make sure that this list is set to [single opt-in](https://help.klaviyo.com/hc/en-us/articles/115005251108#h_01HZ5G5ZQBDHTV20V1BE7D4YAT) to avoid triggering opt-in emails to guests syncing from Cloudbeds.
12. When you’re done, click ****Complete setup****.
13. You’ll receive a success message confirming that your Cloudbeds integration is now connected.

## Upgrade your Cloudbeds integration

To upgrade your Cloudbeds integration, which will allow you to start using Cloudbeds Reservation Objects, you should:

1. Log in to Klaviyo.
2. Select the ****Integrations**** tab.
3. Click ****Cloudbeds****.
4. Click the ****Update**** banner in the integration.
   ![Screenshot 2026-01-28 at 4.50.32 PM.png](https://klaviyo.zendesk.com/hc/article_attachments/46000913156891)
5. Review the permissions in Klaviyo and click ****Allow****.
   ![Screenshot 2026-01-28 at 4.54.27 PM.png](https://klaviyo.zendesk.com/hc/article_attachments/46000898762651)
6. In Cloudbeds, select the properties you’d like to connect with Klaviyo and click ****Continue.****
7. Grant access to the Klaviyo integration in Cloudbeds and click ****Allow Access.****
8. On the next page, check the box **Sync your Cloudbeds email subscribers to Klaviyo** if you’d like to do so.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/41127125448219)
9. If you selected the setting above, select a list from the dropdown to add Cloudbeds email subscribers to. Make sure that this list is set to [single opt-in](https://help.klaviyo.com/hc/en-us/articles/115005251108#h_01HZ5G5ZQBDHTV20V1BE7D4YAT) to avoid triggering opt-in emails to guests syncing from Cloudbeds.
10. When you’re done, click ****Complete setup****.
11. You’ll receive a success message confirming that your Cloudbeds integration is now connected.

## View your Cloudbeds data

To view your Cloudbeds event metrics:

1. Navigate to ****Analytics > Metrics****. Here, you can view all of the metrics in your account. The metrics with a Cloudbeds icon represent all of the metrics synced from your Cloudbeds integration.
2. Use the **All integrations** dropdown and select **Cloudbeds** to view only Cloudbeds metrics.
   ![cloudbeds-metrics.png](https://klaviyo.zendesk.com/hc/article_attachments/47138150306971)

   To view your Cloudbeds objects (note: requires the latest version of the integration):
3. Navigate to ****Content > Objects****. Here, you can view all of the objects in your account. The objects with a Cloudbeds icon represent all of the objects synced from your Cloudbeds integration.

Learn [more about your Cloudbeds data](https://help.klaviyo.com/hc/en-us/articles/39406875083035).

## Segment guests using Cloudbeds event metrics

You can use Cloudbeds metrics and objects to segment guests. Using metrics, for example, you can create a segment of guests who have confirmed a reservation at a specific location.

To create the example segment:

![](https://klaviyo.zendesk.com/hc/article_attachments/40629116525211)

1. Navigate to ****Audience > Lists & segments****.
2. Click ****Create New**** and choose ****Create new segment****.
3. Name your segment and select tags if desired.
4. Select the following definition and filter:
   1. What someone has done (or not done) > Confirmed Reservation (Cloudbeds) > at least once > over all time
   2. where > Property Name > equals > (Property Name)
5. Click ****Create segment****.

   Using objects, you can create a segment of guests who have a reservation start date from tomorrow onwards:

   ![Screenshot 2026-01-28 at 5.38.24 PM.png](https://klaviyo.zendesk.com/hc/article_attachments/46001857523739)
6. Navigate to ****Audience > Lists & segments****.
7. Click ****Create New**** and choose ****Create new segment****.
8. Name your segment and select tags if desired.
9. Select the following definition and filter:
   1. Properties about someone > Reservation (Cloudbeds) > has at least one
   2. where > StartDate > in the next > 5200 weeks
10. Click ****Create segment****.

## Use Cloudbeds data in flows

You can use Cloudbeds metrics to trigger flows, or sequences of automated actions. Klaviyo offers multiple pre-built flows using Cloudbeds data, including:

- Welcome Series
- Guest Winback
- Guest Thank You
- Reservation Confirmation
- Reservation Cancellation
- Reservation No Show
- Happy Birthday
- Reservation Check In
- Reservation Check Out

  To view these pre-built flows:

  1. In Klaviyo, select the ****Flows**** tab.
  2. Click ****Create flow****.
  3. Filter by **Cloudbeds** to see all Cloudbeds flows.![](https://klaviyo.zendesk.com/hc/article_attachments/40629054018203)

  You can also create a flow with Cloudbeds objects. To create a pre-arrival flow, for example, you can:
- Navigate to Flows > ****Create flow**** > ****Build your own.****
- Name the flow and select tags (optional).
- Select the **Date property** trigger.
  ![Screenshot 2026-01-28 at 5.10.42 PM.png](https://klaviyo.zendesk.com/hc/article_attachments/46000913159195)
- Select Cloudbeds, Reservation: StartDate from the Date property dropdown.
- Choose the time you'd like to start the flow.
- Add the relevant messages in.

![Screenshot 2026-01-28 at 5.13.29 PM.png](https://klaviyo.zendesk.com/hc/article_attachments/46000913161115)

You can also create your own flows from scratch.