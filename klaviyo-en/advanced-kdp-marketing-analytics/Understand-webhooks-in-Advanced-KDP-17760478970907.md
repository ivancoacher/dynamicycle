---
id: "17760478970907"
title: "Understand webhooks in Advanced KDP"
source_url: "https://help.klaviyo.com/hc/en-us/articles/17760478970907-Understand-webhooks-in-Advanced-KDP"
section: "Webhooks"
category: "Advanced KDP & Marketing Analytics"
category_slug: "advanced-kdp-marketing-analytics"
klaviyo_updated: "2026-04-21T13:56:43Z"
language: "en"
---
## You will learn

Learn about webhooks, and how you can use them to send information to your third-party applications in response to events captured in Klaviyo. For more detailed information on how to receive system webhooks, head to our developer resource on [working with system webhooks](https://developers.klaviyo.com/en/docs/working_with_system_webhooks).

[Advanced KDP](https://help.klaviyo.com/hc/en-us/articles/17655007276059) is not included in Klaviyo’s standard marketing application, and a subscription is required to access the associated functionality. Head to our [billing guide](https://help.klaviyo.com/hc/en-us/articles/115000976672) to learn about how to purchase this plan.

[Webhooks in Klaviyo CDP Video](https://fast.wistia.net/embed/iframe/kwiicwga5w?web_component=true&seo=true)

## What are webhooks?

Webhooks allow Klaviyo to pass information or “call” other applications, tools, and servers via HTTP requests. They can send information about an event that has happened (e.g. an order placed, a new customer subscribed, etc) or notify your external systems that the event has occurred.

Klaviyo supports 2 kinds of webhooks:

1. ****Webhooks in Advanced KDP****
   Webhooks available as part of Advanced KDP are used to notify your external systems that a particular event has occurred, and allow you to send information in response to a wide array of events without the limitations of being in a Flow.
2. ****Flow webhooks****
   Flow webhooks are only available within the flows interface, and are triggered when the Flow reaches a certain stage or step. They can be used to send data about the event or recipient that triggered the Flow.

### Key components of webhooks

Webhooks are made of a few key components:

- ****Topic****
  The event that causes a webhook to fire
- ****Body (or “the payload”)****
  The data that the webhook sends
- ****Headers****
  A place to pass additional information (such as authentication)

## How do webhooks in Advanced KDP differ from Flow webhooks?

You can use webhooks in Advanced KDP or Flow webhooks depending on your needs.

### Events included

Flow webhooks can only respond to a subset of Klaviyo events, and do not support message related events like **Unsubscribed**, **Received email**, or **Clicked email** as flows generally end with message receipt rather than begin with them. Meanwhile, webhooks in the Advanced KDP allow you to send information in response to any event in your account.

These include:

- Email events (e.g., **Received email**, **Clicked email**, **Marked email as spam, Unsubscribe**)
- SMS events (e.g., **Sent SMS**, **Received SMS**)
- Push notification events (e.g., **Received push**, **Bounced push**)
- Events from integrations ( i.e., events from first-party integrations created by Klaviyo)
- API events (e.g., events synced through [Klaviyo’s APIs](https://developers.klaviyo.com/en/reference/api_overview))

### Payload

Flow webhooks allow you to customize the data included in the request, but you must manually construct the payload. Meanwhile, webhooks in Advanced KDP use a prebuilt payload that does not require any manual work on your end, and are used to notify external systems that an event has occurred.

### Flow limitations

Flow webhooks must be configured within the flows interface, and do not allow you to use several triggers at once. Different triggers must be created through individual flows, and are dependent on the Flow’s overall status (e.g., a flow in draft would not send data through the Flow webhook). Meanwhile, webhooks in Advanced KDP exist outside of the flows interface, and are not dependent on the series of steps leading up the webhook action like a Flow webhook.

## Set up webhooks

To set up a webhook in Klaviyo, navigate to **Webhooks** under ****Advanced KDP**** ****>**** ****Data managment > Webhooks**** in Klaviyo.

To add a new webhook, click the ****Create webhook**** button.

1. On the **Create a webhook** modal, enter the information. This includes:
   - ****Name****
     How you’ll identify your webhook
   - ****Endpoint URL****
     The URL associated with the destination for the webhook request
   - ****Secret key****
     A unique identifier to identify Klaviyo webhook requests in your other systems
   - ****Description****
     An optional description for your webhook.
2. In the **Topics** section, choose the events that you would like to trigger the webhook notification

![Create webhook modal](https://klaviyo.zendesk.com/hc/article_attachments/28704486678683)

The callback URL must:

- Be a valid URL format
- Start with HTTPS://
- Not have a self-signed SSL certificate
- Not redirect to another URL

Once you have created your webhook, it will be listed on the **Webhooks** page along with the:

- Webhook name
- Webhook URL
- Time of the latest sync
- Status

![List of created webhooks](https://klaviyo.zendesk.com/hc/article_attachments/28704478568859)

Note that it can take up to 15 minutes for the webhook to start sending to the URL.

You can delete or disable your webhook using the menu next to the item.

## Test system webhooks

When setting up a webhook in Klaviyo, you can test it to make sure that the connection is successful. To test your webhook, use the ****Test connection**** button after entering the required fields.

![test connection.jpg](https://klaviyo.zendesk.com/hc/article_attachments/39030496797723)

A menu will appear where you can select a topic and send a test to your callback URL.

![Test webhook modal](https://klaviyo.zendesk.com/hc/article_attachments/28704478571931)

After performing the test, you’ll see a message indicating whether it was successful, along with the header and body for the request populated in the **Response** tab.

To verify that a webhook notification is from Klaviyo, use the secret key you created to identify the request.

![Test successful indicator](https://klaviyo.zendesk.com/hc/article_attachments/28704478574491)

## Example payload

Below is an example of the payload for a webhook request in response to the **Email delivered** topic.

Note that the payload may be different based on your account-specific data.

```
{
  "meta": {
    "timestamp": "2023-08-10T07:25:23.700369+00:00",
    "klaviyo_webhook_id": "ID",
    "version": "2023-06-03"
  },
  "data": [
    {
      "topic": "event: email_delivered",
      "external_id": "ID",
      "payload": {
        "data": {
          "id": "ID",
          "type": "event",
          "links": {
            "self": "https://a.klaviyo.com/api/events/ID/"
          },
          "attributes": {
            "uuid": "96150200-374e-11ee-8001-a163313bc6c2",
            "datetime": "2023-08-10 07:21:56+00:00",
            "timestamp": 1691652116,
            "event_properties": {
              "$ESP": 0,
              "Subject": "? Free (Cool!) Swag Alert ?",
              "$message": "01H7F525FKR31P27Y7PNGVBBKK",
              "$event_id": "01H7F525FKR31P27Y7PNGVBBKK:125423419905414052533228990613763937641",
              "$group_ids": [
                "V7adxq"
              ],
              "$attribution": {
                "$send_ts": 0,
                "$attributed_event_id": ""
              },
              "Email Domain": "klaviyo-demo.com",
              "Campaign Name": "Daily Newsletter: 2023-08-10",
              "Inbox Provider": "Amazon SES Inbound",
              "$_cohort$message_send_cohort": "1691652081:01H7F525FKR31P27Y7PNGVBBKK"
            }
          },
          "relationships": {
            "metric": {
              "data": {
                "id": "ID",
                "type": "metric"
              },
              "links": {
                "self": "https://a.klaviyo.com/api/events/ID/relationships/metric/",
                "related": "https://a.klaviyo.com/api/events/ID/metric/"
              }
            },
            "profile": {
              "data": {
                "id": "ID",
                "type": "profile"
              },
              "links": {
                "self": "https://a.klaviyo.com/api/events/ID/relationships/profile/",
                "related": "https://a.klaviyo.com/api/events/ID/profile/"
              }
            }
          }
        }
      }
    },
```

## Additional resources

[How to add a webhook action to a Flow](https://developers.klaviyo.com/en/docs/how_to_add_a_webhook_action_to_a_flow)

[Understanding Klaviyo webhooks](https://help.klaviyo.com/hc/en-us/articles/4534329515931)

[Working with system webhooks (Klaviyo's Webhooks API)](https://developers.klaviyo.com/en/docs/working_with_system_webhooks)