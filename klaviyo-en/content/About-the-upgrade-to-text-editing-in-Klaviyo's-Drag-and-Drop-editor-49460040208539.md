---
id: "49460040208539"
title: "About the upgrade to text editing in Klaviyo's Drag and Drop editor"
source_url: "https://help.klaviyo.com/hc/en-us/articles/49460040208539-About-the-upgrade-to-text-editing-in-Klaviyo-s-Drag-and-Drop-editor"
section: "Templates"
category: "Content"
category_slug: "content"
klaviyo_updated: "2026-04-22T14:18:13Z"
language: "en"
---
## ****Overview****

As part of Klaviyo's upgrade to text editing in the Drag and Drop editor, this rollout happens in two stages: first, all newly created templates will use the new editor by default; then, existing templates still using the old text editor will be automatically migrated. This article explains what to expect at each stage.

## ****Stage 1: New templates****

Starting in the next couple weeks, any new email template you create will use the upgraded text editor for text blocks, table blocks, and split blocks. If you clone an existing template, the cloned template will inherit whichever editor the original template was using.

You may notice a banner when opening a new template letting you know it's using the new editor. This banner will be shown temporarily and will be removed after approximately one month.

If you have existing templates still on the old editor, they will continue to work the same as before until Stage 2 of the rollout reaches your account.

## ****Stage 2: Existing templates****

After Stage 1 is complete, Klaviyo will begin migrating existing templates that still use the old text editor. This rollout is gradual — you'll receive at least 2–4 weeks of advance notice via an in-app banner before any changes are made to your account.

### ****How conversion works****

When migration reaches your account, Klaviyo will automatically attempt to convert each text block, table block, and split block in your existing templates:

- ****If the block can be converted**** — it will be upgraded to the new editor automatically, with no action required from you.
- ****If the block cannot be converted**** — this applies to blocks with complex content such as tables, custom styling, or embedded style tags. These blocks will be converted to an HTML block instead, preserving all of your content while giving you direct control over the code.

Note that this applies not just to text blocks, but also to split blocks and table blocks that use rich text editing.

### ****Source code view****

With this change the source code view is being removed from text blocks, table blocks, and split blocks. If you need to edit HTML directly, you can use a dedicated HTML block, which gives you full control over your code. To add dynamic content using Django tags without writing code, use the new Django Tag Builder.

### ****What is changing****

- Source code view is being removed from text, table, and split blocks. You can use our new Django Tag Builder to create personalization tags in these blocks now.
- Table and Split blocks will move to in-canvas text editing. You will no longer edit text in these blocks through the side panel.

![](https://klaviyo.zendesk.com/hc/article_attachments/49460040192411)

### ****What's not changing****

- Your email content and designs are preserved throughout this process. Either as a new text block, table block, or split block - or as an HTML block.
- You can continue building and editing emails the same way you do today, the only difference is that text editing will no longer include source code view.

## ****What to expect during rollout****

1. ****Advance notice**** — You'll receive at least 2–4 weeks of notice via an in-app banner before migration begins on your account.
2. ****Gradual rollout**** — Migration will be rolled out gradually across accounts.
3. ****Automatic conversion**** — Klaviyo will automatically convert your text blocks where possible.
4. ****HTML fallback**** — Blocks that can't be converted will become HTML blocks. You'll be notified in-app when this occurs.

## ****How to prepare****

Before migration reaches your account, review your existing templates for:

- ****Tables**** within text blocks
- ****Custom styling or inline style tags****
- ****Embedded HTML**** or other complex formatting

For templates in this category, consider migrating to an HTML block proactively, or simplifying the formatting so it converts cleanly.

## ****Additional resources****

- [Guide to the email template editor](https://help.klaviyo.com/hc/en-us/articles/4407911841435)
- [How to use the text block in email templates](https://help.klaviyo.com/hc/en-us/articles/32200923751195)
- [About the upgrade to Klaviyo's text only editor](https://help.klaviyo.com/hc/en-us/articles/48461666134939)