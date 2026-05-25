---
id: "37673288455323"
title: "Getting started with Guesty"
source_url: "https://help.klaviyo.com/hc/en-us/articles/37673288455323-Getting-started-with-Guesty"
section: "Guesty"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-20T17:29:57Z"
language: "en"
---
Learn how to integrate Klaviyo with Guesty, a property management platform for short term rentals. Klaviyo syncs guests, booking, and messages from Guesty, which allow you to personalize your messaging to guests.

## Integrate Klaviyo with Guesty

First, you’ll need to obtain an API key from Guesty:

1. Log in to your Guesty admin.
2. Select ****Integrations > Marketplace****.
3. Search for **Klaviyo**, then select the Klaviyo listing.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/38043405531035)
4. Click ****Connect****.
5. Copy the newly generated Guesty API Key.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/38043390294299)

   Then, you’ll need to set up the integration in Klaviyo:
6. Log in to Klaviyo.
7. Select the ****Integrations**** tab.
8. Click ****Explore apps****.
9. Search for **Guesty** and select the card.
10. Click ****Install****.
11. Paste the Guesty API Key you copied in the box.
    ![](https://klaviyo.zendesk.com/hc/article_attachments/38043390298011)
12. Click ****Connect****.
13. Review the permissions in Klaviyo and click ****Allow****.
    ![](https://klaviyo.zendesk.com/hc/article_attachments/38043390299931)
14. On the next page, check the box **Sync your Guesty email subscribers to Klaviyo** if you’d like to do so.
    ![](https://klaviyo.zendesk.com/hc/article_attachments/38043405546139)
15. If you selected the setting above, select a list from the dropdown to add Guesty email subscribers to. Make sure that this list is set to [single opt-in](https://help.klaviyo.com/hc/en-us/articles/115005251108#h_01HZ5G5ZQBDHTV20V1BE7D4YAT) to avoid triggering opt-in emails to guests syncing from Guesty.
16. When you’re done, click ****Complete setup****.
17. You’ll receive a success message confirming that your Guesty integration is now connected.

![](https://klaviyo.zendesk.com/hc/article_attachments/38043390305819)

## Update your Guesty integration

To update your integration:

1. Log in to Klaviyo.
2. Select the ****Integrations**** tab.
3. Click ****Guesty.****
4. Click the ****Update**** button in the banner.
   ![Screenshot 2026-01-30 at 4.27.40 PM.png](https://klaviyo.zendesk.com/hc/article_attachments/46089570265499)
5. Click ****Connect****.
6. Review the permissions in Klaviyo and click ****Allow****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/38043390299931)
7. On the next page, check the box **Sync your Guesty email subscribers to Klaviyo** if you’d like to do so.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/38043405546139)
8. If you selected the setting above, select a list from the dropdown to add Guesty email subscribers to. Make sure that this list is set to [single opt-in](https://help.klaviyo.com/hc/en-us/articles/115005251108#h_01HZ5G5ZQBDHTV20V1BE7D4YAT) to avoid triggering opt-in emails to guests syncing from Guesty.
9. When you’re done, click ****Complete setup****.
10. You’ll receive a success message confirming that your Guesty integration is now connected.

![](https://klaviyo.zendesk.com/hc/article_attachments/38043390305819)

## Add onsite tracking

If you’re using Guesty’s booking engine, you can add Klaviyo onsite tracking to your site via the installation of a custom code snippet. This snippet also enables the use of [Klaviyo forms](https://help.klaviyo.com/hc/en-us/articles/360026474752) on your site.

To install the code on your site:

1. In Klaviyo, select your account name in the lower left.
2. Select ****Settings****.
3. Click ****API Keys****.
4. Copy your Public API Key.

1. Log in to Guesty.
2. Select the ****Operations**** dropdown at the top, then select ****Growth > Distribution****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/49254970231323)
3. Select ****Guesty Booking Engine****.
4. Click the triple dots next to your booking engine and select ****Edit Booking Engine****.
5. Scroll to the **Custom code snippet** section and make sure ****Turn on custom code snippet**** is toggled on.
6. Copy the [GuestyEvents code from Github](https://gist.github.com/cbarley10/64ebafb5c8043ef5b2c8cb61145d9f5e) and paste it into the custom code snippet box.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/49254970233115)
7. In the code snippet, replace COMPANY\_ID with your Klaviyo Public API Key. To find your Klaviyo Public API Key:
8. Click ****Next**** until you’ve reached the last step of the editor.
9. Select ****Save Booking Engine.****

You’ve now installed onsite tracking for Guesty.

This code tracks the following events for [known browsers](https://help.klaviyo.com/hc/en-us/articles/115005076767#h_01HADAYAACVVC4BXQ0ES5Y50TC) and syncs them to Klaviyo:

- Active on Site
- Viewed Listing
- Started Checkout

## View your Guesty data

To view your Guesty data:

1. Navigate to ****Analytics > Metrics****. Here, you can view all of the metrics in your account. The metrics with a Guesty icon represent all of the metrics synced from your Guesty integration.
2. Use the **All integrations** dropdown and select **Guesty** to view only Guesty metrics.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/38043390310043)

   To view your Guesty objects (note: requires the latest version of the integration):
3. Navigate to****Content > Objects****. Here, you can view all of the objects in your account. The objects with a Guesty icon represent all of the objects synced from your Guesty integration.

Learn [more about your Guesty data](https://help.klaviyo.com/hc/en-us/articles/37673417604507).

## Segment guests using Guesty data

You can use Guesty metrics to segment guests. Using metrics, for example, you can create a segment of guests who have confirmed a reservation at a specific location:

1. What someone has done (or not done) > Confirmed Reservation (Guesty) > at least once > over all time
2. where > Listing Title > equals > (Your Title)
   ![](https://klaviyo.zendesk.com/hc/article_attachments/38043390311835)

1. Navigate to ****Audience > Lists & segments****.
2. Click ****Create New**** and choose ****Create new segment****.
3. Name your segment and select tags if desired.
4. Select the following definition and filter:
5. Click ****Create segment****.

   Using objects, you can create a segment of guests who have a reservation start date from tomorrow onwards:

   ![Screenshot 2026-01-28 at 5.38.24 PM.png](https://klaviyo.zendesk.com/hc/article_attachments/46002390175131)
6. Navigate to ****Audience > Lists & segments****.
7. Click ****Create New**** and choose ****Create new segment****.
8. Name your segment and select tags if desired.
9. Select the following definition and filter:
   1. Properties about someone > Reservation (Guesty) > has at least one
   2. where > StartDate > in the next > 5200 weeks
10. Click ****Create segment****.

## Use Guesty data in flows

You can use Guesty metrics to trigger flows, or sequences of automated actions. Klaviyo offers multiple pre-built flows using Guesty data. These flows include booking confirmations, pre-stay flows, and more.

To view these pre-built flows:

1. In Klaviyo, select the ****Flows**** tab.
2. Click ****Create flow****.
3. Filter by **Guesty** to see all Guesty flows.

![](https://klaviyo.zendesk.com/hc/article_attachments/38043405558555)

You can also create a flow with Guesty objects. To create a pre-arrival flow, for example, you can:

- Navigate to Flows > ****Create flow**** > ****Build your own.****
- Name the flow and select tags (optional).
- Select the **Date property** trigger.
  ![Screenshot 2026-01-28 at 5.10.42 PM.png](https://klaviyo.zendesk.com/hc/article_attachments/46002390176155)
- Select Guesty, Reservation: CheckInDateAndTime from the Date property dropdown.
- Choose the time you'd like to start the flow.
- Add the relevant messages in.

You can also create your own flows from scratch.