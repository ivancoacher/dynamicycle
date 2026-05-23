---
id: 6998274713371
title: "Troubleshooting started checkout tracking"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/6998274713371-Troubleshooting-started-checkout-tracking"
section: "Metrics troubleshooting"
category: "Analytics"
category_slug: "analytics-audience"
klaviyo_updated: "2026-04-21T13:55:04Z"
language: en
---

## Before you begin

**Started Checkout** tracking is included with many ecommerce integrations and does not require any additional setup. Before consulting this guide, make sure you have properly set up, configured, and enabled your ecommerce integration.

It is important to understand how **Started Checkout** events trigger for different integrations. See the list below for a quick overview on how each ecommerce integration triggers the event. You can click on the name of each integration to learn more.

- A customer is logged into their account, adds something to their cart, then views the checkout page
- A customer who is not logged in adds something to their cart, views the checkout page, and enters a billing email address

- [Shopify](https://help.klaviyo.com/hc/en-us/articles/115005080447)
  Referred to as **Checkout Started** and tracks after a customer fills out the email address field on the checkout page. This applies to both one-page checkout and multi-page checkout.
- [BigCommerce](https://help.klaviyo.com/hc/en-us/articles/115005082587)
  Tracks when a customer enters their contact and shipping information on the first page of the BigCommerce checkout process and clicks “Continue”
- [Magento 1](https://help.klaviyo.com/hc/en-us/articles/115005254528)
  Referred to as **Checkout Started** and tracks when a customer enters their contact and shipping information on the first page of the Magento checkout process and clicks “Continue”
- [Magento 2](https://help.klaviyo.com/hc/en-us/articles/115003458852)
  This event only tracks if the customer does not proceed to place an order by the time a Magento 2 periodic sync occurs (which happens every 30 minutes.) For example, if a customer starts checkout right after the last periodic sync but does not complete checkout within 30 minutes, a **Started Checkout** event is sent to Klaviyo. If they proceed to place an order within those 30 minutes, a **Started Checkout** event will not be recorded, and a **Placed Order** event will track instead.

  This event tracks when one of the following occurs:
  - A customer is logged into their account, adds something to their cart, then views the checkout page
  - A customer who is not logged in adds something to their cart, views the checkout page, and enters a billing email address
  - A customer logs into their account, adds something to their cart, and navigates to the checkout page
  - Without logging in, or using guest checkout, a customer adds something to their cart, navigates to the checkout page, and enters their email address
- [WooCommerce](https://help.klaviyo.com/hc/en-us/articles/360030732832)
  Tracks when one of the following occurs:
- [PrestaShop](https://help.klaviyo.com/hc/en-us/articles/360055123191)
  Tracks when one of the following occurs:
- [Shift4Shop](https://help.klaviyo.com/hc/en-us/articles/115005083107)
  Tracks when a customer enters their contact and shipping information on the first page of the Shift4Shop checkout process and clicks “Continue”

If you’re using an ecommerce platform without a pre-built Klaviyo integration, or a custom platform, learn [how to enable Started Checkout tracking](https://developers.klaviyo.com/en/docs/guide-to-integrating-a-platform-without-a-pre-built-klaviyo-integration#started-checkout) on our Developer site.

## Test Started Checkout events

The **Started Checkout** event is commonly used to set up abandoned cart flows. If you have recently set up your account and are attempting to create an abandoned cart flow from Klaviyo’s Flows Library, you may encounter the following warning message:

"We have not received any recent **Started Checkout** events. If you think there might be a problem, contact our Success Team for help."

This does not necessarily mean there is a problem with your account or integration, but it may mean no **Started Checkout** events have triggered yet. If your site is new, this is most likely the case. You can trigger an event by following the steps below to cause this warning to disappear.

To test your **Started Checkout** tracking is set up properly, follow these steps:

1. Navigate to your website.
2. Navigate to a product page on your site with a product in stock.
3. Click the “Add to Cart” button on the page.
4. Proceed to checkout with the item(s) in your cart.
5. On the first page of checkout, fill out all required contact information and click ****Continue**** to move to the next step of the checkout process.
6. Search in Klaviyo for the email address you used during checkout
   ![The searchbar can be found in the top right of Klaviyo where you can search for profiles by email address.](https://klaviyo.zendesk.com/hc/article_attachments/28716066498843)

   You should see that a Klaviyo profile has been created for you (if one didn't exist already) and that a **Started Checkout** event has been tracked on your activity feed.

   Not all ecommerce integrations sync data in realtime due to limitations with some ecommerce platforms. For some integrations, you may need to wait 30 minutes to an hour before events are tracked. Please see our article on [how often integrations sync](https://help.klaviyo.com/hc/en-us/articles/115005253208) for more information.

   To see a feed of all **Started Checkout** metrics over time:
7. Navigate to the [Analytics tab](https://www.klaviyo.com/analytics/) of your account.
8. Click into ****Metrics.****
9. Filter by **Started Checkout** (or **Checkout Started** for Shopify and Magento 1) to view tracked data in an activity feed, activity map, charts, best people, and cohort reports.

![At the top of the Metrics page there is a searchbar where you can search for different metric by name.](https://klaviyo.zendesk.com/hc/article_attachments/28716056049691)

Once you’ve reviewed the troubleshooting scenarios below and made changes, you should test your tracking again to make sure it’s working correctly.

## Troubleshooting scenarios

Review the following questions in order to diagnose the cause of your **Started Checkout** issues. Note that some steps are general, and others depend on what ecommerce platform you are using.

****Are you having issues tracking other metrics as well?****

If you are having issues tracking other metrics as well as **Started Checkout**, there may be an issue with your integration’s setup.

Follow these steps to see if your integration is set up correctly:

1. If the keys appear to match on both sides, check to see if there are any blank spaces before or after the keys. Delete any leading or trailing blank spaces because they can cause errors.

1. Navigate to the Integrations page of your account.
2. In the **Enabled Integrations** tab, make sure that your ecommerce integration is in the list. Otherwise, follow the relevant setup guide linked in the [Before you begin section](#h_01G6W4E472QT850B5ZPSEKFEX5) of this article to make sure you have followed all steps correctly for setting up and configuring your ecommerce integration.
3. If your ecommerce integration is enabled, click ****View Settings**** to check for error messages related to the integration and that all required fields have been filled out.

   ![The integration settings link can be found to the right of each integration in the Enabled Integrations tab.](https://klaviyo.zendesk.com/hc/article_attachments/28716066504091)
4. If your integration requires use of a public API key, private API key, consumer key, and/or consumer secret, make sure the information in Klaviyo matches what is in your ecommerce platform.
5. If you are still encountering issues with your integration, please [contact Klaviyo support](https://help.klaviyo.com/hc/en-us/articles/115001002272-How-to-Contact-Support) for further troubleshooting.

****Have you recently switched ecommerce platforms?****

When you migrate ecommerce platforms, make sure to switch the metrics used for your flows and analytics to the metrics for your new ecommerce platform. For example, if you were to switch from BigCommerce to Shopify, your account’s analytics and flows may still be set to use BigCommerce’s **Started Checkout** metric rather than Shopify’s **Started Checkout** metric. See the guides below for further assistance:

- [How to update Klaviyo after switching ecommerce platforms](https://help.klaviyo.com/hc/en-us/articles/360003124151-Updating-Klaviyo-After-Switching-Ecommerce-Platforms)
- [How to change the conversion metric for flow and campaign reports](https://help.klaviyo.com/hc/en-us/articles/115005199947-How-to-Change-the-Conversion-Metric-for-Flow-and-Campaign-Reports)
- [How to change a flow trigger](https://help.klaviyo.com/hc/en-us/articles/115002775052-How-to-change-a-flow-trigger)

****Are you using a third-party service for your checkout page?****

If you are using a third-party app or extension to handle your checkout process, this may prevent checkout events from triggering properly for your ecommerce platform which will in turn prevent Klaviyo from tracking **Started Checkout** events.

In order to test for this, try disabling the app or extension responsible for managing your checkout process and see if you are able to trigger a **Started Checkout** event using the steps provided in the [Test Started Checkout events section](#h_01G6W4EPHW2E7Y4E662V5YE8SP) of this guide.

****For Wix users: Does your store use a single page for checkout?****

In order for Klaviyo to track **Started Checkout** events on Wix, the shipping and billing info must be on separate pages. If you have a single page checkout process, it is recommended that you adjust any settings, theme, or extension to ensure your checkout process requires the customer to enter information on multiple pages.

****For WooCommerce and Magento users: Are you using the most recent version of your integration plugin?****

If you are using WooCommerce or Magento, problems with **Started Checkout** tracking might be related to other issues with your platform’s Klaviyo plugin.

Check to see if you are using the most up-to-date version of the plugin for your integration. If needed, update to the latest version within WooCommerce or Magento, or you can download the latest version from the relevant platform’s listing.

- [Setup Wizard install](https://marketplace.magento.com/klaviyo-magento2-extension.html)
- [Composer install](https://packagist.org/packages/klaviyo/magento2-extension)

- [Klaviyo WordPress (WooCommerce) plugin](https://wordpress.org/plugins/klaviyo/)
- [Klaviyo Magento 1 extension](https://www.klaviyo.com/media/downloads/MagentoKlaviyo-Latest.tgz)
- Klaviyo Magento 2 extension

## Contact Klaviyo support

If you are still encountering issues after consulting this list and testing your tracking, please reach out in our [Community](https://community.klaviyo.com/got-a-question-1) or to our [Support Team](https://help.klaviyo.com/hc/en-us/articles/115001002272-How-to-Contact-Support).