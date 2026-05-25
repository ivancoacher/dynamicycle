---
id: "19457831690139"
title: "Thanx data reference"
source_url: "https://help.klaviyo.com/hc/en-us/articles/19457831690139-Thanx-data-reference"
section: "Thanx"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-20T17:29:54Z"
language: "en"
---
## You will learn

Learn what data syncs from Thanx to Klaviyo and where to view it. This includes information related to placed orders and customer profiles.

If you have not already, read our guide on [getting started with Thanx](https://help.klaviyo.com/hc/en-us/articles/19458074597659) for instructions on integrating before continuing with this article.

## How to view your data

To view your Thanx data:

1. Click the ****Analytics**** dropdown in the left-hand navigation sidebar.
2. Select ****Metrics****. Here, you can view all of the metrics in your account. Filter by ****Thanx**** to view your Thanx metrics.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28715966264475)
3. Click on ****Placed Order**** to view detailed metric info.

![](https://klaviyo.zendesk.com/hc/article_attachments/28715966266267)

## Synced metrics

Thanx sends 2 types of purchase payloads:

- ****Data Sharing****
  Sent if the webhook consumer qualifies for data sharing.
- ****No Data Sharing****
  Sent if the webhook consumer does not qualify for data sharing.

**No data sharing**payloads are sent, for example, for mall merchants with locations that have not yet opted into data sharing.

### Placed Order

This event occurs when a customer placed an order through your Thanx loyalty program. You can filter and target Placed Order events based on the following criteria:

- ****Purchase ID****
  Unique identifier for the purchase
- ****Merchant ID****
  Unique identifier for the merchant
- ****Order ID****
  The ID for the order
- ****Order Provider****
  The system that accepted the order
- ****Merchant Name****
  Name of the merchant
- ****Location ID****
  Unique identifier for location of purchase
- ****Location Name****
  Name of the location where the purchase was made
- ****Location****
  Additional information about the location including location ID and address
- ****Items****
  Details about what was purchased

## Synced guest data

In addition to the metrics Klaviyo syncs from Thanx, Klaviyo will also create a unique profile for every customer that we sync, which includes:

- First name
- Last name
- Email address
- Email consent
- SMS consent (includes phone number)
- Thanx Loyalty Tier
- Thanx Loyalty Points Balance
- Thanx Loyalty Start Date
- Thanx Birthday
- Thanx Birthday Year
- Thanx Birthday Month
- Thanx Birthday Day

## Sync frequency

The Thanx **Placed Order** event syncs in real time in an ongoing sync starting from the time you integrate.

Historic guest data syncs upon integration, and then periodically every 30 minutes.