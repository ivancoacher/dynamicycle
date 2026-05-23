---
id: 48461666134939
title: "About the upgrade to Klaviyo's text only editor"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/48461666134939-About-the-upgrade-to-Klaviyo-s-text-only-editor"
section: "Build and use templates"
category: "Content"
category_slug: "content"
klaviyo_updated: "2026-05-11T11:07:01Z"
language: en
---

## ****You will learn****

Learn about Klaviyo's upcoming upgrade to the [text only editor](https://help.klaviyo.com/hc/en-us/articles/12415384810651) used in email templates, including what's changing, what to expect, and how to prepare.

## ****Overview****

Klaviyo is upgrading the text only editor used in email templates. This change improves the reliability and consistency of how your email content is processed, and introduces new features including the Django Tag Builder, a visual tool for adding dynamic tags to your emails.

As part of this rollout, Klaviyo will begin enabling the new editor for a subset of accounts and gradually expand access over time. You'll receive advance notice before any changes are made to your account.

## ****What's changing****

The ****text only editor**** is the editing interface used when editing the text only version of an email. The upgrade replaces the underlying editor with an improved version that handles your email content more consistently and adds new features.

## ****Impact on existing templates****

For almost all accounts, this change will be seamless with no visual differences to your templates. A small number of templates may see minor visual or layout differences after the upgrade. In very rare cases, templates with complex content—such as custom styling, tables, or embedded style tags—may not be fully convertible and you will have the option to convert it to an HTML template instead, preserving your content while giving you direct control over the code.

## ****Preview text****

With our previous text only editor, preview text would have to manually be updated by adding it as HTML. In our new text only editor, there will be a dedicated input field within the editor for adding and editing preview text. If this field is left blank, then the preview text will automatically be set to the first few characters of the actual email content. There is also the option to completely hide preview text so it shows up as blank in the recipients’ inboxes.

## ****What's not changing****

- Your email designs and content are preserved throughout this process.
- You can continue building and editing emails in the text only editor the same way you do today.
- If your template is converted to an HTML template, your content remains intact and can be edited directly.

## ****About source code view****

As part of this upgrade, ****the source code view will be removed**** from the text only editor.

If you need to work with custom HTML in your emails, use a dedicated ****HTML template**** designed for this purpose. The HTML template gives you full control over your code.

If you want to add and edit Django Tags in your text only emails, you can use the new ****Django Tag Builder**** to do so without writing any code.

## ****What to expect during rollout****

The upgrade will happen in stages. Here's what the process looks like:

1. ****Advance notice**** — You'll receive at least 2 weeks of notice via an in-app banner before any changes are made to your account.
2. ****Gradual rollout**** — Changes will be rolled out gradually to accounts over a 2-week period.
3. ****Automatic template conversion**** — When your account is upgraded, Klaviyo will automatically convert your existing text only templates to the new editor.

****HTML template fallback**** — For the small number of templates that contain content the new editor can't process automatically (such as tables or custom style tags), you will have a choice between moving forward with the the text editor upgrade, or converting the entire template to HTML to preserve all of the existing content as you originally designed it. You'll see an in-app notification when this occurs and you will be able to preview the previous version vs. the new version.

## ****How to prepare****

Before the upgrade reaches your account, it's a good idea to review text only templates that may include:

- ****Custom HTML or inline style tags****
- ****Tables****
- ****Heavily customized formatting**** that goes beyond standard text styling

For templates in this category, consider migrating the content to an HTML template proactively, or simplifying the formatting so it converts cleanly.

## ****Additional resources****

- [How to create a text-only email](https://help.klaviyo.com/hc/en-us/articles/12415384810651)
- [Guide to the email template editor](https://help.klaviyo.com/hc/en-us/articles/4407911841435)
- [How to use the HTML block in email templates](https://help.klaviyo.com/hc/en-us/articles/115005254488)