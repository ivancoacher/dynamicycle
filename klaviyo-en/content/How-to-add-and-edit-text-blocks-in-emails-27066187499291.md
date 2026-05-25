---
id: "27066187499291"
title: "How to add and edit text blocks in emails"
source_url: "https://help.klaviyo.com/hc/en-us/articles/27066187499291-How-to-add-and-edit-text-blocks-in-emails"
section: "Getting started with templates"
category: "Content"
category_slug: "content"
klaviyo_updated: "2026-04-21T13:54:37Z"
language: "en"
---
## You will learn

Learn how to add, edit, and style a text block in an email using Klaviyo’s drag-and-drop email editor.

## Add a text block

To add a text block to an email, open any email that uses the drag-and-drop editor (e.g., a flow email, campaign email, or email template). Then:

1. Hover over the **Text** block in the **Content** sidebar.
2. Click on the block and drag it into the canvas.
3. When you’re happy with the block’s placement, release your cursor to drop the block in.

![A user drags a block and drops it into the canvas](https://klaviyo.zendesk.com/hc/article_attachments/28717995348507)

## Edit text

You can edit text directly in the email canvas. (Note that other text fields, like text in button blocks and table blocks, must be edited in the block sidebar, rather than in the canvas.)

1. Click any text block to select it.
2. Double-click the selected text block to access the text editor, then begin typing.

![A user edits the text in a text block](https://klaviyo.zendesk.com/hc/article_attachments/28717995350811)

Klaviyo's email editor uses the UTF-8 encoding standard, which means it supports Latin characters, emojis, double byte characters, and more.

To add copy in a language that uses a right-to-left (RTL) script (e.g., Hebrew), add the following code snippet to the source code of a text block or an HTML block at the top of your template:

```
<style type="text/css">
      p, h1, h2, h3, h4, ol, li, ul { direction: rtl; }
</style>
```

## Styling text

The styling includes choosing your font, font size, color, etc.

Klaviyo recommends setting styles in the main **Styles** tab, rather than manually editing the styles for each text block. This reduces code weight, decreases the likelihood that your email will be clipped, and helps ensure your styles are consistent.

### Add styles for all text in an email

1. From the **Content** sidebar, click ****Styles****.
   ![The Styles tab](https://klaviyo.zendesk.com/hc/article_attachments/28717995352475)
2. In the **Text & Headings** section, choose a font, font size, color, and other styles for your normal text, plus your headings (H1-H4). You can also choose a color and style for links in this tab.
   ![Adding settings for different text styles, like Normal or H1](https://klaviyo.zendesk.com/hc/article_attachments/28717995356315)
3. Click ****Done****.

### Manually add styles within a text block

Use this method sparingly, as it can increase the code weight of your email, which may lead to clipping. Always add your standard styles in the ****Styles**** tab, then make adjustments to individual words or phrases with the text block settings.

To add styles to content within a single text block, like bolding a single word or phrase:

1. Open the text block editor.
2. Highlight the text you’d like to style.
3. Choose style options, like a font, size, or color.

![A user bolds part of a text block](https://klaviyo.zendesk.com/hc/article_attachments/28718023179803)