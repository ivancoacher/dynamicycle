---
id: 15800790306715
title: "How to add SMS to a thank you flow"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/15800790306715-How-to-add-SMS-to-a-thank-you-flow"
section: "Brand loyalty SMS flows"
category: "SMS"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-21T13:54:29Z"
language: en
---

## You will learn

Learn how to add SMS to a thank you or order confirmation flow to diversify the type of communication sent to your customers. Both a thank you and order confirmation flow are a type of post-purchase flow.

****What is a post-purchase flow?****

A post-purchase flow is any flow that sends after someone makes a purchase. This is a broad category that includes the following flows:

- Thank you
- Order confirmation
- Cross-sell
- Up-sell
- Product review
- Replenishment

## Before you begin

Before you can start adding SMS to any flow, [turn on SMS](https://help.klaviyo.com/hc/en-us/articles/4404274419355) in your account settings.

The next steps depend on whether or not you have a [post-purchase flow](https://help.klaviyo.com/hc/en-us/articles/360028872611) set up in Klaviyo:

- If you don’t have a post-purchase flow: [create a pre-built flow with SMS](#h_01H19RCGZ7RMPKY9Q81Q9Z0K5K).
- If you have a post-purchase flow: [add SMS into the existing flow](#h_01H19RCW6XASF8JZS8VCHEVVFQ).

## Use a pre-built flow with SMS

If you don’t already have a thank you or order confirmation flow, the easiest option for creating a flow is by using a template.

Depending on the integration you are using, the flow library may have a pre-built thank you or order confirmation flow with SMS. For example, there are many flows that contain SMS when using the Shopify integration with SMS enabled.

To check for this:

1. Navigate to the ****Flows**** tab.
2. Click ****Create Flow****.
3. In the search bar, enter a term for a flow type you want to create such as “thank you.”
   ![Searching for a thank you flow in Klaviyo's Flow Library
                                                              ](https://klaviyo.zendesk.com/hc/article_attachments/28720902055451)
4. Choose the option with “Email & SMS” in the title if available.
5. If you don’t see an SMS option available, make sure you have SMS enabled in your account settings. Otherwise, a pre-built template including SMS may not be available for your integration, but you can add an SMS action to your existing flow.

After creating a flow from a template, edit the email and SMS content to suit your needs.

## Add an SMS action to an existing flow

1. Navigate to the ****Flows**** tab.
2. Click the name of the thank you or order confirmation flow flow where you want to include SMS.
3. In the flow builder, place a conditional split after the first time delay (if there is one) or trigger.
4. Use the following condition:

   This configuration allows you to add the split to an existing post-purchase flow without having to rearrange your email path.
   ![Adding a split before the first email to send SMS subscribers down a different path](https://klaviyo.zendesk.com/hc/article_attachments/28720896724507)
5. On the NO path, add an SMS message.
   ![Placing an SMS on the NO path under the split](https://klaviyo.zendesk.com/hc/article_attachments/28720896729499)
6. Click ****Configure Content**** in the left sidebar.
7. Add in your message. For example:
   “Hey {{ first\_name|title|default:'there' }}, thank you for your purchase! We hope you're getting excited for your order to arrive.”
8. Drag the rejoin icon below the SMS message onto the email path after the first email. This allows you to continue sending customers emails after sending them an SMS.
   ![Rejoining the SMS path to the email path after the first of each message](https://klaviyo.zendesk.com/hc/article_attachments/28720902083227)
9. Set the SMS message to live.
   ![Changing the SMS message from draft to live](https://klaviyo.zendesk.com/hc/article_attachments/28720896734363)

## Best practices for thank you and order confirmation flows

### Message content

Keep your SMS messages short and concise, and ensure they include relevant information. In this case, you want to thank the customer directly and provide information about their order. It’s also a best practice to include information about their order.

Avoid overusing emojis. Having [1 or 2 emojis](https://help.klaviyo.com/hc/en-us/articles/13288640663579#h_01GTCRB502037HE49P0VPBQM3M) in a thank you or order confirmation message might be fine, but multiple repeating emojis are often associated with spam.

### Number of SMS messages

For both thank you and order confirmation flows, we recommend only using 1 SMS. Typically, all you need is a single message per recipient; however, if you want to send multiple messages, we recommend using SMS once and then following up with email.

### Message timing

For the timing of these messages, send the first immediately and, if you’re sending another,

- Message 1: No delay
- Message 2: 3 days

Don’t send email and SMS messages at the same time. Too many messages can overwhelm your customers and cause them to unsubscribe or mark your messages as spam. It is better to alternate between message types.

## Enhance your SMS post-purchase flow

See the example flows below for ways to customize your flow:

### Order value split

If you want to split based on order value, add a trigger split with trigger **$value > is at least > 100**. Replace 100 with whatever order value you’d like to split based on. In both the YES and NO paths add conditional splits that check for SMS consent and add your email and SMS messages accordingly.
![Separating messages based on whether or not the order value was above $100](https://klaviyo.zendesk.com/hc/article_attachments/28720902088603)

### Order collection split

If you want to split based on item collection, add a trigger split with condition **Collections > contains > CollectionName**. Replace “CollectionName” with the name of the collection you’d like to split based on. You can add multiple splits for different collections. In both the YES and NO paths, add conditional splits that check for SMS consent and add your email and SMS messages accordingly.
![Separating messages based on the collection someone purchased from](https://klaviyo.zendesk.com/hc/article_attachments/28720902092571)

### New vs. returning customers

If you want to split based on if the customer is new or returning, add a conditional split with condition **What someone has done (or not done) > Placed Order > Zero Times > over all time**. In both the YES and NO paths add conditional splits that check for SMS consent and add your email and SMS messages accordingly.
![Using a split to send different messages to new customers than returning customers](https://klaviyo.zendesk.com/hc/article_attachments/28720902095515)

## Additional resources

Learn how to use SMS in other flows:

- [How to create an SMS welcome flow](https://help.klaviyo.com/hc/en-us/articles/360036122291)
- [How to add SMS to your abandoned cart flow](https://help.klaviyo.com/hc/en-us/articles/9352115400219)
- [How to add SMS to your browse abandonment flow](https://help.klaviyo.com/hc/en-us/articles/15806802249883)