---
id: 360037501212
title: "Understanding Magento 1 data in flows"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360037501212-Understanding-Magento-1-data-in-flows"
section: "Magento 1"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:46Z"
language: en
---

Klaviyo's Magento 1 integration is no longer accepting new installations and will reach full end-of-support in late 2027. Klaviyo Support is no longer able to assist with Magento 1–related requests.

## You will learn

Learn about what Magento 1 data is synced into Klaviyo, along with examples of how you can use that data in flows. When you integrate your Magento 1 account with Klaviyo, you'll have access to both historic and dynamic Magento 1 data that you can use in Klaviyo to personalize your customers' experience. There are many excellent ways to do this through the use of Klaviyo flows.

For a deep dive into your Magento 1 data: [Review and Understand your Magento 1 Data](https://help.klaviyo.com/hc/en-us/articles/115005254528-Review-and-Understand-your-Magento-1-Data).

Magento 1 data can be used to trigger flows and populate flow emails.

## Flow timing

Flow delays are carefully timed to ensure that your content is relevant to your customers’ experience. When you set up your flows, keep in mind the general timing of your Magento 1 sync.

Magento 1 syncs with Klaviyo every 30 minutes.

For example, if you set your first abandoned cart email to send 15 minutes after someone abandons their cart, your customer may receive this even if they did complete their purchase, since the Placed Order data may not have been synced into Klaviyo before the email was sent. To prevent this from happening, it would be safest to set your delay for a minimum of 45 to accommodate for the Magento general time sync of 30 minutes.

## Abandoned cart flow

Abandoned cart flows are often the highest-revenue flows in a Klaviyo account. Klaviyo provides a pre-built abandoned cart flow which appears in your Flows Library when you integrate with Magento 1.

**Integration requirements:** Magento 1 plugin installs website tracking

**Data you'll use:** [Checkout Started](https://help.klaviyo.com/hc/en-us/articles/115005254528-Review-and-Understand-your-Magento-1-Data#checkout-started4) (Magento 1 metric), dynamic product data

Notice that the **Checkout Started** metric is associated with metadata describing the products added to the cart. You can choose to display or collapse metadata on the event timeline.

**What the metric means:** [Checkout Started](https://help.klaviyo.com/hc/en-us/articles/115005254528-Review-and-Understand-your-Magento-1-Data#checkout-started4) in Magento 1 means that a customer enters their contact and shipping information on the first page of the Magento checkout process and then clicks continue.

**How the metric is triggered:****Checkout Started** in Magento 1 is triggered when someone lands on the checkout page and the customer types into the checkout field; Klaviyo captures the C**heckout Started** event when the email field is changed.  When the Magento cron job runs, the event is synced to Klaviyo.

**Flow name:** Abandoned Cart

**Flow trigger:** Event-based; this flow is triggered by the **Checkout Started** metric

This is an Abandoned Cart flow for a Magento 1 store:
![](https://klaviyo.zendesk.com/hc/article_attachments/28715963355035)

You can create personalized flow emails that feature items left in a customer’s cart by pulling Magento 1 product data using [dynamic template variables](https://klaviyo.zendesk.com/hc/en-us/articles/115000096232) into an email [text block](https://help.klaviyo.com/hc/en-us/articles/115005082447-The-Email-Template-Editor#text-blocks4).

**Learn more:** [How to create an abandoned cart flow](https://klaviyo.zendesk.com/hc/en-us/articles/115002779411)

## Browse abandonment flow

Browse Abandonment flow is a powerful flow that captures client interest when they view specific products on your website.

Klaviyo only tracks the browsing activity of "known browsers," which are browsers who have visited and engaged with your site at least once before. There are 2 key ways we are able to identify a site visitor:

1. If someone clicks through a Klaviyo email to your website.
2. If someone subscribes or opts in through a Klaviyo form. Anonymous browsers are not tracked.

Klaviyo provides a pre-built Browse Abandonment flow in your Flows section, but you can [easily create your own.](https://klaviyo.zendesk.com/hc/en-us/articles/115002775252)

**Integration requirement:** the Magento 1 plugin automatically installs the Viewed Product code snippet. If you have not yet implemented Viewed Product tracking in Magento 1, head over to [Integrate with Magento 1](https://help.klaviyo.com/hc/en-us/articles/115005082187-Integrate-with-Magento-1-x-CE-and-EE-#install-the-klaviyo-extension-in-magento4)

**Data you'll use: Viewed Product** (Klaviyo metric), dynamic product data

**What the metric means:** [**Viewed Product**](https://help.klaviyo.com/hc/en-us/articles/360030732832-Review-and-Understand-Your-WooCommerce-Data#viewed-product5) is tracked when a customer views a product.

**Flow name:** Browse Abandonment

**Flow trigger:** Metric-based; this flow is triggered by the **Viewed Product** metric

This is a Browse Abandonment flow for a Magento 1 store:
![](https://klaviyo.zendesk.com/hc/article_attachments/28715969966491)

**Learn more:** [Guide to Creating a Browse Abandonment flow](https://help.klaviyo.com/hc/en-us/articles/115002775252-Create-a-Browse-Abandonment-Flow)

## Cross-sell and product review flow

Cross-sell flows allow you to target a group of people that have all purchased a particular item, but have not also purchased one or more related items. For example, if someone purchases a video game console, you might consider sending them an email about the most popular video games for that console that they haven't yet purchased.

Product review flows also allow you to target a group of people who purchase a particular item. You may want to filter your cross-sell/product review flow by category or collection so you can provide more relevant recommendations in the content of your emails.

Klaviyo offers a pre-built Product Review/Cross-Sell flow which can be found in your [Klaviyo Flow Library](https://klaviyo.zendesk.com/hc/en-us/articles/115002774932).

**Integration requirement:** an active Magento 1 integration

**Data you'll use:** either the **Fulfilled Order** metric or the **Ordered Product** metric (both Magento 1 metrics)

**What the metrics mean:**

- **Fulfilled Order** (Magento 1 metric) tracks when you mark an order in your Magento store as shipped.
- **Ordered Product** (Magento 1 metric) tracks when a customer places their order. One Ordered Product event is tracked for each item someone purchases.

**Flow name:** Product Review/Cross Sell

**Flow trigger:** Event-based; **Fulfilled Order** metric

This is a Product Review/Cross-Sell flow for a Magento 1 store:
![](https://klaviyo.zendesk.com/hc/article_attachments/28715969958811)

You can personalize your cross-sell emails with catalog or product feeds. For more information [learn how to us product feeds and recommendations](https://klaviyo.zendesk.com/hc/en-us/articles/115005082787).

**Learn more:** [Create a product review flow](https://help.klaviyo.com/hc/en-us/articles/115002779391-Create-a-Product-Review-Flow) or [create an upsell or cross sell flow](https://help.klaviyo.com/hc/en-us/articles/115002775212-Create-an-Upsell-or-Cross-Sell-Flow)

## Customer winback flow

Winback flows are used to re-engage inactive customers before they completely disengage with your brand. Consider [adding past profiles](https://help.klaviyo.com/hc/en-us/articles/115002779231-Back-Populate-a-Flow) to your winback flow after setting it up to ensure that anyone who purchased a long time ago but hasn't purchased since can receive your winback series in a timely manner. Let's say, for example, your first winback email is set to send out 6 months after someone makes a purchase. Rather than wait 6 months until someone qualifies to receive this email, you can add past profiles to the flow so that everyone who placed an order 6 months ago but hasn't purchased since will receive the email right away.

Klaviyo provides a pre-built Customer Winback flow in your Flows section, but you can also easily [build your own](https://klaviyo.zendesk.com/hc/en-us/articles/115002775192).

**Integration requirement:** an active Magento 1 integration

**Data you'll use:** **Placed Order**(Magento 1 metric)

**What the metric means:** [Placed Order](https://help.klaviyo.com/hc/en-us/articles/115005254528-Review-and-Understand-your-Magento-1-Data#placed-order7) is tracked when a customer completes the checkout process and creates an order in your Magento 1 store.

**Flow name:** Customer Winback Flow

**Flow trigger:** Metric-based; this flow is triggered by the **Placed Order** metric

Flow filter: **Placed Order** zero times since starting this flow

This is a Customer Winback flow for a Magento 1 store:
![](https://klaviyo.zendesk.com/hc/article_attachments/28715969973915)

You can personalize your winback emails with catalog or product feeds. For more information review [product feeds and recommendations](https://klaviyo.zendesk.com/hc/en-us/articles/115005082787).

**Learn more:** [Create a winback flow](https://klaviyo.zendesk.com/hc/en-us/articles/115002775192)

## Are you using Amazon Buy with Prime?

If you're using Buy with Prime to power payment and fulfillment for any of the products on your store, you'll need to make some additions to your flows, and create some new flows. First:

- [Integrate Buy with Prime with Klaviyo](https://help.klaviyo.com/hc/en-us/articles/14708088221467) to bring Buy with Prime data into your Klaviyo account.

For your abandoned cart flow:

- Create 2 separate abandoned cart flows: 1 triggered by Magento's checkout event (as described above), and 1 triggered by Buy with Prime's checkout event. For your Buy with Prime flow, read [How to create an abandoned cart flow for Amazon Buy with Prime](https://help.klaviyo.com/hc/en-us/articles/14985388418331).
- For your Magento abandoned cart flow, add the following flow filter to exclude customers who made purchases via Buy with Prime from receiving incorrect messaging:
  - **Placed Order** (Buy with Prime) **zero times since starting this flow.**

For your browse abandonment flow:

- When you create your browse abandonment flow (you only need to create one flow, since it's triggered by the **Viewed Product** event) add the following flow filters to incorporate Buy with Prime data into your flow:
  - **Checkout Started** (Buy with Prime) **zero times since starting this flow**AND
  - **Placed Order**(Buy with Prime)**zero times since starting this flow**.

For your customer winback flow:

- Create two separate winback flows: one triggered by Magento's **Placed Order** event (as detailed above) and one triggered by Buy with Prime's **Placed Order** event to account for customers who placed their original order with Buy with Prime. For your Buy with Prime winback flow, read [How to create a winback flow for Amazon Buy with Prime](https://help.klaviyo.com/hc/en-us/articles/15156331062171).
- When you create your Magento winback flow, add the following flow filter to exclude customers who made purchases via Buy with Prime from receiving incorrect messaging:
  - **Placed Order** (Buy with Prime) **zero times since starting this flow.**

## Additional resources

- [How to integrate with Magento 1.x (CE and EE)](https://klaviyo.zendesk.com/hc/en-us/articles/115005082187)
- [Magento 1 data reference](https://klaviyo.zendesk.com/hc/en-us/articles/115005254528)