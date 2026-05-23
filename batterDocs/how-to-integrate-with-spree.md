<h1>How to integrate with Spree</h1>

## You will learn

Learn how to integrate Spree with Klaviyo. After completing these steps, you'll be able to personalize and target emails based on each customer's purchases and website activity. Here's the data we sync from Spree:

- Sales and order data including which products were purchased, product images, variant details and any discounts applied
- Customer information including first and last name, location, and how they found your store
- Fulfilled order data

A security patch pushed for Spree versions 2.2.14, 2.3.13, 2.4.10, and 3.0.4 forces searchable parameters to be allowlisted. The `updated_at` property of products and orders was not included in the default allowlist. Klaviyo's integration relies on this parameter, and thus you will need to push an update to allowlist this property to ensure your integration runs smoothly. If you don't allowlist the `updated_at` property for orders, **Started Checkout** events may not sync until an order is placed.

## Add the Spree integration in Klaviyo

1. In Klaviyo, select the ****Integrations**** tab.
2. Click ****Explore apps****, search for S**pree**, and click the card. Then, click ****Install****.
3. On the next page, you'll need to provide your Store URL and a Spree API key / Encrypted Password. You can generate this API key in your Spree admin by navigating to ****Users****, choosing an account, and then selecting ****Generate API Key****.
4. Back in Klaviyo, paste your Store URL and API key/encrypted password in the boxes.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28720771093915)
5. If you are using a versioned Spree API (v1), check the corresponding box.
6. Click Connect to Spree.
7. If you would like to add customers who opt-in to receive email from your Spree store to a list in Klaviyo, check the **Add new Spree customers to a Klaviyo list** box on the next page. After checking this box, select a list to which new opt-ins will get added.
8. When you're ready, click ****Complete setup****. You should then see a success message indicating you have integrated successfully.

## Install Klaviyo onsite tracking

To install onsite tracking, which consists of two events - **Active on Site** and **Viewed Product**, first find your public API key. Log in to your Klaviyo account and go to ****Account name > Settings > API keys****. Your public key is six characters long. Securely copy this key for use in the next step.

There are two types of onsite tracking you can leverage:

- ****Active on Site****This metric is tracked whenever an identifiable browser visits your website
- ****Viewed Product****This metric is tracked whenever an identifiable browser views a product page on your website

### "Active on Site" tracking

This metric is tracked whenever an identifiable browser visits your website.

1. To begin tracking **Active on Site** activity, add the following snippet of code to your main store template so it's included on all pages. You should place this snippet either with other analytics scripts you use or right before the closing **</body>** tag.
2. Make sure to replace `Public API Key` with your Klaviyo account's Public API key:

   ```
   <script type="text/javascript" async="" src="https://static.klaviyo.com/onsite/js/klaviyo.js?company_id=PUBLIC_API_KEY"></script>
   <script type="text/javascript">
   //Initialize the Klaviyo object on page load
   !function(){if(!window.klaviyo){window._klOnsite=window._klOnsite||[];try{window.klaviyo=new Proxy({},{get:function(n,i){return"push"===i?function(){var n;(n=window._klOnsite).push.apply(n,arguments)}:function(){for(var n=arguments.length,o=new Array(n),w=0;w<n;w++)o[w]=arguments[w];var t="function"==typeof o[o.length-1]?o.pop():void 0,e=new Promise((function(n){window._klOnsite.push([i].concat(o,[function(i){t&&t(i),n(i)}]))}));return e}}})}catch(n){window.klaviyo=window.klaviyo||[],window.klaviyo.push=function(){var n;(n=window._klOnsite).push.apply(n,arguments)}}}}(); </script>
   ```
3. Depending on the types of templates you use for your website, the **{% if user.is\_logged\_in %}** and **{{ user.email }}**syntax are likely different. Using the template language available, you want to check if the person viewing the current page is logged in. If so, you should output their email and name, if available. If you don't have name information, remove those two lines and the trailing comma after the email **$email** line.
4. This Klaviyo tracking code will allow you to track an **Active on Site**metric so that you can see and leverage data related to site visits and visitor behavior. Through this metric, Klaviyo will track onsite activity for known browsers.
5. To test that your onsite tracking is set up properly, go to a page in your store and add `?utm_email=email@example.com` to the end the URL replacing **email@example.com** with your email address. After your reload the page, search in Klaviyo for your email address. You should see a profile has been created and has tracked your site activity.

### "Viewed Product" tracking

If you'd like to set up [a browse abandonment flow](https://klaviyo.zendesk.com/hc/en-us/articles/115005255408) or build segments based on product browsing data, you'll want to add JavaScript event tracking for a **Viewed Product** metric.

1. On your product page template, add the following snippet:

   ```
   <script type="text/javascript">
    var klaviyo = window.klaviyo || [];
    klaviyo.track("Viewed Product", {
       Title: '{{ product.name }}',
       ItemId: {{ product.id }},
       Categories: {{ category in product.categories|json }}, // The list of categories is an array of strings.
       ImageUrl: '{{ product.image_url }}',
       Url: '{{ product.permalink }}',
       Metadata: {
       Brand: '{{ product.brand }}',
       Price: {{ product.price }},
       OnSale: {{ product.on_sale }},
       RegularPrice: {{ product.regular_price }},
       SalePrice: {{ product.sale_price }}
    }
    });
   </script>
   ```
2. The snippet above uses the `{{ }}` placeholder syntax which may be different for your Spree store. The important part is that product fields are dynamically rendered based on which product page you're viewing.
3. After **Viewed Product** tracking has been configured for your site, **Viewed Product** data should begin populating in your Klaviyo account as known visitors browse your product pages.

### How onsite tracking works

When you add Klaviyo onsite tracking to your site, we are only able to track the browsing activity of "known browsers" - i.e. browsers that have visited and engaged at least once before. There are two key ways we are able to identify a site visitor for onsite tracking purposes:

- If someone has, at some point, clicked through a Klaviyo email to your website
- If someone has, at some point, subscribed/opted-in through a Klaviyo form

Klaviyo will not track anonymous browsers.

## Monitor the Klaviyo sync

To check your integration:

1. Click the ****Analytics**** dropdown in Klaviyo and select ****Metrics****. Here, you can filter to view all Spree metrics.
2. Find Spree's **Placed Order**metric and click on the Activity Feed icon. If your integration has begun syncing data, you will start to see **Placed Order** events populate here.
3. We will automatically sync all historic order data. To verify this, you can compare the number of event on a particular day in Klaviyo with what's in your Spree interface and confirm they match. For example, when exploring the **Placed Order** metric, you can mouse over yesterday's data point or look at the table of data below the chart to see how many orders were reported yesterday.
4. Compare that number to what's stored in Spree from yesterday and you should see they match exactly. If they don't, the issue is most likely that your Klaviyo account's timezone doesn't match your set Spree timezone.
5. To check your timezone setting in Klaviyo:
   - Click your account name in the lower left.
   - Select then clicking ****Settings**** ****> Organization****.
   - Scroll down to **Timezone**.
6. Once this historic sync has completed, you will see a light green border around your Spree integration in the ****Integrations**** tab.

## Data synced from Spree

The Spree integration syncs with Klaviyo every hour.

Below are a list of metrics which Spree syncs into Klaviyo. You can view all Spree metrics which sync into your account under ****Analytics > Metrics****.

![Metrics tab in Klaviyo filtered by Spree showing metrics such as Fufilled Order and Ordered Product](https://klaviyo.zendesk.com/hc/article_attachments/28720771091739)

### Placed Order

This metric records an event every time someone places an order and successfully pays for it. It corresponds to orders in Spree that are complete, meaning a customer has completed the entire checkout process. With this metric, you can easily create dynamic lists of people based on the number of orders they've placed or their lifetime value. You can also create emails to re-engage past customers or send customer thank you emails for first time buyers. You can filter and target **Placed Order** events based on the following criteria:

- ****IsDiscounted****If an order had a discount applied, e.g., **true**or **false**.
- ****ItemNames****The names of the products purchased in this event.

### Ordered Product

This metric is similar to the **Placed Order** metric, however an event is recorded for each item someone orders. For example, if someone purchased a t-shirt and a pair of shorts, this would appear in Klaviyo as one **Placed Order** event and two **Ordered Product** events, one for the t-shirt and one for the pair of shorts. This metric is useful for building lists that target customers who purchased (or have not purchased) specific items or items in specific categories. You can also use the **Ordered Product** metric as a trigger for flows to send emails about related products that naturally go together, but some customers haven't already bought.

- ****Categories****The categories the product ordered belong to, e.g., **Shirts,** **Mens** or **Sale**.
- ****Name****The name of the product purchased, e.g., **Men's Red T-Shirt**.
- ****ProductId****The id of your product as it is set in your store, e.g., **2022, 2023, 2024**.
- ****Quantity****The quantity of a product ordered.
- ****SKU****The SKU of the product as it is set in your store.
- ****Variant Option: Color****The color of the product, if available, e.g., **Red**or**Blue**.
- ****Variant Option: Size****The size of the product, if available, e.g., **Medium**or **Large**.

### Fulfilled Order

This metric records an event when a customer's order ships. The event in Klaviyo includes the tracking number for any shipments, so you can use this metric as a trigger for shipping confirmation emails. Another common email based on the **Fulfilled Order** metric is the product review email, where you ask customers to leave a review for items they recently purchased. Using the **Fulfilled Order** metric allows you to time these emails based on when someone receives their order so you don't have to worry sending them an email before they've received their package. You can filter and target **Fulfilled Order** events based on the following criteria:

- ****IsDiscounted****If an order had a discount applied, e.g., **true**or **false**.
- ****ItemNames****The names of the items purchased in this event.

### Started Checkout

This metric records an event each time someone starts a checkout and has entered their email address. The primary use for this metric is sending abandoned cart emails. With Klaviyo, you can easily set up an email flow to send a cart reminder if someone started to checkout but hasn't placed an order after a few hours. The **Started Checkout** event contains all the information about someone's cart, so you can show the products in their cart as well as images of those products. For more advanced users, you can set up two abandoned cart flows -- one for first-time customers that includes a discount code, and one for repeat purchasers that doesn't include a discount code. You can filter and target **Started Checkout** events based on the following criteria:

- ****IsDiscounted****If an order had a discount applied, e.g., **true**or **false**.
- ****ItemNames****The names of the items purchased in this event.

### Customer data

In addition to the metrics Klaviyo syncs from Spree, there are also customer properties that are added to each Klaviyo profile. You can use these properties in segments and flows. Here are the properties that are automatically synched from Spree:

- Email
- First Name
- Last Name
- City
- State/Region
- Zip Code
- Country
- Phone Number

## Outcome

You've now integrated your Klaviyo account with Spree, installed onsite tracking, and reviewed your synced data.

## Additional resources

- [How often integrations sync reference](https://klaviyo.zendesk.com/hc/en-us/articles/115005253208)
- Need more help integrating with Klaviyo? Check out [Klaviyo's Agency Partners](https://klaviyo.partnerpage.io/?utm_source=helpcenter&utm_medium=integrations)
