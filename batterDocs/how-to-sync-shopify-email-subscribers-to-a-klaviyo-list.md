<h1>How to sync Shopify email subscribers to a Klaviyo list</h1>

## You will learn

Learn how to sync Shopify email subscribers to a Klaviyo list, how the sync works, and best practices. Additionally, learn who gets added to your list and why.

It's important to sync your Shopify subscribers to a Klaviyo list in order to build a list of consented subscribers to send to.

## Before you begin

If you have not already, read our guide on [getting started with Shopify](https://help.klaviyo.com/hc/en-us/articles/115005080407-How-to-Integrate-with-Shopify) for step-by-step instructions on integrating before continuing with this article. When you integrate, make sure to check the setting to sync Shopify email subscribers to a Klaviyo list.

## How to sync subscribers to a list

1. In Klaviyo, select the ****Integrations****tab.
2. Select ****Shopify**** from the list to be brought to your Shopify integration settings page.
3. Under **Sync settings**, on the **From Shopify** tab, check the box next to **Sync your Shopify email subscribers to Klaviyo**.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/32924400693147)
4. Choose the list that you’d like to add subscribers to; as a best practice, add them to your main list such as your Email List. Note that you cannot select a segment; you must add your subscribers to a list.
5. If you don't see any lists populate:
   1. Click the ****Audience**** dropdown and select ****Lists & Segments****.
   2. Click ****Create List/Segment****, then choose ****List**** to create a new list.
   3. Navigate back to your Shopify integration settings to see your new list appear in the dropdown.
6. Click ****Save.****

Klaviyo automatically syncs historical email subscribers when you check **Sync your Shopify email subscribers to Klaviyo**.

For the historical subscriber sync, Klaviyo subscribes profiles based on whether they were subscribed in Shopify, unless the profile already exists in Klaviyo. If the profile already exists, Klaviyo uses the more recent consent status based on its timestamp.

## How do customers get added to my list?

### Ongoing subscriber sync behavior

The information below describes the behavior of the ongoing Shopify subscriber sync (as opposed to the historic sync that takes place initially when you integrate).

Below is an example of an email subscription checkbox on a Shopify checkout page. As a best practice, we recommend not having this box checked by default.

![KlaviyoTees store with Keep me updated on news and exclusive offers checked and highlighted in white](https://klaviyo.zendesk.com/hc/article_attachments/28716063268763)

Once you’ve checked the **Sync your Shopify email subscribers to Klaviyo** setting on your Shopify settings page in Klaviyo (as described in the previous section), you can start collecting subscribers.

Subscribes work in the following way:

- Subscribers are synced from Shopify to Klaviyo via Shopify's subscription model.
- Contacts being created in Shopify for the first time are subscribed in Klaviyo after providing their email and checking the box (essentially, at the **Checkout Started** step).
- Existing contacts in Shopify will need to place an order to be subscribed.
- Customers that subscribe via any Shopify sign-up form, such as a footer form, will also sync to your list.
- Email subscription status can be viewed on individual profiles in Klaviyo, and a **Subscribed to List event** is also recorded in Klaviyo.

Unsubscribes work in the following way:

- If a profile is unsubscribed in Shopify, they are not unsubscribed in Klaviyo.
- If a Klaviyo profile is already subscribed but does not consent at checkout, they will not be unsubscribed in Klaviyo (no change will happen).
- If a profile is unsubscribed in Klaviyo, and then resubscribes at checkout, they will be resubscribed in Klaviyo.

Shopify syncs customer profiles to Klaviyo in real time. Please note that profiles deleted in Klaviyo are not correspondingly deleted in Shopify, and vice versa.

### Shopify one-page checkout

Klaviyo's Shopify integration is fully compatible with Shopify one-page checkout. Whether you're using one-page checkout or multi-page checkout, the **Checkout Started** event is triggered after the customer fills out their email.

If you've customized your checkout, customers may still need to progress to the next step in the checkout process for the **Checkout Started** event to be triggered. Additional customer information will be updated in Klaviyo once the customer is created in Shopify.

## Best practices

### Leave the subscribe box unchecked by default

We strongly recommend keeping your email subscription box on your Shopify checkout page unselected by default to avoid damaging your sender reputation by accumulating passive subscribers. This option can be adjusted by navigating to ****Settings > Checkout**** in your Shopify store admin.

![](https://klaviyo.zendesk.com/hc/article_attachments/36060405741851)

Preselecting this box by default is not a recommended practice because it can lead to people who don’t wish to receive marketing communications from you getting added to your list. They are more likely to unsubscribe, ignore, or mark your emails as spam. If these contacts ignore your emails, they will eventually filter to spam.

If a large percentage of your list consists of passive subscribers added in this way and your email engagement is low, you're [putting your email deliverability at risk](https://help.klaviyo.com/hc/en-us/articles/115005250368-Strengthen-Your-Sender-Reputation-to-Alleviate-Deliverability-Issues). By growing lists of engaged subscribers and focusing on the quality of your leads over quantity, you're setting yourself up for strong email deliverability and higher conversion rates.

### Email subscribers and your welcome series flow

If a customer is added to your email list by signing up to a default Shopify sign-up form, and your welcome flow is set up (as well as your Shopify integration), this customer will be queued for your [welcome series flow](https://help.klaviyo.com/hc/en-us/articles/115002775172-How-to-Create-an-Email-Welcome-Series).

If a customer is added to your email list by clicking the **Subscribe to newsletter** box upon checkout, they will also get queued up for your welcome series flow. You can use flow filters in your welcome series flow to filter out groups of customers that you wish to exclude from this behavior.

## Shopify Checkout Extensibility compatibility

Checkout Extensibility is [Shopify's new foundation for checkout](https://help.shopify.com/en/manual/checkout-settings/customize-checkout-configurations/checkout-extensibility), replacing the now-deprecated **checkout.liquid** file. Klaviyo's Shopify integration is already fully compatible with Checkout Extensibility, and integration updates are not required given that you have not made any checkout.liquid customizations.

## Looking for information on the Accepts Marketing property?

On December 14th, 2022, Klaviyo released an update changing the way email subscribers are synced from Shopify to Klaviyo. This sync previously relied on Shopify’s **Accepts Marketing** tag, but now, subscribers are synced via Shopify’s subscription model.

This property still syncs to Klaviyo for customers who wish to use it, but it no longer determines subscription status in Klaviyo and has [since been deprecated by Shopify](https://shopify.dev/changelog/removal-of-accepts-marketing-fields-in-admin-api-customer-resources#:~:text=As%20of%20API%20version%202024,emailMarketingConsent%20should%20be%20used%20instead.). To learn how subscribers synced from Shopify to Klaviyo before December 14, 2022, check out our [Shopify Accepts Marketing Subscriber Reference](https://help.klaviyo.com/hc/en-us/articles/25184578360603).

## Outcome

You've now learned how to sync Shopify email subscribers to a Klaviyo list and best practices around managing email subscribers.

## Additional resources

- [How often integrations sync reference](https://help.klaviyo.com/hc/en-us/articles/115005253208)
- [Shopify data reference](https://help.klaviyo.com/hc/en-us/articles/115005080447)
- [How to use Shopify tags to filter customers](https://help.klaviyo.com/hc/en-us/articles/115005080907)
