---
id: "115002775192"
title: "How to create a winback flow"
source_url: "https://help.klaviyo.com/hc/en-us/articles/115002775192-How-to-create-a-winback-flow"
section: "Lifecycle flows"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-04-21T13:54:13Z"
language: "en"
---
## You will learn

Learn how to create a series of emails sent to customers who previously engaged with your brand, but have not interacted with you for a certain period of time. A winback flow is an essential part of customer retention and lifecycle marketing, and not having one is leaving money on the table. On average, it is [five times more expensive to acquire a new customer](https://www.invespcro.com/blog/customer-acquisition-retention/) than it is to retain existing customers and encourage repeat orders.

One of the main points to consider with a winback flow is when the initial email should go out. Most customers wait between purchases, but the length of a typical buying cycle depends on your industry and the products you sell. For instance, a company that sells couches will have a much longer buying cycle than one that sells shampoo. The flow should only target those who have not engaged with you for longer than your business's average buying cycle.

In this guide, we will discuss best practices for creating a winback flow.

![](https://fast.wistia.com/embed/medias/a35xhq2nh5/swatch)

## Understand your products and customers

Before you begin creating your winback flow, you should understand the typical buying cycle for your customers. If you meet the qualifications for [Klaviyo's predictive analytics](https://help.klaviyo.com/hc/en-us/articles/360020919731-Guide-to-Klaviyo-s-Predictive-Analytics) feature, you can easily get this information for customer segments.

![Predictive Analytics graph with Historic CLV on the left and Predictive CLV on the right](https://klaviyo.zendesk.com/hc/article_attachments/28716052045595)

To get the average buying cycle for your repeat customers:

1. Create a segment of everyone who has made at least 2 purchases in the last 2 years using the definition ****What someone has done (or not done)****> ****Placed Order**** > ****is at least 2**** > ****over all time****.
2. Export this segment into a CSV file and average the **Average Time Between Orders** column.

If predictive analytics is not yet available for your customer profiles, get into the mindset of your customers by asking yourself the following questions:

- When would you want to order next?
- When would you need more of the product?

For instance, would you want more of the item before it’s used up, or could you go without for a certain period of time? If conditioner is the product, you’d likely want more as soon as it starts to get too low, and you would need it very soon after it runs out.

Answering these questions helps you determine your customers' purchasing time frame.

## Are you using Amazon Buy with Prime?

If you're using Buy with Prime to power payment and fulfillment for any of the products on your store, make sure to do the following:

- [Integrate Buy with Prime with Klaviyo](https://klaviyo.zendesk.com/hc/en-us/articles/14708088221467) to bring Buy with Prime data into your Klaviyo account.
- Create two separate winback flows: one triggered by your ecommerce platform's **Placed Order** event, and one triggered by Buy with Prime's **Placed Order** event in order to account for customers who placed their original order with Buy with Prime. To learn how to create your ecommerce platform winback flow, you should continue following along with this article. For your Buy with Prime winback flow, read [How to create a winback flow for Amazon Buy with Prime](https://klaviyo.zendesk.com/hc/en-us/articles/15156331062171).
- When you create your ecommerce platform winback flow (either pre-built from the flows library, or from scratch) add the following profile filter to exclude customers who made purchases via Buy with Prime from receiving incorrect messaging:
  - **Placed Order** (Buy with Prime) **zero times since starting this flow.**

## Setting up your winback flow

If you have an ecommerce integration, a winback flow is autopopulated in your account. You can use this flow, or delete it if you prefer to use one of the default winback flows from the Flow Library.

It is also quite simple to build your own winback flow.

1. In your Klaviyo account, head to the Flows tab on the left-hand side.
2. Click the ****Create Flow****.
3. Click ****Create From Scratch****.![Create From Scratch button found in the upper right of the Flows tab](https://klaviyo.zendesk.com/hc/article_attachments/28716062387483)
   A popup window will appear where you can name your flow and select any tags you want it to have.
4. When you’re ready, select ****Create Flow****.
5. For the flow trigger, choose ****All triggers >**** ****Metric > Placed Order****.
6. Add a profile filter that details **Placed Order zero times since starting this flow**.
   ![New flow with the Placed Order event chosen as the trigger option in the left sidebar](https://klaviyo.zendesk.com/hc/article_attachments/28716052036763)
7. Click ****Save****.
8. Drag in your initial time delay and set it to be a little longer than your business's average buying cycle to give your customers some leeway time.
9. Craft your email content. Below, we go over best practices for what to (and not to) include.

## Creating winback content

Winback flow emails encourage lapsed customers to re-engage with your brand. Offering discounts is one way to accomplish this, but the copy of the emails should also strike the right tone and provide the right content.

Best practices include:

- Let customers know you noticed they left
- Make it personal via template tags
- Tell customers about the latest updates (e.g., new products)
- Include an incentive or discount
- Create a sense of urgency (e.g., put a time cap on the incentive you're offering)
- Prompt anyone who’s uninterested to unsubscribe/change their preferences
- Avoid overloading customers with too many emails
- Make each email as engaging as possible
- Craft an interesting subject line and customize your preview text
- Make your content look visually interesting

We recommend keeping your winback flow to three emails per recipient and considering the following best-practice pattern:

![Example winback flow with Placed Order trigger and 180 time delay before the first email](https://klaviyo.zendesk.com/hc/article_attachments/28716052039707)

### Email #1

The first email in this series should be a light touchpoint and the shortest of the sequence. Include a select few products, three to six of either your best-selling products or latest releases. In addition, it is a good idea to offer an incentive to your lapsed customers.

Below, you can see an example that uses a Product Block component to display four of the best-selling products.

You can change the number of items shown as well as the rows and columns on the left-hand side.

![Product_block_for_winback_flow.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28716062402331)

In addition, you can choose to populate the products from a certain feed, or select specific ones from your catalog by clicking ****Static > Add Products****. For the latter approach, pick your products and click ****Add Products****.

### Email #2

The second email should act as a reminder to your customers about the incentive from the first email as well as a sense of urgency (e.g., by setting an expiration date on the discount). In this email, add different products from your first email — if you previously included some of your best-selling products, then add some of your newest releases.

This email can also be longer than your first one, giving you the opportunity to provide more detail. Make yourself and the email as engaging as possible. To grab the reader's attention, you can show an image of your employees to make the company seem more human and your message more personal. Another option is designing the email to portray your information in an easy-to-read and visually interesting way. This email from Ballard Designs shows one example.

![Example of a winback email with multiple pictures linking to different parts of the store's website](https://klaviyo.zendesk.com/hc/article_attachments/28716062392347)

### Email #3

For your third email, you want to have a final call to action for customers to either re-engage, change their email preferences, or unsubscribe. Remind your audience that this is the last chance to take your offer.

In addition, include a prominent unsubscribe link. Having one is both a legal requirement and the best way to prevent unengaged subscribers from hurting your deliverability — it is always better for someone to unsubscribe than it is for them to not engage with your messages or mark it as spam.

![Example of winback email offering 15% off coupon and call to action button](https://klaviyo.zendesk.com/hc/article_attachments/28716062399003)

## Optimizing your flow

You may find it helpful to create different winback flows for different types of customers. For example, you might want to have a special winback flow for your VIP customers, or customers who have spent X amount of money at your store. Additionally, you can create separate branches within the same flow using any of the below properties in a [trigger split](https://help.klaviyo.com/hc/en-us/articles/115003885632-Add-a-Trigger-Split). Here are a few additional filters you can add:

- Customers who have spent X amount of money over Y amount of time
- Customers who have made X number of purchases over Y amount of time
- Customers who have been active on your site X number of days ago
- Customers who have opened an email X number of days ago

Apple Mail Privacy Protection (MPP), which was released with iOS15 and updates to other Apple devices, may lead to inflated open rates due to changes in how we receive open rate data.

If you are triggering flows off of opens themselves, we suggest creating a [custom report](https://help.klaviyo.com/hc/en-us/articles/4416803987739) that includes an MPP property to review these affected opens. You can also identify these opens in your individual [subscriber segments](https://help.klaviyo.com/hc/en-us/articles/4416791883163).

Another option is to split your flow or create separate flows for different categories of products, as with the example below. If any of your items are replenishable with a set buying cycle, you may want to exclude them from your winback flow and instead create a separate [replenishment flow](https://help.klaviyo.com/hc/en-us/articles/360003195232-Create-a-Replenishment-Flow) for them.

![Example winback flow with 2 trigger splits that filter for Lip Balm and Matte Gloss](https://klaviyo.zendesk.com/hc/article_attachments/28716062419995)

To find the best timings, subject lines, and content, it’s important to test them one-by-one. Conditional splits and A/B testing enable you to optimize these factors and personalize the flow for your particular audience.

For instance, try splitting your flow based on whether recipients have recently opened and clicked an email or SMS message. Then, you can change the timings between emails or the email content based on this information. For instance, you could change the timings between emails to be slightly shorter for those who have engaged more recently, comparing their performance to the rest of your flow’s recipients. Alternatively, you may want to test if sending fewer messages is more effective for subscribers who have opened or clicked an email in the last 30 days compared to sending all three.

![Example winback flow with conditional split configured to 'Has Opened Email at least once in the last 60 days'](https://klaviyo.zendesk.com/hc/article_attachments/28716052043675)

Another option is changing the messaging depending on how many orders the subscriber previously placed. For example, if someone has made three or more purchases, you might want to see how your best products perform against new arrivals in your first and second emails, respectively.

As your winback flow continues to run, you can test other aspects to improve the flow and tailor it to your audience.

## Additional resources

Find out more about [A/B testing an email flow.](https://help.klaviyo.com/hc/en-us/articles/6960371049115)

Learn about customizing your messages:

- [Template tags and variable syntax reference](https://klaviyo.zendesk.com/hc/en-us/articles/4408802648731)
- [How to insert preview text into an email](https://klaviyo.zendesk.com/hc/en-us/articles/115005082687)

Get more details on creating flows in Klaviyo:

- [How to create an abandoned cart flow](https://help.klaviyo.com/hc/en-us/articles/115002779411-Guide-to-Creating-an-Abandoned-Cart-Flow)
- [How to create a post-purchase flow](https://help.klaviyo.com/hc/en-us/articles/360028872611-Guide-to-Creating-a-Post-Purchase-Flow)