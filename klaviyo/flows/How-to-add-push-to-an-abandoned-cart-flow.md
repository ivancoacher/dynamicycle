---
id: 16839379548571
title: "How to add push to an abandoned cart flow"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/16839379548571-How-to-add-push-to-an-abandoned-cart-flow"
section: "Abandoned cart flows"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-04-21T13:54:30Z"
language: en
---

## You will learn

Learn how to add push notifications to your abandoned cart flow to diversify the types of communication sent to your customers.

## Before you begin

Learn [how to create an abandoned cart flow](https://help.klaviyo.com/hc/en-us/articles/115002779411-How-to-create-an-abandoned-cart-flow) if you don’t have one set up in your account yet.

Before you can send push notifications, note that:

- You must [set up push notifications](https://help.klaviyo.com/hc/en-us/articles/360023213971) in your Klaviyo account.
- Only app users that consent to notifications will receive push notifications from you. When an app user opts in to receive notifications, they are assigned a token that allows you to target them with push notifications through both campaigns and flows in Klaviyo.

## Add a push notification to your abandoned cart flow

Follow these steps to add push to your abandoned cart flow:

1. From the main Klaviyo navigation, head to the ****Flows**** tab.
2. Click the name of your abandoned cart flow to open it in the flow builder.
3. After the first time delay, add a conditional split with the condition: **If someone can or cannot receive marketing >** Person **cannot receive > mobile push marketing**.

   This allows you to keep your existing flow on the left side in the YES path while you add your push notifications to the NO path. With this split, you can send a push notification to those subscribed to push and send a different type of message (e.g., email or SMS) to those who are not subscribed to receive push notifications.
   ![Abandoned cart flow with a conditional split that checks if a profile cannot receive push](https://klaviyo.zendesk.com/hc/article_attachments/29158784347803)
4. In the left sidebar, drag the push notification action into the NO path of your push conditional split.
   ![Abandoned cart flow with a push notification message added to the NO path of the split](https://klaviyo.zendesk.com/hc/article_attachments/29158784353051)
5. Optional: In the sidebar, choose whether you would like to enable/disable [Smart Sending](https://help.klaviyo.com/hc/en-us/articles/115002779311) via the **Skip recently messaged profiles** setting. This setting is disabled by default. We recommend keeping it on for abandoned cart flows.
6. Click ****Edit**** next to **Content**. Under **Type**, choose ****Standard****.
7. Configure the title (optional) and body of the message, such as:
   “Did you forget something? Click here to return to your cart”
   “Your cart is about to expire!”
8. Optional****:**** If you have a static coupon that is usable by all customers, you can include this in your push notification. For dynamic coupons, consider adding an email or SMS to your push notification path, since someone can easily refer back to an SMS or email as opposed to a push notification.
   In the example below, a customer is notified of their abandoned cart through push and then sent a coupon through email or SMS a few days later. They are then reminded of the coupon through push a few more days later.
   ![Example of a flow which first sends a push notification and then sends either an email or SMS.](https://klaviyo.zendesk.com/hc/article_attachments/28722598280859)
   An abandoned cart flow’s filters will remove someone from the flow if they place an order, so if they are still in the flow, you know they haven’t used their coupon. You can add multiple push notifications with delays leading up to the expiration of the coupon, but don’t send a notification every day as this can overwhelm them.
9. Select the ****Behaviors**** tab and select the open action for when the recipient taps the notification. To link a customer back to their cart, choose ****Deep link**** and enter a URL that links the customer to their cart in your app to the relevant field for either iOS or Android. Whether or not this is possible and the exact URL will depend on the design of your app. Consult your development team if you are unsure about this.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/36088733830171)
10. Configure the following optional behaviors:
    - ****Show badge count (iOS only)****Show the badge count on the message.
    - ****Play sound (iOS only)****
      Play a sound when the recipient receives the message.
    - ****Custom data****
      Trigger app behaviors via [key-value pairs](https://help.klaviyo.com/hc/en-us/articles/34331971195675).
11. When you're done with the message settings and content, click ****Save & continue****.
12. Once you're finished configuring your flow, set your message statuses live.

## Best practices

### Message content

Make sure your push notifications contain relevant and actionable information related to your customer’s cart. Avoid overusing emojis. Multiple repeating emojis are often associated with spam.

Here are some examples of content to include in your push notification messages:

- Let them know they have an abandoned cart.
- Alert them that their cart is going to expire.
- Remind them to use a coupon.

If you mention a coupon code in a push notification, make sure that you have included it in an email or SMS first so that the customer can go back and reference it. You can also send it to the profile’s in-app inbox or show it in a banner within the app.

### Message channel diversity

Don’t send push notifications at the same time as other types of messages. Subscribers may already have notifications set up for when they have received an email or SMS, so receiving a push notification at the same time can be redundant.

While push notifications are convenient and helpful, focus on other types of messages such as SMS and email. In an abandoned cart flow, your primary means of communication with your customers will be through email or SMS messages. Unlike with push, SMS and email can include information such as the list of products the customer abandoned.

### Separate email, SMS, and push

If you are using email, SMS, and push, make sure to have splits that check for push and SMS consent individually while making email the default message type. See the example below:

![Example flow which has conditional splits that check for push and SMS consent respectively.](https://klaviyo.zendesk.com/hc/article_attachments/28722598283547)

### Split based on website activity

You can also use splits to send different messages depending on if someone has visited your website before or has only used your app. This is useful if you want to encourage app-only users to visit your website for exclusive promotions and content.

In the example below, a conditional split with the condition **What someone has done (or not done) > Active on Site > at least once > over all time** is used to check if the person in the flow has ever visited your website. If they have not, but they are subscribed to push, then you know that they have only used your app.

![Conditional split configured to check if someone has triggered Active on Site at least once over all time.](https://klaviyo.zendesk.com/hc/article_attachments/21912959707547)

### Split based on custom metrics

If you are using custom metrics to track customer activity in your app, you can split based on these metrics in order to send exclusive coupons or promotional information. Consider implementing custom metrics that track activity such as:

- Profile completed
- Location added
- App rated

Someone completing the actions listed above is engaged with your app. If you want to reserve abandoned cart coupons only for engaged profiles, using customer metrics in a split is a great way to do this.

## Additional resources

Find out more about abandoned carts:

- [How to add SMS to your abandoned cart flow](https://help.klaviyo.com/hc/en-us/articles/9352115400219-How-to-add-SMS-to-your-abandoned-cart-flow)
- [How to create and target a segment of recent cart abandoners](https://help.klaviyo.com/hc/en-us/articles/360032334511-How-to-create-and-target-a-segment-of-recent-cart-abandoners)
- Learn how to [troubleshoot your abandoned cart flow](https://help.klaviyo.com/hc/en-us/articles/12278373016603-Troubleshooting-a-metric-triggered-flow).