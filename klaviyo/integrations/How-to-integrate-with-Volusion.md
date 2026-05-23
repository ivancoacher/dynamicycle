---
id: 115005083427
title: "How to integrate with Volusion"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005083427-How-to-integrate-with-Volusion"
section: "Volusion"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:56:39Z"
language: en
---

## You will learn

Learn how to integrate Volusion with Klaviyo. After completing these steps, you'll be able to personalize and target emails based on synced order data and customer properties.

From Volusion, Klaviyo tracks **Ordered Product**and**Placed Order**metrics; with the addition of some extra code we can track**Abandoned Cart**information as well.

## Before you begin

Volusion requires an [update to your Volusion store's administrator account password every 90 days](http://helpcenter.volusion.com/extend-your-site/more-integrations/the-volusion-api). When making this update your Volusion account, you must also make this update to your Volusion integration in your Klaviyo account. You can also create a permanent API Key by following the steps in the corresponding section of this article.

## Add the Volusion integration in Klaviyo

1. In Klaviyo, select the ****Integrations**** tab.
2. Select ****Explore apps****.
3. Search for **Volusion** and click the card, then click ****Install****.
4. On the next page, enter your Store URL, login email, and API key/encrypted password. Then, click ****Connect to Volusion****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28711662648859)
5. On the next page, you will see a checkbox for **Add new Volusion customers to a Klaviyo list******.****If you check this box, you can pick one of your lists in Klaviyo to which future customers will be added when they place an order.
6. Finally, click ****Complete setup****.

## Disable email to web tracking in Klaviyo

1. The "email to web tracking" feature in Klaviyo uses click tracking to identify a user who arrives at your website through a Klaviyo email before we would originally be able to identify them (such as when they make a purchase or subscribe to your email list).
2. Volusion does not support the URL format that our click tracking uses and produces an error when a user tries to visit your store through one of these links, so this feature will have to be disabled in Klaviyo to make sure links in your email follow through to your Volusion store correctly.
3. You can disable this tracking in your account settings under ****Account name > Settings > Email > Attribution****.
4. The only functionality lost with disabling this feature is the ability to track a new profile on your website through an email they clicked. As long as you have the Klaviyo onsite tracking analytics on your website (which we'll add in the next section), we will still be able to track users as soon as we get their email address through either a purchase in your store or when they sign up for an email list.

## Add onsite tracking to your Volusion store

Klaviyo provides two onsite tracking snippets to help you collect valuable information about your customers:

- ****Active on Site****This snippet tracks when your customers visit your site. This snippet must be added to the site in order for other snippets such as **Viewed Product** to work.
- ****Viewed Product****This snippet tracks when your customers view specific products. You can track this event by adding the **Viewed Product** code snippet to your store.

### Add Active on Site tracking

Add the following Klaviyo.js snippet so that it appears on every page on your website. This will enable **Active on Site** tracking and Klaviyo forms. Make sure to replace PUBLIC\_API\_KEY with your [Klaviyo public API key](https://help.klaviyo.com/hc/en-us/articles/115005062267-How-to-Manage-Your-Account-s-API-Keys).

```
<script type="application/javascript" async="" src="https://static.klaviyo.com/onsite/js/PUBLIC_API_KEY/klaviyo.js"></script>
<script type="text/javascript">
//Script to initialize Klaviyo object on page load
!function(){if(!window.klaviyo){window._klOnsite=window._klOnsite||[];try{window.klaviyo=new Proxy({},{get:function(n,i){return"push"===i?function(){var n;(n=window._klOnsite).push.apply(n,arguments)}:function(){for(var n=arguments.length,o=new Array(n),w=0;w<n;w++)o[w]=arguments[w];var t="function"==typeof o[o.length-1]?o.pop():void 0,e=new Promise((function(n){window._klOnsite.push([i].concat(o,[function(i){t&&t(i),n(i)}]))}));return e}}})}catch(n){window.klaviyo=window.klaviyo||[],window.klaviyo.push=function(){var n;(n=window._klOnsite).push.apply(n,arguments)}}}}(); </script>
```

### Add Viewed Product tracking

To enable **Viewed Product** tracking, you will need to add the snippet of code below to your store's template page in Volusion's File Editor, which you can find by clicking ****Design > File Editor****.

```
<script type="text/javascript">
// Check to see if the customer is on the product page before executing code.
    if ($("meta[property='og:type']").attr("content") == "product") {
        var klaviyo = window.klaviyo || [];
        // Function to track when a product is viewed
        var trackViewedProduct = function(item) {
            klaviyo.track("Viewed Product", item);
            klaviyo.trackViewedItem({
                "Title": item.ProductName,
                "ItemId": item.ProductID,
                "ImageUrl": item.ImageURL,
                "Url": item.URL,
                "Metadata": {
                    "Price": item.Price,
                    "Description": item.Description,
                    "CompareAtPrice": item.CompareAtPrice,
                    "YouSave": item.YouSave
                }
            });
        };
        var item = {}
        $.get(`/ProductDetails.asp?ProductCode=${global_Current_ProductCode}`, function(data) {
            var product_saleprice = $("table.colors_pricebox div.product_saleprice").length ?
                Number(`${$("table.colors_pricebox div.product_saleprice").text().trim().split("$")[1].split(".")[0]}.${$("table.colors_pricebox div.product_saleprice").text().trim().split("$")[1].split(".")[1].substring(0,2)}`) : null;
            var product_listprice = $("table.colors_pricebox div.product_listprice").length ?
                Number(`${$("table.colors_pricebox div.product_listprice").text().trim().split("$")[1].split(".")[0]}.${$("table.colors_pricebox div.product_listprice").text().trim().split("$")[1].split(".")[1].substring(0,2)}`) : null;
            var product_productprice = $("table.colors_pricebox div.product_productprice").length ?
                Number(`${$("table.colors_pricebox div.product_productprice").text().trim().split("$")[1].split(".")[0]}.${$("table.colors_pricebox div.product_productprice").text().trim().split("$")[1].split(".")[1].substring(0,2)}`) : null;
            var product_yousave = $("table.colors_pricebox div.product_yousave").length ?
                Number(`${$("table.colors_pricebox div.product_yousave").text().trim().split("$")[1].split(".")[0]}.${$("table.colors_pricebox div.product_yousave").text().trim().split("$")[1].split(".")[1].substring(0,2)}`) : 0;
            item = {
                "ProductName": $("meta[property='og:title']").attr("content"),
                "ProductID": global_Current_ProductCode,
                "Description": $("meta[property='og:description']").attr("content"),
                "ImageURL": $("meta[property='og:image']").attr("content"),
                "URL": $("meta[property='og:url']").attr("content"),
                "Price": product_saleprice ? product_saleprice : product_productprice,
                "CompareAtPrice": product_listprice ? product_listprice : product_productprice,
                "YouSave": product_yousave
            };
            trackViewedProduct(item);
        });
    }
</script>
```

### Add abandoned cart reminders

Volusion does not provide an out-of-the-box way to track abandoned carts through our integration, but we have created a custom script you can add to your Volusion store which will allow you to use this feature in Klaviyo. This will require some knowledge of adding code to your shop's template so if you have a developer, you can send them this doc to walk through adding the code.

The abandoned cart feature will only work for Volusion stores using the one page checkout feature, and stores that do not require a user to have an account before making a purchase.

1. You will need to add the snippet of code below to your store's template page in Volusion's File Editor, which you can find by clicking ****Design > File Editor****.

   ```
   <script type="text/javascript">
       // Check to see if the customer is on the checkout page before executing code.
       if (window.location.pathname == "/one-page-checkout.asp") {
           var klaviyo = window.klaviyo || [];
           // Function to track when a checkout is started.
           var trackStartedCheckout = function() {
               $.post('/AjaxCart.asp', function(data) {
                   if (!data || !data.Products || !data.Products.length) {
                       return;
                   }
                   var items = [],
                       names = [],
                       skus = [];
                   // Grab each product and its SKU/Name/Quantity/Price/Total price/Image url
                   $.each(data.Products, function(i, record) {
                       var item_price = +(record.ProductPrice.replace(/[\$,]+/g, '')) / record.Quantity;
                       items.push({
                           SKU: record.ProductCode,
                           Name: record.ProductName,
                           Quantity: +record.Quantity,
                           ItemPrice: item_price,
                           RowTotal: item_price * record.Quantity,
                           ImageURL: record.ImageSource
                       });
                       names.push(record.ProductName);
                       skus.push(record.ProductCode);
                   });
                   // Push Started Checkout metric to Klaviyo with the customers data.
                   klaviyo.track("Started Checkout", {
                       $value: +(data.Totals[0].CartTotal.replace(/[\$,]+/g, "")),
                       Items: items,
                       ProductNames: names,
                       SKUs: skus
                   });
               }, 'json');
           };
           $(function() {
               // Grab the email form to get your customers email and tie the event to that email in Klaviyo.
               $('[name="OnePageCheckoutForm"] [name="Email"]').change(function(e) {
                   var email = $(this).val();
                   // Do some light validation. Klaviyo will do more validation when the data is received.
                   if (email && /@/.test(email)) {
                       klaviyo.identify({
                           $email: email
                       });
                       trackStartedCheckout();
                   }
               });
           });
   }
   </script>
   ```
2. This code will only be able to track checkout events going forward; you will not be able to back-populate abandoned cart flows inside Klaviyo.
3. After saving this code to your store, Klaviyo will automatically begin tracking a **Started Checkout** metric from which you can trigger an abandoned cart flow.

## Monitor the Klaviyo sync

1. Once integrated with Volusion, Klaviyo will need time to sync your data before it is ready to be used. You can check the status of this sync by navigating back to the ****Integrations****tab and looking for your Volusion integration on the list of **Enabled Integrations**.
2. If there is a gray outline, this means the integration is still syncing. The bigger your store, the longer a sync can take. When your integration is shown with a green border, you're ready to go.
3. Klaviyo imports all of your historic Volusion data when you first enable the integration. To verify this, you can compare the number of orders on a particular day with what's in the Volusion interface and confirm they match. For example, when exploring the **Placed Order** metric (under ****Analytics > Metrics**** in Klaviyo) you can mouse over yesterday's data point or look at the table of data below the chart to see how many orders were reported yesterday.
4. Compare that number to what's stored in Volusion from yesterday and you should see they match exactly. If they don't, the issue is most likely that your Klaviyo account's timezone doesn't match your Volusion timezone.
5. To check or update your account's timezone:
   - Click your account name in the lower left.
   - Select then clicking ****Settings**** ****> Organization****.
   - Scroll down to **Timezone**.

## Data synced from Volusion

Navigate to ****Analytics > Metrics**** to find all of the metrics in your account. The metrics with a Volusion icon are synced from your Volusion integration. Metrics and profile properties from Volusion are synced within the hour of someone placing an order.
![Metrics tab in Klaviyo filtered by Volusion showing metrics Placed Order and Ordered Product](https://klaviyo.zendesk.com/hc/article_attachments/28711674775067)

### Placed Order

This event is tracked when a customer completes the checkout process and creates an order in your Volusion store. The **Placed Order** event includes all relevant information about the items someone purchased including product names, product codes, images, and price information so you can use that information in purchase follow up emails.

### Ordered Product

This event is also tracked when a customer places an order, but one event is tracked for each item in the order. For example, if someone buys a t-shirt and a pair of pants, one **Placed Order** event is tracked and two **Ordered Product** events - one event for the t-shirt and one event for the pants.

The **Ordered Product** event includes detailed information about each product purchased. This is useful when creating behavioral segments based on product variant options and other detailed information that's not available in the **Placed Order** event. You can filter and target **Ordered Product** events based on the following criteria:

- ****Name****The name or title of the product in Volusion, e.g., **t-shirt**.
- ****Product Code****The product code for your product inside of Volusion.
- ****Quantity****The quantity of the item purchased in an order.

### Customer data synced from Volusion

In addition to the above metrics Klaviyo syncs from Volusion, there are also customer properties that are added to each Klaviyo profile. You can use these properties in segments and flows. Here are the properties that are automatically synched from Volusion:

- Email
- First Name
- Last Name
- City
- State/Region
- Zip Code
- Country
- Phone Number
- Source (Klaviyo will track customers from Volusion with a Source property on their profile set to "Volusion")

## Troubleshooting

### Volusion Placed Order data isn’t reporting in Klaviyo

This may be an issue with your Volusion API settings that allow data to be exported.

1. To fix this, navigate to the **Inventory** tab of your Volusion admin panel. Select **Import/Export**from the dropdown menu.
   ![Inventory dropdown in Volusion with Import/Export in blue](https://klaviyo.zendesk.com/hc/article_attachments/28711662634139)
2. Click on **Volusion API** to access the main API page.
3. In the **Generic** section, you will find the option to ****Run**** the export of your store’s Generic/Orders. Once the export is run, the page will refresh.
   ![Import/Export page in Volusion with mouse over Run for Generic\Orders](https://klaviyo.zendesk.com/hc/article_attachments/28711662626331)
4. Select all columns by clicking the checkbox in the column named ****\***** and click ****Run****.
   ![Volusion API: Run Generic\Orders page with asterisk column checked](https://klaviyo.zendesk.com/hc/article_attachments/28711662644763)
5. After clicking **Run** to export your Generic Orders, an API URL is generated at the top of the page. For example, the URL would appear as: `https://storename.com/net/WebService.aspx?Login=user@storename.com&EncryptedPassword=ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789&EDI_Name=GenericOrder`.
   ![API key highlighted within link on page Volusion API: Run Generic\Orders](https://klaviyo.zendesk.com/hc/article_attachments/28711674788251)
6. The value that appears between "EncryptedPassword=" and "&EDI\_Name=GenericOrders" (highlighted in the screenshot above) serves as your API Key. Use this to re-establish your integration settings from the Integrations tab of your Klaviyo dashboard.
7. Upon completion, test by clicking into ****Analytics > Metrics****. View recent activity for the Volusion **Placed Order** metric to see if any new data has synced in Klaviyo. If you see new data for the **Placed Order** metric, [contact our Support team](https://klaviyo.zendesk.com/hc/en-us/articles/115001002272) to run a gap fill for missing orders in Klaviyo or for any further assistance.
8. For additional information on exporting data using the Volusion API, please refer to [Volusion support](https://support.volusion.com/hc/en-us/articles/208837888-Exports-Orders-Export-Developer-).

### People see an "Invalid Input" error when clicking my email links

The "email to web tracking" feature in Klaviyo uses click tracking to tie activity to a user who arrives at your website through a Klaviyo email before we would originally be able to identify them (such as when they make a purchase or subscribe to your email list).

Volusion does not support the URL format that our click tracking uses and produces an error when a user tries to visit your store through one of these links, so this feature will have to be disabled in Klaviyo to make sure links in your email follow through to your Volusion store correctly.

To fix this issue, make sure to disable email to web tracking in Klaviyo as described at the beginning of this article.

## How to create a permanent API key in Volusion

Normally Volusion will require you to reset your API key every 90 days when you reset the password on your account, causing you to need to re-configure your Voluision integration in Klaviyo. The following steps will allow you to create a non-expiring API key instead; it involved generating API credentials for an admin account you never log in to:

1. From your Volusion admin panel, go to ****Customers > Administrators**** and create a new administrator account.
2. Navigate to ****Inventory > Import/Export**** and select the ****Volusion API**** tab.
3. Under the Generic section, click the link for ****Volusion API Integration Help****.
4. Select ****Export**** and select the new admin you created from the dropdown.
5. Expand the "URL with Query String..." box to find your permanent URL, login, and encrypted password (API Key).

Do not log in with this account, it will be used for API access only. Logging in with this account will cause the password to expire after 90 days and you will need to redo these steps to generate a new permanent API key.

## Outcome

You've now integrated Klaviyo with Volusion, added onsite tracking, reviewed your synced data, and learned how to create a permanent API key.

## Additional resources

- [How often integrations sync reference](https://klaviyo.zendesk.com/hc/en-us/articles/115005253208)
- Need more help integrating with Klaviyo? Check out [Klaviyo's Agency Partners](https://klaviyo.partnerpage.io/?utm_source=helpcenter&utm_medium=integrations)