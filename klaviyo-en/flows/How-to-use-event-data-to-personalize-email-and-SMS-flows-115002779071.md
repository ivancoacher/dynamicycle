---
id: "115002779071"
title: "How to use event data to personalize email and SMS flows"
source_url: "https://help.klaviyo.com/hc/en-us/articles/115002779071-How-to-use-event-data-to-personalize-email-and-SMS-flows"
section: "Add steps or actions to flows"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-05-11T10:59:42Z"
language: "en"
---
## You will learn

Learn what dynamic event data is, when to use it, where to find it, and how to include it in your flow messages. Learn about the different actions your customers take, and how you can use that data for creating personalized messaging flows in Klaviyo. For instance, you could use event data in an abandoned cart flow message to show individuals what product they left behind, an image of the item, and more. This allows for a more personalized experience for the customer, as well as a higher chance of conversion.

## About event variables

When you have an integration with a third-party service or tool, Klaviyo records certain metrics when a customer profile takes an action. What actions Klaviyo tracks depends on your integration, but common ones include **Started****Checkout**, **Placed Order**, and **Viewed Product**. In addition, each metric recorded in Klaviyo includes relevant information about the event, which is called metadata.

For example, when a customer begins to check out, Klaviyo will track this as a **Started****Checkout** event. Klaviyo is periodically sent details from the third-party platform about the item(s) left in the cart, quantity of each item, total, images, etc. In Klaviyo, this data is stored as event variables and includes all of the information associated with an action a specific customer took.

You must have an integration installed for event data to appear. Learn more about [Klaviyo-built integrations](https://help.klaviyo.com/hc/en-us/articles/115000256472) or using [Klaviyo APIs to build a custom integration](https://help.klaviyo.com/hc/en-us/articles/360045726811).

## When you can use event variables

Because event variables are based on a customer’s behavior, they can only be used in metric-triggered flow messages.

List, segment, and date property-triggered flows are not triggered by events, but by information about the customer in their profile. Thus, there are no event variables to pull from and use in a flow email or SMS. Similarly, event variables cannot be used in campaigns, as these are manual, one-time sends and are not based on the action a customer took.

Common examples of metric-triggered flows include:

- [Abandoned cart](https://help.klaviyo.com/hc/en-us/articles/115002779411-Guide-to-Creating-an-Abandoned-Cart-Flow), via the **Started Checkout** or **Added to Cart** metric
- [Post-purchase](https://help.klaviyo.com/hc/en-us/articles/360028872611-Guide-to-Creating-a-Post-Purchase-Flow), via the **Placed Order** metric
- [Product review](https://help.klaviyo.com/hc/en-us/articles/115002779391-Create-a-Product-Review-Flow), via the **Placed Order** metric
- [Browse abandonment](https://help.klaviyo.com/hc/en-us/articles/115002775252-Create-a-Browse-Abandonment-Flow), via the **Viewed Product** metric
- [Winback](https://help.klaviyo.com/hc/en-us/articles/115002775192-Create-a-Winback-Flow), via the **Placed Order** metric

## How to find event variables

### SMS

1. In the flow builder, click the SMS or MMS you want to add an event variable to.
2. Next to **Content**, click ****Edit****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/33627696749595)
3. Here, you can add text, emojis, static or [dynamic images](https://help.klaviyo.com/hc/en-us/articles/1260806102230), and GIFs to your message. You can also insert profile personalization and event variables.
4. To find event variables, click ****Preview & test****. This modal shows the 10 most recent events that you can navigate between (e.g., for a post-purchase flow, the 10 most recent **Placed Order** events will show here).
5. This modal also shows all the associated event variables. To view the variables, open the ****All properties**** menu within the preview modal.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/33627696759835)
6. This dropdown contains information on all of the variables for that event. By clicking any line item, you can automatically copy it to your clipboard, making it easy to add event variables into your message.

### Emails

To add event variables in a flow email:

1. Open the email in the flow editor.
2. Next to **Template**, click ****Edit****.
3. Click ****Preview & test****.
4. Click on a property name from the **Event Properties** menu to copy it.
   ![A user copies an event variable in Klaviyo](https://klaviyo.zendesk.com/hc/article_attachments/28713327618715)
5. Paste the tag into your flow email.

This preview window will show all of the data available for that particular event metric. List entries are numbered starting at 0. For instance, if **{{ event.extra.line\_items.0.product.name }}** is the variable entry for a product, the 0 indicates that it is the first item in the array.

To use event variables, you must copy them exactly. Event variables are case-sensitive, and the slightest deviation from how it appears in the preview window could cause the variable not to work.

## Common examples of event variables

The syntax for different event variables depends on both the integration and event metric. You can see the syntax for all of the available variables for a given event by scrolling through the preview window and clicking on the different entries.

Some common examples of variables by integration are listed below for a **Started Checkout** event. Keep in mind that the exact variable may differ depending on the metric used to trigger the flow.

|  |  |
| --- | --- |
| ****BigCommerce**** | |
| ****Product Name/Title**** | {{ event.extra.line\_items.0.product.name }} |
| ****Product URL**** | {{ event.extra.items.0.product.url }} |
| ****Image**** | {{ event.extra.items.0.product.images.0.src }} |
| ****Price for Product**** | {{ event.extra.line\_items.0.product.price } |
| ****Quantity**** | {{ event.extra.line\_items.0.quantity }} |
| ****Total**** | {{ event.extra.total\_inc\_tax }} |

|  |  |  |
| --- | --- | --- |
|  | ****Magento 1**** | ****Magento 2**** |
| ****Product Name/Title**** | {{ event.extra.line\_items.0.product.name }} | {{ event.extra.line\_items.0.product.name }} |
| ****Product URL**** | {{ event.extra.line\_items.0.product.key }} | {{ event.Items.0.Product.FullURL }} |
| ****Image**** | {{ event.extra.line\_items.0.product.images.0.url }} | {{ event.extra.line\_items.0.product.images.0.url }} |
| ****Price for Product**** | {{ event.extra.items.0.base\_original\_price }} | {{ event.extra.line\_items.0.product.price }} |
| ****Quantity**** | {{ event.extra.line\_items.0.quantity }} | {{ event.extra.line\_items.0.quantity }} |
| ****Total**** | {{ event.extra.base\_grand\_total }} | {{ event.extra.base\_grand\_total }} |

|  |  |
| --- | --- |
| ****Shopify**** | |
| ****Product Name/Title**** | {{ event.extra.line\_items.0.product.title }} |
| ****Product Handle**** | {{ event.extra.line\_items.0.product.handle }} |
| ****Image**** | {{ event.extra.line\_items.0.product.images.0.src }} |
| ****Price for Product**** | {{ event.extra.line\_items.0.line\_price }} |
| ****Quantity**** | {{ event.extra.line\_items.0.quantity }} |
| ****Total**** | {{ event.extra.customer.total\_spent }} |
| ****Shop Currency (base currency of the store)**** | {{ event|lookup:'$currency\_code' }} |
| ****Presentment Currency (currency the customer used)**** | {{ event.extra.presentment\_currency }} |

|  |  |
| --- | --- |
| ****WooCommerce\***** | |
| ****Product Name/Title**** | {{ event.extra.Items.0.Name }} |
| ****Product URL**** | {{ event.extra.Items.0.URL }} |
| ****Image**** | {{ event.extra.Items.0.Images.0.URL }} |
| ****Price for Product**** | {{ event.extra.Items.0.LineTotal }} |
| ****Quantity**** | {{ event.extra.Items.0.Quantity }} |
| ****Total**** | {{ event.extra.Items.0.TotalWithTax }} |

\*You can [rebuild carts from an abandoned cart flow in WooCommerce](https://help.klaviyo.com/hc/en-us/articles/115005255808#rebuilding-carts-from-an-abandoned-cart-flow7) by using the parameter `?wck_rebuild_cart={{ event.extra.CartRebuildKey }}`. Cart rebuilding is also available for Shopify and Magento 1 integrations but is pregenerated in the default abandoned cart flows.

## Event variable arrays (email only)

If you add the variable above to an email, you can pull in the dynamic data for the first item left in the cart. It is similar to going up to a line of people and asking the first person their name. This approach works well if there can only be a single item; however, it is time-consuming for multiple items or when you don’t know how many items someone might add.

Ideally, you would want to use a single command to get all of the event variables for items within a group instantly — like being able to call out “Name” and getting the names of everyone in a long line.

When it comes to a list of event variables, arrays allow you to do just that.

An array occurs when there are multiple entries under one umbrella property (like multiple items in an order). As mentioned above, the first item will have a "0" in the middle or at the end, the next item will have a "1," and so on. Using an array, you can capture information about both the umbrella property (e.g., **Items** or **Collections)** and the individual entries under that property.

In the example below, there are three items in the preview for a **Placed Order** event:

- The variable for the "Sweet Tarts" item is **{{ event.Items.0 }}**
- The variable for the "Runts" item is **{{ event.Items.1 }}**
- The variable for the "Nerds" item is **{{ event.Items.2 }}**

For this example, the event variable array for these items is **event.Items**.

![The data from a basic placed order event in Klaviyo](https://klaviyo.zendesk.com/hc/article_attachments/28713327622811)

## Iterating over dynamic event variables (email only)

There are two different ways of iterating over these or other event variable arrays in emails:

1. ****[The content repeat feature](https://help.klaviyo.com/hc/en-us/articles/115005083467)****
   This feature allows you to add a single block (text, image, etc.) that will automatically repeat itself and iterate over all entries in a property array.
2. ****[A dynamic table](https://help.klaviyo.com/hc/en-us/articles/360032871031)****
   This helps you create a more complex block that loops over all entries for a single variable array.

Note that while you can add dynamic event variables to text messages, you cannot iterate over multiple ones.

## Additional resources

- Find out more about using [message personalization](https://help.klaviyo.com/hc/en-us/articles/115005084927)
- See how to include a [dynamic image in an MMS](https://help.klaviyo.com/hc/en-us/articles/1260806102230)
- Learn how to iterate over an event array:
  - [How to repeat a block based on dynamic data](https://help.klaviyo.com/hc/en-us/articles/115005083467)
  - [How to build dynamic blocks in a flow email](https://help.klaviyo.com/hc/en-us/articles/360032871031)