---
id: "4403589811611"
title: "How to disable notification emails sent by Shopify"
source_url: "https://help.klaviyo.com/hc/en-us/articles/4403589811611-How-to-disable-notification-emails-sent-by-Shopify"
section: "Getting started with Shopify"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:57Z"
language: "en"
---
## You will learn

Learn how to disable certain marketing or notification emails in Shopify such as abandoned checkout or delivery notifications. You should disable these emails if you are currently sending them via Shopify and want to start sending them via Klaviyo, in order to avoid sending them twice.

Make sure to disable these emails right before you enable the corresponding flow in Klaviyo to avoid a gap in sending.

You must request [transactional status for emails](https://help.klaviyo.com/hc/en-us/articles/360003165732-Guide-to-Using-Flows-to-Send-Transactional-Emails) that do not contain marketing content by [contacting our Customer Success team](https://help.klaviyo.com/hc/en-us/articles/115001002272).

## Before you begin

If you have not already, read our guide about [getting started with Shopify](https://help.klaviyo.com/hc/en-us/articles/115005080407-How-to-Integrate-with-Shopify) for step-by-step instructions on integrating, before continuing with this article.

Please note that some email types can only be configured by Shopify Plus customers.

## Disabling notification emails

To disable notification emails, such as those around delivery:

1. Log in to your Shopify admin.
2. Click ****Settings**** in the lower left.
3. Select ****Notifications****, then click ****Customer notifications****.
4. Here, you'll see a full list of notification emails. If you see a toggle, it means you can toggle off that email.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/29897293278875)
5. Toggle off the email(s) you'd like turned off.
6. If you turned off shipping confirmation emails, you'll also want to make sure line items aren't fulfilled automatically on your store. To check this:
   1. In your Shopify admin, navigate to ****Settings > General****.
   2. Find the **Order processing** section.
   3. Make sure that **Don't fulfill any of the order's line items automatically** is selected. This ensures that a fulfillment event won't sync to Klaviyo (and potentially trigger an email) right when the order is paid.

![](https://klaviyo.zendesk.com/hc/article_attachments/29901361969947)

## Disabling marketing emails

To disable marketing emails, such as abandoned checkout:

1. Log in to your Shopify admin.
2. Select ****Marketing**** in the lefthand navigation, then click ****Automations****.
3. Find the email you want to disable, click the triple dots, and select ****Turn off****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/29897293283867)
4. Click ****Turn off**** in the modal that appears.
5. The status of the email will now show **Inactive**.

![](https://klaviyo.zendesk.com/hc/article_attachments/29897293290523)

## Outcome

You have now disabled the emails you've selected in Shopify.