---
id: 38311148860955
title: "Getting started with Mews"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/38311148860955-Getting-started-with-Mews"
section: "Mews"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:56:55Z"
language: en
---

Learn how to integrate Klaviyo with Mews, a property management platform. Klaviyo syncs guests, email subscribers, and reservations from Mews, which allow you to personalize your messaging to guests.

## Generate a Mews access token for Klaviyo

If you’re using ****Mews Multi-Property****, Klaviyo fully supports this setup — once you enter your portfolio-level access token, we’ll sync data from all properties within that Mews portfolio.

To obtain a portfolio-level access token, please contact your Mews representative or reach out to [partnersuccess@mews.com](mailto:partnersuccess@mews.com).

First, you’ll need to generate a Mews access token for Klaviyo:

1. In your Mews admin, open the lefthand navigation.
2. Click ****Marketplace****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/39303110316827)
3. Search for **Klaviyo**.
4. Find the Klaviyo card and click ****Explore.****
5. Click ****Connect integration****.
6. Securely copy the provided access token.

## Integrate Klaviyo with Mews

To set up the integration in Klaviyo:

1. Log in to Klaviyo.
2. Select the ****Integrations**** tab.
3. Click ****Explore apps****.
4. Search for **Mews** in the app marketplace and select the card.
5. Click ****Install****.
6. Paste the access token you copied from Mews.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/39303118102939)
7. Click ****Connect****.
8. Review the permissions in Klaviyo and click ****Allow****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/39303118104347)
9. On the next page, check the box **Sync your Mews email subscribers to Klaviyo** if you’d like to do so.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/39303110322075)
10. If you selected the setting above, select a list from the dropdown to add Mews email subscribers to. Make sure that this list is set to [single opt-in](https://help.klaviyo.com/hc/en-us/articles/115005251108#h_01HZ5G5ZQBDHTV20V1BE7D4YAT) to avoid triggering opt-in emails to guests syncing from Mews.
11. When you’re done, click ****Complete setup****.
12. You’ll receive a success message confirming that your Mews integration is now connected.

## Update your Mews integration

To update the integration in Klaviyo:

1. Log in to Klaviyo.
2. Select the ****Integrations**** tab.
3. Select ****Mews****.
4. Click the ****Update**** button in the banner.
   ![Screenshot 2026-02-02 at 3.11.49 PM.png](https://klaviyo.zendesk.com/hc/article_attachments/46185483637275)
5. Review the permissions in Klaviyo and click ****Allow****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/39303118104347)
6. On the next page, check the box **Sync your Mews email subscribers to Klaviyo** if you’d like to do so.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/39303110322075)
7. If you selected the setting above, select a list from the dropdown to add Mews email subscribers to. Make sure that this list is set to [single opt-in](https://help.klaviyo.com/hc/en-us/articles/115005251108#h_01HZ5G5ZQBDHTV20V1BE7D4YAT) to avoid triggering opt-in emails to guests syncing from Mews.
8. When you’re done, click ****Complete setup****.
9. You’ll receive a success message confirming that your Mews integration is now connected.

## View your Mews data

To view your Mews data:

1. Navigate to ****Analytics > Metrics****. Here, you can view all of the metrics in your account. The metrics with a Mews icon represent all of the metrics synced from your Mews integration.
2. Use the **All integrations** dropdown and select **Mews** to view only Mews metrics.
   ![Screenshot 2026-02-20 at 2.35.28 PM.png](https://klaviyo.zendesk.com/hc/article_attachments/46890947911707)

   To view your Mews objects (note: requires the latest version of the integration):
3. Navigate to ****Content > Objects****. Here, you can view all of the objects in your account. The objects with a Mews icon represent all of the objects synced from your Mews integration.

Learn [more about your Mews data](https://help.klaviyo.com/hc/en-us/articles/38311213022235).

## Segment guests using Mews data

You can use Mews metrics and objects to segment guests. Using metrics, for example, you can create a segment of guests who have confirmed a reservation at a specific location.

![](https://klaviyo.zendesk.com/hc/article_attachments/39303110325275)

To create the example segment:

1. Navigate to ****Audience > Lists & segments****.
2. Click ****Create New**** and choose ****Create new segment****.
3. Name your segment and select tags if desired.
4. Select the following definition and filter:
   1. What someone has done (or not done) > Confirmed Reservation (Mews) > at least once > over all time
   2. where > Service Name > equals > (Location Name)
5. Click ****Create segment****.

   Using objects, you can create a segment of guests who have a reservation start date from tomorrow onwards:

   ![Screenshot 2026-01-28 at 5.38.24 PM.png](https://klaviyo.zendesk.com/hc/article_attachments/46002827800603)
6. Navigate to ****Audience > Lists & segments****.
7. Click ****Create New**** and choose ****Create new segment****.
8. Name your segment and select tags if desired.
9. Select the following definition and filter:
   1. Properties about someone > Reservation (Mews) > has at least one
   2. where > StartDate > in the next > 5200 weeks
10. Click ****Create segment****.

## Use Mews data in flows

You can use Mews metrics to trigger flows, or sequences of automated actions. Klaviyo offers multiple pre-built flows using Mews data, including:

- Welcome Series
- Guest Winback
- Guest Thank you
- Reservation Confirmation
- Reservation Cancellation
- Reservation Inquiry
- Happy Birthday
- Reservation Check In
- Reservation Check Out

  To view these pre-built flows:

  1. In Klaviyo, select the ****Flows**** tab.
  2. Click ****Create flow****.
  3. Filter by **Mews** to see all Mews flows.![](https://klaviyo.zendesk.com/hc/article_attachments/40352395503259)

  You can also create a flow with Mews objects. To create a pre-arrival flow, for example, you can:
- Navigate to Flows > ****Create flow**** > ****Build your own.****
- Name the flow and select tags (optional).
- Select the **Date property** trigger.
  ![Screenshot 2026-01-28 at 5.10.42 PM.png](https://klaviyo.zendesk.com/hc/article_attachments/46002827807515)
- Select Mews, Reservation: ScheduledStartTime from the Date property dropdown.
- Choose the time you'd like to start the flow.
- Add the relevant messages in.

![Screenshot 2026-01-28 at 5.13.29 PM.png](https://klaviyo.zendesk.com/hc/article_attachments/46002827818139)

You can also create your own flows from scratch.