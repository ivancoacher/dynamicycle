---
id: "1260806102230"
title: "How to add a dynamic image to a text message"
source_url: "https://help.klaviyo.com/hc/en-us/articles/1260806102230-How-to-add-a-dynamic-image-to-a-text-message"
section: "Getting started with SMS flows"
category: "SMS"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-21T13:54:26Z"
language: "en"
---
## You will learn

Learn how to add a dynamic image to an MMS message in Klaviyo.

Including a dynamic image allows you to personalize your text messages. For instance, you can show someone the exact product they viewed, started a checkout with, or bought.

## Before you begin

Depending on your use case, you may not always be able to add a dynamic image.

- Only metric-triggered flows can use dynamic images based on event data (e.g., items from a checkout or placed order) or on catalog tags for an event.
- Campaigns and list- and segment-triggered flows can have dynamic images only when the image URL exists as a custom property on the recipient’s profile.

Also, it's important note the following regarding dynamic images:

- Only 1 dynamic image is allowed per MMS.
- Images should be under 600 KB; otherwise carriers will compress it, which may make the image look distorted.
- If you try to send a dynamic image with a sending number that doesn't allow for MMS, the message will send, but the image will be removed.
- You can use conditional statements with dynamic images.
- Mobile carriers don't support WebP files, and attaching this type of image may cause the message to fail.

## How to add a dynamic image

1. Select the flow message where you want to include your dynamic image.
2. In the right sidebar, click ****Edit****.![Sidebar for a new SMS message in a flow](https://klaviyo.zendesk.com/hc/article_attachments/28720670835355)
3. Click the ****Preview & text**** in the upper right corner.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/33627732347035)
4. Find the data source for the image you want to include.
5. Click the data source for an image's first variable, which will typically end in 0.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/33627695663259)
6. Click ****Done****.
7. On the left, click the **Add image** icon (an image icon) in the **Message** box.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/33627695670299)
8. Go to the ****Dynamic Image**** tab.
9. Paste the dynamic variable or dynamic URL for the image.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/33627695672731)
10. Click ****Save****.
11. Check that the dynamic image was added correctly by making sure one appears in the preview screen.

****Use catalog tags****

You can also use [catalog tags](https://help.klaviyo.com/hc/en-us/articles/360004785571) to add dynamic images in the MMS. To do so:

1. From the SMS preview modal, locate the product ID or SKU for the first listed product.
2. Copy this variable.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/33627732367771)
3. Click ****Done**** to return to the SMS editor.
4. On the left, click the **Add image** icon (an image icon) in the message box.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/33627732370587)
5. Go to the ****Dynamic Image**** tab.
6. Paste in the following catalog tag:
   **{% catalog event.id %} {{catalog\_item.featured\_image.thumbnail.src}} {% endcatalog %}**
7. Replace **event.id** in **{% catalog event.id %}** with the variable from the tag you previously copied. Remove the brackets and any filters from the variable (so **{{ event.extra.line\_items.0.product\_id|default:'' }}** becomes **event.extra.line\_items.0.product\_id**).
   Example: **{% catalog event.extra.line\_items.0.product\_id %} {{catalog\_item.featured\_image.thumbnail.src}} {% endcatalog %}**
8. Click ****Save****.

****Example of using conditional statements****

Dynamic images can use conditional statements.

Below is an example of an if/else statement to say that if there's a variant image, show that to recipients; else, use the default image:
{% if event.extra.line\_items.0.product.variant.images.0.src %}{{ event.extra.line\_items.0.product.variant.images.0.src }}{% else %}{{ event.extra.line\_items.0.product.images.0.src }}{% endif %}

Note that exact format for these statements depends on your integration, and you should not copy them from email templates.

## Additional resources

- Find more [MMS image and GIF best practices](https://help.klaviyo.com/hc/en-us/articles/360041074911)
- Learn more about event variables in Klaviyo:
  - [About using event variables to personalize flows](https://help.klaviyo.com/hc/en-us/articles/115002779071)
  - [How to insert a dynamic image in an event-based flow email](https://help.klaviyo.com/hc/en-us/articles/115000104431)