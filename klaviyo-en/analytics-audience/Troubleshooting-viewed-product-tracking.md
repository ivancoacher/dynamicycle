---
id: 4416172774939
title: "Troubleshooting viewed product tracking"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/4416172774939-Troubleshooting-viewed-product-tracking"
section: "Metrics troubleshooting"
category: "Analytics"
category_slug: "analytics-audience"
klaviyo_updated: "2026-04-21T13:55:00Z"
language: en
---

## You will learn

Learn how to troubleshoot issues with your **Viewed Product** tracking, which is used to track when visitors view products on your site. For some ecommerce platforms, **Viewed Product** is tracked automatically when you integrate with Klaviyo. For other ecommerce platforms, a snippet must be manually added to your product page template.

## Before you begin

Before consulting this guide, make sure you:

- Enable**Viewed Product**tracking, if it was not added automatically through your integration.
- Enable Klaviyo’s [**Active on Site**](https://help.klaviyo.com/hc/en-us/articles/115005076767) JavaScript, known as Klaviyo.js, in order for**Viewed Product**tracking to work.

  For the following ecommerce integrations,**Viewed Product**tracking works as follows:
- [Shopify](https://help.klaviyo.com/hc/en-us/articles/115005080407)
  **Viewed Product**tracking will be automatically added to your store if you’ve toggled on the[Klaviyo app embed](https://help.klaviyo.com/hc/en-us/articles/4425956184731)and checked the**Viewed Product**setting for your integration.
- [BigCommerce](https://help.klaviyo.com/hc/en-us/articles/115005082547)
  Learn how to[add the snippet manually](https://help.klaviyo.com/hc/en-us/articles/115005082547-How-to-Integrate-with-BigCommerce#add-viewed-product-tracking4)
- [Magento 1](https://help.klaviyo.com/hc/en-us/articles/115005082187)
  Automatically added by Klaviyo
- [Magento 2](https://help.klaviyo.com/hc/en-us/articles/115005254348)
  Automatically added by Klaviyo
- [WooCommerce](https://help.klaviyo.com/hc/en-us/articles/115005255808)
  Automatically added by Klaviyo

If you are using BigCommerce, and thus added **Viewed Product** tracking manually, make sure that the snippet you’ve added to your site matches exactly with the snippets shown in the articles linked above. If you didn’t copy and paste the entire snippet, it will not work correctly.

If you’re using an ecommerce platform without a pre-built Klaviyo integration, or a custom platform, learn about[how to enable Viewed Product tracking on our Developer site](https://developers.klaviyo.com/en/docs/guide_to_integrating_a_platform_without_a_pre_built_klaviyo_integration#viewed-product-tracking-snippet).

### Test Viewed Product tracking

To test that your**Viewed Product**tracking is set up properly, follow these steps:

1. Navigate to your website
2. On your homepage, add the following to the end of the URL, replacing**testing.email@gmail.com**with your email address:
   **?utm\_email=testing.email@gmail.com**

   ![Shopify test store with ?utm_email=example@gmail.com appended to URL](https://klaviyo.zendesk.com/hc/article_attachments/28720760666651)
3. Reload the page
4. Navigate to a product page on your site
5. Search in Klaviyo for your email address
   ![Search bar in Klaviyo](https://klaviyo.zendesk.com/hc/article_attachments/33675380127515)

   You should see that a Klaviyo profile has been created for you (if one didn't exist already) and that this product view has been tracked on your activity feed.

   To see a feed of all**Viewed Product**metrics over time:
6. Click the****Analytics****dropdown in Klaviyo and select ****Metrics****
7. Filter by**Viewed Product**to view tracked data in an activity feed, activity map, charts, best people, and cohort reports

![Metrics tab in Klaviyo with Viewed Product in search bar and Viewed Product in results with gear icon](https://klaviyo.zendesk.com/hc/article_attachments/28720772435867)

Once you’ve reviewed the troubleshooting scenarios below and made changes, you should test your tracking again to make sure it’s working correctly.

## Table of contents

This guide covers the following troubleshooting scenarios:

- Have you enabled Klaviyo's **Active on Site** tracking?
- Have you recently switched ecommerce platforms?
- Have you recently updated your store's theme, or made any other updates to your ecommerce platform?
- For WooCommerce and Magento users: Are you using the most recent version of your integration plugin?
- For BigCommerce users: Is your ecommerce store connected to multiple Klaviyo accounts?
- For Shopify users: Do you require cookie consent for visitors in the EU, EEA, UK and Switzerland prior to permitting onsite tracking?

## Troubleshooting scenarios

Review the following questions in order to diagnose the cause of your**Viewed Product**issues. Note that some steps are general, and others depend on what ecommerce platform you are using.

****Have you enabled Klaviyo’s “Active on Site” tracking?****

In order for **Viewed Product** tracking to work correctly, you must first enable Klaviyo’s **Active on Site** tracking which allows your customers to be cookied. **Active on Site** tracking is enabled via the addition of a JavaScript snippet (known as “Klaviyo’s onsite JavaScript” or “Klaviyo.js”) to your site.

Klaviyo adds Klaviyo.js automatically during the integration, though some integrations require that you check a setting to enable it. Learn about your specific ecommerce platform and how to test that Klaviyo.js is working:

1. ****Shopify****
   Klaviyo.js is added automatically through the integration or through the Klaviyo app embed in Shopify, if you enable it.
2. ****WooCommerce****
   Klaviyo.js is added automatically when you integrate with WooCommerce, and you can make sure that you’ve completed all steps by reading our [WooCommerce integration guide](https://help.klaviyo.com/hc/en-us/articles/115005255808-How-to-Integrate-with-WooCommerce). To test your onsite JavaScript, navigate to ****Integrations****, then click the ****Setup Web Tracking**** button in the upper right. Then, find the step where you can enter your site URL in the box, and follow the instructions to test your tracking.
3. ****BigCommerce****
   Make sure you’ve checked the option on your [integration settings page](https://www.klaviyo.com/integration/bigcommerce) to **Automatically add Klaviyo onsite JavaScript**. Then, [follow the steps to test your onsite JavaScript](https://help.klaviyo.com/hc/en-us/articles/115005082547-How-to-Integrate-with-BigCommerce#confirm-web-tracking-installation3).
4. ****Magento 1****
   Klaviyo.js is added automatically when you integrate with Magento 1, and you can make sure that you’ve completed all steps by reading our [Magento 1 integration guide](https://help.klaviyo.com/hc/en-us/articles/115005082187-How-to-Integrate-with-Magento-1-x-CE-and-EE-). To test your onsite JavaScript, click your account name in the lower left corner, select ****Integrations****, then click the ****Setup Web Tracking**** button in the upper right. Then, find the step where you can enter your site URL in the box, and follow the instructions to test your tracking.
5. ****Magento 2****
   Klaviyo.js is added automatically when you integrate with Magento 2, and you can make sure that you’ve completed all steps by reading our [Magento 2 integration guide](https://help.klaviyo.com/hc/en-us/articles/115005254348-How-to-Integrate-with-Magento-2-x-CE-and-EE-). To test your onsite JavaScript, click your account name in the lower left corner, select ****Integrations****, then click the ****Setup Web Tracking**** button in the upper right. Then, find the step where you can enter your site URL in the box, and follow the instructions to test your tracking.

****Have you recently switched ecommerce platforms?****

If you’ve recently switched ecommerce platforms, you’ll need to add **Viewed Product** tracking to your new site. Consult the information in the **Before you begin** section above to learn about **Viewed Product** tracking for your new platform.

****Have you recently updated your store’s theme, or made any other updates to your ecommerce platform?****

If you’ve recently updated your store’s theme, you may need to reinstall both Klaviyo.js and the **Viewed Product** snippet on your new theme. Making other updates to your ecommerce platform may also affect the snippets previously added to your site.

To reinstall the **Viewed Product** snippet for BigCommerce, follow the instructions in the **Before you begin** section above.

If you’re using WooCommerce or Magento, or are using the Klaviyo app embed in Shopify, but you’ve made changes to your site and now the event isn’t tracking, you should [contact Klaviyo support](https://help.klaviyo.com/hc/en-us/articles/115001002272-How-to-Contact-Support) to help diagnose the problem.

****For WooCommerce and Magento users: Are you using the most recent version of your integration plugin?****

If you are using WooCommerce or Magento, problems with **Viewed Product** tracking might be related to other issues with your platform’s Klaviyo plugin.

1. If **Viewed Product** events aren’t tracking, check to see if the **Started Checkout** event is tracking by searching for **Started Checkout** within ****Analytics********>********Metrics**** in Klaviyo.
2. If both **Viewed Product** and **Started Checkout** aren’t tracking, there may be an issue with your plugin.
3. Check to see if you are using the most up-to-date version of the plugin for your integration, if possible. If you are still having issues, please [contact Klaviyo support](https://help.klaviyo.com/hc/en-us/articles/115001002272-How-to-Contact-Support).

****For BigCommerce users: Is your ecommerce store connected to multiple Klaviyo accounts?****

If you have one store connected to multiple Klaviyo accounts, this can result in duplicate Klaviyo.js on your site, which can cause **Viewed Product** tracking to break.

To check if you have duplicate Klaviyo.js:

1. Navigate to your main theme file. Klaviyo.js looks like this:

   ```
   <script type="text/javascript" async="" src="https://static.klaviyo.com/onsite/js/klaviyo.js?company_id=API_KEY"></script>
   ```
2. If you search for company\_id within the file and find it twice (and see two of the snippets shown above) then you have duplicate Klaviyo.js. There will typically be two different API keys after the equals sign, one from each Klaviyo account.
3. To make sure the duplicate is removed correctly from your site, please [contact Klaviyo support](https://help.klaviyo.com/hc/en-us/articles/115001002272-How-to-Contact-Support).

****For Shopify users: Do you require cookie consent for visitors in the EU, EEA, UK and Switzerland prior to permitting onsite tracking?****

Based on your Customer Privacy settings in Shopify, Klaviyo may not track onsite events for visitors to your Shopify store in the EU, EEA, UK and Switzerland, unless they have provided consent.

## Contacting Klaviyo support

If you are still encountering issues after consulting this list and testing your tracking, please reach out on our [Community](https://community.klaviyo.com/got-a-question-1) or to our [Support Team](https://help.klaviyo.com/hc/en-us/articles/115001002272-How-to-Contact-Support).