---
id: "115000591251"
title: "Why is my email being clipped?"
source_url: "https://help.klaviyo.com/hc/en-us/articles/115000591251-Why-is-my-email-being-clipped"
section: "Template troubleshooting "
category: "Content"
category_slug: "content"
klaviyo_updated: "2026-05-15T10:22:21Z"
language: "en"
---
## You will learn

Learn how clipping works and what you can do to avoid it.

Clipping occurs in Gmail inboxes when you send a message that exceeds a certain size, which can vary based on the device used to open the email. If your email is being clipped, you can skip ahead to the section on [Reducing an email's size](#h_01FYA0HM50A4JSQ7APRQMY04C0) for tips on avoiding Gmail clipping.

## About Gmail clipping

Clipped emails are undesirable from a marketing standpoint. Additionally, when an email is clipped, the tracking pixel (used to calculate open rate) will also be clipped, so opens will not be tracked correctly.

If you are concerned about the size of your emails and want to ensure opens are tracked correctly, [move the tracking pixel to the top of your emails](https://help.klaviyo.com/hc/en-us/articles/360049695831).

The size limit for emails varies by device.

- ****Desktop****
  On desktop devices, the email size limit is generally 102 KB.
- ****Mobile****
  On mobile devices, the email size limit can vary, ranging from around 20 KB on iOS to around 75 KB on other mobile devices.

The 20 KB limit in Gmail’s iOS app is applied inconsistently. Learn more about [clipping and Gmail for iOS](https://www.emailonacid.com/blog/article/email-development/gmail_ios_app_email_clipping/).

To avoid clipping, ensure that your email code is less than 102 KB once sent. This limit includes all text, styling, links, and any other HTML content; it does not include large image sizes. If a large proportion of your subscribers open emails in Gmail’s iOS app, which has a smaller size limit, consider moving your tracking pixel to the top of your emails.

Your message may also be clipped if you send multiple messages to your inbox with the same subject line. To avoid this, [send a direct email](https://help.klaviyo.com/hc/en-us/articles/115005246328) with a unique subject line.

****What it looks like when a message is clipped****

If your email has been clipped, recipients will see a message like the one below:

![A message in Gmail indicating the email has been clipped](https://klaviyo.zendesk.com/hc/article_attachments/28713332817051)

When recipients click ****View entire message****, your full email will open in their web browser.

The **View entire message** link leads to a version of your email created by Gmail with all `<style>` tags removed. In this version, content alignment, column styles, table styles, and other style elements may be removed entirely or appear differently than intended.

****Large images don't cause clipping****

Image size does not impact an email's risk of clipping, since images are loaded from an external source (e.g., your Klaviyo Brand Library or your website). The code used to display an image in an email contributes to the message size, but the size of the image file does not.

## Check your email’s size

When you preview an email, Klaviyo provides an estimate of the message’s size in a recipient’s inbox, along with its risk of being clipped.

Check your email's size periodically as you build it, as well as when your email is completed and ready to send.

To check an email’s size:

1. Navigate to an email in Klaviyo (i.e., a campaign email, flow email, or email template).

   Klaviyo recommends adding your template to a campaign or flow before checking its size. This allows us to include the impact of UTM parameters in the estimate of your email’s size.
2. In the email editor, click ****Preview & test****.
3. Review the **Email Size** section of your preview modal to understand the likelihood it will be clipped.
   ![The Gmail clipping warning in the inbox](https://klaviyo.zendesk.com/hc/article_attachments/28713327212955)
4. (Optional) If your email contains a large amount of dynamic content (e.g., profile or event data, conditional statements, etc.), preview with more than one profile. The clipping estimate may change, as the dynamic content included for each person varies slightly.

### Understanding clipping risk

Depending on your email’s size, Klaviyo provides an estimate of your risk of Gmail clipping. Note that this is just an estimate; the final size of your message may vary slightly.

- ****<85KB:**** Your email is not at risk of clipping in Gmail.
- ****85KB - 95KB:**** Your template might be at risk of clipping in Gmail.
- ****>95KB:**** Gmail clipping is likely. Consider [reducing the size of your message](#h_01FYA0HM50A4JSQ7APRQMY04C0) or [moving your tracking pixel to the top of your email](https://help.klaviyo.com/hc/en-us/articles/360049695831) to ensure that you accurately track email opens.

## Reduce an email's size

While the quickest way to reduce your email’s size is to remove some of your content, you can also make many small improvements without sacrificing any content.

****Minimize desktop- or mobile-only blocks****

When you include a desktop- or mobile-only block in an email, that block’s code is included in every email send. When someone opens your email, our code will identify what type of device they are viewing on, and determine whether to show or hide the block.

If your email is being clipped, minimize the number of blocks that are set to display on just one device type, and use a block set to display on both ****Desktop & Mobile**** instead.

****Avoid header/link bar blocks****

Because the header/link bar block has many styling options and dynamically adjusts to desktop and mobile devices, it is a code-heavy block.

If you’re using this type of block and find that your email is getting clipped, replace it with an image block containing your logo followed by a text block for your links.

****Enable embedded styles****

If you [disabled embedded styles](https://help.klaviyo.com/hc/en-us/articles/360049848692) for your emails in your account settings, this can increase email size. Navigate to ****Account > Settings > Email > CSS Optimization**** to confirm that **Enable embedded styles** is checked. If not, check this box to make your email less likely to be clipped.

****Remove section background images****

If you added a background image for a section, consider removing it to decrease the size of your message.

****Remove unnecessary styles****

If you copy and paste text from an external source (like Google Docs or Microsoft Word) into a Klaviyo text block, the text you pasted in may include some extra styling as well. You can check this by viewing the ****Source code**** area of a text block. If there is extra formatting, simply highlight the text and remove it.

Alternatively, use ****Ctrl+Shift+V**** or ****Cmd+Shift+V**** when pasting in new content to paste as plain text and avoid adding unnecessary styles.

****Consolidate blocks and sections****

Where possible, consolidate multiple blocks, sections, and column layouts with similar styles into one. For example, a set of 4 small text blocks with the same font style, color, and size will contribute more to your email's code weight than a single large text block.

Similarly, if your template contains many sections or column layouts, try to combine similar ones. If you have 2 two-column layouts in a row, try combining the content into just 1 two-column layout.

Having trouble identifying the block(s) contributing the most to your email's size? Clone your template to create a test version, then delete blocks and sections from it one at a time. After deleting a block, preview your message to see how much the size has decreased, and note the largest drops.