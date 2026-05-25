---
id: "115005082767"
title: "How to migrate from another email service provider to Klaviyo"
source_url: "https://help.klaviyo.com/hc/en-us/articles/115005082767-How-to-migrate-from-another-email-service-provider-to-Klaviyo"
section: "Migrate from an email service provider"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:20Z"
language: "en"
---
## You will learn

Learn how to migrate from another email service provider to Klaviyo. If you are moving from an email service provider (ESP) like Mailchimp or Constant Contact, Klaviyo should fully replace any other email platform you might use. While we do offer integrations with other ESPs, these are meant for one-time use to migrate your contacts into your new Klaviyo account.

## Before you begin

If you see your ESP listed below, you should follow one of our specific guides on how to integrate with Klaviyo:

- [Mailchimp](https://help.klaviyo.com/hc/en-us/articles/115005254948)
- [Constant Contact](https://help.klaviyo.com/hc/en-us/articles/115005082727)
- [Campaign Monitor](https://help.klaviyo.com/hc/en-us/articles/115005254968)
- [Hubspot](https://help.klaviyo.com/hc/en-us/articles/360039708512)
- [Listrak](https://help.klaviyo.com/hc/en-us/articles/360034550591)
- [Sailthru](https://help.klaviyo.com/hc/en-us/articles/360036945872)
- [Salesforce Marketing Cloud](https://klaviyo.zendesk.com/hc/en-us/articles/115000267471)

Some ESPs provide their own guidance on how to migrate to Klaviyo.

## Key guidelines

1. ****Swap out embedded simple sign-up forms****
   Make sure to switch all existing sign-up forms on your site to Klaviyo forms to ensure these individuals now get added to your email list in Klaviyo.
2. ****Redirect integrated subscriber forms****
   If you're using any third-party form tools (e.g. Wufoo, forms on Facebook, etc.) to send people to your ESP, make sure to adjust these so they point to Klaviyo.
3. ****Sync subscribers at checkout****
   If you're automatically collecting email subscribers through your shopping cart checkout process, make sure these subscribers get synced to Klaviyo; for platforms like Shopify and Magento, this feature is available via the standard integration.
4. ****Import current bounces and unsubscribes****
   If you are using a built-in Klaviyo integration to migrate over from your former ESP, you're all set here; if not, you will need to ensure any lists of bounces/unsubscribes are uploaded directly to your [suppression list](https://www.klaviyo.com/people/suppressed) in Klaviyo.
5. ****Migrate current autoresponders****
   Migrate any existing autoresponders to flows and turn them live.
6. ****Migrate saved email templates****
   If you are interested in transferring existing email templates from your former ESP to Klaviyo, you can follow our guide on [importing a custom HTML template](https://help.klaviyo.com/hc/en-us/articles/115005254068).
7. ****Ensure all existing subscribers are added**** ****to**** ****Klaviyo:****
   1. If you're using Mailchimp/Campaign Monitor/Constant Contact/Mad Mimi, Klaviyo has built-in integrations to sync existing lists, which you can find by:
      1. Selecting the ****Integrations****tab in Klaviyo.
      2. Clicking ****Explore apps****.
      3. Searching for your ESP, selecting it, then clicking ****Install**** and following the process.
   2. If you're using an ESP that we don't integrate with or have an existing subscriber list in a CSV or Excel file, you can easily [import your subscribers to Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115002053752).

Once you have completed all of these steps, you will no longer need to be affiliated with your previous ESP.

## Important considerations and best practices

1. Make sure you have imported all of the data you want to save from your previous ESP into Klaviyo so that data will be available to use after you’ve completed the migration.
2. After switching all your sign-up forms to point to Klaviyo, wait a few days and watch your lists in your former ESP. If you notice subscribers are still being added to these lists, there's probably at least one form that still needs to be swapped out.
3. Another important thing to consider before importing any existing email lists is [list cleaning](https://klaviyo.zendesk.com/hc/en-us/articles/115005078347). We highly recommend that you import clean lists into Klaviyo and send to an engaged list from your first send - if you intend to sync over existing email lists, or manually import existing lists into Klaviyo, your email deliverability may be at risk if you skip this step.
4. Your former ESP most likely provides a way to analyze the engagement level of your main list, using data points such as open rates, bounce rates, etc. Before you migrate any existing subscriber lists into Klaviyo, we recommend using all data available to isolate and remove any invalid or inactive emails that will only bloat your sending and drag down your deliverability. This should all be done in advance of your first send with Klaviyo. If Klaviyo doesn't provide a built-in integration with your ESP, there are two ways you can make sure you're sending to an engaged list:
   1. Upload a main list with engagement data as custom properties.
   2. Upload separate main, engaged, and inactive lists.
   3. Once you've done either of the first two options, you should send exclusively to your engaged list or segment for your first few campaigns. If you send daily, send to this group for the first week. If you send more than once a week, send your first 2-3 campaigns to this list or segment.

## Outcome

You've now migrated from another email service provider to Klaviyo.

## Additional resources

- [How to import your contacts from a previous ESP or CRM](https://help.klaviyo.com/hc/en-us/articles/115002053752)
- [Import SMS contact and phone number resources](https://help.klaviyo.com/hc/en-us/sections/7704203383579-Import-SMS-contacts-and-phone-numbers-)
- Need more help integrating with Klaviyo? Check out [Klaviyo's Agency Partners](https://klaviyo.partnerpage.io/?utm_source=helpcenter&utm_medium=integrations)