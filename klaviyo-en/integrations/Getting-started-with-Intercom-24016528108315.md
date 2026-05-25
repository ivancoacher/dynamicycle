---
id: "24016528108315"
title: "Getting started with Intercom"
source_url: "https://help.klaviyo.com/hc/en-us/articles/24016528108315-Getting-started-with-Intercom"
section: "Intercom"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:34Z"
language: "en"
---
## You will learn

Learn how to integrate Intercom with Klaviyo in order to improve your support experience for customers. When you integrate with Intercom, metrics related to ticket and conversation activity as well as profile data will sync to Klaviyo.

## Before you begin

In order to install the Intercom integration, you must have the permission “Can install, configure and delete apps" on the Intercom side. If you don’t have this permission, ask an Admin user to grant you this permission by navigating to ****Settings**** > ****General**** > ****Teammates**** > ****Edit**** in Intercom.

## Set up the Intercom integration

Follow the steps outlined below to integrate Intercom with Klaviyo:

1. Log in to your Klaviyo account.
2. Select the ****Integrations**** tab.
3. Select ****Explore apps****, search for Intercom, and click the card.
4. Click ****Install**** to start setting up the integration.
5. After reviewing what data will be shared between Intercom and Klaviyo, click ****Allow****.
6. Log into Intercom when prompted to complete setup on the Intercom side.
7. Review your business name and click ****Complete setup**** at the bottom of the page.

![](https://klaviyo.zendesk.com/hc/article_attachments/28704487218843)

## Understand your Intercom data

Klaviyo syncs different events from Intercom related to tickets and conversations.

To view your Intercom data:

1. Click the ****Analytics**** dropdown in the left-hand navigation sidebar.
2. Select ****Metrics****. Here, you can view all of the metrics in your account. The metrics labeled “Intercom” represent all of the metrics synced from your Intercom integration.
3. Filter this view to see Intercom metrics by using the filter selector next to the search bar and select ****Intercom****. Intercom metrics will be indicated by the Intercom logo.

![](https://klaviyo.zendesk.com/hc/article_attachments/28704479148059)

Here, you’ll see recent data synced from Intercom to Klaviyo, and a sync progress bar for your historical data sync. If you are experiencing issues with your sync, select ****Restart Import**** here to restart the historical data sync.

The data synced from Intercom to Klaviyo includes:

- Created Conversation
- Rated Conversation
- Read Conversation
- Replied to Conversation
- Created Ticket
- Submitted Ticket
- Replied to Ticket
- Marked Ticket On Hold
- Resolved Ticket

- Profile information associated with conversation and ticket events
- The following order events:

For more information on the properties associated with each event synced from Intercom, see [Intercom data reference](https://klaviyo.zendesk.com/hc/en-us/articles/24016624580379).

## When the integration syncs

The integration syncs in real time which means event metrics and profiles will sync immediately to Klaviyo once events have been triggered in Intercom.

Past events such as **Created****Conversation**, **Rated****Conversation**, **Created****Ticket**, **Resolved****Ticket**, **Submitted****Ticket** will also sync historically.

## Segment customers using Intercom data

You can use Intercom’s metrics to segment customers and for organizational purposes such as in the event you want to include or exclude certain customers from a campaign. For example, you can create a segment of everyone who has submitted a ticket in the last 30 days.

![](https://klaviyo.zendesk.com/hc/article_attachments/28704487217307)

To create such a segment:

1. Click the ****Audience**** dropdown in the left-hand navigation sidebar.
2. Click ****Lists & Segments****.
3. Click ****Create New > Create segment**** in the top right.
4. Name your segment and select tags if desired.
5. Under **Definition**, select ****What someone has done (or not done)**** > ****Submitted Ticket**** > ****at********least********once**** > ****in the last**** > ****30**** > ****days****.
6. Click ****Create********Segment****.

## Use Intercom data in flows

You can use Intercom metrics to trigger flows. For example, you can use the **Rated****Conversation** metric to trigger a flow to send messages to someone immediately after they rated a conversation they had with a support agent.

To create a flow using Intercom metrics:

1. Navigate to the **Flows** tab from the left-hand navigation sidebar.
2. Click ****Create flow**** in the top right.
3. Search for ****Intercom**** to find pre-built flows, or click ****Build your own**** in the top right.
4. Name your flow and select tags if desired.
5. Click ****Create Flow****.
6. In the flow builder, choose ****Metric**** as the trigger.
7. From the dropdown, select an Intercom metric, such as ****Rated Conversation****, indicated by the Intercom icon.
8. The flow builder with the Intercom metric ****Rated Conversation**** used as the trigger of the flow.
9. Click ****Save****.
10. Add time delays and messages relevant to the triggering action.
11. Once your content is ready, set your flow live.

## Outcome

You've now integrated Intercom with Klaviyo and learned about Intercom data in Klaviyo, segmenting customers using Intercom data, and using Intercom data in flows.