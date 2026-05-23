---
id: 115005251108
title: "Understanding the double opt-in process"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005251108-Understanding-the-double-opt-in-process"
section: "Build and use lists"
category: "Audience"
category_slug: "analytics-audience"
klaviyo_updated: "2026-05-11T10:59:30Z"
language: en
---

## You will learn

Learn the difference between single and double opt-in, why double opt-in is important for both SMS and email, and how to update the opt-in settings for a list or keyword in Klaviyo.

## What is double opt-in?

Double opt-in is a process through which a new subscriber must confirm their subscription before being subscribed to a given list. It is the same for both email and SMS subscribers.

Double opt-in can be set at the list level. If a list has double opt-in, everyone who subscribes to that list must confirm their interest before they're added through a confirmation message sent immediately after signing up. This message will prompt them to confirm their subscription. Only subscribers who confirm their subscription will be successfully added to the list, and get queued for a welcome series.

Double opt-in also exists for SMS keywords. For subscribers that opt in through an SMS keyword, the keyword’s opt-in settings will override the list’s.

You should always use double opt-in for SMS lists. Carriers often require it, particularly for abandoned cart messages.

### How does double opt-in work with branded sender IDs?

Branded sender IDs cannot receive text messages, so there's no way for a subscriber to confirm that they want to opt in. Thus, for any country where you're using a branded sender ID, the double opt-in confirmation text is skipped automatically.

However, if you are on a paid plan should, consider using Smart Opt-in as a default for collecting SMS consent. Collecting SMS consent via Smart Opt-in is similar to the double opt-in process in that visitors take 2 steps to opt in: entering their phone number, and then inputting the one-time code that they receive.

### How does double opt-in work with SMS transactional?

Currently, double opt-in does not work with SMS transactional consent. Anyone who signs up for only transactional SMS will not get a confirmation message. Instead, transactional SMS consent is added immediately to the profile.

If someone opts in to both transactional and promotional SMS, transactional consent is added immediately to the profile, but the double opt-in text sends for promotional consent. In this case, you'll be able to send transactional SMS, but you cannot send promotional SMS until the profile confirms via double opt-in.

## Why is double opt-in important?

When you add a signup form to your site, you are not able to control who decides to take advantage of this form. Even if you add an extra level of validation, it isn’t always possible to ensure subscribers only submit valid or accurate email addresses and phone numbers. Well-intentioned subscribers could simply type their email or phone number incorrectly, but spam-bots could also find your form and flood it with fake email addresses or phone numbers.

The double opt-in process helps you grow your list while also minimizing abuse and preventing the accumulation of invalid or mistyped emails and phone numbers. For email in particular, this is important because most major email clients (like Google and Yahoo) track how recipients interact with emails from your domain — how many are marked as spam, how many are opened, how many bounce, etc.

They use this information to determine whether your emails are classified as spam. Having a lot of uninterested people or a lot of invalid emails on your list will only hurt your efforts to reach those that actually want to receive your emails.

List imports do not trigger double opt-in.

## Update opt-in settings

In some specific cases, you may want to remove double opt-in and make your list single opt-in. Most often, brands choose to implement single opt-in when they are using other third-party signup forms or tools and their customers are prompted with a double opt-in confirmation at some other point in the signup workflow. For example, if your third-party signup form has a double-opt in feature enabled, you might want to disable double opt-in on your Klaviyo list so customers don't experience multiple opt-in confirmation messages.

Single opt-in is not recommended for SMS, as double opt-in is required by some carriers and for abandoned cart messages (in the US and Canada).

New lists are created with your [default opt-in setting](https://www.klaviyo.com/settings/account/api-keys). Changing this setting will not update existing lists, to enable single opt-in for a given list:

1. Click into the list you want to edit.
2. Select ****Settings****.
3. Select ****Consent****.
   ![consent tab.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28717991555099)
4. Check the box next to **Single opt-in.**
   ![single opt in settings.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28717985684379)
5. Click ****Save****.

Once this setting changes, when someone subscribes — to email, SMS, or both — they will not need to confirm their subscription. For instance, if someone subscribes via a form and the list they're sent to is single opt-in, they will be added to that list immediately.

SMS keywords are set to single opt-in by default. However, you can control the opt-in settings for keywords as well.

To change the opt-in settings for a keyword:

1. Click your organization name in the lower left corner.
2. Navigate to ****Settings > SMS > Automations****.
3. Find the **Subscribe Keywords** section.
4. Expand the menu for your desired subscribe keyword and select the ****Edit**** button to set your desired opt-in status.

![keywordoptin.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28717991544219)

## API double opt-in settings

If you are collecting consent using [Klaviyo’s APIs](https://developers.klaviyo.com/en/docs/collect_email_and_sms_consent_via_api), the double opt-in behavior is based on whether a profile is being subscribed with or without a list.

### With a list

When subscribing a profile via API with a list, the list’s opt-in settings determine the opt-in process used to subscribe the profile for that API call. The account's [default opt-in settings](https://www.klaviyo.com/settings/account/api-keys) will have no impact on the behavior here when a list is a provided.

### Without a list

When subscribing a profile via API without a list, the opt-in process used to subscribe the profile depends on the account's [default opt-in settings](https://www.klaviyo.com/settings/account/api-keys).

## What happens if someone does not confirm subscription

If someone subscribes to a list via a [subscribe page](https://help.klaviyo.com/hc/en-us/articles/115005251988) with double opt-in enabled, a profile will not be created until the customer confirms their subscription.

If someone subscribes to a list via a Klaviyo signup form or keyword set to double opt-in, but fails to confirm the double opt-in message, Klaviyo creates a blank profile for this individual. That means that this contact is not added to a list and has no further information or activity listed on their profile other than the form’s general properties (such as first name, last name, email address, and phone number).

However, if you use a third-party form, or the signup is passed through our API, Klaviyo will not create an empty profile— instead the subscriber will only sync into your account if they’ve confirmed opt-in.

At this stage, the contact may become [cookied](https://klaviyo.zendesk.com/hc/en-us/articles/360034666712), meaning their future interactions with your brand will be tracked as events on their profile. This means that they can be added to behavior-based segments, even though they are not subscribed to any particular list. It's important to note that these profiles cannot be identified with UTM tracking as Klaviyo does not track who confirms the double opt-in message.

Double opt-in emails are valid for 72 hours.

## Additional resources

- [Understanding opt-in related pages for a list](https://klaviyo.zendesk.com/hc/en-us/articles/115005251848)
- [Why having a single main list is beneficial](https://klaviyo.zendesk.com/hc/en-us/articles/360043947571)