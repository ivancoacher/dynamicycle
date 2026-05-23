---
id: 24206444868251
title: "Getting started with ChowNow"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/24206444868251-Getting-started-with-ChowNow"
section: "ChowNow"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:35Z"
language: en
---

Learn how to integrate with ChowNow, an online ordering platform. Klaviyo’s integration with ChowNow brings order events into Klaviyo, along with associated profiles.

## Integrate ChowNow with Klaviyo

1. Log in to your Klaviyo account.
2. Select your account name in the lower left corner and click ****Integrations****.
3. Click ****Explore apps****.
4. Search for **ChowNow** and select the card.
5. Click ****Install****.
6. Click ****Connect to ChowNow****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/37404916279963)
7. Review the permissions in Klaviyo and click ****Allow****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/37404893963291)
8. Log in to ChowNow if prompted.
9. Review the permissions in ChowNow and click ****Authorize****. You’ll be redirected to Klaviyo and should see a success message.

You’ve now integrated ChowNow with Klaviyo.

## ChowNow data in Klaviyo

The historical sync from ChowNow looks back 2 years. The periodic sync going forward occurs every 5 minutes.

Klaviyo syncs 3 order events from ChowNow:

- Accepted Order
- Placed Order
- Cancelled Order

  Klaviyo syncs the following profile data from ChowNow for profiles associated with order events:
- ChowNow ID
- First name
- Last name
- Phone number

To view your ChowNow data:

1. Click the ****Analytics**** dropdown in the left-hand navigation sidebar.
2. Select ****Metrics****. Here, you can view all of the metrics in your account.
3. Filter by **ChowNow** at the top to see all your ChowNow metrics.

![](https://klaviyo.zendesk.com/hc/article_attachments/37404893964699)

Learn more about your [ChowNow data in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/24206475048219).

## Email consent

Klaviyo does not currently sync email addresses and consent from ChowNow.

## SMS consent

While phone numbers are synced, SMS consent is not. This means that SMS cannot be sent to phone numbers synced from this integration without separately gathering consent.

## Use cases

Klaviyo does not currently sync email addresses and consent from ChowNow. If you’ve collected email consent on a profile from a different source, such as a [POS system](https://help.klaviyo.com/hc/en-us/articles/11117215837211), you can personalize your messaging to that customer using ChowNow data.

Here are some high-level ways you can put your ChowNow data to work in Klaviyo:

- ****Transactional messaging****
  Send order confirmation updates via Klaviyo flows. Learn more about [transactional emails with Klaviyo](https://help.klaviyo.com/hc/en-us/articles/360003165732).
- ****Marketing messaging****
  Create marketing based on ordering preferences (for example, dine-in vs delivery) in an effort to cross-promote different channels. Follow up with first-time guests to drive a second visit or order, or create food-specific promotions based on food preferences or updated menu items.
- ****Reporting****
  Understand menu insights on what’s popular and use these insights to forecast inventory.

To achieve transactional or marketing messaging, you’ll want to segment your customers and reach them via campaign, or reach them with Klaviyo flows. Below, we’ll explain how to do just that.

## Segment customers using ChowNow data

You can use ChowNow metrics to segment customers and target them with a campaign. For example, you can create a segment of everyone who has previously placed an order.

To create this segment:

1. Click the ****Audience**** dropdown in the left-hand navigation sidebar.
2. Click ****Lists & Segments****.
3. Click ****Create List / Segment**** in the top right.
4. Select ****Segment****.
5. Name your segment and select tags if desired.
6. Under **Definition**, select **What someone has done (or not done)** > **Placed Order** > **at least once** > **over all time**.
7. Click ****Create Segment****.

## Use ChowNow data in flows

You can use ChowNow metrics to trigger flows. For example, you can use the **Placed Order** metric to trigger a flow to send messages to someone immediately when they place an order.

To create a flow using ChowNow metrics:

1. Navigate to the ****Flows**** tab from the left-hand navigation sidebar.
2. Click ****Create flow**** in the top right.
3. Click ****Create from scratch**** in the top right.
4. Name your flow and select tags if desired.
5. Click ****Create Flow****.
6. In the flow builder, choose ****Metric**** as the trigger.
7. From the sidebar, choose ****Your metrics > ChowNow > Placed Order****.
8. Click ****Done****.
9. Add time delays and messages relevant to the triggering action. Learn more about [how to create a metric-triggered flow](https://help.klaviyo.com/hc/en-us/articles/360003057151).
10. Once your content is ready, click ****Update Action Statuses**** in the top right of the flow builder to set the flow live.

## Outcome

You've now integrated ChowNow with Klaviyo and learned how to use your ChowNow data in Klaviyo messaging.