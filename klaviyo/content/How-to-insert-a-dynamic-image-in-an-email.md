---
id: 4408810769307
title: "How to insert a dynamic image in an email"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/4408810769307-How-to-insert-a-dynamic-image-in-an-email"
section: "Use variable syntax and tags"
category: "Content"
category_slug: "content"
klaviyo_updated: "2026-04-21T13:55:00Z"
language: en
---

## You will learn

Learn about the **Dynamic Image** option in an email image block, including how to find the right personalization tag to use and add it to an email template.

Dynamic images allow you to customize each recipient’s message based on data stored in their Klaviyo profile or event data. For example, you can use this feature to display an item they recently added to their cart in a flow triggered by the Added to Cart metric. Or, by storing a unique image URL in a subscriber’s profile, you can show that custom image in campaigns you send them.

## Store your images in a profile or event

You can display dynamic images from event data (e.g., started checkout events for an abandoned cart flow) in metric-triggered flow emails. Images stored in event data cannot be displayed in campaigns or non-metric triggered flows, which can only use images stored on the recipient's profile as profile properties.

### Storing images for campaigns and non-metric triggered flows

To display a dynamic image in a campaign or non-metric triggered flow (i.e., a flow triggered by a list, segment, or date), an image URL (e.g., <https://www.klaviyo.com/static/klaviyo-social-share-image.jpg>) must be stored in each recipient’s profile properties. You can add an image URL to their profile properties in the following ways:

- [Upload a CSV of profile data](https://klaviyo.zendesk.com/hc/en-us/articles/1260806293150)
- [Use a third-party integration](https://klaviyo.zendesk.com/hc/en-us/articles/360049626051)
- [Use Klaviyo’s APIs](https://developers.klaviyo.com/en/reference/api_overview)

### Storing images for metric-triggered flows

To display a dynamic image in a metric-triggered flow (e.g., a flow triggered by an Add to Cart event), you can either use profile data stored using the methods outlined above, or use event data from the metric that triggers the flow.

Note that event data can only be used in a flow triggered by that event.

You can add event data to Klaviyo in the following ways:

- [Through a default Klaviyo integration](https://klaviyo.zendesk.com/hc/en-us/articles/115000256472)
- [Through a third-party integration](https://klaviyo.zendesk.com/hc/en-us/articles/360049626051)
- [Using Klaviyo’s APIs](https://developers.klaviyo.com/en/reference/api_overview)

## Add a dynamic image to an email

Once you’ve stored your dynamic image information in Klaviyo, identify the correct tag to use to include it in your email.

1. Open the email template where you’d like to add the dynamic image.
2. Click ****Preview & test****.
3. Scroll through the sample event and profile data under ****All properties**** until you find the image variable. Then, click the variable name to copy it.
4. Once you’ve copied your tag, drag an image block into your message.
5. Click ****Select image > Dynamic Image****.
6. Paste the tag into the **Dynamic variable or dynamic URL** field.
7. Finally, preview your email to ensure that the tag is working correctly. If you don't see your image, double check that you’ve selected an event or profile that contains the variable you used.

## Add a backup image

If you aren’t confident that every email recipient will have an image available in their profile or event data, consider using a backup image so the area doesn’t appear blank. There are 2 ways to add a backup image:

### Use the missing product filter

Add the missing product filter to the end of your dynamic image variable to use Klaviyo’s default backup image. To add this filter, add |missing\_product\_image after the dynamic image variable, like this:

`{{ event.image_url|missing_product_image }}`

If anyone who receives the email is missing an image, they’ll see the missing product image instead:

![The missing image placeholder](https://klaviyo.zendesk.com/hc/article_attachments/28704485792155)

### Set your own backup image

To choose your own backup image, apply the default filter with an image URL of your choosing. This will display your custom backup image if a recipient doesn’t have an image set. To add this filter, add |default:'' to the end of your image variable with your custom image URL between the single quotes, like this:

`{{ event.image_url|default:'www.example.com/custom_image_url.jpg' }}`

## Additional resources

- [How to add personalization into text blocks](https://help.klaviyo.com/hc/en-us/articles/4408810654235)
- [How to build dynamic blocks in a flow email](https://help.klaviyo.com/hc/en-us/articles/4408802597659)
- [How to create a metric-triggered flow](https://klaviyo.zendesk.com/hc/en-us/articles/360003057151)
- [How to embed assets directly in an email](https://klaviyo.zendesk.com/hc/en-us/articles/115005256968)