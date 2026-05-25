---
id: "115002775252"
title: "How to create a browse abandonment flow"
source_url: "https://help.klaviyo.com/hc/en-us/articles/115002775252-How-to-create-a-browse-abandonment-flow"
section: "Browse abandonment flows"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-04-21T13:54:13Z"
language: "en"
---
## You will learn

Learn how to create a browse abandonment flow to show shoppers products they viewed but didn’t purchase.

In browse abandonment flows, a visitor doesn't have to add an item to their cart to trigger this flow. All a site visitor has to do is view an item and move on.

Visiting a product page doesn’t indicate the same level of interest as adding an item to a shopping cart and beginning the checkout process, so we recommend making your browse abandonment messages a "lighter touchpoint" than your abandoned cart flow.

![](https://fast.wistia.com/embed/medias/fl25jmzbha/swatch)

## Configure Viewed Product tracking

Browse abandonment flows are triggered by the **Viewed Product** metric. This flow thus requires **Viewed Product** tracking to be enabled on your website.

For Shopify, **Viewed Product** tracking is enabled by Klaviyo's app embed in Shopify. You can find out more in our guide to [getting started with Shopify](https://help.klaviyo.com/hc/en-us/articles/115005080407-Getting-started-with-Shopify#onsite-tracking4).

For BigCommerce stores, when you first integrated with Klaviyo, the Setup Wizard prompted you to add two onsite tracking code snippets: home page tracking and **Viewed Product** tracking. If you didn't already complete this step, you can do so by following our guide to [getting stared with BigCommerce](https://help.klaviyo.com/hc/en-us/articles/115005082547#h_01HAQ99C0AEYNSZ7YKNX9PX6C9).

For details on adding **Viewed Product**tracking for a different integration, head to our guide on [understanding Viewed Product tracking](https://help.klaviyo.com/hc/en-us/articles/115005076767#h_01HADAYAAC3079D44928A58MTY).

### Custom carts and ecommerce platforms

If you've set up your own custom ecommerce integration and would like to create a browse abandonment flow (or build segments based on product page browsing data), you'll need to add JavaScript event tracking for a **Viewed Product** metric. We've built a snippet [you can add to your product page template](https://developers.klaviyo.com/en/docs/changelog_).

## Monitor the **Viewed Product** metric

When you add onsite tracking to your site, Klaviyo tracks the browsing activity of identifiable browsers (i.e., browsers who that have visited or engaged on your site, submitted a form through a certain action, reached the success step of a form, reached the final reachable step for tap-to-text for SMS, or have been identified or "cookied").

To check on this metric

1. Navigate to ****Analytics >**** ****Metrics****.
2. Search for "Viewed product" in the metric search bar.

If viewed product web tracking has been configured for your site, you should see data populating in your account as known visitors browse your product pages.

If there is no data available, [test the metric out yourself](https://help.klaviyo.com/hc/en-us/articles/115005076767#h_01HADAYAACFYSN7F22XPPCGT6B).

For Shopify stores: Based on your Customer Privacy settings in Shopify, Klaviyo may not track onsite events for visitors to your Shopify store in the EU, EEA, UK and Switzerland, unless they have provided consent. Thus, your browse abandonment flow will not include non-consented individuals.

## Are you using Klaviyo's Amazon Buy with Prime integration?

If you're using Buy with Prime to power payment and fulfillment for any of the products on your store, and you've [integrated Klaviyo and Buy with Prime](https://help.klaviyo.com/hc/en-us/articles/14708088221467), make sure to do the following:

When you create your browse abandonment flow (either pre-built or from scratch) add the following profile filters to incorporate Buy with Prime data into your flow:

- **Checkout Started** (Buy with Prime) **zero times since starting this flow**AND
- **Placed Order** (Buy with Prime) **zero times since starting this flow**

## Use a pre-built browse abandonment flow

Klaviyo provides many integrations with with pre-built browse abandonment flows. These flows include emails designed to dynamically populate with information about the product viewed (the item’s image, name, and price).

If the flow is not in your account, you can access it be following these steps:

1. Navigate to the ****Flows**** tab.
2. Click ****Create flow****.
3. Filter by "browse abandonment" to customize the type of flow you start with.

For Shopify, we also offer an [abandoned collection flow](https://www.klaviyo.com/library/flows?object_id=QTPgWY) and an [abandoned search flow](https://www.klaviyo.com/library/flows?object_id=V3i6gC).

## Build your own browse abandonment flow

We recommend using one of the pre-built flows, if available, rather than creating your own to ensure all the dynamic variables work properly.

1. Navigate to the ****Flows >**** ****Create flow.****
2. Select ****Build your own****.
3. Choose ****All triggers**** ****> Metric****.
4. Select ****Viewed Product.
   ![browse1.jpg](https://klaviyo.zendesk.com/hc/article_attachments/39961670105243)****
5. Add the following profile filters:
   - **Placed Order zero times since starting this flow**
     AND
   - **Started Checkout zero times since starting this flow**
     AND
   - **hasn't been in this flow in the last 30 days**
     AND
   - **Added to Cart zero times since starting this flow**
     - Only applies if you also have a flow triggered by the **Added to Cart**metric, as otherwise, customers could get emails from both flows
       ****![browse2.jpg](https://klaviyo.zendesk.com/hc/article_attachments/39961670109851)****
6. Add in a time delay for at least one hour.
7. (Optional) Add in splits to provide more personalized communications to different groups:
   - Purchasers vs. non-purchasers
   - Domestic vs. international
   - Product type or category
8. Add in your email or SMS.
9. Add in additional time delays, splits, and emails as needed.

## How to show the product viewed in an email

Do not copy the default abandoned cart message for a browse abandonment flow. Whereas the block for an abandoned cart message should be set to ****Dynamic****, the block for a browse abandonment message should be ****Static****. Switching the block type will erase the tags, text, etc. If you already cloned the default abandoned cart message for your browse abandonment flow, copy the tags before changing the block from ****Dynamic**** to ****Static****.

### Build the email

1. Drag an image block into your template.
2. Click ****Select image > Dynamic image****.
3. In the image block’s **Dynamic variable or dynamic URL** field, add `event.ImageURL`
4. Click ****Save.****
5. Drag an image block into your template.
6. In the image block’s **Dynamic Image** or **Placeholder** field, add `event.ImageURL`
7. Drag a text block into your template, then add the following tags:
   - `{{ event.Name }}` where you'd like to insert the product's name
   - `{{ event.Price }}` where you want to insert the product's price
   - `{{ event.URL }}` in any **URL** or **Link URL** field that you’d like to direct to the product page
8. Click ****Preview & test****; you should see dynamic product data populate into the placeholder variables.

If a customer views multiple products, the one that is shown depends on your setup:

- If you are using **hasn't been in this Flow in the last X days**, then it'll be the first item the customer viewed.
- If you're using **has viewed product zero times since starting this flow**, it'll be the most recent.

## Other audiences to target

There are a few different types of audiences you can target with your custom browse abandonment emails, including:

- ****Someone views a product and has received email from flow zero times in the last X days****If you're worried that frequent browsers might receive too many browse abandonment emails, you can add this filter to limit how often someone will get an email from this flow. Leaving Smart Sending ON for all browse abandonment emails is also a good idea.
- ****Someone views a product and has placed order equals zero over all time****This filter allows you to target people that have never purchased before and might be new to your brand. You may want to incentivize these browsers to make a first purchase by including a discount code or promotional offer in your flow email.
- ****Someone views a product and has placed order at least once over all time****This filter is the inverse of the example above -- if you target browsers that have never purchased before in one flow, you will also want to target customers that are re-visiting your site to potentially buy again through a separate flow. You may not want to include a discount offer here, since these customers have already taken the leap to buy and are back again to browse on their own.
- ****Someone views a product and has viewed product at least Z times since starting this flow****This filter allows you to target those that are spending a bit of time on your site viewing different products. Adding this filter means as someone begins to browse, the first X number of products viewed will not trigger this flow -- only after Z number of items are viewed will someone receive your flow email, and the email can be configured to show the last item the recipient viewed.
- ****Someone views product where product equals Product X****This filter allows you to create special offers for those browsing a specific item. Let's say you want to share a special discount for those browsing a more expensive item on your site. You can target those browsing certain items by adding a trigger filter for the specific item you'd like to target.

## Additional resources

Check out this article on [branching flows](https://help.klaviyo.com/hc/en-us/articles/360051182592).

Learn [how to build an upsell or cross-sell flow](https://help.klaviyo.com/hc/en-us/articles/115002775212).