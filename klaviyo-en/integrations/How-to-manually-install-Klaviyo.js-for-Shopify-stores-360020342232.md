---
id: "360020342232"
title: "How to manually install Klaviyo.js for Shopify stores"
source_url: "https://help.klaviyo.com/hc/en-us/articles/360020342232-How-to-manually-install-Klaviyo-js-for-Shopify-stores"
section: "Shopify troubleshooting"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:43Z"
language: "en"
---
## You will learn

Learn how to manually install Klaviyo’s **Active on Site** tracking snippet, also known as Klaviyo’s onsite JavaScript or Klaviyo.js, on your Shopify store. You should only do this if you experience very high web traffic or your site suffers from slow loading time for any other reason (though Klaviyo has recently [improved load times](https://klaviyo.tech/improving-forms-performance-c67c98114d49) and thus may not be the cause). Otherwise, we recommend you install Klaviyo.js by [enabling Klaviyo’s Shopify app embed](https://help.klaviyo.com/hc/en-us/articles/4425956184731).

## Before you begin

If you choose to manually install Klaviyo.js and previously had it enabled via Klaviyo's app embed, you must first disable the app embed in your Shopify theme settings.

![Klaviyo app embed for onsite tracking in Shopify toggled off](https://klaviyo.zendesk.com/hc/article_attachments/28716065121563)

Because pasting this code requires access to your site's HTML and ecommerce platform, our support team is unable to offer hands-on assistance. If you don't have a developer on your team and are not comfortable adding the code yourself, consider [reaching out to a Klaviyo partner for assistance](https://klaviyo.partnerpage.io/).

## Install Klaviyo.js on your Shopify store

1. Copy the code snippet below:

   ```
   <script type="text/javascript" async="" src="https://static.klaviyo.com/onsite/js/PUBLIC_API_KEY/klaviyo.js"></script>
   ```
2. In the code snippet, be sure to replace PUBLIC\_API\_KEY with [your six-digit Klaviyo Public API Key](https://www.klaviyo.com/account#api-keys-tab).
3. If you've enabled [Customer Accounts](https://help.shopify.com/en/manual/customers/customer-accounts) for your store, add an extra script to identify your customers with the email they use to log in to your store. The full set of scripts will look like the following:

   ```
   <script type="text/javascript" async="" src="https://static.klaviyo.com/onsite/js/PUBLIC_API_KEY/klaviyo.js"></script>
   <script type="text/javascript">
   //Initialize the Klaviyo object on page load
   !function(){if(!window.klaviyo){window._klOnsite=window._klOnsite||[];try{window.klaviyo=new Proxy({},{get:function(n,i){return"push"===i?function(){var n;(n=window._klOnsite).push.apply(n,arguments)}:function(){for(var n=arguments.length,o=new Array(n),w=0;w<n;w++)o[w]=arguments[w];var t="function"==typeof o[o.length-1]?o.pop():void 0,e=new Promise((function(n){window._klOnsite.push([i].concat(o,[function(i){t&&t(i),n(i)}]))}));return e}}})}catch(n){window.klaviyo=window.klaviyo||[],window.klaviyo.push=function(){var n;(n=window._klOnsite).push.apply(n,arguments)}}}}(); </script>
   <script type="text/javascript">
   //Customer accounts
   var klaviyo = window.klaviyo || [];
   if ("{{ customer.email }}") {klaviyo.identify({"$email" : "{{ customer.email }}"})};
   </script>
   ```
4. From your Shopify Admin click ****Online Store**** > ****Themes****. From the dropdown click ****Edit Code****.
   ![Shopify Themes page with Action dropdown open showing Edit Code optio](https://klaviyo.zendesk.com/hc/article_attachments/28716065126043)
5. Search for the files you want to add the snippet to and click to open it in the editor. You can add the snippet to any page templates where you want to enable Klaviyo forms and tracking on the corresponding pages.
6. Scroll to the bottom of the file and paste your snippet below the other code.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/30186621806875)
7. Click ****Save****.

## Test your Active on Site tracking

To test that your **Active on Site** tracking is set up properly, follow these steps:

1. Navigate to your website.
2. On your homepage, add the following to the end of the URL, replacing **example@gmail.com** with your email address:
   **?utm\_email=example@gmail.com
   ![Test store in Shopify with ?utm_email=example@gmail.com amended to URL](https://klaviyo.zendesk.com/hc/article_attachments/28716065123227)**
3. Reload the page.
4. Search in Klaviyo for your email address.
   ![Klaviyo dashboard with email address in search bar](https://klaviyo.zendesk.com/hc/article_attachments/28716065129883)

You should see that a Klaviyo profile has been created for you (if one didn't exist already) and that this activity has been tracked on your activity feed.

Now that you've installed Klaviyo.js, you'll be able to utilize Active on Site tracking, Klaviyo sign-up forms, and more.

Based on your Customer Privacy settings in Shopify, Klaviyo may not track onsite events for visitors to your Shopify store in the EU, EEA, UK and Switzerland, unless they have provided consent.

## Additional resources

- [Getting started with Shopify](https://klaviyo.zendesk.com/hc/en-us/articles/115005080407)
- [Getting started with Klaviyo onsite tracking](https://klaviyo.zendesk.com/hc/en-us/articles/115005076767)
- [Getting started with sign-up forms](https://klaviyo.zendesk.com/hc/en-us/articles/360026474752)