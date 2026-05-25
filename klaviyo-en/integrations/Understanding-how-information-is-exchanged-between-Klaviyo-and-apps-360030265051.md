---
id: "360030265051"
title: "Understanding how information is exchanged between Klaviyo and apps"
source_url: "https://help.klaviyo.com/hc/en-us/articles/360030265051-Understanding-how-information-is-exchanged-between-Klaviyo-and-apps"
section: "All integrations"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:44Z"
language: "en"
---
## You will learn

Learn about how information syncs between Klaviyo and your third-party apps via an application programming interface (API). Most data exchanged via a Klaviyo integration is one-way: data is pulled into your Klaviyo account so you can leverage a broad scope of your customer's data.

## How integrations sync information to and from Klaviyo

Klaviyo’s API is a set of interfaces where data is exchanged between Klaviyo and other applications connected to your Klaviyo account. To initially integrate Klaviyo with another application, you’ll need to authenticate via OAuth or use an API key. An API key is a unique identifier tied to your specific account.

Klaviyo generates two types of API keys, both of which [can be found in your account](https://klaviyo.zendesk.com/hc/en-us/articles/115005062267):

- ****Public****
  Your public API key, sometimes referred to as your Site ID, is the unique identifier for your Klaviyo account. This key cannot be used by a third-party app to access private information within your Klaviyo account.
- ****Private****
  Private API keys are used to read data from Klaviyo and manipulate sensitive objects, such as lists. They ensure the process of updating subscriptions and other customer information is secure and private. Private API keys should be treated like your password: kept in a safe place and never exposed to the public. You can generate new private API keys for different applications to trace the source of data being added to your Klaviyo account.

For more specific information regarding types of Klaviyo API Keys, see our [API reference documentation](https://developers.klaviyo.com/en/reference/api_overview#api-key-scopes).

## Klaviyo's REST APIs

REST is an architectural style that provides guidelines for platform-agnostic communication between applications on the internet. The Klaviyo REST APIs primarily communicate using a JavaScript Object Notation (JSON) format, which provides a structured layout for the information contained in the API messages. The following areas of your Klaviyo account can be accessed via the our REST APIs:

- Accounts
- Campaigns
- Catalogs
- Coupons
- Data Privacy
- Events
- Flows
- Images
- Lists
- Metrics
- Profiles
- Reporting
- Segments
- Tags
- Templates

While the APIs above are designed to be called from server-side applications, we also have a Client API for creating events and subscriptions from client-side applications.

## The klaviyo JavaScript object

The [**klaviyo** object](https://developers.klaviyo.com/en/docs/introduction_to_the_klaviyo_object) replaces the legacy \_**learnq** and **klOnsite** objects. These JavaScript objects offer a shorthand way to interact with our APIs and send events into Klaviyo. The klaviyo object allows you to identify known profiles, and track events and actions on your website.

## Additional resources

- [API fundamentals for marketers](https://academy.klaviyo.com/en-us/collections/api-fundamentals-for-marketers)
- [Understanding the types of information exchanged between Klaviyo and apps](https://klaviyo.zendesk.com/hc/en-us/articles/360030696012)
- [Getting started with Klaviyo APIs](https://help.klaviyo.com/hc/en-us/articles/360045726811)
- Need more help integrating with Klaviyo? Check out [Klaviyo's Agency Partners](https://klaviyo.partnerpage.io/)