---
id: 115005083107
title: "Getting started with Shift4Shop"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005083107-Getting-started-with-Shift4Shop"
section: "Shift4Shop"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:21Z"
language: en
---

## You will learn

Learn how to integrate Shift4Shop (formerly 3dcart) with Klaviyo in order to personalize and target emails based on each customer's purchases and website activity. The data synced from Shift4Shop to Klaviyo includes:

- Data about orders your customers make, including sales, refunds, fulfilled orders, and cancelled orders
- Detailed customer information, including when and how often people visit your website

Klaviyo only syncs information for customers who have placed an order within the last three years.

## Table of contents

1. Add the Shift4Shop Integration
2. Add Klaviyo onsite tracking
3. Monitor the data sync
4. Data synced from Shift4Shop
5. Additional resources

## Add the Shift4Shop integration

1. In Klaviyo, select the ****Integrations**** tab.
2. Select ****Explore apps****.
3. Search for **Shift4Shop** and click the card, then click ****Install****.
4. To find your Shift4Shop store URL (also known as your secure URL), open your Shift4Shop account in a new tab.
5. In Shift4Shop, go to ****Settings > General > Store Settings****.
6. Under Store Information, click on ****Manage Domain & Store URL****.![Shift4Shop settings page showing store information](https://klaviyo.zendesk.com/hc/article_attachments/28717985271707)
7. Copy the Store URL from beneath Domain Settings.
   ![Shift4Shop domain settings showing store URL](https://klaviyo.zendesk.com/hc/article_attachments/28717985269659)
8. Back in Klaviyo, paste your Store URL in the box and click ****Connect to Shift4Shop****.
9. Copy the Klaviyo Public API Key that appears on the next page.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28717985290907)
10. Click the ****Go to Shift4Shop**** button.
11. On the **REST API Apps** page in Shift4Shop, click ****Add**** in the top right hand corner to add the Klaviyo API key.
    ![REST API Apps page in Shift4Shop with Add button with blue background](https://klaviyo.zendesk.com/hc/article_attachments/28717991178907)
12. Paste the Klaviyo public API key (2bd83b00fcd7d56916a28c452d3d080c).
    ![Public key setting in Shift4Shop with Save button with blue background](https://klaviyo.zendesk.com/hc/article_attachments/28717985281051)
13. Click ****Save****.
14. A popup window will appear, asking you to give Klaviyo authorization to pull the Shift4Shop data into our platform; click ****Authorize****.
    ![Klaviyo settings in Shift4Shop showing required permissions with Authorize button with blue background](https://klaviyo.zendesk.com/hc/article_attachments/28717991176859)
15. You will be redirected back to your Klaviyo account and your data will begin to sync. A success callout will confirm that your data is syncing.

## Add Klaviyo onsite tracking

There are two Klaviyo onsite tracking code snippets you can add to your Shift4Shop site. The first onsite tracking snippet allows you to track when cookied users are active on your site (the **Active on Site** metric) and the second onsite tracking snippet allows you to track what products they view (the **Viewed Product** metric).

You can then use the **Active on Site** metric to create segments of known browsers who have visited your site but haven't purchased anything. The **Active on Site** snippet (also known as Klaviyo.js) also enables the use of Klaviyo sign-up forms.

**Viewed Product** tracking is most often leveraged to trigger a Browse Abandonment automated email flow. For more information, see our article on [creating a browse abandonment flow](https://help.klaviyo.com/hc/en-us/articles/115002775252).

1. Log in to your Shift4Shop store admin and navigate to ****Content > Site Content****.
2. Click on the ****Edit**** button under Header & Footer.
   ![Site Content page in Shift4Shop with Edit with blue background under Header and Footer](https://klaviyo.zendesk.com/hc/article_attachments/28717985286939)
3. Click the ****+**** to the right of Global Header to open the header editor.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28717985293211)
4. Click the slider next to **WYSIWYG Mode Off / On** to toggle the view to the HTML editor.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28717991195803)
5. To add **Active on Site** tracking, paste the following script at the bottom of the HTML editor:

   ```
   <script type="text/javascript" async="" src="https://static.klaviyo.com/onsite/js/PUBLIC_API_KEY/klaviyo.js"></script>
   <script type="text/javascript">
   //Initialize Klaviyo object on page load
   !function(){if(!window.klaviyo){window._klOnsite=window._klOnsite||[];try{window.klaviyo=new Proxy({},{get:function(n,i){return"push"===i?function(){var n;(n=window._klOnsite).push.apply(n,arguments)}:function(){for(var n=arguments.length,o=new Array(n),w=0;w<n;w++)o[w]=arguments[w];var t="function"==typeof o[o.length-1]?o.pop():void 0,e=new Promise((function(n){window._klOnsite.push([i].concat(o,[function(i){t&&t(i),n(i)}]))}));return e}}})}catch(n){window.klaviyo=window.klaviyo||[],window.klaviyo.push=function(){var n;(n=window._klOnsite).push.apply(n,arguments)}}}}(); </script>
   ```
6. In the first line of the snippet, replace **Public API Key** with your Klaviyo Public API Key, found under ****Account name > Settings > API Keys**** in Klaviyo.
7. To add **Viewed Product** tracking, add this script underneath the **Active on Site** script in the header:

   ```
   <script type="text/javascript">
   var klaviyo = window.klaviyo || [];

   // Track each product view.
   if ('[price]' !== '[' + 'price]') {
      klaviyo.track("Viewed Product", {
         ProductID: "[id]",
         Name: "[name]",
         Description: "[description]",
         URL: [location.protocol, '//', location.host, location.pathname].join(''),
         Categories: "[catid]",
         ImageURL: [location.protocol, '//', location.host, '/[image1]'].join(''),
         Price: parseFloat("[price]".slice(1), 10)
      });
   }
   </script>
   ```

     8. In the top right hand corner of the page, click ****Save****

## Monitor the Klaviyo sync

To view your Shift4Shop integration data:

1. In your Klaviyo account, navigate to ****Analytics > Metrics****.
2. Click on the ****Placed Order**** metric to verify that your data has started to populate. If you see data populating the chart, that means the Shift4Shop integration is successfully syncing to your account. When the sync is complete, you’ll see a green border next to the Shift4Shop integration when viewed in the ****Integrations**** tab.
   ![Shift4Shop integration card in Klaviyo with green bar on the left](https://klaviyo.zendesk.com/hc/article_attachments/28717991184411)
3. Klaviyo imports all of your historic Shift4Shop data. To verify this, compare the number of orders on a particular day in Klaviyo with what's in your Shift4Shop interface and confirm they match.
4. If they don't match, the issue is most likely that your Klaviyo account's timezone doesn't match your Shift4Shop timezone. To check your timezone setting in Klaviyo, go to ****Account name > Settings > Organization****.
5. In the middle of this page, you will see an area to set your timezone. Update your Klaviyo account to the correct timezone and click ****Update Information****.

## Data synced from Shift4Shop

The Shift4Shop integration syncs data into Klaviyo once every hour, so you should see events appear in Klaviyo within an hour of when the event is recorded in Shift4Shop.

The following metrics are synced from Shift4Shop:

- Fulfilled Order
- Ordered Product
- Placed Order
- Started Checkout

![Klaviyo metrics tab filtered by Shift4Shop showing metrics such as Fulfilled Order and Ordered Product](https://klaviyo.zendesk.com/hc/article_attachments/28717991188635)

### Fulfilled Order

This event is tracked when a customer completes the checkout process and creates an order in your Shift4Shop store. It includes all the product information about the items someone purchased including product names, images, and variation information to use in purchase follow-up emails. You can filter and target **Fulfilled Order** events based on the following criteria:

- Items: the names of the products in someone's order, e.g., t-shirt or pants
- Categories: the complete set of the categories of the products in someone's order, e.g., t-shirts, men's, pants, and sale

### Ordered Product

This metric is tracked when a customer places their order, and tracks an event for each item someone purchases. For example, if someone buys a t-shirt and a pair of pants, two **Ordered Product** events are created - one for the t-shirt and one for the pants.

The **Ordered Product** event includes detailed information about each product someone purchases. This is useful when creating behavioral segments based on product variation options and other detailed information that's not available in the **Placed Order** event. You can filter and target **Ordered Product** events based on the following criteria:

- Name: the name or title of the product in Shift4Shop, e.g., t-shirt or pants
- SKU: the SKU of the product variation e.g., REDMEDIUMTSHIRT
- Categories: the complete set of the categories of the product, e.g., t-shirts, men's, and sale

### Placed Order

This event is tracked when a customer completes the checkout process and creates an order in your Shift4Shop store. It includes all of the product information about the items someone purchased including product names, images, and variation information to use in purchase follow-up emails. You can filter and target **Placed Order** events based on the following criteria:

- Items: the names of the products in someone's order, e.g., t-shirt or pants
- Categories: the complete set of the categories of the products in someone's order, e.g., t-shirts, men's, pants, and sale
- Item Count: the number of items in the order, e.g., **2**

Note: By default, Shift4Shop syncs two statuses for Placed Order: 2, 4

### Started Checkout

This event is tracked when a customer enters their contact and shipping information on the page before the payment page in the Shift4Shop checkout process and clicks continue. It includes all of the product information about the items in someone's cart, including product names, images, and variation information to use in your abandoned cart emails. You can filter and target **Started Checkout** events based on the following criteria:

- Items: the names of the products in someone's cart, e.g., t-shirt or pants
- Categories: the complete set of the categories of the products in someone's cart, e.g., t-shirts, men's, pants, and sale

### Customer Data

In addition to the metrics Klaviyo syncs from Shift4Shop, there are also properties that are added to each Klaviyo profile. You can use these properties in segments and in flows. The following built-in Klaviyo properties automatically synced from Shift4Shop:

- Email
- First Name
- Last Name
- City
- State/Region
- Zip Code
- Country
- Phone Number

## Outcome

You’ve now integrated with Shift4Shop, enabled Klaviyo onsite tracking, and verified your synced Shift4Shop data. Now, you can view your Shift4Shop data in Klaviyo and personalize and target emails based on each customer's purchases and website activity.

## Update your Shift4Shop integration

Did you integrate Klaviyo with Shift4Shop before May 12, 2025? If so, you are using our old app. Klaviyo has released a new Shift4Shop app to improve security and stability. Our old app will be retired on September 6, 2025 and will cease to work at that time.

To update to the new integration, you need to re-install your Shift4Shop app in Klaviyo:

1. In Klaviyo, click the ****Integrations**** tab.
2. Select ****Shift4Shop**** from the list of enabled integrations.
3. In the upper right corner, click ****Manage integration****.
4. Select ****Re-authenticate****.
5. Copy the Klaviyo public API key.
6. Click the ****Go to Shift4Shop**** button.
7. On the **REST API Apps** page in Shift4Shop, click ****Add**** to add the Klaviyo API key, and paste the key.
8. Click ****Save****.
9. On the authorization request modal that appears, click ****Authorize****.
10. You will be redirected back to your Klaviyo account, where a confirmation modal will indicate that your Shift4Shop account is now connected.

Your integration has now been updated and will begin using the new app.

While not necessary, you may wish to remove the deprecated Klaviyo app from your **Connected Apps** in Shift4Shop. To do so, remove the "Klaviyo" app from the Shift4Shop REST API Apps page.

## Additional resources

- [Getting started with Klaviyo onsite tracking](https://help.klaviyo.com/hc/en-us/articles/115005076767)
- How to update [Klaviyo after switching ecommerce](https://help.klaviyo.com/hc/en-us/articles/360003124151) platforms