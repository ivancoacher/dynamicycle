---
id: 115005246108
title: "Understanding suppressed email profiles"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005246108-Understanding-suppressed-email-profiles"
section: "Understand profiles"
category: "Audience"
category_slug: "analytics-audience"
klaviyo_updated: "2026-05-15T10:22:19Z"
language: en
---

## You will learn

Learn about suppressed email profiles, including how they differ from [active profiles](https://help.klaviyo.com/hc/en-us/articles/115005246968) and how you can use these profiles to better understand your audience.

## What is a suppressed profile?

When a profile is suppressed for email, they cannot receive marketing messages. A suppressed profile cannot receive marketing messages, even if they have provided consent and indicated they want to receive emails.

A person can become suppressed for the following reasons:

- ****An email hard bounced****
  A hard bounce occurs when an email cannot be delivered due to a permanent reason. This can be caused by a variety of reasons, including a misspelled email address or a deliberate block by the email server. A hard bounce signals a permanent email delivery issue, so Klaviyo will automatically suppress these profiles to help ensure your lists stay clean.
- ****An email soft bounced more than 7 consecutive times****
  A soft bounce occurs when an email cannot be delivered due to a temporary reason. For example, a recipient's inbox may be full or the server may be down. If an email soft bounces more than 7 times in a row, it indicates that this is a consistent issue. To prevent continual soft bounces, Klaviyo will suppress email addresses that soft bounce more than 7 times consecutively. Only soft bounces within the past 2 years are considered for this count.
- ****Spam complaint****
  The recipient previously marked an email message from this account as spam.
- ****Manually suppressed****
  If you have uploaded a file of people to manually suppress them for email, they will appear on your suppression list with the reason **User suppressed.**
- ****The person was suppressed in a previous email service provider****
  This type of suppression occurred prior to your use of Klaviyo and was synced from a third-party service provider, such as Mailchimp. In this case, the suppression reason will be listed as **User suppressed**.

When someone unsubscribes or marks an email as spam they will be unreachable, but these are not displayed as suppression reasons. Instead these profiles will always have an unsubscribed consent status. Profiles that are unsubscribed are unreachable through the channel and do not contribute towards billing plans.

![Unsubscribed status](https://klaviyo.zendesk.com/hc/article_attachments/28711697192731)

## Global vs. list suppressions

Based on your settings in Klaviyo, a profile can be globally suppressed from all lists on your accounts, or just be suppressed for specific lists.

### Global suppressions

If you have [Klaviyo's global unsubscribe feature](https://help.klaviyo.com/hc/en-us/articles/115005078267-A-Guide-to-Unsubscribes-in-Klaviyo) enabled, which is highly recommended, profiles will become globally suppressed for email in your account after unsubscribing from any email. This means that when someone unsubscribes from email, they will be suppressed from any further email sends.

You can access a global unsubscribe link by navigating to ****Settings > Other**** and scrolling down to the **Consent Settings** section.

![Global unsubscribe page link in Klaviyo](https://klaviyo.zendesk.com/hc/article_attachments/28711697135515)

This is a recommended feature that is enabled on accounts by default, because when a customer unsubscribes from one of your emails, they expect to unsubscribe from all of your emails. If a customer continues to receive emails from you after unsubscribing, they will either ignore them, mark them as spam, or take more aggressive action. As a sender, all of these consequences can significantly harm your email deliverability.

Note that the total number of suppressed profiles on your **Profiles** tab represents all profiles that have been globally suppressed in your account. If you turn off the global suppressions and a customer unsubscribes from a particular list, they will not count as a suppressed profile on the **Profiles** tab. If someone unsubscribes from a non-list based send, they will be suppressed from all future emails.

### List-specific suppressions

By default when a recipient unsubscribes from an email you send, they will be suppressed for all future emails.

If you have a paid Klaviyo plan, you can adjust this behavior on the account-level or for specific lists. When the global unsubscribe setting is disabled, those who unsubscribe from a list-based email send will only be suppressed from the list (or lists) that message was sent to, and may still receive emails sent to other lists they have subscribed to. This setting does not impact SMS or push consent.

List-suppressed profiles will not be included in the suppression condition in segmentation (i.e., **If someone can or cannot receive marketing > cannot receive > email marketing > because person is suppressed**) as profiles can still receive some emails.

To maintain strong deliverability and avoid recipients marking your emails as spam, Klaviyo highly recommends that you leave global unsubscribes enabled.

To disable global unsubscribes for a single list:

1. Select your list from the ****Lists & Segments**** tab.
2. Open that list’s settings.
3. Uncheck the option **When someone unsubscribes from [LIST NAME], unsubscribe that person from all future emails.**
4. Click ****Update List Settings****.
   ![Global unsubscribe setting for a list in Klaviyo](https://klaviyo.zendesk.com/hc/article_attachments/28711697129499)

   To disable this setting for all lists:
5. Navigate to ****Settings > Other****.
6. Scroll down to Unsubscribe Behavior.
7. Uncheck the option When someone unsubscribes from a list, unsubscribe that person from all lists.
8. Click ****Update Email Tracking Settings****.

![Update email tracking settings options](https://klaviyo.zendesk.com/hc/article_attachments/28711697152411)

## Viewing a profile’s suppression status

To see if a profile is suppressed for email, navigate to their profile.

On the **Details** tab, you'll see the different channels a profile can be reached through along with their suppression and consent status. You'll see the following statuses here:

- ****A green checkmark****
  This symbol indicates that the profile is able to receive marketing because they have subscribed for the corresponding channel and are not suppressed.


  ![Subscribed for email status](https://klaviyo.zendesk.com/hc/article_attachments/28711675684635)
  ![Subscribed for SMS status](https://klaviyo.zendesk.com/hc/article_attachments/28711697161883)
  ![Subscribed for push notifications status](https://klaviyo.zendesk.com/hc/article_attachments/28711675691803)
- ****A red indicator****
  This symbol indicates that the profile is unable to receive marketing through the channel and is suppressed. This may be because they were manually suppressed, or they had an email hard bounce.
  ![Suppressed for email status](https://klaviyo.zendesk.com/hc/article_attachments/28711675701403)
- ****A yellow exclamation mark****
  A yellow exclamation mark indicates that the profile is able to receive email marketing, but has neither subscribed nor opted out. While they are able receive emails (e.g., an abandoned cart flow email) because they are not suppressed, you should exercise caution when contacting them.

![Never subscribed status for email](https://klaviyo.zendesk.com/hc/article_attachments/28711697179547)

![Never subscribed status for SMS](https://klaviyo.zendesk.com/hc/article_attachments/28711697182107)

For SMS and push notifications, profiles need to provide express consent in order to receive messages. Profiles with a status of **Never subscribed** for SMS and push notifications are not able to receive messages through the channel until they opt-in.

By expanding a channel, you can see information about when and how someone became subscribed and the reason the profile is suppressed. If the profile is suppressed for more than one reason (e.g., manually suppressed and also unsubscribed), only the highest-priority suppression reason will appear. Suppressions are prioritized as follows:

1. Deliverability (i.e., hard bounce or invalid email)
2. Manual (i.e., the profile was manually suppressed)

## Navigating to your email suppression list

### Global suppressions

To see the total number of profiles that are active versus suppressed for email, visit your **Profiles** tab and look at the values in the top left corner of the page.

Click ****Suppressed Profiles**** to view a list of all email suppressions.

![Count of active and suppressed profiles](https://klaviyo.zendesk.com/hc/article_attachments/28711697148315)

Once you navigate to your email suppression list, you can:

- Filter by reason
- Export this list to a CSV
- Add an email address manually
- Upload a file of people you'd like to suppress

![Suppressed profile page options](https://klaviyo.zendesk.com/hc/article_attachments/28711675733787)

### List suppressions

To see the profiles that are suppressed for a specific list, first navigate to your desired list. Under the ****Manage List**** menu in the top-right corner, you’ll see the **List Suppressions** option that will take you to the list’s suppressed users.

![List suppressions option on a list](https://klaviyo.zendesk.com/hc/article_attachments/28711697143067)

When a profile is manually suppressed for a list, the **Manually Suppressed from "List name" Email Marketing** event appear on the profile's activity log.

Note that with global suppressions enabled, profiles that become suppressed will not appear here.

## How to suppress profiles

To suppress a single profile for email, navigate to ****Profiles > Suppressed Profiles**** and click ****Add Email Address****.

Additionally, you can suppress a profile directly from the **Details** tab on a profile. By clicking on the menu next to the consent indicator, you can **Suppress** or **Unsubscribe** the profile.

Only the **Owner**, **Admin**, and **Manager** user roles can suppress profiles.

![Option to suppress a profile on Details tab](https://klaviyo.zendesk.com/hc/article_attachments/28711675710875)

Suppressing a profile through these options will apply a **User Suppressed** suppression reason. Since manually suppressing a profile does not change their consent status, the profile’s consent status will remain **Subscribed** but they are now unable to receive email marketing.

When a profile is manually suppressed, the **Manually Suppressed from Email Marketing** event appear on the profile's activity log.

To learn how to suppress multiple profiles at once, head to our article on [how to bulk delete or suppress contacts in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/24312135764251).

## Updating subscriptions and suppressions

To manually unsuppress a profile, navigate to their profile and select the ****Remove global suppression**** button under the suppressed channel. Alternatively, you can use the **Unsuppress** option in the menu next to the channel's consent indicator.

![Unsuppress option for suppressed profile](https://klaviyo.zendesk.com/hc/article_attachments/28711675719835)

When a profile is manually unsuppressed, the **Manually Unsuppressed from Email Marketing** event appears on the profile's activity log.

Profiles that unsubscribed or marked an email as spam will not display an **Unsubscribe** option. Instead, you are able to use the **Resubscribe** option. If you received explicit consent from a recipient, you can resubscribe them.

![Resubscribe option for unsubscribed profile](https://klaviyo.zendesk.com/hc/article_attachments/28711675727515)

When a profile resubscribes (e.g., via a list uploaded with consent or by filling out a signup form), all non-deliverability suppressions will be lifted. Deliverability suppressions (e.g., those due to hard bounces) are not removed by subscribe actions in order to protect your sender reputation.

## How Klaviyo treats suppressed email profiles

### Suppressed profiles and pricing

Klaviyo's pricing tiers are based on the total number of active profiles in your account. An active profile is any profile that isn't suppressed for email.

Klaviyo does not charge for suppressed profiles. If you navigate to ****Account > Overview****, you will only see active profiles counting towards your email plan limit.

Meanwhile, on the Profiles tab of your account, you can see the counts for total **Active Profiles** and **Suppressed Profiles** separately, as shown above.

### Exclusion from email sends

Klaviyo will automatically exclude all suppressed profiles from email sends. This means that, even if you try to send an email to suppressed profiles, Klaviyo will automatically ensure that these intended recipients are skipped.

For flow emails, under ****Recipient Activity > Other**** you will find a **Skipped: Person Suppressed** count that signals how many people didn't receive the email because they are suppressed in your account.

### Suspicious emails

Suspicious emails are email addresses that have hard bounced at least 3 times across the Klaviyo infrastructure. This means that even if they have never hard bounced in your account, they have previously hard bounced in another Klaviyo user's account.

Suspicious emails will automatically be skipped from receiving emails. This is in an effort to [preserve your sending reputation](https://help.klaviyo.com/hc/en-us/articles/115005247008-Overview-of-Email-Deliverability), as well as the sending reputation of other Klaviyo customers. You can see a count of the number of suspicious email addresses skipped, along with emails skipped for other reasons, in the Campaign Overview. You can also see this count in the Recipient Activity section for a given campaign.

## Consent vs. suppression status

In Klaviyo, there are 2 key concepts to understand which contacts are reachable and which have provided consent to receive marketing. These are consent status and suppression status.

Suppression and consent statuses are separate from each other. For example, a profile that has provided consent and is subscribed can be suppressed and retain its consent status.

### Consent status

[Consent status](https://help.klaviyo.com/hc/en-us/articles/360037101072) refers to whether a profile has opted-in to receive email marketing. At the top of the **Details** tab of a profile page, you'll see a profile’s consent status and ability to receive messages by channel. The different statuses you may see for consent are:

- ****Subscribed****
  **Subscribed** means that a profile has explicitly provided consent to receive marketing, and is able to receive communications through the corresponding channel.
- ****Never subscribed****
  **Never subscribed** means the profile has neither subscribed, nor opted out of email marketing. For example, someone who placed an order or abandoned a checkout on your site may have added their email address during the checkout process, but never explicitly opted in. They are able to receive emails (e.g., an abandoned cart flow email), but you should exercise caution when contacting them.
- ****Unsubscribed****
  **Unsubscribed** means that a profile is no longer interested in receiving your email marketing and has explicitly revoked consent for receiving it. Once unsubscribed, the profile will no longer be able to receive messages through the channel.

### Suppression status

Suppression status refers to whether a profile is reachable through a channel. When a profile is suppressed for email, they cannot receive marketing messages. A suppressed profile cannot receive marketing messages, even if they have provided consent and indicated they want to receive emails, and do not contribute towards your Klaviyo billing plan.

Profiles can either be in a suppressed state, or an unsuppressed state.

## Keeping vs. deleting suppressed profiles

There are several reasons why Klaviyo recommends keeping suppressed profiles in your account instead of deleting them:

- ****Klaviyo will never charge you for suppressed profiles****
  Klaviyo's pricing tiers are based on the total number of active profiles; you will never be prompted to upgrade to pay for suppressed contacts, so there is no cost associated with keeping them in your account. If you list clean and qualify for a lower pricing tier, make sure to select that lower tier under ****Account > Billing > Email Billing****.

  [Klaviyo CDP billing](https://help.klaviyo.com/hc/en-us/articles/115000976672) is separate from Email and SMS plans on Klaviyo. Klaviyo CDP billing is based on total profiles, including suppressed profiles.
- ****Suppressed users still matter for business insights****
  Klaviyo's segmentation tools can help you gain important business insights. If you plan on creating segments to analyze customer behavior, website activity, etc., deleting profiles (even those you can't ultimately email) will skew these segments and make it impossible to get accurate insights.