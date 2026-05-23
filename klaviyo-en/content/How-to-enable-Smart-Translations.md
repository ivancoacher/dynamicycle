---
id: 38068161225243
title: "How to enable Smart Translations"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/38068161225243-How-to-enable-Smart-Translations"
section: "Build and use templates"
category: "Content"
category_slug: "content"
klaviyo_updated: "2026-05-11T12:54:37Z"
language: en
---

You must have a paid Klaviyo account to use this feature.

Learn how to enable Smart Translations for messages so you can send campaigns and flows in multiple languages based on the language preferences of your audience. Klaviyo can translate email content to 60+ languages.

Localizing your messages is great if you have or plan to expand to an international customer base. Sending emails in each subscriber’s preferred language allows you to reach a wider audience which can increase overall engagement.

### What can be translated?

The following can be automatically translated:

- Text blocks
- Labels
- Alt text

  The following can be manually changed per language:
- Links
- Images

  The following **cannot** be translated:
- Product feed content

****Note:****If you have Shopify Markets enabled, Static Product Blocks can be automatically localized independently of Smart Translations. A ****Localize for recipient**** setting in the product block will dynamically resolve product pricing and currency for each recipient based on their region. Learn more in [How to add a product block to an email](https://help.klaviyo.com/hc/en-us/articles/115000219092).

All of this applies to universal and saved content you’ve added to the template.

****Supported languages****

Klaviyo supports Smart Translations for the languages listed in the table below. We recommend using the BCP-47 code listed next to each language in the **Locale** property to indicate a profile’s preferred language; however, Klaviyo will respect plain-text values (e.g., **English**, **French**) as well.

|  |  |
| --- | --- |
| ****Language**** | ****BCP-47 code**** |
| Afrikaans | af |
| Albanian | sq |
| Amharic | am |
| Arabic | ar |
| Armenian | hy |
| Bengali | bn |
| Bosnian | bs |
| Bulgarian | bg |
| Catalan | ca |
| Chinese (Simplified) | zh |
| Chinese (Traditional) | zh-TW |
| Croatian | hr |
| Czech | cs |
| Danish | da |
| Dari | fa-AF |
| Dutch | nl |
| English | en |
| Estonian | et |
| Farsi | fa |
| Filipino, Tagalog | tl |
| Finnish | fi |
| French | fr |
| French (Canada) | fr-CA |
| Georgian | ka |
| German | de |
| Greek | el |
| Gujarati | gu |
| Haitian Creole | ht |
| Hausa | ha |
| Hebrew | he |
| Hindi | hi |
| Hungarian | hu |
| Icelandic | is |
| Indonesian | id |
| Irish | ga |
| Italian | it |
| Japanese | ja |
| Kannada | kn |
| Kazakh | kk |
| Korean | ko |
| Latvian | lv |
| Lithuanian | lt |
| Macedonian | mk |
| Malay | ms |
| Malayalam | ml |
| Maltese | mt |
| Marathi | mr |
| Mongolian | mn |
| Norwegian (Bokmål) | no |
| Pashto | ps |
| Polish | pl |
| Portuguese (Brazil) | pt |
| Portuguese (Portugal) | pt-PT |
| Punjabi | pa |
| Romanian | ro |
| Russian | ru |
| Serbian | sr |
| Sinhala | si |
| Slovak | sk |
| Slovenian | sl |
| Somali | so |
| Spanish | es |
| Spanish (Mexico) | es-MX |
| Swahili | sw |
| Swedish | sv |
| Tamil | ta |
| Telugu | te |
| Thai | th |
| Turkish | tr |
| Ukrainian | uk |
| Urdu | ur |
| Uzbek | uz |
| Vietnamese | vi |
| Welsh | cy |

Some regional variations are supported, however when machine translating, they will use the machine translation language as specified below

|  |  |  |
| --- | --- | --- |
| ****Language**** | ****BCP47**** | ****Machine Translation Language**** |
| English (Australia) | en-AU | en |
| English (Canada) | en-CA | en |
| English (United Kingdom) | en-GB | en |
| English (Ireland) | en-IE | en |
| English (India) | en-IN | en |
| English (New Zealand) | en-NZ | en |
| English (South Africa) | en-ZA | en |
| German (Austria) | de-AT | de |
| German (Switzerland) | de-CH | de |
| Spanish (Argentina) | es-AR | es-MX |
| Spanish (Chile) | es-CL | es-MX |
| Spanish (Colombia) | es-CO | es-MX |
| Spanish (Peru) | es-PE | es-MX |
| French (Belgium) | fr-BE | fr |
| French (Switzerland) | fr-CH | fr |
| Italian (Switzerland) | it-CH | it |
| Dutch (Belgium) | nl-BE | nl |

If you add an unsupported country variant to a profile (e.g., fr-DE, de-NL), Klaviyo will ignore the country variant and translate to the supported language variant instead.

## Enable translation

Before you can translate content, you must enable the feature in your account settings.

1. Navigate to your organization name in the bottom left corner of your screen.
2. Click ****Settings****.
3. Select ****Account**** > ****Translation****.
4. Toggle on ****Translate messages****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/38069823924507)
5. Choose a property to use to determine a profile’s preferred language.

   - **Locale is used by default, but Country or Language can be used if present.**
6. Click ****Save****.

## Configure languages and catalog locale mappings

After enabling the feature, add languages to use for your translations. Your account language will be added by default.

1. In the **Language** section, click the **Additional languages** dropdown and select whichever language you want to use for your content. Repeat this step for each language you’d like to include.
   1. Choose which of your added languages will be the **Fallback language** for when a customer’s preferred language is unavailable or unknown.
2. In the Catalog locale mapping section, click the Add mapping button and select a default mapping for any country you’d like to regionalize. This mapping will be used to regionalize product feed content when a profile's country is unknown.
   1. This functionality is only supported for the Shopify integration when [Shopify Markets](http://help.klaviyo.com/hc/en-us/articles/45224022467739) in enabled
3. Click ****Save****.

![](https://klaviyo.zendesk.com/hc/article_attachments/45234308021275)

Any languages you add in the Language section will be automatically populated as options when translating templates, campaigns, flows, and universal content. Any locale mappings you add in the Catalog locale mapping sections will automatically be used as the fallback locale for each language when a profile's country is unknown or there is no catalog data for the profile's country.

## Collect preferred language property

The default method for determining a profile’s preferred language is **Locale**. In other words, Klaviyo looks at a location property to determine which language to use for the profile. Some integrations such as Shopify (via Shopify Markets) and Prestashop automatically populate the **Locale** property with location information for customers.

You can also collect a preferred language directly from customers. The **Language** property on someone’s profile does not have a value by default, but one can be collected using several different methods.

- [Sign-up form with a preferred language field](https://help.klaviyo.com/hc/en-us/articles/115005239028#h_01HKSVWD1S6QPRW27NEGSDN288)
- [Manually import profile properties using a CSV import](https://help.klaviyo.com/hc/en-us/articles/1260806293150)
- [Links in an email to update a subscriber's profile](https://help.klaviyo.com/hc/en-us/articles/115005255248)
- [Klaviyo’s Profiles API](https://developers.klaviyo.com/en/reference/profiles_api_overview)

When setting the locale property, we recommend using [BCP-47 codes](https://developer.mozilla.org/en-US/docs/Glossary/BCP_47_language_tag) (e.g., en-GB, es-ES). Alternatively, you may use a country or language (e.g., English, France), but BCP-47 codes offer more control and dialect precision.

Profiles that don’t have a Language property set will receive the original language of the email. For product feeds in Smart Translations, profiles that don’t have a Country property set will receive product data selected in the Catalog locale mapping.

## Do Not Translate

The "Do Not Translate" feature allows you to specify a list of terms, brand names, or phrases that should be excluded from machine translation.

When a machine translation is performed, any term added to this list will remain in the original language, ensuring consistency and brand integrity across all translated content.

You can manage your list of terms in your account settings:[Account Translation Settings](https://www.klaviyo.com/settings/account/translation).

![](https://klaviyo.zendesk.com/hc/article_attachments/45615306764571)

## Translate messages

Learn more about translating messages:

- [How to create a multilingual email campaign](https://klaviyo.zendesk.com/hc/en-us/articles/38069585109787)
- [How to create a multilingual email flow](https://klaviyo.zendesk.com/hc/en-us/articles/38069723835547)
- [How to create a multilingual SMS campaign using Smart Translations](https://klaviyo.zendesk.com/hc/en-us/articles/39896599432347)