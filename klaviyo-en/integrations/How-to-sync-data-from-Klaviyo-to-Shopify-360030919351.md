---
id: "360030919351"
title: "How to sync data from Klaviyo to Shopify"
source_url: "https://help.klaviyo.com/hc/en-us/articles/360030919351-How-to-sync-data-from-Klaviyo-to-Shopify"
section: "Shopify best practices"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:44Z"
language: "en"
---
## You will learn

Learn how to sync customer information such as profile information, custom properties, email and SMS subscription statuses, and events from Klaviyo to Shopify. You’ll make these changes from your Shopify integration settings page in Klaviyo. You can choose whether to sync updates for either all existing and new Klaviyo profiles, or only for Shopify-known profiles.

## Before you begin

- If you have not already, read our article on [getting started with Shopify](https://help.klaviyo.com/hc/en-us/articles/115005080407-How-to-Integrate-with-Shopify) for step-by-step instructions on integrating, before continuing with this article.
- Deleting a profile in Klaviyo will not cause it to be deleted in Shopify, and vice versa.

## Synchronizable data

You can customize which data you want to sync via the integration settings page. Once you configure these settings, the following fields will only sync if they were previously empty for an existing customer in Shopify:

- First name
- Last name
- Email
- Phone number

The fields from Klaviyo that will update pre-existing fields in Shopify are:

- Email subscription status
- SMS subscription status

New fields that will be created in Shopify are:

- Custom profile properties.

- You have the option to sync any custom profile properties that exist in Klaviyo, including those ingested from other platforms. These properties will be created as metafield definitions in Shopify and their values will be updated on the corresponding customer in Shopify.
- The number of metafield definitions per object is limited to 250 in Shopify, so you may only sync custom properties up to that limit.
- If you try to sync a custom property from Klaviyo back to Shopify, using a different data type than the one that was originally used to create the metafield definition in Shopify (e.g., string instead of array), the metafield will not update in Shopify.

- Email received (received by a Klaviyo profile, i.e., sent by a Klaviyo customer), opened, and clicked events.
- SMS message received (received by a Klaviyo profile, i.e., sent by a Klaviyo customer) and clicked events.

Please note that Klaviyo email received, opened, and clicked events, along with SMS message received and clicked events, are not individually viewable in Shopify but [are included in marketing attribution reports](https://help.shopify.com/en/manual/promoting-marketing/analyze-marketing/app-data-sharing).

We recommend syncing all profiles and all possible fields for greater data alignment between the platforms. Klaviyo data can be used to drive more value within Shopify, including via enhanced attribution reporting and business automation.

## Sync fields from Klaviyo to Shopify

1. In Klaviyo, head to your [Shopify integration settings page](https://www.klaviyo.com/integration/shopify).
2. Scroll to the **Sync settings** section and click the **To Shopify** tab.
3. Check the setting: ****Sync profiles, profile data, and custom properties**** ****from Klaviyo to Shopify****.
4. Choose whether to sync updates for either all Klaviyo profiles or only for profiles that already exist in Shopify.

   If you choose all profiles, Klaviyo will create new customers in Shopify for all profiles (existing and new) created in Klaviyo. This includes profiles synced from other Klaviyo integrations, or added through list imports, even if they have not interacted with your Shopify store.
5. Next, you can choose which updates to sync to Shopify:
   - ****Name, email address, and phone number****If you choose this option (and you choose to sync all profiles), a backfill of all in-scope profiles will occur after you integrate (or update your integration) to ensure Klaviyo and Shopify are in sync. Going forward, new profiles will be created in Shopify with this data as they are created in Klaviyo (if they do not already exist in Shopify).
   - ****Email subscription status****
     Selecting this setting will not prompt a backfill of email subscription statuses. Going forward, email consent status updates in Klaviyo (i.e., subscribes and unsubscribes) will trigger updates in Shopify. Note that suppression status in Klaviyo does not sync to Shopify and does not affect consent status in Shopify.
   - ****SMS subscription status (if you have SMS enabled)****
     If you choose this option (and you choose to sync all profiles), a backfill of all SMS subscription statuses and associated phone numbers will occur after you integrate (or update your integration) to ensure Klaviyo and Shopify are in sync. Going forward, SMS consent status updates in Klaviyo will trigger updates in Shopify.
   - ****Email received, opened, and clicked events****
     Selecting this option will not prompt a backfill of this data.
   - ****SMS message received and clicked events (if you have SMS enabled)****Selecting this option will not prompt a backfill of this data.
   - ****Custom properties****Click ****Select Properties**** to choose which properties you want to sync to Klaviyo. Then, you can search for properties and click the plus sign to add them, or click ****Add all**** to add all properties. When you are done selecting properties, click ****Save****. You can edit, add, or remove these properties at any time. Selecting custom properties will prompt a backfill for those properties.
     ![](https://klaviyo.zendesk.com/hc/article_attachments/28717381154843)
6. Click ****Save****.

![](https://klaviyo.zendesk.com/hc/article_attachments/28717387436699)

Once you've updated your settings, Klaviyo will begin syncing any necessary backfill to Shopify.

## Sync frequency

****Name, email address, phone number, subscription statuses, and custom properties****: When new changes are made to your specified profiles (after any initial backfill), these will be reflected in Shopify within 30 minutes of a change being made in Klaviyo, though most changes should reflect within a minute.

****Email received, opened, and clicked events, and SMS message received and clicked events****: These changes sync to Shopify within 24 hours.

## Outcome

Shopify profiles will now be updated with Klaviyo data according to the settings you selected.

## Additional resources

- [Getting started with Shopify](https://help.klaviyo.com/hc/en-us/articles/115005080407)
- [How to sync Shopify email subscribers to a Klaviyo list](https://help.klaviyo.com/hc/en-us/articles/115005080667)
- [How to collect SMS consent at checkout on Shopify](https://help.klaviyo.com/hc/en-us/articles/360056824732)