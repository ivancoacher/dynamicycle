<h1>How to create an &quot;Added to Cart&quot; event for BigCommerce</h1>

## You will learn

Learn how to create an **Added to Cart** event for BigCommerce that tracks when a customer adds an item to their cart and can trigger an abandoned cart flow. **Added to Cart** events do not automatically track when you integrate with BigCommerce; you must first add (and potentially modify) a JavaScript snippet (included in this guide) to your BigCommerce theme files.

- You do not need to create the **Added to Cart** event to send an abandoned cart flow; the **Added to Cart** abandoned cart flow is separate from the standard abandoned cart flow, which is triggered by **Started Checkout**.
- Klaviyo’s built-in BigCommerce integration already tracks a **Started Checkout** event when a customer enters their email during the checkout process after adding item(s) to their cart.

## Before you begin

The **Added to Cart** event is only tracked for users previously [cookied by Klaviyo](https://help.klaviyo.com/hc/en-us/articles/360034666712-About-Cookies-in-Klaviyo).

You must already have **Viewed Product** tracking installed in order for the **Added to Cart** event to function properly. Typically, Klaviyo customers install this during the BigCommerce integration process and the instructions can be found in our [integration article](https://help.klaviyo.com/hc/en-us/articles/115005082547-How-to-Integrate-with-BigCommerce#add-viewed-product-tracking4).

## Add the snippet

1. Open your BigCommerce admin and navigate to ****Storefront > My Themes****.
2. Find your current theme, and click the ****Advanced Settings**** dropdown.
3. Search for the ****product.html**** file and click to open it.
4. Paste the snippet below directly underneath the Klaviyo **Viewed Product** snippet.

   ```
   <script text="text/javascript">
   //Initialize Klaviyo object immediately on page load
   !function(){if(!window.klaviyo){window._klOnsite=window._klOnsite||[];try{window.klaviyo=new Proxy({},{get:function(n,i){return"push"===i?function(){var n;(n=window._klOnsite).push.apply(n,arguments)}:function(){for(var n=arguments.length,o=new Array(n),w=0;w<n;w++)o[w]=arguments[w];var t="function"==typeof o[o.length-1]?o.pop():void 0,e=new Promise((function(n){window._klOnsite.push([i].concat(o,[function(i){t&&t(i),n(i)}]))}));return e}}})}catch(n){window.klaviyo=window.klaviyo||[],window.klaviyo.push=function(){var n;(n=window._klOnsite).push.apply(n,arguments)}}}}(); </script>
   <script text="text/javascript">
   //Added to Cart
   var klaviyo = window.klaviyo || [];
   document.getElementById("form-action-addToCart").addEventListener('click',function (){
      klaviyo.track("Added to Cart", item);
   });
   </script>
   ```
5. Next, check if you need to modify your snippet. To do this, you’ll need to check the ID of the “Add to Cart” button on your site, and see if it matches the “Add to Cart” variable highlighted in the snippet below, whose default is `form-action-addToCart`.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28717387201051)
6. To check the ID of the button, open up one of your site’s product pages, right-click your “Add to Cart” button, and select ****Inspect****.
   ![BigCommerce store with demo item Smith Journal, right click menu open on Add to Cart button with Inspect highlighted in blue](https://klaviyo.zendesk.com/hc/article_attachments/28717387183515)
7. The console will open, showing the source code of the “Add to Cart” button. The following image shows the ID of the "Add to Cart" button highlighted in the console.
   ![BigCommerce store demo item with Chrome console open and add to cart button ID, form-action-addToCart, highlighted](https://klaviyo.zendesk.com/hc/article_attachments/28717387187867)
8. The ID of the button on the page shown here matches `form-action-addToCart`, so no changes need to be made.
   - If the ID of the “Add to Cart” button on your site isn’t `form-action-addToCart`, you’ll need to change the variable text within the quotes to match the button’s ID
9. If your source code isn’t showing a button ID, skip ahead to the [next section](https://help.klaviyo.com/hc/en-us/articles/360024310292#alternate-snippet-for--add-to-cart--button-without-a-button-id3) and learn how to use an alternate snippet with class notation instead of button notation.
10. When you’re done, save your ****product.html**** file.

You’ve finished adding the snippet and will now track the **Added to Cart** event.

## Alternate snippet for "Add to Cart" button without a button ID

For styling reasons, some sites use a class notation instead of a button ID for “Add to Cart” buttons.

If your “Add to Cart**”** button does not have a button ID (which you can determine by following the steps in the previous section) and instead uses a class notation, you should use the alternate code snippet below to enable the **Added to Cart** event.

1. If your button is defined by class notation, paste the following alternate snippet at the bottom of your ****product.html**** file:

   ```
   <script text="text/javascript">
   //Initialize Klaviyo object immediately on page load
   !function(){if(!window.klaviyo){window._klOnsite=window._klOnsite||[];try{window.klaviyo=new Proxy({},{get:function(n,i){return"push"===i?function(){var n;(n=window._klOnsite).push.apply(n,arguments)}:function(){for(var n=arguments.length,o=new Array(n),w=0;w<n;w++)o[w]=arguments[w];var t="function"==typeof o[o.length-1]?o.pop():void 0,e=new Promise((function(n){window._klOnsite.push([i].concat(o,[function(i){t&&t(i),n(i)}]))}));return e}}})}catch(n){window.klaviyo=window.klaviyo||[],window.klaviyo.push=function(){var n;(n=window._klOnsite).push.apply(n,arguments)}}}}(); </script>
   <script text="text/javascript">
   //Viewed Product
   var klaviyo = window.klaviyo || [];
   var classname = document.getElementsByClassName("add-to-cart");
   var addToCart = function() {
      klaviyo.track("Added to Cart", item);
   };
   for (var i = 0; i < classname.length; i++) {
      classname[i].addEventListener('click', addToCart, false);
   }
   </script>
   ```
2. This code will likely need to be modified with your class name. Compare your button class name in between the quotations, highlighted in the following example, with the contents in between the parentheses after `getElementsByClassName` in the code snippet above. For example, the class name in the screenshot is `btn product-form_cart-submit btn--secondary-accent` and the class in the snippet is named `add-to-cart`.
   ![Add to cart button code in Chrome console with button class, btn product-form_cart-submit btn--secondary-accent, higlighted in yellow](https://klaviyo.zendesk.com/hc/article_attachments/28717387188891)
   - If these two don't match, change the code snippet to reflect the class name for your button.
3. For example, the code snippet below has been modified with the classname value `btn product-form_cart-submit btn--secondary-accent` surrounded by double quotations.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28717380936347)
4. Save your ****product.html**** file

Once you save, you’ve finished adding the snippet and can now track the **Added to Cart** event.

## Troubleshooting your "Added to Cart" snippet

After you’ve added the snippet, it should watch the "Add to Cart'' button and track an **Added to Cart** event whenever a cookied visitor clicks this button.

This event functions similarly to the **Viewed Product** event. Each item someone adds to their cart will trigger a new event. You can view these events by:

1. Navigating to ****Analytics > Metrics****in Klaviyo
2. Searching for the event
3. Clicking ****Activity Feed
   ![Added to cart metric activity feed in Klaviyo, list shows profile names that have recently added to cart](https://klaviyo.zendesk.com/hc/article_attachments/28717380926747)****

If you don’t see **Added to Cart** events in your account, try the following:

- Make sure your Klaviyo.js (also known as the Active on Site snippet) is working, which is necessary for **Added to Cart** to function properly. This should have been added to your site automatically when you integrated with Klaviyo, but you can check that it’s working by following the steps in the [confirming onsite tracking installation section of our BigCommerce integration article](https://help.klaviyo.com/hc/en-us/articles/115005082547-How-to-Integrate-with-BigCommerce#confirm-web-tracking-installation3).
- Check that your **Viewed Product** tracking is working, which is also necessary for **Added to Cart** to function properly. This snippet is added manually, and you can learn how to add and test it in the [Viewed Product section of our integration article](https://help.klaviyo.com/hc/en-us/articles/115005082547-How-to-Integrate-with-BigCommerce#add-viewed-product-tracking4).

If you are still encountering problems with your **Added to Cart** snippet, it could be due to an issue with identifying the “Add to Cart” button. In this case, [please contact Klaviyo support](https://help.klaviyo.com/hc/en-us/articles/115001002272-How-to-Contact-Support).

## The "Added to Cart" abandoned cart flow

When creating an abandoned cart flow (either using **Added to Cart** or **Started Checkout**) you can leverage Klaviyo SMS in addition to email. For compliance reasons, make sure to only send one SMS in your flow and if you are using multiple types of abandoned cart flows, make sure to only use SMS in one of them.

In the **Essentials** section of the library, you will find the standard abandoned cart reminder flow. This flow is triggered by the **Started Checkout** event.

![Card for standard abandoned cart reminder flow for BigCommerce in the Klaviyo flow library](https://klaviyo.zendesk.com/hc/article_attachments/28717380929051)

To get started with an abandoned cart flow using the **Added to Cart** event, we recommend using the pre-built flow available in Klaviyo's [Flow Library](https://www.klaviyo.com/library/flows) which has the proper flow filters already set up. This flow tends to target more casual potential shoppers who have yet to start checkout.

The abandoned cart flow triggered by the **Added to Cart** event can be found in the "Prevent lost sales" goal section.

![Card for added to cart abandoned cart reminder flow for BigCommerce in the Klaviyo flow library](https://klaviyo.zendesk.com/hc/article_attachments/28717380931483)

If you implemented the BigCommerce **Added to Cart** snippet, this flow will be ready to go with all the recommended filters and dynamic email content ready to power personalized cart followup emails.

## Are you using Amazon Buy with Prime?

If you're using Buy with Prime to power payment and fulfillment for any of the products on your store, you should:

- [Integrate Buy with Prime with Klaviyo](https://help.klaviyo.com/hc/en-us/articles/14708088221467) to bring Buy with Prime data into your Klaviyo account.
- For your abandoned "Added to Cart" flow, add the following flow filters to exclude customers who started checkouts or made purchases via Buy with Prime from receiving incorrect messaging:
  - **Started Checkout** (Buy with Prime) **zero times since starting this flow** AND
  - **Placed Order** (Buy with Prime) **zero times since starting this flow.**

## Additional resources

- [Creating an abandoned cart flow](https://help.klaviyo.com/hc/en-us/articles/115002779411-Guide-to-Creating-an-Abandoned-Cart-Flow)
- [BigCommerce data reference](https://help.klaviyo.com/hc/en-us/articles/115005082587-Reviewing-Your-BigCommerce-Data)
