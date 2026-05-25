---
id: "360047183572"
title: "How to rebrand in Klaviyo"
source_url: "https://help.klaviyo.com/hc/en-us/articles/360047183572-How-to-rebrand-in-Klaviyo"
section: "Organizational"
category: "Account & billing"
category_slug: "account-billing"
klaviyo_updated: "2026-04-21T13:54:49Z"
language: "en"
---
## You will learn

Learn how to change your domain name during a rebrand and best practices for maintaining good deliverability throughout the change.

## Before you begin

Form a rebranding strategy.

When rebranding, you will likely pursue 1 of 3 options:

1. ****Rename your existing Klaviyo domain****
   Follow the steps below to adequately prepare your audience and edit any key marketing copy.
2. ****Merge Klaviyo accounts****
   If you're merging 2 Klaviyo accounts, such as if your company has purchased or merged with another that uses Klaviyo, follow the steps below to update your account and inform your audience.
3. ****Set up an entirely new Klaviyo account****
   Starting fresh? Skip this guide if you want to set up a new Klaviyo account. Instead, check out our [course on Getting started with Klaviyo](https://academy.klaviyo.com/getting-started-with-klaviyo/1459179).

## Prepare your account for the change

Before starting to rebrand, there are a few action items that you must accomplish to maintain good deliverability and communicate accurate information to your customers. Follow these best practices before making any sweeping changes to your account:

1. Update your ecommerce integration.

   - Ensure your ecommerce store and integration reflect your new brand name, logos, and URLs.
   - [Enable onsite tracking](https://help.klaviyo.com/hc/en-us/articles/115005076767) and any other important tracking features you use with Klaviyo; for example, custom [**Added to Cart** events](https://help.klaviyo.com/hc/en-us/articles/115001396711) for Shopify users
2. Review our guide to warming your sending infrastructure.

   - Warming your sending domain is essential to maintain deliverability, and is a required step after renaming your sending domain. Even if you keep the same Klaviyo account, inbox providers treat each new domain as an entirely separate entity. Review our [guide to warming your domain](https://help.klaviyo.com/hc/en-us/articles/360025945671) before proceeding.
3. Notify your customers
   - Inform customers of your rebranding ahead of time to avoid confusion and prevent issues with deliverability. Create email (and SMS, if applicable) campaigns that alert your subscribers about the name and brand changes prior to the first send with your new domain name.
   - What to include in customer notifications:
     - Email campaign: Create a text-based email to draw subscribers’ attention that includse both current and new branding. Your current brand content will help subscribers identify your business, and the new content will show them what they can expect in the future.
     - SMS campaign: Include the current brand name, new brand name, and, if possible, an image of the new logo. Linking to a page that shows off your new branding can also help inform your subscribers.

****What to tell customers (click to expand)****

Transparency is key when it comes to maintaining a positive relationship with your loyal customers. In the email or SMS landing page, explain the following:

- Your new brand and logo
- Any content or product changes
- The domain name that they will soon receive emails from
- The reason for the name change (e.g., rebranding, merging, etc.)

In your email or landing page, you can [add a button](https://klaviyo.zendesk.com/hc/en-us/articles/115005255248) to ask customers if they still want to receive marketing messages from your new brand. Their answer: **yes** or **no**, will become a [profile property](https://klaviyo.zendesk.com/hc/en-us/articles/115005074627).

Using that property, create 2 segments of customers who you want to continue to receive messages: one for emails and one for SMS. Then, create another 2 segments to suppress anyone who no longer wants to receive marketing messages. For those who do not respond, trigger a [sunset flow](https://klaviyo.zendesk.com/hc/en-us/articles/360017518492) to either re-engage or suppress them depending on how they interact with your flow messaging.

****Swoon email example (click to expand)****

For example, [Swoon](https://www.tasteswoon.com/), formerly Be Mixed, merged Klaviyo accounts to consolidate their product into one brand. They kept the name Swoon and discarded Be Mixed; all the while, they communicated this change to customers via campaign emails to make the change more seamless.

![Swoon email as an example of rebranding](https://klaviyo.zendesk.com/hc/article_attachments/28720658132507)

## Update your Klaviyo account

1. Update your sending domain
   - This step applies if you're changing over to a new domain. If you are merging accounts, and thus keeping the name and domain of an account that already exists, skip this step.
   - Follow the instructions in our guide on [setting up a dedicated sending domain](https://klaviyo.zendesk.com/hc/en-us/articles/115000357752). If you're moving to a newly registered domain, you will need to [warm you infrastructure](https://help.klaviyo.com/hc/en-us/articles/360025945671#standard-guided-warming-process3).
2. Adjust your brand information in Klaviyo
   - Once your domain name is updated or, for those simply merging accounts, you have informed your customer base that a change is imminent, edit your brand details within Klaviyo by selecting your account name, then ****Settings >**** ****Account > Organization****. From here, update:
     - Your default sender email address, which is the entity customers receive your messages from.
     - Other information settings that changed during your rebranding process, such as your **Company/organization name**.
     - Be sure to ****Save**** all changes.
       ![The Contact Information menu on the Organization settings page where you can adjust default sender email and other contact details.](https://klaviyo.zendesk.com/hc/article_attachments/29334081028379)
3. Refresh your brand library
   - Head to ****Content > Images & Brand**** to upload new content (e.g., images, brand assets, fonts, etc.) to align with your rebranding, as well as preview, delete, and update existing content and settings.
4. Edit content in flows and templates
   - In addition to the email address associated with your flow emails, you will want to edit any flow content and email templates to reflect the new branding. This includes any:
     - Copy in your emails or SMS messages
     - Subject line content
     - Linked content
     - Template URLs
   - If you merge accounts, set your flows to draft and then [clone all your flows and templates](https://klaviyo.zendesk.com/hc/en-us/articles/24898429283739) to the account you're keeping.
   - You can also create new templates to start from scratch if you choose to redesign your store content entirely. For more information on editing your templates, head to [create, edit, delete, and manage](https://help.klaviyo.com/hc/en-us/articles/115000102752) templates.

## Transferring profiles and engagement data

If you merge accounts, you will want to transfer existing profile data to the account you intend to keep. You can [export your main list to a CSV file](https://klaviyo.zendesk.com/hc/en-us/articles/115005078687) and then import that information directly into your next account.

The only engagement data that will transfer into your other account is **First Click** and **Last Click**. You can use these timeframes to gauge engagement in your new account and resume messaging.

## Warm your domain

Warming your domain causes inbox providers to see you as a "good" new sender and strengthens your sending reputation so that you avoid hitting the spam folder. Any new Klaviyo customer, or those using a newly registered domain who have engagement data or are using a prebuilt integration, will need to follow the [standard guided warming process](https://help.klaviyo.com/hc/en-us/articles/360025945671#standard-guided-warming-process3). Otherwise, if you are coming to Klaviyo without engagement data or not using one of the prebuilt integrations, you can follow the [platform introduction process](https://help.klaviyo.com/hc/en-us/articles/360025945671#platform-introduction-process4).

Note that existing Klaviyo customers simply moving to a dedicated sending domain, do not have to warm your infrastructure again, as long as you have a 30-day sending history.

## Additional resources

- [How to change your account's organization name](https://help.klaviyo.com/hc/en-us/articles/15166435131163)
- [How to ramp and warm your sending infrastructure](https://klaviyo.zendesk.com/hc/en-us/articles/360025945671)
- [Guide to building a brand voice](https://academy.klaviyo.com/guide-to-building-a-brand-voice)
- [Understanding dedicated vs. shared sending domains](https://help.klaviyo.com/hc/en-us/articles/7674941873947)