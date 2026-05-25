---
id: "17928628922395"
title: "Understand Klaviyo's anonymous visitor activity backfill"
source_url: "https://help.klaviyo.com/hc/en-us/articles/17928628922395-Understand-Klaviyo-s-anonymous-visitor-activity-backfill"
section: "Understand profiles"
category: "Audience"
category_slug: "analytics-audience"
klaviyo_updated: "2026-04-21T13:54:31Z"
language: "en"
---
## You will learn

Learn about anonymous visitor activity backfilling and how to capture shoppers’ onsite engagements before they are identified.

## Before you begin

By default, Klaviyo’s web tracking supports:

- ******Active on Site****** ****tracking****
  This metric is tracked whenever an identifiable browser visits your website.
- ******Viewed Product****** ****tracking****
  This metric is tracked whenever an identifiable browser views a product page on your website (for ecommerce stores).

**Active on Site** can help segment you identify profiles that are visiting your site, while **Viewed Product** tracking can enable you to send customers reminders in a browse abandonment flow.

Note that some integrations do not have **Viewed product** tracking installed automatically.

## Anonymous visitor activity backfill

With Klaviyo’s anonymous visitor activity backfill, you can capture onsite activity for a shopper prior to identification. Once that visitor is identified in the future, you’ll then have access to their historical onsite events. This allows you to have a more complete view of your customers’ journeys, regardless of when they are identified through Klaviyo’s web tracking.

The anonymous activity backfill only captures and sets historical events on a profile and other historical information like [Source](https://help.klaviyo.com/hc/en-us/articles/115005075187) will not be captured by this feature.

## How does anonymous visitor backfill work

When a site visitor has consented to analytics and marketing cookies and has not been identified, Klaviyo will track their site activity in their browser’s local storage for up to 14 days under a client side cookie ‘kl-post-identification-sync’. Once the site visitor is identified, all events stored in the cookie will be pushed to Klaviyo for that profile.

Anonymous backfill will be triggered when:

1. After submitting consent through a form
2. Clicking on a link in a Klaviyo message
3. Identified using Klaviyo’s Identify API
4. Contact information has been entered or a purchase has been made on most e-commerce platforms

By default, Klaviyo supports identification via checkout on most e-commerce platforms:

|  |  |
| --- | --- |
| ****E-Commerce Platform**** | ****Supported**** |
| Shopify | ✅ [When Shopify additional tracking is enabled](https://help.klaviyo.com/hc/en-us/articles/4425956184731) |
| WooCommerce | ✅ |
| BigCommerce | ⚠️ - Requires a custom script installed on your checkout page(s) |
| Magento 2 | ⚠️ - Requires validation |
| Salesforce Commerce Cloud | ⚠️ - After version 23.7.0 |
| Prestashop | ✅ |
| Wix | ❌ |
| Custom and other e-commerce platforms | Requires custom script installation |

If you are using BigCommerce, some versions of Magento 2, custom, or other e-commerce platforms the following script needs to be installed on your checkout page if you want to trigger anonymous visitor backfill when a customer makes a purchase on your site:

```
window.onload = function() {    // For grabbing the email right after it's entered     // Add the field that contains the customer's email address to this list    const emailSelectors = [        "input[id='email']",        "input[name='email']",        "input[placeholder='Email']",        "input[type='email']"    ]    document.querySelector(emailSelectors.join(",")).addEventListener('blur', function() {        klaviyo.identify({"email" : this.value}).then(() => console.log("Identified"))    });};window.onload = function() {    // For grabbing the email when the submit/order button is pressed    // Add the field that contains the customer's email address to this list    const emailSelectors = [        "input[id='email']",        "input[name='email']",        "input[placeholder='Email']",        "input[type='email']"    ]    // Add the purchase or complete transaction button to this list     const submitSelectors = [        "input[id='submit']",        "input[name='submit']",        "input[type='submit']"    ]    document.querySelector(submitSelectors.join(",")).addEventListener('click', function() {        klaviyo.identify({            "email" : document.querySelector(emailSelectors.join(",")).value        }).then(() => console.log("Identified"))    });};
```

## Testing anonymous visitor backfill

To verify that anonymous visitor historical backfill is working, you can take the following steps:

Make sure that front-end events, such as **Viewed Product,** are triggering successfully prior to testing, details can be found [here](https://help.klaviyo.com/hc/en-us/articles/115005076767#h_01HADAYAACFYSN7F22XPPCGT6B).

#### Testing the capture of anonymous activity on your site

1. Navigate to your website in a private window and take an onsite action like **Viewed Product.**
2. [Open the developer console](https://www.computerhope.com/issues/ch002153.htm) on your browser and navigate to local storage. This may be on the developer console’s **Storage** or **Application** tab depending on your browser.
   ![Local storage in Chrome console](https://klaviyo.zendesk.com/hc/article_attachments/17929088337691)
3. Verify that the key and values set in the browser match the actions you took while anonymous. Note the timestamp of the data.
4. After confirming that data is being stored in the browser, add ****?utm\_email=example@gmail.com**** to the end of your website URL, replacing **example@gmail.com** with a test email address and reload the page. This will identify the browser based on the email address you provide.
5. Search for the email address in Klaviyo.

You should see a profile matching the email address that you supplied, with an activity timeline corresponding to the actions you took while anonymous. Ensure that the key and values in your local storage have been cleared out, and that the events have made their way into your Klaviyo account with the correct timestamps.

## Testing anonymous visitor backfill from checkout

1. Navigate to your website in a private window and take an onsite action like Viewed Product.
2. Add a product to your cart and start checkout
3. Enter your contact information
4. Place an order
5. Search for the email address in Klaviyo.

You should see a profile matching the email address that you supplied, with an activity timeline corresponding to the actions you took while anonymous. Ensure that the key and values in your local storage have been cleared out, and that the events have made their way into your Klaviyo account with the correct timestamps.

## Frequently asked questions

### Can I disable anonymous visitor activity backfill?

To disable anonymous visitor activity backfill:

1. Navigate to ****Account > Settings**** in the bottom left corner in Klaviyo.
2. On the **Data** tab in your account settings, uncheck the **Enable anonymous visitor tracking** box.
3. Select the ****Update**** button.

![](https://klaviyo.zendesk.com/hc/article_attachments/39973078206363)

### Klaviyo’s standard web tracking

In order for Klaviyo to track a shopper’s onsite activity by default****,**** they must be identified. This is done through[Klaviyo’s JavaScript](https://help.klaviyo.com/hc/en-us/articles/360002035871), which sets a[cookie](https://help.klaviyo.com/hc/en-us/articles/360034666712) that allows for the tracking and identification of site visitors through an auto-generated ID when they:

- Fill out a Klaviyo signup form
- Click a link from a Klaviyo message

This cookie can temporarily hold personally identifiable information and lasts for up to two years.

The Klaviyo cookie is only used for web tracking after a shopper has been identified and does not store data for anonymous visitors.

### How Klaviyo collects onsite data for anonymous visitors

To collect onsite data for anonymous visitors, Klaviyo records data about a visitor's actions as they occur and stores that locally in their browser. In the future when that visitor is identified, that data is then sent to Klaviyo and cleared from the browser. Any future onsite activity will be tracked as usual through the Klaviyo cookie once they have been identified as well.

To store data in the browser, the shopper’s browser must support setting items in local storage.

See a list of browsers that support[writing data into local storage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage#browser_compatibility).

Note that if a site visitor is using any type of cookie-blocking (e.g, incognito in Chrome or private browsing in Safari) Klaviyo cannot record and recover anonymous events.

### What events are included in post-identification syncing?

Only client-side events, also known as front-end events, are captured through Klaviyo’s web tracking for both identified and anonymous visitors. These events are captured through Klaviyo's main onsite tracking snippet, known as Klaviyo.js.

Some common events include:

- Active on site - All integrations
- Viewed product - Most e-commerce integrations
- [Added to cart](https://help.klaviyo.com/hc/en-us/articles/6985692431259) - Most e-commerce integrations

However, any events recorded onsite via[klaviyo.track()](https://developers.klaviyo.com/en/docs/guide_to_setting_up_api_based_website_activity_events) are also included in anonymous activity backfill.

Note that some integrations may use server-side events for these. For example, the **Added to Cart** event on Magento 2 is sent server-side.

### How many events can be stored in local storage?

There is a 5MB limit imposed by a browser’s local storage, allowing for up to 10,000 events.

### Why use local storage for data storage over cookies?

Cookies are less robust compared to local storage. For example, cookies have an expiration date and a maximum size of about 4KB. Local storage can hold 5 MB on average (depending on the browser).

Safari has a 7 day expiration policy for local storage.

### Are there any GDPR or privacy concerns?

Anonymous visitor activity backfill uses a browser's local storage to store data sent as a profile property or event until the browser is identified (after which the local data is cleared).

Until it is cleared, data in local storage is accessible to any on-website Javascript. This can pose a privacy concern if you send certain types of sensitive data through front-end events. For sensitive data, Klaviyo recommends only sending the data via [server-side requests](https://developers.klaviyo.com/en/v1-2/docs/getting-started-with-track-and-identify-apis), or only after a browser is identified.

### Does anonymous visitor activity backfill work with a cookie consent tool?

If your store uses a cookie consent tool (e.g., [OneTrust](https://help.klaviyo.com/hc/en-us/articles/4764571493275)), the shopper would need to opt-in for anonymous activity to be captured. Without access, Klaviyo will not be able to write data to the browser’s local storage.

### Do anonymous visitors trigger flows?

Once an anonymous visitor is identified through Klaviyo's standard web tracking, they will trigger flows as long as they qualify and have not exceeded time delays.