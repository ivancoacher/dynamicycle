---
id: "360028298592"
title: "How to integrate with ShipStation"
source_url: "https://help.klaviyo.com/hc/en-us/articles/360028298592-How-to-integrate-with-ShipStation"
section: "ShipStation"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:44Z"
language: "en"
---
## You will learn

Learn how to integrate ShipStation with Klaviyo. This integration syncs order creation and shipping status data every 30 minutes from ShipStation. After completing the steps in this article, you'll be able to personalize and target emails based on shipping events and order statuses tracked by ShipStation.

## Before you begin

This integration uses ShipStation's V1 API, which requires either the ShipStation Standard or Premium plan.

## Create an API key and secret in ShipStation

To integrate with Klaviyo, you'll need an API key and secret from ShipStation. You must use ShipStation's V1 API to integrate. API keys and API secrets will only show in ShipStation’s UI when they are generated and only to the user who generated them.

If you already generated and saved a V1 key and secret, you can skip ahead to the next section. If not, create them in ShipStation:

1. In your ShipStation account, select the gear icon to access your account settings.
2. Select ****Account > API Settings****.
3. Select ****V1 API**** from the dropdown and click ****Generate API Key****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/37181395592731)
4. Click the verification link sent by ShipStation to your email address. The **Generate API Key** button will reset once you verify your email. Once it has reset, click ****Generate API Key**** again.
5. Set the expiration (3, 6, or 12 months) for your new API key, then click ****Generate****.
6. Copy your newly generated API key and secret and be sure to store them securely. Note that you will need to rotate your key and update it in Klaviyo once it expires.

Learn more about [API key generation and rotation in ShipStation](https://help.shipstation.com/hc/en-us/articles/360025856212-ShipStation-API#UUID-c3bb4750-8145-1d9c-c8be-e3dd663d2eed_UUID-191ce2ed-16c1-9c98-d1fb-99bbf8bf3c0c).

## Integrate ShipStation with Klaviyo

1. Head over to your Klaviyo account and select the ****Integrations**** tab.
2. Click ****Explore apps**** and search for **ShipStation**, then click the card.
3. Then, click ****Install****.
4. Enter the API key and API secret generated in ShipStation, then click ****Connect to ShipStation****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28720892444955)
5. Review the permissions and click ****Allow****.
6. If your integration was successful, you’ll see a success message.

## Monitor the Klaviyo sync

The ShipStation integration syncs data from all of your ShipStation stores, allowing you to filter segments and flows based on the store name, and automatically syncs the last 90 days of data. After the initial integration is complete, a periodic sync runs every 30 minutes, looking for status updates to create additional events in Klaviyo.

To check on your integration sync:

1. Click the ****Analytics**** dropdown in Klaviyo and select ****Metrics****.
2. Click the ****All Integrations**** dropdown, and select ShipStation.
3. Check to see if ShipStation events are being synced to your Klaviyo account by looking at one of the ShipStation metrics. For instance, **Order Awaiting Shipment**. and clicking on the Activity Feed icon for the metric.
4. If your integration has begun syncing data, you will start to see events being added to this **Activity feed**.

Klaviyo imports all of your ShipStation data. To verify this, compare the number of shipped orders added to Klaviyo on a particular day with the number of orders shipped in ShipStation and confirm they match.

1. In Klaviyo, navigate to ****Analytics > Metrics****, and click into the **Order Shipped** metric.
2. This will take you to the metric chart page which, by default, will show you the last 30 days of data.
3. Hover over yesterday's datapoint or look in the table of data below the chart to see how many payments occurred yesterday and compare it to the data you see in ShipStation.

If the data doesn’t match, the issue is most likely that the timezone in your Klaviyo account doesn't match the timezone in your ShipStation account. To check your timezone setting in Klaviyo:

1. Click your account name in the lower left.
2. Select then clicking ****Settings > Organization****.
3. Scroll down to **Time zone**.

## ShipStation metrics

ShipStation syncs the following metrics to Klaviyo:

- Order Awaiting Shipment
- Order Awaiting Payment
- Order On Hold
- Order Shipped
- Order Cancelled

![mceclip0.png](https://klaviyo.zendesk.com/hc/article_attachments/28720892442907)

For more information on specific order statuses that are tracked in ShipStation, check out [ShipStation's documentation](https://help.shipstation.com/hc/en-us/articles/360025869712).

### Order Awaiting Shipment

This metric is tracked when an order is ready to ship in ShipStation.

### Order Awaiting Payment

This metric is tracked when an order is unpaid and marked as **Awaiting Payment** in ShipStation. Not all stores support unpaid orders. When an order is paid for, either the store will send updated information about the order to ShipStation or you can manually mark the order as paid, and then ShipStation will update the order status to **Order Awaiting Shipment**. This event will then be synced to Klaviyo.

### Order on Hold

This metric is tracked when you use the Hold action in ShipStation to place an order on hold. This is useful for pre-orders, delaying orders with out-of-stock products, or delaying orders for any other reason. Orders can be set to **On Hold** until a set date or after a specified number of days.

### Order Shipped

This metric is tracked once a label is printed for an order, at which time ShipStation moves the order to the **Shipped** status. Orders will move here when an outbound shipping label is generated, but will not receive this status if manually marked as shipped or marked as shipped by a shipping third party.

### Order Cancelled

This metric is tracked when an order is cancelled in ShipStation.

## Outcome

You have completed integrating with ShipStation and have verified your ShipStation data in Klaviyo. Now, you'll be able to personalize and target emails based on shipping events and order statuses tracked by ShipStation.

## Additional resources

- [Getting started with flows](https://help.klaviyo.com/hc/en-us/articles/115002774932)
- [How to create a post purchase flow](https://help.klaviyo.com/hc/en-us/articles/360028872611)