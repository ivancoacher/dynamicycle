---
id: "360047955672"
title: "How to use custom fonts in sign-up forms"
source_url: "https://help.klaviyo.com/hc/en-us/articles/360047955672-How-to-use-custom-fonts-in-sign-up-forms"
section: "Build and use forms"
category: "Sign-up forms"
category_slug: "sign-up-forms"
klaviyo_updated: "2026-04-21T13:56:53Z"
language: "en"
---
## You will learn

Learn how to design your sign-up forms with custom fonts so that your customers experience strong brand identity and consistency with the rest of your site.

Creating a beautifully designed sign-up form is paramount to compelling them to follow through with the goal of your form. If your brand uses fonts that are not available natively in the sign-up form editor, adding in these custom fonts is an easy way to make your forms look cohesive with the rest of your site. After you’ve added your fonts, you can use your font to customize your sign-up forms as you see fit.

## Key terms

- Custom font
  Any font that isn't provided by default in the Klaviyo editor. This includes:
  - Google fonts
  - Adobe fonts
  - Imported fonts
- Web-safe font
  A font that is stored locally on most devices, and therefore doesn't need to be loaded from an outside source in order to display.
- Fallback font
  A web-safe font that is used if a page is unable to load the primary font.

## Adding custom fonts to your account

From the main menu along the left side, navigate to the ****Content > Images & Brand****. From there, click into the ****Fonts**** tab. You can add in a Google font, Adobe font, or an Imported font.

If you add a custom font to Klaviyo that is already in use on your site, upload the exact font style (e.g., light, bold, or italic) and weight (e.g., 400) your site currently uses. If you upload a font and select a style or weight that differs slightly, the styles selected in Klaviyo may override some of your site’s existing font styles.

![The Fonts menu of the Images and Brand tab within Klaviyo where you can add a new Google, Adobe, or Imported font.](https://klaviyo.zendesk.com/hc/article_attachments/28716330781595)

### Adding a Google font

To add a Google font:

1. Select the ****Font name**** dropdown to see a list of [all available Google fonts](https://fonts.google.com/), except for the fonts that you have already loaded in your account.
2. Choose your desired font. Upon selecting, you will see a preview of the font below the dropdown, as well as the number of possible variants (e.g., bold, italic, etc.).
   - If you want to add more than 1 variant, click the arrow next to the number of possible variants, and choose the fonts that you want to add.
3. Select a **Fallback font**.
4. Click ****Add font****. Your added font will now display in the **Your Fonts** section at the bottom of the page.

![Adding a new custom font, specifically a Google Font, to an example Klaviyo account](https://fast.wistia.com/embed/medias/1ij0bg4r1v/swatch)

From the **Your Fonts** section, you’ll be able to see the fonts that you have added to your account. To edit or delete any of your fonts in this section, select the three dots on the font.

![The Your Fonts section of the Images and Brand tab showing the 3 dots menu selected on an example font.](https://klaviyo.zendesk.com/hc/article_attachments/28716330776859)

If you choose to use Google fonts, for GDPR purposes, please note that Google Fonts are hosted by Google. By including a Google font into your font library, you are using the Google font. Klaviyo has a selection of custom fonts that we use in our sign-up form templates available for you to easily import and use. [View the list of Klaviyo-hosted fonts](https://klaviyo.zendesk.com/hc/en-us/articles/14780233854363).

### Adding an Adobe font

You must have an Adobe account to use Adobe fonts.

To add an Adobe Font:

1. Navigate to Adobe Fonts.
2. Search for your Adobe font link, then select your font.
3. Next to your font name, click the code icon.
4. If needed, enter a new project name, then click ****Save****.
5. On the next modal, copy the https://use.typekit.net URL for the font that you want to add. Do not include the .css as part of the URL when you copy it.


   ![A video showing how to find your adobe font link by slecting the font, clicking the code icon, and copying the URL for the font you want to add.](https://fast.wistia.com/embed/medias/6c8yc8w6tm/swatch)
6. Navigate back to Klaviyo and paste the URL into the **CSS Address** field.
7. Select ****Continue****, then choose a **Fallback font** for the font you want to upload. Note that if a font is already available in your account, a green checkmark displays next to the font and its existing fallback font shows.


   ![Adding an Adobe font to an example Klaviyo account by asting the link in the CSS Address box, clicking continue, assigning a fallback font, and then clicking Add font.](https://fast.wistia.com/embed/medias/t5nmo17jb8/swatch)
8. Select ****Add font****.

Once you've added your font, it will be listed in the **Your Fonts** section at the bottom of the page. To edit any of your fonts in this section, select the three dots on the font.

![The Your Fonts section of the Images and Brand tab in an example Klaviyo account showing the 3 dots menu selected on one of the fonts.](https://klaviyo.zendesk.com/hc/article_attachments/28716330776859)

### Adding an imported font

If you've purchased or downloaded a custom font that's not hosted by a third-party source, you can still use it in a Klaviyo form. First, [host the font files](https://help.klaviyo.com/hc/en-us/articles/360047999812-Hosting-a-Custom-Font-on-Your-Site) in a location that will be accessible to Klaviyo (for example, in your site’s assets or on a font hosting platform). Make sure to enable Cross-Origin Resource Sharing (CORS) by setting the `Access-Control-Allow-Origin header` to `*`, so the font can be accessed by your recipients’ devices.

To add an imported font:

1. Name your font.
2. Specify a font-weight, style, and a source URL. The source URL must be a valid URL that ends in WOFF, WOFF2, TTF, EOT, or SVG.
3. Optional: To add additional variants, select ****Add font variant****, then repeat step 2 for this variant.
4. Select ****Add Font**** to add this font to the **Your Fonts** section.

![Adding a new imported font to an example Klaviyo account by entering the font name and variant details.](https://fast.wistia.com/embed/medias/re1og8gv6d/swatch)

From **Your Fonts**, you’ll be able to see the fonts that you have imported into your account. You can also delete or edit your fonts by selecting the 3 dots on the font.

![The Your Fonts section of the Images and Brand tab in an example Klaviyo account showing the 3 dots menu selected on one of the fonts.](https://klaviyo.zendesk.com/hc/article_attachments/28716330776859)

## Edit a font

To edit an existing custom font:

1. Navigate to Content > Images & brand > Fonts.
2. Find the font you'd like to edit in the **Your Fonts** section at the bottom of the page.
3. In that font's card, click the 3 dots in the top corner.
4. Choose ****Edit****. From here, you will be able to:
   - Edit the fallback font for any custom font.
   - For Google and Klaviyo-hosted fonts only, edit or add to the selected variants by selecting ****# of font variants**** to expand the list, then selecting any fonts you'd like to add.
     ![The Edit Font menu in Klaviyo showing additional font variants selected to add to an account's existing Google Font.](https://klaviyo.zendesk.com/hc/article_attachments/28716330787739)

     You cannot add variants to Adobe fonts after uploading it since the variants are built into your Typekit link. To add variants to an Adobe font, you must delete the existing font and re-add it using a different Typekit link that has the all variants you want to include.
5. When you’re done editing your font, select ****Update font****.

## Delete a font

To delete a font:

1. Navigate to the **Your Fonts** section.
2. On the font you'd like to delete, click the 3 dots then choose ****Delete****. If you choose to delete your font, a modal will pop up notifying you that, if your font is used in any forms, your fallback font will display after you delete your added font.
   ![The Delete Font confirmation modal that appears when you choose to delete a font.](https://klaviyo.zendesk.com/hc/article_attachments/28716353800603)
3. Select ****Delete****.

Once a custom font is deleted, any forms in Klaviyo that currently use the custom font will immediately revert to the fallback font. If you re-add the font, those forms will begin using it again.

## Using custom fonts in the sign-up form builder

To use your custom font in a sign-up form, simply edit the text in the form preview:

1. Navigate to the ****Sign-up forms**** tab.
2. Find the form you want to edit and click the 3 dots next to it, then select ****Edit form****.
3. In the form preview, select the text you'd like to edit.
4. In the Text menu on the right, highlight the text.
5. Use the fonts dropdown at the top to select your custom font. Note that fonts from the **Your Fonts** section of your account will appear at the top of the list.

   While editing, your custom font will appear in the canvas (e.g., the editing preview), but not in the panel on the left side. The left-side panel will display your fallback font instead of the custom font.
6. Once you're satisfied with your changes, click ****Publish**** to make them live.

![Clicking on the heading text in an example sign-up form, highlighting it in the text menu, and changing its font.](https://fast.wistia.com/embed/medias/xo0pkanu5d/swatch)

## Site font impacted by Klaviyo.js

Klaviyo [active On site tracking](https://help.klaviyo.com/hc/en-us/articles/115005076767#h_01HADAYAABB803T7AGQ6G3HM6B) (Klaviyo.js), must be installed manually or through your ecommerce integration in order to publish Klaviyo sign-up forms on your website. If you have only loaded some font variations, Klaviyo.js loads the remaining variations in your library when it's injected into your site. Because of this, the fonts on your site may be slightly edited in this process, such as a change in the weight of the site's header.

There are 2 options for resolving any changes made to your fonts by Klaviyo.js. You can either:

- Delete the relevant fonts from your Klaviyo font library.
- Update the CSS on your site's header so that it doesn't get overwritten when Klaviyo.js loads the additional variations.

  Because this option would require in-depth knowledge of CSS, you may require the assistance of a developer. Klaviyo cannot offer assistance on adjusting your site's CSS, however we do have a vast [partner network](https://connect.klaviyo.com/).

## Additional resources

- Course: [Creating an effective acquisition strategy using sign-up forms](https://academy.klaviyo.com/creating-an-effective-acquisition-strategy-using-signup-forms)
- [How to host a custom font on your site](https://help.klaviyo.com/hc/en-us/articles/360047999812)