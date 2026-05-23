---
id: 1260807540249
title: "How to set up OAuth for existing Magento 2 integrations"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/1260807540249-How-to-set-up-OAuth-for-existing-Magento-2-integrations"
section: "Magento 2"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:27Z"
language: en
---

## Overview

This guide will cover how to update an existing Magento 2 integration from API credential authentication to the new OAuth workflow. Visit the guide here if you need to [enable your Magento 2 integration](https://klaviyo.zendesk.com/hc/en-us/articles/115005254348) for the first time. If you are using Magento 2 version 2.2.0 or older, follow this guide to [manually enable OAuth](https://help.klaviyo.com/hc/en-us/articles/4403350880411).

## Set up OAuth

Log in to your Magento 2 account. Here, we’ll enable OAuth to securely connect your Klaviyo account to the Magento 2 extension.

Navigate to ****Stores > Configuration****from the admin dashboard. Click on ****Klaviyo**** and select the ****Setup OAuth**** tab. Give your integration a memorable name in the **Name** field, you will need to locate it by this name later. Click ****Save Config**** to proceed.

![OAUTHtab.png](https://klaviyo.zendesk.com/hc/article_attachments/28717987581723)

Next, locate ****System**** from the left hand navigation pane and select ****Integrations**** from the System tray.

Locate the integration with the name you used above and click ****Activate****.

![activateoauth.png](https://klaviyo.zendesk.com/hc/article_attachments/28717993386395)

Activating the integration will open up a window requesting you to approve access to several permissions. Click ****Allow**** to accept the permissions and get redirected to Klaviyo to complete the integration setup.

![oauthperms.png](https://klaviyo.zendesk.com/hc/article_attachments/28717993388315)

Sign in if you have not already done so, or confirm your account name is correct and click ****Integrate.**** This will update the Magento 2 integration in the Klaviyo account shown. If you are logged into multiple Klaviyo accounts and the correct account is not displaying, log out of any other sessions.

![](https://klaviyo.zendesk.com/hc/article_attachments/28717993395739)

If the window closes automatically, the connection was successful. You can also confirm by opening your Klaviyo account in a new browser tab or window and selecting the ****Integrations**** tab. Find Magento 2 on the list of integrations - click on it, and you should see a screen like the one below:

![](https://klaviyo.zendesk.com/hc/article_attachments/28717993399195)

If you receive the following error instead, ensure that the API keys used in the first step correspond to the account you are currently logged in to.

![apierror.png](https://klaviyo.zendesk.com/hc/article_attachments/28717993390235)

When establishing the connection between Magento and Klaviyo, if you receive a list of errors instead, you can click each error to learn more about the cause.
![oauthgenerror.png](https://klaviyo.zendesk.com/hc/article_attachments/28717993393563)