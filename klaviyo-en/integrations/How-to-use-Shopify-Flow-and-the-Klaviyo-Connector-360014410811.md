---
id: "360014410811"
title: "How to use Shopify Flow and the Klaviyo Connector"
source_url: "https://help.klaviyo.com/hc/en-us/articles/360014410811-How-to-use-Shopify-Flow-and-the-Klaviyo-Connector"
section: "Shopify best practices"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:43Z"
language: "en"
---
Learn how to use the Klaviyo Connector with Shopify Flow to track events (to send data from your workflow to Klaviyo).

## Before you begin

If you have not already, read our guide on [getting started with Shopify](https://help.klaviyo.com/hc/en-us/articles/115005080407-How-to-Integrate-with-Shopify) for step-by-step instructions on integrating, before continuing with this article.

## What is Shopify Flow?

Shopify Flow is an ecommerce automation platform that Shopify stores can use to automate common tasks, such as:

- Tagging high-value customers
- Flagging and cancelling high-risk orders
- Sending reordering requests when your inventory levels become low
- Identifying and adding tags to products based on their title or SKU

Shopify Flow is an app offered by Shopify in their App Store and is available for those on the Shopify plan and up (it is not available for those on the Basic plan). You can access the app [in Shopify's app store](https://apps.shopify.com/flow) and should install it before following the steps in this article.

For Shopify merchants using Flow, there are a number of resources available for understanding what's possible with Flow, and workflows you can download and import into your store:

1. [Workflow examples from Shopify Help Center doc](https://help.shopify.com/en/manual/shopify-plus/flow2/reference/examples)
2. [14 top workflows blog post](https://www.shopify.com/enterprise/ecommerce-automation-software-shopify-flow)

## What can I do with Klaviyo Connector for Shopify Flow?

Shopify Connectors is a feature that allows Shopify stores to create app triggers and actions that third-party partners have built.

The Klaviyo Connector supports the Track an event action:

- This action sends data from your workflow to Klaviyo for it to track.
  - ****Example workflow****When a customer's loyalty tier changes, you can track this change in Klaviyo.
  - ****How it works****
    1. This workflow is triggered by LoyaltyLion when a customer moves up a loyalty tier. LoyaltyLion send the tier information to Shopify Flow.
    2. Shopify Flow sends data about the customer to Klaviyo, to track the event, and to LoyaltyLion, to add bonus points the customer's loyalty account.

## How to use the Klaviyo Connector

In a Shopify Flow, you can add actions into a workflow.

1. When in the ****Select an action**** menu, you can choose from **Standard Actions** developed by Shopify or additional actions developed by third-party apps. This is where you'll find the Klaviyo Connector if it's installed.
2. The action available in the Klaviyo Connector is ****Track an event********.********![Screenshot 2025-10-16 at 9.17.20 AM.png](https://klaviyo.zendesk.com/hc/article_attachments/42182674738075)****

### Track an event

Once you choose the ****Track an Event**** action, you'll need to fill out the following fields:

- ****Klaviyo Public API Key****Learn how to [locate your public API key in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115005062267-How-to-manage-your-account-s-API-keys#find-your-api-keys2).
- ****Event Name****Name of the event you want to track. This will appear on the customer profile's event timeline.
- ****Customer Email Address****Email of the person going through the Flow whose activity will be tracked in Klaviyo.
- ****Customer First Name****First name of the person going through the Flow whose activity will be tracked in Klaviyo.
- ****Customer Last Name****Last name of the person going through the Flow whose activity will be tracked in Klaviyo.
- ****Customer Properties****Hash dictionary of customer properties to be included in their Klaviyo profile as a custom field.
  ![Customer properties box with first name and Has Account, and Event properties box with value, item count, and total discount](https://klaviyo.zendesk.com/hc/article_attachments/28717992039707)
- ****Event Properties****Hash dictionary of custom information about this event.

It is important to note that anything sent as a list, such as customer or event properties, will need to be formatted as a JSON list to appear properly in Klaviyo. For example, you could format customer tags in the following way:
`{"tags": [{% for tags_item in customer.tags %}{% if forloop.first != true %},{% endif %}{{ tags_item | json}}{% endfor %}]}`

These events will be tracked in Klaviyo as Shopify events, as indicated by the Shopify icon alongside each event. To view your Shopify Flow event data:

1. Click the ****Analytics**** dropdown in Klaviyo and select ****Metrics****
2. Select ****Shopify**** from the dropdown menu. The tab will display only the events synced from Shopify.
   ![Timeline of Shopify metrics in Klaviyo with metrics such as VIP status cancelled and credit card fraud detected](https://klaviyo.zendesk.com/hc/article_attachments/28717992047899)

### Create a campaign

The Create a campaign action has been retired as of October 16th, 2025.

#### How can I replicate the “Create a campaign” functionality?

We recommend updating your workflows to use the "[Track an event](https://help.klaviyo.com/hc/en-us/articles/360014410811#h_01HCFKXSHCSG8M2RN0EESGVTVY)" action. This action allows you to create data from Shopify to Klaviyo, which can then be used to trigger a flow or build a segment for a campaign.

1. In your Shopify Flow, remove the "Create a campaign" action.
2. In its place, add the "Track an event" action to create the relevant customer data to Klaviyo.
3. In Klaviyo, you can then use this new event as a trigger for a flow or create a segment based on it to create a campaign to the right audience.

## Troubleshooting

### Is your data not showing in Klaviyo as expected?

Make sure that the Customer Properties box and the Event Properties box are valid JSON. If the input is not valid JSON, the Track an Event step will not pass data into Klaviyo as expected. For example, your data variables may include for-loop statements. When the for-loop statements are evaluated, they might leave trailing spaces due to the new line that the variables exist on within the for-loop syntax:

```
"{% for lineItems_item in order.lineItems %}
{{lineItems_item.name}}
{% endfor %}"
```

This will not be ingested by Klaviyo due to it being invalid JSON. To resolve, remove the line breaks in between the syntax of the for-loop like this:

```
"{% for lineItems_item in order.lineItems %}{{lineItems_item.name}}{% endfor %}"
```

## Outcome

You've now learned how to use the Klaviyo Connector with Shopify Flow to track events.

## Additional resources

- [Getting started with Shopify](https://klaviyo.zendesk.com/hc/en-us/articles/115005080407)
- Learn more about [Connectors on the Shopify Help Center](https://help.shopify.com/en/manual/shopify-flow/reference/connectors)