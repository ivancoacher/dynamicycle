---
id: "115005082247"
title: "How to integrate with Chargebee"
source_url: "https://help.klaviyo.com/hc/en-us/articles/115005082247-How-to-integrate-with-Chargebee"
section: "Chargebee"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:20Z"
language: "en"
---
## You will learn

Learn how to integrate Chargebee with Klaviyo in order to personalize and target messaging based on invoice and payment data from your customers. The following data is synced from Chargebee to Klaviyo:

- When an invoice is issued, and the items included in each invoice
- Payment information for when a user fails payment, is refunded, or successfully pays

## Add the Chargebee integration

1. In Klaviyo, select the ****Integrations**** tab.
2. Select ****Explore apps****, search for **Chargebee**, then click the card. Then, click ****Install****.
3. On the next page, enter the subdomain of your Chargebee URL.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28720758388507)
4. Enter your Chargebee API Key.
5. Click ****Connect to Chargebee****.

## Monitor the Klaviyo sync and verify data

To check the data synced from your integration:

1. Click the ****Analytics**** dropdown in Klaviyo and select ****Metrics****.
2. Filter by Chargebee.
3. Look for Chargebee's **Issued Invoice** metric and click on the ****Activity Feed**** icon.
   ![Activity feed in Klaviyo for Chargebee Issued Invoice metric showing example metrics](https://klaviyo.zendesk.com/hc/article_attachments/28720770263707)
4. If your integration has started syncing data, you'll see **Issued Invoice** events added to this activity feed.

Klaviyo imports all of your Chargebee data. To verify this, you can compare the number of successful payments on a particular day with what's in the Chargebee interface and confirm they match.

1. In Klaviyo, navigate to ****Analytics**** ****>**** ****Metrics****.
2. Find and click on the ****Successfully Paid**** metric to be brought to the metric chart page where you can view the last 30 days of data.
3. Mouse over the data points from the previous day or look in the table of data below the chart to see how many payments you had yesterday.
4. Compare that number to the data stored in Chargebee and you should see they match.
   ![Chart in Klaviyo for Chargebee Issued Invoice metric showing the number of invoices over time](https://klaviyo.zendesk.com/hc/article_attachments/28720758383899)

## Data synced from Chargebee

### Chargebee metrics

The following metrics are synced to Klaviyo from Chargebee:

- ****Activated Subscription****
  This metric records when a subscription has been moved from the "Trial" state to an "Active" state.
- ****Cancelled Subscription****
  This metric records when a subscription is cancelled. If the subscription is cancelled due to non-payment or because the card details are not present, the subscription will have the possible reason as 'cancel\_reason'.
- ****Created Subscription****
  This metric records when a subscription is newly-created.
- ****Failed Payment****
  This metric records an event when a payment is marked as failed in Chargebee. With this metric, you can target customers who fail to make payments and let them know they have an overdue balance.
- ****Issued Invoice****
  This metric records an event every time an invoice is issued to your customers through Chargebee. This metric is useful for segmenting customers who have been issued an invoice but either have not paid or had a failed payment. It can also be used to trigger segments to notify customers of an upcoming payment.
- ****Refunded Payment****
  This metric records an event when you refund a payment through Chargebee.
- ****Successfully Paid****
  This metric records an event each time a customer successfully pays an invoice through Chargebee. These events will include data about your customer, their invoice, and the products in their invoice. This is useful for sending automated invoices to customers after they pay, or using email flows to determine when a customer has been active on your website but hasn't made any payments for your products or services. You can send those users emails offering discounts to make a purchase on your website.

### Customer data

In addition to the metrics Klaviyo syncs from Chargebee, if an email address exists in Chargebee and is not in Klaviyo, we will create a new Klaviyo profile for that person. This profile will include the following information:

- ****General Contact Details****First Name, Last Name, Company, Phone Number
- ****Custom Properties****Chargebee Card Status, Payment Type, Payment Status, and Chargebee Subscription Status\*

\*Note that the Chargebee Subscription Status property may not accurately reflect the most recent subscription status.

## Outcome

You've now integrated with Chargebee and reviewed the data that syncs from Chargebee to Klaviyo. You can now use your Chargebee data to personalize and targeting messaging based on invoice and payment data from your customers.

## Additional resources

- [Information exchanged between Klaviyo and apps reference](https://help.klaviyo.com/hc/en-us/articles/360030696012)