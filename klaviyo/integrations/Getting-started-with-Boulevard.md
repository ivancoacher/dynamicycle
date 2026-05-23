---
id: 16131320434459
title: "Getting started with Boulevard"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/16131320434459-Getting-started-with-Boulevard"
section: "Boulevard"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:29Z"
language: en
---

Learn how to integrate with Boulevard, a tool that assists salon and spa brands with booking, scheduling, marketing, payments, reporting, and more.

## Before you begin

Before you begin, confirm that you have access to the Boulevard API. This integration relies on Boulevard Webhooks and APIs, which require a subscription to the Boulevard API package. If you are unsure if you have this package, contact your Boulevard CSM to confirm.

## Integrate Boulevard with Klaviyo

To integrate Boulevard with Klaviyo:

- Select a Klaviyo list from the dropdown for these subscribers.
- Select a Klaviyo list from the dropdown for these subscribers. We recommend keeping separate lists for email and SMS.

1. In the Boulevard console, navigate to ****Manage Business > App & Integration****.
2. Scroll to **Custom Apps** and click ****Install****.
3. Enter the Klaviyo application ID:

   ```
   0d2168f5-934c-4586-85b0-03ef0f5c54be
   ```
4. In Klaviyo, select the ****Integrations**** tab.
5. Click ****Explore apps****, then search for **Boulevard** and select the card.
6. On the next page, click ****Install****.
7. Enter your Boulevard Business ID and click ****Connect****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/37276456067483)
8. Review the permissions and click ****Allow****.
9. On the next page, check the box to **Sync your Boulevard email subscribers to Klaviyo**.
10. Check the box to **Sync your Boulevard SMS subscribers to Klaviyo**.
11. When you’re done, click ****Save****.

You’ve now integrated Boulevard with Klaviyo.

## Understand your Boulevard data

Klaviyo syncs many different events from Boulevard related to appointments and membership. When you integrate, we sync all historic data stored in Boulevard and then sync ongoing data in real time.

To view your Boulevard data in Klaviyo:

1. Click the ****Analytics**** dropdown in the left-hand navigation sidebar.
2. Select ****Metrics****. Here, you can view all of the metrics in your account. The metrics with a Boulevard icon represent all of the metrics synced from your Boulevard integration.
3. Filter this view to see only Boulevard metrics by using the filter selector next to the search bar.

![List of Boulevard metrics found on the Metrics page in Klaviyo.](https://klaviyo.zendesk.com/hc/article_attachments/28720671545755)

Learn more about [your Boulevard data](https://klaviyo.zendesk.com/hc/en-us/articles/16130796656667).

## Segment customers using Boulevard data

You can use Boulevard’s metrics to segment customers and target them with a campaign. For example, you can create a segment of everyone who has completed an appointment in the last 30 days and send a campaign to that segment.

![Example segment which checks if someone has Completed Appointments in the last 30 days.](https://klaviyo.zendesk.com/hc/article_attachments/28720659737371)

To create the example segment shown above:

1. Click the ****Audience**** dropdown in the left-hand navigation sidebar.
2. Click ****Lists & Segments****.
3. Click ****Create List / Segment**** in the top right.
4. Select ****Segment****.
5. Name your segment and select tags if desired.
6. Under **Definition**, select ****What someone has done (or not done)**** > ****Completed Appointments**** > ****at least once**** > ****in the last**** > ****30**** > ****days****. If you have multiple integrations, make sure to choose the **Completed Appointments** metric with the Boulevard logo.
7. Click ****Create Segment****.

   For this example, if you’d like to make sure the segment only includes people who completed an appointment for the first time:
8. Click ****AND**** to add a new exclusive condition.
9. Add the condition ****What someone has done (or not done)**** > ****Completed Appointments**** > ****equals**** > ****1**** > ****over all time****. This will exclude anyone who has completed an appointment more than once.

![Example segment which checks if someone has only Completed Appointments once over all time.](https://klaviyo.zendesk.com/hc/article_attachments/28720671540507)

## Use Boulevard data in flows

You can use Boulevard metrics to trigger flows. For example, use the **Completed Appointments** metric to trigger a flow to send messages to someone immediately when they complete an appointment.

If you are using Boulevard to send email and SMS notifications, make sure to turn off messages that you would rather send through Klaviyo flows so that your customers aren’t receiving repetitive messages. See [Boulevard’s support documentation](https://support.boulevard.io/) for more information on how to disable email and SMS notifications.

To create a flow using Boulevard metrics:

1. Navigate to the ****Flows**** tab from the left-hand navigation sidebar.
2. Click ****Create flow**** in the top right.
3. Click ****Create from scratch**** in the top right.
4. Name your flow and select tags if desired.
5. Click ****Create Flow****.
6. In the flow builder, choose ****Metric**** as the trigger.
7. From the dropdown, select a Boulevard metric, such as ****Completed Appointments****, indicated by the Boulevard icon.
   ![Choosing the Completed Appointments metric as the trigger in the left sidebar of the flow builder.](https://klaviyo.zendesk.com/hc/article_attachments/28720671552539)
8. Click ****Done****.
9. Add a message relevant to the triggering action, such as a thank you message.
   ![Example flow using the Completed Appointments metric as the trigger.](https://klaviyo.zendesk.com/hc/article_attachments/28720671554203)
10. Once your content is ready, click ****Update Action Statuses**** in the top right of the flow builder to set the flow live.

## Outcome

You've now integrated Boulevard with Klaviyo and learned about Boulevard data in Klaviyo, segmenting customers using Boulevard data, and using Boulevard data in flows.