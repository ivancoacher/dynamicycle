---
id: 15038587235995
title: "How to create a push welcome series"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/15038587235995-How-to-create-a-push-welcome-series"
section: "Welcome series flows"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-04-21T13:54:29Z"
language: en
---

## You will learn

Learn how to add push notifications to your welcome flow to target those who download your mobile app.

## Before you begin

Unlike with email and SMS welcome flows, a push welcome series is not triggered when someone subscribes to a list or opts in to SMS. Your development team must configure a custom metric using [Klaviyo’s APIs](https://developers.klaviyo.com/en/docs/get_started) that triggers when someone installs or otherwise takes a specific action in your mobile app.

Before you can send push notifications, note that:

- You have to [set up push notifications](https://help.klaviyo.com/hc/en-us/articles/360023213971) in your Klaviyo account.
- Only app users that consent to notifications will receive push notifications from you. When an app user opts in to receive notifications, they will be assigned a push token that allows you to target them with notifications through both campaigns and flows in Klaviyo.

## Create a welcome series for app users

There are 2 ways you can set up a welcome flow for push subscribers:

- Recommended: Use a custom metric from your app (e.g., signed up for app).
- Create a segment based on if someone can receive mobile push marketing and trigger a segment-triggered flow.
  - Note that segment-based flows can take longer to trigger than metric-based flows, so this is not recommended unless your app has no way to sync new users to Klaviyo.
    ![](https://klaviyo.zendesk.com/hc/article_attachments/30481906425627)

### Add a push notification action

Follow these steps to create a welcome series for your push subscribers triggered by a custom metric:

1. Using the main Klaviyo navigation, go to the ****Flows**** tab.
2. Create a new metric-triggered flow triggered by your app’s custom metric or a segment-triggered flow triggered by your segment of subscribers that can receive push marketing.
3. Click the trigger of the flow.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/34451446507547)
4. Next to **Profile filters**, click ****Add****.
5. Add a profile filter to remove anyone who has ever been in this flow. See the example below:
   ![Example filter with definition 'has not been in this flow at any time.'](https://klaviyo.zendesk.com/hc/article_attachments/28704478303643)
6. From the left sidebar, drag the push notification action into your flow.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/34451463052699)
7. Edit the message title and body, typically to thank the person for downloading your app. Example:
   “Thanks for joining our app!”
   ![](https://klaviyo.zendesk.com/hc/article_attachments/34451446513819)
8. Select the ****Behaviors**** tab.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/34451446519963)
9. Select what should happen when a recipient taps on the notification - open app, or deep link.
10. For iOS:
    - Choose whether to show a badge count.
    - Choose if you would like subscribers to hear a sound when they receive the push notification.
11. Optional: Toggle on ****Custom data**** and include [key-value pairs](https://help.klaviyo.com/hc/en-us/articles/34331971195675) along with your notification to trigger app behaviors.
12. When you are done, click ****Save & continue****.
13. In the **Push notification details** sidebar, choose whether you would like to ****Skip recently messaged profiles****, which enables/disables [Smart Sending](https://help.klaviyo.com/hc/en-us/articles/115002779311). This setting is disabled by default. We recommend keeping it off for welcome series flows.
    ![](https://klaviyo.zendesk.com/hc/article_attachments/34451446524955)
14. Optional: Add additional filters to the push notification.
15. Add a time delay after this message.
    Note****:**** Like with SMS, push notifications ping a recipient’s phone, so sending too often may overwhelm your recipients. For larger flows, such as those with more than 3 messages, avoid sending a push notification every day.
16. Add and configure 2-3 push notifications, adding time delays between each message.
17. Once you're finished configuring your push notifications, [set the status to live](https://klaviyo.zendesk.com/hc/en-us/articles/360048376172).

## Best practices

### Message content

Make sure your push notifications contain relevant and actionable information related to your app. Avoid overusing emojis. Multiple repeating emojis are often associated with spam.

Here are some examples of content to include in your push notifications listed in order of importance:

- Thank people for subscribing.
- Remind them to fill out their profile.
- Remind them to set their location.
- Ask for feedback on your app’s setup experience.
- Mention any features that are relevant to a new app user.

### Split based on customer actions

Depending on the content of your push notifications, you may want to use conditional splits to check if a customer has performed specific actions (e.g., set up their profile) before sending a relevant notification. Depending on your app’s design, you must either set up custom metrics or custom profile properties to use with these splits.

![Example flow that checks for the profile property App Profile Complete](https://klaviyo.zendesk.com/hc/article_attachments/28704486399003)

The above example shows a flow triggered by a segment of profiles with who can receive push marketing. If a custom metric is used instead of a segment, use a conditional split to check for the ability to receive push marketing or flow filters to filter out profiles that do not have a push token.

### Time delays

Make sure to add appropriate time delays between your push notifications so you are not overwhelming your subscribers.

For a welcome series flow, we recommend the following delays:

- Message #1: no delay
- Message #2: 1 day
- Message #3: 3 days
- Other messages: 3+ days

## Troubleshooting

If you are using a custom metric to trigger your flow and it is no longer triggering, contact the developer who configured this metric for your custom integration or the developer of your third-party integration for further assistance.

If you are using a segment-triggered flow but it is not triggering, make sure your segment has “someone can receive mobile push marketing” as part of the definition.

Segment-triggered flows only send to people who enter the segment after the flow is set live. If you’d like to send to older segment members, [learn how to add past profiles to a flow](https://help.klaviyo.com/hc/en-us/articles/360049924272).

## Additional resources

Learn about other actions you can use in your flow:

- [How to add an update profile property action to a flow](https://help.klaviyo.com/hc/en-us/articles/360001768432-How-to-add-an-update-profile-property-action-to-a-flow)
- [How to add a notification action to a flow](https://help.klaviyo.com/hc/en-us/articles/360050242251-How-to-add-a-notification-action-to-a-flow)