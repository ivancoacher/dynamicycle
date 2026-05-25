---
id: "24263920096027"
title: "Understanding active profile management in Klaviyo"
source_url: "https://help.klaviyo.com/hc/en-us/articles/24263920096027-Understanding-active-profile-management-in-Klaviyo"
section: "Profile management"
category: "Audience"
category_slug: "analytics-audience"
klaviyo_updated: "2026-05-11T13:49:22Z"
language: "en"
---
## You will learn

Learn how to manage active profiles in your Klaviyo account and reduce the number of billable profiles by suppressing those that have not engaged with your business for a sustained period of time.

In this guide, you will find our general recommendations for suppressing profiles without causing a negative revenue impact for your business.

## Active profiles in Klaviyo

Any profile that can be emailed through Klaviyo is considered an active email profile. There are 2 main categories of active profiles:

- ****Subscribers****
  Subscribers have filled out a sign-up form or otherwise explicitly consented to receive email marketing.

- ****Profiles added by general engagement****It is possible for someone to share their email with you without explicitly consenting to ongoing email marketing. For example, someone who placed an order or abandoned a checkout on your site may have added their email address during the checkout process, but never explicitly opted in.

Ecommerce integrations (e.g., Shopify and WooCommerce) can add both types of active profiles to Klaviyo, depending on the actions a visitor takes while on your site.

## Suppressed profiles in Klaviyo

When a profile becomes [suppressed](https://help.klaviyo.com/hc/en-us/articles/115005246108), they will no longer be eligible to receive any marketing emails. Klaviyo will automatically skip over suppressed profiles at send time. Additionally, suppressed profiles do not contribute towards your billing plan’s profile count.

Once a profile is suppressed, even if that contact starts a checkout on your website or makes a purchase, they will remain suppressed and ineligible to receive any marketing emails.

Profiles can be unsuppressed if they resubscribe to email marketing, at which point their suppression will be lifted and email marketing consent will be set again, or if their suppression is manually removed.

It is important to note that suppressing profiles too early, when they may still come back and engage with your brand in the future, can lead to potential revenue loss for your brand as you will be unable to nurture them towards a conversion.

## Billing plans in Klaviyo

[Klaviyo email billing](https://help.klaviyo.com/hc/en-us/articles/115000976672) is structured around the number of active profiles (or contacts) in your Klaviyo account. Every Klaviyo user must have a base plan, which is contingent on the number of active profiles you have in your account and the number of emails you send.

Your plan must allow enough profiles to accommodate the number of active profiles in your account, or you may be automatically upgraded the next billing cycle.

For email sends, the limit is 10 times the maximum number of profiles in your plan.

For instance, if you have a plan that allows 500 profiles, you can send up to 5,000 emails to any of these profiles. It can be an equal amount (10 to each profile) or a unique distribution in which more emails are sent to certain profiles, and only 1 to others.

## What is active profile management?

Active profile management is the process of suppressing inactive subscribers, or churned customers. These are profiles that have demonstrated a long, sustained period of inactivity (i.e., no website visits, purchases, or marketing engagement). Due to this sustained period of inactivity, it is highly unlikely that these profiles will engage with your brand.

If a profile is not generating any revenue for your business in Klaviyo, and you do not see any opportunity to win them back, you can take action to suppress them so they do not count towards your Klaviyo billing plan.

## Understanding inactivity

Even with a strong marketing strategy that nurtures your customers over the course of their lifecycle with your brand, some contacts may not engage with you for a long, sustained period of time. This means that these profiles are both no longer engaging with your regular email sends, and no longer taking any measurable actions to engage with your business well beyond their expected buying cycles.

These profiles are not responding to events like product launches, winback messages, or even big sales like Black Friday. They have never purchased, have no tracked visits to your website, no checkouts started, and have not engaged with your sends. These are truly “inactive” contacts that can be suppressed in Klaviyo.

Since these profiles are considered churned, you can safely suppress them and stop communication without incurring any likely revenue loss.

You can make use of a [sunset flow](https://help.klaviyo.com/hc/en-us/articles/360017518492) as a last-ditch effort to win back a profile’s business and suppress anyone who is not responsive.

## Inactivity segment

You can create a segment of inactive profiles to suppress from your account using the following conditions:

- If someone can or cannot receive marketing > Person ****can receive**** ****email marketing****
  AND
- Properties about someone > ****Email is set****AND
- Properties about someone > ****Created**** is at least ****180**** days ago
  AND
- What someone has done (or not done) > has ****Received Email at least 5**** in the last ****72**** weeks
  AND
- What someone has done (or not done) > has ****Opened Email 0 times**** ****over all time****
  AND
- What someone has done (or not done) > has ****Clicked Email 0 times over all time****
  AND
- What someone has done (or not done) > has ****Active on Site 0 times**** ****over all time****
  AND
- What someone has done (or not done) > has ****Viewed Product 0 times over all time****
  AND
- What someone has done (or not done) > has ****Checkout Started 0 times over all time****
  AND
- What someone has done (or not done) > has ****Placed Order 0 times over all time****

![Inactivity segment](https://klaviyo.zendesk.com/hc/article_attachments/33680967155483)

This segment identifies profiles that should be suppressed; they have experienced a sustained period of inactivity and are unlikely to return as customers, but are still billable in Klaviyo.

## Tools to suppress inactive profiles

In Klaviyo, you can suppress profiles on an [individual basis](https://help.klaviyo.com/hc/en-us/articles/115005246108#h_01HBDYFEQ1YWDRDZ3TMQF1611R) and [in bulk.](https://help.klaviyo.com/hc/en-us/articles/24312135764251)

Only the **Owner**, **Admin**, and **Manager** [user roles](https://help.klaviyo.com/hc/en-us/articles/115005231648) can suppress profiles.

### Suppress a single email profile

To suppress a single profile for email, there are 2 options:

- Navigate to ****Profiles**** > ****View s********uppressed profiles**** and click ****Add Email Address****.
  ![](https://klaviyo.zendesk.com/hc/article_attachments/32057440302491)
- Go to that profile and click ****Profile actions****> ****Suppress profile****.
  ![](https://klaviyo.zendesk.com/hc/article_attachments/32057431332635)

### Bulk suppress profiles

You can bulk suppress the profiles in a list or segment. To bulk suppress a group of profiles, navigate to the **Lists & segments** page under the **Audience** tab in Klaviyo.

Next to the list or segment you’d like to suppress, open the action menu. To suppress all the members of the group, select ****Suppress current members******.**

![Bulk suppress option for Klaviyo list](https://klaviyo.zendesk.com/hc/article_attachments/28705699447195)

This action applies to all the profiles within the list or segment at the time of suppression, and does not impact profiles that join after. If a profile in the group is already suppressed, their status will not be impacted.

Learn more about [suppressing profiles in bulk](https://help.klaviyo.com/hc/en-us/articles/24312135764251).

Suppressing a profile through these options will apply a **User Suppressed** suppression reason. Since manually suppressing a profile does not change their consent status, the profile’s consent status will remain **Subscribed,** but they are now unable to receive email marketing.

When a profile is manually suppressed, the **Manually Suppressed from email marketing** event appears on the profile's activity log.

Klaviyo will also automatically suppress profiles in the following cases:

****An email hard bounced****

A hard bounce occurs when an email cannot be delivered due to a permanent reason. This can be caused by a variety of reasons, including a misspelled email address or a deliberate block by the email server. A hard bounce signals a permanent email delivery issue, so Klaviyo will automatically suppress these profiles to help ensure your lists stay clean.

****An email soft bounced more than 7 consecutive times****

A soft bounce occurs when an email cannot be delivered due to a temporary reason. For example, a recipient's inbox may be full or the server may be down. If an email soft bounces more than 7 times in a row, it indicates that this is a consistent issue. To prevent continual soft bounces, Klaviyo will suppress email addresses that soft bounce more than 7 times consecutively.

****The person was suppressed in a previous email service provider****

This type of suppression occurred prior to your use of Klaviyo and was synced from a third-party service provider, such as Mailchimp. In this case, the suppression reason will be listed as **User Suppressed**.

There are 2 ways profiles can become reachable (i.e., unsuppressed) again, even after being manually suppressed:

1. They resubscribe to email marketing, at which point their suppression will be lifted and email marketing consent will be set again.
2. You manually [remove a suppression](https://help.klaviyo.com/hc/en-us/articles/115005246108#h_01HBDYFEQ1P8AFRSN9SN0S7YM7) for an profile via their profile page or a bulk unsuppression in Klaviyo. Note that removing a manual suppression will not change the profile’s email [marketing consent status](https://help.klaviyo.com/hc/en-us/articles/360037101072).

Learn how to [remove suppressions in bulk](https://help.klaviyo.com/hc/en-us/articles/24312135764251).

## Active profile management vs. list cleaning

Maintaining strong email deliverability requires a proactive effort to exclude unengaged recipients from your regular high volume marketing. This is a different concept than managing your active profiles and rendering profiles unreachable due to long, sustained periods of inactivity with your business.

|  |  |  |
| --- | --- | --- |
| ****Goal**** | ****Description**** | ****Tactic**** |
| Keep your regular marketing list “clean” to avoid deliverability issues | Most major email service providers (e.g., Google and Yahoo) track how recipients interact with emails from your domain and use this information to determine whether your emails are classified as spam. Having lots of unengaged recipients on your list hurts your efforts to reach those who actually want to receive your emails. By regularly sending to only your engaged audience, you can improve inboxing and build a strong sender reputation. | Focus on shorter timeframes: Recipients that have received at least 5 emails but have not opened or clicked in 90 days. Exclude from regular campaigns: Do not suppress these profiles, but rather create an “Unengaged Subscriber” segment you can easily exclude from your daily or weekly bulk campaign sends to avoid deliverability issues.  To learn more, view our guide on [list cleaning](https://help.klaviyo.com/hc/en-us/articles/115005078347). |
| Manage your active profiles in Klaviyo and suppress inactive contacts without risking revenue | An inactive subscriber or churned customer, is someone that has demonstrated a long, sustained period of inactivity (i.e., no website visits, purchases, or marketing engagement). If these profiles are not generating any revenue in Klaviyo, and you do not perceive any opportunity to win them back, you can suppress these profiles so they do not count towards your Klaviyo billing plan. | 1. ****Focus on longer timeframes:**** Look for profiles that have never engaged but have been in your account for a longer period of time. 2. ****Suppress in Klaviyo:**** We recommend running these profiles through one last sunset flow to attempt to spark engagement before proceeding to suppress them. To learn more, view our guide on [creating a sunset flow](https://help.klaviyo.com/hc/en-us/articles/360017518492). |

## Outcome

After completing these steps, contacts who have churned as customers will be suppressed and no longer be considered billable profiles. You should continue to manage your active profiles on an ongoing basis to avoid paying for contacts that are no longer providing revenue for your business.

## Additional resources

- [How to create a sunset flow](https://help.klaviyo.com/hc/en-us/articles/360017518492)
- [Understanding email deliverability](https://help.klaviyo.com/hc/en-us/articles/115005247008)
- [How to create an engaged segment](https://help.klaviyo.com/hc/en-us/articles/115000200072)