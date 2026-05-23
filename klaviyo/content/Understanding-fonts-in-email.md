---
id: 4405396468379
title: "Understanding fonts in email"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/4405396468379-Understanding-fonts-in-email"
section: "Design best practices"
category: "Content"
category_slug: "content"
klaviyo_updated: "2026-04-21T13:54:59Z"
language: en
---

## You will learn

Learn about the opportunities and limitations of using fonts online, and how to send emails that align with your brand.

Looking for information on how to use custom fonts? Learn [how to use custom fonts](https://klaviyo.zendesk.com/hc/en-us/articles/4412748537627).

## How fonts work

Fonts are representations of text, and can be used in print or online media. You may be familiar with some of the more common fonts, like Arial or Times New Roman, but there are thousands of other fonts you can use to communicate and represent your brand.

With online media (like websites or emails), your font options are nearly limitless. However, when you share your creation with someone else, it may not look exactly the same, because not all devices have access to the same fonts.

There are two main ways a device can access and use a font: ****system fonts**** (i.e., fonts stored on the device you’re using) and ****web fonts**** (i.e., fonts loaded from an external server)

### About system fonts

Computers and phones come pre-loaded with a variety of fonts. There are some commonly installed fonts (most devices come with Georgia and Verdana, for example), but devices can vary widely in what they include by default. Fonts that are used by most devices are called “web-safe” fonts.

### About web fonts

Different from web-safe fonts, web fonts are loaded from an external server at the same time as the content you’re viewing. Custom fonts are generally web fonts. If you use a web font, you’ll want to set a web-safe fallback font as well, in case a particular device is unable to load your web font.

### About fallback fonts

When you view anything online, whether it’s a webpage or an email, there’s CSS (code used to style content online) behind the scenes that tells your device which font to display. If your device can’t access the font, it will check the CSS for a “fallback font” (a font, or fonts, selected by the person who created the website or email message, to be used in case the preferred font wasn’t available). Fallback fonts should be [web-safe fonts](https://www.cssfontstack.com/) that most devices can use. They give you more control over how your message appears when someone views it on a device that doesn’t support custom/web fonts.

If there’s no fallback font available, or if the fallback font isn’t supported by the device being used, then the device will use a default font, like Arial or Times New Roman. Default fonts vary widely across devices and apps.

## How fonts work in email

Some email clients support web fonts, but others don’t. When someone opens your email in an inbox or device that does not support web fonts, they will see a default font used instead. You can control which system fonts are used as backups by setting a fallback font.

If someone opens your email on a device that supports web fonts, it will load the font from the URL provided in your email’s CSS. If the device is able to access the font, it will display it; otherwise, it’ll move on to the fallback fonts.

The following email clients support web (custom) fonts:

- Apple Mail
- iOS Mail (the default email browser on iOS)
- Google Android (except Android 2.3, which doesn’t support the `@import` method used by Google and Adobe fonts)
- Samsung Mail (Android 8.0)
- Outlook for Mac

Note that Gmail, one of the biggest email clients, does not generally support web fonts. However, there is one exception: Gmail does support Roboto.

## Optimizing fonts in your emails

The best way to ensure your email looks consistent across devices is to use a web-safe font. Klaviyo’s default fonts are generally web-safe. Find the fonts Klaviyo provides in:

- ****Content > Images & Brand >********Brand Assets****
- The ****Styles**** tab of your emails
- The ****Styles**** section of any email blocks containing text
- The ****Styles**** tab of the signup form editor

Three of the fonts Klaviyo provides are not supported by some devices: Century Gothic, Tahoma, and Apple Black. These fonts do not come preinstalled on iOS devices (e.g., iPhones), so if you use these fonts, they may appear as the inbox’s default font when viewed on an iOS device.

### Tips for using custom fonts

If you prefer to use a custom font, use the tips below to ensure that your emails look well-designed across devices.

#### Use fallback fonts

Select a web-safe [fallback font](https://help.klaviyo.com/hc/en-us/articles/4412748537627#01FVFRR1PC7ARCZ66Z6SM3CNPR) that matches your custom font as closely as possible. You can select a fallback font from Klaviyo’s default fonts when configuring the custom font.

#### Use text in images

While an all-image email can hurt your deliverability, you can strategically use a combination of text in images and text in text blocks to create an email that aligns with your brand. Choose a custom, branded font for your headings and calls to action (CTAs), and pair it with a web-safe font to use for your body text.

Use images containing your branded font for select text, and make sure to [add alt text](https://help.klaviyo.com/hc/en-us/articles/360034711931-Best-Practices-for-Building-Accessible-Emails-and-Forms-#basic-email-design3) when you add the images to your email. Then, apply the web-safe font to the rest of the text in your email. The result is a branded email that matches your site, while also being accessible for your subscribers’ inboxes.

#### Test thoroughly

Regardless of which methods you choose, [test your emails](https://help.klaviyo.com/hc/en-us/articles/115005081907-How-to-Preview-and-Send-Test-Emails-in-Klaviyo) thoroughly, especially when using a new design. Send the email to yourself on multiple devices to ensure you’re happy with how it appears on each. You can also make use of email testing programs like Litmus or Email on Acid to test using a broader range of devices.