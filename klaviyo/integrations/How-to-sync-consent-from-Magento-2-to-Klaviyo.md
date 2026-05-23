---
id: 5510558435739
title: "How to sync consent from Magento 2 to Klaviyo"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/5510558435739-How-to-sync-consent-from-Magento-2-to-Klaviyo"
section: "Magento 2"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:55:04Z"
language: en
---

## Overview

When you integrate your Magento 2 store with Klaviyo, there are a number of options to sync consent captured in Magento to Klaviyo.

It is important to configure your consent syncing options during integration as they do not work retrospectively.

An overview of each sync option is presented in the table below

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Setting | Signup Location | Speed | Double Opt In | Historical Data | $source value | Added to list events |
| Klaviyo Integration Checkbox | Account registration and Magento newsletter forms | Subscribes as part of periodic sync (every 30 minutes) | Will not be triggered even if enabled | Will sync historical customers if enabled before historical sync starts | None | Not triggered |
| Klaviyo Magento Extension Newsletter Setting | Magento newsletter forms | Real time | Can trigger if enabled (customisable) | Not synced | API | Triggered |
| Klaviyo Magento Extension Checkout Setting | Checkbox at checkout | Real time | Will trigger if enabled | Not synced | Magento | Triggered |

## Capture Consent for Account Registration Users

If you give your customers the option to register for an account and sign up for your newsletter at the same time, their consent status can be synced to Klaviyo.

You will need to enable the “Subscribe new customers to a Klaviyo list” setting within your Klaviyo account ****(****not the Magento Extension). This is located at Integrations -> Magento 2

Customers will not receive a double opt-in email, even if you have double opt-in configured for the list you select.

Selecting this setting will sync any new customers to Klaviyo as part of your periodic sync (roughly every 30 minutes), including all customers on your newsletter table. If you specify a different Klaviyo list for your Newsletter Form sync (see [Capture Consent via a Magento Newsletter Form](https://docs.google.com/document/d/1rlWkN0Y03eINGtJiM3W-hfqWipVsDQjMxYnTDe7_zC8/edit#heading=h.99a19ljrnvpv)), then you will see those customers being synced to both lists.

Make sure to check this setting while setting up your integration in order for Klaviyo to  sync all of your historic newsletter subscribers to the specified Klaviyo list.

## Capture Consent via a Magento Newsletter Form

If you are capturing consent via a native Magento newsletter form, then you will need to enable a setting on Klaviyo’s Magento extension to sync that subscription to Klaviyo.

This information syncs to Klaviyo in real time.

You have the option to honor or override the lists' double opt-in settings when using this feature.

****Note:**** **This setting will only apply to customers subscribed after the setting was enabled. It will not sync the consent of previously subscribed customers**

## Capture Consent at Checkout

You can capture consent at checkout using the Klaviyo extension. When this option is enabled, a checkbox will be added at checkout, and the customer will be subscribed in real time to the selected list after completing their purchase.

You can adjust the location of this checkbox on the page by adjusting the “Sort Order”. The higher the number, the further down the checkout page it will be.

If you have double opt-in enabled for the list you’ve selected, customers will receive a double opt-in confirmation email.