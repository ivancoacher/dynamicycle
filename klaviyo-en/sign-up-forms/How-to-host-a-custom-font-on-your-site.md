---
id: 360047999812
title: "How to host a custom font on your site"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360047999812-How-to-host-a-custom-font-on-your-site"
section: "Form best practices"
category: "Sign-up forms"
category_slug: "sign-up-forms"
klaviyo_updated: "2026-05-11T10:59:25Z"
language: en
---

## You will learn

Learn how to upload a font, meaning a font that is not hosted by Google or Adobe, to your ecommerce site to import in your Klaviyo sign-up forms. If you want to use an imported font in your sign-up form, there are 2 options:

1. Use the public font hosted on your website.
2. Host your own font publicly and use the URL to import your font into your sign-up forms.

This article will walk you through how upload a custom font to your ecommerce site to use in your forms, not your email templates. For information on adding custom fonts to your email templates, head to our article on [custom fonts in email templates](https://klaviyo.zendesk.com/hc/en-us/articles/115005256008).

## Using your website’s font

To begin, you can use the public URL on your site to upload the font in Klaviyo.

Note that this method for hosting a custom font is not supported with Shopify stores.

1. Head to your site.
2. Right-click to select ****Inspect**** or ****Inspect Element****, depending on your internet browser.
3. From there, navigate to ****Network**** > ****Fonts.****
4. Refresh the page.
   You will see all of your fonts listed. If the name of the font does not populate and you instead see a string of numbers and letters, select the preview tab to decide which font you want to use in your sign-up form.
5. Under **Name**, click on the font you want to import.
6. Select the ****Headers tab.****
7. Copy the URL of the font you want to use.
8. In Klaviyo, navigate to ****Content > Images & brand > Fonts.****
9. Select ****Import font****.
10. Upload your custom font by [pasting the URL](https://help.klaviyo.com/hc/en-us/articles/360047955672#h_01HK5YMHFNNG6988YPM8E5FRY1) in the **Source Address**.

## Uploading a self-hosted font

To begin, if the font isn’t already publicly hosted online, download the font that you want to use to your computer. Note that the file must be in WOFF, WOFF2, TTF, EOT, or SVG format to use in Klaviyo. Also, be cautious downloading font files from the internet, as they can contain malware. From there:

1. Upload the font to your ecommerce site’s assets. You will need to do this within the code of your site.
2. Save it.

For more information, head to the respective ecommerce platform help centers for more information on how to add an asset to your site

- [Shopify](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/file-uploads#upload-a-file-on-the-files-page)
- [BigCommerce](https://support.bigcommerce.com/s/article/How-do-I-add-and-link-to-a-file-in-my-store)

Once you get the URL, navigate back to Klaviyo and select ****Content > Images & brand > Fonts****. From here, click the ****Import**** font tab and [import your font](https://help.klaviyo.com/hc/en-us/articles/360047955672#h_01HK5YMHFNNG6988YPM8E5FRY1).

![The Import font menu of the Images and branding tab within Klaviyo.](https://klaviyo.zendesk.com/hc/article_attachments/28713332394139)

## Site font impacted by Klaviyo.js

Klaviyo [active On site tracking](https://help.klaviyo.com/hc/en-us/articles/115005076767#h_01HADAYAABB803T7AGQ6G3HM6B) (Klaviyo.js), must be installed manually or through your ecommerce integration in order to publish Klaviyo sign-up forms on your website. If you have only loaded some font variations, Klaviyo.js loads the remaining variations in your library when it's injected into your site. Because of this, the fonts on your site may be slightly edited in this process, such as a change in the weight of the site's header.

There are 2 options for resolving any changes made to your fonts by Klaviyo.js. You can either:

- Delete the relevant fonts from your Klaviyo font library.
- Update the CSS on your site's header so that it doesn't get overwritten when Klaviyo.js loads the additional variations.

  Because this option would require in-depth knowledge of CSS, you may require the assistance of a developer. Klaviyo cannot offer assistance on adjusting your site's CSS, however we do have a vast [partner network](https://connect.klaviyo.com/).

## Additional resources

- [How to use custom fonts in sign-up forms](https://klaviyo.zendesk.com/hc/en-us/articles/360047955672)
- Course: [Creating an effective acquisition strategy using sign-up forms](https://academy.klaviyo.com/creating-an-effective-acquisition-strategy-using-signup-forms)
- [How to add custom fonts in email templates](https://help.klaviyo.com/hc/en-us/articles/115005256008)