<h1>Understand the different webhooks available in Klaviyo</h1>

## You will learn

Learn about the differences between webhook solutions available in Klaviyo, and when you should use each one.

## Before you begin

[Advanced KDP](https://help.klaviyo.com/hc/en-us/articles/17655007276059) is not included in Klaviyo’s standard marketing application, and a subscription is required to access the associated functionality. Head to our [billing guide](https://help.klaviyo.com/hc/en-us/articles/115000976672) to learn how to purchase this plan.

## What are webhooks?

Webhooks allow Klaviyo to pass information or “call” other applications, tools, and servers via HTTP requests. They can send information about an event that has happened (e.g. an order placed, a new customer subscribed, etc) or notify your external systems that the event has occurred.

Webhooks are made of a few key components:

- ****Topic****The event that causes a webhook to fire.
- ****Body**** (or “the payload”)
  The data that the webhook sends.
- ****Headers****
  A place to pass additional information (such as authentication).

## Flow webhooks

You can add [webhooks in flows](https://help.klaviyo.com/hc/en-us/articles/4534329515931) as an action that occurs when the flow reaches a certain stage or step. Once a flow reaches the webhook action, a POST request is sent with data about the event or the recipient that triggered the flow, based on how you construct the payload.

Flow webhooks can only send based on flow-triggered events (i.e., events that can be used as a flow trigger). Additionally, flow webhooks do not support message-related events (e.g., **Received email**, **Clicked email**, **Marked email as spam**) as flows typically end in message receipt.

Unsubscribed from Email Marketing can be used as a flow trigger and the topic for a flow webhook.

### Example use cases for flow webhooks

Some example uses case where flow webhooks would be most effective include:

- Send a message or POST request that triggers based on a subscriber being added to a segment or list.
- Automate suppressions when a profile enters an unengaged segment.
- Send a personalized thank you message through a service like Whatsapp or Facebook messenger when customers purchase.

## Webhooks in Advanced KDP

Advanced KDP is not included in Klaviyo’s standard marketing application, and a subscription is required to access the associated functionality. Head to our billing guide to learn more about adding this functionality to your plan or get started if you are a new customer.

Webhooks in Advanced KDP allow you to notify external systems in response to events, without depending on a series of steps leading up the webhook action. Advanced KDP webhooks do not require you to manually construct or specify the body of the webhook request. If you want to notify your external systems that an event has occurred without any custom development, webhooks in Advanced KDP are most effective.

Advanced KDP webhooks also support a wider range of topics to trigger the request, and allow you to send information in response to any event that can be queried for via the [Get Events API](https://developers.klaviyo.com/en/reference/get_events).

These include:

- Email events (e.g., Received email, Clicked email, Marked email as spam)
- SMS events (e.g., Sent SMS, Received SMS)
- Push notification events (e.g., Received push, Bounced push)
- Events from integrations ( i.e., events from first-party integrations created by Klaviyo)
- API events (e.g., events synced through Klaviyo’s APIs)

This includes message-related events like **Unsubscribed**, **Received email**, or **Clicked email** that are not supported by flow webhooks.

Additionally, Advanced KDP webhooks allow you to subscribe to multiple triggers at once, unlike flow webhooks, which depend on single-trigger flows.

Destination URLs must be publicly accessible HTTP endpoints.

### Example use cases for Advanced KDP webhooks

- Sync customers’ **Unsubscribed** events to external systems.
- Report **Received Email** events to help desk software so agents can see email history to better serve customers.
- Sync all email sends, opens, and clicks into a data warehouse that is not supported by Klaviyo's [data warehouse sync](https://help.klaviyo.com/hc/en-us/articles/17759932376475).

## Code

Code is a feature included in Klaviyo Advanced KDP. It is not included in Klaviyo’s standard marketing application, and a Advanced KDP subscription is required to access the associated functionality. Head to our billing guide to learn more about adding this functionality to your plan or get started if you are a new customer.

Code leverages webhooks to enable the execution of custom functions in response to an event trigger. You can write code directly in Klaviyo’s editor, and Klaviyo manages the code execution, monitoring, and logging.

If you want to send requests to your external systems without hosting a public HTTP endpoint, you can use Code. Additionally, if you want to execute custom functions in response to an event occurring, you should use Code rather than the other webhook solutions available in Klaviyo.

Code also supports more granularity with event triggers over webhooks in Advanced KDP. You can select individual metrics to act as the topic rather than all integration or API events.

Note that Code does not support the following events as topics:

- Email opened
- Email received

### Example Code use cases

- Import Python JSON libraries to parse event payloads and extract something.
- Set custom profile properties based on event metadata using [Klaviyo’s APIs](https://developers.klaviyo.com/en/reference/api_overview).
- Import chatGPT libraries and create a custom message for each abandoned cart based on the profile and items in the cart.

## Additional resources

[Understand webhooks in flows](https://help.klaviyo.com/hc/en-us/articles/4534329515931)
[Understand webhooks in Advanced KDP](https://help.klaviyo.com/hc/en-us/articles/17760478970907)
[Getting started with Code](https://help.klaviyo.com/hc/en-us/articles/18620644491035)
