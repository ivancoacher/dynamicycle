---
id: 28858764961947
title: "Understanding Klaviyo Reviews language and translation settings"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/28858764961947-Understanding-Klaviyo-Reviews-language-and-translation-settings"
section: "Build and use reviews"
category: "Reviews"
category_slug: "reviews"
klaviyo_updated: "2026-04-20T16:49:49Z"
language: en
---

## You will learn

Learn about language, translation, and locale settings for reviews widgets. These settings determine which language your widgets and the review submission form appear in.

## Set a default widget language

By default, all Klaviyo reviews content is in English. To select a different language:

1. Navigate to the ****Reviews**** tab in Klaviyo.
2. Click ****Reviews settings****.
   ![The Reviews settings tab](https://klaviyo.zendesk.com/hc/article_attachments/28858800593179)
3. Select ****General****.
   ![The General section of reviews settings](https://klaviyo.zendesk.com/hc/article_attachments/28858800595611)
4. In the **Select language** menu, choose your preferred language.

Updating the language for Klaviyo reviews affects all of the following:

- Review submission page
- Onsite widgets
  - Star rating widget
  - Review summary widget
  - Review list widget
  - Product reviews widget
  - Featured review carousel widget
  - SEO widget (formerly All reviews widget)

You cannot update the language setting for individual widgets using this method. The selected language applies to all widgets, including those that are already live on your site, and changes are applied immediately.

Updating your language for Klaviyo reviews ****does not**** apply to other Klaviyo features (e.g., custom questions, flows, sign-up forms, consent pages, the content of customer-submitted reviews, etc.). These must be manually translated and edited.

## Set language based on each visitor’s browser settings

Klaviyo can determine a site visitor’s country using their browser settings. To use this information to automatically select a reviews widget language:

1. Navigate to the ****Reviews**** tab in Klaviyo.
2. Click ****Reviews settings****.
   ![The Reviews settings tab](https://klaviyo.zendesk.com/hc/article_attachments/28858800593179)
3. Select ****General****.
   ![The General section of reviews settings](https://klaviyo.zendesk.com/hc/article_attachments/28858800595611)
4. Turn on the ****Set language based on visitor preferences**** toggle.
5. Optional: check the option **If available, use the visitor's shipping location to set language.**
6. Select ****Save changes****.

Reviews widgets can only be translated into the languages shown in the default language dropdown menu. If Klaviyo detects that a site visitor is in a region that isn't yet supported, your default language will be used instead.

Shipping location can only be used on the review submission page. If a visitor’s shipping location is unavailable, the language falls back to their browser settings. If browser settings are not available, the language defaults to the language selected in your Klaviyo Reviews settings.

## Set language programmatically (requires custom code)

This option is only available for custom-coded implementations of Klaviyo Reviews. If you used a drag-and-drop editor to install your reviews widgets, this option is not available to you.

If you have access to a developer, you can implement a custom-coded language selection process for reviews widgets.

All reviews widgets accept a lang parameter, which accepts a [2-letter ISO 639 language code](https://www.iso.org/iso-639-language-code). You only need to apply this parameter to 1 review widget on a page. Once set for 1 widget, all other widgets will use this parameter as well.

When implemented correctly, the language parameter in reviews code looks like this:

`<div id="klaviyo-reviews-all" data-id="{{product.id}}" lang="en"></div>`

### The **lang** parameter and single-page apps

This setting is fetched upon injection of the widget code. In single-page applications, live changes to the **lang** parameter will only take effect if the widget placeholder element is unmounted and remounted.

## Additional resources

- [How to customize content based on language](https://klaviyo.zendesk.com/hc/en-us/articles/115005239028)
- [How to customize review widgets](https://klaviyo.zendesk.com/hc/en-us/articles/16691401577883)
- [How to customize the review submission page](https://klaviyo.zendesk.com/hc/en-us/articles/19481466872859)