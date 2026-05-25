---
id: "115005082687"
title: "How to insert preview text into an email"
source_url: "https://help.klaviyo.com/hc/en-us/articles/115005082687-How-to-insert-preview-text-into-an-email"
section: "Getting started with templates"
category: "Content"
category_slug: "content"
klaviyo_updated: "2026-04-21T13:54:20Z"
language: "en"
---
## You will learn

Learn what preview text is, where it appears in your emails by default, and how to insert it into the body of your emails.

## About preview text

Preview text is one of the first things recipients see when an email reaches their inbox. It is displayed in the inbox after the subject line of an email and is usually pulled from the first line of text within the body of an email.

![In a Gmail inbox, the preview text portion of an email is highlighted](https://klaviyo.zendesk.com/hc/article_attachments/28720758454939)

There are 2 main ways you can use preview text to enhance your emails:

1. Use preview text to summarize the email.
2. Use preview text to complement your subject line.

If you do not specifically insert preview text, inboxes will automatically pull it from the first line of text within an email -- this means that ALT text, your navigation bar, etc. could be pulled as the preview text, so it's best to specify what exactly you want your preview text to display. To learn more about how to strategically use preview text, [head to the Klaviyo Blog](http://www.klaviyo.com/blog/how-to-use-preheader-text).

This feature is only supported in Klaviyo's drag and drop templates. For custom HTML templates (including [custom HTML templates with drag-and-drop support](https://help.klaviyo.com/hc/en-us/articles/115005254188-Import-a-Custom-HTML-Template-with-Drag-and-Drop-Support)), your email designer should insert your desired preview text into the beginning of the email's code. For text-only emails, the very beginning of your email is used as preview text.

## Add preview text to a flow email

To insert preview text for a flow email on the email preview screen:

1. Open the flow containing the email you'd like to edit.
2. Click the flow message to open the **Email details** sidebar.
   ![preview1.jpg](https://klaviyo.zendesk.com/hc/article_attachments/38062196975387)
3. Under **Subject and sender**, click ****Edit**** from the content sidebar.
4. In the **Preview text** field, add your desired preview text.
   ![preview2.jpg](https://klaviyo.zendesk.com/hc/article_attachments/38062169938587)

## Add preview text to a campaign email

To insert preview text for a campaign on the email preview screen:

1. Open the campaign you'd like to edit.
2. Click ****Next****.
3. In the **Preview text** field, add your desired preview text.
   ![preview3.jpg](https://klaviyo.zendesk.com/hc/article_attachments/38062196976411)

## Preview text in the inbox

The **Preview Text** input automatically adds spacers, so only the preview text you enter displays in your customers' inboxes.

![A Gmail inbox with one message with the subject line Things your boss wants you to know and Preview Text Give 'em the numbers](https://klaviyo.zendesk.com/hc/article_attachments/28720770371995)

Different devices and email clients have different limits on the amount of preview text characters displayed, with smaller screens displaying fewer preview characters. Keep this in mind, and keep preview text concise. Here are the character limits broken down by email client:

![Preheader character limits listed by email client, between 34 for Gmail iOS and 236 for Outlook.com](https://klaviyo.zendesk.com/hc/article_attachments/28720758448795)
**Image via [Email on Acid](https://www.emailonacid.com/blog/article/email-development/tips-for-coding-email-preheaders)**

Gmail may remove commas within a set of numbers from your preview text. For example, 10,000 will be converted to 10000 in Gmail's preview.

## Display preview text inside your emails

In some cases, you may want to display your preview text inside the body of your template. You can reference any preview text you set on the email preview screen using following tag:

```
{% render_variable preview_text %}
```

Paste the tag into any text block in your template.

## Hide preview text

If you want to completely hide any preview text and have only your subject line appear in your customer's inboxes, add the code snippet below to the very top of your email. This code pushes your email content past the preview text viewing area, so it will appear blank.

1. Add an HTML block to the very top of your email, above all other content.
2. Add the following code snippet:

   ```
   <div style="display: none; max-height: 0px; overflow: hidden;">͏ &zwnj;
       &nbsp; &shy; ͏ &zwnj; &nbsp; &shy; ͏ &zwnj; &nbsp; &shy; ͏ &zwnj; &nbsp; &shy; ͏ &zwnj; &nbsp; &shy;
       ͏&zwnj; &nbsp; &shy; ͏ &zwnj; &nbsp; &shy; ͏ &zwnj; &nbsp; &shy; &zwnj; &nbsp; &shy; ͏ &zwnj; &nbsp;
       &shy; ͏ &zwnj; &nbsp; &shy; ͏ &zwnj; &nbsp; &shy; &zwnj; &nbsp; &shy; ͏ &zwnj; &nbsp; &shy; ͏ &zwnj;
       &nbsp; &shy; ͏ &zwnj; &nbsp; &shy; &zwnj; &nbsp; &shy; ͏ &zwnj; &nbsp; &shy; ͏ &zwnj; &nbsp; &shy;
       ͏&zwnj; &nbsp; &shy; ͏ &zwnj; &nbsp; &shy; ͏ &zwnj; &nbsp; &shy; ͏ &zwnj; &nbsp; &shy; ͏ &zwnj; &nbsp;
       &shy; &zwnj; &nbsp; &shy; ͏ &zwnj; &nbsp; &shy; &zwnj; &nbsp; &shy; ͏ &zwnj; &nbsp; &shy; ͏ &zwnj;
       &nbsp; &shy; ͏ &zwnj; &nbsp; &shy; ͏ &zwnj; &nbsp; &shy; ͏ &zwnj; &nbsp; &shy; &zwnj; &nbsp; &shy;
       ͏&zwnj; &nbsp; &shy; ͏ &zwnj; &nbsp; &shy; ͏ &zwnj; &nbsp; &shy; ͏ &zwnj; &nbsp; &shy; ͏ &zwnj; &nbsp;
       &shy; ͏ &zwnj; &nbsp; &shy; ͏ &zwnj; &nbsp; &shy; &zwnj; &nbsp; &shy; ͏ &zwnj; &nbsp; &shy; ͏ &zwnj;
       &nbsp; &shy; ͏ &zwnj; &nbsp; &shy; ͏ &zwnj; &nbsp; &shy; ͏ &zwnj; &nbsp; &shy; ͏ &zwnj; &nbsp; &shy;
       ͏&zwnj; &nbsp; &shy;
   </div>
   ```
3. Save the HTML block.

When your emails hit the inbox, customers will only see your subject line.

![A Gmail inbox shows an email with a subject line, but no preview text](https://klaviyo.zendesk.com/hc/article_attachments/28720758451867)

## Additional resources

- [Message personalization reference](https://klaviyo.zendesk.com/hc/en-us/articles/115005084927)
- [Templates and design glossary](https://klaviyo.zendesk.com/hc/en-us/articles/14904583929755)