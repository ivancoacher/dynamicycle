<h1>How to create a replenishment flow</h1>

## You will learn

Learn how to create a replenishment flow that can nurture customers at different points in their lifecycles if you're selling products that your customers purchase repeatedly within a certain timeframe. By reviewing your existing purchase data, you can determine the established buying cycles of your customers and products, then set up a replenishment flow to target purchasers with a friendly and well-timed reminder.

## Flow trigger and filters

For Shopify and BigCommerce integrations, there are pre-built replenishment flows available in the flows library after you've set up and enabled your integration. To view these:

1. Navigate to the ****Flows**** tab.
2. Click ****Create Flow**** to view the flows library.
3. In the **Browse by goal** section, click ****Encourage repeat purchases****or use the search bar to search for "replenishment."

However, as long as you have the **Placed Order** event, you can build this flow from scratch by creating a metric-triggered flow and then using the **Placed Orde**r event. If you're creating a flow for a specific product, you can add a [trigger filter](https://help.klaviyo.com/hc/en-us/articles/115002779051-Flow-Triggers-and-Filters#setting-trigger-filters) that will limit this flow to customers who purchase the product.

![Example trigger filter with configuration 'Items contains Premium Energy Water'](https://klaviyo.zendesk.com/hc/article_attachments/28723519600027)

You'll also want to ensure that customers who make a purchase after entering this flow are removed. The pre-built replenishment flow comes with a [profile filter](https://help.klaviyo.com/hc/en-us/articles/115002779051-Flow-Triggers-and-Filters#setting-flow-filters) that checks before every email sends to ensure that customers have not purchased a product since entering the flow. Make sure you have this profile filter added. If you're limiting your flow to a specific product, you should also limit this filter to the specific product.

![Conditional split that checks if someone has not placed an order for Premium Energy Water since starting the flow](https://klaviyo.zendesk.com/hc/article_attachments/28723507929627)

## Flow timing

Adjust the timing of your first reminder based on your customers' established buying cycles. For example, if you're selling a supplement that comes with a 30 day supply, you'll most likely want to send a reminder email about 25 days after customers enter the flow.

![Placed Order flow trigger with 1 trigger filter and 1 flow filter](https://klaviyo.zendesk.com/hc/article_attachments/28723519607835)

You can experiment with additional reminder emails, but remember not to badger your customers. A good rule of thumb is to send two reminder emails, and then one follow-up after the projected buying cycle has passed that includes an extra incentive like a discount or a coupon.

![Example flow with the first email after 25 days and a second email after 3 days](https://klaviyo.zendesk.com/hc/article_attachments/28723519603995)

## Flow content

You'll want to tailor your content to include product information relevant to the customer's purchase based on your goals. For example, if you're selling a product with a 30 day supply, then you'll want to send content that reminds the customer to purchase this same product again.

![Example replenishment email with the name and image of Premium Energy Water and a Buy Again button link](https://klaviyo.zendesk.com/hc/article_attachments/28723519597211)

You might also want to include suggestions for similar products using a product block. For example, if you're selling coffee beans, a replenishment flow might suggest purchasing a new flavor or a mug.

## Additional resources

- [How to create a product-specific flow](https://help.klaviyo.com/hc/en-us/articles/115002779431)
- [How to use flows to send transactional emails](https://help.klaviyo.com/hc/en-us/articles/360003165732)
