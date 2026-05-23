---
id: 360004059711
title: "Understanding the default account, email, and list settings"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360004059711-Understanding-the-default-account-email-and-list-settings"
section: "Message settings"
category: "Account & billing"
category_slug: "account-billing"
klaviyo_updated: "2026-04-21T13:54:42Z"
language: en
---

## You will learn

Learn about the settings that are pre-set in your Klaviyo account for timezones, UTM tracking, emails, and lists. Depending on your business's particular model and needs, you may wish to change these defaults. In this article, you will learn what these default account settings are.

For information on SMS default settings, please read [Understand your SMS settings](https://klaviyo.zendesk.com/hc/en-us/articles/360035285472).

## General account defaults

- ****Timezone:****By default, your account will display all timing data in EST. To change this, navigate to ****Settings > Organization**** and select your preferred timezone.
- ****UTM tracking:**** If you would like to [configure the UTM parameters](https://help.klaviyo.com/hc/en-us/articles/115005247808) that are appended to links in Klaviyo, you can do so by navigating to ****Settings > Other > UTM tracking.****Here, you can add custom UTM parameters, edit the defaults that Klaviyo tracks, and toggle UTM tracking ON for all messages.

## Email account defaults

### Sender information

Here, you can update the Klaviyo default branding for your emails. This applies to all Klaviyo emails.

![Sender information options to choose from Klaviyo default or your own branding in emails](https://klaviyo.zendesk.com/hc/article_attachments/28717380607515)

### Sending preferences

#### Smart Sending Period (email)

Smart Sending prevents you from inadvertently over-emailing people. It causes people to be skipped from receiving an email if they received another one within the Smart Sending window. By default, this window is set to 16 hours. This means that anyone who received an email within 16 hours of your most recent send will be skipped.

If you use Klaviyo to send [transactional emails](https://help.klaviyo.com/hc/en-us/articles/360003165732-Using-Flows-to-Send-Transactional-Emails), you can also specify whether or not you want Smart Sending to apply to transactional emails.

#### Preview Emails

Choose to set a default prefix for the subject lines of all of your preview emails. This makes it easier to distinguish preview emails from actual campaign or flow sends. By default, there is no prefix appended to preview emails.

#### CSS Optimization

Leaving this checked ensures that your emails [use embedded styles instead of inline CSS](https://klaviyo.zendesk.com/hc/en-us/articles/360049848692). While inline CSS can allow your emails to render better in lesser-known inbox providers or places with regional requirements, it adds length to your emails, making them more likely to be clipped. Only uncheck this box if you know that a large part of your customer base is either using a lesser-known inbox provider or is in a region that requires it.

### Tracking

#### Bot clicks

Check this box to exclude bot clicks from your account's reporting data. Note that you have the choice to filter out bot clicks from email, SMS, or both channels. Enabling this setting will exclude bot clicks in calculations of click rate, total clicks, and unique clicks across most reporting surfaces. Learn more about [excluding and monitoring bot clicks in your account](https://help.klaviyo.com/hc/en-us/articles/22981852783899).

![The Tracking menu within an account's default email settings showing the Exclude bot clicks setting unchecked.](https://klaviyo.zendesk.com/hc/article_attachments/28717380612891)

Any A/B tests created after this setting is enabled will use a click rate that excludes bot clicks, which may impact the winning variant. For this reason, we recommend not enabling this setting during an ongoing A/B test that uses clicks as a metric.

#### Email-to-website tracking

Leaving this checked allows you to attribute web activity to specific emails.

![Box checked for email to website tracking enabled](https://klaviyo.zendesk.com/hc/article_attachments/28717386863771)

#### Email tracker position

Check this box to place an email tracking pixel at the top of your emails.

Tracking pixels record when someone opens or clicks into an email. By default, the pixel adds to the bottom of the email to minimize impact on design. If you have long emails that get truncated, you can ensure accurate tracking by placing the tracking pixel at the top of your emails.

![Radio button options for either having the tracking pixel at the top or the bottom of your email](https://klaviyo.zendesk.com/hc/article_attachments/28717380604059)

### Domains

#### Sending Domain

Here, you can set up or manage your dedicated or branded sending domain. Sending from a branded sending domain can improve your deliverability performance, helping you reach your audience's inboxes more often.

![Option to set up a branded sending domain by clicking on Enable](https://klaviyo.zendesk.com/hc/article_attachments/28717380610971)

#### Default sender name and email address label

When you first sign up, the name and email you use to create your account are set to your default sender name and your default sender email address. When you create a new campaign or flow, these values auto-populate.

![View of when you first sign up for Klaviyo with your default sender email name and address fields.](https://klaviyo.zendesk.com/hc/article_attachments/28717386856347)

Going forward, you can update your default sender name and sender email address from ****Settings > Organization****.

Updating your default sender name label or sender email address only affects emails going forward. If you want to update existing flows or campaigns, you have to make these updates manually.

## Flows defaults

All default flow settings can be edited by clicking on the email component, then clicking the gear icon in the **Settings**section.

- ****Smart Sending:****With the exception of the pre-built abandoned cart emails, Smart Sending is on by default for all flow emails. [Learn more about Smart Sending](https://klaviyo.zendesk.com/hc/en-us/articles/115002779311).
- ****UTM Tracking:****UTM tracking for Google Analytics is OFF by default for all flows, but this can be adjusted in your account-level settings, as outlined above.
- ****Additional Filters:****By default, no flow emails will have additional filters.

## Campaign defaults

Campaign settings are configured as you move through the scheduling wizard.

- ****Smart Sending:****For campaign emails, Smart Sending is always on by default. It is recommended that you leave Smart Sending on for campaigns to avoid over-emailing subscribers. [Learn more about Smart Sending](https://klaviyo.zendesk.com/hc/en-us/articles/115002779311).
- ****UTM Tracking:****UTM tracking for Google Analytics is OFF by default for campaigns, but this can be adjusted in your account-level settings, as outlined above.
- ****Subject Line:****If you don't designate a subject line for your campaign, it will default to the name of the campaign.
- ****Date & Time:****When scheduling a campaign, the default date/time value will be the soonest half-hour in your time zone.
- ****Determining Recipients:****As outlined above, this can be configured on an account-wide basis. When scheduling a campaign, if you haven't updated your preferences in ****Settings > Messaging****,this will default to**Determine recipients now**.
- ****Sending Strategies:****When scheduling a campaign, Klaviyo will default to sending to everyone at the time you specify, regardless of where they live.

## List defaults

When you create a new list, there will be a number of default settings that can be configured in the **Settings** tab.

- ****Unsubscribes:****Choose whether or not you want people to be globally unsubscribed when they unsubscribe from a particular list. This is not checked by default, but can also be edited in your account-level settings, as outlined above.
- ****Double Opt-In****: By default, all lists are double opt-in. However, you can set your list to be single opt-in instead. [Learn more about double opt-in](https://klaviyo.zendesk.com/hc/en-us/articles/115005251108).
- ****Language:****By default, all content in the subscribe pages and signup forms affiliated with a particular list will be in English. Learn how to [change the language of your consent pages](https://help.klaviyo.com/hc/en-us/articles/360049498631).

## Additional resources

- [Understand your SMS settings](https://klaviyo.zendesk.com/hc/en-us/articles/360035285472)
- [Understand multi-account user privileges](https://klaviyo.zendesk.com/hc/en-us/articles/360002165611)
- [Getting started with Klaviyo](https://academy.klaviyo.com/getting-started-with-klaviyo/1405979)