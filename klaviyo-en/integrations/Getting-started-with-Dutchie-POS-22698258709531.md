---
id: "22698258709531"
title: "Getting started with Dutchie POS"
source_url: "https://help.klaviyo.com/hc/en-us/articles/22698258709531-Getting-started-with-Dutchie-POS"
section: "Dutchie POS"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:34Z"
language: "en"
---
## You will learn

Learn how to integrate Klaviyo with Dutchie Point of Sale (POS) in order to sync customer profiles and order data to Klaviyo. With this data, you’ll be able to reach customers with targeted messaging through segmentation, campaigns, and flows.

Integrating with Dutchie POS will sync customer profiles and order data to your Klaviyo account going forward.

Note that Klaviyo’s integration does not currently sync any web data from Dutchie Ecommerce to Klaviyo (such as **Started Checkout**, **Order Submitted**, etc.). Only Dutchie POS events (that is, **Placed Order** and **Ordered****Product**) can be synced. Without web events like **Started Checkout,** you will not be able to use Klaviyo flows like **Abandoned Cart**.

## Before you begin

- You are responsible for ensuring compliance with any cannabis-related laws in the territories you are operating in and the territories where the customers you are marketing to are located.
- In Dutchie, product images can flow from POS to Ecommerce, but they do not flow from Ecommerce to POS. To ensure that Klaviyo can sync product images, make sure you are updating images via Dutchie POS.
- In a typical Dutchie set up, each state-level retailer (parent) has multiple individual locations (children). Child locations are separate instances in Dutchie, each with their own API keys. When Klaviyo integrates on your behalf, we can connect the child locations you specify (from a single parent) to one Klaviyo account.
- Profile and transactional data is unified at the parent level, but we specify locationName within synced order data.

## How to integrate with Dutchie POS

Dutchie is not currently listed on the Klaviyo app marketplace. You must reach out to Dutchie support for your API key, then reach out to Klaviyo, and we will integrate on your behalf. You'll also need to allow the Klaviyo team access to your account.

1. First, you’ll need your API key from Dutchie. API keys are provisioned through their Support team directly. Have your account admin contact [possupport@dutchie.com](mailto:possupport@dutchie.com) to get your API key. You can use the following template when making this request to Dutchie:

   - **Dutchie team,**
     **[Customer Account Name] will be integrating with Klaviyo - please provide the Dutchie API key(s) for the following locations:**
     **Location Name 1, Location Name 2, etc.**
2. Then, send an email to [wellness@klaviyo.com](mailto:wellness@klaviyo.com) with the subject **Dutchie Integration setup** and include:

   - A secure link that contains your Dutchie API key(s) obtained in step 1. You can use a site like [onetimesecret.com](https://onetimesecret.com) to generate a secure link. Make sure to include the passphrase in the email if you choose one.
   - Your [Klaviyo public API key](https://www.klaviyo.com/settings/account/api-keys) for the Klaviyo account you want to integrate with.
3. Log in to Klaviyo and navigate to the [account security page](https://www.klaviyo.com/settings/account/security). Under **Klaviyo Remote Access**, select a date at least one week in the future, then click ****Save****. This will allow the Klaviyo team to complete your Dutchie setup.

## Data synced from Dutchie POS to Klaviyo

To check on the data sync from Dutchie POS to Klaviyo:

1. In your Klaviyo account, select ****Analytics > Metrics****.
2. At the top, filter by **Dutchie**.

Here, you’ll see a list of order events synced from Dutchie POS to Klaviyo:

![](https://klaviyo.zendesk.com/hc/article_attachments/28705638982683)

The data synced from Dutchie to Klaviyo includes:

- Profile information associated with order events.
- The following order events:
  - **Placed Order**
  - **Ordered Product**

Klaviyo will only sync profiles that have an email address. We recommend turning on the setting **Require email address for guest checkout** in Dutchie Ecommerce, which can be found under ****Settings > Options > Checkout****. The email address will sync to Dutchie POS.

For more information on the properties associated with events synced from Dutchie, check out our article [Dutchie POS data reference](https://help.klaviyo.com/hc/en-us/articles/22698234676507).

## Add onsite tracking (optional)

You can choose to manually add Klaviyo’s onsite JavaScript, known as Klaviyo.js, to your Dutchie site via Google Tag Manager. Klaviyo.js enables **Active on Site** tracking and the use of Klaviyo sign-up forms. Google Tag Manager is supported by both Dutchie and Klaviyo.

Read about [how to add Klaviyo onsite tracking using Google Tag Manager](https://help.klaviyo.com/hc/en-us/articles/360015392131).

## Dutchie and email sending

Customers who consent to email marketing during a Dutchie Ecommerce checkout are not synced to Dutchie POS. Currently, Klaviyo only syncs data from Dutchie POS, and thus, no profiles synced from Dutchie POS to Klaviyo will have explicitly consented to your email marketing.

For instance, the following scenario could occur:

1. Your customer places a delivery order online and provides their email at checkout. They choose to subscribe to email via a checkbox.
2. The email provided in the online checkout is attached to the order.
3. The order is delivered, and the customer checks out using the POS.
4. The placed order information, along with the attached email address, syncs to Klaviyo, but email subscription information from the online checkout does not sync to Klaviyo.

Klaviyo will mark synced profiles from Dutchie as **Never Subscribed** in Klaviyo. Profiles marked as **Never Subscribed** can technically receive emails, though they have not provided explicit consent. To learn more about marketing consent and its best practices, read our guide about [explicit versus implicit consent](https://help.klaviyo.com/hc/en-us/articles/4404203889947).

Note that for catalog items, Klaviyo cannot capture the Product URL from Dutchie. It is recommended to [style the product as unlinked](https://help.klaviyo.com/hc/en-us/articles/115000219092#h_01HA9YF09BS80CBMQC520PW9KR) in your emails. You can choose to manually add product links, or links to anywhere on your site, to your emails.

## Dutchie and SMS sending

Klaviyo does not allow SMS sending for Dutchie merchants. This is because mobile carriers prohibit SMS and MMS sending about [certain substances](https://help.klaviyo.com/hc/en-us/articles/4401822831771#h_01H1VHNYQEWZBEB38FKFHT4DEK), which include marijuana/cannabis.

## Dutchie use cases

Here are some example use cases for email sending using Dutchie data:

- ****Product recommendations****
  Use a [Klaviyo product feed](https://help.klaviyo.com/hc/en-us/articles/115005082787) to send customers recommendations based on their previous orders.
- ****VIP customer messaging****
  [Create a VIP segment](https://help.klaviyo.com/hc/en-us/articles/115005065707) in order to target your most valuable customers.
- ****Product education****
  Educate your customers about the products you offer through a newsletter or targeted sends.
- ****Sales and promotion notifications****
  Let your customers know when a sale is happening, and target customers’ preferred product categories using segmentation.
- ****Loyalty program communications and offers****
  Further engage your VIP customers by [building a VIP loyalty program with Klaviyo](https://academy.klaviyo.com/create-a-vip-loyalty-program).

## Outcome

You’ve integrated Dutchie with Klaviyo and verified your synced data. Now, you can create automated flow messages, personalize campaigns, segment your lists, and more based on data synced from Dutchie POS.

## Why am I seeing the notification “Your account is calling a retired revision”?

Are you seeing a notification in Klaviyo that reads “[ACTION Required] Your account is calling a retired revision”, like the one below?

![](https://klaviyo.zendesk.com/hc/article_attachments/31085307999771)

Please ignore this notification; no action is currently needed on your part. Your Dutchie POS integration is managed by Klaviyo and will continue to work as expected.