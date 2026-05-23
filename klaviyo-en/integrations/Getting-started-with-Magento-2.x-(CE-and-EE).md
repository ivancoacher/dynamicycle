---
id: 115005254348
title: "Getting started with Magento 2.x (CE and EE)"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005254348-Getting-started-with-Magento-2-x-CE-and-EE"
section: "Magento 2"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:56:40Z"
language: en
---

## You will learn

Learn how to integrate Klaviyo with your Magento 2 CE or EE store. You'll need to install the Klaviyo extension in Magento, configure the extension and set up OAuth, then enable the integration in Klaviyo. This guide covers all required integration steps, as well as how to confirm your historical data sync is successful.

## Before you begin

Please note that Magento 2 versions below 2.4.0 are not supported.

To ensure that Klaviyo can make the necessary API calls for integration, your Magento 2 server must have a publicly accessible hostname. Magento 2 servers hosted locally will be unable to fully integrate with Klaviyo.

Klaviyo's Magento 2 extension should be installed via Composer. Please note that installation via Composer requires an IT administrator with SSH access to the server where Magento 2 is hosted.

## Install the Klaviyo extension in Magento 2

![](https://fast.wistia.com/embed/medias/yc7dejd9jw/swatch)

1. Log in to your Magento 2 server and navigate to the root directory of your Magento app from your command line tool. This guide shows example outputs for Terminal, but these steps can be modified for any command line tool of your choice.
2. Run the following command to access the latest version of the Klaviyo extension from Packagist. Packagist is a repository for PHP code libraries which allows you to easily install the latest version of the extension.
   `composer require klaviyo/magento2-extension`
3. Run the following command to enable the Klaviyo extension you just downloaded:
   `php bin/magento module:enable Klaviyo_Reclaim --clear-static-content`
   ![composer2.png](https://klaviyo.zendesk.com/hc/article_attachments/28720758835867)
4. As displayed in the sample output, you must now enable any additional modules. Run the following command to enable them:
   `php bin/magento setup:upgrade`
5. Scan the output for `Module 'Klaviyo_Reclaim'` to confirm that the Klaviyo module is enabled and running.
6. To ensure that the CSS and JS on your Magento 2 store continues to work properly, you’ll need to run a static content deploy command.
   `php bin/magento setup:static-content:deploy -f`
   ![composer3.png](https://klaviyo.zendesk.com/hc/article_attachments/28720770744219)
7. You can now return to the Magento admin dashboard from your browser.

Installation via Composer is complete! Proceed to the next section for configuration instructions.

## Configure the Klaviyo extension

### How-to video

![](https://fast.wistia.com/embed/medias/m7vqtc4psz/swatch)

1. In your Klaviyo account, navigate to the [API keys tab](https://www.klaviyo.com/settings/account/api-keys).
2. In a new tab, navigate to your Magento store admin.
3. Under **Settings**, click ****Stores********>********Configuration****.
4. From the Klaviyo dropdown, click ****General****.
5. Set **Enable Klaviyo Extension** to ****Yes****.
6. Copy your six-digit Klaviyo public API key from the API keys tab and paste it in the corresponding box in Magento.
7. On the Klaviyo API keys tab, generate a new private key and then paste it into the corresponding box in Magento. Authenticating with your private API key will allow you to sync Newsletter subscriptions from Magento to Klaviyo.

In the next section, you'll set up OAuth, which enables other aspects of the integration.

![](https://klaviyo.zendesk.com/hc/article_attachments/28720770782235)

### Set up OAuth

Next, you'll enable OAuth authentication to securely connect your Klaviyo account to the Magento 2 extension.

1. Navigate to the ****Setup OAuth**** tab in Magento.
2. Give your integration a memorable name, as you will need to locate it by this name later.
3. Click ****Save Config**** to proceed.
   ![OAUTHtab.png](https://klaviyo.zendesk.com/hc/article_attachments/28720758843931)
4. Locate ****System**** in the left hand navigation pane and select ****Integrations**** from the **System** tray.
5. Locate your integration name and click ****Activate****. Activating the integration will open up a window requesting you to approve access.
   ![activateoauth.png](https://klaviyo.zendesk.com/hc/article_attachments/28720770752923)
6. Click ****Allow**** to be redirected to Klaviyo, where you'll complete the integration setup.
   ![oauthperms.png](https://klaviyo.zendesk.com/hc/article_attachments/28720770756379)
7. Sign in to Klaviyo if prompted, or confirm your account name is correct and click ****Integrate.**** This will add the Magento 2 integration to the Klaviyo account associated with the API key you used for setup. If you are logged into multiple Klaviyo accounts and the correct account is not displaying, log out of any other sessions.

![](https://klaviyo.zendesk.com/hc/article_attachments/28720758864027)

If the window closes automatically, the connection was successful. You can also confirm success by opening your Klaviyo account in a new browser tab or window, selecting the ****Integrations**** tab, and looking for Magento 2 on the list.

If you receive the following error instead, ensure that the API keys used in the first step correspond to the account you're currently logged in to.

![apierror.png](https://klaviyo.zendesk.com/hc/article_attachments/28720770768027)

When establishing the connection between Magento and Klaviyo, if you receive a list of errors instead, you can click each error to learn more about the cause.

![oauthgenerror.png](https://klaviyo.zendesk.com/hc/article_attachments/28720758849819)

### Set a newsletter list

Next, you'll select a Klaviyo list to sync your newsletter subscribers to. You also have the option of using Klaviyo opt-in settings or Magento 2 opt-in settings for your chosen list.

1. In Magento, click ****Newsletter****.
2. Select the Klaviyo list you want to sync your Magento sign-up form to from the dropdown.
3. Click ****Save Config****.

![newsletterm2.png](https://klaviyo.zendesk.com/hc/article_attachments/28720758855579)

### Enable consent at checkout

Next, you can choose to enable consent at checkout for email and SMS.

Please note that if you enable consent at checkout, you'll also need to enable webhooks (below) in order for consent at checkout to function properly.

1. On the **Configuration** page, under **Klaviyo**, navigate to ****Consent at Checkout****.
   ![m2cac-new.png](https://klaviyo.zendesk.com/hc/article_attachments/28720758860571)
2. You’ll see a section for collecting email consent and SMS consent. The two are treated separately, so that you can collect just email, just SMS, or both. If you gather both SMS and email subscribers, choose a different list for SMS than for email. This makes sure that consent will always be properly attributed to the correct channel.

   - Consent will not sync (for both email and SMS) until the customer finishes placing the order and, if applicable, confirms their subscription due to double opt-in.
   - Note that for users already logged in to your Magento 2 store, the email consent checkbox will not appear at checkout by default.
3. Under **Email**, select ****Yes**** for **Subscribe contacts to email marketing at checkout**.
4. Select an email list to sync subscribers to, such as a newsletter.
5. Enter the email opt-in checkbox text you wish to use.
   ![2021-03-24_13-00-56.png](https://klaviyo.zendesk.com/hc/article_attachments/28720758831387)
6. Under **SMS**, select ****Yes**** for **Subscribe contacts to SMS marketing at checkout**.
7. Choose the list you want your SMS contacts to sync to. For additional detail regarding these settings, check out our guide to [collecting SMS consent at checkout](https://help.klaviyo.com/hc/en-us/articles/360058698511-How-to-Collect-SMS-Consent-at-Checkout-on-Magento-2).
   ![m2smscac.png](https://klaviyo.zendesk.com/hc/article_attachments/28720758825755)
8. Sort order allows you to change the placement of the email and SMS consent boxes. By default, these boxes appear under the first email input and shipping phone number field, respectively. Thus, if you haven’t rearranged the checkout page, you do not need to change the sort order. If you have changed the layout, adjust the sort order accordingly.
9. When you are finished, click ****Save Config**** in the upper right.

### Enable webhooks

Next, you'll enable Klaviyo webhooks in your Magento 2 account. Please note that enabling webhooks is required for consent at checkout to function correctly.

1. From the admin dashboard, navigate to ****Stores > Configuration****.
2. Click on ****Klaviyo**** and select the ****Webhooks**** tab.
3. Create a webhook secret and enter it into the corresponding ****Webhook Secret**** field. The webhook secret is a key that Klaviyo will use for validation. This secret can be anything you choose, but we recommend creating a secure string of letters and numbers. Magento will hide your webhook secret with asterisks for security purposes, so be careful to enter it correctly.

   If you are using a multi-store integration, the webhook secret in this field should be entered in your default configuration, and the same secret will be used as validation for each store configuration. The webhook secret should only be added to the default config and should not be added per store.
   ![m2webhooktab.png](https://klaviyo.zendesk.com/hc/article_attachments/28720770746779)
4. Next to the webhooks you wish to enable, select ****Yes**** from the dropdown. To read more about the webhooks supported by Klaviyo, check out our [guide to webhooks for Magento 2](https://help.klaviyo.com/hc/en-us/articles/360055336451).
5. Click ****Save Config****.

## Enable the Magento 2 integration in Klaviyo

### How-to video

![](https://fast.wistia.com/embed/medias/evlfi7fbya/swatch)

1. Open Klaviyo, then select ****Integrations**** from the left-hand navigation. Find Magento 2 on the list and select it.
2. On the next page, you'll have the option to add new Magento 2 customers to a Klaviyo list. Click the checkbox to **Add new Magento 2 customers to a Klaviyo list** and select a list from the dropdown. Note that checking this setting will only add customers to the selected list, but not subscribe them to marketing messages.

   This setting will only sync new customers; existing customers need to be [manually migrated from your Magento list to Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115005082407).
   ![](https://klaviyo.zendesk.com/hc/article_attachments/47104011603483)
3. Next, select which store views from Magento 2 you would like to sync to Klaviyo. All store views are synced to Klaviyo by default. This setting allows you to be selective about which stores you integrate with. If you’re using Multi-Source Inventory (MSI) in Magento 2, check **Specific Magento 2 store views** and select the stores you wish to sync in order to see your inventory properly represented in Klaviyo.
4. Under **Advanced**, enable the following settings as needed:

   - ****Special price settings****
     This setting refers to a special sale price for items that can optionally take effect in a certain date range. We highly recommend enabling this feature if you're planning to use it, as it's more difficult to enable later. When you enable **Use special price for product prices when applicable**, the product block will display the special price when applicable. When using a dynamic product feed, the special price will populate at send time. When manually selecting items from your catalog, the special price will populate once you select the product(s). For each product, there are 4 metadata fields that will sync:
     - ****price****
       (Required, float) The standard price of the item.
     - ****special\_price****
       (Optional, float) This is a special sale price for the item. When this price is in effect, you will see this special\_price next to a strikethrough of the price.
     - ****special\_from\_date****
       (Optional, date) This specifies a start date for special\_price to take effect.
     - ****special\_to\_date****
       (Optional, date) This specifies an end date for special\_price being in effect.
   - ****Custom Media Root URL****
     This setting allows you to change the default path for your site images. Enable this setting if you host your product images on a URL that is different than your website.
5. Click ****Save****.

You've now successfully enabled the Magento 2 integration! Your data will begin to sync to Klaviyo in minutes.

After the initial historical data sync is complete, the Magento 2 integration syncs every 30 minutes.

## Data synced with the Magento 2 integration

Klaviyo's Magento 2 integration pulls key customer information from your Magento platform.

Here is some of the data we sync from Magento:

- Customer information including first name, last name, and location.
- Sales and order data including which items were purchased, item images, item categories, and any discounts applied.
- Fulfillment, refunded, and canceled order data.
- When people visit your website and which items they view; web tracking is handled by the extension.

To learn more, head over to our [Magento 2 data reference](https://help.klaviyo.com/hc/en-us/articles/115003458852).

## Convert Magento order values into a single currency

Klaviyo supports the conversion of all foreign currencies in Magento to one primary currency in Klaviyo. Please [contact support](https://help.klaviyo.com/hc/en-us/articles/115001002272) to enable this feature. This is especially helpful if you have multiple stores with transactions in different currencies.

When this feature is enabled:

- The conversion happens when Magento syncs order data into Klaviyo.
- Klaviyo will check if the **order\_currency\_code** is the same as the set **global\_currency\_code**. If not, Klaviyo will convert the order total from the order currency to the global currency specified to ensure that your financial analytics are accurate. Please note that order line items will remain in the order currency code and not be converted.

## Upgrade your extension

Looking to upgrade your Klaviyo Magento 2 extension? Follow the instructions detailed in the[**Install**](#h_01HGGJNFJT8CTEQ8PVGDVNB6GB) [section a](#h_01HGGJNFJT8CTEQ8PVGDVNB6GB)[bove](#h_01HGGJNFJT8CTEQ8PVGDVNB6GB) and run the command to install the latest version. This will overwrite your current version and your update will be complete - there’s no need to re-configure the extension or re-enable the integration in Klaviyo.

## Re-sync your catalog

You can prompt a full historical re-sync of your Magento 2 catalog at any time. Re-syncing your catalog can help you take advantage of Klaviyo updates to inventory and variant-related features.

To re-sync your catalog:

1. In Klaviyo, select the ****Integrations**** tab.
2. Select your Magento 2 integration from the list.
3. Click the ****Data**** tab.
4. Under **Sync catalog data**, click ****Re-sync****.

![](https://klaviyo.zendesk.com/hc/article_attachments/38564204532379)