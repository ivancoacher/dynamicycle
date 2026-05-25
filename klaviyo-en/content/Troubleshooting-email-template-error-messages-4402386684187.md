---
id: "4402386684187"
title: "Troubleshooting email template error messages"
source_url: "https://help.klaviyo.com/hc/en-us/articles/4402386684187-Troubleshooting-email-template-error-messages"
section: "Template troubleshooting "
category: "Content"
category_slug: "content"
klaviyo_updated: "2026-04-21T13:54:57Z"
language: "en"
---
## You will learn

If you encounter errors or warnings in an email template, you may need to resolve them before sending your message. Search this resource for the error message or warning you’re encountering to find tips for resolving the issue.

## Campaign sending warnings

- ****We found # blocks in your email that either still have the default text unmodified or are blank. Please review your email before continuing.****
  If you encounter this warning, look for empty blocks or placeholder content (e.g., “This is a text block. Click here to edit it.”) in your template. Check the desktop and mobile versions of the template. If you can’t find an empty block or placeholder content, send a preview message to yourself and review it on both desktop and mobile. If the preview looks good, it’s safe to send the message and ignore this warning.
- ****Possible Email Content Issues. It doesn’t look like there are any links in your email. Did you forget to add them to your email?****
  This warning appears if your plain-text or custom HTML email doesn’t include any links. Review the message to make sure all content has been added, including links for any calls-to-action. If you do not want to include any links in your email (other than your unsubscribe link), you can ignore this warning.
- ****Unsubscribe Link. We couldn’t find an unsubscribe link in your email. Klaviyo will automatically add an unsubscribe link when sending the email if you don’t add one.****
  This warning appears if you haven’t added an unsubscribe tag to your message (e.g., {% unsubscribe %} or {% unsubscribe\_link %}). [Add an unsubscribe link](https://help.klaviyo.com/hc/en-us/articles/115006054267-How-to-Add-an-Unsubscribe-Link-to-Email-Campaigns) to avoid Klaviyo’s default footer being appended to your message.

## Preview errors

When previewing a message, you may encounter this error message:

****Message displayed without tags or variables****
****Fix invalid template tags or variables to preview the message with actual profiles and events.****

This error means that there is invalid syntax somewhere in your message. To locate the source of the error, check your message’s subject line and body content for variables, tags, or conditional statements (i.e., anything in your template surrounded by curly brackets **{}**) that don’t follow the format outlined in [Klaviyo’s Help Center resources](https://help.klaviyo.com/hc/en-us/articles/115005084927). Below are some tips for locating the error:

- Check both the desktop and mobile versions of your message.
- If your message contains a [dynamic coupon](https://help.klaviyo.com/hc/en-us/articles/115005084727-How-to-Use-Coupon-Codes-in-Klaviyo), make sure the coupon name is correct, and that your coupon has been configured in the **Coupons** tab.

## Custom HTML template errors

- ****We couldn't find the following images: ... Make sure they are included in the zip file you uploaded.****
  Check that you’ve spelled all image source paths correctly, and that they match the file names of the images you uploaded. If no image paths are provided in the error message, review your HTML file for empty background attributes (e.g., **background=””**)
- ****An {% unsubscribe %} tag is required.****
  Add a [Klaviyo unsubscribe tag](https://help.klaviyo.com/hc/en-us/articles/115005078267) to your message footer to resolve this error.
- ****Could not parse the remainder: 'Z' from 'XYZ'.****
  This error means that one of your tags (anything surrounded by {% %}) is not recognized by Klaviyo. Refer to our guide to [message personalization reference](https://klaviyo.zendesk.com/hc/en-us/articles/4408802648731) to see accepted tags.

## Catalog errors

If your template uses a [catalog lookup tag](https://klaviyo.zendesk.com/hc/en-us/articles/360004785571), you may encounter the error ****Unable to find item with code: \_\_. It may have been deleted.****

If you see this error, it means we don't recognize the item ID included in the tab. Make sure that:

- You're previewing with an event that contains item IDs (if the item ID dynamically references event data).
- The reference to your event data's item ID is correctly formatted.
- The item ID from your event data matches what's in your Klaviyo catalog.

## Shopify template errors

- { % for item in...
- {% endfor %}
- {% if...
- {% elsif...
- {% else %}
- {% endif %}

- ****Body html Liquid syntax error: Unknown tag 'unsubscribe'****
  ****Body html Liquid syntax error: Unknown tag 'web\_view'****
  These errors, and other errors like them, mean that a Klaviyo-specific tag was added to your template before exporting it to Shopify. Shopify doesn’t support Klaviyo’s unsubscribe, manage preferences, or web view links.
- ****Body Html Liquid Syntax Error : Unknown tag "Load"****
  Shopify cannot support Klaviyo’s product block feature. If you add a product block into your Shopify notification template, then import that template into Shopify, this error will appear. Remove the product block, export your template’s HTML, and import it into Shopify.
- ****Body html Liquid syntax error: Unknown tag 'elsif'****
  ****Body html Liquid syntax error: 'if' tag was never closed****
  ****Body html Liquid syntax error: 'X' Tag Was Never Closed****
  Many of Klaviyo’s Shopify notification templates include conditional statements, which make your message dynamic based on the customer’s order status. If part of a conditional statement is deleted, you’ll see an error like the ones above.

  To resolve this, open the template in Klaviyo and remove the remaining elements of the conditional statement. Search for tags that begin with: