---
id: 4408023789083
title: "Getting started with Gorgias"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/4408023789083-Getting-started-with-Gorgias"
section: "Gorgias"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:59Z"
language: en
---

You must be an Owner or Admin to set up this integration.

Learn how to integrate with Gorgias Helpdesk to sync support ticket information between Gorgias and Klaviyo. With this integration, you can:

- Sync information about open tickets from Gorgias to Klaviyo.
- Respond to incoming SMS and WhatsApp messages with Gorgias.
- Create support tickets for negative reviews if you are using [Klaviyo Reviews](https://help.klaviyo.com/hc/en-us/articles/15937542819355).

If you manage multiple brands in Gorgias, tickets, SMS messages, WhatsApp messages and reviews can be synced on a per-brand basis, given that you’ve set up proper tagging in Gorgias. We recommend syncing one Gorgias brand per Klaviyo account to make it easy to use your ticket data and organize your SMS conversations. We detail how to implement Gorgias tagging with a multi-brand setup below.

## Before you begin

Please note that this integration does not automatically create Gorgias tickets when a customer responds to emails sent from Klaviyo. That being said, Gorgias will create tickets for any incoming emails to your support email address. Thus, if your sender email address in Klaviyo is the same as your support email address in Gorgias, tickets will be created for responses to any marketing emails you send.

### SMS prerequisites

Using the SMS-related features of the Gorgias integration is only supported for accounts that have SMS set up:

- The SMS integration only works in countries where you have a toll-free number, long code, or short code.
  - Branded sender IDs (also called alphanumeric sender IDs) cannot receive text messages, so you cannot use this integration for subscribers in countries where you're using a branded sender ID. Learn more [about SMS sending numbers](https://help.klaviyo.com/hc/en-us/articles/6637671573403).
- If you plan to use Gorgias to respond to SMS, you must have previously [set up SMS in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/4404274419355).
- Make sure that you’ve [reviewed key Inbox settings](https://help.klaviyo.com/hc/en-us/articles/360059002271#h_01JMFEZW49YCGTZ5TPZ35ZYMZN) including your auto-responder.
- Make sure that your [Inbox email notification address](https://www.klaviyo.com/inbox/settings/inbound-messages) is different from your Gorgias contact email address. If not, notifications in Gorgias will not appear properly.

### WhatsApp prerequisites

You’ll need to [set up WhatsApp in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/40111819732635). This involves connecting your WhatsApp Business account to Klaviyo, getting a phone number, and verifying your account.

### Reviews prerequisites

To use the reviews portion of the integration, you must collect reviews using Klaviyo Reviews. Learn how to [get started with Klaviyo Reviews](https://help.klaviyo.com/hc/en-us/articles/15937542819355).

****Multi-brand account guidance****

If you manage multiple brands within one Gorgias account, syncing one Gorgias brand per Klaviyo account makes it easy to use your ticket data and organize your SMS and WhatsApp conversations.

Before integrating Klaviyo with Gorgias, you’ll need to create a rule for each brand to tag tickets, and optionally create a view based on brand tags, to enable brand-specific syncing to and from Klaviyo.

#### Create rules in Gorgias to tag tickets by brand

In Gorgias, for each brand, you’ll need to create a rule that looks at the email the user is writing in to, and then tags the ticket with the appropriate brand:

1. In your Gorgias settings, select ****Rules**** (found under **Productivity**).
2. Add a new rule.
3. Name your rule something descriptive.
4. Add the following rule conditions:
   1. WHEN > TICKET CREATED > THEN
   2. IF > message integration > IS > [Brand-specific email address]
   3. THEN > ADD TAGS > [Brand-specific tag]
      ![](https://klaviyo.zendesk.com/hc/article_attachments/37721807239707)
5. Make sure **Enable rule** is set to ****On****.
6. Click ****Create Rule****.

Repeat this process for each brand that you want to integrate with a separate Klaviyo account.

#### (Optional) Create views in Gorgias based on brand tags

After setting up rules to auto-tag tickets, we recommend creating a view in Gorgias for each brand, containing all of the tickets tagged with the brand name:

1. In Gorgias, create a new view.
2. Add the following filter: Tags > Contains all of > [Brand tag]

![](https://klaviyo.zendesk.com/hc/article_attachments/37721807244699)

Repeat this process for each brand that you want to integrate with a separate Klaviyo account.

## Integrate with Gorgias

Follow the steps outlined below to integrate Gorgias with Klaviyo:

1. Log in to your Klaviyo account.
2. Select the ****Integrations**** tab.
3. Select ****Explore apps****, search for **Gorgias**, and click the card. Then, click ****Install****.
4. Enter your Gorgias helpdesk URL and click ****Connect to Gorgias****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/37721809907099)
5. Log in to Gorgias, if prompted.
6. Allow Klaviyo access to all resources by clicking ****Authorize****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/37721809908635)
7. Select whether you want to sync all new Gorgias tickets to Klaviyo, or only specific tickets containing certain tags.
   1. Klaviyo’s integration with Gorgias allows for syncing tickets on a per-brand basis through the use of tags.
   2. If you manage more than one brand within one Gorgias account, we recommend syncing one brand per Klaviyo account in order to avoid duplicate profiles across accounts. In the section above, we explained how to add tags and set up views for each brand in Gorgias.
      ![](https://klaviyo.zendesk.com/hc/article_attachments/37721807261339)
8. Check the **Sync SMS conversations** box to use SMS integration functionality.
   1. For multi-brand accounts, we recommend adding a tag corresponding to the Gorgias brand you want to use with this Klaviyo account.
      ![](https://klaviyo.zendesk.com/hc/article_attachments/37721809916827)
9. Check the box to **Sync WhatsApp conversations** to use WhatsApp integration functionality.
   1. Support agents can also use [a template to extend the WhatsApp conversation](https://help.klaviyo.com/hc/en-us/articles/40116778911259), ensuring they can continue engaging with the recipient beyond the 24-hour service window.
      ![Conversations box showing the option to sync WhatsApp conversations](https://klaviyo.zendesk.com/hc/article_attachments/41259951528475)
10. If you want to use the integration’s reviews functionality, check the **Sync reviews** box and select a threshold.
    1. The default threshold is 3, which means any reviews submitted with a rating of 3 or lower will automatically create a Gorgias ticket for your team to follow up on.
    2. For multi-brand accounts, we recommend adding a tag corresponding to the Gorgias brand you want to use with this Klaviyo account.
       ![](https://klaviyo.zendesk.com/hc/article_attachments/37721809920411)
11. RECOMMENDED: Check **Sync customer profile information from Klaviyo to Gorgias** to send contacts’ email addresses, phone numbers, profile properties, and more into Gorgias. This data will only sync if you have SMS or reviews enabled.
    ![](https://klaviyo.zendesk.com/hc/article_attachments/37721807279643)
12. If you're using [Customer Hub](https://help.klaviyo.com/hc/en-us/articles/33660324811675) and AI Agent: You can hand off customer queries the AI Service Agent can't answer to your team in Gorgias. Click ****Manage setting**** to go to the AI Agent settings and elect Gorgias as your [agent handoff.](https://klaviyo.zendesk.com/hc/en-us/articles/37659474656027)
    ![](https://klaviyo.zendesk.com/hc/article_attachments/38074454281243)
13. Click ****Complete setup****.

## Metrics synced between Gorgias and Klaviyo

The following metrics are synced in real time from Gorgias to Klaviyo. The metrics will appear on an individual’s profile page and can be used in segments and flows.

- **Opened Ticket**
- **Resolved Ticket**
- Satisfaction survey responded (e.g., **Completed Survey**)

  Each metric is stored with an associated profile. If a profile doesn't exist, one will be created in Klaviyo.

  If you are in a specific profile and view the activity for a metric, you’ll be able to see information such as:
- Who the ticket was assigned to
- Ticket ID and URL
- Channel (SMS or email)
- Message content
- Brand

  If you checked **Sync customer profile information from Klaviyo to Gorgias**, and have enabled SMS or reviews functionality, the following fields will sync from Klaviyo to Gorgias and appear in the right sidebar:
- Email address
- Phone number
- Location
- Consent
- Custom properties
- Activity

Note that if a profile doesn’t have a phone number or email address on their profile, Klaviyo will sync a placeholder (i.e., **555-555-5555** or **sms-integrations+kl{customer phone number})@klaviyo.com**). Do not use these placeholders to send support messages, as they will not be received.

## How the Gorgias SMS integration works

After the integration is set up, Klaviyo will automatically create a ticket in Gorgias whenever:

- A consented SMS subscriber texts a phone number associated with your account.
- The text message does not contain a keyword (i.e., one of the [subscribe words](https://help.klaviyo.com/hc/en-us/articles/360050384091) listed in your SMS Settings page in Klaviyo). The 2 exceptions to this are HELP and INFO, which will both create a ticket.

Branded sender IDs (also called alphanumeric sender IDs) cannot receive text messages, so you cannot use this integration for subscribers in countries where you're using a branded sender ID. Learn more [about SMS sending numbers](https://help.klaviyo.com/hc/en-us/articles/6637671573403).

If a customer sends an image or GIF with a text message, the image will not be displayed in Gorgias. Similarly, you cannot send MMS messages from Gorgias.

Any subsequent messages are automatically added to the ticket.

Responses from within Gorgias will also appear in Klaviyo, but responses sent within the [Klaviyo Inbox](https://help.klaviyo.com/hc/en-us/articles/360059002271) will not appear in Gorgias. For this reason, we recommend that you only reply to customers from 1 platform. Additionally, flow, campaign, and auto-response messages sent via Klaviyo will not appear in Gorgias.

Replies from Gorgias are sent using the same channel as the latest inbound message, and sent via a phone number associated with your Klaviyo account. If a subscriber texts you, the reply will be an SMS sent via the toll-free number, long code, or short code in your account.

Messages from Gorgias count toward your [SMS billing](https://help.klaviyo.com/hc/en-us/articles/115000976672) plan like any other message. We recommend creating a template in Gorgias for SMS responses that fall under 153 characters if possible. Learn more about [SMS best practices](https://help.klaviyo.com/hc/en-us/articles/360035661191#h_01HCJKFZS852ZMJJF6SXW2SJ55).

## How the Gorgias WhatsApp integration works

After the integration is set up, Klaviyo will automatically create a ticket in Gorgias whenever:

- A customer sends an inbound message to your business on WhatsApp.
- If the message doesn’t match compliance, subscribe, or automated conversation keywords, Klaviyo will prompt the creation of a support ticket in Gorgias.

Your support agent can answer the customer in Gorgias, and the response will send via your WhatsApp business number.

Please note that the agent response type will appear in Gorgias as **Email**, but it will be sent via WhatsApp.

![Agent response type in Gorgias](https://klaviyo.zendesk.com/hc/article_attachments/41259964479003)

In the **Klaviyo channel** side panel, you’ll be able to see information about the message, including the channel (WhatsApp or SMS) and the consent status.

![Message details, showing consent for WhatsApp](https://klaviyo.zendesk.com/hc/article_attachments/41259964480155)

If the WhatsApp consent status is **Expired**, and you’ve enabled the follow-up setting referenced in the previous section, your agent can click ****WhatsApp Follow Up**** to send the template to the customer. If the customer responds, the 24 hours window resets and the conversation can continue.

If a customer sends an image or other media with a WhatsApp, the image will not be displayed in Gorgias. Similarly, you cannot send images or other media messages from Gorgias.

## How the Gorgias reviews integration works

After the integration is set up, Klaviyo will automatically create a new ticket whenever someone submits a review that meets the criteria you set (i.e., has a star rating at or below your selection).

The contact details available within the ticket depend on whether or not you enable the **Sync customer profile information from Klaviyo** option in your Gorgias integration settings.

- If the setting is disabled:
  Klaviyo will only sync the reviewer’s phone number, if available. If the reviewer does not have a phone number in Klaviyo, we will use a spoof phone number (555-555-5555) to create the ticket, and you may not see any real contact information for the ticket in Gorgias.
- If the setting is enabled:
  Klaviyo will sync their profile information into Gorgias, including email and phone number. If a profile doesn’t have an email address, Klaviyo will sync a spoof email address instead: sms-integrations+kl{customer phone number})@klaviyo.com. If a profile doesn’t have a phone number, we will sync a spoof phone number (555-555-5555). Every profile will have at least 1 valid form of contact information.

  Regardless of the profile information setting selected, the following review details will be available in the ticket sidebar:
- Review attributes:
  - Star rating
  - Author
  - Review date
  - Verified status
  - Publish status
- Product information:
  - Product name
  - Product URL
  - Product image URL

    Additionally, the ticket contains the following information:
- Product name
- Customer rating
- Review body

## When the integration syncs

The integration syncs in real time. As soon as an SMS subscriber texts you or a customer submits a review, that message will appear in Gorgias.

Note that there is no historic sync. SMS tickets in Klaviyo and past reviews won’t appear in Gorgias if a subscriber texted you or left a review before you set up this integration. However, all further messages will sync. If a subscriber texts you or submits a review once before you enable the integration and once after, the message that comes in after you set up the integration will show in Gorgias, but the one sent before will not.