<h1>How to configure out-of-stock items for automated flows on Shopify</h1>

## You will learn

Learn how to make sure out-of-stock items are not displayed in abandoned cart or browse abandonment emails by updating the way dynamic content is populated in your emails.

If you often sell out of popular items, it's possible that a customer will place an item in his/her cart one minute and come back hours later to find the same item out-of-stock. While abandoned cart and browse abandonment flows can drive significant revenue to your business, fast selling inventory can make it challenging to send reminders that don't fall flat. Encouraging customers to return to a cart full of out-of-stock items can lead to a frustrating customer experience.

## Before you begin

If you have not already, read our guide on [getting started with Shopify](https://help.klaviyo.com/hc/en-us/articles/115005080407-How-to-Integrate-with-Shopify) for step-by-step instructions on integrating, before continuing with this article.

Before following the steps in this article, it's important to note the following:

- Klaviyo will only "un-publish" out-of-stock items for Shopify stores if you do not allow customers to purchase products when they go out-of-stock.
- If you have multiple variations of an item, all variations must be out-of-stock in order for Klaviyo to consider the entire item out-of-stock and unpublish it.

## The abandoned cart flow

Klaviyo's default abandoned cart email templates (for our abandoned cart flow triggered by **Checkout Started**) feature a dynamic table that is used to populate each email with the specific items the recipient left behind in their abandoned cart.

If you would like an abandoned cart email to automatically be canceled if it is going to feature one or more items that have since gone out-of-stock, you will need to adjust the image section of the existing dynamic table in a given template.

1. In Klaviyo, open the abandoned cart flow email template you wish to edit.
2. Click on your dynamic table. Under ****Content****, you'll see Column 1 currently selected.
3. If Column 1 is currently set to ****Image****, switch it to ****Text****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/32421808336795)
4. Under ****Cell Content****, click the ****Source code**** icon.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/32421808345755)
5. Copy and paste the following snippet into the source code text box:

   ```
   {% catalog item.product_id unpublished="cancel" %}
   <a href="{{ event.extra.responsive_checkout_url }}">
   <img alt="" src="{{ catalog_item.featured_image.thumbnail.src }}" style="width: 200px;" width="200px" /></a>
   {% endcatalog %}
   ```
6. Once you've finished, click ****Done**** in the upper left.
7. Save your template.

This code will ensure that:

- Before a given email in your flow is scheduled to send, Klaviyo will look up each item that will dynamically populate in the individual email.
- If any one item is "unpublished" in your catalog at time of lookup, the entire email will get skipped.

For a given flow email, you can navigate to ****Analytics > Recipient Activity > Other**** and see a category labeled: ****Skipped: Catalog Item Unavailable****. This is where you can view all emails that were canceled - i.e. skipped - because an item featured in the email was out-of-stock or otherwise unavailable (if the item is no longer in your catalog).

It is not possible to remove a single out-of-stock item from an email and send the rest of the email as scheduled. If at least one item in a cart has gone out of stock, the entire email will be canceled.

### Responsive checkout page in Shopify

If you're having trouble with the "Return to Cart" button in your abandoned cart flow emails linking to the correct page, you may have to change the link that your button is pointing to.

1. In Klaviyo, open the abandoned cart flow email template you wish to edit.
2. Click on the "Return to Cart" button to edit the link URL.
3. Change the Link URL from

   ```
   {{ event.extra.checkout_url }}
   ```

   to the following:

   ```
   {{ event.extra.responsive_checkout_url }}
   ```
4. The image below shows an example.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/32421808352923)

## The browse abandonment flow

Klaviyo's default browse abandonment email template features a dynamic table block that is used to populate each email with the specific item a recipient browsed your website.

If you would like browse abandonment emails to automatically be canceled if they are going to feature an item that has since gone out-of-stock, you will need to adjust the image section of the existing table in a given template.

1. In Klaviyo, open the browse abandonment flow email template you wish to edit.
2. Click on your dynamic table. Under ****Content****, you'll see Column 1 currently selected.
3. If Column 1 is currently set to ****Image****, switch it to ****Text****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/32421808358171)
4. Under ****Cell Content****, click the ****Source code**** icon.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/32421808360859)
5. Copy and paste the following snippet into the source code text box:

   ```
   {% catalog event.ProductID unpublished="cancel" %}
   <a href="{{ catalog_item.url }}">
   <img src="{{ catalog_item.featured_image.full.src }}" style="width: 200px;" width="200px" /></a>
   {% endcatalog %}
   ```
6. Once you've finished, click ****Done**** in the upper left.
7. Save your template.

This will ensure that:

- Before a given email in your flow is scheduled to send, Klaviyo will look up the item that will dynamically populate in the individual email.
- If this item is "unpublished" in your catalog at the time of lookup, the email will be skipped.

For a given flow email, you can navigate to ****Analytics > Recipient Activity > Other**** and you will see a category labeled: ****Skipped: Catalog Item Unavailable****. This is where you can view all emails that were canceled - i.e. skipped - because an item featured in the email was out-of-stock or otherwise unavailable (if the item is no longer in your catalog).

## How to test your out-of-stock feature

You can test this feature by:

1. Adjust your email templates as explained above.
2. View an item on your site and/or start a checkout with a single item in your cart.
3. Wait until you see your tracked event appear in your account's ****Metric's tab****, under ****Analytics****.
4. Temporarily mark this single item out-of-stock in your store's backend.
5. Navigate to the flow that is triggered by the action you took (**Viewed Product** or **Started Checkout**) and has your newly adjusted email templates.
6. Click to preview one of these emails, and make sure the "choose a recent event to preview with" window features your own recent event.
7. When you click ****Preview****, you should see a preview where the item's image doesn't populate and instead the following message appears: ****Item (Number) is not published and unavailable******.
   ![Example email preview in Klaviyo showing block with item unavailable, outlined in red](https://klaviyo.zendesk.com/hc/article_attachments/28716329389467)**

## Outcome

You've now learned how to make sure out-of-stock items are not displayed in abandoned cart or browse abandonment emails, and how to test your out-of-stock feature.

## Additional resources

- [How to create an abandoned cart flow](https://klaviyo.zendesk.com/hc/en-us/articles/115002779411)
- [How to create a browse abandonment flow](https://klaviyo.zendesk.com/hc/en-us/articles/115002775252)
- [How to install back in stock for Shopify](https://klaviyo.zendesk.com/hc/en-us/articles/360001895651)
