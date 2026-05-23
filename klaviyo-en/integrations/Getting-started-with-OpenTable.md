---
id: 23112971772699
title: "Getting started with OpenTable"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/23112971772699-Getting-started-with-OpenTable"
section: "OpenTable"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:34Z"
language: en
---

## You will learn

Learn how to integrate with OpenTable, a real-time online reservation network for fine dining restaurants.

## Before you begin

To integrate with OpenTable, you need to name Klaviyo as a third party processor in order to gain access to the Sync API, which is OpenTable's API that will allow us to pull data directly into Klaviyo.

1. Contact your OpenTable account manager about naming Klaviyo as a third party processor.
2. Once OpenTable creates a DocuSign for your restaurant, provide the following info:

   ****API(s) to be Access by Recipient****: Sync API
   ****Recipient Name****: Klaviyo, Inc.
   ****Relationship to Client****: Vendor/Service Provider

   ****Recipient Address****
   125 Summer St. Floor 10
   Boston, MA 02110

   ****Contact Information****
   Klaviyo Team
   [restaurants@klaviyo.com](mailto:restaurants@klaviyo.com)
   +1 800-338-1744
   (no fax)

   You must also create a list in Klaviyo for anyone who has opted in via OpenTable.
3. Navigate to ****Audience**** > ****Lists********&********Segments****.
4. Click ****Create new**** > ****Create list**** in the top right corner.
5. Name the list something that will make its purpose obvious such as “OpenTable Subscribers Ongoing”.
6. Click ****Create list****.
7. While viewing the new list, select the ****Settings**** tab.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28723524398491)
8. Copy the list ID of this list. You will need this later.
9. Navigate to the ****Consent**** tab on the left and set the list to ****Single opt-in****.
   It’s important that this list is single opt-in to prevent subscribers from all receiving a confirmation email once the integration is installed.

![](https://klaviyo.zendesk.com/hc/article_attachments/28723524413083)

## Integrate OpenTable with Klaviyo

To integrate with OpenTable:

1. OpenTable Client ID (can be found [here](https://dev.opentable.com/partner-portal/profile/credentials))
2. OpenTable Secret ID (can be found [here](https://dev.opentable.com/partner-portal/profile/credentials))
3. Klaviyo List ID (as mentioned in the **Before you begin** section of this article)
4. OpenTable Restaurant ID and Restaurant Name

1. Log into your OpenTable account to make sure some of the links below will work.
2. In Klaviyo, click ****Integrations > Explore apps****.
3. Search for **OpenTable**, and click on the card. Then, click ****Install****.
4. On the setups page, enter the following information:
   1. Whatever the name is will be what you can filter by later, so if you have multiple locations, you should put that in the name.
5. Click the ****Complete setup**** to begin the integration. This will start a 2 year historical sync of OpenTable guest and reservation data. Going forward, there’ll be a periodic sync every 30 minutes that pulls in guest and reservation data so your account is always up to date.

## Understand your OpenTable data

Klaviyo syncs different events from OpenTable related to membership and OpenTable properties. We sync 2 years of historical data from OpenTable.

Klaviyo syncs email addresses and email consent from OpenTable. Please note that only subscribes are synced from OpenTable, and unsubscribes are not.

While phone numbers are synced, SMS consent is not. This means that SMS cannot be sent to phone numbers synced from this integration.

To view your OpenTable data:

1. Click the ****Analytics**** dropdown in the left-hand navigation sidebar.
2. Select ****Metrics****. Here, you can view all of the metrics in your account. The metrics labeled “OpenTable” represent all of the metrics synced from your OpenTable integration.
3. Filter this view to see OpenTable metrics by using the filter selector next to the search bar and select ****OpenTable****.

![](https://klaviyo.zendesk.com/hc/article_attachments/28723524415515)

Learn more about your [OpenTable data](https://help.klaviyo.com/hc/en-us/articles/23113172847259).

## Segment customers using OpenTable data

You can use OpenTable’s metrics to segment customers and target them with a campaign. For example, you can create a segment of everyone who has previously completed a reservation.

![](https://klaviyo.zendesk.com/hc/article_attachments/28723546329499)

To create the example segment shown above:

1. Click the ****Audience**** dropdown in the left-hand navigation sidebar.
2. Click ****Lists & Segments****.
3. Click ****Create List / Segment**** in the top right.
4. Select ****Segment****.
5. Name your segment and select tags if desired.
6. Under Definition, select ****What someone has done (or not done)**** > ****Completed Reservation**** > ****at least once**** > ****over all time****.
7. Click ****Create Segment****.

### Segment by reservation value

If you want to segment by the value of a reservation, you'll need to have your POS connected to OpenTable. If your POS is not connected to OpenTable, value amounts will not sync from OpenTable to Klaviyo.

For example, if you are using both OpenTable and Square and have Square connected to OpenTable, you'll see an OpenTable event called **Completed Reservation Value**, which you can use in segmentation and filtering. Note that this metric will not appear in the **Metrics** tab.

## Use OpenTable data in flows

You can use OpenTable metrics to trigger flows. For example, you can use the **Completed Reservation** metric to trigger a flow to send messages to someone immediately when they complete a reservation.

To create a flow using OpenTable metrics:

1. Navigate to the ****Flows**** tab from the left-hand navigation sidebar.
2. Click ****Create flow**** in the top right.
3. Click ****Create from scratch**** in the top right.
4. Name your flow and select tags if desired.
5. Click ****Create Flow****.
6. In the flow builder, choose Metric as the trigger.
7. From the sidebar, choose ****Your metrics**** > ****OpenTable**** > ****Completed Reservation**** or ****All triggers**** > ****Metric**** > ****Completed Reservation****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28723524404251)
8. Click ****Done****.
9. Add time delays and messages relevant to the triggering action. Learn more about [how to create a metric-triggered flow](https://help.klaviyo.com/hc/en-us/articles/360003057151).
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28723546333467)
10. Once your content is ready, click ****Update Action Statuses**** in the top right of the flow builder to set the flow live.

## Outcome

You've now integrated OpenTable with Klaviyo and learned about OpenTable data in Klaviyo, segmenting customers using OpenTable data, and using OpenTable data in flows.

## Why am I seeing the notification “Your account is calling a retired revision”?

Are you seeing a notification in Klaviyo that reads “[ACTION Required] Your account is calling a retired revision”, like the one below?

![](https://klaviyo.zendesk.com/hc/article_attachments/31085192132251)

Please ignore this notification; no action is currently needed on your part. Your OpenTable integration is managed by Klaviyo and will continue to work as expected.