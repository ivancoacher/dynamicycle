---
id: 115005082207
title: "How to integrate with Recurly"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005082207-How-to-integrate-with-Recurly"
section: "Recurly"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:20Z"
language: en
---

## You will learn

Learn how to integrate Recurly with Klaviyo in order to personalize and target emails based on invoice and payment data from your customers. Klaviyo syncs the following data from Recurly:

- When an invoice is issued, and the items included in each invoice
- Payment information for when a customer fails payment, is refunded, or successfully pays
- Profile properties associated with Recurly information

## Integrate Recurly with Klaviyo

1. To integrate Recurly with Klaviyo, you’ll need your Recurly API Key, so start by logging in to your Recurly account.
2. Navigate to ****Integrations > API Credentials****.
3. Copy the Private API Key under ****Default API Key**** for use later.

   Private API keys, such as your default key used here, should be treated like passwords; keep them in a safe place and never expose them to the public.

   ![Default API Key section in Recurly with private API key blurred out](https://klaviyo.zendesk.com/hc/article_attachments/28715962324763)
4. If your default API key is already in use with another third-party integration, you can generate a new default API key for the Klaviyo integration by clicking on ****Add Private API Key****. ![Private API Keys in Recurly showing Default API Key blurred out and Add Private API Key with gray background at the bottom](https://klaviyo.zendesk.com/hc/article_attachments/28715968889883)

   Recurly will only generate 5 private API keys to integrate with third-party applications.
5. If you created a new API key, copy it for use in your Klaviyo account.
6. In your Klaviyo account, select the ****Integrations**** tab.
7. Click ****Explore apps****, search for **Recurly**, and click the card. Then, click ****Install****.
8. Enter your Recurly subdomain and your API key copied earlier, then click ****Connect to Recurly****. ****![](https://klaviyo.zendesk.com/hc/article_attachments/28715962340123)****
9. If the integration is successful, a success message will appear.

## Monitor the Recurly sync

You can monitor the data syncing from Recurly to Klaviyo.

1. In Klaviyo, click the ****Analytics**** dropdown and then select ****Metrics****.
2. Search for one of the Recurly metrics such as **Issued Invoice** and click on the Activity Feed icon. ![Page showing list of Issued Invoice via Recurly metrics in Klaviyo with timestamps](https://klaviyo.zendesk.com/hc/article_attachments/28715968896155)
3. If your integration has started syncing data, you will start to see **Issued Invoice** events, with the Recurly icon, added to this activity feed.
4. Klaviyo imports all of your Recurly data, and to verify this, you can compare the number of successful payments on a particular day to the data in Recurly and confirm they match.
5. If the data doesn’t match up, the issue is most likely that the timezone in your Klaviyo account doesn't match the timezone in your Recurly account.
6. To check your timezone setting in Klaviyo:
   - Click your account name in the lower left corner.
   - Select ****Settings**** .
   - Select ****Organization****, then scroll down to **Timezone**.

## Data synced from Recurly to Klaviyo

### Metrics

Recurly syncs the following metrics to Klaviyo:

- ****Failed Payment****
  Recorded every time a payment made through Recurly is marked as failed.
- ****Issued Invoice****
  Recorded every time an invoice is issued to a customer through Recurly.
- ****Ordered Product****
  Recorded every time a customer places an order through Recurly.
- ****Refunded Payment****
  Recorded when you refund a payment through Recurly.
- ****Successfully Paid****
  Recorded each time a customer successfully pays an invoice through Recurly.
  ![Metrics tab in Klaviyo filtered by Recurly with metrics such as Failed Payment and Issues Invoice](https://klaviyo.zendesk.com/hc/article_attachments/28715962335259)

### Profile properties

The following properties are synced from Recurly to Klaviyo profiles:

- Recurly Account Code
- Recurly Card Expiration Date
- Recurly Plan Codes
- Recurly Plans

## Outcome

You’ve finished integrating Recurly with Klaviyo and have verified your synced data. Now, you can personalize and target emails based on invoice and payment data from your customers.

## Additional resources

- [Getting started with flows](https://help.klaviyo.com/hc/en-us/articles/115002774932)
- [Getting started with segments](https://help.klaviyo.com/hc/en-us/articles/115005237908)
- [Types of data exchanged between Klaviyo and apps reference](https://help.klaviyo.com/hc/en-us/articles/360030696012)