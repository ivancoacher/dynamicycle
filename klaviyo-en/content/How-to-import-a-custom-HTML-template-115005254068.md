---
id: "115005254068"
title: "How to import a custom HTML template"
source_url: "https://help.klaviyo.com/hc/en-us/articles/115005254068-How-to-import-a-custom-HTML-template"
section: "Advanced template design"
category: "Content"
category_slug: "content"
klaviyo_updated: "2026-04-21T13:54:23Z"
language: "en"
---
## You will learn

Learn how to import a custom HTML template into Klaviyo.

We only recommend using custom HTML for technically savvy marketers, or for anyone who has access to a developer. While our product does support custom HTML, our support team cannot help you build out your custom templates beyond offering the general guidance covered in this documentation. To maintain the security of your data, Klaviyo's support team is not able to open your HTML files.

## Upload a custom HTML template

Custom HTML templates must be .html files and must include an unsubscribe link (i.e., an {% unsubscribe %} or {% unsubscribe\_link %} tag). Learn more about [unsubscribes in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115005078267).

1. Navigate to ****Content > Templates****.
2. Select the ****Email templates**** tab.
3. Click ****Import****.
4. Enter a name and upload the HTML file of your template.
5. Upload any images or assets referenced in your HTML.
6. Click ****Import Template****.

Exporting a template built in Klaviyo's drag and drop editor and then importing it back into Klaviyo is not recommended, and can cause problems with the template's functionality.

****Removing unsupported template tags and variables****

When you export a template from a different email service provider, it may contain tags and variables that aren’t supported by Klaviyo. Before you import your HTML file, remove those tags (and, if needed, replace them with [Klaviyo personalization tags](https://help.klaviyo.com/hc/en-us/articles/4408802648731)).

For example, see the message and HTML below. This message was exported from another email service provider and contains tags for the current year, a company’s address, and more. These external tags are not compatible with Klaviyo.

![A template with unsupported tags](https://klaviyo.zendesk.com/hc/article_attachments/28716302197275)

![The HTML of a template that includes unsupported tags](https://klaviyo.zendesk.com/hc/article_attachments/28716302194331)

Klaviyo template tags are contained within curly brackets. Variables are surrounded by two pairs of curly brackets (e.g., `{{ first_name }}`), and template tags are surrounded by a pair of curly brackets and percent symbols (e.g., `{% unsubscribe %}`). If the template tags and variables in your template are denoted by other characters, Klaviyo will not support them.

### Add images and attachments (optional)

You can reference images and attachments by uploading a zip file that includes your attachments and referencing them by their filename within your template.

When you click to import your template, these images and assets are automatically added to our CDN and their references are updated within your template.

## Add hidden preview text to a custom HTML template

If you’d like to set the preview text for a custom HTML template (rather than letting inboxes pull preview text from your message content), add the code block below to your template. This code should be added immediately after the opening `<body>` tag of your template.

```
<div style="display:none; font-size:1px; line-height:1px; max-height:0px; max-width:0px; opacity:0; overflow:hidden;">
Insert preview text here.
</div>
```

## Emojis and custom HTML templates

As of February 2024, all emojis are supported in all Klaviyo email editors (i.e., the drag-and-drop editor, hybrid editor, text-only editor and custom HTML editor).

## Additional resources

- [Troubleshooting custom CSS, JavaScript, and HTML in Klaviyo](https://klaviyo.zendesk.com/hc/en-us/articles/115005254488)
- [How to import a custom HTML template with drag and drop support](https://klaviyo.zendesk.com/hc/en-us/articles/115005254188)