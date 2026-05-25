---
id: "115005255408"
title: "How to integrate with OpenCart"
source_url: "https://help.klaviyo.com/hc/en-us/articles/115005255408-How-to-integrate-with-OpenCart"
section: "OpenCart"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:24Z"
language: "en"
---
## You will learn

Learn how to integrate OpenCart with Klaviyo. After completing these steps, you'll be able to personalize and target emails based on each customer's purchase and website activity. The OpenCart integration syncs every hour.

## Before you begin

Please note that Klaviyo does not sync your catalog from OpenCart.

## Add the OpenCart integration

The process of adding Klaviyo's OpenCart integration is multi-step and requires taking actions inside of both OpenCart and Klaviyo.

To get started, Klaviyo currently supports OpenCart 1.4.x and 1.5.x. Download the Klaviyo OpenCart module from here: <https://www.klaviyo.com/media/downloads/OpenCartKlaviyo-1.1.0.tgz>.

1. Unzip the file into the root of your OpenCart installation.
2. Log in to the OpenCart admin section and go to the ****Extensions > Modules**** page.
3. Install the Klaviyo module and then click **Edit** for the Klaviyo module.
4. The last thing to do with your OpenCart install is copy and paste the following PHP code at the end of the `upload/index.php`, right before the `$response->getOutput();` line:

   ```
   // [Klaviyo] Save customer cart if it exists.
   if ($registry->get('cart')->hasProducts()) {
     $registry->get('load')->model('module/klaviyo');

     if ($registry->get('customer')->isLogged()) {
       $registry->get('model_module_klaviyo')->saveCustomerCart(
         session_id(),
         $registry->get('customer')->getId(),
         $session->data['cart']
       );
     } else if (array_key_exists('guest', $session->data)) {
       $registry->get('model_module_klaviyo')->saveGuestCart(
         session_id(),
         $session->data['guest'],
         $session->data['cart']
       );
     }
   }
   ```
5. In Klaviyo, select the ****Integrations**** tab.
6. Click ****Explore apps**** and search for **OpenCart**, then click the card. Then, click ****Install****.
7. You will be taken to an **Integration Settings**page. On the settings page, enter the URL of your OpenCart site and click ****Connect to OpenCart****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28715969274139)
8. On the next page, copy the API key under **Klaviyo OpenCart Module** and paste it into the Klaviyo module settings in OpenCart. Save the Klaviyo module settings in the OpenCart admin.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28715969282587)
9. If desired, check the setting **Add new OpenCart customers to a Klaviyo list**, then select a list from the dropdown.
10. Back in Klaviyo, click ****Complete setup**** to start syncing data.

## Install Klaviyo onsite tracking

To track onsite activity in OpenCart, first find your Klaviyo public API key by logging in to your account, clicking your account name in the lower left corner, and navigating to****Settings > API Keys****. Your public key is six characters long. There are two types of onsite tracking you can install:

- ****Active on Site****This metric is tracked whenever an identifiable browser visits your website
- ****Viewed Product****This metric is tracked whenever an identifiable browser views a product page on your website

### Add "Active on Site" tracking

This metric is tracked whenever an identifiable browser visits your website. To begin tracking **Active on Site** activity:

1. Add the following snippet of code to your main store template so it's included on all pages. You should place this snippet either with other analytics scripts you use or right before the closing **</body>** tag:

   ```
   <script type="text/javascript" async="" src="https://static.klaviyo.com/onsite/js/PUBLIC_API_KEY/klaviyo.js></script>
   <script type="text/javascript">
   //Initialize Klaviyo object on page load
   !function(){if(!window.klaviyo){window._klOnsite=window._klOnsite||[];try{window.klaviyo=new Proxy({},{get:function(n,i){return"push"===i?function(){var n;(n=window._klOnsite).push.apply(n,arguments)}:function(){for(var n=arguments.length,o=new Array(n),w=0;w<n;w++)o[w]=arguments[w];var t="function"==typeof o[o.length-1]?o.pop():void 0,e=new Promise((function(n){window._klOnsite.push([i].concat(o,[function(i){t&&t(i),n(i)}]))}));return e}}})}catch(n){window.klaviyo=window.klaviyo||[],window.klaviyo.push=function(){var n;(n=window._klOnsite).push.apply(n,arguments)}}}}(); </script>
   ```
2. Make sure to replace `PUBLIC_API_KEY` with your Klaviyo account's Public API key.
3. If visitors or customers can create accounts for your store, add the following snippet directly below the first snippet:

   ```
   <script type="text/javascript">
     var klaviyo = window.klaviyo || [];
     {% if user.is_logged_in %}
     klaviyo.identify({
       $email: '{{ user.email }}',
       $first_name: '{{ user.first_name }}',
       $last_name: '{{ user.last_name }}'
       });
     {% endif %}
   </script>
   ```
4. Depending on the types of templates you use for your website, the **{% if user.is\_logged\_in %}** and **{{ user.email }}**syntax are likely different. Using the template language available, you want to check if the person viewing the current page is logged in. If so, you should output their email and name, if available. If you don't have name information, remove those two lines and the trailing comma after the email **$email** line.

### Add "Viewed Product" tracking

If you'd like to set up [a Browse Abandonment flow](https://help.klaviyo.com/hc/en-us/articles/115002775252-Create-a-Browse-Abandonment-Flow) or build segments based on product browsing data, you'll want to add JavaScript event tracking for a "Viewed Product" metric.

1. On your product page template, add the following snippet:

   ```
   <script type="text/javascript">
       var klaviyo = window.klaviyo || [];
       klaviyo.track("Viewed Product", {
         Title: '{{ product.title }}',
         ItemId: {{ product.id }},
         Categories: {{ category in product.categories|json }}, // The list of categories is an array of strings.
         ImageUrl: '{{ product.image_url }}',
         Url: '{{ product.url }}',
         Metadata: {
           Brand: '{{ product.brand }}',
           Price: {{ product.price }},
           CompareAtPrice: {{ product.compare_at_price }} // If you have a compare at price. You could also include this for a sale or special price.
         }
     });
   </script>
   ```
2. The snippet above uses the `{{ }}` placeholder syntax which may be different for your OpenCart store. The important part is that product fields are dynamically rendered based on which product page you're viewing.
3. After **Viewed Product** tracking has been configured for your site, **Viewed Product** data should begin populating in your Klaviyo account as known visitors browse your product pages.

### How onsite tracking works

When you add Klaviyo web tracking to your site, we are only able to track the browsing activity of "known browsers" - i.e. browsers that have visited and engaged at least once before. There are two key ways we are able to identify a site visitor for web tracking purposes:

- If someone has, at some point, clicked through a Klaviyo email to your website
- If someone has, at some point, subscribed/opted-in through a Klaviyo form

Klaviyo will not track anonymous browsers.

## Monitor the Klaviyo sync

The time it will take to sync all historic customer and order data from your OpenCart store depends on the size of your store. Once this historic sync is complete, you will see a green border around your OpenCart integration under **Enabled Integrations**.

To check your integration:

1. Navigate to your account's ****Metrics**** tab, found under ****Analytics****. Here, you can filter to view all OpenCart metrics. Find OpenCart's **Placed Order**metric and click on the Activity Feed icon. If your integration has begun syncing data, you will start to see **Placed Order** events populate here.
2. We will automatically sync all historic order data. To verify this, you can compare the number of event on a particular day in Klaviyo with what's in your OpenCart interface and confirm they match.
3. For example, when exploring the Placed Order metric, you can mouse over yesterday's data point or look at the table of data below the chart to see how many orders were reported yesterday.
4. Compare that number to what's stored in OpenCart from yesterday and you should see they match exactly. If they don't, the issue is most likely that your Klaviyo account's timezone doesn't match your set OpenCart timezone.
5. To check or update your account's timezone:

   - Click your organization name in the bottom left.
   - Select ****Settings****.
   - Go to the ****Organization**** tab.

## Data synced from OpenCart

- ****Sales and order data****Which products were purchased, including product details and images.
- ****Customer information****First name, last name, location, and customer group.
- ****Started checkout data****Used to trigger Abandoned Cart emails. This is enabled by the PHP code snippet you added when integrating.
- ****Fulfilled order data****Used to track when orders are shipped.
- ****Onsite tracking****When people visit your website

To your OpenCart metrics, navigate to ****Analytics > Metrics**** in Klaviyo****,**** where you can filter by OpenCart.

![Metrics tab in Klaviyo filtered by OpenCart with Fulfilled Order, Ordered Product, Placed Order, and Started Checkout in list](https://klaviyo.zendesk.com/hc/article_attachments/28715969267995)

By default, Klaviyo syncs the following statuses for **Placed Order** and **Fulfilled Order** metrics:

- ****Placed Order:****Pending, Processed, Processing, Shipped, Complete
- ****Fulfilled Order:****Shipped, Complete

## Additional resources

- [How often integrations sync reference](https://klaviyo.zendesk.com/hc/en-us/articles/115005253208)
- Need more help integrating with Klaviyo? Check out [Klaviyo's Agency Partners](https://klaviyo.partnerpage.io/?utm_source=helpcenter&utm_medium=integrations)