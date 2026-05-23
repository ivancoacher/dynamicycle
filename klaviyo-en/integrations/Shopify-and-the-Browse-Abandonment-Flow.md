---
id: 115005080787
title: "Shopify and the Browse Abandonment Flow"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005080787-Shopify-and-the-Browse-Abandonment-Flow"
section: "Shopify best practices"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:19Z"
language: en
---

## Overview

Browse abandonment emails are similar to abandoned carts, but are triggered when an identifiable browser visits a product page — a visitor doesn't have to add an item to his/her cart to trigger this flow, all a site visitor has to do is view the item.

Because visiting a product page doesn’t quite indicate the same level of interest as adding an item to a shopping cart, we recommend including related or similar products in your browse abandonment emails to broaden your net. Adding a discount code into a browse abandonment email can also help turn a casual browser into an enthusiastic customer.

The following guide will walk you through how to get a new Browse Abandonment flow up and running.

## Add the Viewed Product Tracking Code

First, you'll need to add a snippet of code to your Shopify store's backend. This code will get added to your store's product.liquid template.

|  |
| --- |
| Note: If you have already added code to your product.liquid template to enable product page tracking, you may need to replace this previously added snippet of code with the new updated code shared in this guide. |

Find your store's product.liquid template by navigating to **Online Store** --> **Themes** --> **Edit HTML/CSS**--> **product.liquid**in your Shopify Admin portal.

Click into your product.liquid template and scroll down to the very bottom. This is where you will place the following code:

```
<script text="text/javascript">
 var _learnq = _learnq || [];
 var item = {
   Name: {{ product.title|json }},
   ProductID: {{ product.id|json }},
   Categories: {{ product.collections|map:'title'|json }},
   ImageURL: "https:{{ product.featured_image.src|img_url:'grande' }}",
   URL: "{{ shop.secure_url }}{{ product.url }}",
   Brand: {{ product.vendor|json }},
   Price: {{ product.price|money|json }},
   CompareAtPrice: {{ product.compare_at_price_max|money|json }}
 };

 _learnq.push(['track', 'Viewed Product', item]);

 _learnq.push(['trackViewedItem', {
   Title: item.Name,
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

Once this code has been pasted at the bottom of your product.liquid template, click **Save**.

Remember: If you previously added a very short snippet of code to your product.liquid template to enable product page tracking, you may need to replace it with the above snippet. The updated code will look this this in your product.liquid template:

![647553](https://klaviyo.zendesk.com/hc/article_attachments/28717849944987)

## Monitor the "Viewed Product" Metric

|  |
| --- |
| Note: When you add the Klaviyo tracking snippet above to your site, we will not track the **Viewed Product**event for all site visitors. We are only able to track this event for "known browsers". There are a two key ways we will be able to identify a site visitor for web tracking purposes:  - When someone clicks through a Klaviyo email to your website - When someone has, at some point, subscribed/opted-in through a Klaviyo form |

After this code snippet has been pasted and saved into your store's product.liquid template, "Viewed Product" data should begin populating in your Klaviyo account as known visitors browse your product pages.

To check on this metric, click into your account's **[Dashboard](https://www.klaviyo.com/dashboard)**and navigate to the **Activity Feed**tab. Here, you will see a dropdown labeled "Showing Feed for". Adjust this dropdown to filter for the metric "Viewed Product".

![647543](https://klaviyo.zendesk.com/hc/article_attachments/28717849946139)

If there is no data available, test the metric out yourself by browsing your own website and clicking around to view different products. You should see this data begin to flow into Klaviyo. After you send your first campaign, or begin to grow your subscriber list, this browsing data will grow as Klaviyo is able to identify more and more people engaging with your site. If you are concerned this code snippet is not functioning properly, [contact our Success Team](https://help.klaviyo.com/hc/en-us/requests/new) and we'll help troubleshoot!

## Set Up the Browse Abandonment Flow

If Klaviyo's best-practice Browse Abandonment flow was not pre-populated in your account, you can grab this flow now from the **Browse I****deas**section of your **Flows** tab.

![647541](https://klaviyo.zendesk.com/hc/article_attachments/28717810315675)

|  |
| --- |
| [Reference this guide](https://docs.klaviyo.com/customer/portal/articles/2475177#section4) for information on how to customize Klaviyo's Browse Abandonment flow or build your own! |