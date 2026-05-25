---
id: "22311212640027"
title: "Understanding when and how to use custom conversion metrics"
source_url: "https://help.klaviyo.com/hc/en-us/articles/22311212640027-Understanding-when-and-how-to-use-custom-conversion-metrics"
section: "Metrics best practices"
category: "Analytics"
category_slug: "analytics-audience"
klaviyo_updated: "2026-04-21T13:54:34Z"
language: "en"
---
## You will learn

Learn best practices for when to use and create custom metrics. By default, Klaviyo provides metrics that track your business’s performance and measure success (e.g., a **Placed Order** event). However, there may be instances where you need to create custom metrics to more accurately capture how your business runs. For example, your **Placed Orders** events include recurring subscriptions by default, and you’d like to review only orders placed through your ecommerce website. This article walks you through common use cases for creating different types of custom metrics.

For information on setting up custom metrics, visit our guide on [configuring custom metrics](https://help.klaviyo.com/hc/en-us/articles/22311085738395/).

Please note that this guide walks through the most common use cases, but does not reflect all the potential possibilities of custom-created metrics.

Custom metrics cannot currently be used in segmentations, triggering, splitting, or filtering flows, or found on a profile itself. Custom metrics are currently limited to a subset of reports. More information on where to find custom metric information in reporting [noted below](#h_01HN3978N02P12Y36T5KCJ7ZQ8).

## Before you begin

Depending on your subscription provider, e-commerce integration, or e-commerce platform implementation, your custom metric creation may differ slightly.

For customers using Klaviyo’s marketing application, you have access to create 1 custom metric. For customers also using Advanced KDP or Marketing Analytics, you have increased flexibility to create up to 50 custom metrics. To learn more about these plans, head to our [billing guide](https://help.klaviyo.com/hc/en-us/articles/115000976672).

Any time you adjust this custom metric, applicable reporting will update. Reporting where you can use this custom metric includes:

And any time you adjust a custom metric, applicable reporting will update. Reporting where you can use this custom metric includes:

- The [home dashboard](https://help.klaviyo.com/hc/en-us/articles/9974064152347) (main dashboard that greets you when logging in)
- [Business review dashboards](https://help.klaviyo.com/hc/en-us/articles/16427152766619) (within the dashboards section)
- [Overview or analytics dashboards](https://help.klaviyo.com/hc/en-us/articles/4708299478427) (within the dashboards section)
- [Flow performance reports](https://help.klaviyo.com/hc/en-us/articles/360047044892) (within custom reports)
- [Campaign performance reports](https://help.klaviyo.com/hc/en-us/articles/360047022912) (within custom reports)
- [Single](https://help.klaviyo.com/hc/en-us/articles/360046242952) and [multi-metric reports](https://help.klaviyo.com/hc/en-us/articles/360046234772) (within custom reports)
- Within flow analytics (in the flows list page itself)
- Within [campaign conversions](https://help.klaviyo.com/hc/en-us/articles/115005199947#section1) (in the campaigns list page itself)
- The [audience performance report](https://help.klaviyo.com/hc/en-us/articles/17798068936219) (Advanced KDP and Marketing Analytics customers only)
- The [conversion overview dashboard](https://help.klaviyo.com/hc/en-us/articles/28474458127899) (Advanced KDP and Marketing Analytics customers only)
- The [customer lifetime value (CLV) dashboard](https://help.klaviyo.com/hc/en-us/articles/17797912816795) (Advanced KDP and Marketing Analytics customers only)
- The [recency, frequency, and monetary (RFM) analysis report](https://help.klaviyo.com/hc/en-us/articles/17797889315355) (Advanced KDP and Marketing Analytics customers only)
- The [product analysis dashboard](https://help.klaviyo.com/hc/en-us/articles/26685770823451) (Advanced KDP and Marketing Analytics customers only)

## Removing or excluding certain events

There may be instances where you want to separate out certain events from your default metrics to analyze performance more accurately, especially if you are on an integration that automatically combines different customer events—like recurring and one-time purchases, or in-store and online purchases. This way, you more accurately analyze what marketing strategies are contributing to your revenue.

The sections below walk through these in more detail, depending on your integration and needs.

### Removing recurring subscription events with Shopify, WooCommerce, or BigCommerce

As noted above, standard Shopify integrations, WooCommerce, and BigCommerce will include subscriptions in **Placed Order** events automatically. This means that they are calculating both ecommerce and subscription orders together. In the example below, by using does not equal, you can isolate and review **Placed Order** metrics that do not include subscription orders.

![source name does not equal subscriptoin.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28717995043867)

Keep in mind that as of December 2023, for BigCommerce, all order events from subscription providers should pull into the **Source Name** field automatically. If you are not seeing these values reflected in the metric setup, you will need to delete and run a historical sync of **Placed Order** data to have this pull in.

### Separating retail and ecommerce events (Shopify or other custom integrations)

With Shopify and some custom integrations, physical retail (POS) and e-commerce orders will come through as a single event (e.g., Shopify **Placed Order** event).

However, if you would like to separate these out to see the efficacy of each individual event type, you can set up a custom metric like the example below. Here, the point of sale (POS) is not being included in the **Placed Order** event and combined with other ecommerce data.

![source does not equal pos.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28717995036443)

### Separating certain brands or types of products purchased

If your business has certain sub-brands or product types within your catalog, you may find that you want to see the data of some types vs. others. For example, if your company sells third-party products besides your own, you may want to see how revenue compares between your products and these third-party ones.

In the example below, it has targeted third-party products to be excluded from **Placed Order** events. You could also individually add all third-party products or brands here if they are individually set up in your ecommerce store.

![metric third party does not contain.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28718022871707)

## Capturing or combining events

You may run a business that has many types of revenue or customer events, outside of the default Klaviyo events.

For example, you may have a business that includes:

- A subscription model (and you are not on an integration that automatically adds these to your **Placed Order** events)
- Paid virtual classes
- Lead generation or sign-ups in person
- In-person point of sale/physical retail locations (where the data is held in different systems or integrations).

The sections below walk through the most common ways to combine these different metric events.

### Adding in subscriptions

#### For Shopify, BigCommerce, or WooCommerce

By default, standard Shopify integrations (not including headless implementations), BigCommerce, and WooCommerce automatically include subscriptions within **Placed Order** events. If you need information on how to exclude these events, check out the section above on removing subscription orders.

#### For ecommerce integrations (non-Shopify, BigCommerce, or WooCommerce)

In the custom metric example below, **Placed Order** events will now include subscriptions as well as regular ecommerce orders. When setting up this custom metric, it’s important to make sure that the **Source Name** matches the name of your subscription value (here it’s just “subscription”). Additionally, make sure that the **Relationship** is reflected as **contains**.

![source namd contains subscription.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28717995041819)

Once you update your **Placed Order** metric to include subscription conversions, your Klaviyo reporting will reflect this new combination of revenue events.

Magento2 and WooCommerce pass their data in a way that makes it challenging for Klaviyo to accurately recognize subscription reporting. In these instances, it may not make sense to create subscription-specific custom metrics.

### Adding in other non-subscription revenue events

#### For any integration

If your business conducts other revenue generating practices such as live events, classes, webinars, etc. you may want to combine these into your **Placed Order** events as well.

As shown in the example below, by using **Source name** and **contains** you can include all live classes in your **Placed Order** custom metric. This way, you are capturing all revenue from both your website and classes that happen either in person or purchased via a different platform.

![source name contains live class.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28718022882715)

## Additional resources

[How to configure custom conversion metrics](https://help.klaviyo.com/hc/en-us/articles/22311085738395/)
[Analytics glossary](https://help.klaviyo.com/hc/en-us/articles/360037957832)
[Understanding how Klaviyo billing works](https://help.klaviyo.com/hc/en-us/articles/115000976672#01H84M7N02NW9Z4RKQRP3D76YY)