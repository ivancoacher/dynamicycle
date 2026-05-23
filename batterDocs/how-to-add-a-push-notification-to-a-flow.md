<h1>How to add a push notification to a flow</h1>

## You will learn

Learn how to use Klaviyo to send push notifications from your iOS or Android app via flows.

Sending push notifications in flows allows you to complement your email or SMS strategy. For example, you may want to send abandoned cart push notifications in addition to email reminders.

Just like in SMS and emails, you can use emojis, variables, and template tags to personalize push messages.

## Before you begin

Before you can send push notifications, note that:

- You have to [set up push notifications](https://help.klaviyo.com/hc/en-us/articles/360023213971) in your Klaviyo account.
- Only app users that consent to notifications will receive push notifications from you. When an app user opts in to receive notifications, they will get a push token that allows you to target them with notifications through both campaigns and flows in Klaviyo.

Note that what you can do with flows depends on how you integrate your app with Klaviyo. For instance, if you want to send messages about your app’s loyalty program, related events (e.g., reached 100 stars) must sync into Klaviyo. We recommend working with your development team or a third party to make sure the proper data and events are tracked.

****Common use cases****

Push notifications are often used in flows, including:

- Welcome series
- Abandoned cart and browse abandonment notifications
- Thank you flows
- Fulfillment flows (e.g., order shipped or ready for in-store pickup)
- Winback flows
- Wish list notifications
- App loyalty program messages
- Profile alerts (e.g., complete your profile)

## Push notifications in flows

To use this feature:

1. Navigate to the ****Flows**** tab.
2. Either create a new flow or edit an existing one.
3. Drag the push notification action into your flow.
4. In the **Content** tab, select the type of push notification you want to send:
   - ****Standard****
     Display a push notification on users’ lock screens.
   - ****Silent****
     Send a [hidden notification](https://help.klaviyo.com/hc/en-us/articles/34331926591003) to your user’s mobile app.
5. For both standard and silent push notifications:
   - Select the ****Behaviors**** tab.
   - Under ****Custom data****, you can include key-value pairs along with your notification to trigger app behaviors from both standard and silent push notifications. You can add up to 10 key-value pairs per push. Learn about [key-value pairs](https://help.klaviyo.com/hc/en-us/articles/34331971195675).
     ![](https://klaviyo.zendesk.com/hc/article_attachments/36088735596187)
6. The following push settings apply to standard push notifications:
   - In the ****Content**** tab, configure your message’s title and content. The character limit for push notifications is 178 characters.
   - Optional: add an image or GIF (iOS only).
   - Click into the ****Behaviors**** tab to adjust the following message settings:
     - ****Open action****Choose whether you want subscribers to go to your app's home page (open app) or to a specific page (deep link).
     - ****Show badge count (iOS****)
       Decide if you want the badge count to increase by 1, be set to a certain number, or be set to the value of a specific property.
     - ****Sound (iOS)****
       Choose if you would like subscribers to hear a sound when they receive the push notification.
7. Optional: Edit the push notification component settings:
   - ****Skip recently messaged profiles****This setting enables [Smart Sending](https://help.klaviyo.com/hc/en-us/articles/115002779311). We recommend leaving this setting on for any high-revenue and transactional flows, and turning it off for any silent push.
   - ****Additional Filters****If you would only like certain people to receive a push notification, you can edit the [additional filters](https://help.klaviyo.com/hc/en-us/articles/115002779111) to further hone your audience. Additional filters are not recommended for silent push notifications.
8. Once you're finished configuring your push notification, set it live.

## Additional resources

- [How to use deep links in push notifications](https://help.klaviyo.com/hc/en-us/articles/14750403974043)
- [How to create a push notification campaign](https://help.klaviyo.com/hc/en-us/articles/360006653972)
- [Understanding your push notification settings](https://help.klaviyo.com/hc/en-us/articles/12932500186907)
