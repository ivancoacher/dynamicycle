---
id: 22495505773083
title: "How to enable Back in Stock for Salesforce Commerce Cloud"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/22495505773083-How-to-enable-Back-in-Stock-for-Salesforce-Commerce-Cloud"
section: "Salesforce Commerce Cloud"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:34Z"
language: en
---

## You will learn

Learn how to enable Klaviyo Back in Stock and variant syncing for Salesforce Commerce Cloud (SFCC). First, you’ll make sure Back in Stock is enabled within your SFCC integration via the addition of a snippet, which will also enable variant syncing. Then, you’ll set up a Back in Stock form on your site using Klaviyo’s APIs. Lastly, you’ll set up a Back in Stock flow in Klaviyo to email customers who have subscribed to alerts.

## Before you begin

If you've yet to integrate your SFCC store with Klaviyo, you should [integrate first](https://help.klaviyo.com/hc/en-us/articles/360033744951), then skip ahead to the **Add a Back in Stock form** section of this article.

If you've already integrated Klaviyo with SFCC previously, please note that the following will happen when you enable Back in Stock in SFCC:

- Your Klaviyo catalog will be restructured. Variants that were previously synced as top-level products will now become nested variants under their respective parent. If you are using static product blocks in messaging for any of your product variants, these will need to be updated.
- For a brief period after you add the enable Back in Stock, your **Best-selling products** feed recommendations will appear empty, or may recommend unusual products. Within 3 days, these recommendations should return to normal. You may want to pause any messaging using the **Best-selling products** feed for this period.

## Enable Back in Stock / variant syncing for SFCC

To use Klaviyo’s Back in Stock functionality with SFCC, you’ll need to add a **/variations** snippet to your OCAPI Data API settings, if you haven’t done so already. This snippet also enables variant syncing. To do this:

1. In your SFCC Business Manager, navigate to ****Administration > Site Development > Open Commerce API Settings****.
2. Add the following JSON as a listed resource under the type **Data** and context **Global (organization-wide)**, under the client\_id assigned to Klaviyo (you should already have other snippets here):

   ```
   {
                  "resource_id":"/products/*/variations",
                  "methods":["get"],
                  "read_attributes":"(**)",
                  "write_attributes":"(**)"
   }
   ```

   Once added, the settings should appear similar to this:
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28704487196955)
3. Click ****Save****.

That’s it! Next time your catalog sync runs (this sync runs every 8 hours), you’ll see product variants synced to your Klaviyo catalog. To view them:

1. Head to ****Content >**** ****Products**** in Klaviyo.
2. Search for a parent product and click on it.
3. Scroll to the bottom and click the ****Variants**** dropdown to verify that the variants are listed correctly.

## Add a Back in Stock form

Now, it’s time to add a Back in Stock button and form to your site so that your customers can request back in stock alerts. This button and accompanying form should appear on out-of-stock product pages, and when it’s submitted, a request should be made to our [Back in Stock API](https://developers.klaviyo.com/en/reference/create_back_in_stock_subscription).

Check out our developer portal to [learn how to make client-side requests to our Back in Stock API and subscribe customers to email alerts](https://developers.klaviyo.com/en/docs/how_to_set_up_custom_back_in_stock#client-side-request).

## Build your Back in Stock flow

Finally, you’ll want to create a flow to automatically message customers (via email, SMS, or both) who’ve subscribed to Back in Stock notifications:

- Check out our article to [learn how to set up this flow](https://help.klaviyo.com/hc/en-us/articles/115003872251#h_01HBBYWCR7VMA1Q70QTGAXQBGR).
- When setting up the flow, choose the pre-built Back in Stock flow for SFCC from the Flow Library:
  ![](https://klaviyo.zendesk.com/hc/article_attachments/28704487199259)
- Make sure to [configure your account’s Back in Stock flow settings](https://help.klaviyo.com/hc/en-us/articles/115003872251#h_01HBBYXYTAXRW86A1XXE4FRV2T).

## Additional resources

- [Getting started with SFCC](https://help.klaviyo.com/hc/en-us/articles/360033744951)
- [SFCC data reference](https://help.klaviyo.com/hc/en-us/articles/360058323811)
- [How to upgrade your SFCC cartridge](https://help.klaviyo.com/hc/en-us/articles/16708128591259)