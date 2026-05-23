---
id: 32200923751195
title: "How to use a text block in an email"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/32200923751195-How-to-use-a-text-block-in-an-email"
section: "Build and use templates"
category: "Content"
category_slug: "content"
klaviyo_updated: "2026-05-11T11:00:27Z"
language: en
---

## You will learn

Learn how to use text blocks in Klaviyo’s email template editor, including how to style them, add personalization tags, and use AI to draft and revise your copy.

## Add a text block to a template

1. Within the email template editor, locate the ****Text**** block under **Content**.
2. Drag the block into the email canvas and drop it wherever you’d like it to appear.
   ![A user drags a text block and drops it into the canvas](https://klaviyo.zendesk.com/hc/article_attachments/32200923731611)
3. Double click within the text field to begin editing the text.

If you write your copy outside of the Klaviyo editor (for example, in Google Docs or Microsoft Word), make sure to paste as plain text when pasting your text into the editor. Use Command+Shift+V (Mac) or Ctrl+Shift+V (Windows) to paste as plain text. Otherwise, certain style tags will be pasted in along with the text, which can cause design issues.

## Use AI to revise content

Klaviyo’s AI revision tool can help cure writer’s block, improve existing drafts, or adjust copy for different audiences. This feature is only available on paid accounts.

1. Within any template, select a text block that contains text you’ve written.
2. Click ****Revise text****.
   ![The AI Revise text button](https://klaviyo.zendesk.com/hc/article_attachments/32200923734171)
3. Write your own prompt or select from the default options.
   ![Text revision prompt options](https://klaviyo.zendesk.com/hc/article_attachments/32200938549019)
4. Select ****Generate****.
5. Toggle between the 3 generated options.
6. Once you’ve selected one you’d like to use, click ****Insert****.

## Style a text block

There are 2 ways to style a text block:

- [Using the email’s ****Styles**** tab](#h_01JFWG39EDKM7KAJX700RVK1B8), which sets style defaults for the entire email (recommended)
- [Using the block’s formatting menu](#h_01JFWG39EDCTPGX7C33BEVJBY0)

As a best practice, use the ****Styles**** tab first to apply formatting to all your blocks, then make small tweaks as needed within individual blocks. Following this process results in:

- Email designs that are easier to reuse
- Lower code weight (i.e., less chance of [email clipping](https://help.klaviyo.com/hc/en-us/articles/115000591251))
- More consistent styles with less manual editing

### Apply email-level styles

1. Navigate to the main ****Styles**** tab.
   ![The main Styles tab](https://klaviyo.zendesk.com/hc/article_attachments/32200938550299)
   - You may first need to click the back arrow to exit out of a block you’re currently editing. The main **Styles** tab is different from a block’s **Styles** tab.
     ![A text block's Styles tab](https://klaviyo.zendesk.com/hc/article_attachments/32200938550683)
2. Scroll to **Text and headings**.
   ![The Text and headings section](https://klaviyo.zendesk.com/hc/article_attachments/32200923739163)
3. Choose settings for your **Body** text (i.e., your default paragraph formatting).
4. Select a different text style from the menu (e.g., Heading 1, Heading 2, etc.) and select styles for it.
   ![The text styles dropdown](https://klaviyo.zendesk.com/hc/article_attachments/32200923739931)
5. Repeat this process for all the text styles. As a best practice, use:
   - **Body** for most of your text
   - **Heading 1** for your most important headings
   - **Heading 2** for subheadings
   - Etc.

### Apply block-level styles

1. Select a text block within your email.
2. Double click within the text field to open the styles menu.
3. Highlight the text you’d like to adjust. You can highlight all the text within the block, or just a portion of it.
4. Within the formatting bar at the top of the canvas, choose a text style (e.g., Body, Heading 1) to apply the styles you set in your main **Styles** tab, or manually select a font, font size, color, and more.
   ![Additional text formatting options](https://klaviyo.zendesk.com/hc/article_attachments/32201199886363)

## Add personalization to emails

Personalization tags are a great way to connect with your subscribers and make every email feel intentional and unique. To add personalization tags:

1. Add a text block or locate an existing one in your email template.
2. Double click to open the formatting menu.
3. Click the personalization icon on the right side of the menu.
   ![The personalization icon](https://klaviyo.zendesk.com/hc/article_attachments/32200923747483)
4. Use the **All types** menu to select a type (e.g., Profile, Organization, etc.), search by property name, or scroll through the options.
5. Select a personalization tag.
6. In the **Set up** modal, optionally add a default value and choose capitalization.
7. Click ****Insert****.

The personalization menu offers certain limited personalization options. To add more complex personalization (e.g., event data, catalog tags, and more), learn more about [message personalization](https://help.klaviyo.com/hc/en-us/articles/4408802648731).

## Text blocks and RTL languages

To add copy in a language that uses a right-to-left (RTL) script (e.g., Hebrew), add the following code snippet to an HTML block at the top of your template:

```
<style type="text/css">
      p, h1, h2, h3, h4, ol, li, ul { direction: rtl; }
</style>
```

This will apply RTL formatting to all text blocks in the email.

## Supported characters

Klaviyo's email editor uses the UTF-8 encoding standard, which means it supports Latin characters, emojis, double byte characters, and more.

## Additional resources

- [How to insert personalization into text blocks](https://help.klaviyo.com/hc/en-us/articles/4408810654235)
- [How to preview and send test emails in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115005081907)
- [Guide to the email template editor](https://help.klaviyo.com/hc/en-us/articles/4407911841435)