---
id: 46624475312539
title: "How to add WhatsApp to your browse abandonment flow"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/46624475312539-How-to-add-WhatsApp-to-your-browse-abandonment-flow"
section: "Send and use WhatsApp with Klaviyo"
category: "WhatsApp"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-20T16:51:03Z"
language: en
---

Learn how to add WhatsApp to your browse abandonment flow to diversify how you engage customers.

Adding WhatsApp to a browse abandonment flow helps you follow up with shoppers who viewed a product but did not add it to their cart. Because browse abandonment signals lighter intent than abandoned cart, your WhatsApp message should feel like a gentle reminder.

## What’s the difference between browse abandonment and abandoned cart flows?

To enter an abandoned cart flow, someone must add an item to their cart and, in some cases, begin checkout.

For browse abandonment flows, someone only needs to view an item and leave your site.

Viewing a product page shows less purchase intent than adding an item to a cart. Keep browse abandonment WhatsApp messages lighter than abandoned cart reminders.

## Before you begin

Before adding WhatsApp to your browse abandonment flow:

- [Set up WhatsApp in your account](https://help.klaviyo.com/hc/en-us/articles/40111819732635).
- Create a browse abandonment flow if you do not already have one.

## Add a WhatsApp message to a browse abandonment flow

Follow these steps to add WhatsApp to your existing browse abandonment flow.

1. Navigate to the ****Flows**** tab.
2. Click the name of the browse abandonment flow where you want to include WhatsApp.
3. In the flow builder, place a conditional split after the first time delay.
4. Configure the split using the condition:

   **Person is or is not consented to receive WhatsApp > is not**.
5. On the NO path, add a WhatsApp message.
6. Click ****Configure Content**** in the left sidebar.
7. Add your message. For example:

   “Hey {{ first\_name|title|default:'there' }}, did you see something you liked? Take another look here. [URL button {{ event.URL }}]”
8. Drag the rejoin icon below the WhatsApp message onto the email path after the first email. This allows customers to continue receiving emails after the WhatsApp message.
9. Set the WhatsApp message live.

## Enhance your WhatsApp browse abandonment flow

You can customize your flow using additional splits and targeting.

### Item category split

If you want to split based on item categories:

1. Add a **Trigger Split** with the condition:
   **Categories > contains > CategoryName**.
2. Replace “CategoryName” with the category you want to target. You can add multiple splits for different categories.

### New vs. returning customers

If you want to split based on whether someone has purchased before:

1. Add a conditional split with the condition:
   **What someone has done (or not done) > Placed Order > zero times > over all time**.
2. Place your message for new customers in the YES path.
3. Place your message for returning customers in the NO path.

### Continue the conversation

You can ask shoppers a question in your WhatsApp message to encourage engagement. If a customer replies, you can respond directly or trigger a follow-up flow based on their response.

For example, you might say: “No longer interested in this item? Reply 1 if it’s too pricey, 2 if it’s not your style, or 3 if you’ll revisit later.”

## Next steps

After adding WhatsApp to your browse abandonment flow:

1. Test the flow to confirm messages send correctly.
2. Review timing between WhatsApp and email messages.
3. Monitor performance and adjust message tone or targeting as needed.