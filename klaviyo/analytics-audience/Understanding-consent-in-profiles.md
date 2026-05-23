---
id: 360037101072
title: "Understanding consent in profiles"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360037101072-Understanding-consent-in-profiles"
section: "Understand profiles"
category: "Audience"
category_slug: "analytics-audience"
klaviyo_updated: "2026-04-23T10:23:49Z"
language: en
---

## You will learn

Learn how to understand consent in profiles and best practices for email and SMS compliance.

Rules around customer consent vary between email and SMS. It is crucial to understand these differences to comply with international laws and maintain a positive relationship with your customers.

## Viewing a profile’s consent status

To see if a profile is able to receive messages and has provided consent, navigate to their profile.

At the top of the **Details** tab of a profile page, you'll see the profile’s consent status and ability to receive messages by channel. The different statuses you may see are:

The oldest consent record that can be set in Klaviyo is January 1, 1990. If you see this date is set as the timestamp for a consent record in Klaviyo, this is because an earlier date was set and the timestamp was updated to the minimum consent date possible in the system.

- ****Subscribed****
  The **Subscribed** status (represented by a green checkmark) indicates that the profile has provided explicit consent to receive marketing and is reachable through the channel.



  ![Subscribed to email on a profile](https://klaviyo.zendesk.com/hc/article_attachments/32433846149019)
  ![Subscribed to SMS marketing on a profile](https://klaviyo.zendesk.com/hc/article_attachments/32433892790811)
  ![Subscribed to SMS transactional on a profile](https://klaviyo.zendesk.com/hc/article_attachments/32433892792219)
  ![Subscribed to mobile push marketing on a profile](https://klaviyo.zendesk.com/hc/article_attachments/32433892795931)
- ****Unsubscribed****
  **Unsubscribed** (represented by a red indicator) means that the profile is unable to receive marketing through the channel because they have explicitly opted-out. Note that consent status and suppression status are separate from each other. For example, a profile that is subscribed can be manually suppressed.
  ![Unsubscribed status for SMS](https://klaviyo.zendesk.com/hc/article_attachments/32433892802587)
- ****Never subscribed****
  **Never subscribed** (represented by a yellow exclamation) means the profile has neither subscribed nor opted out of email marketing. They are able to receive emails since they are not suppressed (e.g., an abandoned cart flow email), but you should exercise caution when contacting them.

![Never subscribed status shown on profile](https://klaviyo.zendesk.com/hc/article_attachments/28722595585051)

SMS consent is separated into SMS marketing and SMS transactional. In both cases, profiles need to provide express consent in order to receive messages. Profiles with a status of **Unsubscribed** or **Never Subscribed** for SMS are not able to receive messages through the channel until they opt in and will have a red indicator. Currently, if someone opts out of SMS marketing, it also opts them out of transactional (and vice versa).

By expanding a channel, you can see additional details around the profile’s subscription status.

![SMS channel expanded to show details](https://klaviyo.zendesk.com/hc/article_attachments/28722595589787)

If a profile is not able to receive messages because they are suppressed, there are details around their suppression at the bottom of the channel when expanded.

![Consent channel expanded to show suppression reason](https://klaviyo.zendesk.com/hc/article_attachments/28722595588379)

Unsubscribed and spam complaints are not displayed as a suppression reason in this section. If these suppressions exist, the profile will always have an unsubscribed consent status.

For more information on suppression and unsubscribes, see our guide on [suppressed profiles](https://help.klaviyo.com/hc/en-us/articles/115005246108) in Klaviyo.

## Profiles that have never subscribed

There are certain methods of adding a profile that results in a consent status of **Never Subscribed**. If this is the case and the person is not suppressed, the profile shows a yellow exclamation mark for that channel. For example, subscribers that provided their information when starting a checkout without opting in to email marketing, would have a consent status of **Never Subscribed**.

You can only send emails to these profiles; you cannot send them SMS marketing, SMS transactional, or mobile push messages. And even with email, you should exercise caution when contacting them. Depending on your local regulations you may be permitted to email these profiles if you believe they have implied consent. Make sure to [use good list cleaning practices](https://help.klaviyo.com/hc/en-us/articles/115005078347) and consider each contact’s [engagement](https://help.klaviyo.com/hc/en-us/articles/115000200072) when deciding whether to send to them.

Klaviyo recommends that you only email profiles with express consent to protect your deliverability and sender reputation.

## Email

When someone subscribes to one of your lists (e.g., through a signup form) their consent status is marked as **Subscribed** in Klaviyo. This results in the creation of their profile in your account (if it does not already exist) and a green checkmark representing their subscription status.

![Channel expanded to show subscription details](https://klaviyo.zendesk.com/hc/article_attachments/28722557214491)

****Consent vs. suppression status****

### GDPR

In some cases, international laws will affect email consent. A prime example of this is GDPR, which governs residents of the EU. For information on how to remain compliant and access appropriate consent for EU customers, please see our article on [collecting GDPR-compliant consent.](https://help.klaviyo.com/hc/en-us/articles/360003536031)

### Best practice

It is best practice to have [double opt-in](https://help.klaviyo.com/hc/en-us/articles/115005251108) enabled in your account. This means that, when a customer subscribes via a signup form or other subscription method, they will receive a confirmation email to verify that they want to subscribe. Double opt-in ensures that you [maintain good deliverability](https://help.klaviyo.com/hc/en-us/articles/115000201131) and avoid spam traps that negatively affect your sender reputation.

Klaviyo also requires that you include an unsubscribe link in all of your emails. This is required by US law and ensures a seamless experience for your customers, improving email deliverability. It is always better that someone unsubscribes from your content rather than marks it as spam. You can [customize your unsubscribe link](https://help.klaviyo.com/hc/en-us/articles/115006054267) as well to fit your business style and needs.

## SMS marketing and transactional

[SMS consent](https://help.klaviyo.com/hc/en-us/articles/360035056972) is collected separately from email consent. If you have email consent for a profile, that does not mean that you can legally send that same contact text messages and vice versa.

In order to send an SMS message to a profile, you must collect their SMS consent. You can ask for SMS consent in a landing page on your site, prompt website visitors to subscribe in a signup form, or request it from email subscribers in a campaign. To learn more about how to gain SMS consent, head to our [guide on collecting SMS subscribers](https://help.klaviyo.com/hc/en-us/articles/360035056972).

SMS marketing consent includes the ability to send a profile transactional messages, but the opposite is not true. If someone only has SMS transactional consent, they can only receive SMS transactional flow or conversational messages.

Once SMS consent is provided by a profile, you will see another green checkmark denoting their consent status next to their phone number on the **Details** tab of the profile page.

![both sms marketing and transactional.png](https://klaviyo.zendesk.com/hc/article_attachments/31776540001051)

SMS consent is only associated with the specific phone number that opts in. If the phone number for a profile changes after the initial opt-in, the customer needs to subscribe again with the new number.

### Best practices

Like email, double opt-in for SMS marketing is highly recommended, although not for SMS transactional. This will confirm that the phone number of the recipient is legitimate, provide you with a record of consent, and allow text message recipients to opt-out if they change their mind.

A recipient marking a text message as spam carries greater consequences than a recipient marking an email as spam. If you are reported as spam by recipients, you may be subject to hefty fines. [SMS consent laws](https://help.klaviyo.com/hc/en-us/sections/360000775792) depend on the country. To comply with their laws, Klaviyo requires that you send certain keyword responses to customers. These keyword responses are free of charge and can be edited. Note that any optional keywords, such as [custom subscribe keywords](https://help.klaviyo.com/hc/en-us/articles/360050384091), are not free.

![Keywords responses that are sent in Klaviyo](https://klaviyo.zendesk.com/hc/article_attachments/28722557186843)

## Mobile push notifications

In order to send a push notification to a profile, you must collect their [explicit consent](https://help.klaviyo.com/hc/en-us/articles/4404203889947) first.

Push notification consent is collected separately from email and SMS consent. If you have consent for a different channel, that does not mean that you can send push notifications to that contact until they specifically opt in to receive push notifications.

Once a profile grants consent, you will see a green check mark denoting their consent status on their profile page.

![Push channel expanded to show details](https://klaviyo.zendesk.com/hc/article_attachments/28722557222427)

### Best practices

To collect push notification consent, you must provide customers with a permission screen prompt during their first interaction with your mobile app. It is best practice for your permission screen prompt to include consent language that provides the following information and allows them to opt in or opt out:

- ****What types of notifications your brand sends****
  Include details about the different push notifications your brand plans to send (for example, account changes, reminders, and special discounts).
- ****Why users should opt in****
  Include information around why a customer should provide permissions (for example, to receive important updates or early access to sales).

Learn more about collecting [push notification consent](https://help.klaviyo.com/hc/en-us/articles/14781686592283) and best practices.

## Updating subscriptions and suppressions

You can update subscriptions and suppressions for a recipient on the **Details** tab of the profile page as well.

### Resubscribe or remove suppressions from a profile

If a profile has unsubscribed or marked an email as spam, you can resubscribe them if necessary. Ensure that this profile would like to be subscribed and receive marketing before resubscribing.

To resubscribe a profile that is unreachable because they unsubscribed or marked an email as spam, click on the menu next to the consent indicator for the profile:

![Option to resubscribe a profile](https://klaviyo.zendesk.com/hc/article_attachments/28722595594139)

You can also remove any suppressions for profiles that may be suppressed from specific lists.

When a profile is suppressed from a specific list, you can remove that list specific suppression by selecting ****Remove**** for the appropriate list.

![Profile suppressed from a specific list](https://klaviyo.zendesk.com/hc/article_attachments/28722557218715)

Klaviyo does not support sending SMS or mobile push marketing to profiles that have a consent status of **Never Subscribed**. To receive SMS messages, a profile must opt-in to the channel.

### Suppress or unsubscribe a profile

You can also suppress and unsubscribe a profile on the **Details** tab. To do this, click on menu next to the consent indicator on a profile:

![Suppress and unsubscribe option for subscribed profile](https://klaviyo.zendesk.com/hc/article_attachments/28722557221147)

## Subscription events

When a profile provides consent to receive marketing, Klaviyo sets an event on the profile to capture this. This event is set when the profile successfully subscribes to a channel, and was previously never subscribed, unsubscribed, or manually suppressed.

Depending on the channel a profile has subscribed to, these events are:

- ****Subscribed to email marketing****
- **Subscribed to SMS marketing**
- **Subscribed to SMS transactional**

If a profile is added to a list when they subscribe, the **Subscribed to list** event will also appear on their event timeline.

Prior to March 29, 2024 the **Subscribed to email marketing** event was only emitted when a profile subscribed to email marketing without being added to a list. **Unsubscribed from email marketing** events are only emitted beginning March 29th, 2024 as well.

When profiles unsubscribe, events are also captured on their event timeline to reflect this. The **Clicked and Unsubscribed from Email** event is emitted when a profile clicks the unsubscribe link in an email to unsubscribe from email marketing. This event is only set when a profile takes action to unsubscribe themselves by clicking on the link in an email.

The **Unsubscribed from Email marketing** event is also set whenever a profile has email marketing consent removed, including when it's done manually for a profile by a user on your account or through Klaviyo’s APIs.

Additionally, if a profile is removed from a list when they unsubscribe, the **Unsubscribed from list** event will also appear on their event timeline.

For SMS marketing, the **Unsubscribed for SMS** event is set whenever a profile is unsubscribed for the SMS channel.

You can use these subscription events to understand when profiles have opted in and out of a channel, and can be segmented on to create groups of profiles with similar subscribe or unsubscribe dates.

If subscription events are being sent to your account with a timestamp in the past, flows will not be triggered. In order for subscriptions to trigger flows, the **historical\_import** flag must be set to false (i.e., the default value) when making requests through Klaviyo’s [Subscribe Profiles](https://developers.klaviyo.com/en/reference/subscribe_profiles) API endpoint, and the subscription date will be set to the current date.

## Onsite tracking

By enabling basic [onsite tracking](https://help.klaviyo.com/hc/en-us/articles/115005076767) on your website, you can collect helpful information around browsing activity that can be leveraged to further personalize your marketing.

When you add onsite tracking to your site, Klaviyo only tracks the browsing activity of "known browsers;" i.e., browsers that have visited, engaged, and been identified (or "[cookied](https://help.klaviyo.com/hc/en-us/articles/360034666712)") at least once before. Klaviyo will not track anonymous browsers.

There are 2 main ways Klaviyo is able to identify customers and cookie them so they are tracked during all future visits to your page and their onsite behavior tracked:

A visitor will be identified when they:

- Submit a Klaviyo sign-up form
- Click a link from a Klaviyo email

For Shopify users, based on your Customer Privacy settings, Klaviyo may not track onsite events for visitors to your store in the EU, EEA, UK, and Switzerland unless they have provided consent.