---
id: "13001662470939"
title: "Getting started with Shopware"
source_url: "https://help.klaviyo.com/hc/en-us/articles/13001662470939-Getting-started-with-Shopware"
section: "Shopware"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:27Z"
language: "en"
---
## You will learn

Learn how to integrate with Shopware 6 in order to bring site activity, order, catalog, and subscriber data into Klaviyo.

## Before you begin

Please note the following:

- Before integrating, make sure you're logged in to the Klaviyo account you want to integrate.
- The Shopware 6 integration is supported by Klaviyo through a third party. If you need to contact support, see the [section below on how to do so](#h_01HBC3PT82ESVQCM2KR7GGVC80).

## Add the plugin to your Shopware account

1. Go to the [Klaviyo plugin page](https://store.shopware.com/en/klavi31418217175f/klaviyo.html) in the Shopware Store.
2. Log in when prompted, then select ****Add to cart****.
3. Proceed to checkout and complete your order.
4. Once the order is confirmed, click the option to go to your ****Shopware Account****.
5. In your Shopware Account, navigate to ****Merchant > Shops****.
6. Select the shop you purchased the plugin for.
7. Under the Licenses section, locate the Klaviyo plugin and open the plugin details page.

## Download and install the extension

You can install via of one of two methods: via Composer or via downloading our extension. After selecting an installation method, you should use that same method each time you update.

### Install via Composer

When installing via Composer, you'll need to specify the Klaviyo extension version; not all extensions work for all Shopware versions.

Are you using a Shopware version between 6.4.4.0 and 6.4.XX.XX? Run the command with the following extension version:

```
composer require klaviyo/shopware-klaviyo:1.22.0
```

Are you using a Shopware version between 6.5.0.0 and 6.5.XX.XX? Run the command with the following extension version:

```
composer require klaviyo/shopware-klaviyo:2.22.0
```

Are you using a Shopware version between 6.6.0.0 and 6.6.XX.XX? Run the command with the following extension version:

```
composer require klaviyo/shopware-klaviyo:3.6.0
```

Are you using Shopware version 6.7.0.0 or above? Run the command with the following extension version:

```
composter require klaviyo/shopware-klaviyo:4.2.0
```

### Install via upload

1. Open the plugin details page and download the latest available version (or any required version):
   - Using a Shopware version between 6.4.4.0 and 6.4.XX.XX? Download [Klaviyo extension version 1.22.0](https://github.com/klaviyo/shopware-klaviyo/archive/refs/heads/master-1.x.x.zip).
   - Using a Shopware version between 6.5.0.0 and 6.5.XX.XX? Download [Klaviyo extension version 2.22.0](https://github.com/klaviyo/shopware-klaviyo/archive/refs/heads/master-2.x.x.zip).
   - Using a Shopware version between 6.6.0.0 and 6.6.XX.XX? Download [Klaviyo extension version 3.6.0](https://github.com/klaviyo/shopware-klaviyo/archive/refs/heads/master-3.x.x.zip).
   - Using Shopware version 6.7.0.0 or above? Download [Klaviyo extension version 4.2.0](https://github.com/klaviyo/shopware-klaviyo/tree/master-4.x.x).
2. Log in to your Shopware admin for the store you wish to integrate.
3. Click ****Extensions > My extensions****.
4. Click ****Upload extension**** and select the ZIP file you downloaded from your Shopware Account. You may see a warning message during the upload. Click ****Confirm**** to continue.


   ![](https://klaviyo.zendesk.com/hc/article_attachments/28711680131995)
5. Once the extension appears on your extension list, click ****Install****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28711701445019)
6. Toggle on the Klaviyo extension.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28711680138523)

## Configure the extension in Shopware

1. In your Shopware store admin, navigate to ****Settings**** and click the ****Extensions**** tab.
2. Select ****Klaviyo****. You will be brought to the Klaviyo extension settings page.
3. Under **Sales Channels**, select the sales channel you wish to integrate with Klaviyo from the dropdown. Only integrate one sales channel with Klaviyo per Shopware store. You must also configure your settings for each sales channel individually.
4. Under **Interaction settings**, select the cookie consent tool you’d like to use with this integration. Note that visitors who do not accept Klaviyo cookies will not be tracked by Klaviyo, nor will they be able to view Klaviyo forms. The cookie consent tool options are:
   - ****Nothing****
     If this option is selected, Klaviyo has free access to store cookies.
   - ****Shopware Default****
     If this option is selected, cookie management will be implemented via Shopware's default method, given that it's turned on. To turn it on, navigate to ****Settings > Shop > Basic information****, find the **Security and Privacy** section, and then toggle on ****Use Default Cookie Notification****.
   - ****CookieBot****
     If this option is selected, cookie management will be implemented by CookieBot. If you wish to select CookieBot, you must already have it installed on your Shopware store.
   - ****Consent Manager****
   - If this option is selected, consent management will be implemented via Consent Manager. If you wish to select Consent Manager, you must already have it installed on your Shopware store.
   - ****Usercentrics CMP****
     If this option is selected, consent management will be implemented via Usercentrics CMP. If you wish to select Usercentrics CMP, you must already have it installed on your Shopware store.
5. If you do not use a cookie management tool (which already blocks Klaviyo’s script from loading) and want to speed up page load times, toggle on the setting **Initialize Klaviyo After First Interaction With Page**. This will enable the following behavior:
   - After the client starts interacting with the page, the Klaviyo scripts will be initialized.
   - On subsequent page transitions, the scripts will be initialized immediately.
     ![Cookie Consent set to Shopware default and Initialize Klaviyo after first interaction with page toggled on](https://klaviyo.zendesk.com/hc/article_attachments/28711701425051)
6. To continue, obtain your public and private API keys from Klaviyo. To do this, open a new tab and log in to the Klaviyo account you want to integrate with Shopware.
   1. Click your account name in the lower left and select ****Settings****.
   2. Select ****API keys****.
   3. Click ****Create Private API Key****. Name the key "Shopware Integration," then select ****Full Access Key**** and click ****Create****. On the next page, click ****Copy Key****.
   4. Paste the private API key into the corresponding setting within Shopware.
   5. Back in Klaviyo, click ****Done****. Then, copy your public API key from the page.
   6. Paste the public API key in Shopware in the corresponding box.
7. Next, pick a Klaviyo list from the dropdown for profiles who subscribe via a Shopware form to be added to.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28711680128027)
8. Select an identifier to use for Back in Stock variant field mapping. You should use the identifier that matches the one you use in your catalog.
9. Toggle on all the metrics you want to sync from Shopware to Klaviyo.
   ![List of all metrics toggled on to blue](https://klaviyo.zendesk.com/hc/article_attachments/28711680104731)
10. If you choose to track Back in Stock, you can customize the text color and background of the Back in Stock pop-up opening button, pop-up close button, and subscribe button. Click the square, then use the selector to choose a color, or, if you have the hex color codes for your brand’s colors, paste it in the corresponding box.
    ![Pop-up opening button settings with color set to white and background set to dark blue](https://klaviyo.zendesk.com/hc/article_attachments/28711680111515)
11. Under **Snippet names**, you’ll find a reference for how to refer to different Back in Stock components in HTML. You can choose to customize them within your site code.
    ![Snippet names for open button, close button, and email field label](https://klaviyo.zendesk.com/hc/article_attachments/28711680120347)
12. Custom Field Mapping: Here, you’ll see custom fields you’ve set up in Shopware (with the technical name in gray). Any field assigned to the Customer object can be synced to Klaviyo. To sync these custom fields to Klaviyo profiles, toggle the individual field to **Active**. Then, under **Field Name**, type the corresponding name you’d like the field to have in Klaviyo.
    ![Field name Favorite Color mapped to favorite_color, with field toggled to active](https://klaviyo.zendesk.com/hc/article_attachments/28711680122651)
13. When you are finished, click ****Save****.
14. To run a sync of historical events, click ****Synchronize historical events**** at the top of the page.
15. To run a sync of existing subscribers, click ****Synchronize subscribers**** at the top of the page.

After you initially run these syncs manually, they will run automatically going forward. The subscriber and transactional event syncs run every 5 minutes. Onsite events (**Active on Site**, **Viewed Product**, and **Started Checkout**) sync in real time.

## Sync your catalog feed

To complete your integration with Klaviyo, you must generate a feed of your product catalog, then sync it to Klaviyo. To generate the feed:

1. Log in to your Shopware store admin.
2. Click ****+**** next to **Sales Channels** to add a new channel.
3. Next to **Product** **comparison**, click ****Add Sales Channel****.
4. Under **Template**, choose ****Klaviyo XML****.
5. Give the channel a name, such as **Klaviyo Export**.
6. Under **Tax collection**, select ****Line by line (horizontal) calculation****.
7. Under **Storefront Sales Channel**:
   - Select the Storefront Sales Channel this catalog is for.
   - Select the Storefront domain.
   - Select the currency.
   - Select the language.
   - Select the Customer Group.
8. Under **Product export**:
   - Name the file (e.g., **klaviyo.xml**).
   - Select the encoding ****UTF-8****.
   - Select the file format ****XML****.
9. Leave **Export variants as discrete products** toggled off.
10. Select the interval: ****1 day****.
11. Leave **Generate via scheduler** toggled off.
12. Select your dynamic product group.
13. Under **Status**, toggle on ****Active****.
14. Click ****Save**** in the upper right.
15. Scroll down and copy the **Export URL**, which you will use for the Klaviyo sync.
16. Now that the feed is generated, you must sync it to Klaviyo. Follow the instructions [to sync a custom catalog feed to Klaviyo](https://developers.klaviyo.com/en/docs/guide_to_syncing_a_custom_catalog_feed_to_klaviyo).

## Data synced from Shopware

To learn all about the data synced from Shopware and how to access it in Klaviyo, read our [Shopware data reference](https://help.klaviyo.com/hc/en-us/articles/13006716790299).

## Klaviyo sign-up forms

You can add [Klaviyo sign-up forms](https://help.klaviyo.com/hc/en-us/articles/360026474752-Getting-started-with-sign-up-forms) to your Shopware store in order to collect subscribers. Note that only site visitors who accept Klaviyo cookies will be able to see Klaviyo sign-up forms.

## How to contact support

The Klaviyo Shopware 6 integration is supported by Klaviyo through a third party. If you have questions about the integration and need support, you can contact integration-specific support by [filling out our form](https://docs.google.com/forms/d/e/1FAIpQLSewwJzxlnFtsbn18ZVubgIORubQWpAKBuYQv6WKxy8xSxVZog/viewform).

If you need general support for Klaviyo-related questions, [contact Klaviyo support](https://help.klaviyo.com/hc/en-us/articles/115001002272-How-to-contact-support).

## Outcome

You’ve integrated Shopware 6 with Klaviyo to bring site activity, order, catalog, and subscriber data into Klaviyo. You can now start using Klaviyo for your owned marketing needs.

## Additional resources

- [How to sync a custom catalog feed to Klaviyo](https://developers.klaviyo.com/en/docs/guide_to_syncing_a_custom_catalog_feed_to_klaviyo)
- [Shopware 6 data reference](https://help.klaviyo.com/hc/en-us/articles/13006716790299)