---
id: "13913401149595"
title: "Understanding how Klaviyo monitors metric activity for flows"
source_url: "https://help.klaviyo.com/hc/en-us/articles/13913401149595-Understanding-how-Klaviyo-monitors-metric-activity-for-flows"
section: "Test and optimize flows"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-04-21T13:54:27Z"
language: "en"
---
Learn how Klaviyo monitors and alerts you of unusual activity with ecommerce metrics that are used to trigger flows in your Klaviyo account. When a metric has a sudden drop in activity, you will be alerted so you can troubleshoot the potential issue. This type of monitoring is also known as anomaly detection.

### Which metrics are monitored?

Metric alerts support ecommerce metrics such as **Placed Order**, **Fulfilled Order, Started Checkout**, and **Added to Cart**, and also support custom metrics set up with Klaviyo's [Metrics API](https://developers.klaviyo.com/en/reference/metrics_api_overview) and [Events API](https://developers.klaviyo.com/en/reference/events_api_overview).

## Before you begin

If you have not done so, enable and configure an ecommerce integration in your account. To get started, see Klaviyo’s [list of ecommerce integrations](https://help.klaviyo.com/hc/en-us/articles/115000256472). Otherwise, work with a developer to [create a custom integration using Klaviyo’s APIs](https://developers.klaviyo.com/en/docs/guide_to_integrating_a_platform_without_a_pre_built_klaviyo_integration).

## How metric monitoring works

Klaviyo will alert you if there is a sudden drop in activity for one of your ecommerce metrics compared to historical activity for your account.

When an unusual drop in metric activity is detected, you will be notified several different ways:

- Email to the account owner, admins, and managers
- In-app notification
- At the top of the **Home** tab
  ![](https://klaviyo.zendesk.com/hc/article_attachments/40155941349147)
- On the **Flows** tab next to the title of the affected flow
  ![](https://klaviyo.zendesk.com/hc/article_attachments/40155941352731)
- In the sidebar of the flow builder when clicking on the flow trigger

![](https://klaviyo.zendesk.com/hc/article_attachments/40155941354907)

## Dismiss or suppress alerts

If the drop in activity is expected or is already under investigation, you can dismiss or suppress alerts to prevent them from showing in your account.

- Dismissing an alert will cause the alert message to disappear until it is triggered again.
- Suppressing an alert will prevent the alert from triggering again for that metric until the amount of time specified.
  - ****Suppress for 30 days****
  - ****Suppress for 60 days****
  - ****Suppress for 120 days****
  - ****Suppress for 365 days****

  To dismiss an alert:

  1. If you are on the **Home** tab, navigate to the affected flow by clicking ****View affected flow**** on the metric alert. Otherwise, navigate to the affected flow from the **Flows** tab.
  2. Click on the trigger of the flow.
  3. In the trigger settings sidebar, click ****Dismiss****.

     To suppress an alert:
  4. If you are on the **Home** tab, navigate to the affected flow by clicking ****View affected flow**** on the metric alert. Otherwise, navigate to the affected flow from the **Flows** tab.
  5. Click on the trigger of the flow.
  6. Click the arrow next to the ****Dismiss**** button.
  7. Click one of the following options:

After choosing a suppression option, a success message will appear with the date when the suppression expires. Once the suppression period is over, if drops in activity are still detected, alerts will continue to trigger until you suppress them again.

## Troubleshoot a sudden drop in activity

While a sudden drop in activity can be alarming, there are some common explanations for this occurrence. Causes specific to your ecommerce store include:

- Maintenance on your store or the server on which your store is hosted
- Temporary server outages for your ecommerce platform

  Check your store’s settings or internal logs for any scheduled maintenance. If you are hosted on a paid platform such as Shopify or BigCommerce, check their publicly available status page for information on server outages and downtime. Status pages usually consist of the the service’s main URL with the status subdomain added to beginning such as the examples below:
- [https://status.shopify.com](https://status.shopify.com/)
- <https://status.bigcommerce.com>

For causes specific to Klaviyo, review the sections below. Click the section relevant to your issue to learn more.

****Have you switched to a different ecommerce platform recently?****

When you migrate ecommerce platforms, make sure to update the metrics used to trigger your flows to the metrics for your new ecommerce platform. For example, if you were to switch from BigCommerce to Shopify, your account’s existing flows may still be set to use BigCommerce’s **Placed Order** metric rather than Shopify’s **Placed Order** metric.

See the guides below for further assistance:

- [How to change a flow trigger](https://help.klaviyo.com/hc/en-us/articles/115002775052-How-to-change-a-flow-trigger)
- [Updating Klaviyo after switching ecommerce platforms](https://help.klaviyo.com/hc/en-us/articles/360003124151-Updating-Klaviyo-After-Switching-Ecommerce-Platforms)
- [How to change the conversion metric for flow and campaign reports](https://help.klaviyo.com/hc/en-us/articles/115005199947-How-to-Change-the-Conversion-Metric-for-Flow-and-Campaign-Reports)

****For BigCommerce, have you changed your store’s theme?****

Some metrics such as **Viewed Product** and **Added to Cart** require installing code snippets into your store’s theme files. If you changed your store’s theme, make sure you re-install these code snippets.

For **Viewed Product**, see the setup guides for this integration:

- [Getting started with BigCommerce](https://help.klaviyo.com/hc/en-us/articles/115005082547#add-viewed-product-tracking4)

  For **Added to Cart**, see this article:
- [How to create an "Added to Cart" event for BigCommerce](https://help.klaviyo.com/hc/en-us/articles/360024310292-How-to-create-an-Added-to-Cart-event-for-BigCommerce)

****Are you using a custom or third-party integration?****

While Klaviyo provides resources for the development of custom and third-party integrations, these types of integrations are created and managed without Klaviyo’s direct involvement. If you are experiencing issues with such an integration, please contact your development team or the support team associated with the third-party integration for further assistance.

For more information on API calls, see our article on [getting started with Klaviyo APIs](https://help.klaviyo.com/hc/en-us/articles/360045726811#make-your-first-call4).

****Is your ecommerce integration enabled and configured in Klaviyo?****

There are a few common scenarios which can cause a previously working integration to stop:

- If you were using a free trial for your ecommerce platform and the trial has expired.
- If the URL for your store has changed but was not updated in Klaviyo.
- If you reinstalled your integration but did not fully configure it.

If you are using one of Klaviyo’s pre-built integrations, follow these steps to confirm your ecommerce integration is installed and enabled:

1. Select the ****Integrations**** tab.
2. Look for the name of your ecommerce platform.
3. Check to make sure that the **Status** column lists the integration as **enabled**.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28720896311451)
4. If your ecommerce integration is not listed as enabled, [search for the setup guide in Klaviyo’s Help Center](https://help.klaviyo.com/hc/en-us/articles/115000256472) for further instructions.
5. If your ecommerce integration is enabled, select it to view its configuration.
6. Review the content of the integrations settings page. Depending on the integration,
   make sure the correct information is entered for fields related to your store URL or any credentials.
7. If necessary, correct any information on the settings page and click ****Update Settings****, ****Save****, or ****Connect**** at the bottom of the page.

****Are you using a firewall or security software on your server?****

If you have a firewall or security measures such as Sucuri, Cloudflare, or something similar, this may inadvertently block Klaviyo from communicating with your store or rate limit the speed and amount of data that can be synced.

Learn how to [allowlist Klaviyo integration traffic](https://help.klaviyo.com/hc/en-us/articles/19143781289115).

### Review our troubleshooting guides for specific metrics

If you could not find your solution in the previous sections, see these articles for additional troubleshooting steps on specific metrics:

- [Troubleshooting Viewed Product tracking](https://help.klaviyo.com/hc/en-us/articles/4416172774939-Troubleshooting-Viewed-Product-tracking)
- [Troubleshooting Added to Cart tracking](https://help.klaviyo.com/hc/en-us/articles/6985692431259-Troubleshooting-Added-to-Cart-tracking)
- [Troubleshooting Started Checkout tracking](https://help.klaviyo.com/hc/en-us/articles/6998274713371-Troubleshooting-Started-Checkout-tracking)
- [Troubleshooting Placed Order tracking](https://help.klaviyo.com/hc/en-us/articles/7000906101019-Troubleshooting-Placed-Order-tracking)