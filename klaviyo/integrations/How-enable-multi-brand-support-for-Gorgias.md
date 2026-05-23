---
id: 33997568400539
title: "How enable multi-brand support for Gorgias"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/33997568400539-How-enable-multi-brand-support-for-Gorgias"
section: "Gorgias"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:56:49Z"
language: en
---

Learn how enable multi-brand support for Klaviyo's Gorgias integration, if you integrated Klaviyo and Gorgias before Klaviyo introduced support for multiple Gorgias brands.

Tickets, SMS messages, WhatsApp messages and reviews can now be synced on a per-brand basis. If you manage multiple brands within one Gorgias account, syncing one Gorgias brand per Klaviyo account makes it easy to use your ticket data and organize your SMS and WhatsApp conversations.

Enabling multi-brand support requires 4 steps:

1. (Optional) Remove existing “incorrect” Gorgias profiles from Klaviyo
2. Create rules in Gorgias to tag tickets by brand
3. (Optional) Create views in Gorgias based on the brand tag
4. Update your Gorgias integration settings

Looking to integrate for the first time? Head to [Getting started with Gorgias](https://help.klaviyo.com/hc/en-us/articles/4408023789083).

## Before you begin

Please note that when you update your Gorgias integration to enable multi-brand support, historical data previously synced through the integration will remain in your account, unless you choose to manually remove Klaviyo profiles.

## (Optional) Remove Gorgias profiles from Klaviyo

If you want to now associate your Klaviyo account with a specific Gorgias brand, you may want to remove Gorgias profiles previously synced through the integration.

Since there is no brand associated with these older profiles, profiles from specific brands cannot be precisely deleted. Instead, we recommend deleting profiles that synced through your Gorgias integration but did not have any interactions with the ecommerce site associated with your Klaviyo account. These profiles are likely to have been synced from the “wrong” brand(s).

To do this, we recommend creating a segment of these profiles and then deleting it. This should be done before you update your Gorgias integration.

To create the segment:

1. What someone has done or not done > Opened Ticket (Gorgias) > at least once > over all time AND
2. What someone has done or or not done > Viewed Product > zero times > over all time AND
3. What someone has done or or not done > Checkout Started > zero times > over all time AND
4. What someone has done or or not done > Placed Order > zero times > over all time AND
5. What someone has done or or not done > Subscribed to List (Klaviyo) > zero times > over all time

1. In Klaviyo, navigate to ****Audience > Lists & segments****.
2. Select ****Create New > Create segment****.
3. Name your segment and select any tags.
4. Add the following segment conditions, using events synced from your ecommerce platform:
5. You can also add conditions for any other applicable events in your account, specifying that a profile has not tracked them.
6. Click ****Create segment****.
7. Then, delete the segment you created above by following our [bulk deleting instructions](https://help.klaviyo.com/hc/en-us/articles/24312135764251#h_01HT5F82SYT68E2X2Z68DC78RR).

## Create rules in Gorgias to tag tickets by brand

In Gorgias, for each brand, you’ll need to create a rule that looks at the email the user is writing in to, and then tags the ticket with the appropriate brand:

1. WHEN > TICKET CREATED > THEN
2. IF > message integration > IS > [Brand-specific email address]
3. THEN > ADD TAGS > [Brand-specific tag]
   ![](https://klaviyo.zendesk.com/hc/article_attachments/37720714482587)

1. In your Gorgias settings, select ****Rules**** (found under **Productivity**).
2. Add a new rule.
3. Name your rule something descriptive.
4. Add the following rule conditions:
5. Make sure **Enable rule** is set to ****On****.
6. Click ****Create Rule****.

Repeat this process for each brand that you want to integrate with a separate Klaviyo account.

## (Optional) Create views in Gorgias based on the brand tag

After setting up rules to auto-tag tickets, we recommend creating a view in Gorgias for each brand, containing all of the tickets tagged with the brand name:

1. In Gorgias, create a new view.
2. Add the following filter: Tags > Contains all of > [Brand tag]

![](https://klaviyo.zendesk.com/hc/article_attachments/37720796406427)

Repeat this process for each brand that you want to integrate with a separate Klaviyo account.

## Update your Gorgias integration settings

To update your Gorgias integration settings and enable multi-brand support in a given Klaviyo account:

1. In Klaviyo, select the ****Integrations**** tab.
2. Select **Gorgias** from the list of enabled integrations.
3. We recommend connecting one Gorgias brand per Klaviyo account. Under **Tickets**, select the tag corresponding to the Gorgias brand that you want to use with this Klaviyo account and sync new tickets to Klaviyo for.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/37720914786459)
4. If you’re using SMS conversations: Under **Conversations**, we recommend adding a tag corresponding to the Gorgias brand you want to use with this Klaviyo account.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/37720900025883)
5. Check the box to **Sync WhatsApp conversations** to use WhatsApp integration functionality.
   1. Support agents can also use [a template to extend the WhatsApp conversation](https://help.klaviyo.com/hc/en-us/articles/40116778911259), ensuring they can continue engaging with the recipient beyond the 24-hour service window.
      ![Conversations box showing the option to sync WhatsApp conversations](https://klaviyo.zendesk.com/hc/article_attachments/41259966180635)
6. If you’re using reviews: Under **Reviews**, we recommend adding a tag corresponding to the Gorgias brand you want to use with this Klaviyo account.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/37720900027291)
7. When you’re done, click ****Update settings****.

You’ll need to integrate with Gorgias and configure the above brand-related settings for each Klaviyo account that you want to connect with a Gorgias brand.