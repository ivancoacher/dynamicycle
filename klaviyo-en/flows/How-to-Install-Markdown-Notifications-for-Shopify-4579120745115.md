---
id: "4579120745115"
title: "How to Install Markdown Notifications for Shopify"
source_url: "https://help.klaviyo.com/hc/en-us/articles/4579120745115-How-to-Install-Markdown-Notifications-for-Shopify"
section: "Add steps or actions to flows"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-04-21T13:56:58Z"
language: "en"
---
## Overview

Learn how to install Klaviyo's markdown notifications snippet for Shopify so that your customers can subscribe to markdown alerts when an item’s price drops, as well as how to build a markdown notification flow to send out the alerts.

Klaviyo's Markdown Notifications feature for Shopify stores has two key components:

1. ****Markdown Notification Flow****: When someone subscribes to a markdown alert, a "Subscribed to Markdown Notifications" event will be tracked on their Klaviyo profile. This is the event you will use to trigger your Markdown Notification Flow. Shoppers will enter the flow when they subscribe to a markdown alert and wait at a "Markdown Notification Delay" until their item of interest goes on sale.
2. ****Website Button****: You will need to add a snippet to your Shopify theme that will automatically show a "Notify me when price drops" button when items reduce in price. When shoppers click this button, they will fill out a form and subscribe for notifications.

## Adding the Markdown Notification Snippet

Because pasting this code requires access to your site's HTML and ecommerce platform, our support team is unable to offer hands-on assistance. If you don't have a developer on your team and aren't comfortable adding the code yourself, consider [reaching out to a Klaviyo partner for assistance](https://klaviyo.partnerpage.io/).

Using the Markdown Notification feature involves pasting a JavaScript snippet into your Shopify product page template.

As soon as you install the snippet provided below, the following will occur:

- When a shopper browses a product, a "Notify me when price drops" button will appear on the product page.
- When someone clicks the "Notify Me..." button, a form will pop up that allows the shopper to signup to be notified when the item’s price drops.
- As soon as the form is submitted, that shopper can receive alerts from a markdown notification flow.

The Markdown Notification snippet is:

```
[INSERT MARKDOWN NOTIFICATION CODE SNIPPET]
```

Product page templates are managed differently for Shopify 2.0 themes. Please see the appropriate section below depending on your theme.

### For Shopify 2.0 Themes

If your Shopify store uses a Shopify 2.0 theme, you’ll need to add the Markdown Notification snippet via a Custom Liquid block.

1. In Shopify, navigate to your theme and click ****Customize****.
2. At the top of the page, click the ****Home page**** dropdown, and select ****Products > Default**** ****product**** to be brought to your default product page.

1. If you have multiple product page templates other than the default, you’ll need to add the snippet to those templates as well.

3. Click ****Add Section**** in the left sidebar, and then select ****Custom Liquid****.
4. Paste the snippet from the above section into the Custom Liquid text box.

   ****[INSERT SCREENSHOT OF CODE SNIPPET IN CUSTOM LIQUID BLOCK]****
5. Click ****Save**** in the upper right.
6. In the left bar, your new Custom Liquid block should automatically have been placed below the other sections on the page.

1. If it needs to be moved, hover over the block and click the six dots to drag it below your other sections.
   ![Shopify product page section hierarchy with custom liquid option showing six gray dots, below product recommendations section which is below product information section](https://klaviyo.zendesk.com/hc/article_attachments/28717988165659)

### For All Other Themes

For other Shopify themes, the Markdown Notification snippet will need to be pasted at the bottom of your ****product.liquid**** file.

1. Copy the code snippet included earlier in this article.
2. From your Shopify Admin click ****Online Store > Themes****. From the dropdown, click ****Edit Code****.
   ![Shopify themes page showing espresso shot glasses on right bottom corner with Actions dropdown open and Edit Code selected](https://klaviyo.zendesk.com/hc/article_attachments/28717988160411)
3. Search for the ****product.liquid**** file. Click the file to open it in the editor.
   ![Shopify’s Edit Theme page grayed out with the product.liquid file selected and highlighted](https://klaviyo.zendesk.com/hc/article_attachments/28717988162331)
4. Paste the code snippet at the bottom of the file, after all the existing code, and click ****Save****.

   ****[INSERT SCREENSHOT OF CODE SNIPPET IN SHOPIFY THEME EDITOR]****

If you are using custom product pages, you may need to add this snippet to a different theme file, or to your individual custom product pages.

## Set Up a Markdown Notifications Flow

Klaviyo has a pre-built markdown notification flow available in the [Flow Library](https://www.klaviyo.com/library/flows).

Once you navigate to the Flows tab, you can choose either ****Create Flow**** or ****Browse Ideas**** to be taken to the library directly.

You can easily find this markdown notification flow by searching for "markdown notification" in the toolbar at the top of the Flows Library.

****[INSERT SCREENSHOT OF THE PRE-BUILT FLOW IN THE FLOW LIBRARY]****

After populating any flow in your account from the library, we recommend reviewing all email content and updating the templates to match your brand.

If you'd like to build a markdown notification flow from scratch, you can do this as well.

1. Click ****Create Flow****, name your markdown notification flow, and add tags.
2. Once in the Visual Flow Builder, choose the trigger option ****Takes an Action****. In the dropdown menu that follows, choose the metric **Subscribed to Markdown Notifications**. Do not add any trigger or flow filters, and click ****Done****.
3. The next component you'll want to drag in — directly after the trigger — is the **Markdown Notification Delay**. Recipients that enter your flow will wait at this delay until their item of interest is restocked. After this occurs, they will move on to the next step in your flow (which is typically an email but could be an SMS).
4. Typically, you will only need a single message in this flow as a notification that the item has dropped in price. Make sure to [turn Smart Sending off](https://help.klaviyo.com/hc/en-us/articles/115002779311-Smart-Sending-for-Flows#how-to-disable-smart-sending) for this message to ensure everyone gets the alert.

****[INSERT SCREENSHOT OF A BASIC MARKDOWN NOTIFICATION FLOW]****

You do not need to add any time delay components to this series, as the markdown notification delay will ensure each person that enters your flow waits until the item they subscribed to drops in price before moving forward.

## Markdown Notification Flow vs Price Drop Flow

Klaviyo has a similar feature to Markdown Notifications in the form of the [Price Drop Flow](https://help.klaviyo.com/hc/en-us/articles/4404249033755-Guide-to-Creating-a-Price-Drop-Flow). Both features allow a flow to be triggered based on when an item’s price is reduced. However, there are some key differences. Please see the chart below for comparison.

|  |  |
| --- | --- |
| ****Markdown Notification Flow**** | ****Price Drop Flow**** |
| Only available for Shopify stores. | Available for BigCommerce, Magento 2, Shopify, and WooCommerce stores. |
| Requires customers to explicitly subscribe to a markdown alert for a product through a form on the product’s store page. | Triggers based on if the customer started checkout with a specific product in their cart or viewed the product within a specified time period. |
| To align with customer expectations, customers will be notified about **any** price drop for the product since they have explicitly subscribed to a markdown alert. | Allows you to customize at what amount or percentage a product's price needs to drop in order to trigger the flow. |
| A customer can subscribe to a markdown alert even if they have purchased a product in the past. | Will not send to anyone who has already purchased the product, regardless of whether they bought it at full price or when it was discounted. |

It is possible to use both flow types simultaneously, though if you feel this will be redundant, you can choose to use the feature which best aligns with your preferred business strategy.

## Additional Resources

- In this course, see how you can [automate the customer journey with flows](https://academy.klaviyo.com/automating-the-customer-journey-with-flows)
- Learn how to create other flows on the Help Center:

- [Welcome series flow](https://help.klaviyo.com/hc/en-us/articles/115002775172-How-to-Create-an-Email-Welcome-Series)
- [Back in stock flow](https://help.klaviyo.com/hc/en-us/articles/115003872251-Building-a-Back-in-Stock-Flow)
- [Upsell or cross-sell flows](https://help.klaviyo.com/hc/en-us/articles/115002775212)
- [Date property-triggered flows](https://help.klaviyo.com/hc/en-us/articles/360002732652)