---
id: "41008338238875"
title: "Understanding omnichannel attribution"
source_url: "https://help.klaviyo.com/hc/en-us/articles/41008338238875-Understanding-omnichannel-attribution"
section: "Attribution (Advanced KDP and Marketing Analytics)"
category: "Advanced KDP & Marketing Analytics"
category_slug: "advanced-kdp-marketing-analytics"
klaviyo_updated: "2026-04-21T13:54:56Z"
language: "en"
---
## You will learn

Learn what changes you should make to your account when enabling omnichannel attribution to improve the quality of omnichannel attribution data. What steps you need to take when enabling omnichannel attribution to capture site sessions for each customer who places an order on your site. As part of this guide, you may need to update settings within your Klaviyo account or e-commerce storefront, and in some instances you may need to add a custom javascript snippet to your checkout page.

## Before you begin

[Advanced KDP](https://help.klaviyo.com/hc/en-us/articles/17655007276059) and [Marketing Analytics](https://help.klaviyo.com/hc/en-us/articles/33789259613595) are not included in Klaviyo’s standard marketing application, and a subscription is required to access the associated functionality.Head to our [billing guide](https://help.klaviyo.com/hc/en-us/articles/115000976672) to learn about how to purchase these plans.

## How does omnichannel attribution work?

Omnichannel attribution works by using site sessions from the Active on Site event in addition to Klaviyo message interactions in your attribution model. Omnichannel attribution is available for all types of Klaviyo attribution models.

Klaviyo’s onsite javascript functions as a tracking pixel to track site sessions for all identified site visitors and tracks these sessions in every account using the Active on Site metric, to learn more about the Active on Site metric click here. Omnichannel attribution will add these site sessions into attribution along with interaction events with Klaviyo owned messages to provide you with a holistic view into performance across your marketing strategy, and will capture any attribution which can be tracked as a site session.

Please note Active on Site events will only be used in Attribution after 4/19/2025, prior to 4/18/2025 attribution will Klaviyo message interaction events only.

## Omnichannel attribution methodology

Once Active on Site events are included in your attribution model, Klaviyo’s omnichannel will use any site sessions including direct sessions which meet the following criteria:

- Originated from sources other than Klaviyo messages
- Does not have a UTM Source equal to Klaviyo
- Has at least a UTM Medium or UTM Source

Active on Site events are treated the same as Klaviyo message interaction events, and there is no bias towards Klaviyo’s messages or channels in Klaviyo’s attribution model.

You can enable omnichannel attribution by including Active on Site events in attribution and more information on updating your account's attribution model can be found [here](https://help.klaviyo.com/hc/en-us/articles/11118357030555)

## Overview

To access omnichannel attribution analytics you can navigate to Advanced>Marketing analytics>Attribution

![](https://klaviyo.zendesk.com/hc/article_attachments/41008329452827)

Klaviyo offers two views into omnichannel attribution data:

- Platform performance: How your marketing across different channels and platforms performed overtime. If you have not enabled omnichannel attribution by adding Active on Site events into attribution the Platform performance page will show a simple preview and provide an in-app set up guide.
- Campaign insights: Performance of specific campaigns for non-Klaviyo owned marketing shown at the UTM campaign, platform, and media type level

## Key Concepts

### Platforms and Media types

Omnichannel attribution provides views into the performance of platforms and media types

- Platforms - Provides information about where the traffic originated from. Platforms are currently identified using UTM Source on Active on Site events. Currently Klaviyo supports a fixed list of platforms based on each platform’s default UTM’s, and if we do not have a mapping for a given UTM Source we will aggregate the data into an Unknown grouping.
- Media type - Provides detail on the type of engagement that drove the traffic from a platform. Media Types are classified using UTM Medium on Active on Site events. Currently Klaviyo supports a fixed list of Media Types - Owned, Paid, Organic, and Unknown

A list of the currently supported Platform and Media Type mappings can be found [here](https://docs.google.com/spreadsheets/d/1hmWYau597boWs4F69ajhieeWMNXZX6EQv9DjKSh3TuQ/edit?usp=sharing)

### Metric definitions

When reviewing analytics for omnichannel attribution, and the key definitions are:

- Sessions: The number of Active on Site events identified for a platform and media type or campaign
- Conversion rate - Klaviyo: For Klaviyo platform and channels we follow the standard product definition - # of unique profiles with an attributed conversion for each message / # of messages received
- Conversion rate - non-Klaviyo platforms: For all non-Klaviyo platforms - # unique profiles with an attributed conversion for each site session / # of site sessions

## Frequently asked questions

### Can I filter out direct sessions in Attribution?

Today that is not possible

### Can I break down the unknown platform and media types into new or existing groupings?

Today that is not possible

### Can I customize how platforms are mapped in on the Platform Performance report?

Today that is not possible

### Why am I seeing attribution to a platform that I am no longer actively using?

Site visitors commonly visit from various bookmarks and saved links, and these visits will at times generate an Active on Site event which we can attribute to.

### Why am I seeing differences in attribution when in Klaviyo’s omnichannel attribution compared to other attribution products like Google Analytics (GA4)?

There are a few common sources of discrepancies in attribution between attribution in Klaviyo and other products which include:

1. Attribution model and model configuration - Products like GA4 uses a data-driven attribution model with a fixed lookback window for site sessions whereas Klaviyo leverages a more flexible configuration and by default uses last touch attribution
2. Attributable interaction events - Klaviyo leverages a blend of message interaction events for messages sent using Klaviyo in addition to site sessions for attributing to platforms and channels outside of Klaviyo
3. Conversion or Order data capture - Klaviyo leverages direct integrations with various platforms rather than relying on a client side JS to publish conversions and order events to your account and because of this Klaviyo captures orders from a variety of sources including POS, recurring subscription purchases, manual orders, and more. You can customize your Klaviyo conversion metrics using Custom Conversion Metrics and more details can be found here.