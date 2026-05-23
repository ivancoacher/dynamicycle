<h1>Getting started with Amazon Buy with Prime</h1>

## You will learn

Learn how to enable Klaviyo’s Buy with Prime integration in order to bring your customer profile and order data into Klaviyo. [Buy with Prime](https://buywithprime.amazon.com/how-to-get-started) is a service that allows ecommerce platform merchants (such as those on Shopify, WooCommerce, Adobe Magento, and more) to power purchase payment and fulfillment through Amazon, via the addition of a “Buy with Prime” button to individual product pages on their store. This guide walks through connecting Buy with Prime and Klaviyo to automatically sync this purchase data, so that you can reach customers with targeted messaging.

## Before you begin

If you are already using [Shopify's Buy with Prime app](https://apps.shopify.com/buy-with-prime), and you've [integrated Klaviyo with Shopify](https://help.klaviyo.com/hc/en-us/articles/115005080407), you do not need to install Klaviyo's Buy with Prime integration. Buy with Prime data is already syncing to Klaviyo via Shopify, and you'll see these purchases tagged as **Buy with Prime**.

Before integrating, make sure you are:

- In an owner, admin, or developer role in your Buy with Prime account.
- In an owner, admin, or manager role in your Klaviyo account.
- Logged in to the Klaviyo account you want to integrate with Buy with Prime.

The Buy with Prime integration is supported by Klaviyo through our partner Sixads. If you need to contact support, see the [section below on how to do so](https://help.klaviyo.com/hc/en-us/articles/14708088221467#h_01HWDSPNZDW9SG586H8BCCMQFN).

## Add the Buy with Prime integration

1. Log in to your Klaviyo account if you have not done so already.
2. Select the ****Integrations**** tab.
3. Click ****Explore apps****, search for **Amazon Buy with Prime**, and select the card.
4. On the next page, click ****Install****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/39460679079323)
5. Log in to your Buy with Prime account if needed. Review the permissions on the page, then click ****Authorize****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28705665073307)
6. Enter an email address for important app updates, then click ****Connect****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28705638229019)
7. If your Klaviyo login has multiple accounts associated with it, you’ll be prompted to select the account you want to integrate with.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28705665079707)
8. Review the access information and click ****Allow****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28705638230171)
9. If the integration setup is successful, you’ll see a green flag reading **Connected** and data will begin syncing to Klaviyo.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28705665082907)

## Monitor your data sync

New data will sync to Klaviyo in real time. Currently, there is no historical sync of Buy with Prime data to Klaviyo. To learn about the events synced from Buy with Prime to Klaviyo, read our [Buy with Prime data reference](https://help.klaviyo.com/hc/en-us/articles/14708160794779).

## How to contact support

- Klaviyo’s Buy with Prime integration is supported by Klaviyo through Sixads. If you have questions about the integration and need support, you can contact integration-specific support by emailing support@sixads.net. Please include the following in your email:

- Your company name.
- Your [Klaviyo public API key](https://help.klaviyo.com/hc/en-us/articles/115005062267#find-your-api-keys2).
- The issue you’re experiencing.
- A screenshot of your issue, if applicable.

- If you need general support for Klaviyo-related questions, [contact Klaviyo support](https://help.klaviyo.com/hc/en-us/articles/115001002272-How-to-contact-support).

## Using Buy with Prime data in Klaviyo flows

Flows, also known as automations or drip campaigns, are Klaviyo’s tools for personalized communications with your customers. Including Buy with Prime data in your flows ensures that your customers are receiving accurate messaging around their purchase behavior.

#### Abandoned cart flow

For an abandoned cart flow, you'll need to create 2 flows: 1 triggered by your ecommerce platform's checkout event, and the other triggered by Buy with Prime's checkout event.

- [Ecommerce platform abandoned cart flow how-to](https://klaviyo.zendesk.com/hc/en-us/articles/115002779411).
- [Buy with Prime abandoned cart flow how-to.](https://klaviyo.zendesk.com/hc/en-us/articles/14985388418331)

#### Browse abandonment flow

For a browse abandonment flow, you only need to create 1 flow, since this flow is triggered by Klaviyo's **Viewed Product** event. In this flow, you'll including flow filtering using ecommerce platform and Buy with Prime data.

- [Browse abandonment flow how-to.](https://klaviyo.zendesk.com/hc/en-us/articles/115002775252)

#### Winback flow

For a winback flow, you'll need to create 2 flows: 1 triggered by your ecommerce platform's **Placed Order** event, and the other triggered by Buy with Prime's **Placed Order** event.

- [Ecommerce platform winback flow how-to.](https://klaviyo.zendesk.com/hc/en-us/articles/115002775192)
- [Buy with Prime winback flow how-to.](https://klaviyo.zendesk.com/hc/en-us/articles/15156331062171)

## Outcome

You’ve integrated Buy with Prime with Klaviyo to bring order and customer data into Klaviyo. You can now reach Buy with Prime shoppers with targeted messaging through Klaviyo.

## Additional resources

- Learn about data synced between Amazon and Klaviyo with the [Buy with Prime data reference.](https://help.klaviyo.com/hc/en-us/articles/14708160794779)
- Not using Buy with Prime yet? [Learn how to get started.](https://buywithprime.amazon.com/how-to-get-started)
