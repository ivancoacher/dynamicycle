---
id: "115005252988"
title: "How to integrate with Segment"
source_url: "https://help.klaviyo.com/hc/en-us/articles/115005252988-How-to-integrate-with-Segment"
section: "Segment"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:23Z"
language: "en"
---
## You will learn

Learn how to integrate Segment with Klaviyo to be able to trigger and filter flows, and define segments using events synced to Klaviyo from your Segment project. Klaviyo is able to sync any `track` and `identify` calls you make from Segment to Klaviyo.

This integration takes two steps: enabling the integration on the Segment side, and enabling the integration on the Klaviyo side. Make sure to also explore Segment's [comprehensive guide to integrating with Klaviyo](https://segment.com/docs/connections/destinations/catalog/actions-klaviyo/).

## Before you begin

This integration now supports the two-way flow of information between Segment and Klaviyo, but you will need to select either Klaviyo or Segment as your primary source of truth for profile creation.

If you select Klaviyo as your primary source, note the following: profiles generated in Segment contain a unique ID which Klaviyo keeps track of to record where these profiles came from. Klaviyo cannot easily reconcile duplicate profiles from different sources, so there is a chance of pushing duplicated profiles to Segment. See the **Enable Integration in Klaviyo** section below for more information.

## Connect Segment and Klaviyo

### Add Klaviyo destination to Segment

1. From your Segment project page, click ****Connections**** in the left hand navigation bar, then click ****Add Destination**** on the right side of the page.
   ![Connections tab in Segment with Add Destination button with blue background](https://klaviyo.zendesk.com/hc/article_attachments/28723518315803)
2. Search for **Klaviyo** in the Segment catalog. Once it appears, click on the Klaviyo tile, and then click ****Configure Klaviyo**** on the next page.
   ![Segment catalog with Klaviyo in search bar and Klaviyo card in results](https://klaviyo.zendesk.com/hc/article_attachments/28723518312987)
3. Select and confirm a source from your Segment project. On the next page, enter all of the following:
   - Your public Klaviyo API key. Learn [how to find your public and private API keys in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115005062267).
   - The list ID of the default Klaviyo list you want to sync with. Learn [how to find your List ID in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115005078647).
   - A private Klaviyo API key. Treat private API keys like passwords kept in a safe place and never exposed to the public.
     ![Klaviyo setup page in Segment with fields for API key, List ID, and Enter your private API Key](https://klaviyo.zendesk.com/hc/article_attachments/28723506665883)
4. Finally, scroll down to **Other Settings** to verify that **Enforce Email as Primary Identifier** is set to ****On****. It should be toggled on by default. If not, click into the setting and set it to ****On****.
   ![Klaviyo setup page in Segment Other Settings section with Confirm Optin set to On and Enforce Email as Primary Identifier set to On](https://klaviyo.zendesk.com/hc/article_attachments/28723506671643)
5. To enable the integration on Klaviyo’s side, you’ll first need to get your write key from Segment. In Segment, navigate to ****Connections > Sources****, and click on the site you’d like to connect with Klaviyo.
   ![List of sources in Connections tab in Segment showing test website in list](https://klaviyo.zendesk.com/hc/article_attachments/28723518319771)
6. Click on the ****Settings**** tab at the top and then select ****API Keys****.
   ![Test website source page in Segment with Settings tab selected, with Source ID and Write Key blurred out](https://klaviyo.zendesk.com/hc/article_attachments/28723506684059)
7. Copy your **Write Key**. Your write key is another private API key. Treat it like a password; keep it in a safe place and never expose it to the public.

### Enable the integration in Klaviyo

1. In Klaviyo, select the ****Integrations**** tab.
2. Select ****Explore apps****, search for **Segment**, and then click the card. Then, click ****Install****.
3. Paste the write key you copied earlier into the box, then click ****Connect to Segment****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28723506700315)
4. On the next page, you'll have the ability to limit the data you pass back to Segment, by checking the box next to **Do not sync profiles that are not updated by the Klaviyo Destination**.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28723518331035)
   - As noted in the Overview, this integration now supports the ability to pass information back and forth between Segment and Klaviyo, using a unique ID to keep track of which profiles are originally from Segment. If you have multiple integrations enabled in Klaviyo, there is a possibility that the same customer will interact with you from two separate sources, and as a result, this customer will end up with duplicated profiles in Klaviyo.
   - To help avoid this duplication of profiles across multiple services, you can check the box above, which will limit the profiles Klaviyo syncs with Segment to only the profiles originally created in Segment.
5. Once finished, click ****Complete setup****.

## Segment metrics

We recommend syncing the most important events to Klaviyo, such as:

- When a customer signs up
- When a customer starts to checkout or expresses interest in paying
- What a customer buys (including pictures of items and descriptions of items)

For each event you send through Segment, a customer is identified by their email address. For detailed information on how to format these events, see the [Segment's Klaviyo Integration](https://segment.com/docs/connections/destinations/catalog/actions-klaviyo/) guide.

For transactional web businesses and ecommerce platforms, we recommend following our [guide to integrating a custom ecommerce cart or platform](https://developers.klaviyo.com/en/v1-2/docs/guide-to-integrating-a-platform-without-a-pre-built-klaviyo-integration) guide for detailed information on the events that should be sent to Klaviyo through Segment.

## Monitoring the Klaviyo sync

Once you activate the Klaviyo integration inside of Segment, your `identify` and `track` calls will begin sending data to Klaviyo within 5-10 minutes. To verify Segment is sending data to Klaviyo, click the ****Analytics**** dropdown in Klaviyo and select the ****Metrics**** tab.

As events are triggered in Segment, they will send data to Klaviyo, where the event name from the Segment `track` call is used to create the metric name. Klaviyo treats Segment metrics as third-party API metrics, so each metric will have a gear icon next to its name in Klaviyo. To view the data as it flows into Klaviyo, navigate to the **Activity Feed** for each metric.

![segment9.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28723506691995)

## Outcome

You've now integrated Segment with Klaviyo and can start using Segment data to trigger and filter flows, and define segments using events synced to Klaviyo from your Segment project.

## Additional resources

- [Getting started with flows](https://help.klaviyo.com/hc/en-us/articles/115002774932)
- [Getting started with segments](https://help.klaviyo.com/hc/en-us/articles/115005237908)
- [How to add a conditional split to a flow](https://help.klaviyo.com/hc/en-us/articles/115003872171)