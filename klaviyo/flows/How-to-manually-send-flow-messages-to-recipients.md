---
id: 115002779331
title: "How to manually send flow messages to recipients"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115002779331-How-to-manually-send-flow-messages-to-recipients"
section: "Send, resend, and pause flows"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-04-21T13:54:14Z"
language: en
---

## You will learn

Learn what manual mode is and how to use it to manually send flow messages. There are several instances where you might want to review a flow message before it sends. For instance, if you want to check who gets your messages or if you are testing a flow. In this case, setting flow messages to manual mode is your best option.

## About manual mode

When you are done configuring a new email or SMS and are interested in testing it out, you can place it in manual mode. When a message is in manual, it is active in your flow, but no emails or SMS will send automatically at send time; you will need to review and send all scheduled messages manually.

To change the status of a message:

1. Find the flow and click on the specific message you want to update.
2. Change the status in the details sidebar that appears on the right.
   ![When you click on the details sidebar for a message, you will see the options for Draft, Manual, and Live.](https://klaviyo.zendesk.com/hc/article_attachments/28705662407451)
   You can also toggle a message's status on the card itself to change the message status, as shown below.
   ![When you click on the status dropdown for a message, you will see the options for Draft, Manual, and Live.](https://klaviyo.zendesk.com/hc/article_attachments/28705662408859)

## Sending messages to recipients in **Needs Review** status

When a message's status is manual, at send time, each recipient will move to the **Needs Review** tab. This means they will not receive messages automatically and you will need to manually review the emails and SMS before they are sent out.

To review if you have recipients in the **Needs Review** status:

1. Click on the specific flow message.
2. Click on ****Show Analytics**** in the top toolbar.
3. On your message, review the number of recipients currently in **Review** status.
   ![Within a flow message showing analytics displayed with review and amount highlighted.](https://klaviyo.zendesk.com/hc/article_attachments/28705662416923)

To view recipients in the **Needs Review** list:

1. Click on a message in your flow.
2. Click ****View details**** in the **Performance** section of the right sidebar.
   ![Within the Performance section of the details sidebar, the view details button is highlighted](https://klaviyo.zendesk.com/hc/article_attachments/28705635649307)
3. Click on the ****Recipient activity**** tab for the message. When you click ****Needs Review**** in the sidebar, you will be taken directly to this list of recipients.
   ![View of the needs review list of recipients that require review before receving a message](https://klaviyo.zendesk.com/hc/article_attachments/28705662413339)

You can individually preview, send, and/or cancel each email and SMS that requires your review. If you have a lot of recipients that need review, you can bulk send and cancel messages with the ****Send All**** or ****Cancel All**** buttons, as shown below.
![The send all and cancel all buttons within the recipients activity tab](https://klaviyo.zendesk.com/hc/article_attachments/28705635655067)
If you send an email or SMS to a contact who is in **Needs Review** status and no longer meets the filters for the flow, they will be skipped and will not receive the message, even if the filters were added after recipients moved into **Needs Review**.

## Turning a message from manual to live

When you turn an email or SMS from manual to live, recipients that are scheduled in the **Waiting** tab will automatically receive the message at send time. However, recipients who are in the **Needs Review** tab will remain there until you take action.

When a flow message's sending status is updated from manual to live, recipients in the **Needs Review** tab will not automatically receive the messages. These messages will still require your manual review in order to send.

## Additional resources

- [Understand how contacts move through a flow](https://help.klaviyo.com/hc/en-us/articles/360017706091)
- [How to manage messages in a flow](https://help.klaviyo.com/hc/en-us/articles/115002779271)
- [How to pause a flow message](https://help.klaviyo.com/hc/en-us/articles/115002779291)