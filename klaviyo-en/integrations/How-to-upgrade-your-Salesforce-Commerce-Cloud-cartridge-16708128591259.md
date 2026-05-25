---
id: "16708128591259"
title: "How to upgrade your Salesforce Commerce Cloud cartridge"
source_url: "https://help.klaviyo.com/hc/en-us/articles/16708128591259-How-to-upgrade-your-Salesforce-Commerce-Cloud-cartridge"
section: "Salesforce Commerce Cloud"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:30Z"
language: "en"
---
## You will learn

Learn how to upgrade your Klaviyo Salesforce Commerce Cloud cartridge.

Are you using a cartridge version older than 23.7.0? We recommend upgrading immediately to version 23.7.0 or higher. Older versions of the cartridge use Klaviyo’s v1 and v2 APIs which are retired and no longer operate as expected. We always recommend upgrading to our newest version (currently, 25.7.0).

## Before you begin

Version 23.7.0 includes a number of meaningful improvements, some of which are architectural changes around how events are triggered. Special considerations for upgrading from any version below 23.70 to any version above it are detailed below.

## Understand your current integration

It is important to be familiar with your current SFCC integration and what changes or customizations may have been made specifically for your website. Most importantly, you should consider whether or not the specific event data you send to Klaviyo has been altered or augmented, and if you’ve added any custom events.

We recommend comparing your code that assembles event data against the previous version of the Klaviyo cartridge, [available on Klaviyo’s Github](https://github.com/klaviyo/SFCC_Klaviyo/releases). Assuming that your integration has not been heavily customized, you will find your current data assembly functions in `int_klaviyo_core/cartridge/scripts/utils/klaviyo/klaviyoUtils.js`, and for **Order Confirmation** in `int_klaviyo_core/cartridge/scripts/utils/klaviyo/emailUtils.js`.

Note any customizations so that you can re-apply them once the new cartridge has been installed.

## Connect an SFCC sandbox to a Klaviyo test account

If you have not yet created a secondary Klaviyo account for testing, separate from the account that is tied to your SFCC production environment, you should do so. Then, connect your SFCC sandbox environment to the new account. We recommend completing this step using your prior Klaviyo cartridge version so that you can verify that events are successfully being sent to and received by your secondary Klaviyo account before proceeding to upgrade your codebase with the new Klaviyo cartridge.

## Remove the previous Klaviyo cartridge code

If your integration was not heavily customized, you will be able to remove the majority of the previous Klaviyo integration by simply deleting the two Klaviyo cartridge folders: int\_klaviyo\_core and either int\_klaviyo (for Site Genesis) or int\_klaviyo\_sfra (for SFRA) from the codebase. However, you will also have to remove any Klaviyo-specific code that may have been added to template files, and possibly JavaScript files.

### For Site Genesis

Standard integrations for Site Genesis will have the following code added to footer\_UI.isml:

```
<isinclude template="components/footer/klaviyoFooter"/>
```

They will also have the following block added to minicart.isml, cart.isml, and any other “cart” isml files:

```
<isif condition="${pdict.CurrentHttpParameterMap.cartAction == 'add' || pdict.CurrentHttpParameterMap.cartAction
  == 'update'}">
   <isinclude url="${URLUtils.url('Klaviyo-RenderKlaviyoAddToCart')}"/>
</isif>
```

### For SFRA

Standard integrations for SFCC will have the following code added to pageFooter.isml:

```
<isinclude template="klaviyo/klaviyoFooter"/>
```

They will also have the following code added to to the AddProduct route in the Cart.js controller:

```
 if(dw.system.Site.getCurrent().getCustomPreferenceValue('klaviyo_enabled')){
   var KlaviyoUtils = require('*/cartridge/scripts/utils/klaviyo/klaviyoUtils');
 KlaviyoUtils.trackAddToCart();
}
```

For both Site Genesis and SFRA, after the cartridge folders and the above mentioned code snippets have been removed, it is advisable to search the codebase for the word “Klaviyo.” Make sure you’re familiar with what any Klaviyo-related code that remains in your codebase is doing before removing it, as these blocks may represent customizations that you will need to put back in place after the new cartridge is installed.

## Remove services

The previous integration will have created a KlaviyoTrackService, KlaviyoTrackProfile and KlaviyoTrackCredentials at ****Administration > Operations > Service****. All three can be safely removed as the process of integrating the new Klaviyo cartridge will create new services with different names.

It is not critical that the old services be removed, but it is recommended that you clean them out to avoid future confusion.

## Review site preferences

The process of integrating the new Klaviyo cartridge will retain some of the previous Klaviyo site preferences, and will also add some new ones. Take a look at your site preferences in the **Klaviyo** preference group at ****Merchant tools > Site Preferences > Custom Preferences > klaviyo****, and check to see if any custom preferences have been added specifically for your website. If you customized the cartridge to add your own settings, you'll want to preserve them. For reference, here are the four site preferences that are built into the previous Klaviyo integration:

- ****Klaviyo Enabled (ID: klaviyo\_enabled)**** Flag if Klaviyo is on or off.
- ****Klaviyo Account (ID: klaviyo\_account)****Your Klaviyo public API key, or Site ID.
- ****Klaviyo Private API Key (ID: klaviyo\_api\_key)****
  A Klaviyo private api key.
- ****Image Type for Klaviyo (ID: klaviyo\_image\_size)****
  Large, small, thumbnail, etc.

Before setting up the new cartridge, we recommend backing up your current site preferences by exporting them at ****Administration > Site Development > Site Import & Export****. Expand ****Sites****, then your ****Site Name****, and check the Site Preferences box before entering a filename to export them to. Your current Klaviyo preferences should not be adversely affected when you later install the new cartridge, but it is a good idea to back them up for future reference.

## Remove the Klaviyo cartridges from the cartridge path

Remove int\_klaviyo\_core and either int\_klaviyo (Site Genesis) or int\_klaviyo\_sfra (SFRA) from your cartridge path at ****Administration > Sites > Manage Sites > [Site Name] > Settings****. If you do not perform this step, you will get errors resulting from SFCC looking for cartridges to load that no longer exist.

## Check the developer console and server side log for errors

At this point, you should no longer have any Klaviyo code in your codebase. We recommend reviewing your frontend, visiting pages such as Search Results, PLPs, and PDPs, and performing actions such as adding products to cart, entering, and completing checkout. As you do so, keep an eye on the Developer Console to see if any new errors are generated. Do the same with the Request Log. If you are seeing new errors related to Klaviyo, there is a good chance that you have not fully removed all of the previous Klaviyo code. It is important to track down the source of any new errors and note them before removing them.

## Install the new Klaviyo cartridge

Follow the steps laid out in [Getting started with Salesforce Commerce Cloud](https://help.klaviyo.com/hc/en-us/articles/360033744951) to integrate the new cartridge into your codebase. There may be steps that you do not need to complete - for example, your SFCC instance may or may not have the connections already established for the OCAPI portion - but in general, you should follow each step of integration. You will definitely need to replace both Klaviyo cartridges and add back code snippets.

Do not simply copy/paste the new cartridge folders over the old ones. Per the instructions above, delete the old folders completely before adding the new ones.

Note that after importing metadata.zip, you will have four new site preferences, in addition to the four that were created by the previous version of the cartridge. Your previous preferences should not have been affected by importing the new ones, but it is recommended that you double-check that all Klaviyo site preferences are correct before proceeding.

Since you are upgrading from a cartridge prior to version 23.7.0, the new site preferences **Label Events as SFCC** and **Send Added To Cart Event as ‘Add To Cart’** should be set to **No** and **Yes**, respectively. This will continue sending events without the **Salesforce Commerce Cloud** metric label and use the **Add To Cart** event type (as opposed to the new **Added to Cart**). Having these two site preferences set incorrectly will result in a breakage of reporting and potentially, a breakage of existing flows in Klaviyo.

## Verify that all out-of-the-box events are working

Before attempting to add back in any customizations from your previous integration, be sure to verify that the new installation of the Klaviyo cartridge is working correctly. Use the frontend to generate events for **Searched Site**, **Viewed Category**, **Viewed Product,** **Added To Cart**, **Started Checkout** and **Order Confirmation**, and then check your Klaviyo account to make sure that these events are being tracked correctly.

Check the developer console for any new errors that may be related to the integration on all pages that generate Klaviyo events. Enable verbose service logging by checking the **Communication Log Enabled** checkbox at ****Administration > Operations > Services > KlaviyoEventService - Details****, and then review the server-side log files to verify that there are no errors, and that event data is being properly generated for each event type.

## Compare event data with production

You should now compare the event data in your testing and production Klaviyo accounts to ensure that nothing is missing, and that current values match the expected type. It is important to determine if any reporting or flows will be affected by the new integration. You will find that additional properties are now being set and sent to Klaviyo compared to the prior cartridge version.

## Add back site-specific customizations

You can now start adding customizations back into your Klaviyo code. Due to the fact that there are heavy structural and architectural changes with the newest Klaviyo cartridge, it is unlikely that you will be able to simply copy and paste custom code directly into the Klaviyo cartridge.

Each event type in the Klaviyo cartridge has a getData function that lives in a separate script file named for each event type. These files can be found in the `int_klaviyo_core/cartridge/scripts/klaviyo/eventData` folder, and are the most likely place that you will alter in order to add or update the data objects that get passed for each event. If you are creating new custom events, we recommend following the established pattern of adding code to server-side controllers **(**i.e., directly in SiteGen or via server.append in SFRA) that calls a getData function from a script file dedicated to the new event, and then uses the trackEvent function to send that data to Klaviyo via the KlaviyoEventService.

## Outcome

You’ve now upgraded your Klaviyo cartridge for Salesforce Commerce Cloud.

## Additional resources

- [Getting started with Salesforce Commerce Cloud](https://help.klaviyo.com/hc/en-us/articles/360033744951)
- [Salesforce Commerce Cloud data reference](https://help.klaviyo.com/hc/en-us/articles/360058323811)
- [How often integrations sync reference](https://help.klaviyo.com/hc/en-us/articles/115005253208)
- [How to contact support](https://help.klaviyo.com/hc/en-us/articles/115001002272)