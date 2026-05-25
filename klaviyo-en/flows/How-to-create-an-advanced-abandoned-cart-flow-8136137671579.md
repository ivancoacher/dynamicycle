---
id: "8136137671579"
title: "How to create an advanced abandoned cart flow"
source_url: "https://help.klaviyo.com/hc/en-us/articles/8136137671579-How-to-create-an-advanced-abandoned-cart-flow"
section: "Abandoned cart flows"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-04-21T13:56:59Z"
language: "en"
---
## Taking your abandoned cart flow to the next level

[Walkthrough of the more advanced flow options available after the base abandoned cart flow is setup](https://fast.wistia.net/embed/iframe/lae6h33k0g?videoFoam=true)

Once you have a basic abandoned cart flow set up, you may wonder what comes next and how you can make your existing flow even better. Because all businesses are different and have their own unique audiences, there isn't just one formula that will work for everyone.

The [****Browse Ideas**** tab](http://www.klaviyo.com/library/flows?tags=Abandoned%20Cart) is a great place to look for new ideas and inspiration when leveling up your abandoned cart flow, and includes many of the best practice branched flows outlined below.

Testing new ideas is the best way to optimize your abandoned cart flow. Below are a few recommendations for where to start.

To influence open rate (email only):

- Timing
- Subject lines
  - Urgency
  - Emojis

To influence click rate:

- Content
  - Plain text vs. graphic rich
  - CTA location
  - General email layout
  - MMS vs. SMS

To influence conversion rate or revenue per recipient:

- Branching
  - Purchasers vs. non-purchasers
  - Domestic vs. international
  - Product category/collection
  - Value of items in cart
  - Number of items in cart

Below, we talk about different branches you can use in your abandoned cart flows.

### Branching by purchasers vs. non-purchasers

Messaging existing customers and non-customers differently is a good practice, especially if you plan on offering an incentive if your abandoned cart flow. You don't want to over-discount, so you may want to only offer a coupon code to shoppers who have never purchased from you before to encourage them to buy for the first time.

If you take this approach, be sure to include language like, "Take 10% off your first purchase" so that recipients don't grow to expect a discount every time they abandon a cart. Additionally, use dynamic coupon codes to prevent sharing on sites like RetailMeNot, etc.

Learn more about how to use coupon codes in Klaviyo:

- [Dynamic coupons for Shopify](https://help.klaviyo.com/hc/en-us/articles/115006155388-Unique-Coupon-Codes-for-Shopify)
- [Dynamic coupons for Magento 1](https://help.klaviyo.com/hc/en-us/articles/115005246547-Set-Up-Coupons-for-Magento-1-x-)
- [Dynamic coupons for other integrations](https://help.klaviyo.com/hc/en-us/articles/115005084727-How-to-Use-Coupon-Codes-in-Klaviyo#overview0)

To split your flow by purchasers versus non-purchasers, first, drag a conditional split into the top of your flow. Then, set this split to be based on **What someone has done or not done >****Has Placed Order at least once over all time.** People who have never placed an order before will go down the NO path while existing customers will go down the YES path.

![An example of a conditional split placed at the top of the flow if a subscriber placed an order at least once or not](https://klaviyo.zendesk.com/hc/article_attachments/28720760944923)

Then, you can include a coupon in the final email of the NO path.

### Branching by domestic vs. international shoppers

You may be able to offer special perks to domestic customers that you don't to international customers, like free shipping. Branching your flow by domestic versus international customers allows you to highlight these perks if your emails to domestic customers to persuade them to purchase.

First, drag a conditional split to the top of the flow. Then, set this split to be based on **Properties about someone > Country equals US.** Those who flow down the YES path will be domestic customers, and those on the NO path are international.

![An example of split of a flow using branching to separate out if a subscriber is in the US or not](https://klaviyo.zendesk.com/hc/article_attachments/28720772751131)

### Branching by product category or collection

If you have a large product offering, you may want to branch your abandoned cart flow by category or collection to include more relevant copy and images in your emails. One key example is if you sell men's and women's products. In this case, it's also important to include a default branch in case the product in someone's cart is not in either the men's or women's collection.

First, drag a trigger split to the top of the flow. Set the collection (or "category," depending on your ecommerce integration) to contain Women's. Then, drag another trigger split directly beneath the first one. Set this collection to contain Men's. Those who flow down NO path after this trigger split should receive a more generic abandoned cart flow.

![A flow example separating subscribers through the product category of men's versus women's clothing](https://klaviyo.zendesk.com/hc/article_attachments/28720760950683)

### Branching by cart value

You may want to message customers with larger cart values differently than those at or below your store's [average order value](https://help.klaviyo.com/hc/en-us/articles/360000676712-Calculating-Your-Average-Order-Value-AOV-). For example, if the value of the items in someone's cart adds up to triple your average order value, you may want to offer them an incentive to encourage them to complete the purchase.

To do this, drag a Trigger Split to the top of the flow. In this example, our average order value is $100. Next, configure the split to be based on**Checkout started value is less than 300.**Those whose carts are worth less than $300 will flow down the YES path, while those with triple your average order value or more will flow down the NO path.

![An example flow where a Trigger Split is used to separate out the monetary value of less than 300 or higher of a potential cart.](https://klaviyo.zendesk.com/hc/article_attachments/28720760952603)

### Branching by cart size

Similarly, you may want to branch your abandoned cart flow based on the number of items someone has in their cart. For example, you may want to offer someone with three or more items in their cart a buy one get one free (BOGO) or other promotion to encourage them to place an order.

To do this, first drag a Trigger Split to the top of the flow and configure it based on **Item Count is less than 3**. Shoppers with fewer than 3 items will flow down the YES path, while those with more than 3 items will flow down the NO path.

![An example flow where a Trigger Split is used to separate the number of items in a potential cart between Item Count is less than 3 or higher](https://klaviyo.zendesk.com/hc/article_attachments/28720772759451)