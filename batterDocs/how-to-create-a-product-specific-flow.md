<h1>How to create a product-specific flow</h1>

## You will learn

Learn how to create several types of product-specific flows. You must have metrics in your account in order to split or filter by a product. If there's no metrics, the dimension fields will not populate any products.

When setting up an abandoned cart, browse abandonment, or post-purchase flow, you may want to filter or split your flow based on the specific item someone left in their cart, viewed, or purchased. This can be useful if you want to offer instructions or messaging around a specific product or products.

This practice works best if you only offer a handful of products and would like to offer very tailored information on each (or only one) of them. This can also be a useful technique if you would like to target people who are purchasing specific items together and tailor the post-purchase experience to this combination of products.

## Filter or split a flow based on one specific product

### Post-purchase

In our post-purchase flow example, let's say that we just released a new product (a lip balm) and would like to reach out to customers who bought this item to provide feedback. Keep in mind that the trigger filters and splits available for you to use will depend on the event that triggers the flow in the first place. Not all flow triggers will be filterable by product.

In this example, our flow will be triggered by placing an order. Then, we're going to want to get more granular and identify the specific item someone bought.

To configure this, we'll need the following flow trigger and trigger split conditions:

- ****Trigger:**** Placed Order
- ****Trigger Split Filter 1:**** Item Count equals "1"
  AND
- ****Trigger Split Filter 2:****Items contains "lip balm"

We only want to identify customers who bought one item because we want to assume that the lip balm is the only item they purchased. If we would like to target anyone who bought lip balm, regardless of whether or not they bought something else, we can remove this filter.

![Trigger Split with configuration 'Items contains lip balm' before the first email](https://klaviyo.zendesk.com/hc/article_attachments/28723517398939)

You can use this configuration as a trigger filter as well in case you would like to create entirely separate flows for whenever someone purchases a specific product (and only that product).

![Trigger Setup menu with trigger filter 'Items contains lip balm'](https://klaviyo.zendesk.com/hc/article_attachments/28723505746843)

### Browse abandonment

In our browse abandonment flow example, let’s say you want to offer a discount to only those who view the product with the highest margin or price (matte gloss). Select a browse abandonment flow from the Flow Library and then add a trigger split.

To configure this split, we’ll need the following flow trigger and trigger split conditions:

- ****Trigger****: Viewed Product
- ****Profile Filter****: Placed Order zero times since starting this flow
  AND
- ****Profile Filter****: Started Checkout zero times since starting this flow
- ****Profile Filter****: Has not been in flow in the last 30 days
- ****Trigger Split Filter 1****: Name contains “matte gloss”

![Trigger split with configuration 'Name contains matte gloss'](https://klaviyo.zendesk.com/hc/article_attachments/28723517406747)

### Abandoned cart

In our abandoned cart flow example, let's say we have excess inventory and want to offer shoppers a discount to buy a specific product (matte gloss), but only that product. We're going to start with the default abandoned cart flow and then drag in a Trigger Split to isolate this specific item.

To configure this, we'll need the following Flow Trigger and Trigger Split conditions:

- ****Trigger:**** Started Checkout
- ****Profile Filter:**** Placed Order zero times since starting this flow
- ****Trigger Split Filter 1:**** Items contains "matte gloss"
  AND
- ****Trigger Split Filter 2:**** Item Count equals "1"

![Trigger split with configuration 'Items contains matte gloss AND Item Count equals 1'](https://klaviyo.zendesk.com/hc/article_attachments/28723505753755)

## Filter or split a flow based on a combination of products

There may be cases in which you would like to filter or split your flow based on a combination of products. Let's say that we'd like to offer specific advice to people who buy two items at the same time (a lip balm and a certain lip gloss). To configure this, we'd follow the same steps as above, but change the following:

- ****Flow Trigger:****Placed Order
- ****Trigger Split Filter 1:**** Items contains "lip balm"
  AND
- ****Trigger Split Filter 2:**** Items contains "matte gloss
  AND
- ****Trigger Filter 3:**** Item Count equals "2"

![Trigger split with configuration 'Item Count equals 2 AND Items contains lip balm AND Items contains matte gloss'](https://klaviyo.zendesk.com/hc/article_attachments/28723517413403)

## Additional resources

Learn how to create different types of flows:

- [How to create a post-purchase flow](https://klaviyo.zendesk.com/hc/en-us/articles/360028872611)
- [How to create a browse abandonment flow](https://klaviyo.zendesk.com/hc/en-us/articles/115002775252)
- [How to create an abandoned cart flow](https://klaviyo.zendesk.com/hc/en-us/articles/115002779411)

Learn more about trigger filters and splits:

- [Understand flow triggers and filters](https://help.klaviyo.com/hc/en-us/articles/115002779051)
- [How to add a trigger split to a flow](https://help.klaviyo.com/hc/en-us/articles/115003885632)
- [Understand flow branching](https://help.klaviyo.com/hc/en-us/articles/115003883992)

See how to [create a upsell or cross-sell flow](https://help.klaviyo.com/hc/en-us/articles/115002775212)
