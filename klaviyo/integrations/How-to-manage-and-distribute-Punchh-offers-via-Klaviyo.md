---
id: 50585012261531
title: "How to manage and distribute Punchh offers via Klaviyo"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/50585012261531-How-to-manage-and-distribute-Punchh-offers-via-Klaviyo"
section: "PAR Punchh"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-05-19T20:05:57Z"
language: en
---

## You will learn

Learn how to create and manage Punchh reward offers directly within Klaviyo and tie them to your existing lists and segments. This allows you to orchestrate sophisticated loyalty experiences while using Klaviyo to handle the distribution, messaging, and attribution.

## Before you begin

Before you can create an offer in Klaviyo, ensure that your Punchh redeemables have been configured in your Punchh account.

## Create an offer

The first step is defining the campaign details for your Punchh campaign in Klaviyo.

1. In Klaviyo, select the ****Integrations**** tab.
2. Click your ****Punchh**** integration.
3. In the **Offer management**section, click ****Create offer.****

![Punchh integration settings page showing connection details, webhook setup, subscriber sync, and offer management.](https://cdn.sanity.io/images/6ct6b26e/help-center-prod/4e973b74ddaacb1191bb086389870128a24d650c-3456x1688.png)

4. Create a new Punchh campaign within Klaviyo and enter the **Name** and **Start date** for your campaign.

- You can select a Start date up to 3 months in the future.

![Screenshot of a marketing platform's 'Create offer' page, showing input fields for campaign details, redeemable assignment, and a warning about final changes.](https://cdn.sanity.io/images/6ct6b26e/help-center-prod/5b2b23ec9dd3c4e3d5289ba079808e7b5eab647a-3456x1662.png)

## Assign redeemables

Once your redeemables are defined, you must decide which customers are eligible for which reward by mapping them to your Klaviyo data.

1. Navigate to the ****Assign redeemable**** section of the offer builder.
2. Create a mapping between your redeemable and a specific ****Klaviyo list or segment****.

You can map a single redeemable to a single Klaviyo list or segment.

![A web application's "Create offer" page, showing "Punchh campaign details" with an open dropdown menu for "Search redeemable" and a warning message.](https://cdn.sanity.io/images/6ct6b26e/help-center-prod/d9c301f2e461ce87b5bb2497be259fb3dadf8991-3456x1662.png)

## Distribute rewards via Klaviyo messages

After you create the offer, Klaviyo will automatically sync profiles in the Klaviyo list or segment to the Punchh segment if they already exist in Punchh. When a profile is issued a reward based on your mapping, Klaviyo records an ****Earned Reward**** metric and a ****Reward**** object via the Punchh integration for that profile.

### Using the Earned Reward metric

To distribute your Punchh rewards using Klaviyo, you can use the **Earned Reward** metric to trigger automated flows, ensuring customers receive their reward notification the moment they qualify. You can also use dynamic blocks to include reward details within your message.

![](https://klaviyo.zendesk.com/hc/article_attachments/50585012249755)

### Using the Reward object

To distribute your Punchh rewards using Klaviyo, you can also use the **Reward** object to trigger automated flows and segment your customers. You can also use dynamic blocks to include reward details within your message.

For example, if you wanted to send a reminder to your customers before their reward expires, you can set up a [date-triggered flow](https://help.klaviyo.com/hc/en-us/articles/35146374047515#h_01JPTG7J0Q843B5XQGRMB6DVXM) on your **Reward** object by referencing the **ExpiringAt** property.

![](https://klaviyo.zendesk.com/hc/article_attachments/50585012251291)