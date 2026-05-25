---
id: "115001396711"
title: "How to manually create an \"Added to Cart\" event for Shopify"
source_url: "https://help.klaviyo.com/hc/en-us/articles/115001396711-How-to-manually-create-an-Added-to-Cart-event-for-Shopify"
section: "Shopify best practices"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-05-11T11:00:04Z"
language: "en"
---
## You will learn

Learn how to manually create an **Added to Cart** event for Shopify to track when a customer adds an item to their cart, which you can use to trigger an abandoned cart flow.

Klaviyo now offers an **Added to Cart** event that [syncs automatically through our Shopify integration when enabled](https://help.klaviyo.com/hc/en-us/articles/4425956184731) and is Shopify-branded. We recommend using the branded event, since it is actively maintained by Klaviyo. If you prefer not to use our automatic event, this article details how to manually create the event using a code snippet, which will sync to Klaviyo with a gear icon.

**Added to Cart** differs from Klaviyo’s **Checkout Started** event. **Checkout Started** triggers after a customer adds item(s) to their cart, enters their email during the checkout process, and continues to checkout. This happens further down the funnel, whereas **Added to Cart** triggers as soon as a customer adds an item to their cart.

## Before you begin

- Read our article [Getting started with Shopify](https://help.klaviyo.com/hc/en-us/articles/115005080407-How-to-Integrate-with-Shopify) for step-by-step instructions on integrating before continuing with this article.
- Make sure you already have [Klaviyo onsite tracking enabled](https://help.klaviyo.com/hc/en-us/articles/4425956184731) (including Viewed Product tracking) in order for the Added to Cart event to function properly.
- Please note that the Added to Cart event only tracks users [previously cookied by Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115005076767-Guide-to-Klaviyo-Onsite-Tracking#who-klaviyo-tracks5).

Based on your Customer Privacy settings in Shopify, Klaviyo may not track onsite events for visitors to your Shopify store in the EU, EEA, UK and Switzerland, unless they have provided consent.

## Create the “Added to Cart” event

There are 3 steps to creating the **Added to Cart** event:

1. Choose where to place the code snippet
2. Add the snippet to your store
3. Test the code snippet

## Where should I paste the snippet?

Make sure to paste the snippet in both your default product page, and in any other product pages you may have.

### If your store has custom liquid blocks, you should use one for the snippet

1. In Shopify, navigate to ****Online Store > Themes****.
2. Find your theme and click ****Customize****.
3. At the top of the page, click the ****Home page**** dropdown.
4. Select ****Products > Default product**** to be brought to your default product page.
5. Click ****Add section**** in the left sidebar and then select ****Custom Liquid****.
6. Paste the provided snippet in the box.
7. Click ****Save**** in the upper right.
8. In the left sidebar, your new Custom Liquid block for **Added to Cart** should automatically appear below the other sections on the page.
   - If your **Added to Cart** block needs to be moved, hover over the block and click the 6 dots to drag it below your other sections


     ![Shopify product page section hierarchy with two custom liquid sections, one showing six gray dots, below other product sections](https://fast.wistia.com/embed/medias/3up33yx3rq/swatch)

### If your store does not have custom liquid blocks, you should place the snippet in your theme.liquid file

1. In Shopify, navigate to ****Online Store > Themes****.
2. Find your theme and click ****Customize****.
3. Click the three dots at the top and select ****Edit code****.
4. Open the ****theme.liquid**** file.
5. Paste the provided snippet after all other code, before the closing `</body>` tag.
   ![Theme.liquid file in Shopify showing text reading Add snippet here highlighted in blue, followed by </body](https://klaviyo.zendesk.com/hc/article_attachments/28711660840475)
6. Above the snippet, add the following opening tag: `{% if product %}`
   ![Theme.liquid file in Shopify showing if product tag highlighted in blue, followed by text reading Add snippet here, followed by </body>](https://klaviyo.zendesk.com/hc/article_attachments/28711660843675)
7. Directly after the snippet, add the following closing tag: `{% endif %}`
8. Your file should look like this:
   ![Theme.liquid file in Shopify showing if product and endif tags surrounding text reading Add snippet here, followed by </body>](https://klaviyo.zendesk.com/hc/article_attachments/28711660847003)
9. Click ****Save****.

## Add the snippet to your site

The following **Added to Cart** snippet should work for most Shopify stores.

Every Shopify store is different. If you try the snippet below, test it, and it doesn't work, you can always try a backup snippet provided under the "Having trouble?" dropdown below.

Add the snippet below to your Shopify store in the location you determined above.

```
<script>
  window.addEventListener('load', function() {
  var _learnq = window._learnq || [];
  function addedToCart() {
   fetch(`${window.location.origin}/cart.js`)
   .then(res => res.clone().json().then(data => {
    var cart = {
      total_price: data.total_price/100,
      $value: data.total_price/100,
      total_discount: data.total_discount,
      original_total_price: data.original_total_price/100,
      items: data.items
    }
    if (item !== 'undefined') {
      cart = Object.assign(cart, item)
    }
    if (klAjax) {
       _learnq.push(['track', 'Added to Cart', cart]);
       klAjax = false;
      }
   }))
  };
  (function (ns, fetch) {
    ns.fetch = function() {
      const response = fetch.apply(this, arguments);
      response.then(res => {
        if (`${window.location.origin}/cart/add.js`
          .includes(res.url) && res.url !== '') {
              addedToCart()
        }
      });
      return response
     }
  }(window, window.fetch));
  var klAjax = true;
  var atcButtons = document.querySelectorAll("form[action*='/cart/add'] button[type='submit']");
  for (var i = 0; i < atcButtons.length; i++) {
    atcButtons[i].addEventListener("click", function() {
      if (klAjax) {
        _learnq.push(['track', 'Added to Cart', item]);
        klAjax = false;
      }
    })
  }
  });
</script>
```

When you're done, test the event using the directions in the next section.

## Test your "Added to Cart" event

It's important to note that Klaviyo only tracks "known browsers," or those who've been cookied (via clicking through an email, filling out a form, etc). For this reason, **Added to Cart** events may not start showing up in your account as quickly as you expect. To learn more about more about who Klaviyo tracks, head to our [article about onsite tracking](https://help.klaviyo.com/hc/en-us/articles/115005076767-Getting-started-with-Klaviyo-onsite-tracking#who-klaviyo-tracks5).

In order to test your **Added to Cart** event, you'll need to manually cookie your email address. Follow these steps:

1. Navigate to your website.
2. On your homepage, add the following to the end of the URL, replacing **testing.email@gmail.com** with your email address:
   **?utm\_email=testing.email@gmail.com
   ![Shopify test store with ?utm_email=example@gmail.com appended to URL](https://klaviyo.zendesk.com/hc/article_attachments/28711673004699)**
3. Reload the page.
4. Navigate to a product page on your site and click your **Add to Cart** button.
5. Search in Klaviyo for your email address.
   ![Top corner of Klaviyo dashboard with testing.email@gmail.com in search bar](https://klaviyo.zendesk.com/hc/article_attachments/28711673006235)

You should see that a Klaviyo profile has been created for you (if one didn't exist already) and that this **Added to Cart** event has been tracked on your activity feed.

## Having trouble tracking Added to Cart with the given snippet?

If you are having trouble tracking **Added to Cart** with the given snippet, you can try the 2 additional snippets below, which we'll refer to as **Snippet 2** and **Snippet 3**. Before testing a new snippet, make sure to first remove the one that didn't work.

### Determine which backup snippet to try

Does your store use a button ID to define the **Add to Cart** button? If the answer is yes, ‌try Snippet 2. If your **Add to Cart** button is instead defined by class notation, you should use Snippet 3. Here's how to find out if your store uses a button ID or class notation:

1. 1. Open up one of your site’s product pages.
   2. Right-click the "Add to Cart" button, and select ****Inspect****.
   3. The console will open, showing the source code of your "Add to Cart" button in the console’s **Elements** tab.
   4. In the **Elements** tab, your code may look something like this:
      ![Product page with coffee bag on left and console open to Elements tab, with inspect element pop up above Add to Cart and button code highlighted in console](https://klaviyo.zendesk.com/hc/article_attachments/28711672966299)
   5. Notice that this "Add to Cart" button does not have a button ID (which would include something like `id = "button_ID_name"`); instead, it is referenced by a class notation (`class= "btn product-form_cart-submit
      btn–secondary-accent"`).

### Snippet 2

If your **Add to Cart** button is defined by a button ID, add the snippet below to your Shopify store in the location you determined in the "Where should I place the snippet?" section, along with any needed tags.

```
<script type="text/javascript">
var _learnq = _learnq || [];
	document.getElementById("AddToCart").addEventListener('click',function (){
 		_learnq.push(['track', 'Added to Cart', item]);
	});
</script>
```

This snippet will likely need to be modified, because the **Add to Cart** variable in the snippet needs to match the button ID used on your site.

The **Add to Cart** variable, whose default name is `AddToCart`, is highlighted within the snippet below:
![Klaviyo's Added to Cart snippet with Add to Cart button ID highlighted in yellow](https://klaviyo.zendesk.com/hc/article_attachments/28711672969115)

Checking the ID of the button requires the same steps as checking for the presence of a button ID on your site:

1. Open up one of your site’s product pages.
2. Right-click your "Add to Cart" button and select ****Inspect****.
3. The console will open, showing the source code of your "Add to Cart" button. The following image shows the ID of the "Add to Cart" button highlighted in the console.
   ![Add to cart button code in console with ID equals addToCart-product-template](https://klaviyo.zendesk.com/hc/article_attachments/28711672971931)
   The ID of the button on the page shown here (`addToCart-product-template`) is different from the variable in the default snippet (`AddToCart`).
4. If they don’t match, modify the snippet to match the ID of your button. Our example’s modified snippet looks like this:
   ![Klaviyo's add to cart snippet defined by button ID with add to cart variable modified to be addToCart-product-template](https://klaviyo.zendesk.com/hc/article_attachments/28711672975003)

### Snippet 3

If your **Add to Cart** button is defined by class notation, add the snippet below to your Shopify store in the location that you determined in the "Where should I place the snippet?" section, along with any needed tags.

```
<script type="text/javascript">
var _learnq = _learnq || [];
  var classname = document.getElementsByClassName("add-to-cart");
var addToCart = function() {
_learnq.push(['track', 'Added to Cart', item]);
}; for (var i = 0; i < classname.length; i++) {
classname[i].addEventListener('click', addToCart, false);
}
</script>
```

This snippet will likely need to be modified, because the **Add to Cart** variable in the snippet needs to match the class used on your site.

1. Open up one of your site’s product pages.
2. Right-click your "Add to Cart" button and select ****Inspect****.
3. The console will open, showing the source code of your "Add to Cart" button. The following image shows the class of the "Add to Cart" button highlighted in the console.
   ![Add to cart button code in console with class equals btn product-form_cart-submit btn--secondary-accent highlighted in yellow](https://klaviyo.zendesk.com/hc/article_attachments/28711672981275)
4. Compare your button code in between the quotations, highlighted in the above example, with the contents in between the parentheses after `getElementsByClassName` in the code snippet above. For example, the class listed in the screenshot is `btn product-form_cart-submit btn--secondary-accent` and the variable listed in the snippet is `add-to-cart`.
5. If they don’t match, modify the snippet to match the class of your button. Our example’s modified snippet looks like this:
   ![Klaviyo's alternate Added to Cart snippet with classname value btn product-form_cart-submit btn--secondary-accent](https://klaviyo.zendesk.com/hc/article_attachments/28711660835739)

If you are encountering problems tracking **Added to Cart** after trying these different options, it could be due to an issue with identifying the **Added to Cart** button. In this case, [please contact Klaviyo support.](https://help.klaviyo.com/hc/en-us/articles/115001002272-How-to-Contact-Support)

## Next step: Enable the abandoned “Added to Cart” flow

The default Klaviyo abandoned cart flow is triggered by the **Checkout Started** event, whereas the **Added to Cart** abandoned cart flow targets more casual shoppers who have yet to start checkout.

To enable this flow, we recommend using the pre-built flow available in Klaviyo's flow library:

1. Navigate to Klaviyo’s [flow library](https://www.klaviyo.com/library/flows).
2. Click into the "Prevent lost sales" goal section.
3. Select an ****Added to Cart Trigger, Abandoned Cart Reminder**** flow. There are two options: email only, or email and SMS.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28711673008667)
4. If you created the **Added to Cart** event, this flow will be ready to go with all the recommended filters and dynamic email content ready to power personalized cart followup messaging.

## Are you using Amazon Buy with Prime?

If you're using Buy with Prime to power payment and fulfillment for any of the products on your store, you should:

- [Integrate Buy with Prime with Klaviyo](https://help.klaviyo.com/hc/en-us/articles/14708088221467) to bring Buy with Prime data into your Klaviyo account.
- For your abandoned "Added to Cart" flow, add the following flow filters to exclude customers who started checkouts or made purchases via Buy with Prime from receiving incorrect messaging:
  - **Started Checkout** (Buy with Prime) **zero times since starting this flow** AND
  - **Placed Order** (Buy with Prime) **zero times since starting this flow.**

## Outcome

You have now created and tested a Shopify **Added to Cart** event, and enabled an abandoned **Added to Cart** flow.

## Additional resources

- [Getting started with the abandoned cart flow](https://help.klaviyo.com/hc/en-us/articles/115002779411-Guide-to-Creating-an-Abandoned-Cart-Flow)
- [Shopify data reference](https://help.klaviyo.com/hc/en-us/articles/115005080447-Reviewing-Your-Shopify-Data)
- [Troubleshooting your Shopify integration](https://help.klaviyo.com/hc/en-us/articles/4403927899291-Troubleshooting-Your-Shopify-Integration)