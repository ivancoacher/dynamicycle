---
id: "25995019549979"
title: "How to choose a product ID variable for a dynamic review quote block"
source_url: "https://help.klaviyo.com/hc/en-us/articles/25995019549979-How-to-choose-a-product-ID-variable-for-a-dynamic-review-quote-block"
section: "Build and use reviews"
category: "Reviews"
category_slug: "reviews"
klaviyo_updated: "2026-04-20T16:49:36Z"
language: "en"
---
## You will learn

Learn how to select a product ID variable to display dynamic review quotes related to the products someone is interested in. These variables vary between events, so make sure to use the right variable for your flow.

## Before you begin

This block is only available in accounts that use Klaviyo Reviews. Learn how to [get started with Klaviyo Reviews](https://help.klaviyo.com/hc/en-us/articles/15937542819355).

## About dynamic review blocks

Dynamic review quote blocks can display different reviews depending on when the email is sent and what actions the recipient has taken, unlike static review blocks, which feature the same product for every recipient.

This article specifically covers dynamic review blocks, not static. Static review quote blocks do not require a product ID variable.

This process is only supported in certain flow emails: event-triggered flows, back in stock flows, low inventory flows, and price drop flows. Learn how to [add a dynamic review block](https://klaviyo.zendesk.com/hc/en-us/articles/18007373861915) to your emails.

In many cases, Klaviyo will auto-detect the product ID. In these cases, you don’t need to manually choose a product ID variable. If you see a button like the one below indicating your flow’s trigger, that means Klaviyo will auto-detect your product ID, and you do not need to follow the steps outlined here.

![](https://klaviyo.zendesk.com/hc/article_attachments/33237640856475)

However, for some custom flows, you may need to manually input a product ID variable. If you see the **Product ID variable** field shown in the screenshot below, follow these steps to add a variable.

![](https://klaviyo.zendesk.com/hc/article_attachments/33237663341211)

## Product ID variables

The table below offers the most common event variables used for review quote blocks. In addition to those in the table below, you can use any other event variable that references a product ID. To find a product ID variable other than those in the table below:

1. From your flow email, click ****Preview & test****.
2. Click the event variable you’d like to use in your review quote block. When you click the variable name, the tag will be copied to your clipboard.
3. Remove all extraneous information from the tag: the curly quotes that surround it and any filters, which follow the tag information. For example, if the original tag was {{ event.product.id|default:”” }}, remove everything from the tag except **event.product.id**.
4. Paste this variable into the **Event variable for product ID** field.

If a trigger event contains multiple items (e.g., abandoned cart flows), only the first item is considered when choosing reviews. We do not recommend using the second, third, or any other items, because not every instance of the event will contain multiple items.

### Shopify product ID variables

|  |  |
| --- | --- |
| ****Flow trigger**** | ****Event variable**** |
| Browse abandonment | event.ProductID |
| Abandoned cart (**Add to cart** trigger) | event.ProductID |
| Abandoned checkout (**Checkout started** trigger) | event.extra.line\_items.0.product.id |
| Back in stock | event.ProductID |
| Price drop | event.product\_id |
| Low inventory | event.product\_id |
| Placed order | event.extra.line\_items.0.product.id |

### WooCommerce product ID variables

|  |  |
| --- | --- |
| ****Flow trigger**** | ****Event variable**** |
| Browse abandonment | event.ProductID |
| Abandoned cart (**Add to cart** trigger) | event.ProductID |
| Abandoned checkout (**Checkout started** trigger) | event.extra.Items.0.ProductID |
| Placed order | event.extra.Items.0.ProductId |