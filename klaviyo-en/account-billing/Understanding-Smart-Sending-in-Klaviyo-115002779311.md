---
id: "115002779311"
title: "Understanding Smart Sending in Klaviyo"
source_url: "https://help.klaviyo.com/hc/en-us/articles/115002779311-Understanding-Smart-Sending-in-Klaviyo"
section: "Message settings"
category: "Account & billing"
category_slug: "account-billing"
klaviyo_updated: "2026-04-21T13:56:37Z"
language: "en"
---
## You will learn

Learn about Smart Sending, which allows you to limit the number of emails, SMS messages, or push notifications someone can receive within a set period of time.

This is a good way to prevent your subscribers from receiving too many messages at once if you have many active flows and campaigns.

## Before you begin

Keep the following in mind when using Smart Sending:

- All channels have separate Smart Sending windows.
  - Email default: 16 hours
  - SMS default: 24 hours
  - Push notification default: 24 hours
- You can change the Smart Sending windows at any time, but it will not take effect immediately.
  - Updating the smart sending window does not retroactively affect recipients.
    - Example: If you send an email campaign and then change the email Smart Sending window from 16 to 10 hours, anyone who received that campaign will be skipped from emails with Smart Sending turned on until the full 16 hours pass.
- Messages skipped due to Smart Sending are not rescheduled automatically.
  - For information on resending emails, read [how to resend emails in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/360046797191).
  - Currently, it’s not possible to resend a text message or push notification to someone who was skipped due to Smart Sending except by doing so manually.
- If Smart Sending is off for any message, recipients can receive that message even if it’s sent before the Smart Sending window closes.
- Smart Sending for different channels (e.g., SMS and email) are managed independently and do not affect each other.
  - For instance, after someone receives an email, you can still send them an SMS the same day when Smart Sending is on. The SMS Smart Sending window only applies to SMS, and the email window only applies to emails.

****Why does changing the Smart Sending window not take effect immediately, and is there anything I can do about it?****

Think of Smart Sending like a countdown timer on each profile:

- The amount of the time is the same as the Smart Sending window at the time you send.
- The timer starts for everyone who Klaviyo tried to deliver that message to:
  - Includes those that received the message and those where the message failed after leaving Klaviyo (e.g., the message bounced, an inbox provider or wireless carrier filtered the message, etc.).
  - Does not include those skipped by Klaviyo (e.g., due to Smart Sending, flow filters, excluded lists or segments, etc.).
- The timer is specific to each profile, so the remaining amount of time on each timer varies.

Say that you do the following:

1. Send an email to your full list.
2. Change the Smart Sending window from 5 days to 1 hour.
3. Send a second email with Smart Sending.

In this example, the second email will be skipped. All subsequent emails with Smart Sending sent within the next 5 days will also be skipped.

|  |  |  |  |
| --- | --- | --- | --- |
| ****Message**** | ****Timing**** | ****Smart Sending turned on?**** | ****Received email?**** |
| Email 1 | Before changing Smart Sending | Yes | Yes |
| Email 2 | 1 hour after the change | Yes | No |
| Email 3 | 3 hours after the change | Yes | No |

The only exception is if you turn off Smart Sending for a message. In this case, 2 things will happen:

- Klaviyo will send the message to everyone on your list.
- Because Klaviyo attempted to deliver a new message, the timer will be reset to the current Smart Sending window.

Let’s add this to the example we just looked at. You:

1. Send an email to your full list.
2. Change the Smart Sending window from 5 days to 1 hour.
3. Send a second email that has Smart Sending.
4. But now, you send another email without Smart Sending.

For this last message, everyone you sent to will receive it. Furthermore, the Smart Sending window is now set to 1 hour, so you can send more messages before the rest of the 5 days is up, even when Smart Sending is turned on.

|  |  |  |  |
| --- | --- | --- | --- |
| ****Message**** | ****Timing**** | ****Smart Sending turned on?**** | ****Received email?**** |
| Email 1 | Before changing Smart Sending window | Yes | Yes |
| Email 2 | 1 hour after the change | Yes | No |
| Email 3 | 3 hours after the change | No | Yes |
| Email 4 | 6 hours after the change | Yes | Yes |

The above scenarios cover if you send all messages to all profiles, but what if the messages are sent to different groups? Or what if Klaviyo skips someone from the message without Smart Sending?

To illustrate what happens, let’s see what happens if we only send the email where Smart Sending is off to a portion of our audience.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ****Message**** | ****Group sent to**** | ****Timing**** | ****Smart Sending turned on?**** | ****Received email?**** |
| Email 1 | A and B | Before changing Smart Sending window | Yes | Yes |
| Email 2 | A and B | 1 hour after the change | Yes | No |
| Email 3 | A | 3 hours after the change | No | Yes |
| Email 4 | A and B | 6 hours after the change | Yes | A: Yes  B: No |

As you can see, group B is skipped from email 4. Because they didn’t receive email 3, their timer was not reset. Thus, Klavyo will skip them for 4 more days unless they are sent an email without Smart Sending.

The same is true for anyone who was skipped from email 3 (e.g., if they failed a filter or were excluded).

****Is there a way I can change the Smart Sending window for a profile?****

The only way is by sending a message where Smart Sending is off.

Doing so allows your message to be sent without being skipped, and it will reset the timer, updating it to the current window.

As an example, say you:

1. Send an email to your full list.
2. Change the Smart Sending window from 5 days to 1 hour.
3. Send a second email that has Smart Sending.
4. Send a third email without Smart Sending.

Now, this third message will be sent, and the timer will now be set at 1 hour.

|  |  |  |  |
| --- | --- | --- | --- |
| ****Message**** | ****Timing**** | ****Smart Sending turned on?**** | ****Received email?**** |
| Email 1 | Before changing Smart Sending window | Yes | Yes |
| Email 2 | 1 hour after the change | Yes | No |
| Email 3 | 3 hours after the change | No | Yes |
| Email 4 | 6 hours after the change | Yes | Yes |

## Change the Smart Sending timeframe

As mentioned the Smart Sending timeframes for email, SMS, and push are separate, so you can adjust one without affecting the other.

### Email Smart Sending window

By default, the email Smart Sending window is 16 hours.

1. Navigate to your organization name in the bottom left corner of your screen.
2. Click ****Settings****.
3. Select ****Email > Sending preferences****.
4. Update the number of hours under **Smart Sending Period**.
   ![Smart sending modal](https://klaviyo.zendesk.com/hc/article_attachments/33469179056923)
5. Check the box to ****Ignore transactional messages**** if you send [transactional emails](https://help.klaviyo.com/hc/en-us/articles/360003165732).
   - In almost all cases, Smart Sending should remain disabled for transactional emails, as these are messages that customers anticipate receiving and search for in their inboxes.

### SMS Smart Sending window

By default, the SMS Smart Sending window is 24 hours.

1. Navigate to your organization name in the bottom left corner of your screen.
2. Click ****Settings****.
3. Select ****SMS > Sending preferences****.
4. Edit your Smart Sending period within the **SMS Sending Settings** area.

For SMS, you can set distinct Smart Sending timeframes for campaigns and flows.

![](https://klaviyo.zendesk.com/hc/article_attachments/30910478392219)

### Push notification Smart Sending window

1. Navigate to your organization name in the bottom left corner of your screen.
2. Click ****Settings****.
3. Select ****Push notifications****.
4. Edit your Smart Sending period within the **Push Sending Settings** area.
5. Click ****Update Push Sending Settings****.
   ![Push smart sending settings](https://klaviyo.zendesk.com/hc/article_attachments/33469155306651)

## Disable Smart Sending for a message

### Campaigns

Smart Sending is enabled by default for all campaigns. You can choose to disable Smart Sending on a per-campaign basis. We recommend keeping Smart Sending turned on for most, if not all, marketing emails.

In step 1 of the campaign, toggle off the option to:

- Email: Skip profiles who recently received an email.
  ![](https://klaviyo.zendesk.com/hc/article_attachments/30910487106843)
- SMS:
  - Skip profiles who recently received a campaign message.
  - Skip profiles who recently received a flow message.
    ![](https://klaviyo.zendesk.com/hc/article_attachments/30910478399003)
- Push: Skip profiles who recently received a push message.

### Flows

Smart Sending is enabled for flow messages in many pre-built flows. If you are using a pre-built flow, and Smart Sending is enabled, you can choose to turn it off for individual flow messages.

1. Click on an individual flow message.
2. Scroll down to **Skip recently email profiles**.
3. Toggle off ****Smart Sending****.

![Smart sending option for flow email](https://klaviyo.zendesk.com/hc/article_attachments/33469155313051)

Note that SMS Smart Sending uses the phone number to determine if a message to a profile should be skipped. If multiple profiles share the same number, and that number has received an SMS message within the Smart Sending window, any new messages to that number will be skipped, regardless of which profile triggers the send.

## Smart Sending and A/B testing

[A/B tests](https://help.klaviyo.com/hc/en-us/articles/115005228148) that receive no results due to Smart Sending are automatically cancelled. This means that everyone in the test pool for your A/B test campaign got skipped because they received another message too recently. If you receive an in-app notification like the one below, your A/B test has been canceled and you need to resend your campaign to reach your recipients.

## Additional resources

- Check out [how to resend emails in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/360046797191)
- Find out more about A/B testing:
  - [A/B testing campaigns](https://help.klaviyo.com/hc/en-us/articles/115005228148)
  - [A/B testing an individual flow message](https://help.klaviyo.com/hc/en-us/articles/6960371049115)