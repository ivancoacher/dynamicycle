---
id: "40116763040411"
title: "How to add WhatsApp to a flow"
source_url: "https://help.klaviyo.com/hc/en-us/articles/40116763040411-How-to-add-WhatsApp-to-a-flow"
section: "Send and use WhatsApp with Klaviyo"
category: "WhatsApp"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-20T16:50:34Z"
language: "en"
---
Learn how to add a WhatsApp message action to a flow. Like SMS or push notifications, you can use WhatsApp in combination with email flows to reach your audience in their preferred channel.

## Before you begin

Make sure to do the following before using WhatsApp with flows:

- [Import](https://help.klaviyo.com/hc/en-us/articles/40116243735579) or [collect](https://help.klaviyo.com/hc/en-us/articles/40116301104539) WhatsApp consent.
- Create [WhatsApp templates](https://help.klaviyo.com/hc/en-us/articles/40116644987675) specific to your flows.

## Which flows to add WhatsApp to

You can use WhatsApp in any flow where you're currently using email.

The first 2 flows to add WhatsApp to are:

- [Abandoned cart flow](https://help.klaviyo.com/hc/en-us/articles/360036126951)
- [Browse abandonment flow](https://help.klaviyo.com/hc/en-us/articles/15806802249883)

For welcome series flows, it’s best practice to create separate flows for email and other channels such as text messaging or WhatsApp as customers may sign up to receive messages from each at separate times. With all other flows, add WhatsApp to your existing email flows.

## Add a conditional split to check for consent

If you’re adding WhatsApp to an existing flow, you should first add a conditional split to check if someone has subscribed to WhatsApp.

1. In the flow builder, drag a conditional split component from the left sidebar and drop it right before the first email. Notice that your email message is now on the YES path of the split and there is an empty NO path where you can start your WhatsApp path.
2. Click on the split.
3. In the details sidebar, add the following condition: ****If someone can or cannot receive marketing**** > ****cannot receive**** > ****WhatsApp marketing****. Using “cannot receive” keeps your email messages on the YES path of the split. Anyone who isn’t subscribed to WhatsApp will receive emails instead.
5. Click ****Save****.

## Add a WhatsApp action to the flow

To add a new WhatsApp message into a flow:

1. In the flow builder, drag the WhatsApp action from the left sidebar and drop it on the flow canvas. If you’re using a conditional split to check for consent, drop the WhatsApp action on the path opposite your email path.
3. Click on the WhatsApp message in the flow.
4. In the details sidebar, click ****Select template****.
5. Click on the name of the template you want to use.
6. Click ****Use template****.
8. In the **Settings** section of the sidebar, turn off [Smart Sending](https://help.klaviyo.com/hc/en-us/articles/115002779311) if you want. This is on by default.
9. Change the status of the WhatsApp message to ****Live****.