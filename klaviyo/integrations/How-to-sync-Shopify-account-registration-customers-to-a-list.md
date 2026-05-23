---
id: 4403349019163
title: "How to sync Shopify account registration customers to a list"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/4403349019163-How-to-sync-Shopify-account-registration-customers-to-a-list"
section: "Shopify best practices"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:57Z"
language: en
---

## You will learn

Learn how to sync subscribers collected via a Shopify account registration form to a Klaviyo list. If you want to use a Klaviyo form instead, read about [getting started with sign-up forms](https://klaviyo.zendesk.com/hc/en-us/articles/360026474752).

To achieve this goal, you will need to add an **Accepts Marketing** checkbox to your registration form.

## Before you begin

If you have not already, read our article [Getting started with Shopify](https://help.klaviyo.com/hc/en-us/articles/115005080407-How-to-Integrate-with-Shopify) for step-by-step instructions on integrating, before continuing with this article.

Make sure that you have chosen a list for email subscribers to be added to in your Shopify integration settings (in Klaviyo, this can be found by selecting the ****Integrations**** tab, then finding Shopify on the list and selecting it). The setting can be found under **Sync settings**, on the **From Shopify** tab. This is the list the account registration customers will be added to, once you add the checkbox to your form.

![](https://klaviyo.zendesk.com/hc/article_attachments/32924412323739)

## Enable "Accepts Marketing" on your Shopify registration form

In order to have customers who register for an account on your Shopify site be added to a list within Klaviyo, you will need to add some additional code to your registration form, which can be found in the registration.liquid file (or similar).

1. Add the following code to your registration form to add an **Accepts Marketing** checkbox:

   ```
    <div id="accepts_marketing_checkbox">
     <input type="checkbox" name="customer[accepts_marketing]" checked="checked" value="true" id="marketing">
     <label for="marketing">Yes! Sign me up to receive emails about all the latest tots.</label>
     </div>
   ```
2. You will need to customize the label text with the label you would like to use on your form.

Customers will have to check this box in order to be added to your list.

Note that if you have double opt-in enabled in Shopify, the customer will first need to confirm their subscription via Shopify's double opt-in email before being added to the list. If you have double opt-in enabled for the specified list in Klaviyo, the customer will need to confirm their subscription via Klaviyo's double opt-in email before they are added to the list.

You can test that this process is working by filling out the registration form, checking **Accepts Marketing**, and then looking to see if your test profile has been added to your selected list.

## Troubleshooting

If you are uncomfortable with editing and adding code, and require developer assistance, we recommend reaching out to a [Klaviyo partner agency](https://klaviyo.partnerpage.io/).

## Outcome

You're now syncing Shopify account registration customers to a Klaviyo list.