---
id: "115005254668"
title: "How to remove out-of-stock items in flows for Magento 2"
source_url: "https://help.klaviyo.com/hc/en-us/articles/115005254668-How-to-remove-out-of-stock-items-in-flows-for-Magento-2"
section: "Magento 2"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:24Z"
language: "en"
---
## You will learn

Learn how to prevent out-of stock items from showing in flow emails when you are using Klaviyo's Magento 2 integration.

If you run a business with high-demand inventory and often sell out of popular items, it's possible that a customer will place an item in his/her cart one minute and come back hours later to find that the same item is out of stock.

While abandoned cart and browse abandonment flows can drive significant revenue to your business, fast selling inventory can make it challenging to send reminders that don't fall flat. Encouraging customers to return to a cart full of out-of-stock items can lead to a frustrating customer experience.

In Klaviyo, you can adjust any abandoned cart or browse abandonment flow to ensure emails featuring out-of-stock items get automatically canceled. To take advantage of this feature, you will need to slightly update the way dynamic content is populated in your abandoned cart or browse abandonment emails.

For Magento 2 stores, Klaviyo will "un-publish" an item when one of the following is true:

- The "visibility" of an item is 1, meaning the visibility status is  `NOT VISIBLE`
- The "status" of an item is 2, meaning the status is `DISABLED`
- The product is out-of-stock, where `IS_IN_STOCK -> 0`

You must have "manage stock" = yes in your Magento Admin panel.

## Abandoned cart flow

Klaviyo's default abandoned cart templates feature a dynamic table that is used to populate each email with the specific items the recipient left behind in his/her abandoned cart.

If you would like an abandoned cart email to automatically be canceled if it is going to feature one or more items that have since gone out-of-stock, you will only need to adjust the image section of the existing dynamic table in a given template.

1. Click on your dynamic table in the email template editor.
2. In the ****Content**** tab, click the left dynamic row.
3. Under **Cell Content**, toggle content from ****Image**** to ****Text****.
   ![Example of a dynamic table block configuration in the email template editor.](https://klaviyo.zendesk.com/hc/article_attachments/28704484629531)
4. Above the text box, click into the `Source` of this text block by clicking the ****</>**** button on the right.
5. In the ****Source**** area, you are going to copy and paste the following snippet:

   ```
   {% catalog item.product.id unpublished="cancel" %}
   <a href="{{ event.extra.checkout_url }}"><img alt="" src="{{ catalog_item.featured_image.thumbnail.src }}" width="200" /></a>
   {% endcatalog %}
   ```
6. Make sure to then click ****Source**** again before clicking ****Done**** in the top left to save this snippet in your text block.

What this will do:

- Before a given email in your flow is scheduled to send, Klaviyo will look up each item that will dynamically populate in the individual email
- If any one item is "unpublished" in your catalog at the time of lookup, the email will not be sent
- For a given flow email, you can navigate to ****Analytics > Recipient Activity > Other**** and you will see a category labeled: ****Skipped: Catalog Item Unavailable****
- This is where you can view all emails that were canceled -- i.e. skipped -- because an item featured in the email was out-of-stock or otherwise unavailable (if the item is no longer in your catalog)

![Recipient Activity page showing skipped reason 'Catalog item unavailable'.](https://klaviyo.zendesk.com/hc/article_attachments/28704476492187)

At this time, it is not possible to remove a single out-of-stock item from an email and send the rest of the email as scheduled. If someone abandons 5 items in a cart, and only 1 of the 5 items has gone out-of-stock, this feature will still cancel the full email.

## Browse abandonment flow

Klaviyo's default browse abandonment email template features a static table block that is used to populate each email with the specific item a recipient browsed your website.

If you want browse abandonment emails to automatically get canceled if they are going to feature an item that has since gone out-of-stock, you have to adjust the image section of the existing table in a given template.

1. Click on your dynamic table in the email template editor.
2. In the ****Content**** tab, click the left dynamic row.
3. Under **Cell Content**, toggle content from ****Image**** to ****Text****.
   ![Example of a dynamic table block configuration in the email template editor.](https://klaviyo.zendesk.com/hc/article_attachments/28704484629531)
4. Above the text box, click into the `Source` of this text block by clicking the ****</>**** button on the right.
5. In the ****Source**** area, copy and paste the following snippet:

   ```
   {% catalog event.ProductID unpublished="cancel" %}
   <a href="{{ catalog_item.url }}"><img src="{{ catalog_item.featured_image.full.src }}" width="200" /></a>
   {% endcatalog %}
   ```
6. Make sure to then click ****Source**** again before clicking ****Done**** in the top left to save this snippet in your text block.

What this will do:

- Before a given email in your flow is scheduled to send, Klaviyo will look up the item that will dynamically populate in the individual email
- If this item is "unpublished" in your catalog at the time of lookup, the email will get skipped
- For a given flow email, you can navigate to ****Analytics > Recipient Activity > Other****and you will see a category labeled: ****Skipped: Catalog Item Unavailable****
- This is where you can view all emails that were canceled -- i.e. skipped -- because an item featured in the email was out-of-stock or otherwise unavailable (if the item is no longer in your catalog)

## Test the out-of-stock feature

The best way to test out this feature:

1. Adjust your email templates as explained above
2. View an item on your site and/or start a checkout with a single item in your cart
3. Wait until you see your tracked event appear in your account's [Activity Feed](https://www.klaviyo.com/dashboard/activity)
4. Mark this single item out-of-stock in your store's backend
5. Navigate to the flow that is triggered by the action you took (**Viewed Product** or **Started Checkout**) and has your newly adjusted email templates
6. Click to preview one of these emails, and make sure the "choose a recent event to preview with" window features your own recent event
7. When you click ****Preview****, you should see a preview where the item's image doesn't populate and instead the following message appears "Item (XXXXXX) is not published and unavailable."

![Example of an email preview showing a message that a specific item is unavailable.](https://klaviyo.zendesk.com/hc/article_attachments/28704484630427)

## Additional resources

Learn more about the Magento integration:

- [Magento 2 data reference](https://klaviyo.zendesk.com/hc/en-us/articles/115003458852)