---
id: "115003872251"
title: "How to build a back in stock flow"
source_url: "https://help.klaviyo.com/hc/en-us/articles/115003872251-How-to-build-a-back-in-stock-flow"
section: "Back in stock flows"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-04-21T13:54:15Z"
language: "en"
---
## You will learn

Learn how to build a Klaviyo back in stock flow to alert customers about inventory if you are using the Shopify, BigCommerce, Magento 2, PrestaShop, SFCC, or Shopware platforms, or if you have an inventory-aware catalog synced via custom catalog feed or API.

The **Back in Stock** feature has 2 key components:

1. ****Back in stock flow****When someone subscribes to a restock alert, a **Subscribed to Back in Stock** event will be tracked on their Klaviyo profile. This is the event you will use to trigger your back in stock flow. Shoppers will enter the flow when they subscribe to a restock alert and wait at a back in stock delay until their item of interest is restocked.
2. ****Back in stock form****Once your flow is ready and waiting, you can add the back in stock form to your website. There are 2 types of back in stock forms.
   - The first uses Klaviyo's form builder which is available for Shopify and Bigcommerce.
     - [How to set up a back in stock form for Shopify and BigCommerce.](https://help.klaviyo.com/hc/en-us/articles/38767539287323)
   - The second method requires you to add a back in stock snippet to your store's theme files. This snippet will automatically show a "notify me when available" button when items become sold out. When shoppers click this button, they'll fill out a form and go right into your flow. Instructions for specific platforms are below:
     - [Magento 2](https://developers.klaviyo.com/en/docs/how_to_set_up_custom_back_in_stock)
     - [PrestaShop](https://help.klaviyo.com/hc/en-us/articles/33059375555099)
     - [SFCC](https://help.klaviyo.com/hc/en-us/articles/22495505773083)
     - [Shopware](https://help.klaviyo.com/hc/en-us/articles/13325405718939)
     - [Custom catalog feeds](https://developers.klaviyo.com/en/docs/how_to_enable_back_in_stock_for_custom_catalog_feeds)[API](https://developers.klaviyo.com/en/docs/how_to_set_up_custom_back_in_stock)

Custom metrics cannot be used to trigger a back in stock flow. Only the Klaviyo-specific metric used with one of the listed integrations, a custom catalog, or a back in stock subscription API call can trigger a back in stock flow.

Keep in mind that if you're using Shopify's point-of-sale (POS) hardware and an ecommerce store, the back in stock flow will count all of the inventory in your physical store as well as in your warehouse.

## Flow best practices

There are a couple best practices to keep in mind when using flows:

- Start with pre-built flows from the flows library for templates that implement best practices.
- Keep the flow between 1 to 3 messages to not overload your subscribers.
- [Optimize your sending frequency](https://help.klaviyo.com/hc/en-us/articles/10948996125083) to ensure customers have enough time to check their email.
- Turn on [Smart Sending](https://help.klaviyo.com/hc/en-us/articles/115002779311) for non-essential messages.

If you haven't done so, set up these flows to maximize conversions from your subscribers:

- [Welcome series](https://klaviyo.zendesk.com/hc/en-us/articles/115002775172)
- [Abandoned cart](https://klaviyo.zendesk.com/hc/en-us/articles/115002779411)
- [Browse abandonment](https://klaviyo.zendesk.com/hc/en-us/articles/115002775252)
- [Winback](https://klaviyo.zendesk.com/hc/en-us/articles/115002775192)
- [Review request](https://klaviyo.zendesk.com/hc/en-us/articles/115002779391)
- [Post-purchase](https://klaviyo.zendesk.com/hc/en-us/articles/360028872611)

## Set up a back in stock flow

Klaviyo has pre-built back in stock flows available in the flows library.

1. Navigate to the ****Flows**** tab.
2. Choose ****Create flow****.
3. You can find all loyalty and sales-oriented flows we offer by filtering your view by the following goal: "Remind people to purchase."
   ![The Flows Library screen highlighting the pre-built back in stock flow category.](https://klaviyo.zendesk.com/hc/article_attachments/28720666883739)

You can also easily find these available Back in Stock flows by searching for "back in stock" in the toolbar at the top of the flows library.

After populating any flow in your account from the library, we recommend reviewing all email content and updating the templates to match your brand.

If you'd like to build a back in stock flow from scratch, you can do this as well.

![A Klaviyo email flow sample setup to alerts subscribers if an item is back in stock with an email alert](https://klaviyo.zendesk.com/hc/article_attachments/28720621559067)1. Click  ****Create flow > Build your own****.

2.Once in the flow builder trigger selection, select ****Your metrics****.Choose the Klaviyo-branded metric **Subscribed to Back in Stock**. Do not add any trigger or flow filters, and click ****Save****.

3. The next component you'll want to drag in — directly after the trigger — is the **Back in stock delay**. Recipients that enter your flow will wait at this delay until their item of interest is restocked. After this occurs, they will move on to the next step in your flow (which is typically an email but could be an SMS).

4. Typically, you will only need a single message in this flow as a notification that the item is back. Make sure to [turn Smart Sending off](https://help.klaviyo.com/hc/en-us/articles/115002779311-Smart-Sending-for-Flows#how-to-disable-smart-sending) for this message to ensure everyone gets the alert.

You do not need to add any time delays components to this series, as the back in stock delay will ensure each person that enters your flow waits until the item they subscribed to goes back in stock before moving forward.

## Back in stock flow settings

There are 2 key settings you can adjust regarding your back in stock flow:

- Minimum inventory rules
- Customer notification rules

These can be configured in your Account's settings and work for both email and SMS. Select your account name in the lower left, then click ****Settings > Other > Back in stock settings****.

The **Back in stock settings** tab only appears after at least 1 **Subscribed to Back in Stock** event is recorded in your account.  If you don't see these settings, make sure to trigger an event first.

![](https://klaviyo.zendesk.com/hc/article_attachments/34361520770843)

### Minimum inventory rules

Minimum inventory rules refer to how many items need to be restocked before you notify those who subscribed.

Depending on how you handle restocking when inventory runs out, you may only receive a few products in for a given SKU or variant at a time. If this is the case, you may prefer to have a threshold at which you consider the volume significant enough to let people know the item is back in stock.

### Notification strategy rules

Notification strategy rules have 2 sub-settings that work together to customize how many and how frequently to send back in stock messages. These settings allow you to send restock notifications all at once or in batches. The 2 components that you can configure are:

- ****Customers to notify****This determines how many customers are notified when an item is restocked. If you have a high-demand item, you might receive hundreds of subscriptions when it goes out of stock. If one item is restocked, you don't want to email all of those people for that single item.
- ****Wait time between notifications****This determines how long to wait between batches of emails if you choose to specify the number of emails that are sent out per item that is restocked.

  For example, if an item's inventory of 20 units were restocked, and you set the "customers to notify" to 5, then 5 customers will be notified per unit, resulting in the oldest 100 customers being notified. The flow will then wait based on the "wait time between notifications" setting before sending to next batch of customers based on the remaining inventory.

  Emails will continue to be sent in batches until the existing inventory drops below your account's minimum inventory threshold. If additional items are restocked during the waiting period, additional emails won't be sent until the end of the waiting period. At the end of the waiting period, we will determine how many items are in stock for this item and notify the correct number of subscribers.

## Back in stock reports

Check the back in stock reports page to see activity on your back in stock flow.

1. Click on a back in stock delay component.
2. Click on the ****View back in stock reports**** link in the details sidebar.
   ![Left sidebar inside a back in stock delay component, with the cursor hovering over the link for View Back in Stock Product Request Report](https://klaviyo.zendesk.com/hc/article_attachments/28720621560987)

This page will show the recent back in stock activity, which you can also export to a CSV file.

While not shown on the back in stock reports page, you can [export a CSV file of all currently queued back in stock subscribers](https://help.klaviyo.com/hc/en-us/articles/1260805819449).

You can also subscribe to receive email notifications for this report by clicking the ****Subscribe**** button.

![Klaviyo stock reports modal, with menu options for report to subscribe to, a field for email address, and menus for frequency of delivery](https://klaviyo.zendesk.com/hc/article_attachments/28720621546011)

The ****Scheduled Reports**** tab allows you to adjust which reports you're subscribed to and the settings for each report. You can navigate to this tab by going to ****Account > Settings > More > Back in Stock Reports****.

![View of the Klaviyo Scheduled Reports page showing report name, frequency, and who receives the reports](https://klaviyo.zendesk.com/hc/article_attachments/28720621551899)

## Additional resources

Find other articles on back in stock flows:

- [How to add SMS to a back in stock flow](https://help.klaviyo.com/hc/en-us/articles/7954040204827)
- [How to configure back in stock emails](https://help.klaviyo.com/hc/en-us/articles/360051612751)
- [Understand how back in stock flows work](https://help.klaviyo.com/hc/en-us/articles/360051612551)
- [How to export a list of queued back in stock subscribers](https://help.klaviyo.com/hc/en-us/articles/1260805819449)