---
id: 360050242251
title: "How to add an internal alert action to a flow"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360050242251-How-to-add-an-internal-alert-action-to-a-flow"
section: "Add steps or actions to flows"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-04-21T13:54:50Z"
language: en
---

## You will learn

Learn how to send an internal alert (previously called **notification**) when a customer first triggers or reaches a particular point in a flow. It sends emails to your team around certain activities that require specific follow-up or attention; for example, notifying your customer experience team when someone leaves a detractor NPS score or alerting your sales team when someone is added to a wholesale or VIP list.

## Before you begin

While these internal alert emails can be sent to any confirmed email addresses, recipients do not need to have customer profiles in your account. Note that all emails sent do count toward any account email sending limits.

There is a maximum limit of 5 recipients per internal alert action.

You will not be able to use the following in an internal alert:

- - Dynamic coupons
  - Data or product feeds
  - Webview, preference, or unsubscribe link tags

## Add the internal alert action

To add a new internal alert action into a flow:

1. Drag the internal alert action from the sidebar and drop it on any green drop point.
   ![Internal alert highlighted in the list of flow actions](https://klaviyo.zendesk.com/hc/article_attachments/28716055627547)
2. After adding a new alert to your flow, specify between 1 and 5 recipients in the right sidebar.
   - Recipients do not need to be account users or have profiles in your Klaviyo account, but internal alert actions have their own recipient opt-in process.
     ![Internal alert editor, where you can add or remove recipients and customize the message](https://klaviyo.zendesk.com/hc/article_attachments/28716066140699)
3. Customize the Send to, From, From / Reply-to email, Subject, and Message sections.
   - When customizing your message content, you can include [personalization variables](https://klaviyo.zendesk.com/hc/en-us/articles/4408802648731) that will populate with information regarding the contact that reached this step in the flow; i.e., the contact triggering the notification. For metric-triggered flows, you can also use event variables in your message.
4. Click ****Save****.
   - All new or unconfirmed recipients will receive an email prompting them to confirm opt-in to receive notifications from your account. See our article on the [recipient opt-in and opt-out process](https://help.klaviyo.com/hc/en-us/articles/360050242551) for more information.
   - You can see the opt-in status of each recipient based on the icon next to their email address when selecting the **Send to** dropdown.
5. Change the status to live.
   ![Dropdown of statuses for a message](https://klaviyo.zendesk.com/hc/article_attachments/28716055632923)

## View activity

When reviewing your internal alert action, you can see a summary of how many notifications are currently scheduled and how many have been sent in the left-hand panel. Scheduled alerts will appear as **Waiting.**

**![Email address of notification action recipient found in the left sidebar of the flow builder.](https://klaviyo.zendesk.com/hc/article_attachments/28716066148379)**

Click ****View details**** to view the following:

- Internal alerts that are scheduled and in **Waiting**
- Internal alerts in **Needs Review** (if the flow component is/was in manual mode)
- Internal alerts that were **Sent**
- Internal alerts that were **Skipped**

The recipient activity view shows you, for each internal alert triggered, who received the notification message and which profile they were alerted about. Keep in mind that these alerts will only send to actively confirmed recipients saved as part of your **Send to** list.

![Notification action activity tab that displays the recipients and time of notification.](https://klaviyo.zendesk.com/hc/article_attachments/28716066150427)

If all intended recipients are **Unconfirmed** or **Disabled** at send time, we will skip the internal alert entirely and you will see this reflected in the **Skipped: No Confirmed Recipients** tab of the activity view.

## Filters

Like all flow actions, internal alerts are affected by profile filters. If a profile is skipped from the rest of a flow due to filters, this will also prevent it from triggering an internal alert.

For example, say you have an internal alert at the end of your abandoned cart flow to alert you whenever someone goes through the entire flow without making a purchase. The profile filters for a typical abandoned cart flow skip someone from the flow once they make a purchase, so if they are skipped from the flow before reaching the end, they also won't trigger the internal alert.

## Additional resources

- Find out more about the internal alert action:
  - [How to opt in and out of an internal alert action](https://help.klaviyo.com/hc/en-us/articles/360050242551)
  - [Understanding internal alert action use cases](https://help.klaviyo.com/hc/en-us/articles/360049857552)
- [Getting started with flows](https://help.klaviyo.com/hc/en-us/articles/115002774932)