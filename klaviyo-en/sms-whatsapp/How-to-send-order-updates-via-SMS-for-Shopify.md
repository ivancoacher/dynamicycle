---
id: 18389135527323
title: "How to send order updates via SMS for Shopify"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/18389135527323-How-to-send-order-updates-via-SMS-for-Shopify"
section: "Brand loyalty SMS flows"
category: "SMS"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-21T13:56:44Z"
language: en
---

## You will learn

Learn how to send order updates via text to people not opted in to your SMS marketing program.

These messages are a great way to:

1. Expand your SMS audience, potentially converting recipients to sign up for marketing text messages.
2. Decrease customer support questions by proactively providing information about orders.

Shopify customers can now collect transactional SMS consent on their thank you and order status pages via an app block and sync it to Klaviyo. Shopify Plus customers can also collect transactional SMS consent on their checkout pages the same way. Please note that collecting both transactional-only consent at checkout via app block and collecting consent for SMS order updates may appear repetitive to customers.

## Before you begin

Please note the following about SMS order updates:

- This feature is only available for paid accounts with Shopify stores.
- Consent given for order updates only applies to that 1 order.
  - This permission does not apply to SMS updates on any future orders, nor does it apply to SMS marketing messages. It is not the same as [transactional consent](https://help.klaviyo.com/hc/en-us/articles/35067557759771).
- These messages send to anyone who either subscribed to receive:
  - Only order updates.
    Or
  - SMS marketing messages.
- Before using this feature, your message must be approved by Klaviyo, either via using a pre-approved template or by submitting a custom message and going through the approval process.
  - The approval process can take up to 24 hours (1 business day).
  - Editing a transactional message after it has been approved removes its transactional status, and the message will need to be re-submitted for approval.
- You can send order updates via post-purchase flows triggered by one of these metrics:
  - **Placed Order**
  - **Fulfilled Order**
  - **Partially Fulfilled Order**
  - **Refunded Order**
  - **Cancelled Order**
  - **Confirmed Shipment**
  - **Delivered Shipment**
  - **Marked Out for Delivery**
- You cannot use this feature if you are an [alcohol or firearms brand,](https://help.klaviyo.com/hc/en-us/articles/17252552814875) regardless of whether you have age-gating or not.

Note that **Confirmed Shipment**, **Delivered Shipment**, and **Marked Out for Delivery** only sync to Klaviyo if they are available in Shopify, and these events are only available for certain shipping carriers.

****What is the difference between consenting to SMS marketing and order updates?****

Subscribing to order updates is a more limited consent than subscribing to SMS marketing.

- Order update subscribers can only receive SMS messages about the order, such as when it was shipped or delivered.
- SMS marketing subscribers can receive SMS messages for anything, including sales, product launches, and updates for all orders.

|  |  |  |  |
| --- | --- | --- | --- |
| ****Use case**** | | ****Order updates**** | ****SMS marketing**** |
| Campaigns | | ✖ | ✔ |
| Flow messages | Order updates | ✔ | ✔ |
| Abandoned cart, welcome, winback, etc. | ✖ | ✔ |
| SMS conversations | | ✖ | ✔ |

## Understand how consent for order updates works

The way someone opts in to receive SMS order updates is by:

- Going to the Shopify checkout page.
- Inputting their phone number in the shipping address field.
  ![Example of Shopify checkout page when order updates is enabled](https://klaviyo.zendesk.com/hc/article_attachments/28716118142619)
- Placing an order.

When any order-related event (e.g., **Placed Order**, **Fulfilled Order**, etc.) syncs to Klaviyo, it includes a field specifying that they've opted in to SMS order updates.

This consent only applies to that 1 order. If someone places multiple orders, they will only receive updates about the order(s) where they inputted their phone number within the shipping address field.

****How can I see if someone consented to order updates?****

You can view whether or not someone opted in to receive order updates in the event details. This field is called **OptedInToSMSOrderUpdates**.

The example below is for a **Placed Order** event, but this field is also included in other order-related events.

![Example of an event with order update details](https://klaviyo.zendesk.com/hc/article_attachments/28716118158747)

This information will not show on their profile; it’s not a profile property or part of channel consent.

****What happens if someone unsubscribes?****

Unsubscribing removes consent for all SMS messages.

For instance, say that a customer previously consented to both order updates and SMS marketing. If they unsubscribe, either by clicking a link or texting an opt-out keyword, you will not be able to send them any SMS message, including order updates, until they [opt back in](https://help.klaviyo.com/hc/en-us/articles/360035056972#h_01H91A80BJ8M5D4JVJYYYAGWX6).

## Collect order update consent

If you haven’t already, you must update your settings in Shopify so that you can start collecting consent for order updates.

1. Log in to your Shopify store.
2. Navigate to ****Settings > Checkout****.
3. Under **Customer contact method**, select ****Email**** (if it’s not already selected).
   ![Shopify checkout settings when Email is selected for customer contact method](https://klaviyo.zendesk.com/hc/article_attachments/28716118147099)
4. Scroll down to the **Customer information** section.
5. Locate the option for **Shipping address phone number**, and select ****Optional****.
   ![Making the shipping address phone number field optional](https://klaviyo.zendesk.com/hc/article_attachments/28716118152091)
6. Save your changes.
7. Locate the **Checkout language** section.
8. Click ****Manage checkout language****.
9. Search for the **Checkout contact** section.
10. In the **Optional phone label** field, add the following language:

    - “Phone number to receive order updates.”
11. In the **Phone tooltip** field, add the SMS consent language, replacing the URL placeholders with the URLs to your privacy policy and terms of service:

    - Suggested consent language: “Enter your phone number to consent to order-related text messages (order and shipping updates), including messages sent by autodialer. Consent is not a condition of any purchase. Msg & data rates apply. Msg freq varies. Unsubscribe by replying STOP or clicking the unsubscribe link (where available). View our Privacy Policy [Insert your URL] and Terms of Service [Insert your URL].”
    - Example: “ View our Privacy Policy [mystore.com/polices/privacy-policy] and Terms of Service [mystore.com/policies/terms-of-service].”
    - If you have engineering resources, we recommend adding this language directly to your checkout page. That way, the language is conspicuous to customers, which helps toward compliance. See [Shopify’s Help Center for instructions](https://help.shopify.com/en/manual/checkout-settings/checkout-extensibility/checkout-editor).
12. Save your changes.
13. In the left sidebar, click ****Notifications > Customer notifications****.
14. Select ****Order Confirmation > SMS****.
15. If the status is **Active**, click ****Deactivate****.

![Example of active order confirmation SMS in Shopify](https://klaviyo.zendesk.com/hc/article_attachments/28716118155035)

## Create your transactional message

Note that your flow must use one of the following metrics as the triggering event:

- **Placed Order**
- **Fulfilled Order**
- **Partially Fulfilled Order**
- **Refunded Order**
- **Cancelled Order**
- **Confirmed Shipment**
- **Delivered Shipment**
- **Marked Out for Delivery**

### Creating a custom transactional message

1. Drag an SMS into your flow.
2. Edit the content of your message (e.g., “Your order has shipped! Track it here [LINK]”).
3. Save the content.
4. In the right sidebar, click ****Apply for transactional status****.

   - Note: if you want multiple messages in a flow to be transactional, you must select them one at a time.
5. Wait at least 24 hours (i.e., 1 business day) to see if your message was approved. While waiting:

   - You will not be able to edit the message content.
   - You cannot set up an A/B test.![SMS message waiting to be reviewed for its transactional content](https://klaviyo.zendesk.com/hc/article_attachments/28716118168475)
6. After 24 hours, you will see whether your message has been approved or denied.

![SMS message after it's been approved for transactional status](https://klaviyo.zendesk.com/hc/article_attachments/28716118171931)

If your message is approved, note that any subsequent edits to the message content will remove the transactional status. If you want to edit the content, you must uncheck the transactional status, edit the content, and then submit the message for approval.

### What to do if the message was rejected

If your message was rejected you can:

- Keep the message as-is (and not have it be marked transactional).
- Edit the content and re-submit it for approval.
- Submit an appeal.

  For the appeal, you must submit a ticket to Klaviyo Support with the subject line and include:
- “Transactional appeal” as the subject line/reason for the ticket
- Flow message ID
- Example (or 2) of the message you want to send
- Screenshot of your call to action (CTA)
- Estimate of how many times per month someone could receive this message
- The opt-out and SMS disclosure language you’re using
- Links to your privacy policy and terms of service

## Targeting your SMS subscribers

Transactional messages send to both SMS marketing and order update subscribers. However, you may want to split your SMS sending depending on which of these groups someone is in.

To do this, you need to use a trigger split and set it to **OptedInToSMSOrderUpdates****equals True**. (The conditional split **Can receive SMS** only checks for SMS marketing consent, so everyone opted in to only SMS order updates will go down the **No** path.)

1. Drag in a conditional split and set it to: **If someone can or cannot receive marketing > can receive > SMS marketing**.
2. On the **Yes** path, add an SMS message and either create your message and include promotional content, or mark the message as transactional.
3. On the **No** path, place a trigger split and set it to **OptedInToSMSOrderUpdates****equals True**.
4. On the **Yes** path of the trigger split, add an SMS message.
5. Create your transactional message and submit for approval.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/34231483440667)
6. Optional: turn off Smart Sending and quiet hours, and turn on UTM tracking.
7. When you're ready, update your flow status to ****Live****.

If you have an existing flow that is more complex (with several splits, emails, or time delays), you can switch the splits so that you don’t have to move anything to a different path.