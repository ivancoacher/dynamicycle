---
id: 115003492771
title: "Guide to supporting multiple Magento stores (for Magento 2.x)"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115003492771-Guide-to-supporting-multiple-Magento-stores-for-Magento-2-x"
section: "Magento 2"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:14Z"
language: en
---

## Overview

If you have a single Magento 2 server that hosts more than one store, you have two options as you get setup with Klaviyo:

1. ****Create Separate Klaviyo Accounts for Each Magento 2 Store****If you're interested in creating separate Klaviyo accounts for each of your Magento 2 stores, click the advanced option on the Magento 2 integration page to retrieve a list of your stores, and select the stores you want to sync to the Klaviyo account you're working with.
2. ****Sync All Store Data to a Single Klaviyo Account****This option requires you to then use Klaviyo's Segment Builder and flow filter capabilities to leverage data for each store separately.

   Since Klaviyo is not currently optimized to support multiple brands in a single account, we recommend using this method only for multiple languages of the same brand (e.g English and French stores) or if you have an online/offline store of the same brand.

## Create Separate Klaviyo Accounts for Each Magento Store

If you're interested in creating separate Klaviyo accounts for each of your Magento 2 stores, you can select the specific Magento 2 stores you want to connect to your account on the Magento 2 integration page.

While [integrating with Magento](https://klaviyo.zendesk.com/hc/en-us/articles/115005254348), if you check the setting ****Only sync specific Magento 2 stores****, Klaviyo will give you the option of which to sync.

![](https://klaviyo.zendesk.com/hc/article_attachments/28711673376155)

Choosing one or more stores here means that Klaviyo will exclusively sync customer and order data from these chosen stores.

If you don't check this setting and a new store gets added in the future, data from that new store will also begin syncing into Klaviyo at this time.

## Sync All Store Data to a Single Klaviyo Account

When you integrate a Magento 2 server that has multiple stores on it to a single Klaviyo account, we will sync all profiles and order data from each store into this one account.

Additionally, we will sync **Magento Store Name** and **Magento Website ID** properties for each profile created to let you know which of your stores that profile comes from. You will then be able to configure our extension on a site-by-site level to pick which list to add subscribers to, and you can filter flows and segments using the Magento 2 store name to separate flows between stores.

However, as noted above, Klaviyo is not currently optimized to support more than one store in a single account. This means it is not possible to fully isolate each store's data within a single Klaviyo account.

## Scope the Klaviyo Magento Extension to a Single Store View

When you install the Klaviyo Magento Extension, you will be able to enable it for a specific configuration scope. If you would like to configure our extension on a site-by-site level, you just need to shift the scope and set the right Klaviyo API Keys for each view. Make sure to set these API keys at the website level as well as the store view level.

The screenshot below shows all the available store scopes. Here, you can also see the API key for the English store's associated Klaviyo account.

![2021-03-22_10-50-19.png](https://klaviyo.zendesk.com/hc/article_attachments/28711661193755)

Meanwhile, the screenshot below uses the same site, only now the French store is selected. The API key for that store's associated Klaviyo account is also added.

![2021-03-22_13-37-59.png](https://klaviyo.zendesk.com/hc/article_attachments/28711661199131)

## Finding Store IDs for your Magento Stores

Each Magento store within your Klaviyo account is assigned a unique **Store ID**. Use this property to keep your flows distinct for each Magento store.

To find your Magento **Store IDs**, navigate to Klaviyo and select the ****Integrations**** tab. Select ****Magento 2**** and scroll down to the **Advanced** settings.

![](https://klaviyo.zendesk.com/hc/article_attachments/28711673378459)

Notice that each store is associated with a distinct Store ID that you can use to filter your flows.

## Flows for Multiple Magento 2 Stores

You may want to set up different messaging for multiple Magento stores. For example, if you support multiple languages in your Magento stores, you may want to create a post purchase flow and with different flow branches for your French-speaking stores and for your English speaking stores. You can accomplish this by creating a conditional split based on the **MagentoStore** profile property.

This is an example of a post purchase flow with a conditional split based on the **MagentoStore** profile property. This flow splits to create a flow branch for a Magento 2 "French" store:

![](https://klaviyo.zendesk.com/hc/article_attachments/29859702292251)

Another branch can be created based on the **MagentoStore** value equaling **English-UnitedStates**.

## Sign-up Forms for Multiple Magento Stores

You'll want to customize your sign-up forms for each of your Magento stores.

- You can design a distinct form for each of your Magento stores
- You can use one sign-up form and [show or hide blocks based on dynamic variables](https://klaviyo.zendesk.com/hc/en-us/articles/115005258208)

In addition to custom styling, you can choose to surface a form only to specific URLs:

Within ****Sign-up Forms****, navigate to the ****Targeting &**** ****Behaviors**** tab.

Under **Targeting**, check the  **URL** option and enter the specific URL you wish to target.

![mceclip0.png](https://klaviyo.zendesk.com/hc/article_attachments/28711673372955)

You may also want to consider [including a hidden field](https://klaviyo.zendesk.com/hc/en-us/articles/360040841811) in your sign-up form which passes a custom language property. This will ensure that each subscriber is associated with a hidden language property that you can later use to segment your customers.

## Support for Multiple Languages within your Klaviyo Account

You may have multiple Magento stores in different languages. You can customize your email templates and target your customers based on their location and/or language preferences.

For more information on supporting multiple languages within your Klaviyo account, head over to [Klaviyo's Support for Multiple Languages](https://klaviyo.zendesk.com/hc/en-us/articles/115005239028)