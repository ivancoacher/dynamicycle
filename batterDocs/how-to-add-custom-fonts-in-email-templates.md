<h1>How to add custom fonts in email templates</h1>

## You will learn

Learn how to add new fonts to the Klaviyo email template editor so that your emails match your brand style. In this article, you’ll also learn about the tradeoffs when using custom fonts, and how to choose a font supported by the widest range of inboxes.

You can use Google Fonts, Adobe Typekit, or imported (i.e., self-hosted) fonts in your emails. However, keep in mind that only certain email inboxes support custom fonts, and many popular clients (like Gmail and Yahoo) do not.

This article will walk you through how to use custom fonts in your email templates, not your sign-up forms. For information on adding custom fonts to your sign-up forms, head to our article on [custom fonts in sign-up forms](https://help.klaviyo.com/hc/en-us/articles/360047955672).

![](https://fast.wistia.com/embed/medias/udi1mz4yzz/swatch)

## Key terms

- ****Custom font****
  Any font that isn’t provided by default in the Klaviyo editor
- ****Web font****
  A custom font that must be loaded from an outside source
- ****Web-safe font****
  A font that is stored locally on most devices, and therefore doesn’t need to be loaded from an outside source in order to display
- ****Fallback font****
  A web-safe font that is used in inboxes that don’t support your custom font

## Custom font support and limitations

Custom fonts can help keep your marketing cohesive, aligning your email content with your ecommerce site. However, web fonts (i.e., fonts loaded from an outside source, rather than available from the device’s storage) may not render as expected on all devices or email clients. Klaviyo’s default fonts are pre-installed on the vast majority of computers and devices, so you can deliver a consistent experience for all subscribers.

Email clients that do support web fonts include:

- Apple Mail
- iOS Mail (the default email browser on iOS)
- Google Android (except Android 2.3, which doesn’t support the @import method used by Google and Adobe fonts)
- Samsung Mail (Android 8.0)
- Outlook for Mac

### Custom fonts in Gmail and other unsupported inboxes

Your recipients who use Gmail (or other inboxes that don’t support custom fonts) may see your fallback font (which you can set in your email template), rather than the custom font you choose. To avoid this, consider selecting a web-safe custom font, which is available on most devices regardless of their support for web fonts.

[Find web-safe fonts here](https://www.cssfontstack.com/), along with a breakdown of support by device.

## Add a new custom font in the email template editor

To add a custom font to an email template:

1. Open a text block in your template, or your template's ****Styles**** tab.
2. In the font dropdown, click ****Add Font**** at the bottom of the dropdown menu.
3. In the modal that appears, choose ****Google Font****, ****Adobe Font****, or ****Import**** ****Font****, depending on your font’s source.
4. Follow the instructions in the sections below for your font type ([Google](#01FVFRR1PCNVDQWQGF9AFEPXR0), [Adobe](#01FVFRR1PCNGNQF4TN1SW921AV), or [Imported Fonts](#01FVFRR1PCGE46QEC5C4BMP7AJ)).

Once you’ve added a font to your email templates, it will be available for all other templates as well as your sign-up forms.

![](https://fast.wistia.com/embed/medias/2opf7nk0gl/swatch)

### Add additional font variants to an existing custom font

You can always edit, delete, or update the selected variations for your custom fonts under ****Brand & Images > Fonts****.

#### Update an existing font

To select additional variants for a custom Google or imported font you've already added:

1. Navigate to ****Content > Images & brand**** in Klaviyo.
2. Click ****Fonts****.
3. Find the font you'd like to edit beneath **Your Fonts**.
4. In that font's card, click the three dots in the top right corner.
5. Click ****Edit**** in the menu that appears.
6. Click ****# font variants selected**** to expand the list of font variants.
7. Select any additional variants you'd like to add.
8. Click ****Update Font****.

You cannot add variants to an Adobe font after uploading it, since the variants are built in to your Typekit link.

If you receive the error message **A font with this name already exists**, follow the steps above to edit the existing version of the font, rather than re-adding it.

#### Delete a font

1. Navigate to ****Content > Images & brand**** in Klaviyo.
2. Click ****Fonts****.
3. Find the font you'd like to edit beneath **Your Fonts**.
4. In that font's card, click the three dots in the top right corner.
5. Click ****Delete**** in the menu that appears.

Any messages in Klaviyo that currently use the custom font will immediately revert to the fallback font. If you re-add the font, those email will begin using it again.

### Add a Google font

To add a Google Font:

1. Type the name of the Google font you’d like to use.
2. Choose a fallback font.
3. Click ****Add Font****.

### Add an Adobe font

Adobe fonts are only available to users who have an active Adobe Fonts subscription. To add an Adobe font:

1. Click ****Adobe Font.****
2. Paste in your CSS Address. The address should follow this format: <https://use.typekit.com/123ABC>.
3. Choose a fallback font.
4. Click ****Add Font****.

### Add an imported font

Imported fonts, sometimes called self-hosted fonts, are recommended only for senders who have access to a developer. You cannot directly upload the font file to Klaviyo. If you don't have access to a developer team, we recommend finding a Google or Adobe font that is similar to your desired font.

To use an imported font:

1. Host the font on your servers or using a font-hosting service. Make sure to enable Cross-Origin Resource Sharing (CORS) by setting the Access-Control-Allow-Origin header to \*, so the font can be accessed by your recipients’ inboxes. [Learn more about CORS.](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)
2. Once you’ve successfully hosted the font, click ****Import Font**** in the **Add Font** modal and paste your hosting URL into the **Source address** field.
3. Add in your font’s name, weight, and style to the appropriate fields.
4. Choose a fallback font.
5. Click ****Add Font****.

### About fallback fonts

With all types of custom fonts, you’ll need to select a fallback font. This font will appear for those recipients using clients that don’t support your custom font. Choose a font from the list of available options that is similar in style to your custom font.

![Fallback font options](https://klaviyo.zendesk.com/hc/article_attachments/28705637660827)

For example, if you use Poppins (a Google font) as your custom font and Arial as your fallback font, email recipients will see the following fonts:

- Recipients who open your email in a browser that supports web fonts (e.g., Apple Mail, iOS Mail) will see Poppins
- Recipients who open your email in a browser that does not support web fonts (e.g., Gmail) will see Arial

## Apply a custom font

Once you’ve set up a custom font, you can apply it to any text in your template, including:

- In your main template styles
- In any block’s styles
- To a specific piece of text in a text block
- To button blocks, product blocks, and any other block types containing text

To apply a custom font in a text block:

1. Select the text block that contains the text that you'd like to apply the font to.
2. Highlight the specific text you’d like to apply the font to.
3. Select the custom font from the dropdown.

![Apply a custom font](https://klaviyo.zendesk.com/hc/article_attachments/28705664490395)

For all other block types, or for block and template styles, select the font from the appropriate dropdown.

![Apply custom font in styles tab](https://klaviyo.zendesk.com/hc/article_attachments/28705637661851)

In table blocks and split blocks, your custom font will appear in the canvas (e.g., the editing preview), but not in the panel on the left side. The left-side panel will display your fallback font instead of the custom font.

## Preview your custom fonts

Once your template is ready, send yourself a preview email by clicking ****Preview & test > Send Test****. Try opening the message on a variety of devices to see how it will appear to different recipients. You can also use a tool like [Email on Acid](https://www.emailonacid.com/) to preview across a wider variety of devices.

## Additional resources

- [Guide to the email template editor](https://help.klaviyo.com/hc/en-us/articles/4407911841435-Guide-to-the-Email-Template-Editor-new-editor-)
- [Understanding fonts in email](https://klaviyo.zendesk.com/hc/en-us/articles/4405396468379)
