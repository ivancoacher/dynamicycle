---
id: "29910716707355"
title: "How to change compliance keyword responses and languages"
source_url: "https://help.klaviyo.com/hc/en-us/articles/29910716707355-How-to-change-compliance-keyword-responses-and-languages"
section: "Understanding SMS compliance settings"
category: "SMS"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-21T13:54:38Z"
language: "en"
---
## You will learn

Learn how to configure the language and responses compliance keyword settings in Klaviyo. These settings help you personalize replies to your audience in each country.

This information is intended solely for educational and informational purposes and should ****not**** be construed as legal advice. The content provided is general in nature and may not reflect the most up-to-date information. Klaviyo strongly advises consulting with a qualified legal counsel to ensure your compliance with applicable laws and regulations in connection with your use of our services.

## Before you begin

Please note the following about compliance keywords:

- You cannot edit the response for certain words in specific countries:
  - United States: STOP and START in English cannot be edited.
  - Canada: STOP, START, and INFO in English cannot be edited.
- Responses are tied to both a country and language.
  - The only exception is for English responses when you use a toll-free number for both the United States and Canada.
- The available languages vary based on the country,
  - Klaviyo supports all the official languages, and English, in each country.

For instance, English is available for every country, while French is currently only available in Canada.

Additionally, changing keyword responses in one country does not automatically update it in the same language for another country. For example, if you change the response of HELP for Ireland, it does not change the same response for the United States.

See this article on [understanding compliance keywords in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/29928896469531) for more information.

## Configure compliance keywords

There are a few settings you can change for SMS compliance keywords, such as:

- A keyword’s response message
- The primary language for a country

Callout: See this article to instead learn how to [configure when opt-out keywords remove SMS consent](https://help.klaviyo.com/hc/en-us/articles/29109965092251).

### Edit a compliance keyword’s response

Changing the response message is a potential compliance risk. Consult with your legal counsel before making any edits.

If you want to personalize a response for a certain audience, you can change the wording of the response message for a country. For instance, you could use British spelling in the UK and American spelling in the US.

The only response you cannot change is for opt-out keywords in the US and Canada. This is because wireless carriers (and not your SMS provider) send this response in many cases.

To change the response for a compliance keyword:

1. Select your account name in the lower left corner
2. Click ****Setting > SMS****.
3. Navigate to ****Keyword responses****.
4. In the **Compliance keywords** section, choose the country and language from the dropdown.
5. Select ****Edit**** next to the keyword response you want to edit.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/29910716690331)
6. Edit the message to suit your business needs.
   Note that there’s a character count so you know how many [message segments](https://help.klaviyo.com/hc/en-us/articles/13502982552347#h_01HKT07YTW6HCRSCVV6FY1PMES) this response will be.
7. Select ****Save**** to update that response.

This change only applies to that country and language. If you want to change the response for every country, you must do so by repeating these steps for each country.

### Change primary language for a country

Klaviyo uses the primary language when it doesn’t have information about a subscriber’s preferred language. This typically happens when someone signs up for SMS without a keyword.

By default, Klaviyo uses the most commonly spoken language in a country. In addition, not all countries have multiple languages to choose from.

To change the primary language:

1. Select your account name in the lower left corner
2. Click ****Setting > SMS****.
3. Navigate to ****Keyword responses****.
4. In the **Compliance keywords** section, choose the country where you want to change the primary language.
5. Click the ****Edit Primary****.
6. In the modal that appears, open the primary language dropdown.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/29910716692507)
7. Select the language you want.
8. Click ****Save****.

## Outcome

Going forward, if a keyword response is required and the language is unknown, the response will be sent in the primary language.

Once you do so, you can start building segments based on the profile’s preferred language by using the subscribe or opt-in word they used.

## Additional resources

- Learn more about keywords in Klaviyo:
  - [How to configure your opt-out keyword settings](https://help.klaviyo.com/hc/en-us/articles/29109965092251)
  - [How to add, update, or delete SMS custom keywords](https://help.klaviyo.com/hc/en-us/articles/360050384091)
- See more about [sending multi-nationally with Klaviyo](https://help.klaviyo.com/hc/en-us/articles/23740503987099)