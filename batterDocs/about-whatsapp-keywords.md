<h1>About WhatsApp keywords</h1>

Learn about WhatsApp keywords, including how compliance and subscribe keywords work, and how autoresponders and notifications function within WhatsApp message flows.

## ****What are WhatsApp keywords****

WhatsApp keywords are automated words or phrases that trigger specific actions in Klaviyo. These keywords help you meet compliance standards, manage customer preferences, and automate common responses.

There are three main types of WhatsApp keywords:

- ****Subscribe keywords**** — used for voluntary opt-ins
- ****Autoresponder keywords**** — trigger when someone sends an unrecognized keyword or message
- ****Compliance keywords**** — to manage opt-ins and opt-outs

Each type plays a unique role in maintaining deliverability and trust with your audience.

## Subscribe keywords

A subscribe keyword allows someone to opt in to your WhatsApp messages (for example, JOIN).
These differ from compliance keywords because they are a **marketing opt-in method**, not a legal requirement.

When a person sends your subscribe keyword, they are added to your specified list and can start receiving campaigns or flows.

You can create custom subscribe keywords that:

- Contain between 3 and 20 characters
- Use only letters and numbers (A–Z, 0–9)
- Exclude spaces and special symbols
- Avoid overly common words (such as “the,” “that,” or “and”)

## Autoresponders

Autoresponders automatically send a confirmation or welcome message after a contact subscribes through a keyword.

In [Helpdesk](https://help.klaviyo.com/hc/en-us/articles/360059002271#h_01K2FBMRZBW3DTFGHG3NV3D7AC), you can edit:

- The ****autoresponder message**** itself to match your brand tone
- The ****email notifications**** associated incoming unrecognized keywords

## Compliance keywords

Compliance keyword responses are automatically toggled on to respond when someone replies to one of your WhatsApp messages. These keywords help ensure legal compliance and support double opt-in workflows.

Keep in mind: Keyword and response pairs are available in multiple languages.

Compliance keywords include:

|  |  |  |
| --- | --- | --- |
| ****Keyword(s)**** | ****Default response**** | ****Details**** |
| ****STOP, STOPALL, UNSUBSCRIBE, CANCEL, END, QUIT**** | You have successfully unsubscribed from WhatsApp updates. | This message is sent after someone opts out. |
| ****YES, Y**** | You have successfully subscribed to WhatsApp updates. | Only applies after someone confirms they want to subscribe using double opt-in. |

Double opt-in is only available for paid Mobile Messaging plans.

## Opt-out keywords: when they remove consent

Klaviyo offers two options for how messages with opt-out keywords are handled:

### Contains word (default)

If an opt-out keyword appears anywhere in a message, or the message is an exact match, the subscriber is opted out. For example, if someone sends “I want to cancel my order” on WhatsApp, this removes WhatsApp consent.

### Exact match

When a message only contains an opt-out keyword and nothing else, the subscriber is opted out. For example, someone must send ****CANCEL**** on its own (not case-sensitive) for consent to be removed.

When choosing between these options, note that the behavior applies to all countries and languages.

## How language detection works

Klaviyo supports compliance keywords for WhatsApp in each country’s official languages, plus English. This ensures that when someone sends a compliance keyword on WhatsApp, they receive a response in the appropriate local language.

For example, if someone in Switzerland sends ****OUI**** or ****JA**** via WhatsApp, Klaviyo can respond in French or German, respectively.

Languages and responses are determined by the subscriber’s country code. This means:

- A language available in one country may not be available in another.
- A compliance keyword’s response can vary by country, even when the language is the same.

For instance, French may be supported for Canada, France, and Switzerland, but not for Ireland. Additionally, editing the response for ****OUI**** in Canada does not affect the response for ****OUI**** in France or Switzerland.

## The primary language

Each country has a primary language that serves as a fallback when the subscriber’s language cannot be determined.

For example, the primary language is used if a customer opts in through a non-keyword method and Klaviyo needs to send a required compliance message, such as an opt-in confirmation, on WhatsApp.

By default, the primary language is set to the most widely spoken language in each country (for example, German in Switzerland). You can update the primary language at any time, such as switching Switzerland’s primary language from German to French.

## Available languages by country (WhatsApp)

Below are the languages supported for WhatsApp compliance keywords by country. An asterisk (\*) indicates the default primary language.

While WhatsApp messaging is available in many countries, compliance keyword support is limited to the countries listed below.

| Country | Default language | Other languages available |
| --- | --- | --- |
| Canada | English\* | French |
| Belgium | English\* | French, Dutch |
| Germany | German\* | English |
| Austria | German\* | English |
| Netherlands | Dutch\* | English |
| Switzerland | German\* | English, French, Italian |
| Spain | Spanish\* | English |
| Sweden | Swedish\* | English |
| Norway | Norwegian\* | English |
| Finland | Finnish\* | English |
| Denmark | Danish\* | English |
| Italy | Italian\* | English |
| Hungary | Hungarian\* | English |
| Poland | Polish\* | English |
| Portugal | Portuguese\* | English |
| Australia | English\* | N/A |
| United States | English\* | N/A |
| New Zealand | English\* | N/A |
| United Kingdom | English\* | N/A |
| Ireland | English\* | N/A |
| Everywhere else | English\* | **N/A** |

## ****Best practices****

- Keep compliance responses concise and consistent across languages.
- Regularly test that opt-in and opt-out messages trigger correctly.
- Review autoresponder tone to align with your brand voice.
- Use a clear confirmation path when implementing double opt-in.
