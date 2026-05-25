---
id: "15751697785883"
title: "Getting started with Olo"
source_url: "https://help.klaviyo.com/hc/en-us/articles/15751697785883-Getting-started-with-Olo"
section: "Olo"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:29Z"
language: "en"
---
## You will learn

Learn how to integrate with Olo, a tool that assists restaurants with online ordering.

## Before you begin

- In Olo, confirm that you have access to Dev Tools within the Olo Console Dashboard. See Olo’s documentation on the [overview dashboard](https://olosupport.zendesk.com/hc/en-us/articles/115000076446) for up-to-date information.
- Ensure you are logged in to Klaviyo and Olo in separate tabs to streamline the installation.

## Integrate Olo with Klaviyo

### Install the Olo integration in Klaviyo

1. In Klaviyo, select the ****Integrations**** tab.
2. Click ****Explore apps****.
3. Search for **Olo** and select the card.
4. On the next page, click ****Install****.
5. On the next page, click ****Connect to Olo.****
6. Review the permissions and click ****Allow****.
7. Copy the webhook URL that has been generated for you and save it to a secure location.

![](https://klaviyo.zendesk.com/hc/article_attachments/41573712736411)

### Configure webhooks in Olo

1. In Olo, select ****Dev Tools > Webhooks**** in the left navigation bar.
2. Click ****Add Webhook**** in the top right.
   ![The Add Webhook button within Olo.](https://klaviyo.zendesk.com/hc/article_attachments/28716056424091)
3. Fill in the form with the following:
   1. Select all **Order Events** and **User Events**.
      1. Webhook Name: Klaviyo.
      2. Destination URL: The URL you copied in Step 7 in the Install the ****Olo integration in Klaviyo section****.
      3. Developer Partner: Klaviyo (select from dropdown).
      4. Event Type.
4. Click ****Publish Webhook****.

### Completing the installation in Klaviyo

1. Check the setting to sync Olo email subscribers to Klaviyo. Then, select your main email list (or another list, if desired) from the dropdown. We recommend setting this list to[single opt-in](https://help.klaviyo.com/hc/en-us/articles/115005251108#h_01HZ5G5ZQBDHTV20V1BE7D4YAT).
   ![](https://klaviyo.zendesk.com/hc/article_attachments/41574255868827)
2. Check the setting to sync Olo SMS subscribers to Klaviyo. Then, select your main SMS list (or another list, if desired) from the dropdown.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/41574280135835)
3. Click ****Complete setup****.

   Your integration is now activated and profiles, events, and consent updates will start syncing to Klaviyo.

## Understand your Olo data

Klaviyo syncs many different events from Olo related to appointments and membership.

To view your Olo data:

1. Click the ****Analytics**** dropdown in the left-hand navigation sidebar.
2. Select ****Metrics****. Here, you can view all of the metrics in your account. The metrics with an Olo icon represent all of the metrics synced from your Olo integration.
3. Filter this view to see only Olo metrics by using the filter selector next to the search bar.

![List of Olo metrics found within Klaviyo.](https://klaviyo.zendesk.com/hc/article_attachments/28716066864155)

Third party deliveries (Uber Eats, DoorDash, etc.) sync from Olo to Klaviyo, and you can view them in Klaviyo to help understand your order sources. These profiles, though, are automatically suppressed and thus won't count as active profiles for Klaviyo billing.

Learn more about [your Olo data](https://help.klaviyo.com/hc/en-us/articles/15752146245403).

## Segment customers using Olo data

You can use Olo’s metrics to segment customers and target them with a campaign. For example, you can create a segment of everyone who placed an order in the last 30 days and send a campaign to that segment.

![Example segment using Olo metrics.](https://klaviyo.zendesk.com/hc/article_attachments/28716056427803)

To create the example segment shown above:

1. Click the ****Audience**** dropdown in the left-hand navigation sidebar.
2. Click ****Lists & segments****.
3. Click ****Create New**** in the top right.
4. Select ****Create segment****.
5. Name your segment and select tags if desired.
6. Under **Definition**, select ****What someone has done (or not done)**** > ****Placed Order**** > ****at least once**** > ****in the last**** > ****30**** > ****days****.
7. Click ****Create segment****.

## Use Olo data in flows

You can use Olo metrics to trigger flows. For example, you can use the **Placed Order** metric to trigger a flow to send messages to someone immediately when they place an order.

To create a flow using Olo metrics:

1. Navigate to the ****Flows**** tab from the left-hand navigation sidebar.
2. Click ****Create flow**** in the top right.
3. Click ****Build your own**** in the top right.
4. Name your flow and select tags if desired.
5. Click ****Create flow****.
6. In the flow builder, choose ****Placed order**** as the trigger.
   ![Flow builder where you can choose the trigger event](https://klaviyo.zendesk.com/hc/article_attachments/34594327249051)
7. Check that the trigger is set to sync from Olo.
8. Click ****Save****.
9. Add time delays and messages relevant to the triggering action. Learn more about [creating a post-purchase flow](https://help.klaviyo.com/hc/en-us/articles/360028872611).
10. Once your content is ready, click ****Update status**** in the top right of the flow builder to set the flow live.

## Outcome

You've now integrated Olo with Klaviyo and learned about Olo data in Klaviyo, segmenting customers using Olo data, and using Olo data in flows.

## Additional resources

Take our course on [enhancing restaurant guest relationships](https://academy.klaviyo.com/en-us/courses/enhance-restaurant-guest-relationships).

Learn more about [Klaviyo-built integrations](https://help.klaviyo.com/hc/en-us/articles/115000256472).

Learn [how often integrations sync data](https://help.klaviyo.com/hc/en-us/articles/115005253208).