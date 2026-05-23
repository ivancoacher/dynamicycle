---
id: 4403350880411
title: "How to manually enable OAuth for Magento 2 v2.2.0 and older"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/4403350880411-How-to-manually-enable-OAuth-for-Magento-2-v2-2-0-and-older"
section: "Magento 2"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:57Z"
language: en
---

## Overview

Magento 2 version 2.2.0 requires an older version of the Klaviyo extension that does not allow for OAuth setup within the extension settings. For customers currently using v2.2.0 (versions older than 2.2.0 are not supported), we recommend you add OAuth to your integration manually. We also recommend updating to the latest version of Magento 2 to take advantage of all new and upcoming Klaviyo integration features. This guide covers how to set up OAuth after you have already installed the extension and configured webhooks. If you need to install the Klaviyo extension for Magento 2, please check out [our instructions for installation](https://klaviyo.zendesk.com/hc/en-us/articles/115005254348).

## Set up OAuth

First, make sure you are logged in to your Magento 2 account. Here, we’ll enable OAuth to securely connect your Klaviyo account to the Magento 2 extension you've just installed.

Navigate to ****Systems**** from the left hand navigation pane and select ****Integrations****. Click ****Add New Integration**** in the top right corner to manually set up your integration with OAuth authentication. Give your new integration a name in the **Name** field and enter your secure password in the **Your Password** field.

![manualoauth.png](https://klaviyo.zendesk.com/hc/article_attachments/28723544125339)

Fill in the **Callback URL** field with the following URL and update the <**Company ID>** to your Klaviyo public API key. Be sure to delete any extra spaces in the URL that may be automatically added.

```
https://www.klaviyo.com/integration-oauth-one/magento-two/auth/confirm?c=<Company ID>
```

Then, update the **Identity Link URL** using the following URL:

```
https://www.klaviyo.com/integration-oauth-one/magento-two/auth/handle
```

Select the ****API**** tab on the left and navigate to ****Resource Access**** drop down menu. We recommend that you select ****All**** to grant all API access rules needed by Klaviyo.

If you wish to allow only specific selections, ensure the following are checked.

- "Catalog > Inventory > Categories"
- "Carts > Manage Carts"
- "Customers > Customer Groups"
- "Customers > All Customers"
- "Sales > Operations > Orders > Actions > View"
- "Stores > Attributes > Product"
- "Catalog > Inventory > Products"
- "Sales > Operations > Shipments"
- "Stores > Settings > All Stores"
- "Marketing > Communications > Newsletter Subscribers"

When you have finished making your selections, click ****Save.****

Then locate the integration with the name you used above and click ****Activate****.

![activateoauth.png](https://klaviyo.zendesk.com/hc/article_attachments/28723522207899)

Activating the integration will open up a window requesting you to approve access. Click ****Allow**** to be redirected to Klaviyo to complete the integration setup.

![oauthperms.png](https://klaviyo.zendesk.com/hc/article_attachments/28723522209691)

Sign in if you have not already done so, or confirm your account name and ID are correct and click ****Integrate Magento 2.**** This will add the Magento 2 integration to your Klaviyo account associated with the API key you used for setup. If you are logged into multiple Klaviyo accounts and the correct account is not displaying, log out of any other sessions.

![m2authorize.png](https://klaviyo.zendesk.com/hc/article_attachments/28723544135451)

If the window closes automatically, the connection was successful.

If you receive the following error instead, ensure that the API keys used in the first step correspond to the account you are currently logged in to.

![apierror.png](https://klaviyo.zendesk.com/hc/article_attachments/28723522214811)

When establishing the connection between Magento and Klaviyo, if you receive a list of errors instead, you can click each error to learn more about the cause.

![oauthgenerror.png](https://klaviyo.zendesk.com/hc/article_attachments/28723522217627)

## Next steps

Now that you have enabled OAuth, proceed to [enabling the Magento 2 integration in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115005254348#enable-the-magento-2-integration-in-klaviyo8).