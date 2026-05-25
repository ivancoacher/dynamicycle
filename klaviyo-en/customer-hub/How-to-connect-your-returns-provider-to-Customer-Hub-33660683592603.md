---
id: "33660683592603"
title: "How to connect your returns provider to Customer Hub"
source_url: "https://help.klaviyo.com/hc/en-us/articles/33660683592603-How-to-connect-your-returns-provider-to-Customer-Hub"
section: "Integrate other platforms with Customer Hub"
category: "Customer Hub"
category_slug: "customer-hub"
klaviyo_updated: "2026-04-21T13:56:49Z"
language: "en"
---
## You will learn

Learn how to connect your third-party returns management platform to Customer Hub. This setup allows customers to start returns right from the Customer Hub interface on your site, streamlining the returns experience and reducing strain on your support team.

Customer Hub for Shopify currently supports standard storefronts and Shopify Headless. For WooCommerce, navigate to https://help.klaviyo.com/hc/en-us/articles/47792369863451

For feedback about Customer Hub functionality, email customerhub@klaviyo.com.

## Before you begin

Before proceeding, ensure that the Customer Hub feature is enabled in your Klaviyo account. [Learn more about Customer Hub](https://klaviyo.zendesk.com/hc/en-us/articles/33660324811675).

## Supported returns platforms

The following returns providers are currently supported:

- Loop
- Aftership
- Parcel Lab
- Narvar

If you do not use one of these portals, you can either choose ****Other**** and provide a URL to your returns portal, or keep this setting disabled. Klaviyo will expand this feature to other platforms in the future.

## How returns work in Customer Hub

When a signed-in customer views the **Orders** tab in the Customer Hub drawer, they see their order history. Clicking on an order shows its details, status, and help options for repurchasing the item, shipment tracking, and accessing various support channels.

![CHreturns4.jpg](https://klaviyo.zendesk.com/hc/article_attachments/34196954781851)

Once an order has been delivered, a “Start a Return” button appears within the order details. The customer’s experience when they click this button depends on which returns provider you connect:

- ****Loop****:
  - Customers are sent directly to a personalized return workflow in Loop via Loop’s deep link API. Their order details are passed securely, so no manual entry is required.
- ****Aftership, Parcel Lab, Narvar****:
  - Klaviyo redirects to your platform’s portal and attaches the order number and customer’s email in the URL. If supported in the platform, this information is pre-filled to help the customer’s return get started.
- ****Other****:
  - Customers are sent to your custom portal link and must enter their order details manually, as no information is passed from Klaviyo.

Note that connecting your returns platform to Customer Hub won’t automatically sync data between the two platforms. Instead, providing a link to your external portal within the Customer Hub allows your customers to click a button and instantly start a return process with the specific order within your return platform.

### Connect your returns provider to Customer Hub

Choose your provider below and follow the appropriate steps. If you don’t see your provider’s name, follow the instructions for “Other.”

Note that if your Customer Hub is live, saving publishes this change live on your site. If it’s not, you’ll see this change once you set live in the **General** settings menu.

### Connect Loop Returns

1. In Loop, copy your API key from the [**Developer tools** page](https://help.loopreturns.com/en/articles/1911681#finding_api_keys).
2. In Klaviyo, navigate to ****Customer Hub****.
3. Select ****Extensions****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/40774432810139)
4. Under **Returns**, toggle the setting on.
5. Select ****Loop**** as your returns provider and paste your API key.
   - While creating an API key in Loop, ensure that it has ****Order**** and ****Return**** access.
   - Double-check your API key, as Klaviyo will not verify it. If it’s incorrect, customers will see an error when starting a return.
     ![CHing3.jpg](https://klaviyo.zendesk.com/hc/article_attachments/39787595557659)
6. Click ****Save****.

When customers click “Start a Return,” they are sent directly into the personalized return workflow in Loop.

### Connect Aftership, Parcel Lab, Narvar, or another provider

1. In Klaviyo’s left-hand navigation, select ****Customer Hub****.
2. Select ****Integrations****.
   ![CHsub2.jpg](https://klaviyo.zendesk.com/hc/article_attachments/39787606446875)
3. Under **Returns**, toggle the setting on, then select your provider (Aftership, Parcel Lab, Narvar, or Other).
4. Paste your returns portal URL.
   ![CHint4.jpg](https://klaviyo.zendesk.com/hc/article_attachments/39787606455835)
5. Click ****Save****.

When customers click "Start a Return," they’ll be redirected to your portal. If supported, order number and email are pre-filled to simplify the process.

For “Other,” customers must enter their order details manually.

## Disable your returns platform

To prevent the “Start a return” button from appearing on fulfilled orders in Customer Hub, disconnect your returns platform:

1. In Klaviyo’s left-hand navigation, select ****Customer Hub****.
2. Select ****Extensions****.
3. In the **Returns** menu, toggle the setting off.
4. Click ****Save****.

Saving this change will remove the “Start a Return” button from order details view within Customer Hub.

## Additional resources

- [Getting started with Customer Hub](https://klaviyo.zendesk.com/hc/en-us/articles/33660324811675)
- [How to configure help settings for Customer Hub](https://klaviyo.zendesk.com/hc/en-us/articles/33660636674843)
- [How to create content blocks in Customer Hub](https://klaviyo.zendesk.com/hc/en-us/articles/33660517680795)