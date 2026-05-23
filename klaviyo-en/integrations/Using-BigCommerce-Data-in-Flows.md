---
id: 360037937891
title: "Using BigCommerce Data in Flows"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360037937891-Using-BigCommerce-Data-in-Flows"
section: "BigCommerce best practices"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:47Z"
language: en
---

## Overview

When you integrate your BigCommerce account with Klaviyo, you'll have access to both historic and dynamic BigCommerce data that you can use to personalize your customers' experience. There are many excellent ways to do this with Klaviyo flows.

For a deep dive into your BigCommerce data, check out our article on how to [Review and Understand your BigCommerce Data](https://klaviyo.zendesk.com/hc/en-us/articles/115005082587).

BigCommerce data can be used to trigger flows and populate content in flow emails. This article will highlight specific types of data with examples of how you can use that data in flows.

## Flow Timing

Time delays allow you to control when someone receives one step in a flow relative to the previous step. This allows you to ensure that your flow emails are timely and relevant. When setting time delays, it's important to consider how often integration events sync with your Klaviyo account if they are being used to trigger a flow.

BigCommerce syncs with Klaviyo in real-time, using webhooks, so you should not expect a delay in when an event occurs in BigCommerce and when it is synced with Klaviyo.

## Abandoned Cart Flow

Abandoned cart emails are one of the most valuable emails for any ecommerce business. They’re an email or sequence of emails sent to someone who added an item to their shopping cart, but failed to complete the purchase. Not contacting these customers is leaving money on the table -- almost 70% of shopping carts are abandoned on average. Klaviyo provides a pre-built abandoned cart flow that appears in your ****Flows**** tab when you integrate with BigCommerce.

**Integration requirements:** BigCommerce plugin installs website tracking

**Data you'll use: [Started Checkout](https://help.klaviyo.com/hc/en-us/articles/115005082587-Review-and-Understand-Your-BigCommerce-Data#started-checkout1)** (BigCommerce metric), dynamic product data
![BCflow5.png](https://klaviyo.zendesk.com/hc/article_attachments/28717381708059)

**What the metric means:** [Started Checkout](https://help.klaviyo.com/hc/en-us/articles/360030732832-Review-and-Understand-Your-BigCommerce-Data#started-checkout1) in BigCommerce means that a customer enters his/her contact and shipping information on the page before the payment page and clicks continue. The event Klaviyo tracks includes all of the product information about the items in someone's cart including product names, images, and category information so you can use that information in your abandoned cart emails.

**Flow name:** Abandoned Cart

**Flow trigger:** Event-based; this flow is triggered by the **Started Checkout** metric

This is an Abandoned Cart flow for a BigCommerce store:
![BCflow3.png](https://klaviyo.zendesk.com/hc/article_attachments/28717388013083)

This is the profile of a person who started checkout, entered an abandoned cart flow, and received the first abandoned cart flow email:
![BCflow11.png](https://klaviyo.zendesk.com/hc/article_attachments/28717388033947)

You can personalize flow emails to feature items left in a customer's cart by pulling BigCommerce product data using [dynamic template variables](https://klaviyo.zendesk.com/hc/en-us/articles/115000096232) into an email [Text Block](https://help.klaviyo.com/hc/en-us/articles/115005082447-The-Email-Template-Editor#text-blocks4).

![BCAbCartEmails.png](https://klaviyo.zendesk.com/hc/article_attachments/28717381705499)

**Learn more:** [Guide to Creating an Abandoned Cart Flow](https://klaviyo.zendesk.com/hc/en-us/articles/115002779411)

## Browse Abandonment Flow

A browse abandonment flow is a powerful flow that captures client interest when they view specific products on your website. Although this flow is not triggered by a BigCommerce metric, the flow incorporates BigCommerce data in flow emails.

Klaviyo is only able to track the browsing activity of "known browsers," which are browsers who have visited and engaged at least once before. There are two key ways we are able to identify a site visitor: if someone has clicked through a Klaviyo email to your website, or if someone has subscribed or opted-in through a Klaviyo form. Anonymous browsers are not tracked.

Klaviyo provides a pre-built browse abandonment flow which appears in your ****Flows**** tab when you integrate with BigCommerce.

**Integration requirement:** you must already have installed the Viewed Product code snippet to your BigCommerce Store. If you have not already added that code, follow these directions to [add Viewed Product for Stencil Themes](https://help.klaviyo.com/hc/en-us/articles/115005082547#add-viewed-product-tracking5) or [Add Viewed Product for Blueprint themes](https://help.klaviyo.com/hc/en-us/articles/115005082627#add-viewed-product-tracking3).

**Data you'll use:** **Viewed Product** (Klaviyo metric), dynamic product data
 ![wooflow15.png](https://klaviyo.zendesk.com/hc/article_attachments/28717381736603)

**What the metric means:** [Viewed Product](https://help.klaviyo.com/hc/en-us/articles/360030732832-Review-and-Understand-Your-BigCommerce-Data#viewed-product5) is tracked when a customer views a product.

**Flow name:** Browse Abandonment

**Flow trigger:** Metric-based; this flow is triggered by the **Viewed Product** metric

This is a Browse Abandonment flow for a BigCommerce store:
 ![wooflow9.png](https://klaviyo.zendesk.com/hc/article_attachments/28717381739931)

You can personalize flow emails to feature viewed items by pulling BigCommerce product data using [dynamic template variables](https://klaviyo.zendesk.com/hc/en-us/articles/115000096232) in an email [Text Block](https://help.klaviyo.com/hc/en-us/articles/115005082447-The-Email-Template-Editor#text-blocks4).

![BCBrowseEmails.png](https://klaviyo.zendesk.com/hc/article_attachments/28717388031515)

This is the profile of a person who viewed several products. Klaviyo tracks this browsing activity as **Viewed Product** events which are stored in the customer's profile:
![BCflow10.png](https://klaviyo.zendesk.com/hc/article_attachments/28717381722011)

**Learn more:** [Guide to Creating a Browse Abandonment flow](https://help.klaviyo.com/hc/en-us/articles/115002775252-Create-a-Browse-Abandonment-Flow)

## Product Review / Cross Sell Flow

Product review flows allow you to target a group of people who purchase a particular item. Cross sell flows allow you to target a group of people that have all purchased a particular item, but have not also purchased one or more related items. For example, if someone purchases a video game console, you might consider sending them an email about the most popular video games for that console that they haven't yet purchased.

You may want to filter your Product Review/Cross Sell flows by category or collection so you can provide more relevant recommendations in the content of your emails.

Klaviyo offers a pre-built Product Review/Cross Sell flow which can be found in your [Klaviyo Flow Library](https://klaviyo.zendesk.com/hc/en-us/articles/115002779211).

**Integration requirement:** an active BigCommerce integration

**Data you'll use:** either the **Fulfilled Order** metric or the **Ordered Product** metric (both BigCommerce metrics)
![BCflow6.png](https://klaviyo.zendesk.com/hc/article_attachments/28717388022043)

**What the metrics mean:**

- **[Fulfilled Order](https://help.klaviyo.com/hc/en-us/articles/115005082587-Review-and-Understand-Your-BigCommerce-Data#ordered-product3)**(BigCommerce metric)is tracked when an order's status updates to either **Shipped** or **Completed**.
- **[Placed Order](https://help.klaviyo.com/hc/en-us/articles/115005082587-Review-and-Understand-Your-BigCommerce-Data#placed-order2)**(BigCommerce metric)is tracked when a customer completes the checkout process and creates an order in your BigCommerce store. Many products can be included in one **Placed Order** event.

**Flow name:** Product Review/Cross Sell

**Flow trigger:** Event-based; **Ordered Product** metric

This is a Product Review/Cross Sell flow for a BigCommerce store:
![BCflow7.png](https://klaviyo.zendesk.com/hc/article_attachments/28717381713307)

You can personalize your cross sell emails with catalog or product feeds. For more information review [Product Feeds and Recommendations](https://klaviyo.zendesk.com/hc/en-us/articles/115005082787).

![BCCrossEmails.png](https://klaviyo.zendesk.com/hc/article_attachments/28717388026651)

This is the profile of a person who purchased and received an item that has been flagged for cross sell. The completion of the order is indicated by the **Fulfilled Order** metric, and the customer has received and opened a flow email:
![BCflow8.png](https://klaviyo.zendesk.com/hc/article_attachments/28717381719323)

**Learn more:** [Create an Upsell or Cross Sell Flow](https://help.klaviyo.com/hc/en-us/articles/115002775212-Create-an-Upsell-or-Cross-Sell-Flow) and [Create a Product Review Flow](https://help.klaviyo.com/hc/en-us/articles/115002779391-Create-a-Product-Review-Flow).

## Customer Winback Flow

Winback flows are used to re-engage inactive customers before they completely disengage with your brand. Consider [back-populating](https://help.klaviyo.com/hc/en-us/articles/115002779231-Back-Populate-a-Flow) your winback flow after setting it up to ensure that anyone who purchased a long time ago but hasn't purchased since can receive your winback series in a timely fashion. Let's say, for example, your first winback email is set to send out six months after someone makes a purchase. Rather than wait six months until someone qualifies to receive this email, you can back-populate the flow so that everyone who placed an order six months ago but hasn't purchased since will receive the email right away.

Klaviyo provides a pre-built Customer Winback flow in your Flows section, but you can also easily [build your own](https://help.klaviyo.com/hc/en-us/articles/115002775192).

**Integration requirement:** an active  BigCommerce integration

**Data you'll use:** **Placed Order**(BigCommerce metric)
![BCflow12.png](https://klaviyo.zendesk.com/hc/article_attachments/28717388037275)

**What the metric means:** [Placed Order](https://help.klaviyo.com/hc/en-us/articles/115005082587-Review-and-Understand-Your-BigCommerce-Data#placed-order2) is tracked when a customer completes the checkout process and creates an order in your BigCommerce store.

**Flow name:** Customer Winback Flow

**Flow trigger:** Metric-based; this flow is triggered by the **Placed Order** metric

Flow filter: **Placed Order** zero times since starting this flow

This is a Customer Winback flow for a BigCommerce store:
![BCflow13.png](https://klaviyo.zendesk.com/hc/article_attachments/28717381731483)

You can personalize your winback emails with catalog or product feeds. For more information review [Product Feeds and Recommendations](https://help.klaviyo.com/hc/en-us/articles/115005082787).
![wooflow27.png](https://klaviyo.zendesk.com/hc/article_attachments/28717388050715)

This is the profile of a person who purchased an item some time ago. They've been a non-purchaser long enough to trigger a winback flow:
![BCflow14.png](https://klaviyo.zendesk.com/hc/article_attachments/28717388042651)

**Learn more:** [Create a Winback Flow](https://help.klaviyo.com/hc/en-us/articles/115002775192)