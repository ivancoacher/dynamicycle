---
id: "16691649553179"
title: "Klaviyo Reviews data reference"
source_url: "https://help.klaviyo.com/hc/en-us/articles/16691649553179-Klaviyo-Reviews-data-reference"
section: "Reviews best practices"
category: "Reviews"
category_slug: "reviews"
klaviyo_updated: "2026-04-20T16:49:04Z"
language: "en"
---
## You will learn

Learn about the additional data available in Klaviyo when you start using reviews. This data falls into two broad categories: delivery metrics (Shopify only) and reviews metrics (available for WooCommerce and Shopify).

## How to view your data

Klaviyo Reviews syncs several metrics to your Klaviyo account. To view these metrics:

1. Click the ****Analytics**** dropdown in the left navigation of Klaviyo.
2. Select ****Metrics****.
   ![The Metrics menu item](https://klaviyo.zendesk.com/hc/article_attachments/28717418075163)
3. From the ****All integrations**** dropdown, choose ****Klaviyo****.
4. Klaviyo Reviews metrics are displayed among other Klaviyo metrics. Search for a specific metric, or read below to identify the metrics available through Klaviyo Reviews.

![Klaviyo reviews metrics](https://klaviyo.zendesk.com/hc/article_attachments/28717390814875)

## Delivery metrics

Delivery-related metrics include **Package in transit**, **Package delivered**, and more. Use these metrics to build flows and segments based on the status of a customer’s order.

Delivery-related metrics are only available for those who use Shopify. If you use WooCommerce as your ecommerce platform, these metrics are not available.

### Package delivered

This event is tracked when a customer’s package is delivered. Use this metric to trigger a flow message to let your customer know their order has arrived.

### Package in transit

This event is tracked when a carrier accepts a package you’ve shipped to a customer. Unlike **Fulfilled Order** events, which are generally tracked when you create a shipping label for an order, this event isn’t tracked until the carrier scans the package into their system and indicates it is in transit.

Use this event to trigger your shipment confirmation flow so that your customers can view carrier tracking information for their order right away.

### Package out for delivery

This event is tracked when a carrier indicates a package is set to be delivered that day. Use this event to trigger a message letting your customer know to be on the lookout for their order today.

### Delivery metrics properties

All delivery metrics include the following properties:

- ****product****
  (Legacy, Shopify only) Contains an array of details about the reviewed product, including its title, URL, and images.
- ****store\_url****
  Your store’s website URL.
- ****structured\_product****
  Contains an array of details about the reviewed product, including its title, URL, and images.
- ****review\_link****
  The custom link your customer will use to submit their review.
- ****shopify\_order\_number****
  The order number in your Shopify admin.
- ****order\_number****
  The order number from your ecommerce platform.
- ****package\_tracking\_number****
  The tracking number used to locate the package.
- ****package\_status****
  This may be **unknown**, **out\_for\_delivery**, or **delivered**.
- ****est\_delivery\_date****
  The estimated date when the order will be delivered.
- ****shipping\_destination****
  The country code (e.g., US) where the package was shipped.
- ****shipping\_carrier****
  The package carrier (e.g., USPS, FedEx).
- ****extra****
  Additional details about the order from your ecommerce platform, including items shipped, shipping address, and more.

## Reviews metrics

### Ready to review

This metric is tracked when an item is delivered or fulfilled and meets the criteria you set to indicate an item is ready to be reviewed. Learn how to [customize the](https://klaviyo.zendesk.com/hc/en-us/articles/16682549669403) [**Ready to review**](https://klaviyo.zendesk.com/hc/en-us/articles/16682549669403) [metric](https://klaviyo.zendesk.com/hc/en-us/articles/16682549669403).

This metric triggers the **Request review - Klaviyo Reviews** flow found in the flow library.

**Ready to review** events are only triggered for orders placed after you begin using Klaviyo Reviews. Learn how to [populate the](https://klaviyo.zendesk.com/hc/en-us/articles/25930166202651) [**Ready to review**](https://klaviyo.zendesk.com/hc/en-us/articles/25930166202651) [metric for past orders](https://klaviyo.zendesk.com/hc/en-us/articles/25930166202651).

This metric’s top-level properties include:

- ****product****
  (Legacy, Shopify only) Contains an array of details about the reviewed product, including its title, URL, and images.
- ****store\_url****
  Your store’s website URL.
- ****structured\_product****
  Contains an array of details about the reviewed product, including its title, URL, and images.
- ****review\_link****
  The custom link your customer can use to submit their review.
- ****shopify\_order\_number****
  The order number in your Shopify admin.
- ****package\_tracking\_number****
  The tracking number used to locate the package.
- ****package\_status****
  This will always be **delivered**.
- ****est\_delivery\_date****
  The date when the order was delivered.
- ****shipping\_destination****
  The country code (e.g., US) where the package was shipped.
- ****shipping\_carrier****
  The package carrier (e.g., USPS, FedEx).
- ****extra****
  Additional details about the order from your ecommerce platform, including items shipped, shipping address, and more.
- ****$event\_id****
  The unique ID for the **Package** **out for delivery** event.

### Submitted review

This metric is tracked when a customer submits a review. It serves as the trigger for the **Review reward - Klaviyo Reviews** flow in the flow library.

This metric’s top-level properties include:

- ****product****
  (Legacy, Shopify only) Contains an array of details about the reviewed product, including its title, URL, and images.
- ****store\_url****
  Your store’s website URL.
- ****structured\_product****
  Contains an array of details about the reviewed product, including its title, URL, and images.
- ****review\_link****
  The custom link your customer used to submit their review.
- ****review\_rating****
  A number 1-5 indicating the customer’s rating.
- ****review\_images****
  An array of image URLs, if the reviewer submitted product images.
- ****review\_author****
  The handle of the person who submitted the review.
- ****review\_email****
  The email address of the person who submitted the review.
- ****review\_content****
  The body text of the review submitted by the customer.
- ****review\_title****
  The title of the review submitted by the customer.
- ****review\_status****
  Whether the review is published or pending when it is initially submitted. This field does not update if a review’s status changes (i.e., moves from pending to rejected).
- ****review\_verified****
  True or false, indicating whether the review is from a verified purchaser. Reviews are marked as verified if they are submitted through a review request flow message sent via Klaviyo or if a user checks the **I confirm that the imported reviews are genuine** option when uploading reviews.
- ****review\_has\_media****
  True or false, indicating whether an image or video was included in the review.
- ****$event\_id****
  The unique ID for the review event.

Klaviyo only collects variant information when a review is submitted in response to a review request. Reviews submitted by navigating to a product page and manually clicking the Write a review button will not include variant information.

### Submitted rating

This metric is tracked when a customer submits a rating (i.e., a star rating for a product without additional content like a text review).

- ****product****
  (Legacy, Shopify only) Contains an array of details about the reviewed product, including its title, URL, and images.
- ****store\_url****
  Your store’s website URL.
- ****structured\_product****
  Contains an array of details about the reviewed product, including its title, URL, and images.
- ****review\_link****
  The custom link your customer used to submit their review.
- ****shopify\_order\_number****
  (Shopify only) The order number from Shopify.
- ****order\_number****
  The order number from your ecommerce platform.
- ****package\_tracking\_number****
  The tracking number for the item the customer reviewed.
- ****package\_status****
  The package status; generally **delivered** for all rated products.
- ****shipping\_destination****
  The city and state where the package was shipped.
- ****shipping\_carrier****
  The carrier for the reviewed item's package (e.g., USPS, FedEx).
- ****est\_delivery\_date****
  The product's delivery date (generally a date in the past).
- ****extra****
  Additional details about the order from your ecommerce platform, including items shipped, shipping address, and more.
- ****$event\_id****
  The unique ID for the review event.

### Analyzed review topic sentiment

This metric is tracked when Klaviyo uses AI to [analyze a review’s content](https://help.klaviyo.com/hc/en-us/articles/22567673911707#h_01J06Y8YXHDPPTYQZWTA09J0EJ). Use this metric to filter flows or [create support tickets](https://help.klaviyo.com/hc/en-us/articles/16680027976731) automatically.

- ****product****
  (Legacy, Shopify only) Contains an array of details about the reviewed product, including its title, URL, and images.
- ****$service****
  Always “klaviyo.”
- ****store\_url****
  Your store’s website URL.
- ****review\_link****
  The custom link your customer used to submit their review.
- ****order\_number****
  The order number from your ecommerce platform.
- ****package\_tracking\_number****
  The tracking number for the item the customer reviewed.
- ****package\_status****
  The package status; generally **delivered** for all rated products.
- ****shipping\_destination****
  The city and state where the package was shipped.
- ****shipping\_carrier****
  The carrier for the reviewed item's package (e.g., USPS, FedEx).
- ****est\_delivery\_date****
  The product's delivery date (generally a date in the past).
- ****extra****
  Additional details about the order from your ecommerce platform, including items shipped, shipping address, and more.
- ****review\_id****
  The ID used in Klaviyo for the review.
- ****review\_rating****
  A number 1-5 indicating the customer’s rating.
- ****review\_author****
  The handle of the person who submitted the review.
- ****review\_email****
  The email address of the person who submitted the review.
- ****review\_content****
  The body text of the review submitted by the customer.
- ****review\_title****
  The title of the review submitted by the customer.
- ****review\_status****
  Whether the review is published or pending when it is initially submitted. This field does not update if a review’s status changes (i.e., moves from pending to rejected).
- ****review\_verified****
  True or false, indicating whether the review is from a verified purchaser. Reviews are marked as verified if they are submitted through a review request flow message sent via Klaviyo or if a user checks the **I confirm that the imported reviews are genuine** option when uploading reviews.
- ****review\_has\_media****
  True or false, indicating whether an image was included in the review.
- ****review\_images****
  An array of image URLs, if the reviewer submitted product images.
- ****product\_external\_id****
  The ID of the reviewed product from your product catalog.
- ****structured\_product****
  Contains an array of details about the reviewed product, including its title, URL, and images.
- ****topic****
  The topic of the review, as identified by Klaviyo AI (e.g., “productQuality”).
- ****topic\_name****
  The friendly name of the topic of the review, as identified by Klaviyo AI (e.g., “Product Quality”).
- ****sentiment****
  The review’s sentiment (i.e., “positive” or “negative”).
- ****snippet****
  A portion or summary of the review used by Klaviyo AI to identify its topic and sentiment.
- ****subtopic****
  Additional information about the review’s topic, as identified by Klaviyo AI.
- ****confidence****
  The level of confidence Klaviyo AI has that it’s identification of the review’s topic and sentiment is correct (i.e., “low”, “medium”, “high”).
- ****klaviyo\_token****
  Your Klaviyo public API key.

## Profile data

If you set up custom review questions, reviewers’ answers will be saved as custom profile properties in Klaviyo. Learn more about [how to use profile properties](https://help.klaviyo.com/hc/en-us/articles/115005074627).