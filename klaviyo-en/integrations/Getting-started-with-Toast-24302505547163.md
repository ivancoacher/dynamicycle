---
id: "24302505547163"
title: "Getting started with Toast"
source_url: "https://help.klaviyo.com/hc/en-us/articles/24302505547163-Getting-started-with-Toast"
section: "Toast"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-05-08T13:45:24Z"
language: "en"
---
## You will learn

Learn how to integrate Klaviyo with Toast, a tool that assists restaurants with accepting payments seamlessly and securely. Klaviyo syncs order events from Toast, which allow you to personalize your messaging to customers.

Klaviyo syncs online orders from Toast and offline orders when guest identifiers are provided, including waitlisted guest orders when “Start Order on POS” is enabled for Toast Tables.

## Add the Klaviyo integration in Toast

Before taking actions in Klaviyo, first add the integration in Toast.

1. Log into your Toast account.
2. Follow Toast’s guide on [how to set up Toast Partner Connect](https://central.toasttab.com/s/article/Toast-Partner-Connect-Setting-Up-Integrations-with-Toast).
3. Search for and add the **Klaviyo** integration. Learn more from Toast’s guide on [how to add or remove an integration](https://central.toasttab.com/s/article/Adding-or-Removing-an-Integration-with-Toast-Partner-Connect).
4. If you have multiple locations, collect the IDs for each of your restaurants by navigating to ****Reports**** > ****Settings**** > ****Data Exports**** and exporting your [restaurant ID mapping](https://www.toasttab.com/restaurants/admin/export/restaurantidmapping).

## Add the Toast integration in Klaviyo

1. In Klaviyo, select ****Integrations**** ****> Explore apps****.
2. Search for **Toast**, and click on the card. Then, click ****Install****.
3. On the setup page, enter the ID for your restaurant which you obtained in the previous section. Enter multiple restaurant IDs as a comma separated list (e.g. a1b2-c3d4, e1f2-g3h4) if you are connecting multiple restaurants.

   ![](https://klaviyo.zendesk.com/hc/article_attachments/45709956500379)
4. Click ****Connect****.

## Understand your Toast data

Klaviyo syncs many different order placement and fulfillment-related events from Toast. Klaviyo syncs online orders from Toast and offline orders when guest identifiers are provided, including waitlisted guest orders when “Start Order on POS” is enabled for Toast Tables. Klaviyo syncs 3 years of historical data from Toast.

Toast does not sync email and SMS consent with Klaviyo, but the Toast integration can add data to profiles that have already provided consent through other sources. It is generally advised to [import consent manually via CSV upload](https://help.klaviyo.com/hc/en-us/articles/360043841811).

To view your Toast data:

1. Navigate to ****Analytics > Metrics.****
   Here, you can view all of the metrics in your account. The metrics with a Toast icon represent all of the metrics synced from your Toast integration.
2. In the **Search metrics** field search for the “Toast” integration or use the **All integrations** dropdown to find it and filter your view.

![Metrics screen showing a search bar, a 'Toast' filter, and a list of order metrics: Fulfilled Order, Ordered Product, Placed Order, Prepared Order, and Refunded Order.](https://cdn.sanity.io/images/6ct6b26e/help-center-prod/3ca74e49bf07b000f15b96481b8fd6f90e4f4838-437x453.png)

Learn more about your [Toast data](https://help.klaviyo.com/hc/en-us/articles/24302613403931).

## Segment customers using Toast data

You can use Toast’s metrics to segment customers and target them with a campaign. For example, you can create a segment of everyone who placed an order in the last 30 days and send a campaign to that segment to inform them about a promotional event or deal.

To create the example segment:

1. Navigate to ****Audience > Lists & segments****.
2. Click ****Create New**** and choose ****Create new**** ****segment****.
3. Name your segment and select tags if desired.
4. Under **Definition**, select ****What someone has done (or not done)**** > ****Placed Order**** > ****at least once**** > ****in the last**** > ****30**** > ****days****.
5. Click ****Create segment****.

![](https://klaviyo.zendesk.com/hc/article_attachments/28720660479771)

## Use Toast data in flows

You can use Toast metrics to trigger flows. For example, you can use the **Placed Order** metric to trigger a flow to send messages to someone immediately when they place an order.

To create a flow using Toast metrics:

1. Navigate to ****Flows****.
2. Click ****Create flow**** in the top right.
3. Click ****Create from scratch**** in the top right.
4. Name your flow and select tags if desired.
5. Click ****Create Flow****.
6. In the flow builder, choose ****Your**** ****metrics > Toast**** in the trigger sidebar.
7. From the list, select a Toast metric, such as **Placed Order**.

   ![](https://klaviyo.zendesk.com/hc/article_attachments/28720660481563)
8. Click ****Save > Confirm and save****.
9. Add any time delays and messages relevant to the triggering action. Learn more about [creating a post-purchase flow](https://help.klaviyo.com/hc/en-us/articles/360028872611).
10. Once your content is ready, click ****Review and turn on**** or ****Update action statuses**** in the top right of the flow builder to set the flow live.

## Outcome

You've now integrated Toast with Klaviyo and learned about Toast data in Klaviyo, segmenting customers using Toast data, and using Toast data in flows.

## Add additional restaurant locations

If you expand your business or add new locations to your Toast account after your initial integration, you can add these Restaurant IDs to your integration settings to ensure data flows for those specific locations.

To add new locations:

1. ****In Toast****, ensure the new locations have been authorized for the Klaviyo integration. For specific steps on managing locations within the Toast platform, see Toast’s guide on [how to add or remove an integration](https://central.toasttab.com/s/article/Adding-or-Removing-an-Integration-with-Toast-Partner-Connect).
2. ****In Klaviyo****, click ****Integrations**** in the left-hand navigation menu.
3. Select ****Toast**** from your list of enabled integrations to open the settings page.
4. Locate the **Restaurant IDs** section and click ****Add****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/46509585937691)
5. Input the Toast Restaurant IDs you would like to add. If adding multiple IDs at once, separate them with a comma (e.g., a1b2-c3d4, e1f2-g3h4).
6. Click ****Add****.
7. A notification will appear at the bottom of the screen regarding unsaved changes. Click ****Save**** to finalize the update.

Once saved, Klaviyo will begin syncing data for the new locations. It may take a short period for historical data from these new Restaurant IDs to populate in your Klaviyo account.