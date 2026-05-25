---
id: "20920631501979"
title: "Getting started with data capture in Klaviyo"
source_url: "https://help.klaviyo.com/hc/en-us/articles/20920631501979-Getting-started-with-data-capture-in-Klaviyo"
section: "All integrations"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:33Z"
language: "en"
---
## You will learn

Learn about the various data capture methods in Klaviyo that you can use to collect data. Klaviyo allows you to unify data captured from multiple sources across your marketing stack and create a single customer view from millions of data points to personalize your marketing.

## Types of data in Klaviyo

There are three main types of data in Klaviyo:

1. ****Event data****
   Events populate along a customer's timeline each time they take a certain action. Each event, such as **Active on Site**, **Placed Order**, or **Fulfilled Order,** is known as a metric. There can be multiple instances of metric data for one contact, as long as they take the corresponding action more than once. For instance, when a customer places several orders on your website, they will have several **Placed Order** metrics listed on their timeline.
2. ****Profile data****
   Profile data describes an aspect of a contact's identity, and is made up of both Klaviyo properties and custom properties. Klaviyo properties are natively tracked and include attributes such as **First Active**, **Last Active**, **Source**, **First Name**, and **Last Name**. Custom properties are additional profile data which you can create and are often specific to your business. Common custom properties include gender, birthday, or product preference. You can also pull in custom properties through third-party integrations, which allow you to import reviews, ratings, and other information not natively tracked in Klaviyo.
3. ****Catalog data****
   Catalog data describes items found within your product catalog. This data is frequently modified on your ecommerce platform as you add or remove products from your store. Examples of catalog data include variants such as color and size. Within Klaviyo, catalog data pulls in and populates product feeds, campaigns, and flow messages.

For more information, see our guide to [understanding the types of information exchanged between Klaviyo and apps](https://help.klaviyo.com/hc/en-us/articles/360030696012).

## Data capture methods

### Sign-up forms

A [sign-up form](https://help.klaviyo.com/hc/en-us/articles/360026474752) is a tool to collect information from your website visitors and grow your subscriber lists. This can include contact information (e.g., an email address and phone number) or other personal information and preferences (e.g., names, birthdays, or the products a customer is interested in). Information collected with sign-up forms can be used to segment your customer base and personalize your marketing.

### Consent pages

[Consent pages](https://help.klaviyo.com/hc/en-us/articles/115005251848) serve as landing pages where you can collect information and marketing consent from your website visitors. Similar to sign-up forms, these pages can collect personal information and customer preferences that can be used to personalize your marketing.

### Integrations and apps

Klaviyo’s large app marketplace allows you to capture data across your entire marketing ecosystem and gain a unified customer view.

Klaviyo integrates with many common ecommerce platforms and pulls in order data from your store, like **Placed Order**, **Checkout Started**, and other events. Klaviyo also has many integrations with other tools (e.g., platforms you may use for payments, cart and order management, support tickets, subscriptions, shipping, surveys, referrals, and more) so you can capture data from a variety of channels.

[Klaviyo's APIs](https://developers.klaviyo.com/en/reference/api_overview) also enable a large variety of [third-parties](https://help.klaviyo.com/hc/en-us/articles/360049626051) to build their own integrations with the platform. Similarly, if you have a tool in your marketing stack that does not have an existing integration with Klaviyo, you can [develop your own](https://developers.klaviyo.com/en/docs/build_your_integration).

For a full list of available integrations, see Klaviyo’s [app marketplace](https://marketplace.klaviyo.com/en-us/).

### Cookies

Klaviyo uses [cookies](https://help.klaviyo.com/hc/en-us/articles/360034666712) as a part of its identity capture functionality to automatically identify users that click through your emails or submit a Klaviyo form. Since Klaviyo only uses first-party cookies, web tracking only applies to your customers that have opted-in and received marketing from you. Klaviyo’s cookies also enable [onsite tracking](https://help.klaviyo.com/hc/en-us/articles/115005076767), allowing you to collect helpful information around browsing activity. You can then leverage this information to further personalize your marketing and understand your customer’s shopping behaviors.

### Anonymous visitor activity backfill

With Klaviyo’s [anonymous visitor activity backfill](https://help.klaviyo.com/hc/en-us/articles/17928628922395), you can capture onsite activity for a shopper prior to identification. Once that visitor is identified in the future, you’ll then have access to their historical onsite events. This allows you to have a more complete view of your customers’ journeys, regardless of when they are identified through Klaviyo’s web tracking.

To collect onsite data for anonymous visitors, Klaviyo records data about a visitors actions as they occur and stores that locally in their browser. In the future when that visitor is identified, that data is then sent to Klaviyo and cleared from the browser. Any future onsite activity will be tracked as usual through the Klaviyo cookie once they have been identified as well.

### Data feeds

Catalog data can be sent to Klaviyo using a data feed. [Product feeds](https://help.klaviyo.com/hc/en-us/articles/115005082787) in Klaviyo take in data from your store's product catalog and customer behavior (e.g., the products they’ve viewed or purchased in the past). You can also set up your own [custom web feeds](https://help.klaviyo.com/hc/en-us/articles/115005258768) to populate data dynamically from an external URL within a Klaviyo email.

These options are great for data that is frequently updated, like a product catalog or blog post, and allow you to automatically include the latest content from different parts of your marketing stack in your communications with customers.

### APIs

Klaviyo has a number of [APIs](https://developers.klaviyo.com/en/reference/api_overview) that you can use to send data programmatically from your store and other parts of your ecommerce ecosystem. Klaviyo’s REST API allows you to send and request data regarding your:

- Metrics
- Profiles
- Lists and segments
- Data privacy
- Campaigns
- Templates
- Catalogs

Meanwhile, the [Events API](https://developers.klaviyo.com/en/reference/events_api_overview) is used for tracking people and the events they trigger or actions they perform.

### Manual uploads

Klaviyo also allows you to manually upload data to the platform. There are two main types of data you can manually import in Klaviyo:

1. ****Historic event data****If your integration with Klaviyo doesn’t sync historical event data automatically, you can [manually upload data](https://help.klaviyo.com/hc/en-us/articles/115005081247) with a CSV file.
2. ****Profile and subscription data****
   You can import profile data to Klaviyo through a CSV upload. This includes profile properties you can use to store information about profiles, and data regarding your contacts’ consent statuses for various channels.

### SFTP

Klaviyo can ingest data from external systems into Klaviyo through [SFTP](https://developers.klaviyo.com/en/docs/use_klaviyos_sftp_import_tool) (Secure File Transfer Protocol), allowing you to transfer files securely. This feature is ideal for customers who want to bulk import CSV data using an SFTP client of their choice. At this time, Klaviyo supports the following functionality through SFTP:

- Profile creating and updating
- Event creation

## Additional resources

- [Understanding integrations](https://help.klaviyo.com/hc/en-us/articles/115000256472)
- [Understanding data types](https://help.klaviyo.com/hc/en-us/articles/115005237648)
- [Frequently asked questions about integrations](https://help.klaviyo.com/hc/en-us/articles/115005081007)