---
id: "360039002832"
title: "Meta Ads data reference"
source_url: "https://help.klaviyo.com/hc/en-us/articles/360039002832-Meta-Ads-data-reference"
section: "Meta Ads"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-17T00:33:08Z"
language: "en"
---
## You will learn

Learn about the data that syncs from Meta Ads to Klaviyo, and from Klaviyo to Meta, through Klaviyo's Meta Ads integration.

## Before you begin

Before data can flow into your Klaviyo account, you must first [integrate with Meta Ads](https://klaviyo.zendesk.com/hc/en-us/articles/115005082127), which includes syncing a Klaviyo list or segment with a Meta audience, and/or syncing a Lead Ad.

## Data synced with Meta audiences

You can sync your Klaviyo lists and segments with Meta audiences. Klaviyo pushes email addresses to a Meta audience in a one-way sync. Due to Meta limitations, custom audiences can take 24-48 hours to update in Meta.

This is how data is synced between Klaviyo and Meta audiences:

- Klaviyo pushes email addresses to a Meta audience.
- Only email addresses associated with a Facebook login will be synced, so the size of your audience may not exactly match the size of your list/segment.
- As profiles are added or removed from the list or segment, they will also be added or removed from the Meta audience.

## Data synced from Lead Ad forms

When you connect a Lead Ad forms to Klaviyo lists, profile information is added to the list you select. Only lists, not segments, can be synced with Lead Ad forms. Lead Ad forms can be placed on both Facebook or Instagram, so profile information can be pulled from either social media source. Data from lead ads syncs to Klaviyo in real time.

### Profile information

The design of your Lead Ad form determines what information is pulled into Klaviyo. For example, a Lead Ad with fields for **email address** and **first name** will pull in that information. If you include a **phone number** field on your Lead Ad form, a phone number will be pulled in as well.

### Filled Out Lead Ad metric

When a person signs up via a Lead Ad form, the person’s profile information is synced into Klaviyo along with a **Filled Out Lead Ad** metric.

In Klaviyo, you can navigate to your account's ****Metrics**** tab (in the ****Analytics**** dropdown) to view all of the metrics in your account; the **Filled Out Lead Ad** metric is associated with a Meta icon. You can filter this view to see only Meta Ads metrics by using the filter selector.

The **Filled Out Lead Ad** metric is triggered when a person subscribes via a Lead Ad form either on Facebook or Instagram. The metric is associated with additional properties known as metadata.

This is a list of metadata associated with the **Filled Out Lead Ad** metric:

- ****AdID****
  The Ad Form ID; this can be located within your Facebook Ad Account
- ****AdName****
  The name of the Ad
- ****AdsetName****
  The name of the parent Ad Set
- ****CampaignName****
  The name of the Campaign that contains the ad
- ****FormName****
  The Lead Ad sync label
- ****PageName****
  The page the ad is displayed on
- ****Platform****
  The platform on which the ad appears: either Facebook (fb) or Instagram (ig)

Klaviyo gives you the ability to filter and segment based on all metrics and metadata pulled into your account, so you can customize your customer journey on a granular level.

## Additional resources

- [How to integrate with Meta Ads](https://help.klaviyo.com/hc/en-us/articles/115005082127-How-to-Integrate-with-Facebook-Advertising)
- [Getting started with advanced targeting on Facebook and Instagram](https://help.klaviyo.com/hc/en-us/articles/360039769672-Guide-to-Advanced-Targeting-on-Facebook-and-Instagram)