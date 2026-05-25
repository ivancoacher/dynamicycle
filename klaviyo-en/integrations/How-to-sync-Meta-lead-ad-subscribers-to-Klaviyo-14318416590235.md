---
id: "14318416590235"
title: "How to sync Meta lead ad subscribers to Klaviyo"
source_url: "https://help.klaviyo.com/hc/en-us/articles/14318416590235-How-to-sync-Meta-lead-ad-subscribers-to-Klaviyo"
section: "Meta Ads"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-17T07:01:52Z"
language: "en"
---
## You will learn

Learn how to sync subscribers (both email and SMS) collected through a Meta lead ad to Klaviyo, via Klaviyo’s Meta Ads integration. First, you’ll create a lead ad to collect subscriptions and include disclaimer text. Then, you’ll use Klaviyo’s Meta Ads integration to sync lead ad subscribers to a Klaviyo list. We’ll also cover how to edit a pre-existing lead ad sync.

The information provided here is intended to be educational and should not be construed as legal advice. Klaviyo encourages all of our customers — and all ecommerce merchants — to work with their legal counsel to ensure they are complying with all applicable laws in connection with their marketing activities.

## Before you begin

It is important to understand and adhere to best practices around collecting consent in your region. Before continuing, review the following articles as applicable:

- To learn about consent in Klaviyo profiles, including best practices for email and SMS compliance, read [Understanding consent in profiles](https://help.klaviyo.com/hc/en-us/articles/360037101072-Understanding-consent-in-profiles).
- To learn about SMS consent and how to properly collect it, read [Guide to collecting SMS consent](https://help.klaviyo.com/hc/en-us/articles/360035056972-Guide-to-collecting-SMS-consent).
- To learn about collecting GDPR compliant consent, read [How to collect GDPR compliant consent](https://help.klaviyo.com/hc/en-us/articles/360003536031-How-to-collect-GDPR-compliant-consent).

## About the lead ad sync

There is no historical sync for lead ads. Data from lead ads syncs to Klaviyo on an ongoing basis, in real time.

When you sync a lead ad with a Klaviyo list, the following will happen:

- Those who sign up to your lead ad will be added to the Klaviyo list you selected.
- If you choose to subscribe profiles to email or SMS (or both) this consent will be added to the individual’s profile in Klaviyo.
- If you choose to subscribe profiles to email or SMS, and you have double opt-in enabled for the selected list, the individual will receive double opt-in messaging. Note that double opt-in messaging may take up to an hour to send, and that the profile will not be added to your list until they complete the double opt-in process.
- If you choose to subscribe profiles to email or SMS, and you have a list-triggered welcome flow enabled for the selected list, or a subscription-triggered welcome flow, the individual will enter the welcome flow.
- If you choose to not subscribe profiles, the individual will be added to the list you select, but they will not be subscribed to marketing, nor will they receive a double opt-in message. If you have a welcome series triggered by consent for SMS or email, they will not receive it, but if your welcome series is a list-triggered flow, they will receive it.

## Create a lead ad form to collect subscribers

When creating your lead ad form in Meta, make sure to do the following:

- Collect email and/or SMS subscriptions. This can be done via a checkbox after you collect names, email addresses, phone numbers, etc. in your form.
- For each field below, the field names used in your lead ad should match one of the following, in order for them to map properly in Klaviyo:
  - ****Email****
    email, e-mail, correo electrónico, e-post
  - ****First Name****
    first\_name, nombre, fornavn
  - ****Last Name****
    last\_name, apellidos, etternavn
  - ****Full Name****
    full\_name, nombre\_completo, fullt\_navn
- Review the materials around consent and compliance linked in the **Before you begin** section above.
- Add disclaimer/consent collection language to your lead ad form. The requirements vary for email and SMS. See table below for example disclaimer text.

### Suggested disclaimer text

|  |  |  |
| --- | --- | --- |
| ****Channel**** | ****Disclaimer should include**** | ****Example disclaimer**** |
| Email | - Confirmation that the user would like to receive messages , including examples of types of messages (“(such as promotions and cart reminders)”). - Message frequency. - Unsubscribe language. - Link to privacy policy. | **By submitting this form and signing up for emails, you consent to receive marketing emails (such as [promotion codes] and [cart reminders]) from [company name] from time to time. You can unsubscribe at any time by clicking on the “Unsubscribe” link at the bottom of our emails. For more information on how [company name] processes your personal information and what rights you have in this respect, please see our Privacy Notice [link].** |
| SMS | - Confirmation that the user would like to receive messages, including examples of types of messages (“(e.g. promos, cart reminders)”). - Message frequency. - Rates disclaimer. - Unsubscribe language. - Links to privacy policy and SMS/mobile terms of service. | **By submitting this form and signing up for texts, you consent to receive marketing text messages (e.g. promos, cart reminders) from [Company name] at the number provided, including messages sent by autodialer. Consent is not a condition of purchase. Msg & data rates may apply. Msg frequency varies. Unsubscribe at any time by replying STOP or clicking the unsubscribe link (where available). Privacy Policy [insert privacy policy link] & Terms [insert terms of service link]** |

![](https://klaviyo.zendesk.com/hc/article_attachments/28981896117147)

## How to sync subscribers from lead ads to Klaviyo

You can create a new connection when initially integrating Klaviyo with Meta Ads, or you can add one after integrating. You can also edit existing connections after integrating. If you haven’t yet integrated Klaviyo with Meta Ads, follow the instructions in [Getting started with Meta Ads](https://klaviyo.zendesk.com/hc/en-us/articles/115005082127). Creating a new connection after integrating and editing an existing connection will be outlined below.

Klaviyo does not backfill historical lead ad submissions that occurred prior to setting up the lead ad connection in Klaviyo.

## How to create a new connection (after integrating)

1. In Klaviyo, select the ****Integrations**** tab.
2. Select ****Meta Ads**** from the list.
3. Select the ****Lead Ads**** tab.
4. Under **Lead ads** click ****Add connection****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28981896119835)
5. Select a lead ad from the **Meta lead ad** dropdown, then select a Klaviyo list from the corresponding dropdown.
6. Click the **Subscriptions** dropdown and select whether to subscribe customers who fill out the lead ad form to email, SMS, email and SMS, or none (“Do not subscribe”).
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28981896120987)
7. Add as many connections as you would like. Note that a given lead ad can only be chosen in one sync. When you are finished, click ****Save****.

## How to edit an existing connection

Prior to April 6, 2023, lead ad connections synced signups to a Klaviyo list but did not mark profiles as consented to email or SMS, or send them double opt-in messaging.

If you previously created a lead ad connection and want to subscribe new signups going forward, you can edit your pre-existing connection. You can also edit your pre-existing connection to change its Klaviyo list.

To edit a pre-existing connection:

1. In Klaviyo, select the ****Integrations**** tab.
2. Select ****Meta Ads**** from the list.
3. Select the ****Lead ads**** tab.
4. Under **Lead ads**, find the connection you want to edit, then click the triple dots. Then, click ****Edit****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28981883303835)
5. Edit the fields you wish to update. If you want to sync subscribers, choose the channel (email, SMS, or both) you want to subscribe them to from the **Subscription** dropdown.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28981896124187)
6. When you are finished, click ****Save****.

## Outcome

You’ve now learned how to sync subscribers collected via a Meta lead ad form to Klaviyo, and how this sync works.