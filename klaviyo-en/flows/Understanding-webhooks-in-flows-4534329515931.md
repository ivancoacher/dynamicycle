---
id: "4534329515931"
title: "Understanding webhooks in flows"
source_url: "https://help.klaviyo.com/hc/en-us/articles/4534329515931-Understanding-webhooks-in-flows"
section: "Add steps or actions to flows"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-04-21T13:55:01Z"
language: "en"
---
## You will learn

Learn about webhooks in flows and how they send information from Klaviyo to your third-party tools and applications. It’s important to note that setting up webhooks can be complex. It’s advised to have development knowledge or development resources to correctly complete this setup. If you are looking for these development directions, learn [how to add a webhook action to a flow](https://developers.klaviyo.com/en/docs/how_to_add_a_webhook_action_to_a_flow).

## What are webhooks?

Simply put, webhooks create a comprehensive way for all your marketing and data tools to talk to one another. As an example, let’s imagine how online banking and fraud protection on your credit card work. If someone fraudulently uses your card, that transaction logs at the retailer and then sends to your bank, who then analyzes it and alerts you via phone or email when there is an issue with your card. This purchase prompted a series of systems to communicate, move this data, and ultimately alert you. These systems are most likely using webhooks to pass this data along. Webhooks:

- Allow your application to pass information or “call” other applications, tools, and servers via HTTP request.
- Send information about an event that has occurred (e.g. an order placed, a new customer subscribed, etc.).
- Can tell your system that an event has happened or notify you of that event.

This event information will then deliver in the manner and place of your choosing. In other words, webhooks provide valuable ways to share data and information from within Klaviyo, out to your other marketing and tools in the manner that you see fit.

You should not use webhooks to subscribe profiles to new lists.

### Key components of webhooks

Webhooks are made of a few pieces:

- ****Trigger****
  The event that causes a webhook to fire
- ****Message (or “the payload”)****
  What the webhook sends, such as key details about the triggering event URL where the message is sent or the URL of the system receiving the message
- ****Headers****
  A place to pass additional information (such as authentication)

## Webhooks in flows

Webhooks are currently only available within flows, and send when a flow reaches a certain stage or step. The webhook will then send a POST request with data about the event or recipient that triggered the flow.

It’s important to note that only one event can initiate the webhook to send. When a subscriber meets the trigger criteria, the webhook will fire, sending the message to the designated URL. Additionally, you can only send webhooks off of flow triggered events, meaning events that can be used as a flow trigger. For example, you can't send a webhook off a profile property changing, as a flow cannot trigger directly from profile changes.
Examples of events in Klaviyo include:

- Placed Order
- Started Checkout
- Subscribed to List

Klaviyo cannot assist with any data issues outside of our system, should the failure be caused by your application or the data not being sent correctly. We suggest reviewing our [How to add a webhook action to a flow](https://developers.klaviyo.com/en/docs/how_to_add_a_webhook_action_to_a_flow) guide to make sure you have correctly set up the action.

## Webhook use cases

It is key to understand the flow triggers that can generate webhooks, as well as some practical use cases on how to implement these with your other applications.

Examples include:

- Sending a message to re-engage lapsed customers.
- Sending a message on your customers’ birthday, and giving them a gift in the form of loyalty points.
- Sending the webhook any time a new subscriber joins your lists. You can send their profile data to another platform.
- Sending a customer an NPS survey to learn more about your subscribers.
- Sending a message or POST request that triggers based on a subscriber being added to a segment or list. However, note that we do not support the “Received Email" event as a flow trigger.

### Real-world example

You decide to connect Klaviyo to your direct mailing tool so you can communicate with customers online and by mail. Your new customer Shah went to your website and bought a few items from your ecommerce store. You want to send Shah a print catalog of your full collection in the future.

Here is where the webhook can tie these experiences together. You would already have your ecommerce store integrated into Klaviyo. In Klaviyo, you set up a flow to trigger based on the **Placed Order** event. You would then provide us with the webhook of the direct mail tool and include details like the customer’s name, address, and what they ordered in the message (i.e., the payload).

Now, every time someone (like Shah) places an order, an event could initiate a print catalog to be sent to their address. The webhook purchase event will prompt info to be sent to your direct mailing tool in potential real-time right from Klaviyo (i.e., the message or payload).

## What can Klaviyo webhooks not do?

Webhooks are not meant to be a bidirectional sync of data. This means that although you can connect other platforms to Klaviyo to send data from us to them, you cannot pass data back to Klaviyo. Information will flow from Klaviyo into the designated systems or applications that you have connected to but cannot flow the other way. Webhooks, unlike API’s, will only work in this one-direction manner.

It’s also important to consider the events that you choose to prompt your information, how often this will happen, and where that data ultimately goes in your system. Klaviyo will provide the framework for connecting your flows data to a platform, but the ultimate value depends on where that information goes after leaving Klaviyo, and what it potentially prompts. Therefore, Klaviyo can only monitor if the webhook is working and not where the data is going or what it is doing after it leaves our system.

Finally, it’s important to consider the data that Klaviyo can and cannot send via a webhook. Klaviyo cannot send certain data points through a webhook based on the way that our flow triggers function. For example, we cannot send email open engagement data for every time that a subscriber opens an email, as you cannot trigger a flow based on opens.

Similarly, while you can use event-based dynamic variables in your webhook payload in an event-triggered flow, the available variables are connected to the original event that triggered the flow (i.e., just like with flow emails). For example, if you have an Abandoned Cart flow triggered by the **Started Checkout** event, you can use dynamic variables from that event in the webhooks payload. But, if in the same flow you’re also using a flow filter or split using an **Added to Cart** metric, you cannot include this additional data in the webhook payload.

Thus, when setting up your webhooks, it’s important to consider what flows can support for data points and what you are looking to achieve in your webhook setup.

Currently, coupon codes, web feeds, and product feeds are not supported in flow webhooks.

## Who should set up webhooks?

As noted above, the systems that you connect to Klaviyo, the manner in which the information or data is packaged, and what data or info you choose to grab, are completely at your discretion.

With this in mind, we strongly recommend a development resource to set up webhooks to ensure that the right events are sent from Klaviyo and post correctly in your application. Klaviyo will also provide you with errors if any webhook fails. However, we may not be able to diagnose any deeper issues with the webhook setup, or how the data is ultimately posting to your application.

### Requirements and considerations

In addition to making sure you have a developer resource to properly set up your webhook and test it on your accompanying system, Klaviyo has some key requirements for using this functionality:

- Only user roles who have [access to create flows](https://help.klaviyo.com/hc/en-us/articles/115005231648-Guide-to-User-Management-and-Privileges) can set up webhooks in Klaviyo. This includes the roles of Manager, Admin, and Owner.
- For added security, [two-step authentication](https://help.klaviyo.com/hc/en-us/articles/360026617692) must be enabled within your account in order to use webhooks or add new webhook actions within an existing flow.

## Ready to set up?

Webooks provide powerful mechanisms for communicating data from Klaviyo to your other outside systems or applications. If you are ready to set up your webhooks, you can read our developer documentation guide on [How to add a webhook action to a flow](https://developers.klaviyo.com/en/docs/how_to_add_a_webhook_action_to_a_flow).