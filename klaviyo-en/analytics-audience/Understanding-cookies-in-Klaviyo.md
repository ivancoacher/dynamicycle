---
id: 360034666712
title: "Understanding cookies in Klaviyo"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360034666712-Understanding-cookies-in-Klaviyo"
section: "About cookies in Klaviyo"
category: "Analytics"
category_slug: "analytics-audience"
klaviyo_updated: "2026-04-21T13:54:45Z"
language: en
---

## You will learn

Learn more about how Klaviyo uses cookies as a part of our web tracking to gather information and help improve conversion rates and email performance. This article explains the specific cookie we use and its purposes so that you understand how customers are tracked. This information helps you understand how Klaviyo gathers data, and how this may impact customer privacy and compliance laws.

In order to [maintain GDPR compliance](https://help.klaviyo.com/hc/en-us/articles/360003211651), you should display links to your Privacy Policy, Terms of Service, and cookie policy in all of your emails.

## Klaviyo tracking cookies

When Klaviyo’s JavaScript is enabled, the `__kla_id` cookie can track and identify site visitors through an auto-generated ID. This cookie can temporarily hold personally identifiable information. Once a visitor is identified, the cookie can pass their data into Klaviyo. A visitor can be identified when they:

- Fill out a Klaviyo signup form
- Click a link from a Klaviyo email or SMS message.

SMS click and conversion tracking is dependent on having a link, and this link must use the Klaviyo link shortener. When setting up your SMS messages, it’s important to have the option checked for ****Automatically shorten links**** to ensure you are using the default tracking.

## Cookie identification timing, extended ID, and Shopify-branded onsite tracking

### Default timing

When a visitor is identified (e.g., by filling out a form or clicking an email link), the `__kla_id` cookie is set to last up to 2 years. Learn more below about [extending this temporary cookie to hold PII longer](https://help.klaviyo.com/hc/en-us/articles/32053410094619).

On Safari desktop and iOS mobile web browsers, Apple's Intelligent Tracking Prevention (ITP) may cap cookie expiration to 7 days, rather than lasting the full 2 years. Campaign email/SMS links use the `_kx` parameter, which is stored
in session storage and is not subject to ITP cookie limits.

### Extended ID

If you choose to turn on extended ID, it is strongly suggested that you re-issue your cookie notices to your customers and inform them that Klaviyo will use a first-party cookie to re-issue the Klaviyo cookie. This will allow Klaviyo and your business to re-identify users after their browser cookie expires. Furthermore, it is recommended that you update your privacy notice to ensure that your customers are notified of this re-identification process.

With certain desktop browsers (e.g. Safari) and mobile operating systems (iOS), Apple's ITP may cap tracking cookies to 7 days.. If your Klaviyo cookie expires quickly (e.g., after 24 hours), you may miss out on valuable tracking events such as when a user is on your site or views a product. Shoppers may also not receive automated flows or campaigns that would trigger on these browsing revisits.

If you want to track a user’s future visits after the Klaviyo cookie has expired or been deleted, you can turn on the extended ID option. Extended ID is a first-party identity graph feature that allows you to track and hold this cookie up to 1 year.

Extended ID is available on all Klaviyo plans.

### How does extended ID work?

Extended ID works by reading common deterministic identifiers (i.e., exact unique identifiers) stored in a user's browser. These long-lasting, first-party unique identifiers (i.e. cookies) are created by other platforms for use cases such as analytics.

When a user returns to the website and a new Klaviyo cookie is issued, extended ID reads the first-party identifier information in the browser and restores the previous Klaviyo identity cookie so that the user is re-identified. If there is no match and the user cannot be identified, Klaviyo stores the association between the first-party unique identifier and the unique Klaviyo identifier in their cookie for future potential re-identification. For other platforms or solutions, you will need to set up custom identifiers.

Extended ID is a more persistent form of user tracking that may not be covered by a user consent obtained for ordinary third-party cookie tracking. It may require you to explain to your customers that extended ID makes use of first-party cookie identifiers and may re-identify them even where previous Klaviyo cookies have been cleared. You may also need to seek specific user consent from each customer visit before extended ID is used. You also may wish to review your privacy policy and consent wording to ensure that your customers are properly informed, and have consented to this re-identification process.

It’s important to note that while extended ID can help identify shoppers longer, it doesn’t automatically create new profiles based on shopper info from other sites. A shopper needs to already have a Klaviyo profile for extended ID to re-identify them and update their Klaviyo identity cookie.

Learn how to [turn on and set up extended ID](https://help.klaviyo.com/hc/en-us/articles/32053410094619).

### Shopify-branded onsite tracking

In addition to Klaviyo’s identification methods as part of [standard web tracking](https://help.klaviyo.com/hc/en-us/articles/115005076767), the Shopify's onsite tracking pixel enables identification during checkout if customers submit their information.

For a visitor’s identity to be captured during checkout, they must complete one of the following [Shopify events](https://shopify.dev/docs/api/web-pixels-api/standard-events):

- checkout\_completed
- payment\_info\_submitted
- checkout\_contact\_info\_submitted
- checkout\_shipping\_info\_submitted

This will cause anonymous activity to sync over to the associated profile, even if they never submitted a Klaviyo form or clicked a link in a Klaviyo email or SMS.

In order for visitors’ identities to be captured during checkout, the following requirements must be met:

1. Anonymous activity tracking must be enabled.
2. Shopify [behavioral events must be enabled](https://help.klaviyo.com/hc/en-us/articles/4425956184731).
3. Site visitors must accept marketing and analytics cookies.

## Disabling cookies

There may be instances where you choose to disable Klaviyo cookies from tracking. These reasons may include:

- You don't want to track users because of privacy, GDPR, or other security concerns.
- Customers have asked not to be tracked.
- You have a lean marketing program or want all customers to receive the same marketing, regardless of whether they have interacted with your brand before, bought, etc.

Klaviyo forms, including popups, will continue to appear on your website regardless of whether you have cookies turned off or on. However, you will not be able to personalize different types of forms to different types of users (e.g., they are already subscribed) or will not be able to see what they do on your site after they fill out a form.

If the JavaScript option is off, customers will not be cookied, and you will not have access to web tracking or their specific behaviors on your site. The **static-tracking.klaviyo.com** domain is used to serve all Javascript related to tracking (e.g., analytics.js). If you wish to block all tracking, this domain can also be blocked using cookie consent management tools (e.g., [OneTrust](https://help.klaviyo.com/hc/en-us/articles/4764571493275) or other domain-level blocking tools).

If you want to maintain Klaviyo JavaScript but remove a cookie, there is one workaround. Toggle the Klaviyo tracking on and off by creating a new cookie, `__kla_off`, and running `document.cookie = "__kla_off=true"`.

## Using API to access cookies

Using API to access cookies is useful to check whether or not Klaviyo can identify a customer. You can do this by running JavaScript and typing in klaviyo.isIdentified(). The response will then either be **true** or **false**.

## Email to website tracking

When [email to website tracking](https://help.klaviyo.com/hc/en-us/articles/115005248128) is enabled, Klaviyo identifies individuals that click through a Klaviyo email and browse your website. You can toggle on and off Klaviyo's ability to track email to website activity in your account's email settings.

With the release of iOS15, macOS Monterey, iPadOS 15, and WatchOS 8, Apple Mail Privacy Protection (MPP) changed the way that we receive open rate data on your emails by prefetching our tracking pixel. With this change, it’s important to understand that open rates will be inflated.

To see if your opens are affected, we suggest creating a [custom report](https://help.klaviyo.com/hc/en-us/articles/4416803987739) that includes an MPP property. You can also identify these opens in your individual [subscriber segments](https://help.klaviyo.com/hc/en-us/articles/4416791883163).

For complete information on MPP opens, visit our [iOS 15: How to Prepare for Apple’s Changes](https://www.klaviyo.com/blog/apple-ios15-klaviyo) guide.

To navigate to your email settings page click ****Account > Settings > Email > Tracking****.

![Email to website tracking with checkbox option checked off](https://klaviyo.zendesk.com/hc/article_attachments/28716055138715)

When this is on, we add an additional parameter to all URLs in your emails to track activity. This is called the \_kx parameter, and \_kx will appear directly in the URL. The unique encrypted value is then decrypted by our web tracking and allows us to identify the user that clicked through the URL.

For Shopify stores: Based on your Customer Privacy settings in Shopify, Klaviyo may not track onsite events for visitors to your Shopify store in the EU, EEA, UK and Switzerland, unless they have provided consent. Thus, email to website tracking will not identify these individuals.

To learn more, check out our article on [Klaviyo onsite tracking](https://help.klaviyo.com/hc/en-us/articles/115005076767).