<h1>Troubleshooting added to cart tracking</h1>

## Before you begin

For some ecommerce platforms, **Added to Cart** events are tracked automatically. For other ecommerce platforms, a code snippet must be manually added to your site.

Before consulting this guide, make sure you:

- Enable **Added to Cart** tracking, if it was not added automatically through your integration.
- Enable Klaviyo’s “Active on Site” JavaScript, known as Klaviyo.js, in order for **Added to Cart** tracking to work. Learn how in the ["Active on Site" section](#h_01G6W496F0XVGZDAWAJ2RW5KEG) below.

  If you are using BigCommerce, make sure to enable **Viewed Product** tracking, which is required in order for **Added to Cart** tracking to function properly. Guidance around enabling **Viewed Product** tracking is given in the setup guides linked below. If you are experiencing issues with **Viewed Product** tracking, please see our guide on [troubleshooting Viewed Product tracking](https://help.klaviyo.com/hc/en-us/articles/4416172774939-Troubleshooting-Viewed-Product-Tracking).

  The following ecommerce integrations support **Added to Cart** tracking, and it works as follows:
- [Shopify](https://help.klaviyo.com/hc/en-us/articles/115005080407)
  Enabled via a [Shopify Server Pixel](https://help.klaviyo.com/hc/en-us/articles/4425956184731#h_01J6F7TREZAJM7M3R3DFVZSDGT) when you check the **Track behavioral events** setting
- [BigCommerce](https://help.klaviyo.com/hc/en-us/articles/115005082547)
  Requires a [manually installed code snippet](https://help.klaviyo.com/hc/en-us/articles/360024310292)
- [Magento 2](https://help.klaviyo.com/hc/en-us/articles/115005254348)
  Automatically added by Klaviyo
- [WooCommerce](https://help.klaviyo.com/hc/en-us/articles/115005255808)
  Automatically added by Klaviyo
- [PrestaShop](https://help.klaviyo.com/hc/en-us/articles/360054551492-How-to-Integrate-with-PrestaShop)
  Automatically added by Klaviyo
- [Salesforce Commerce Cloud](https://help.klaviyo.com/hc/en-us/articles/360033744951)
  Automatically added by Klaviyo - only tracked for logged-in users

If you’re using an ecommerce platform without a pre-built Klaviyo integration, or a custom platform, learn about [how to enable Viewed Product and Added to Cart tracking on our Developer site](https://developers.klaviyo.com/en/docs/guide-to-integrating-a-platform-without-a-pre-built-klaviyo-integration#viewed-product).

## Test Added to Cart tracking

To test that your **Added to Cart** tracking is set up properly, follow these steps:

1. Navigate to your website
2. On your homepage, add the following to the end of the URL, replacing **example@gmail.com** with your email address:
   **?utm\_email=example@gmail.com**

   ![After modifying the email address used in the example, add it to the end of your site's URL and visit your site in any browser.](https://klaviyo.zendesk.com/hc/article_attachments/28705664805275)
3. Reload the page
4. Navigate to a product page on your site with a product that is in stock
5. Click the “Add to Cart” button on the page
6. Search in Klaviyo for the email address you used in step 2
   ![The searchbar can be found in the top right of Klaviyo where you can search for profiles by email address.](https://klaviyo.zendesk.com/hc/article_attachments/28705664806427)

   You should see that a Klaviyo profile has been created for you (if one didn't exist already) and that an **Added to Cart** event has been tracked on your activity feed.

   To see a feed of all **Added to Cart** metrics over time:
7. Navigate to ****Analytics > Metrics**** in Klaviyo.
8. Filter by **Added to Cart** to view tracked data in an activity feed, activity map, charts, best people, and cohort reports. Please note that for Shopify, **Added to Cart** will have a Shopify icon, but for all other integrations it will have a gear icon.

![At the top of the Metrics page there is a searchbar where you can search for different metric by name.](https://klaviyo.zendesk.com/hc/article_attachments/28705637945755)

Once you’ve reviewed the troubleshooting scenarios below and made changes, you should test your tracking again to make sure it’s working correctly.

## Troubleshooting scenarios

Review the following questions in order to diagnose the cause of your **Added to Cart** issues. Note that some steps are general, and others depend on what ecommerce platform you are using.

****Have you enabled Klaviyo’s Active on Site tracking?****

In order for **Added to Cart** tracking to work correctly, you must first enable Klaviyo’s **Active on Site** tracking which allows your customers to be cookied. **Active on Site** tracking is enabled via the addition of a JavaScript snippet (known as “Klaviyo’s onsite JavaScript” or “Klaviyo.js”) to your site.

Klaviyo adds Klaviyo.js automatically during the integration, though some integrations require that you check a setting to enable it. Learn about your specific ecommerce platform and how to test that Klaviyo.js is working:

1. ****Shopify****
   Klaviyo.js is added automatically through the integration or through the Klaviyo app embed in Shopify, if you enable it. Learn more about the [app embed and onsite tracking for Shopify](https://help.klaviyo.com/hc/en-us/articles/4425956184731).
2. ****WooCommerce****
   Klaviyo.js is added automatically when you integrate with WooCommerce, and you can make sure that you’ve completed all steps by reading our [WooCommerce integration guide](https://help.klaviyo.com/hc/en-us/articles/115005255808-How-to-Integrate-with-WooCommerce). To test your onsite JavaScript, select the ****Integrations**** tab, then click ****Manage data >********Set up web tracking****. Then, find the step where you can enter your site URL in the box, and follow the instructions to test your tracking.
3. ****BigCommerce****
   Make sure you’ve checked the option on your [integration settings page](https://www.klaviyo.com/integration/bigcommerce) to **Automatically add Klaviyo onsite JavaScript**. Then, [follow the steps to test your onsite JavaScript](https://help.klaviyo.com/hc/en-us/articles/115005082547-How-to-Integrate-with-BigCommerce#confirm-web-tracking-installation3).
4. ****Magento 2****
   Klaviyo.js is added automatically when you integrate with Magento 2, and you can make sure that you’ve completed all steps by reading our [Magento 2 integration guide](https://help.klaviyo.com/hc/en-us/articles/115005254348-How-to-Integrate-with-Magento-2-x-CE-and-EE-). To test your onsite JavaScript, select the ****Integrations**** tab, then click ****Manage data >********Set up web tracking****.
5. Then, find the step where you can enter your site URL in the box, and follow the instructions to test your tracking.
6. ****PrestaShop****
   Klaviyo.js is added automatically when you integrate with PrestaShop, and you can make sure that you’ve completed all steps by reading our [PrestaShop integration guide](https://help.klaviyo.com/hc/en-us/articles/360054551492). To test your onsite JavaScript, select the ****Integrations**** tab, then click ****Manage data >********Set up web tracking****.
7. Then, find the step where you can enter your site URL in the box, and follow the instructions to test your tracking.

****For Shopify users: have you enabled the app embed?****

Once you enable the app embed in Shopify and check the **Track 'Viewed Product' events** setting, **Viewed Product** tracking will turn on automatically. Read our article on [enabling the Klaviyo app embed in Shopify](https://help.klaviyo.com/hc/en-us/articles/4425956184731#enabling-the-klaviyo-app-embed-in-shopify4) for more information.

****Have you recently switched ecommerce platforms?****

If you’ve recently switched ecommerce platforms, you’ll need to add both **Viewed Product** and **Added to Cart** tracking to your new site. Consult the information in the [Before you begin section](#h_01G6W48MBT2PX8MCX7D6RVT14Z) above to learn about **Viewed Product** and **Added to Cart** tracking for your new platform.

****Have you recently updated your store’s theme, or made any other updates to your ecommerce platform?****

If you’ve recently updated your store’s theme, you may need to reinstall Klaviyo.js, the **Viewed Product** snippet, and the **Added to Cart** snippet (for BigCommerce) on your new theme depending on the platform. Making other updates to your ecommerce platform may also affect the snippets previously added to your site.

To reinstall the **Viewed Product** snippet for BigCommerce, follow the instructions in the [BigCommerce integration setup guide](https://help.klaviyo.com/hc/en-us/articles/115005082547-How-to-Integrate-with-BigCommerce#confirm-web-tracking-installation3), and for the **Added to Cart** snippet follow the [guide to creating an "Added to Cart" event for BigCommerce](https://help.klaviyo.com/hc/en-us/articles/360024310292-Guide-to-Creating-an-Added-to-Cart-Event-for-BigCommerce).

If you’re using WooCommerce or Magento, or are using the Klaviyo app embed in Shopify, but you’ve made changes to your site and now the event isn’t tracking, you should [contact Klaviyo support](https://help.klaviyo.com/hc/en-us/articles/115001002272-How-to-Contact-Support) to help diagnose the problem.

****For BigCommerce users: Is your ecommerce store connected to multiple Klaviyo accounts?****

If you have one store connected to multiple Klaviyo accounts, this can cause problems with **Active on Site**, **Viewed Product**, and **Added to Cart** tracking. Duplicate Klaviyo.js can cause onsite tracking to break.

To check if you have duplicate Klaviyo.js:

1. Navigate to your main theme file. Klaviyo.js looks like this:

   ```
   <script type="text/javascript" async="" src="https://static.klaviyo.com/onsite/js/klaviyo.js?company_id=API_KEY"></script>
   ```
2. If you search for company\_id within the file and find it twice (and see two of the snippets shown above) then you have duplicate Klaviyo.js. There will typically be two different API keys after the equals sign, one from each Klaviyo account.
3. To make sure the duplicate is removed correctly from your site, please [contact Klaviyo support](https://help.klaviyo.com/hc/en-us/articles/115001002272-How-to-Contact-Support).

****For BigCommerce users: Are you using the correct code snippet for your Add to Cart button?****

BigCommerce requires a manually installed code snippet to use **Added to Cart** tracking. There are 2 different snippets that can be installed into your theme depending on if your “Add to Cart” button has an ID or not. Please see our guide on [how to create an "Added to Cart" event for BigCommerce](https://help.klaviyo.com/hc/en-us/articles/360024310292) for more information on how to check this.

****For WooCommerce and Magento users: Are you using the most recent version of your integration plugin?****

If you are using WooCommerce or Magento, problems with **Added to Cart** tracking might be related to other issues with your platform’s Klaviyo plugin.

1. If **Added to Cart** events aren’t tracking, check to see if the **Started Checkout** event is tracking by searching for **Started Checkout** within ****Analytics > Metrics**** in Klaviyo.
2. If both **Added to Cart** and **Started Checkout** aren’t tracking, there may be an issue with your plugin.
3. Check to see if you are using the most up-to-date version of the plugin for your integration. If needed, update to the latest version within WooCommerce or Magento, or you can download the latest version from the relevant platform’s listing.

- [Klaviyo WordPress (WooCommerce) plugin](https://wordpress.org/plugins/klaviyo/)
- [Klaviyo Magento 1 extension](https://www.klaviyo.com/media/downloads/MagentoKlaviyo-Latest.tgz)
- [Klaviyo Magento 2 extension](https://help.klaviyo.com/hc/en-us/articles/115005254348#h_01F7458JT1BK3PB93NXHJPMSKE)

****For Shopify users: Do you require cookie consent for visitors in the EU, EEA, UK and Switzerland prior to permitting onsite tracking?****

Based on your Customer Privacy settings in Shopify, Klaviyo may not track onsite events for visitors to your Shopify store in the EU, EEA, UK and Switzerland, unless they have provided consent.

## Contact Klaviyo support

If you are still encountering issues after consulting this list and testing your tracking, please reach out in our [Community](https://community.klaviyo.com/got-a-question-1) or to our [Support Team](https://help.klaviyo.com/hc/en-us/articles/115001002272-How-to-Contact-Support).

Learn how to troubleshoot other metrics:

Other resources:
