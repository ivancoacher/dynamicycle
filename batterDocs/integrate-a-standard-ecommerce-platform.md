<h1>Integrate a Standard Ecommerce Platform</h1>

## Overview

If you've built your own custom cart solution, or the ecommerce data you would like to track in Klaviyo is not yet supported by one of our pre-built integrations, you can integrate with Klaviyo using our [JavaScript API](https://www.klaviyo.com/docs/getting-started), [server-side API](https://www.klaviyo.com/docs/http-api), and Custom Catalog integration.

The key components of integrating a custom ecommerce cart are:

- Customer data
- Subscribers
- Website activity
- Order activity

This guide focuses on how to sync important metrics, or key customer activities, to Klaviyo. While our JavaScript and server-side Track and Identify APIs can be used interchangeably, we recommend using the following setup for ecommerce businesses. Use this as a checklist when setting up your integration:

- Use our JavaScript Track APIfor the following:
  - ****Active on Site**** - When someone visits your website
  - ****Viewed Product**** - When someone views a product
  - ****Added to Cart**** - When someone adds an item to their cart
  - ****Started Checkout**** - When someone lands on the checkout page
- Use our server-side Track API for the following:
  - ****Placed Order**** - When an order successfully processes on your system
  - ****Ordered Product**** - An event for each item in a processed order
  - ****Fulfilled Order**** - When an order is sent to the customer
  - ****Cancelled Order**** - When a customer cancels their order
  - ****Refunded Order**** - When a customer’s order is refunded
- Use our Custom Catalog Feed integration for the following:
  - ****Catalog Feed**** - An XML feed or JSON feed of your product catalog

The level of detailed data you send to Klaviyo within these website, purchase, and checkout events will determine how you can filter and segment based on these events in Klaviyo. To understand how data must be structured so that key event details are available for segmentation, [check out our guide on segment conditions](https://help.klaviyo.com/hc/en-us/articles/115005062847-Understand-the-Data-Available-for-Segmentation).

Note that the snippets in this guide use example data. You will need to update the values of the JSON properties in these snippets such that they dynamically pull from the relevant information needed for that property.

Make sure to check out our [custom integration FAQ](https://help.klaviyo.com/hc/en-us/articles/360031078492) for any questions about custom integrations or [reach out to our Support Team](https://help.klaviyo.com/hc/en-us/requests/new).

## On-Site Behaviors (JavaScript Track API)

To enable our JavaScript API and the ability to publish forms directly from Klaviyo to your site, add the following snippet so appears on every page on your website (often the end of the footer is a good place to add this). Make sure to replace PUBLIC\_API\_KEY with your Klaviyo account's 6 character [Public API Key](https://www.klaviyo.com/account#api-keys-tab):

```
<script type="application/javascript" async
src="https://static.klaviyo.com/onsite/js/klaviyo.js?company_id=PUBLIC_API_KEY"></script>
```

### Active on Site

Once you’ve added the snippet above, ****Active on Site**** activity will now trigger for any person who is cookie-ed:

- Via a [Javascript Identify API request](https://help.klaviyo.com/hc/en-us/articles/115000751052-Klaviyo-API-Reference-Guide#identifying-users--javascript-3)
- By signing up through a Klaviyo form
- By clicking on a Klaviyo email and landing on your site

### Viewed Product

If you'd like to set up a [browse abandonment flow](https://help.klaviyo.com/hc/en-us/articles/115002775252-Create-a-Browse-Abandonment-Flow) or build segments based on product browsing data, you'll need to add JavaScript event tracking for a ****Viewed Product**** metric. On your product page template, add the following snippet:

```
<script text="text/javascript">
   var _learnq = _learnq || [];
   var item = {
     "ProductName": "Winnie the Pooh",
     "ProductID": "1111",
     "Categories": ["Fiction", "Children"],
     "ImageURL": "http://www.example.com/path/to/product/image.png",
     "URL": "http://www.example.com/path/to/product",
     "Brand": "Kids Books",
     "Price": 9.99,
     "CompareAtPrice": 14.99
   };

   _learnq.push(["track", "Viewed Product", item]);

   _learnq.push(["trackViewedItem", {
     Title: item.ProductName,
     ItemId: item.ProductID,
     Categories: item.Categories,
     ImageUrl: item.ImageURL,
     Url: item.URL,
     Metadata: {
       Brand: item.Brand,
       Price: item.Price,
       CompareAtPrice: item.CompareAtPrice
     }
   }]);
 </script>
```

### Added to Cart

If you’d like to send abandoned cart emails **before** someone lands on the checkout page, you’ll need to track information about the cart when someone takes a particular action. For this, we recommend sending an ****Added to Cart**** event when someone adds an item to their cart. A person will still need to have been "identified," or cookie-ed, to track this event. For the payload, you should include all of the cart information (like ****Started Checkout**** below) and information about the item that was just added (like Viewed Product above). Here's an example Track request:

```
<script text="text/javascript">
   _learnq.push(['track', Added to Cart, {
     "$value": 29.98,
     "AddedItemProductName": "A Tale of Two Cities",
     "AddedItemProductID": "1112",
     "AddedItem_SKU": "TALEOFTWO",
     "AddedItem_Categories": ["Fiction", "Classics"],
     "AddedItem_ImageURL": "http://www.example.com/path/to/product/image2.png",
     "AddedItem_URL": "http://www.example.com/path/to/product2",
     "AddedItem_Price": 19.99,
     "AddedItem_Quantity": 1,
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
   }]);
 </script>
```

### Started Checkout

Checkout data is important if you'd like to send [abandoned checkout emails](https://help.klaviyo.com/hc/en-us/articles/115002779411-Guide-to-Creating-an-Abandoned-Cart-Flow). When someone starts the checkout process, you'll send Klaviyo an event indicating they started checking out. The best place to trigger this event is when someone visits the checkout page after they’ve been "identified" or when they enter their email address on the checkout page if they have not already been identified.

You'll want to make sure you include all the details of the line items so your abandoned checkout emails can be customized to include pictures, links, and other information about the products in someone's cart. Here's an example Track request:

```
<script text="text/javascript">
   _learnq.push(['track', 'Started Checkout', {
     "$event_id": "1000123_1387299423",
     "$value": 29.98,
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
   }]);
 </script>
```

The `$event_id` should be a unique identifier for the cart combined with the UNIX formatted time when the event was triggered. This allows someone to trigger the ****Started Checkout**** more than once when they return after adding additional items.

## Server-Side Metrics

We recommend tracking certain metrics on the server-side due to potential limitations of frontend code as well as security concerns. If someone has a slow connection/computer or a JavaScript-blocking plugin on their browser, the JavaScript requests might not fire. In the case of more crucial metrics (like those for orders and other transactional events and properties) or ones that would contain sensitive data, use our server-side Track and Identify APIs.

### Placed Order

After an order is placed, you should make a Track request to our [server-side API](https://www.klaviyo.com/docs). We have libraries available for [Python](https://github.com/klaviyo/python-klaviyo), [Ruby](https://github.com/klaviyo/ruby-klaviyo), and [PHP](https://github.com/klaviyo/php-klaviyo), but in a general sense, the API just requires making an HTTP GET request with a base64 encoded JSON payload.

It is a good practice to send your historical order data as well. This will enhance your ability to segment off that data and improve historical accuracy in revenue tracking. Historical data can be sent to us by iterating through your historical orders and generating ****Placed Order**** and ****Ordered Product**** Track API requests for each. The special “time” property for these events should be the UNIX timestamp of when that order occurred.  More details on these metrics below.

You'll want to send order data to Klaviyo in one of two ways: real-time or batch.

- ****Real-time -**** You'll make requests as soon as an order is placed
- ****Batch -**** You’ll write a script that will run at least once an hour to send all events that occurred in that past hour

If you plan to send abandoned cart/checkout emails, you'll need to send order data at least at a frequency that falls within your email delay in order to stop the email from going to people who have completed their order. For example, if you have a one-hour time delay between when someone triggers the abandoned cart flow and when they receive the first email, you'll need to make sure that you send data over at least once every hour.

For each order, we recommend you send two types of events:

- One event named ****Placed Order**** for the entire order
  - This includes a `$value` property that represents the total value of an entire order including shipping, tax, discounts, etc.
- One event for each line item named ****Ordered Product****
  - This includes a `$value` property that represents the total cost of an item in the order before any adjustments as well as more SKU-level detailed information about the item

Key things to be aware of when tracking server-side events:

- Make sure to replace `API_KEY` with [your public API key](https://www.klaviyo.com/account#api-keys-tab).
- The `$event_id` should be a unique identifier for the order (eg. Order ID).
- If the same combination of `event` and `$event_id` are sent more than once, we will skip all tracked events after the first with the same combination.
- `$value` is a special property that allows Klaviyo to track revenue; this should be the total numerical, monetary value of the event with which it’s associated.
- The "Items" array should contain one dictionary for each line item.
- `time` is a special property that should be a UNIX timestamp of the order date and time.

Here’s an example Track request for ****Placed Order****:

```
{
   "token": "API_KEY",
   "event": "Placed Order",
   "customer_properties": {
     "$email": "john.smith@example.com",
     "$first_name": "John",
     "$last_name": "Smith",
     "$phone_number": "5551234567",
     "$address1": "123 Abc st",
     "$address2": "Suite 1",
     "$city": "Boston",
     "$zip": "02110",
     "$region": "MA",
     "$country": "USA"
   },
   "properties": {
     "$event_id": "1234",
     "$value": 29.98,
     "Categories": ["Fiction", "Classics", "Children"],
     "ItemNames": ["Winnie the Pooh", "A Tale of Two Cities"],
     "Brands": ["Kids Books", "Harcourt Classics"],
     "Discount Code": "Free Shipping",
     "Discount Value": 5,
     "Items": [{
         "ProductID": "1111",
         "SKU": "WINNIEPOOH",
         "ProductName": "Winnie the Pooh",
         "Quantity": 1,
         "ItemPrice": 9.99,
         "RowTotal": 9.99,
         "ProductURL": "http://www.example.com/path/to/product",
         "ImageURL": "http://www.example.com/path/to/product/image.png",
         "Categories": ["Fiction", "Children"],
         "Brand": "Kids Books"
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
         "Categories": ["Fiction", "Classics"],
         "Brand": "Harcourt Classics"
       }
     ]
   },
   "time": 1387302423
 }
```

### Ordered Product

For each line item, you should also make Track request for an ****Ordered Product**** event:

```
{
   "token": "API_KEY",
   "event": "Ordered Product",
   "customer_properties": {
     "$email": "john.smith@example.com",
     "$first_name": "John",
     "$last_name": "Smith"
   },
   "properties": {
     "$event_id": "1234_WINNIEPOOH",
     "$value": 9.99,
     "ProductID": "1111",
     "SKU": "WINNIEPOOH",
     "ProductName": "Winnie the Pooh",
     "Quantity": 1,
     "ProductURL": "http://www.example.com/path/to/product",
     "ImageURL": "http://www.example.com/path/to/product/image.png",
     "ProductCategories": [
       "Fiction",
       "Children"
     ],
     "ProductBrand": "Kids Books"
   },
   "time": 1387302423
 }
```

### Fulfilled Order, Cancelled Order, and Refunded Order

Depending on how your products are sent to the customer, or whether they are able to be cancelled or refunded, you may want to send additional events that reflect these actions. Each of these order-related events will have almost the same payload as a ****Placed Order**** event.

For ****Fulfilled Order****, the only update to be made is the event name and the time at which the fulfillment took place:

```
{
   "token": "API_KEY",
   "event": "Fulfilled Order",
   "customer_properties": {
     "$email": "john.smith@example.com",
     "$first_name": "John",
     "$last_name": "Smith",
     "$phone_number": "5551234567",
     "$address1": "123 Abc st",
     "$address2": "Suite 1",
     "$city": "Boston",
     "$zip": "02110",
     "$region": "MA",
     "$country": "USA"
   },
   "properties": {
     "$event_id": "1234",
     "$value": 29.98,
     "Categories": [
       "Fiction",
       "Classics",
       "Children"
     ],
     "ItemNames": [
       "Winnie the Pooh",
       "A Tale of Two Cities"
     ],
     "Brands": [
       "Kids Books",
       "Harcourt Classics"
     ],
     "Discount Code": "Free Shipping",
     "Discount Value": 5,
     "Items": [
       {
         "ProductID": "1111",
         "SKU": "WINNIEPOOH",
         "ProductName": "Winnie the Pooh",
         "Quantity": 1,
         "ItemPrice": 9.99,
         "RowTotal": 9.99,
         "ProductURL": "http://www.example.com/path/to/product",
         "ImageURL": "http://www.example.com/path/to/product/image.png",
         "Categories": [
           "Fiction",
           "Children"
         ],
         "Brand": "Kids Books"
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
         "Categories": [
           "Fiction",
           "Classics"
         ],
         "Brand": "Harcourt Classics"
       }
     ]
   },
   "time": 1387312956
 }
```

For ****Cancelled Order**** and ****Refunded Order****, update the event name and the timestamp and add an additional property for the cancellation or refund reason:

#### Cancelled Order

```
   "token": "API_KEY",
   "event": "Cancelled Order",
   "customer_properties": {
     "$email": "john.smith@example.com",
     "$first_name": "John",
     "$last_name": "Smith",
     "$phone_number": "5551234567",
     "$address1": "123 Abc st",
     "$address2": "Suite 1",
     "$city": "Boston",
     "$zip": "02110",
     "$region": "MA",
     "$country": "USA"
   },
   "properties": {
     "$event_id": "1234",
     "$value": 29.98,
     "Reason": "No longer needed",
     "Categories": [
       "Fiction",
       "Classics",
       "Children"
     ],
     "ItemNames": [
       "Winnie the Pooh",
       "A Tale of Two Cities"
     ],
     "Brands": [
       "Kids Books",
       "Harcourt Classics"
     ],
     "Discount Code": "Free Shipping",
     "Discount Value": 5,
     "Items": [
       {
         "ProductID": "1111",
         "SKU": "WINNIEPOOH",
         "ProductName": "Winnie the Pooh",
         "Quantity": 1,
         "ItemPrice": 9.99,
         "RowTotal": 9.99,
         "ProductURL": "http://www.example.com/path/to/product",
         "ImageURL": "http://www.example.com/path/to/product/image.png",
         "Categories": [
           "Fiction",
           "Children"
         ],
         "Brand": "Kids Books"
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
         "Categories": [
           "Fiction",
           "Classics"
         ],
         "Brand": "Harcourt Classics"
       }
     ]
   },
   "time": 1387312956
 }
```

#### Refunded Order

```
{
   "token": "API_KEY",
   "event": "Refunded Order",
   "customer_properties": {
     "$email": "john.smith@example.com",
     "$first_name": "John",
     "$last_name": "Smith",
     "$phone_number": "5551234567",
     "$address1": "123 Abc st",
     "$address2": "Suite 1",
     "$city": "Boston",
     "$zip": "02110",
     "$region": "MA",
     "$country": "USA"
   },
   "properties": {
     "$event_id": "1234",
     "$value": 29.98,
     "Reason": "No longer needed",
     "Categories": [
       "Fiction",
       "Classics",
       "Children"
     ],
     "ItemNames": [
       "Winnie the Pooh",
       "A Tale of Two Cities"
     ],
     "Brands": [
       "Kids Books",
       "Harcourt Classics"
     ],
     "Discount Code": "Free Shipping",
     "Discount Value": 5,
     "Items": [
       {
         "ProductID": "1111",
         "SKU": "WINNIEPOOH",
         "ProductName": "Winnie the Pooh",
         "Quantity": 1,
         "ItemPrice": 9.99,
         "RowTotal": 9.99,
         "ProductURL": "http://www.example.com/path/to/product",
         "ImageURL": "http://www.example.com/path/to/product/image.png",
         "Categories": [
           "Fiction",
           "Children"
         ],
         "Brand": "Kids Books"
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
         "Categories": [
           "Fiction",
           "Classics"
         ],
         "Brand": "Harcourt Classics"
       }
     ]
   },
   "time": 1387312956
 }
```

## Catalog Feed Integration

Integrating your catalog will allow you to use our [Product Feeds](https://help.klaviyo.com/hc/en-us/articles/115005082787-Product-Feeds-and-Recommendations) and [Product Blocks](https://help.klaviyo.com/hc/en-us/articles/115000219092-Insert-a-Product-Block) in emails. In order to set up a custom catalog integration, please reach out to our [Support Team](mailto:success@klaviyo.com). They will pass along the documentation and examples for this setup and will need to be notified once the setup is complete in order to activate the feed on your account.

## Syncing Historical Data

It is a good practice to send us your historical order data as well. This will enhance your ability to segment off that data and improve historical accuracy in revenue tracking. This data can be sent to us by iterating through your historical orders and generating ****Placed Order**** and ****Ordered Product**** Track API requests for each.
