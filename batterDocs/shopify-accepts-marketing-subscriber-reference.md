<h1>Shopify Accepts Marketing subscriber reference</h1>

## You will learn

Learn about how subscribers in your account were synced from Shopify to Klaviyo before Klaviyo updated this sync in December 2022.

## Before you begin

On December 14th, 2022, Klaviyo released an update changing the way email subscribers are synced from Shopify to Klaviyo. This sync previously relied on Shopify’s **Accepts Marketing** tag, but now, subscribers are synced via Shopify’s subscription model.

This property still syncs to Klaviyo for customers who wish to use it, but it no longer determines subscription status in Klaviyo and has [since been deprecated by Shopify](https://shopify.dev/changelog/removal-of-accepts-marketing-fields-in-admin-api-customer-resources#:~:text=As%20of%20API%20version%202024,emailMarketingConsent%20should%20be%20used%20instead.).

If you'd like to learn about how Klaviyo's subscriber sync currently functions, head to [How to sync Shopify email subscribers to a Klaviyo list](https://help.klaviyo.com/hc/en-us/articles/115005080667). If you are looking to understand your Shopify subscribers synced before this December 2022, read on.

## How did subscribers previously sync from Shopify?

Before December 14, 2022, Klaviyo's subscriber sync from Shopify relied on Shopify’s **Accepts Marketing** tag.

Below is an example of how the property appeared on a customer's profile in Klaviyo.

![Information section of a Klaviyo profile including Accepts Marketing property set to true](https://klaviyo.zendesk.com/hc/article_attachments/28715972898331)

There are a few situations which can could have caused a pre-existing customer to have **Accepts Marketing** set to false, but they're still subscribed to your email list:

- If a customer checked out and decided not to accept email marketing at that time, but later subscribed through a Klaviyo sign-up form, they still would have been added to your email list.
- If a customer checked out and accepted email marketing, they'd be added to your email list. If they checked out again, they probably decided not to subscribe again since they were already subscribed. Depending on your checkout configuration, Shopify might have seen this as not accepting marketing (**Accepts Marketing** = **false**.) You probably don't want to treat this customer as an unsubscribe. Rather, you'll want to keep this customer on your email list.

Additionally, it's important to note that a pre-existing customer who has **Accepts Marketing** set to **false** won't automatically be suppressed. To learn more about suppression, check out our article [Understanding suppressed email profiles](https://help.klaviyo.com/hc/en-us/articles/115005246108).

## Additional resources

- [Getting started with Shopify](https://help.klaviyo.com/hc/en-us/articles/115005080407)
- [How to sync Shopify email subscribers to a Klaviyo list](https://help.klaviyo.com/hc/en-us/articles/115005080667)
