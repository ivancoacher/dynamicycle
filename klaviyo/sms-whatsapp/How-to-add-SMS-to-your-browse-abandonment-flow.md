---
id: 15806802249883
title: "How to add SMS to your browse abandonment flow"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/15806802249883-How-to-add-SMS-to-your-browse-abandonment-flow"
section: "Revenue-generating SMS flows"
category: "SMS"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-21T13:54:29Z"
language: en
---

## You will learn

Learn how to add SMS to your browse abandonment flow to diversify the type of communication sent to your customers.

****What’s the difference between browse abandonment and abandoned cart flows?****

To enter an abandoned cart flow, someone must add an item to their cart and (in some cases) begin to check out.

As for browse abandonment flows, all they need to do is view an item and move on.

Visiting a product page doesn’t indicate the same level of interest as adding an item to a shopping cart and beginning the checkout process, so we recommend making your browse abandonment messages a lighter touchpoint" than your abandoned cart flow, particularly when using SMS.

## Before you begin

Before you start adding SMS to your browse abandonment flow:

- [Turn on SMS](https://help.klaviyo.com/hc/en-us/articles/4404274419355) in your account settings.
- Learn [how to create a browse abandonment](https://help.klaviyo.com/hc/en-us/articles/115002775252) flow if you don’t yet have one in your account.

### Browse abandonment compliance

Always use [quiet hours](https://help.klaviyo.com/hc/en-us/articles/4408737146651) for browse abandonment SMS messages. This feature, which is on by default, prevents SMS from sending too early or late in the day. Most countries forbid sending SMS during certain hours, and quiet hours can help you avoid fines.

## Add an SMS action to a browse abandonment flow

1. Navigate to the ****Flows**** tab.
2. Click the name of the browse abandonment flow where you want to include SMS.
3. In the flow builder, place a conditional split after the first time delay.
   - Note: the time delay must be within 48 hours of when the flow triggers.
4. Use the following condition:
   **Person is or is not consented to receive SMS > is not**
   This configuration allows you to add the split to an existing browse abandonment flow without having to rearrange your email path.
   ![Adding a split to send SMS subscribers down a different path](https://klaviyo.zendesk.com/hc/article_attachments/28716333017627)
5. On the NO path, add an SMS message.
6. Click ****Configure Content**** in the left sidebar.
7. Add in your message. For example:
   “Hey {{ first\_name|title|default:'there' }}, did you see something you liked? Time to check it out! {{ event.URL }}”
   ****Note****: Dynamic content depends on your integration, so the tags in the example may not work for you. Learn more [about dynamic content](https://help.klaviyo.com/hc/en-us/articles/115002779071#01FK12GQZA6JMB1MN5JSXSM8GA).
8. Drag the rejoin icon below the SMS message onto the email path after the first email. This allows you to continue sending customers emails after sending them an SMS message.
   ![Rejoining the SMS and email paths after the first of each message](https://klaviyo.zendesk.com/hc/article_attachments/28716355982491)
9. Do not turn off either quiet hours or Smart Sending for this message.
   Quiet hours is an [SMS compliance requirement](https://help.klaviyo.com/hc/en-us/articles/7956171032091), while Smart Sending is a general best practice.
10. Set the SMS message live.

## Enhance your SMS browse abandonment flow

See the examples flows below for ways to customize your flow:

### Item category split

If you want to split based on item categories:

1. Add a **Trigger Split** with the condition:
   **Categories > contains > CategoryName**.
2. Replace “CategoryName” with the name of the category you’d like to split based on. You can add multiple splits for different categories.

![Separating the flow messages based on the product category](https://klaviyo.zendesk.com/hc/article_attachments/28716355984795)

### New vs. returning customers

If you want to split based on whether the person browsing has purchased from you before:

1. Add a conditional split with the condition:
   **What someone has done (or not done) > Placed Order > zero times > over all time**.
2. Put your message for new customers in the YES path
3. Place your message for returning customers in the NO path.

![Adding a split to separate messages for returning customers and new customers](https://klaviyo.zendesk.com/hc/article_attachments/28716333022619)

### Add customers to continue the conversation

While you can only send 1 SMS message to a site visitor who abandoned their session, you can ask the customer to continue chatting. If you ask a question and the subscriber responds, you can use flows or 1-on-1 SMS conversations to keep talking.

For instance, you can say something like "No longer interested in X? Tell us why! 1 for too pricey, 2 for not my style, 3 for I’ll revisit later."

If the subscriber replies, you either respond back via a conversation or set up a [flow to trigger for the incoming message](https://help.klaviyo.com/hc/en-us/articles/360049930372), customizing the response based on what the subscriber says.
![The trigger filters of a flow that checks if the message contains 1, 2, or 3](https://klaviyo.zendesk.com/hc/article_attachments/28716333026587)
![A Sent SMS flow to reply to a subscriber's reason for not buying an item they browsed](https://klaviyo.zendesk.com/hc/article_attachments/28716333024411)

## Additional resources

Learn how to use SMS in other flows:

- [How to create an SMS welcome flow](https://help.klaviyo.com/hc/en-us/articles/360036122291)
- [How to add SMS to your abandoned cart flow](https://help.klaviyo.com/hc/en-us/articles/9352115400219)
- [How to add SMS to your thank you or order confirmation flow](https://help.klaviyo.com/hc/en-us/articles/15800790306715)