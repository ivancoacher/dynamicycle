<h1>How to migrate from Salesforce Marketing Cloud</h1>

## You will learn

Learn how to integrate Salesforce Marketing Cloud (previously ExactTarget) with Klaviyo. This integration is designed to help you move from Salesforce Marketing Cloud to Klaviyo. We don't recommend using both platforms at once other than during the interim period as you make the switch.

## Before you begin

Make sure to consult our [general checklist](https://klaviyo.zendesk.com/hc/en-us/articles/115005082767) that covers how to completely migrate over to Klaviyo from a different email service provider (ESP).

The Salesforce Marketing Cloud user you use when integrating should have access to webservices. Learn how to [find the WSDL link.](https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/wsdl-endpoint-links.html)

## Add the Salesforce Marketing Cloud integration

1. In Klaviyo, select the ****Integrations**** tab.
2. On the next page, select ****Explore apps**** and search for **Salesforce Marketing Cloud**. Then, click on the card.
3. Click ****Install****.
4. On the next page, provide the username and password you use to log into Salesforce Marketing Cloud, along with the WSDL link to connect to the SOAP API for your Salesforce Marketing Cloud instance.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28716328059163)
5. Click ****Connect to Salesforce Marketing Cloud****.
6. On the next page, under **Advanced**, you will have the option to 1) Collect open and click data from your campaigns (highly recommended) and 2) Only sync specific lists, which will allow you to pick the specific lists you want to sync from Salesforce Marketing Cloud.
   - If you select both checkboxes, Klaviyo will sync all campaign data regardless of whether the campaign was sent to the specified list. Additionally, Klaviyo will subsequently create profiles for all the people who opened and/or clicked those campaigns, regardless of whether they’re on the specified list.
7. When you're done, click ****Complete setup.**** Your integration should now be enabled.

## Monitor the Klaviyo sync

To check on your enabled integration, click the ****Audience**** dropdown in Klaviyo, then select the ****Lists & Segments**** tab.

Here, you should begin to see your Salesforce Marketing Cloud lists populate in Klaviyo. These lists will be synced with subscribers from your Salesforce Marketing Cloud lists.

Klaviyo receives historical engagement data from Salesforce Marketing Cloud from the last 180 days. New data syncs to Klaviyo every 5 minutes.

The following metrics will be synced with Klaviyo:

- Clicked Email
- Opened Email
- Received Email

If you select the ****Analytics**** dropdown in Klaviyo, then select ****Metrics****, you'll be able to review these metrics.

![Metrics tab in Klaviyo filtered by Salesforce Marketing Cloud with Clicked Email, Opened Email, and Received Email in list](https://klaviyo.zendesk.com/hc/article_attachments/28716328052763)

If a profile has an inactive status in Salesforce Marketing Cloud, that profile will be globally suppressed within Klaviyo. Inactive statuses include Bounced, Held, Unsubscribed, and Deleted.

## Best practices

You can use the above engagement metrics to segment your Salesforce Marketing Cloud lists in Klaviyo. This will protect your deliverability and ensure that you start off on the right foot by sending exclusively to contacts who want to receive your emails.

To start, build an engaged segment of your subscribers:

- Has Opened Email (ExactTarget) at least once in the last 30 days OR
- Has Clicked Email (ExactTarget) at least once in the last 30 days

![Engaged subscribers segment in Klaviyo segment builder using ExactTarget events](https://klaviyo.zendesk.com/hc/article_attachments/28716300671387)

If you're a daily sender, you should send your first week's worth of campaigns to this segment. If you're a bi-weekly sender, you should send your first 2-3 campaigns to this segment. For more information, see our article on [how to create an engaged segment](https://help.klaviyo.com/hc/en-us/articles/115000200072).

## Outcome

You've now integrated Salesforce Marketing Cloud with Klaviyo, verified your synced data, and reviewed best practices.

## Additional resources

- [Getting started with segments](https://help.klaviyo.com/hc/en-us/articles/115005237908)
- [Understanding email deliverability](https://help.klaviyo.com/hc/en-us/articles/115005247008)
