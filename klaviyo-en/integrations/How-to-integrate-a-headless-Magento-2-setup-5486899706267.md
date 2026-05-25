---
id: "5486899706267"
title: "How to integrate a headless Magento 2 setup"
source_url: "https://help.klaviyo.com/hc/en-us/articles/5486899706267-How-to-integrate-a-headless-Magento-2-setup"
section: "Magento 2"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:55:03Z"
language: "en"
---
## You will learn

Learn about how to integrate Klaviyo with a headless Magento 2 setup. If you are using Magento 2 to power your ecommerce store’s backend, but a different framework for the frontend (such as React.js, Angular, etc.), then the following information is relevant for you.

This integration requires 3 steps:

1. Connect your Magento 2 store via Klaviyo’s native integration to sync order, catalog, and subscriber data.
2. Manually add code snippets to your site to enable onsite tracking functionality.
3. (If you are using a custom URL structure for your product catalog) Add rewrite rules for product URLS.

## Connect Klaviyo's native integration

First, connect your Magento 2 store via Klaviyo’s native integration to sync order, catalog, and subscriber data by [following the steps in Getting started with Magento 2](https://help.klaviyo.com/hc/en-us/articles/115005254348).

A large part of Klaviyo’s Magento 2 integration relies on fetching data via Magento's server side API. Typically, this isn’t affected by using a decoupled frontend, and the native integration will track the following events without further setup:

- Placed Order
- Fulfilled Order
- Fulfilled Shipment
- Canceled Order
- Refunded Order
- Started Checkout

  Additionally, please note that:
- **Started Checkout** events will sync provided you are still creating quotes and assigning an email address to them when the user checks out.
- If you’ve enabled syncing customers subscribed to the Magento 2 newsletter table, the sync should work as anticipated.

## Manually add code snippets

If you are using a headless setup, you must manually add Klaviyo’s “Active on Site” JavaScript (also known as **Klaviyo.js**) to your site. Klaviyo.js tracks when users are active on your site and enables Klaviyo forms.

We also provide snippets that allow you to do the following:

- ****Viewed Product tracking****
  Track when a user views specific products on your site (which can be leveraged in a [browse abandonment flow](https://help.klaviyo.com/hc/en-us/articles/115002775252-Create-a-Browse-Abandonment-Flow)).
- ****Recently Viewed Items tracking****
  Track recently viewed items on a user's profile.
- ****Added to Cart tracking****
  Track when a user adds an item to their cart.
- ****Logged in User tracking****
  If you have account creation functionality, track when a user logs in.

### Active on Site

Add the following Klaviyo.js snippet so that it appears on every page on your website. This will enable **Active on Site** tracking and Klaviyo forms. Make sure to replace PUBLIC\_API\_KEY with your [Klaviyo public API key](https://help.klaviyo.com/hc/en-us/articles/115005062267-How-to-Manage-Your-Account-s-API-Keys).

```
<script type="text/javascript" async="" src="https://static.klaviyo.com/onsite/js/PUBLIC_API_KEY/klaviyo.js"></script>
```

After adding Klaviyo.js, you'll need to load the [Klaviyo object](https://developers.klaviyo.com/en/docs/introduction_to_the_klaviyo_object) on any page where you want to add one of the following snippets (such as **Viewed Product**, **Added to Cart**, etc). The**klaviyo**object only needs to be loaded once per page.

To load the **klaviyo** object, manually install the following snippet on the necessary pages:

```
<script type="text/javascript"> !function(){if(!window.klaviyo){window._klOnsite=window._klOnsite||[];try{window.klaviyo=new Proxy({},{get:function(n,i){return"push"===i?function(){var n;(n=window._klOnsite).push.apply(n,arguments)}:function(){for(var n=arguments.length,o=new Array(n),w=0;w<n;w++)o[w]=arguments[w];var t="function"==typeof o[o.length-1]?o.pop():void 0,e=new Promise((function(n){window._klOnsite.push([i].concat(o,[function(i){t&&t(i),n(i)}]))}));return e}}})}catch(n){window.klaviyo=window.klaviyo||[],window.klaviyo.push=function(){var n;(n=window._klOnsite).push.apply(n,arguments)}}}}(); </script>
```

### Viewed Product

If you'd like to set up a [browse abandonment flow](https://help.klaviyo.com/hc/en-us/articles/115002775252-Create-a-Browse-Abandonment-Flow) or build segments based on product browsing activity, you'll need to add JavaScript event tracking for the **Viewed Product** metric. All **Viewed Product** metrics are tied to user profiles. On your product page template, add the following snippet.

```
<script type="text/javascript">
var klaviyo = window.klaviyo || [];
var item = {
     "ProductName": item.ProductName,
     "ProductID": item.ProductID,
     "SKU": item.SKU,
     "Categories": item.Categories,
     "ImageURL": item.ImageURL,
     "URL": item.URL,
     "Brand": item.Brand,
     "Price": item.Price,
     "CompareAtPrice": item.CompareAtPrice
 };
 klaviyo.track("Viewed Product", item);
 </script>
```

Make sure to update the values of the JSON properties in the snippet so that they dynamically pull from the relevant information needed for that property.

### Recent Viewed Items

Additionally, there is another snippet that allows entries to be added to a visual “Recently Viewed Items” feed on the user’s profile. The following snippet can be added directly below the **Viewed Product** snippet.

Make sure to replace item.\_\_\_ in the snippet with whatever item object your platform uses for product properties.

```
<script type="text/javascript">
var klaviyo = window.klaviyo || [];
klaviyo.trackViewedItem({
     "Title": item.ProductName,
     "ItemId": item.ProductID,
     "Categories": item.Categories,
     "ImageUrl": item.ImageURL,
     "Url": item.URL,
     "Metadata": {
       "Brand": item.Brand,
       "Price": item.Price,
       "CompareAtPrice": item.CompareAtPrice
     }
   });
 </script>
```

### Added to Cart

If you’d like to send abandoned cart emails to visitors who add items to their cart, but don’t make it to the checkout page, you’ll want to track an **Added to Cart** metric. A customer must be identified (i.e., cookied) to track this event. Here's an example request where the cart already contained one item (Winnie the Pooh) and another item was just added to the cart (A Tale of Two Cities):

```
<script type="text/javascript">
klaviyo.track("Added to Cart", {
     "$value": 29.98,
     "AddedItemProductName": "A Tale of Two Cities",
     "AddedItemProductID": "1112",
     "AddedItemSKU": "TALEOFTWO",
     "AddedItemCategories": ["Fiction", "Classics", "Children"],
     "AddedItemImageURL": "http://www.example.com/path/to/product/image2.png",
     "AddedItemURL": "http://www.example.com/path/to/product2",
     "AddedItemPrice": 19.99,
     "AddedItemQuantity": 1,
     "ItemNames": ["Winnie the Pooh", "A Tale of Two Cities"],
     "CheckoutURL": "http://www.example.com/path/to/checkout",
     "Items": [{
         "ProductID": "1111",
         "SKU": "WINNIEPOOH",
         "ProductName": "Winnie the Pooh",
         "Quantity": 1,
         "ItemPrice": 9.99,
         "RowTotal": 9.99,
         "ProductURL": "http://www.example.com/path/to/product",
         "ImageURL": "http://www.example.com/path/to/product/image.png",
         "ProductCategories": ["Fiction", "Children"]
       },
       {
         "ProductID": "1112",
         "SKU": "TALEOFTWO",
         "ProductName": "A Tale of Two Cities",
         "Quantity": 1,
         "ItemPrice": 19.99,
         "RowTotal": 19.99,
         "ProductURL": "http://www.example.com/path/to/product2",
         "ImageURL": "http://www.example.com/path/to/product/image2.png",
         "ProductCategories": ["Fiction", "Classics"]
       }
     ]
   });
 </script>
```

### Logged in users

If customers can create accounts on your website, you may want to add additional code to identify and track logged-in users. This code should be executed once the user has logged in.

Here is an example script to get you started:

```
klaviyo.identify({
  "$email" : customer.email,
  "$first_name" : customer.first_name,
  "$last_name" : customer.last_name
});
```

## Add rewrite rules for product URLs

Your Magento 2 product catalog should sync normally with Klaviyo via our native integration, though if you are using a custom URL structure you will need to add some rewrite rules to your codebase.

The default Magento 2 product URL follows the below structure:

```
https://[YOUR STORE]/catalog/product/view/id/[PRODUCT ID]
```

If your store is using a URL structure like:

```
https://[YOUR STORE]/products/[Product Name]
```

Then you will need to add some rewrite rules to your codebase to redirect the standard Magento 2 product links to your custom URL structure