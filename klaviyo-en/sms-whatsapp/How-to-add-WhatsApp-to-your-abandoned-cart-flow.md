---
id: 46623602305563
title: "How to add WhatsApp to your abandoned cart flow"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/46623602305563-How-to-add-WhatsApp-to-your-abandoned-cart-flow"
section: "Send and use WhatsApp with Klaviyo"
category: "WhatsApp"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-20T16:51:02Z"
language: en
---

Learn how to add WhatsApp messages to your abandoned cart flow and follow best practices.

Adding WhatsApp to your abandoned cart flow lets you remind shoppers to complete their purchase using a direct and immediate channel. When combined with email, this can increase recovery while maintaining a good customer experience.

## Add WhatsApp to an abandoned cart flow

Follow these steps to add WhatsApp to your existing abandoned cart flow.

1. Navigate to ****Flows****.
2. Find the abandoned cart flow where you want to include WhatsApp.
3. In the flow, place a conditional split after the first time delay.
4. Configure the split using the condition:

   **If someone can or cannot receive marketing > Person cannot receive > WhatsApp marketing**.
5. On the NO path, add a WhatsApp message.
6. Click the WhatsApp message card.
7. Click ****Edit**** in the details panel.
8. Add your message content. For example:

   “Hey {{ person|lookup:"first\_name"|default:'there' }}, your cart is about to expire. Did you want to check it out? [URL Button with Link]”
9. To encourage conversions, consider including a discount. For example:

   “Hey {{ person|lookup:"first\_name"|default:'there' }}, your cart is about to expire. Get 10% off now with code. [Copy Code button {% coupon\_code 'YOUR\_COUPON' %}] [URL Button with Link]”
10. Rejoin the split after the WhatsApp message to the main flow after the first email.
11. Set the WhatsApp message to live.

## Improve your WhatsApp abandoned cart flow

You can customize your abandoned cart flow with additional targeting and splits.

While you should limit reminders to one WhatsApp message per recipient for a single abandoned cart event, you can include additional WhatsApp messages in the flow by targeting different audiences.

### Skip WhatsApp if the product is unavailable

A best practice is to showcase only one item in a WhatsApp message. This keeps the message concise and ensures clarity.

Because WhatsApp messages cannot dynamically display multiple abandoned items in the same way as email, focus on the first item in the cart. If that item is out of stock, you can cancel the message using the following format:

```
{% catalog event.ProductID unpublished="cancel" %}
Your abandoned cart reminder message
[Link to product]
{% endcatalog %}
```

### Value split

Use a trigger split to send different WhatsApp messages based on cart value. For example, offer a discount only to customers whose cart value exceeds a certain threshold.

### Product collection split

Add a trigger split based on collection to tailor your WhatsApp message to specific product categories.

### New purchaser vs. returning customer split

Use a conditional split to send different WhatsApp messaging to new customers versus returning customers.

### Frequent purchaser split

Create a conditional split based on purchase frequency to reward loyal customers with different incentives.

## Next steps

After adding WhatsApp to your abandoned cart flow:

1. Test the flow to confirm messages send correctly.
2. Review timing to ensure WhatsApp and email messages are spaced appropriately.
3. Monitor performance and adjust incentives or copy to improve recovery rates.