---
id: "115005255808"
title: "Getting started with WooCommerce"
source_url: "https://help.klaviyo.com/hc/en-us/articles/115005255808-Getting-started-with-WooCommerce"
section: "Getting started with WooCommerce"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:25Z"
language: "en"
---
## You will learn

Learn how to install the Klaviyo WooCommerce extension and enable the WooCommerce integration in your Klaviyo account.

The main steps to integrating with WooCommerce are:

- Install the Klaviyo extension (also known as the Klaviyo plugin) in WooCommerce.
- Enable the WooCommerce integration in Klaviyo.

This article also guides you through testing your WooCommerce integration.

The WooCommerce integration syncs data to Klaviyo in real time.

![](https://fast.wistia.com/embed/medias/bsnk4fwstw/swatch)

## Before you begin

If you have active caching plugins or redirect plugins in WordPress, these can interfere with Klaviyo’s integration and cause connection issues. We recommend disabling these plugins during the integration setup process. Having other issues with setup? Check out [Troubleshooting your WooCommerce Integration](https://help.klaviyo.com/hc/en-us/articles/4515829067803).

It is highly recommended to add Klaviyo IPs to your firewall provider’s allow list to minimize authentication and configuration issues. For more details, please check out [How to allowlist Klaviyo integration traffic IP addresses](https://help.klaviyo.com/hc/en-us/articles/19143781289115).

## Install the Klaviyo extension in WooCommerce

Klaviyo’s WooCommerce extension allows you to add a newsletter sign-up form to your website, enable website activity tracking, and get data about when people start checkouts and view products so you can send out abandoned cart emails. Our extension is also compatible with High Performance Order Storage (HPOS).

Before you begin, we recommend that you log in to your Klaviyo and WooCommerce accounts. If you have more than one Klaviyo account, log out of any accounts you don’t wish to integrate with WooCommerce.

1. In WooCommerce, click the ****WooCommerce**** tab in the lefthand navigation, then select ****Extensions****.
2. Search for **Klaviyo**, then select **Klaviyo for WooCommerce** to be brought to the Klaviyo extension page in the WooCommerce Marketplace.

   ![](https://klaviyo.zendesk.com/hc/article_attachments/28720771148059)
3. Click ****Add to cart****.
4. Make sure you are logged in to your WooCommerce Marketplace account, then check out.
5. Continue the checkout to be brought to an order confirmation page, then click ****Add to Site****.
6. If your WooCommerce Marketplace account isn't connected to your WooCommerce site, copy paste your Store URL in the box. If it's already connected, select your site from the dropdown. Then, click ****Add to site****.

   ![](https://klaviyo.zendesk.com/hc/article_attachments/28720771150235)
7. Navigate back to your WooCommerce admin, then select ****Plugins****. Scroll through the list of installed plugins to find Klaviyo, then click ****Activate****.
8. Select ****Marketing**** from the lefthand navigation, then click ****Klaviyo****.
9. Click ****Connect Account**** to begin, then proceed to the next section.

![](https://klaviyo.zendesk.com/hc/article_attachments/33640943535515)

Have issues with setup? Check out [Troubleshooting your WooCommerce Integration](https://help.klaviyo.com/hc/en-us/articles/4515829067803).

## Enable the WooCommerce integration in Klaviyo

1. If prompted, log in to Klaviyo. You can make sure that you are logged in to the correct Klaviyo account by opening a new tab, navigating to your [Klaviyo dashboard](https://www.klaviyo.com/dashboard/performance), and checking the account name. If you need to switch accounts, click ****Logout**** and then log in to the correct account before proceeding.
2. Review the permissions, then grant them by clicking ****Approve****.

   ![](https://klaviyo.zendesk.com/hc/article_attachments/33641463439899)
3. On the integration settings page, confirm the account name is correct.

   ![](https://klaviyo.zendesk.com/hc/article_attachments/33640943542555)
4. Check the box next to ****Add email marketing consent checkbox to your checkout page**** to easily add this option to your WooCommerce site.

   - Select a list from the dropdown under ****Add email subscribers to this list****. If no lists are available in the drop down, head over to the [Lists & Segments tab](https://www.klaviyo.com/lists) to create a new list.
     Anyone who subscribes via the checkbox during checkout will be added to this list. Consent is sent to Klaviyo after the customer clicks the **submit order** button during checkout.
   - Under ****Email marketing consent label****, enter the consent language you wish to appear next to the checkbox on your checkout page. The default language is **Sign me up to receive Email updates and news**.![](https://klaviyo.zendesk.com/hc/article_attachments/28720759277979)
5. Check the box next to ****Add SMS marketing consent checkbox to your checkout page**** if you want to add this option to your WooCommerce site. Please note that SMS consent will not sync to Klaviyo if [your company is age-gated](https://help.klaviyo.com/hc/en-us/articles/17252552814875).

   - Select a list from the dropdown under ****Add SMS subscribers to this list.**** Users who consent to SMS marketing via this checkbox will be subscribed to the list you select. Consent is sent to Klaviyo after the customer clicks the **submit order** button during checkout and the order is created in WooCommerce.
   - Under ****SMS marketing consent label****, include the text you wish to appear next to the checkbox on your checkout page.
   - Next, add ****SMS consent disclosure text****, which is required for TCPA compliance. Use the default Klaviyo consent language or add your own.
6. If you wish to convert all future **Placed Order** and **Ordered Product** events to a selected currency using the exchange rate at the time they are processed, check the box ****Convert all currencies to one standard**** ****currency****, then select a currency. Changing this setting will not impact previously integrated data. This setting does not change the default currency on your account.
7. When you are satisfied with these settings, click ****Complete setup.**** You can go back and edit these settings at any time by navigating to the ****Integrations**** tab and selecting ****WooCommerce****.

Congratulations! Your WooCommerce account is now connected to Klaviyo.

### Troubleshooting

If you received an error message "Unable to test API by fetching order count. Invalid count" this means that when Klaviyo tries to validate the WooCommerce integration and get a count of orders, their API doesn’t return a value Klaviyo expects or it returns nothing at all. Since the integration hasn't officially connected to Klaviyo yet, this means that it needs to be resolved within WooCommerce.

To get more information about this error, use an application like Postman to make an API call to the order count endpoint which will provide more insight into what is being passed to Klaviyo.
The endpoint you need is: **{customers-url}/wc-api/v1/orders/count**Change {customers-url} to your WooCommerce store URL.

## Test your WooCommerce integration

To test out your integration, go to your website and follow these instructions:

1. Add an item to your cart.
2. Proceed to the checkout page.
3. Fill in your email address and phone number on the checkout page. If enabled, check the boxes to subscribe to email and SMS marketing.
4. Submit your test order.
5. Check for the following (these may take a minute or two to update):

- **Started Checkout** event logged under ****Recent Data****.
- Profile created in the lists you selected for email and SMS marketing.
- **Placed Order** event logged under ****Recent Data****.

### Recent data

The Recent Data section displays the most recent instance of an event.

### Historical data

The Historical Data Progress bar updates in real-time as your historical sync is processed.

## Next steps

Congratulations on getting set up! With your account setup and integrated, it's time to start using Klaviyo's core features. After you are done with the items in this category you'll be all set to get the most out of Klaviyo's features. Check out our [Getting started with Klaviyo course](https://academy.klaviyo.com/getting-started-with-klaviyo/1405979) to ensure you're up and running to get the most from your Klaviyo account.

### Rebuilding carts from an abandoned cart flow

You can use WooCommerce Data to Rebuild Carts from an Abandoned Cart Flow.

We will generate a key on the Started Checkout event that allows you to create a link that rebuilds the customer's cart in case they return to their cart via an email triggered by this event on another device. You can create this link using the following url parameter in an Abandoned Cart flow email triggered by a Started Checkout:

```
/cart?wck_rebuild_cart={{ event.extra.CartRebuildKey }}
```

Assembled, the url should look like the following:

```
{{ organization.url|trim_slash }}/cart?wck_rebuild_cart={{ event.extra.CartRebuildKey }}
```

The dynamically-generated product title link pulls directly from the URL you have inserted in your account settings. If needed, this URL can be updated in the email template editor.

![Button block in Klaviyo's email template editor showing button text, cart rebuild URL, cancel with grey background, and save with blue background](https://klaviyo.zendesk.com/hc/article_attachments/28720759259675)

If you are using {{ organization.url }} to link to a non-secure HTTP URL, you will need to manually add your URL using HTTPS for the cart to rebuild correctly.

## Extension reference information

### Enable auto-updates

To enable auto-updates:

1. Click on the ****Plugins**** tab. Scroll down to find the **Klaviyo** plugin.
2. Click ****Enable auto-updates****.

If you prefer, you can still [download the Klaviyo WooCommerce extension](https://woocommerce.com/products/klaviyo-for-woocommerce/) manually from the WooCommerce Marketplace.

### Find the changelog

Release notes are included in the changelog for each new extension update. You can view our extension's changelog on the [Wordpress plugin directory](https://wordpress.org/plugins/klaviyo/#developers).

### How do I upgrade my WooCommerce integration to real-time, if I integrated using the Legacy API?

To start, install the latest WooCommerce extension by following the extension installation steps described above. Next, create a REST API key for the v3 integration with read/write permissions. This is different from the Legacy API key you created when you first installed the extension.

Update your integration in Klaviyo by selecting ****Save settings**** on the WooCommerce integrations settings page.

Please note that in order to use WooCommerce’s API v3 you must be on WC Version 3.5x or later and WP Version 4.4 or later.