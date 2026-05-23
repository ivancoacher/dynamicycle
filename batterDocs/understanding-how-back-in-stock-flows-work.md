<h1>Understanding how back in stock flows work</h1>

## You will learn

Learn about how back in stock flows work, how contacts move through them, and how they appear different from most other metric-triggered flows. For instance, they have the back in stock delay component, which is unique to this type of flow.

Klaviyo back in stock is supported for customers using the following:

- [Shopify](https://help.klaviyo.com/hc/en-us/articles/38767539287323)
- [BigCommerce](https://help.klaviyo.com/hc/en-us/articles/38767539287323)
- [Magento 2](https://developers.klaviyo.com/en/docs/how_to_set_up_custom_back_in_stock)
- [PrestaShop](https://help.klaviyo.com/hc/en-us/articles/33059375555099)
- [SFCC](https://help.klaviyo.com/hc/en-us/articles/22495505773083)
- [Shopware](https://help.klaviyo.com/hc/en-us/articles/13325405718939)
- [Custom catalog feeds](https://developers.klaviyo.com/en/docs/how_to_enable_back_in_stock_for_custom_catalog_feeds)
- [API](https://developers.klaviyo.com/en/docs/how_to_set_up_custom_back_in_stock)

If you haven't set up back in stock in your Klaviyo account or store yet, learn [How to build a back in stock flow.](https://klaviyo.zendesk.com/hc/en-us/articles/115003872251)

## Triggering the flow

When a customer subscribes to an out of stock product on your site, you'll see an event tracked on their profile: **Subscribed to Back in Stock.** Those that subscribe to a back in stock alert will automatically enter your flow triggered off this **Subscribed to Back in Stock** event.

## Back in stock delay component

After triggering the flow, you will see the contact added to the ****Waiting**** list of recipients at the back in stock delay component.

To explore who is waiting at this step, click ****View details**** in the **Performance** section of the details sidebar for this delay.

![](https://klaviyo.zendesk.com/hc/article_attachments/47037001826971)

## Sending to back in stock subscribers

When a product comes back into stock, you'll see those waiting on this item move into the **Moved to Next Step** category. Depending on your back in stock settings, some or all of the contacts will receive a message alerting them that the item is available.

Your flow's message status must be set to **Live** or **Manual** for subscribers to be added to the waiting list for the back in stock delay. If the message after the delay is set to **Draft**, no one will be put in the waiting list.

To view recipient activity around your stock alert email or SMS, click on the message itself. Here, in the **Performance** section of the sidebar, you will see a summary of activity over the last 30 days. Click ****View details****to explore activity over a longer, or custom, timeframe.

Note that it's not possible to check if the item is still in stock before sending a second message. After the initial message is sent, Klaviyo cannot check the inventory for the item to see if the item has gone out of stock again.

## Adding past profiles to back in stock flows

Adding past profiles to back in stock flows typically won't bring in new people. Back in stock flows are triggered by the **Subscribed to Back in Stock** metric, and [metric-triggered flows add past profiles based on time delays](https://help.klaviyo.com/hc/en-us/articles/115002779231#metric-triggered-flows2). Since back in stock flows are best without time delays (and the **back in stock** delay functions differently), adding past profiles won't have any effect. If you wish to reach out to those in a back in stock report, we recommend sending a campaign.

That said, if your back in stock flow does contain a time delay, adding past profiles will work similarly to how other metric-triggered flows add past profiles. The only difference is that with back in stock flows, someone in the waiting queue will be notified as soon as the product is back in stock.

## Additional resources

Learn more about back in stock flows:

- [How to create a back in stock flow](https://help.klaviyo.com/hc/en-us/articles/115003872251)
- [How to configure back in stock emails](https://help.klaviyo.com/hc/en-us/articles/360051612751)
- [How to add SMS to a back in stock flow](https://help.klaviyo.com/hc/en-us/articles/7954040204827)

Read about [How contacts move through a flow](https://help.klaviyo.com/hc/en-us/articles/360017706091)
