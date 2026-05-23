---
id: 7000906101019
title: "Troubleshooting placed order tracking"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/7000906101019-Troubleshooting-placed-order-tracking"
section: "Metrics troubleshooting"
category: "Analytics"
category_slug: "analytics-audience"
klaviyo_updated: "2026-04-21T13:55:05Z"
language: en
---

## Before you begin

**Placed Order** tracking is included with ecommerce integrations and does not require any additional setup. Before consulting this guide, make sure you have properly set up, configured, and enabled your ecommerce integration.

For all ecommerce integrations, a **Placed Order** event tracks when a customer completes the checkout process and creates an order in your store, but for the following integrations, Klaviyo tracks a **Placed Order** event only when an order reaches a certain state and has a certain status in the eCommerce platform:

- [BigCommerce](https://help.klaviyo.com/hc/en-us/articles/115005082587)
  By default, any order with any of the following statuses will not sync as a **Placed Order**: **Incomplete**, **Pending**, **Awaiting Payment**
- [Magento 2](https://help.klaviyo.com/hc/en-us/articles/115003458852)
  Orders with status **pending\_payment** will be ignored
- [WooCommerce](https://help.klaviyo.com/hc/en-us/articles/360030732832)
  Order must have a status of **processing** to trigger a **Placed Order** event
- [PrestaShop](https://help.klaviyo.com/hc/en-us/articles/360055123191)
  Order must have a status of **processing** to trigger a **Placed Order** event
- [Shift4Shop](https://help.klaviyo.com/hc/en-us/articles/115005083107)
  Order must have a status of **2** or **4** to trigger a **Placed Order** event

If you’re using an ecommerce platform without a pre-built Klaviyo integration, or a custom platform, learn [how to enable Placed Order tracking](https://developers.klaviyo.com/en/docs/guide-to-integrating-a-platform-without-a-pre-built-klaviyo-integration#placed-order) on our Developer site.

## Test Placed Order events

The **Placed Order** event is commonly used to set up post-purchase flows such as a thank you flow. If you have recently set up your account and are attempting to create a post-purchase flow from Klaviyo’s Flows Library, you may encounter the following warning message:

"We have not received any recent **Placed Order** events. If you think there might be a problem, contact our Success Team for help."

This does not necessarily mean that there is a problem with your account or integration, but it may mean that no **Placed Order** events have triggered yet. This may be because your store is new. You can trigger an event by following the steps below to cause this warning to disappear.

Because a **Placed Order** event triggers from a transaction, Klaviyo Support is unable to test **Placed Order** event tracking for you.

Some ecommerce platforms such as Shopify offer methods for placing test orders. Consult your platform’s help documentation for information on how to place a test order. Otherwise, you can place a real order and refund it to test your integration.

To test that your **Placed Order** tracking is set up properly using a real transaction, follow these steps:

1. Navigate to your website
2. Navigate to a product page on your site for an available product
3. Click the “Add to Cart” button on the page
4. Proceed to checkout with the item in your cart
5. Complete checkout using a real credit card or other payment method
6. If you're using a third-party payment provider, log into your payment provider to make sure that the funds were processed
7. Cancel and refund the order as soon as possible to refund yourself
8. Search in Klaviyo for the email address you used during checkout

![The searchbar can be found in the top right of Klaviyo where you can search for profiles by email address.](https://klaviyo.zendesk.com/hc/article_attachments/28723544866971)

You should see that a Klaviyo profile has been created for you (if one didn't exist already) and that a **Placed Order** event has been tracked on your activity feed.

Not all ecommerce integrations sync data in realtime due to limitations with some ecommerce platforms. For some integrations, you may need to wait 30 minutes to an hour before events are tracked. Please see our article on [how often integrations sync](https://help.klaviyo.com/hc/en-us/articles/115005253208) for more information.

## Troubleshooting scenarios

Review the following questions in order to diagnose the cause of your **Placed Order** issues. Note that some steps are general, and others depend on what ecommerce platform you are using.

****Are you having issues triggering other metrics as well?****

If you are having issues tracking other metrics as well as **Placed Order**, there may be an issue with your integration’s setup.

Follow these steps to check to see if your integration is set up correctly:

1. If the keys appear to match on both sides, check to see if there are any blank spaces before or after the keys. Delete any leading or trailing blank spaces because they can cause errors.

1. Navigate to the **Integrations** page of your account
2. In the **Enabled Integrations** tab, make sure that your ecommerce integration is in the list. Otherwise, follow the relevant setup guide linked in the [Before you begin section](#h_01G6W9BDQH54CC3N49MYC0PN22) of this article to make sure you have followed all steps correctly for setting up and configuring your ecommerce integration.
3. If your ecommerce integration is enabled, click ****View Settings**** to check for any error messages related to the integration and that all required fields have been filled out.

   ![The integration settings link can be found to the right of each integration in the Enabled Integrations tab.](https://klaviyo.zendesk.com/hc/article_attachments/28723522895515)
4. If your integration requires use of a public API key, private API key, consumer key, and/or consumer secret, make sure the information in Klaviyo matches what is in your ecommerce platform.

****Have you recently switched ecommerce platforms?****

When you migrate ecommerce platforms, make sure to switch the metrics used to trigger your flows and within your analytics to the metrics for your new ecommerce platform. For example, if you were to switch from BigCommerce to Shopify, your account’s analytics and flows may still be set to use BigCommerce’s **Placed Order** metric rather than Shopify’s **Placed Order** metric. See the guides below for further assistance:

- [Updating klaviyo after switching ecommerce platforms](https://help.klaviyo.com/hc/en-us/articles/360003124151-Updating-Klaviyo-After-Switching-Ecommerce-Platforms)
- [How to change the conversion metric for flow and campaign reports](https://help.klaviyo.com/hc/en-us/articles/115005199947-How-to-Change-the-Conversion-Metric-for-Flow-and-Campaign-Reports)
- [How to change a flow trigger](https://help.klaviyo.com/hc/en-us/articles/115002775052-How-to-change-a-flow-trigger)

****Are you using custom order statuses for placed orders?****

For some integrations, the **Placed Order** event triggers in Klaviyo based on specific order statuses. See the [Before you begin section](#h_01G6W9BDQH54CC3N49MYC0PN22) of this article for a list of integrations that have order status requirements.

If you are using non-standard or custom order statuses, please [contact Klaviyo support](https://help.klaviyo.com/hc/en-us/articles/115001002272-How-to-Contact-Support) to have your integration configuration changed to allow for other order statuses to be tracked as **Placed Order** events.

****Are you using a firewall or security software on your server?****

If you have a firewall or security measures enabled such as Sucuri, Cloudflare, or something similar, this may inadvertently block Klaviyo from communicating with your store or rate limit the speed and amount of data that can be synced.

Since Klaviyo uses dynamic IPs, we do not provide a range of IPs to whitelist. Instead, we recommend whitelisting our user agent, which is: ****Klaviyo/1.0****

If you are unsure how to whitelist Klaviyo, please consult the documentation for your security software on how to whitelist a user agent.

****For WooCommerce and Magento users: Are you using the most recent version of your integration plugin?****

If you are using WooCommerce or Magento, problems with **Placed Order** tracking might be related to other issues with your platform’s Klaviyo plugin.

1. If **Placed Order** events aren’t tracking, check to see if the **Started Checkout** event is tracking by searching for **Started Checkout** within ****Analytics > Metrics**** in Klaviyo.
2. If both **Placed Order** and **Started Checkout** aren’t tracking, there may be an issue with your plugin.
3. Check to see if you are using the most up-to-date version of the plugin for your integration. If needed, update to the latest version within WooCommerce or Magento, or you can download the latest version from the relevant platform’s listing.

- [Setup Wizard install](https://marketplace.magento.com/klaviyo-magento2-extension.html)
- [Composer install](https://packagist.org/packages/klaviyo/magento2-extension)

- [Klaviyo WordPress (WooCommerce) plugin](https://wordpress.org/plugins/klaviyo/)
- [Klaviyo Magento 1 extension](https://www.klaviyo.com/media/downloads/MagentoKlaviyo-Latest.tgz)
- Klaviyo Magento 2 extension

## Contact Klaviyo support

If you are still encountering issues after consulting this list and testing your tracking, please reach out in our [Community](https://community.klaviyo.com/got-a-question-1) or to our [Support Team](https://help.klaviyo.com/hc/en-us/articles/115001002272-How-to-Contact-Support).

Learn how to troubleshoot other metrics:

Other resources: