---
id: "18596283143707"
title: "How to add a dynamic image to a push notification"
source_url: "https://help.klaviyo.com/hc/en-us/articles/18596283143707-How-to-add-a-dynamic-image-to-a-push-notification"
section: "Push notification campaigns"
category: "Campaigns"
category_slug: "campaigns"
klaviyo_updated: "2026-04-20T16:49:11Z"
language: "en"
---
## You will learn

Learn how to add a dynamic image to a push notification.

Dynamic images are a great way to personalize your push notifications. For instance, you can show someone the exact product they favorited, started a checkout with, or bought.

## Before you begin

You can use dynamic images in:

- Metric-triggered flows, using either event data (e.g., items from a checkout or placed order) or catalog tags for an event.
- Campaigns and list- and segment-triggered flows, but only when the image URL exists as a custom property on the recipient’s profile.

  Also, note the following regarding push dynamic images:
- Only 1 dynamic image is allowed per push notification.
- Images must be under 1 MB.
- You can use conditional statements with dynamic images.

Want to request a feature for Klaviyo push notifications? Fill out this [Google form](https://forms.gle/7iPm6JQ4eKB6H2C4A) to tell us about it!

## Add a dynamic image to a push notification

1. Select the message where you want to include your dynamic image.
2. In the left sidebar, click ****Configure Content**** or ****Edit****.
3. Add or select the push notification in the flow.
4. Click the ****View details**** icon in the upper right-hand corner.
   ![View Details icon within the push preview window](https://klaviyo.zendesk.com/hc/article_attachments/28717418395291)
5. Find the data source for the image you want to include.
6. Click the data source for an image's first variable, which will typically end in 0.
   ![Example of what the data source looks like for an image](https://klaviyo.zendesk.com/hc/article_attachments/28717391149467)
7. On the left, click the **Insert media** icon in the **Body** box.
   ![Add media to push.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28717391154459)
8. Go to the ****Dynamic Image**** tab.
9. Paste the dynamic variable or dynamic URL for the image.
   ![Dynamic Image tab after pasting in an example variable](https://klaviyo.zendesk.com/hc/article_attachments/28717418408731)
10. Click ****Save****.
11. Check that the dynamic image was added correctly by making sure one appears in the preview screen.

****Example of using catalog tags****

You can also use catalog tags to add dynamic images in a rich push notification. To do so:

1. Go to ****Analytics > Metrics****.
2. Select the metric you want to use (e.g., **Ordered Product**).
3. Click ****Details**** for a specific event.
4. Find either the SKU or product ID tag.
5. Copy the label for the tag (except any parentheses or colon) so you have the exact spelling and capitalization.
   In the example below, we copy "ProductID."
   ![image5.png](https://klaviyo.zendesk.com/hc/article_attachments/28717391147547)
6. Paste this somewhere you won't lose it.
7. Navigate to a flow triggered by the same metric you just selected.
8. Select the push notification where you want to include your dynamic image.
9. In the left sidebar, click ****Configure Content**** or ****Edit****.
10. On the left, click the **Insert media** icon in the **Body** box.
    ![Add media to push.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28717391154459)
11. Go to the ****Dynamic Image**** tab.
12. Paste in the following catalog tag:
    {% catalog event.id %} {{catalog\_item.featured\_image.thumbnail.src}} {% endcatalog %}
13. Replace id in {% catalog event.id %} with the label you previously copied.
    Example: {% catalog event.ProductID %} {{catalog\_item.featured\_image.thumbnail.src}} {% endcatalog %}
14. Click ****Save****.

****Example of using conditional statements for dynamic images****

Dynamic images can use conditional statements.

Below is an example of an if/else statement to say that if there's a variant image, show that to recipients; else, use the default image:

**{% if event.extra.line\_items.0.product.variant.images.0.src %}{{ event.extra.line\_items.0.product.variant.images.0.src }}{% else %}{{ event.extra.line\_items.0.product.images.0.src }}{% endif %}**

Note that the exact format for these statements depends on your integration, and you should not copy them from email templates.