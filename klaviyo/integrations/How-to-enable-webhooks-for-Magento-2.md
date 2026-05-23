---
id: 360055336451
title: "How to enable webhooks for Magento 2"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360055336451-How-to-enable-webhooks-for-Magento-2"
section: "Magento 2"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:52Z"
language: en
---

## You will learn

Learn how to enable Klaviyo webhooks, which will empower your Magento 2 integration to sync catalog product removals real-time, and enable consent at checkout.

## Before you begin

If you have not already enabled your Magento 2 integration, you will need to complete the setup steps outlined in the [Magento 2 Integration guide](https://help.klaviyo.com/hc/en-us/articles/115005254348-How-to-Integrate-with-Magento-2-x-CE-and-EE-), which also includes instructions on enabling Klaviyo webhooks.

## Enable webhooks

1. Log in to your Magento 2 account and navigate to ****Stores > Configuration**** from the admin dashboard.
2. Click on ****Klaviyo**** and select the ****Webhooks**** tab.![Image showing the Webhooks tab of the Store Configuration dashboard.](https://klaviyo.zendesk.com/hc/article_attachments/28720658704411)
3. Create a webhook secret and enter it into the corresponding ****Webhook Secret**** field. The webhook secret is a key that Klaviyo will use for validation. This secret can be anything you choose, but we recommend creating a secure string of letters and numbers. Magento will hide your webhook secret with asterisks for security purposes, so be careful to enter it correctly.
   If you are using a multi-store integration, the webhook secret in this field should be entered in your default configuration, and the same secret will be used as validation for each store configuration. The webhook secret should only be added to the default config and should not be added per store.
4. Next to **Use Product Delete Webhook?** select ****Yes**** from the dropdown options. The **Product Delete** webhook allows the integration to remove products that you have deleted in Magento 2 from the catalog in Klaviyo.
5. Click ****Save Config**** to complete the setup. Your Magento 2 integration will now remove deleted products from the catalog in real-time.

## Additional resources

- [How to Integrate with Magento 2.x (CE and EE)](https://klaviyo.zendesk.com/hc/en-us/articles/115005254348)
- [Reviewing Your Magento 2 Data](https://klaviyo.zendesk.com/hc/en-us/articles/115003458852)