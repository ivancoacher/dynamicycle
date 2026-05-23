<h1>How to create a low inventory flow</h1>

Learn how low inventory flows work and how to set them up in Klaviyo. Note that a low inventory flow does not send to anyone who has already purchased the item within the set timeframe. For low inventory flows, you can use either a catalog from an ecommerce integration or a custom catalog.

Low inventory flows let customers know when products they’ve looked at are low on inventory and likely to sell out. This can mean an easy sale for you, as customers love a deal, especially on items they actually want. These flows are also a valuable tool for marketers, as the messages typically receive high engagement and conversion rates.

## Understand how low inventory works for your integration

Low inventory flows are available for stores using Shopify, BigCommerce, Wix, Magento 2, PrestaShop, Salesforce Commerce Cloud, or a [custom catalog](#h_01K1K6WV5SB3RSJH3JQ2M85QGG). The low inventory trigger supports different metrics depending on the integration and whether or not you select product or variant inventory tracking.

For example, with Shopify, you can set up the flow to trigger when inventory for an entire product is low (e.g., T-shirt) or just a specific variant (e.g., black T-shirt). See the chart below for more information.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Tracking type | Started Checkout | Viewed Product | Added to Cart |
| Shopify | Product | ◉ | ◉ | ◉ |
| Variant | ◉ |  |  |
| BigCommerce | Product | ◉ | ◉ | ◉ |
| Variant | ◉ |  |  |
| Wix | Product | ◉ |  |  |
| Variant | ◉ |  |  |
| Magento 2 | Product | ◉ | ◉ | ◉ |
| Variant | ◉ |  | ◉ |
| PrestaShop | Product | ◉ | ◉ | ◉ |
| Variant | ◉ |  | ◉ |
| Salesforce Commerce Cloud | Product | ◉ | ◉ | ◉ |
| Variant | ◉ |  | ◉ |

## How to trigger a low inventory flow

1. You can adjust it at any point, but it will only apply to events triggered after you change it.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28717391283099)
2. A time delay is not recommended, as you want to inform customers as soon as the stock changes.
3. Be careful about adding additional messages since you don’t know how soon the item will sell out after the first message.

1. Navigate to ****Flows > Create flow > Build your own****.
2. Name your flow and add tags.
3. Click ****Create flow**** to continue.
4. In the flow builder, select ****Low inventory**** from the **All triggers** tab.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28717418530587)
5. Select whether you’d like the trigger to apply to the entire product or specific variants. Note that only certain events may be available for variants and the variant level is not available for all integrations.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28717418522523)
6. Choose when the low inventory flow should trigger; i.e., at what amount a product’s stock is considered low.
7. Adjust the engagement timeframe to exclude people who have already purchased the item within a specified amount of time.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28717391287067)
8. Add a message immediately after the trigger.
9. Click ****Review and turn on**** at the top of the flow builder when you're ready for the flow to start sending.
10. Choose ****Live**** from the dropdown.
11. Click ****Turn on****.

## Use filters in your low inventory flow

You can use trigger and profile filters to restrict when your low inventory flow triggers.

### Trigger filters

You can use trigger filters to limit the low inventory flow to only trigger for certain items or to exclude specific items using either the product's name or ID. You can also include or exclude specific collections, depending on the integration.

For example, if you'd like your flow to trigger for most items, but exclude a specific item, set the trigger filter to **Product ID doesn't equal** followed by the ID for the specific product you want to exclude. It's better to use the ID instead of the product name because product names can change.

![](https://klaviyo.zendesk.com/hc/article_attachments/32374808865819)

You can also exclude entire collections by setting the trigger filter to "****Collections********doesn't equal****" followed by the name of the collection.

![](https://klaviyo.zendesk.com/hc/article_attachments/32374808867611)

### Profile filters

You can use the same profile filters you can use for other types of flows. The most common use cases for using profile filters in a low inventory flow include:

- Limit how often someone can enter the flow within a specified span of time.
  ![](https://klaviyo.zendesk.com/hc/article_attachments/32374798558235)
- Limit the flow to trigger based on purchase history, e.g., returning customers, first time purchasers, non-purchasers, etc.
  ![](https://klaviyo.zendesk.com/hc/article_attachments/32374808871067)
- Limit the flow to trigger based on engagement history.

![](https://klaviyo.zendesk.com/hc/article_attachments/32374798561179)

## Low inventory flows and custom catalogs

Before you can use a custom catalog in a low inventory flow, you must first set up the catalog. If you have not done so, learn [how to sync a custom catalog feed to Klaviyo](https://developers.klaviyo.com/en/docs/guide_to_syncing_a_custom_catalog_feed_to_klaviyo) on the Developer Portal.

Make sure your custom catalog meets the following requirements:

- Products or variants must have inventory fields mapped with data available.
- **Ordered Product** and at least 1 other metric, such as **Viewed Product**, **Started Checkout**, or **Added to Cart**, must have **product ID** and/or **variant ID** fields as part of the event payload, as well as existing instances of these events in your account from your ecommerce integration.

  Even if the catalog contains product variants, these events must include parent product level IDs.

  Please be aware of the following before setting up this feature:
- If you’re using the [Catalogs API](https://developers.klaviyo.com/en/reference/get_catalog_items), your catalog must contain variants, even if the variant is a duplicate of the main product.
- If you are using a custom catalog in addition to a catalog from an ecommerce integration, low inventory flows will only trigger based on one of these catalogs. If you set up your flow to trigger off of your custom catalog, you may contact Klaviyo Support to revert this back to your integration catalog.

### Use a custom catalog in a low inventory flow

- The account which has a custom catalog, if you have multiple accounts
- Event IDs for all metrics used as triggers with product data such as **Ordered Product, Viewed Product, Started Checkout**, and **Added to Cart**
- For each event, the field names for product ID and price
- For **Started Checkout**, the field name for the list that contains the products from the checkout

1. From the main Klaviyo menu, navigate to ****Content > Products**** to confirm that products from your custom catalog have been synced.
2. [Reach out to our support team](https://help.klaviyo.com/hc/en-us/articles/115001002272-How-to-Contact-Support) and request access to the “low inventory trigger for custom catalogs” feature. Make sure to specify the following:
3. Continue to with the instructions above.

## Next steps

- [Upsell or cross-sell flows](https://help.klaviyo.com/hc/en-us/articles/115002775212)
- [Price drop flow](https://help.klaviyo.com/hc/en-us/articles/4404249033755)
- [Date property-triggered flows](https://help.klaviyo.com/hc/en-us/articles/360002732652)

- In this course, see how you can [automate the customer journey with flows](https://academy.klaviyo.com/automating-the-customer-journey-with-flows)
- Learn how to create other flows on the Help Center:
