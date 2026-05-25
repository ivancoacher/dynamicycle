---
id: "12278373016603"
title: "Troubleshooting a metric-triggered flow"
source_url: "https://help.klaviyo.com/hc/en-us/articles/12278373016603-Troubleshooting-a-metric-triggered-flow"
section: "Troubleshooting flows"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-04-21T13:54:26Z"
language: "en"
---
## You will learn

Learn how to troubleshoot a metric-triggered flow when you notice it's behaving differently from expected.

Flows are highly customizable and can vary in complexity. The information in this guide is designed to be broad, and will mainly cover common issues which can apply to most Klaviyo accounts.

Please review the troubleshooting scenarios below to see if any are relevant to your issue before asking for assistance.

### How do I know if my flow is metric-triggered?

Follow these steps to confirm whether your flow is a metric-triggered:

1. Click on the trigger of the flow in the flow builder.
2. View the top section of the sidebar to see if the flow is triggered by a metric and the name of the metric. For metrics triggered by an integration, the icon of the integration will appear next to the name of the metric.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/46898095213339)
3. Click on the name of the metric to view it in the **Metrics** tab.

Common metric-triggered flows:

- Abandoned checkout
- Browse abandonment
- Customer winback
- Order confirmation
- Shipping confirmation
- Winback

## General troubleshooting steps

Click on each section to learn more.

### Use pre-built flows to avoid issues

To avoid issues with common flow types, we recommend creating your first flows using the pre-built templates from our [flows library](https://help.klaviyo.com/hc/en-us/articles/115002774932-Getting-started-with-flows#choose-a-pre-built-flow-from-the-library3) and adjusting the content to match your branding.

### If flow messages are not sending, check the flow status

Make sure your messages are set to **Live** status in order to start sending out to customers. If your messages are set to **Draft** they will not send nor will they queue profiles in a waiting list. If they are set to **Manual** status, the messages will queue profiles, but will not send out the messages until you manually send them.

If your messages are currently or were previously set to **Manual** status, follow these steps to send messages manually:

1. 1. In the **Performance**section of the details sidebar, click ****View details****.
   2. Navigate to ****Recipient activity****> ****Needs Review****.
   3. This will take you to a list of profiles that reached the message in the flow when it was set to **Manual** status.
      1. You can individually preview, send, and/or cancel each email and SMS that requires your review.
      2. If you have a lot of recipients that need review, you can bulk send and cancel messages with the ****Send All**** and ****Cancel All**** buttons, respectively. If you send an email or SMS to a contact who is in Needs Review and no longer meets the filters for the flow, they will be skipped and will not receive the message.
         ![The send all and cancel all buttons within the recipients activity tab](https://klaviyo.zendesk.com/hc/article_attachments/28720895405851)
      3. To send the message automatically moving forward, set it to **Live** status by clicking on the status dropdown for the message in the flow builder.
         ![A flow email item with the dropdown open to set the item to draft, manual, or live mode](https://klaviyo.zendesk.com/hc/article_attachments/28720900727323)

### Check if there is a delay between when an event occurred versus when Klaviyo recorded the metric

When an event occurs on another platform (e.g., Shopify, Magento, a custom integration, etc), it is marked with a timestamp which is sent to Klaviyo. The related metric in Klaviyo will have a separate timestamp marking when Klaviyo received the information. In many cases, these events are sent between platforms in real time, but some integrations sync data via periodic syncs every 30 minutes to 1 hour. [Learn how often specific integrations sync data](https://help.klaviyo.com/hc/en-us/articles/115005253208).

If there is a delay of 6 hours or more between the event's timestamp and Klaviyo's recorded timestamp, the event will not trigger a metric-triggered flow. However, for flows marked as transactional, the delay between timestamps can be up to 7 days.

To check for a delay, follow these steps:

1. If you are having trouble with a specific flow, such as an abandoned cart flow, view the ****Flows**** page to determine which metric triggers the flow, such as **Placed Order.**
2. If you know of a specific profile that is being affected, navigate to the profile page for this profile by searching for their name or email address in the top left search bar of the main Klaviyo interface. Otherwise, if this is a widespread issue, view the profile page of any profile that has triggered the affected metric.
3. In the activity log for the profile, click the action button (3 dots) and ****Activity details**** to the right of the affected metric.
   ![Example of a profile page in Klaviyo.](https://klaviyo.zendesk.com/hc/article_attachments/28720895409819)
4. In the **Activity Details** modal, compare the 2 timestamps which are listed in UTC format (YYYY-MM-DDThh:mmTZD). If there is a 6 hour or more difference between the timestamps, then this indicates there is a sync issue between Klaviyo and the external platform. If the flow message was marked as transactional, look for a delay of 7 days or more.
   ![Timestamps shown on the Activity Details modal.](https://klaviyo.zendesk.com/hc/article_attachments/28720895418779)

In most cases, these types of delays are due to an issue on the external platform's end.

****For stores hosted on paid platforms (Shopify, BigCommerce, Prestashop, etc)****

Check their publicly available status page for information on server outages and downtime. Status pages usually consist of the the service’s main URL with the status subdomain added to beginning such as the examples below:

- <https://status.shopify.com>
- <https://status.bigcommerce.com>
- [http://status.prestashop.com](http://status.prestashop.com/)

****For self-hosted integrations such as (Magento, WooCommerce, custom integrations, etc)****

If you enabled a firewall or security measures such as Sucuri, Cloudflare, or something similar, this may inadvertently block Klaviyo from communicating with your store or rate limit the speed and amount of data that can be synced.

Since Klaviyo uses dynamic IPs, there isn’t a range of IPs available to whitelist. Instead, whitelist Klaviyo’s user agent, which is: ****Klaviyo/1.0****

If you are unsure how to whitelist Klaviyo, please consult the documentation for your security software on how to whitelist a user agent.

If you are using a custom integration, contact the development team of your integration for further assistance.

### For previously working flows, review the flow’s changelog

If your flow was working previously, but you have recently noticed changes in behavior, you should first look at the flow’s changelog. This is especially important for older flows and accounts with multiple users. If you notice that a flow’s behavior has changed after a certain date and time, the changelog will be able to tell you the following:

- What changed
- Who made the change
- When the change took place (date and time in your account’s timezone)

If changes coincide with when you started experiencing issues with your flow, it is likely that the change is the source of the issue.

Follow these steps to view a flow’s history:

1. In the header bar, click on the ****View flow history****icon button.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/46898125312155)
2. Selecting ****View flow history**** will open the Flow history panel on the right-hand side of the screen.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/46898125315355)

Find out more about the Flow History panel in our article on [how to review the changelog for a flow](https://help.klaviyo.com/hc/en-us/articles/4402385748635).

## Abandonment flow scenarios

Examples: abandoned cart, abandoned checkout, browse abandonment, etc.

Click on the scenario that best fits your issue.

### A lot of profiles are being skipped from abandonment flows

You may notice that the messages in your abandonment flows are showing a lot of skipped profiles. This is normal (and correct) for abandonment flows.

How an abandonment flow works is that everyone who triggers the flow’s trigger metric will enter the flow, and the flow filters will skip people who no longer abandoned their browsing or cart. See the explanations below:

- ****Browse abandonment****
  Triggered by the **Viewed Product** event and will skip people who trigger **Started Checkout**

- ****Abandoned cart (default)****
  Triggered by the **Started Checkout** event and will skip people who trigger **Placed Order**

- ****Abandoned cart (alternate)****
  Triggered by the **Added to Cart** event and will skip people who trigger **Placed Order**

If you still believe there is an issue with the skipped profiles, check the following:

****Confirm that the skips are caused by the correct filters.****

1. In the flow builder, click on a message in your flow.
2. In the sidebar, click ****View details**** in the **Performance**section of the sidebar.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/46898095220635)
3. Click on the **Recipient activity** tab.
4. Click the ****Skipped**** tab.
   ![Skipped reason dropdown found in the Recipient Activity tab.](https://klaviyo.zendesk.com/hc/article_attachments/28720895411739)
5. If most of the skipped profiles are skipped due to **Fails Flow Filters**, this is normal. If you are concerned about other skipped reasons, find out more about the other skipped reasons in our article on [understanding the skipped reason for a flow message](https://help.klaviyo.com/hc/en-us/articles/1260805003210-Understanding-the-skipped-reason-for-a-flow-message).
6. You can click ****Skipped: Fails Flow Filters**** to see the profiles that are being skipped.

****Check that the filters are set up correctly****

1. Click on the trigger of the flow in the flow builder.
2. Click ****Flow Filters**** in the sidebar.
3. Make sure that the flow filters match the configuration below:
   ****Browse abandonment****
   ![Flow filter with the configuration 'Checkout Started zero times since starting this flow.'](https://klaviyo.zendesk.com/hc/article_attachments/28720900690459)
   ****Abandoned cart****
   ****![Flow filter with the configuration 'Placed Order zero times since starting this flow.'](https://klaviyo.zendesk.com/hc/article_attachments/28720900692891)****
4. Change the flow filters to match the examples above if necessary and remove any contradicting flow filters.
5. If you have any additional filters, such as those that prevent someone from entering the flow again within a certain timespan, make sure they are configured the way you intend.
   ****![Flow filter with the configuration 'Has not been in this flow in the last 3 days.'](https://klaviyo.zendesk.com/hc/article_attachments/28720900694683)****

### Browse abandonment flow is not sending

The browse abandonment flow triggers based on the **Viewed Product** event metric and has filters to remove someone from the flow if they start checkout or place an order. If you notice that this flow is not sending, check the following:

****Check that the**** ******Viewed Product****** ****metric is being recorded.****

1. Click on the trigger of the flow in the flow builder.
2. Click on the metric namein the **Trigger** section of the sidebar.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/46898095221787)
3. This will take you to the analytics page for the **Viewed Product** event metric. You can hover over the activity chart or click the ****Activity Feed**** tag to see the last time that the metric triggered.
   ![Viewed Product analytics chart showing recent activity.](https://klaviyo.zendesk.com/hc/article_attachments/28720895364251)
4. If the **Viewed Product** metric is not being recorded in your account, please see our guide on [troubleshooting Viewed Product tracking](https://help.klaviyo.com/hc/en-us/articles/4416172774939-Troubleshooting-Viewed-Product-tracking). If the metric is being recorded, move onto the next step.

****Check that the flow filters are set up as you intended.****

1. Click on the trigger of the flow in the flow builder.
2. Click ****Flow Filters**** in the sidebar.
3. Make sure that the flow filters match the configuration below:
   ![Flow filters with the configuration 'Started Checkout zero times since starting this flow' and 'Placed Order zero times since starting this flow.'](https://klaviyo.zendesk.com/hc/article_attachments/28720895367579)
4. Change the flow filters to match the examples above if necessary and remove any contradicting flow filters.
5. If you have any additional filters, such as those that prevent someone from entering the flow again within a certain timespan, make sure they are configured the way you intend.
   ****![Flow filter with the configuration 'Has not been in this flow in the last 3 days.'](https://klaviyo.zendesk.com/hc/article_attachments/28720900694683)****

### Profiles are still receiving abandoned cart emails after placing an order

The filters of an abandonment cart flow are designed to remove someone from the flow if they place an order, since this means they converted and thus didn’t abandon their cart or browsing. If your customers are not being removed properly after placing an order, check the following:

****Check that**** ******Placed Order****** ****events are being recorded by your account.****

1. Go to the [Metrics tab](https://www.klaviyo.com/analytics/metrics) in Klaviyo.
2. Click on ****Placed Order.****
3. Hover over the activity chart or click the ****Activity Feed**** tag to see the last time that the metric triggered.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28720895422619)

If the **Placed Order** metric is not being recorded in your account, please see our guide on [troubleshooting Placed Order tracking](https://help.klaviyo.com/hc/en-us/articles/7000906101019-Troubleshooting-Placed-Order-tracking).

If the **Placed Order** metric is being recorded, check for a delay between when the event was triggered by your ecommerce platform and when it was recorded by Klaviyo. If the **Started Checkout**event triggered, but the **Placed Order** event was delayed, someone may receive emails from the abandoned cart flow. You can check for this by doing the following:

1. Navigate to the profile page of an affected person, someone who you know has received an abandoned cart email despite placing an order before the time delay configured in your flow.
2. Click on the timestamp of the **Placed Order** event in their activity feed.
3. In the **Activity Details** modal, view the 2 timestamps listed at the top.

****Check the flow filters****

1. Click on the trigger of the flow in the flow builder.
2. Click ****Flow Filters**** in the sidebar.
3. Make sure that the flow filters match the configuration below:
   ![Flow filter with configuration 'Placed Order zero times since starting this flow'.](https://klaviyo.zendesk.com/hc/article_attachments/28720900708635)
4. If you have any additional filters, such as those that prevent someone from entering the flow again within a certain timespan, make sure they are configured the way you intend.

****If you are using Shopify draft orders, add a trigger filter.****
Shopify draft orders trigger a **Started Checkout** event, but do not trigger a **Placed Order** event, so you will need to add a trigger filter in order to prevent these types of orders from triggering your abandoned cart flow. Draft orders do not contain a normal list of items, but instead contain a single item named “Amount to pay for order” followed by an order number.
![Checkout Started feed showing events with draft order items listed as 'Amount to pay for order...'.](https://klaviyo.zendesk.com/hc/article_attachments/28720900710939)
To exclude these orders from your abandoned cart flow, follow these steps:

1. Click on the trigger of the flow in the flow builder.
2. Click ****Trigger Filters**** in the sidebar.
3. Click ****Add a Trigger Filter**** to create a new filter if there are none. Otherwise, click ****AND**** to add an additional filter.
4. Set the filter’s **Type** to “Text”
5. Adjust the trigger filter so that it matches the configuration below:
   ![Trigger filter with configuration: Items doesn't contain 'Amount to pay for order'.](https://klaviyo.zendesk.com/hc/article_attachments/28720895383195)

## Post-purchase flow scenarios

Examples: order confirmation, shipping confirmation, product review, thank you, cross-sell, etc.

Click on the scenario that best fits your issue.

### Post-purchase flow is not sending to anyone

If your flow is configured to trigger on the **Placed Order** or **Fulfilled Order** event, but has not been sending, check the following:

****Understand the difference between Placed Order or Fulfilled Order.****
Depending on if a flow is triggered by **Placed Order** or **Fulfilled** order, there are different possible issues and fixes, so it is important to understand the difference. While there are differences between various ecommerce integrations, in general they work as follows:

- The **Placed Order** metric triggers after an order has been created in your ecommerce store.
- The **Fulfilled Order** metric triggers after an order has a status equivalent to “shipped” for physical orders or “completed” for digital orders in your ecommerce platform.

****Make sure that the**** ******Placed Order****** ****or**** ******Fulfilled Order****** ****metric is being recorded properly.****

1. Click on the trigger of the flow in the flow builder.
2. Click on the metric namein the **Trigger** section of the sidebar.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/46898095224347)
3. Hover over the activity chart or click the ****Activity Feed**** tag to see the last time that the metric triggered.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28720900786843)
4. ![Placed Order analytics chart showing recent activity.](https://klaviyo.zendesk.com/hc/article_attachments/28720900700699)
5. If the **Placed Order** metric is not being recorded in your account, please see our guide on [troubleshooting Placed Order tracking](https://help.klaviyo.com/hc/en-us/articles/7000906101019-Troubleshooting-Placed-Order-tracking). If the metric is being recorded, move onto the next step.

****If you have changed ecommerce integrations, make sure you have changed the flow trigger.****
When you migrate ecommerce platforms, make sure to switch the metrics used for your flows and analytics to the metrics for your new ecommerce platform. For example, if you were to switch from BigCommerce to Shopify, your account’s analytics and flows may still be set to use BigCommerce’s **Placed Order** metric rather than Shopify’s **Placed Order** metric. See our guide on [how to change a flow trigger](https://help.klaviyo.com/hc/en-us/articles/115002775052-How-to-change-a-flow-trigger).

### Flow filters are not excluding profiles properly

If you are using flow filters to exclude specific profiles from triggering a post-purchase flow, but these profiles are still going through the flow, check the following:

****Preview the trigger to see why profiles are passing the filter.****

1. Click on the trigger of the flow in the flow builder.
2. Click ****Preview**** in the sidebar.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/46898125320731)
3. The trigger preview will show whether or not recent profiles are passing the flow filters and why.
4. If profiles are passing the filters when they shouldn’t be, this preview will show you which filters they are passing.

****Check that the filters are set up as you intended.****

1. Click on the trigger of the flow in the flow builder.
2. Click ****Flow Filters**** in the sidebar.
3. Make sure the configuration of each filter matches what you intended. For example, if you wish to **exclude** profiles from the flow if they match a specific condition, use filters using terms like “doesn’t equal”, “doesn’t contain”, or “zero times”.

****Check the connectors between filters.****
If you are trying to exclude certain people (such as using "doesn't contain") you want to use AND connectors. With an AND connector, someone must match **both** filters. If you use OR connectors, a profile only needs to match one **or** the other filter.

See the example below:

![Two flow filters connected by an OR connector.](https://klaviyo.zendesk.com/hc/article_attachments/28720900717211)

If a person’s recorded country is the United States, they fail the first filter. but if Shopify Tags doesn't contain "US", then they pass the second part of the filter and they will enter the flow. To cover both scenarios you need to connect them with AND.

1. Delete the second filter by clicking the trash can button in the bottom right.
2. Click ****AND**** to add an AND connector and a new filter.
3. Recreate your previous filter.
   ![Two flow filters connected by an AND connector.](https://klaviyo.zendesk.com/hc/article_attachments/28720895389979)

Please see this guide from our Help Center for a more detailed explanation: [AND vs. OR Guide](https://help.klaviyo.com/hc/en-us/articles/360036534631-AND-vs-OR-Guide?source=search&auth_token=eyJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50X2lkIjoxNjE0NDE0LCJ1c2VyX2lkIjo0MDAzMDM2MzkzMzEsInRpY2tldF9pZCI6NTg4MTQ5LCJjaGFubmVsX2lkIjo2MywidHlwZSI6IlNFQVJDSCIsImV4cCI6MTYyNTc4MTA1OX0.ACc0CMAWZOV8TJ4Y2R25fisA0NWiSOMv8kAHebm6Xu0)

### Trigger filters are not excluding items properly

If you are using trigger filters to exclude events with specific items from triggering a post purchase flow, but these filters are not excluding events properly, check the following:

****Preview the trigger to see why profiles are passing the filter.****

1. Click on the trigger of the flow in the flow builder.
2. Click ****Preview**** in the sidebar.![](https://klaviyo.zendesk.com/hc/article_attachments/46898125320731)
3. The trigger preview will show whether or not recent profiles are passing the flow filters and why.
4. If profiles are passing the filters when they shouldn’t be, this preview will show you which filters they are passing.

****Check that the name of the item or collection is up-to-date.****
If you have changed the name of the item or collection (referred to as “category” by some integrations), you need to update the name in the filter configuration. To check if the name of the item has changed, follow these steps:

1. From the main Klaviyo sidebar, click ****Products**** to view your [product catalog](https://www.klaviyo.com/catalog/items).
2. Search for the name of the item you want to exclude by its name or ID.
3. Click on the name of the item to view its collection or category.
4. After confirming the name of the item or collection, navigate back to your flow in the flow builder.
5. Click on the trigger of the flow in the flow builder.
6. Click ****Trigger Filters**** in the sidebar.
7. Adjust the item or collection used in the sidebar to match the new name of the item or collection.

****Check the type of filter.****
Orders can contain multiple items and collections. Filters must use the type “List” in order to check for a specific entry within the list of items or collections.

Check that your filters are using the “List” type and the configuration “contains” or “doesn’t contain” in order to include or exclude specific items or collections.

![Filter type set to List.](https://klaviyo.zendesk.com/hc/article_attachments/28720895352603)

In the example above, if you were to use the configuration “doesn’t equal,” the filter will only exclude orders where “New Items” is the only collection. Since orders can contain multiple collections, you need to use “doesn’t contain” to properly exclude orders that contain “New Items” alongside other collections.

****Check the connectors between filters.****
If you are trying to exclude certain people (such as using "doesn't contain"), use AND connectors. If you use OR connectors, then a profile only needs to match one **or** the other filter. In other words, the profile might not match the first "doesn't contain" filter, but it does match the rest so it will trigger the flow. If you use an AND connector, then the event needs to match both filters.

See the example below:

Say you set up conditions like in the example below. If a person’s order contains the collection “New Items,” then they fail the first filter but if the item list also doesn't contain "T-Shirt," then they pass the second part of the filter and they will enter the flow. To cover both scenarios, you need to connect them with AND.

![Two trigger filters connected by an AND connector.](https://klaviyo.zendesk.com/hc/article_attachments/28720895344923)

To fix this:

1. Delete the second filter by clicking the trash can button in the bottom right.
2. Click ****AND**** to add an AND connector and a new filter.
3. Recreate your previous filter.
   ![Two trigger filters connected by an OR connector.](https://klaviyo.zendesk.com/hc/article_attachments/28720900686107)

Please see this guide from our Help Center for a more detailed explanation: [AND vs. OR Guide](https://help.klaviyo.com/hc/en-us/articles/360036534631-AND-vs-OR-Guide?source=search&auth_token=eyJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50X2lkIjoxNjE0NDE0LCJ1c2VyX2lkIjo0MDAzMDM2MzkzMzEsInRpY2tldF9pZCI6NTg4MTQ5LCJjaGFubmVsX2lkIjo2MywidHlwZSI6IlNFQVJDSCIsImV4cCI6MTYyNTc4MTA1OX0.ACc0CMAWZOV8TJ4Y2R25fisA0NWiSOMv8kAHebm6Xu0)

## Contact Klaviyo support

If you are still encountering issues after consulting this article and reviewing your flow’s history, please [create a post in our Community forums](https://community.klaviyo.com/got-a-question-1) or [reach out to our support team](https://help.klaviyo.com/hc/en-us/articles/115001002272-How-to-Contact-Support).