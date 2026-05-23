<h1>How to create an abandoned cart flow</h1>

## You will learn

Learn how to set up an abandoned cart flow in Klaviyo in order to increase your ecommerce revenue and personalize communication to your customers.

If you use Shopify or BigCommerce, you might already have abandoned cart emails enabled through your store. Klaviyo allows you much more customization and targeting than your ecommerce platform’s default abandoned cart flow. In Klaviyo, you can fully customize the content of the email and SMS, add multiple messages, and branch the flow based on things like the value of the item in the cart, and much more. You’ll want to turn off any default platform abandoned cart messages to prevent duplicating messages to customers.

![](https://fast.wistia.com/embed/medias/yd4q80uil4/swatch)

Learn more about abandoned cart flows by clicking the questions below:

****What is an abandoned cart flow?****

An abandoned cart flow is a message or sequence of messages sent to someone who added an item to their shopping cart, but failed to complete the purchase. Reminding customers about their cart can greatly prevent lost sales: almost 70% of shopping carts are abandoned on average.

****Why should I use an abandoned cart flow?****

There are a lot of reasons why someone might abandon a cart. Perhaps the customer didn't have their credit card in front of them or wanted to browse your site a bit more before making a decision. Whatever their reason is for leaving mid-checkout, they may still be interested in the product. Reaching out to them can remind or encourage them to continue with their purchase.

### Need assistance with your flow?

If you already have an abandoned cart flow set up and are looking for ways to troubleshoot an issue, learn how to [troubleshoot a metric-triggered flow](https://help.klaviyo.com/hc/en-us/articles/12278373016603?utm_source=abandonedcart&utm_medium=hc&utm_campaign=troubleshooting).

## Before you begin

Because an abandoned cart flow sends messages based on a customer's activity in your store, make sure that you first [integrate your ecommerce platform](https://help.klaviyo.com/hc/en-us/articles/115000256472) with Klaviyo.

#### Understand how your integration syncs

If you’re using an integration besides Shopify or Bigcommerce, we may not sync **Started Checkout** data immediately. You will want to double check how [often data is synced from your ecommerce store to your Klaviyo account](https://help.klaviyo.com/hc/en-us/articles/115005253208-How-Often-Integrations-Sync) to ensure that your first abandoned cart email doesn’t send until after these events are synced.

For example, if you set an abandoned cart email to send 30 minutes after someone abandons a cart, your customer may not receive the first email at exactly 30 minutes. Some integrations sync once every hour. In general, we would not recommend a time delay that short, but if your business needs a short delay, as a best practice, we recommend setting a time delay of at least 1 hour and 15 minutes to accommodate different sync timings.

## Are you using Klaviyo's Amazon Buy with Prime integration?

If you're using Buy with Prime to power payment and fulfillment for any of the products on your store, and you've [integrated Klaviyo and Buy with Prime](https://help.klaviyo.com/hc/en-us/articles/14708088221467), make sure to do the following:

- Create two separate abandoned cart flows: one triggered by your ecommerce platform's checkout event, and one triggered by Buy with Prime's checkout event. To learn how to create your ecommerce platform flow, you should continue following along with this article. For your Buy with Prime flow, read [How to create an abandoned cart flow for Amazon Buy with Prime](https://klaviyo.zendesk.com/hc/en-us/articles/14985388418331).
- When you create your ecommerce platform abandoned cart flow (either pre-built from the flow library, or from scratch) add the following flow filter to exclude customers who made purchases via Buy with Prime from receiving incorrect messaging:
  - **Placed Order** (Buy with Prime) **zero times since starting this flow.**

## Create an abandoned cart flow from the flow library

After you integrate your ecommerce store with Klaviyo, you'll find several best practice flows populated automatically within the [flow library](https://www.klaviyo.com/library/flows), including a pre-built abandoned cart flow.

Depending on your integration, you may see several different types of abandoned cart flows that suit different needs. We recommend choosing one of these pre-built flows to start off, then you can customize the flow to your liking.

Most pre-built abandoned cart flows trigger based on the **Started Checkout** metric, which triggers when someone enters their information at checkout and moves to the next step of the process, but some ecommerce integrations track the **Added to Cart** metric, which triggers when someone adds an item to their cart. If you are using BigCommerce, you will need to [set up this metric manually](https://help.klaviyo.com/hc/en-us/articles/360024310292). For Shopify, you'll need to [check the](https://help.klaviyo.com/hc/en-us/articles/4425956184731#h_01J6F7TREZM0NY2336G80MJFM3) [**Track behavioral events**](https://help.klaviyo.com/hc/en-us/articles/4425956184731#h_01J6F7TREZM0NY2336G80MJFM3) [setting to enable Added to Cart.](https://help.klaviyo.com/hc/en-us/articles/4425956184731#h_01J6F7TREZM0NY2336G80MJFM3) Then, you can use our [pre-built abandoned cart flow triggered by](https://www.klaviyo.com/library/flows?object_id=RwjNFq) [**Added to Cart**](https://www.klaviyo.com/library/flows?object_id=RwjNFq)**.**

****Build an abandoned cart flow yourself****

While it is recommended that you choose a pre-built flow from the flow library, you can also build your own abandoned cart flow from scratch, but you’ll have to manually add the dynamic elements discussed later in this guide. Follow the steps below to create a flow from scratch.

1. Navigate to the ****Flows**** tab.
2. Click the ****Create Flow**** button in the top right.
3. Click ****Build your own**** in the top right.
   ![Create From Scratch button in the top right of the Flow Library](https://klaviyo.zendesk.com/hc/article_attachments/31431676250651)
4. Name your flow "Abandoned Cart" or something similar.
5. Click ****Create flow****.
6. In the flow builder, select ****Metric**** from either the **Recommended** or **All triggers** tab.
   ![List of flow triggers with the Metric option highlighted](https://klaviyo.zendesk.com/hc/article_attachments/31431686971547)
7. Configure and add components to your flow as discussed in the sections below.

#### Set up the flow trigger and filters

The most common type of abandoned cart flow uses the **Started Checkout** event as a trigger. This works by tracking:

1. When someone adds an item to a cart and then proceeds to the checkout page.
   1. The event will trigger once the customer has filled out their contact information and proceeded to the shipping page or the page has been reloaded, depending on the integration. Contact information is required for creating a profile.
2. If someone completes their purchase and places an order.

   If someone adds an item to their shopping cart but does **not** make a purchase, this is considered an abandoned cart. You need to add a filter to prevent people who complete a purchase from continuing into the flow.
3. Click on the trigger.
4. Choose ****Profile Filters****.
5. Click the ****Add a Flow Filter**** button.
6. Choose ****What someone has done (or not done)****.
7. Configure the filter to check for **Person has Placed Order zero times since starting this flow.**

   ![Flow figure configuration set to 'Placed Order zero times since starting this flow'](https://klaviyo.zendesk.com/hc/article_attachments/28715968599579)
8. Click ****Save.****

   This configuration will prevent anyone who places an order before the time delay from continuing into the flow and will also prevent someone from receiving further emails if they place an order after receiving the first email.

   It is important to note that everyone who starts a checkout will enter the flow. If they go on to place an order, they will be skipped for the rest of the flow. For this reason, you will typically see a large number of people who enter the flow being skipped due to "failing profile filters**."** This is actually a good thing and simply means the flow is functioning correctly by not sending abandoned cart emails to people who placed an order.

   Another flow filter you might want to add is **Hasn't been in flow in the last X days**. This will prevent those who recently received your abandoned cart messages from receiving them again within the specified timeframe.
9. Click on the trigger.
10. Choose ****Profile Filters.****
11. Click the ****Add a Flow Filter**** button.
12. Choose ****Has not been in this flow.****
13. Select ********hours********, ********days********, or ********weeks.********
14. Type the amount of time you want to prevent someone from entering the flow again.
    ![Flow filter configuration set to 'Has not been in this flow in the last 7 days'](https://klaviyo.zendesk.com/hc/article_attachments/28715961996827)
15. Click ****Save.****

If you have more than 1 message in your flow, Klaviyo will check your profile filters before each individual email. This means that if someone completes their purchase after the first message, they won't receive any other messages in your flow.

If you have customers from outside the US and in a region with data protection laws, you should consult your legal team before turning your abandoned cart flow live. Check out our guide to [best practices for complying with data privacy laws](https://help.klaviyo.com/hc/en-us/articles/360038973652) for more information.

## Time delays: when to send your messages

Immediately after your flow trigger, include a time delay. You'll want to give customers an adequate amount of time to complete their purchase before determining that they've abandoned their cart and sending them a reminder.

#### Determine your first time delay

Klaviyo's pre-built abandoned cart flows include a 4-hour time delay before sending the first message if the customer does not complete their purchase. We have found that this timing works well for a broad group of customers, but each business is different, so you may find that a different time delay works better for you.

Deciding when to send your first abandoned cart email can be difficult. We recommend sending your first message between 2–4 hours after someone starts a checkout, and then sending a second email 20-48 hours later.

![Example abandoned cart flow with a 2 hour delay before the first message and a 20 hour delay before the second message](https://klaviyo.zendesk.com/hc/article_attachments/28715962023323)

As mentioned, there is no one-size-fits-all rule for the best time to send abandoned cart messages. Timing may vary depending on what you sell. For example, if you sell big-ticket items, like mattresses, the buying process likely requires more consideration than something smaller, like shoes. For this reason, you might find that a longer time delay is more effective. If you email someone too soon after they abandon a cart without giving them the opportunity to finish making a purchase, you can come off as overly pushy.

## Content to include in your abandoned cart flow

Generally speaking, your abandoned cart emails should match the style of your other email templates. If you are using a pre-built flow, [save any blocks](https://help.klaviyo.com/hc/en-us/articles/115005413888) with dynamic content and then modify the template to match your store's branding.

#### Understand the dynamic content block

One of the most compelling aspects of an abandoned cart message is the ability to include information about the item someone abandoned directly in the message. Klaviyo's default abandoned cart flow contains a dynamic content block that is unique to each ecommerce integration. This content block includes the following details about each product:

- Image
- Title
- Quantity
- Price

![View of the default dynamic content block in the email template editor](https://klaviyo.zendesk.com/hc/article_attachments/28715962000795)

The dynamic block is also designed to repeat itself for each item in someone's cart if they have multiple items. A **Return to Cart** button is underneath the content block in pre-built emails that links back to the customer’s cart.

The link used to return to the cart will depend on your integration. Some integrations allow you to rebuild a customer's cart fully no matter which device they click the link from.

See the list below for examples of URLs that use variables to rebuild a customer's cart:

****Shopify****

```
{{ event.extra.checkout_url }}
```

****Magento 2****

```
{{ organization.url }}/reclaim/checkout/cart?quote_id={{ event.Extra.QuoteID }}
```

****Prestashop****

```
{{ event.ReclaimCartUrl }}
```

****WooCommerce****

```
{{ organization.url|trim_slash }}/cart?wck_rebuild_cart={{ event.extra.CartRebuildKey }}
```

****Custom integration****

The URL and whether or not cart rebuilding is possible will depend on how your custom integration was built. Consult with your integration's developer for more information.

****How to edit the dynamic content block****

While it's true that the dynamic content is pulled in automatically for the pre-built abandoned cart flows in Klaviyo, you may want to customize it. Further, if you are building an abandoned cart flow from scratch, you'll have to build a dynamic block yourself. For more details, check out this [article on using dynamic variables to personalize flow messages](https://help.klaviyo.com/hc/en-us/articles/115002779071).

Because these blocks utilize tags that are unique to each integration, it can be challenging to rebuild them on your own. We highly recommend [saving these blocks](https://help.klaviyo.com/hc/en-us/articles/115005413888-Create-and-Manage-Saved-Blocks) before editing the default email or swapping out the template. This way, you can completely customize the design of your email, but don't have to worry about affecting its functionality.

![The save block button found when hovering over a block](https://klaviyo.zendesk.com/hc/article_attachments/28715968605595)

By default, the abandoned cart block will pull in all the items that someone has left in their cart. To change or limit the number of items displayed, you can edit the block.

****How to restore a deleted dynamic content block****

If you accidentally delete either of these dynamic blocks, you can re-add Klaviyo's default abandoned cart flow to your account from the flow library in the **Browse Ideas** tab using the [instructions above on creating an abandoned cart flow.](https://help.klaviyo.com/hc/en-us/articles/115002779411#create-an-abandoned-cart-flow-from-the-flows-library2)

As we mentioned, the core part of Klaviyo's default abandoned cart flow that you will want to keep is the dynamic content. We recommend saving the dynamic content block and button before editing the default template to ensure that you don't overwrite it. Then, if you have a base template that you've already designed for your other emails, you can use this as your abandoned cart template and drag in the dynamic content from the Saved Blocks library.

#### Example message

Below is an example of a well-designed abandoned cart email:

![Example of a well-designed abandoned cart email using a dynamic content block](https://klaviyo.zendesk.com/hc/article_attachments/28715968607515)

Notice that the primary focus of the message is the item that the recipient left in their cart. This dynamic content should be the core of your email template. After all, this is the item that they demonstrated an interest in in the first place.

## Content best practices

#### How many abandoned cart messages to send

Based on research from thousands of Klaviyo ecommerce customers, we have found that sending 2–3 abandoned cart messages in your flow leads to optimal performance. For more information on how we determined this result, check out our [abandoned cart benchmark report](https://www.klaviyo.com/marketing-resources/abandoned-cart-benchmarks#section2).

#### What products to include

In the email, it’s best practice to only include the products that the customer abandoned. It’s not advised to have other products highlighted in the abandoned cart message since your main goal is to drive customers back to their cart to complete their purchase. Including other products can distract from this message and lead to an overall lower conversion rate.

#### What language to use

The language you use in your abandoned cart message should encourage people to reach out if they have questions about your products and inspire a sense of urgency to convince them to complete the purchase. For example, you could lead with "Hurry, before it sells out!"

#### When to include coupons

While it's common to include a discount or incentive in an abandoned cart flow, we don't encourage you to include a coupon in the first email. This can train customers to abandon carts in order to get the discount and is oftentimes unnecessary. If you would like to include an incentive in your abandoned cart flow, it's best to hold off until the final email, or only offer it to people who have never purchased before.

You can set up a conditional split like this:

![](https://klaviyo.zendesk.com/hc/article_attachments/47036846666395)

## ****Use SMS in your abandoned cart flow****

We recommend setting up an email only abandoned cart flow first to make sure everything is set up properly. If you'd like to include SMS in your flow, check out our guide on [how to add SMS to your abandoned cart flow](https://help.klaviyo.com/hc/en-us/articles/9352115400219).

## Set your abandoned cart flow live

Once you're satisfied with your flow's setup, turn it live and it will start sending automatically to eligible contacts.

1. Click the ****Update status**** button in the top right of the flow builder. If you created your flow from scratch and all flow actions are set to ****Draft**** status, the button instead will say ****Review and turn on,**** but it will function the same.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/47036846668443)
2. From the dropdown, choose ****Live**** to allow all messages to send.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/47036846672411)
3. Otherwise, if only part of your flow is ready, you can update the status of individual actions by clicking on the ****status button**** at the bottom of each flow action, as shown below.

![](https://klaviyo.zendesk.com/hc/article_attachments/47036846673435)

As mentioned before, make sure to turn off any abandoned cart messages sent by your ecommerce platform, so that customers are only receiving messages from Klaviyo.
