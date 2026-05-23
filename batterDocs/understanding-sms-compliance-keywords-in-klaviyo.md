<h1>Understanding SMS compliance keywords in Klaviyo</h1>

Owners, Admins, and Managers can edit the settings for compliance keywords

## You will learn

Learn about compliance keywords in Klaviyo, including what they are, how they work, and which languages they’re available in. In addition, it explains the options for when opt-out keywords can remove consent.

This article goes over how compliance keywords work in Klaviyo. For details on how to change these settings, see this article on [configuring your compliance keyword language](https://help.klaviyo.com/hc/en-us/articles/29910716707355).

## What are compliance keywords?

Compliance keywords are certain words that require a reply or action when you receive them.

Examples of compliance keywords include:

- HELP or INFO
- STOP, QUIT, END, or CANCEL
- YES or Y
- START or UNSTOP

When someone texts any of these words, you must provide specific information or take a certain action, like opting them out or in to SMS marketing.

However, not all keywords are the same. STOP, for instance, has stricter limitations than any other keyword. For toll-free numbers, the response for STOP comes from wireless carriers (not your SMS platform), and for US and Canadian short codes, the response to STOP has certain requirements.

****Compliance vs. subscribe and other keywords****

There are a few types of SMS keywords. The main 3 are:

- ****Compliance****
  Keywords that require responses, either by law or wireless carriers.
- ****Subscribe**** (also called “custom”)
  Keywords someone can send to opt in to SMS.
- ****Other****
  Other types of keywords a brand may use, such as for quizzes (e.g., “Are you a cat- or dog-person? Text CATS or DOGS to let us know!)

## How compliance keywords work in Klaviyo

Compliance keywords require a response, which Klaviyo handles automatically.

Compliance keywords are not available for branded sender IDs, as this number type cannot receive inbound SMS messages.

If someone sends a compliance keyword, Klaviyo:

- Provides a reply automatically, typically in the [same language](#h_01J9RN0FABGN4B3YNQ03QBA3J2).
- Adds or removes SMS consent from that profile, if applicable.
  - Note: you can configure [when opt-out keywords remove consent](#h_01J9RN0FABYZ184E85D3ZJ25QW).

While not recommended, you can [edit the responses](https://help.klaviyo.com/hc/en-us/articles/29910716707355) to most compliance keywords. The only exception is for opt-out keywords in the US and Canada, as the opt-out response is often sent by wireless carriers or has certain requirements.

## Responding to compliance keywords in the same language

Klaviyo supports compliance keywords and responses in each country’s official languages, plus English. This way, if someone in Switzerland texts OUI or JA, Klaviyo can respond in French or German, respectively.

Languages and responses are both based on the subscriber’s country code, meaning:

- A certain language available for one country may not be available in another.
- A keyword’s response can vary from one country to another, even if it’s in the same language.

For instance, French might be available for Canada, France, and Switzerland, but not in Ireland. Further, if you edit the response for OUI for Canada, this does not affect the response of OUI in France or Switzerland.

While compliance keywords themselves can be in different languages, the wording of the opt-out instruction included at the end of messages (“Text STOP to opt-out”) and the auto-response setting for “when no keyword is recognized” are not.

### The primary language

Each country has a primary language, which will be used as the fallback for cases when the user’s language is unknown.

For instance, the primary language will be used if a customer signs up without texting a keyword and Klaviyo needs to send the double opt-in confirmation message.

The primary language is set to the most spoken language in each country by default (e.g., German in Switzerland). However, you can change the primary language at any time (e.g., from German to French in Switzerland).

### Available languages by country

Below, you can see the supported languages for compliance keywords by country.

An asterisk (\*) indicates the default primary language for each country.

Note that while Klaviyo SMS is available in many other countries, the ones below are the only ones where 2-way messaging (which includes compliance keywords) is available.

|  |  |  |
| --- | --- | --- |
|  | ****Default language**** | ****Other languages available**** |
| Canada | English | French |
| Belgium | English | French, Dutch |
| Germany | German | English |
| Austria |
| Netherlands | Dutch | English |
| Switzerland | German | English, French, Italian |
| Spain | Spanish | English |
| Sweden | Swedish | English |
| Norway | Norwegian | English |
| Finland | Finnish | English |
| Denmark | Danish | English |
| Italy | Italian | English |
| Hungary | Hungarian | English |
| Poland | Polish | English |
| Portugal | Portuguese | English |
| Australia | English | N/A |
| United States |
| New Zealand |
| United Kingdom |
| Ireland |

## Opt-out keywords: when they remove consent

Klaviyo offers 2 options when messages include an opt-out keyword:

1. ****Contains word**** (default)
   If an opt-out keyword appears anywhere in an SMS, or the message is an exact match, the subscriber is opted out (e.g., if someone texts “I want to cancel my order,” this removes SMS consent).
2. ****Exact match****
   When a message only contains an opt-out keyword and nothing else, the subscriber is opted out (e.g., someone must text CANCEL on its own (not case-sensitive) for consent to be removed).

When picking between these options, know that the behavior applies to all countries and languages. Learn how to [change the opt-out behavior](https://help.klaviyo.com/hc/en-us/articles/29109965092251).

Network messages always include the word “STOP” when responding to any opt-out keyword.

### Which option should I choose?

The best option to use varies from business to business.

In general, using **contains** is better for those who want to remain strictly compliant. Using this option ensures that someone is automatically unsubscribed as soon as they mention any opt-out word, such as if someone texts “please cancel.”

However, there are exceptions. For instance, subscription businesses may want to use **exact match** for words like “cancel,” “unsubscribe,” “end,” and “quit.” Customers may send these when discussing the subscription itself rather than their SMS consent.

If you choose to use **exact match** for any keyword, please include unsubscribe instructions in your auto-response message (i.e., **when no keyword is recognized**), if applicable. Alternatively, make sure your support team reviews your conversations regularly to catch any instances where someone intends to cancel and then manually removes SMS consent from the profile.
