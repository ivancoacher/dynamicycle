---
id: "29109965092251"
title: "How to configure your opt-out keyword settings"
source_url: "https://help.klaviyo.com/hc/en-us/articles/29109965092251-How-to-configure-your-opt-out-keyword-settings"
section: "Understanding SMS compliance settings"
category: "SMS"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-21T13:54:37Z"
language: "en"
---
You must be an Owner, Admin, or Manager to use this functionality.

## You will learn

Learn how to control when an opt-out keyword results in an unsubscribe.

Opt-out keywords are a type of compliance keyword, requiring both an action and response (i.e., removing consent and then confirming the opt-out). With this functionality, you can choose to remove consent when a subscriber sends an opt-out keyword either:

- Anywhere in an SMS (contains word)
  or
- As the only word in the SMS (exact match)

This information is intended solely for educational and informational purposes and should ****not**** be construed as legal advice. The content provided is general in nature and may not reflect the most up-to-date information. Klaviyo strongly advises consulting with a qualified legal counsel to ensure your compliance with applicable laws and regulations in connection with your use of our services.

## Before you begin

Please note the following:

- For any subscriber in the US, you cannot set the STOP keyword to **Exact match**.
  - Any time a US number includes the word stop in a text, Klaviyo automatically and immediately removes SMS consent.
  - This is to protect you from potential compliance issues, as the laws surrounding the STOP keyword are stricter in the US.
- The auto-response for opt-out keywords always uses the word "stop," regardless of which opt-out keyword was used.
- You cannot edit the auto-response for an opt-out keyword.

For more information, see this [article on how compliance keywords work.](https://help.klaviyo.com/hc/en-us/articles/29928896469531)

## How each option for opt-out keywords works

Klaviyo offers 2 options when messages include an opt-out keyword:

1. ****Contains word**** (default)

   - If an opt-out keyword appears anywhere in an SMS or the word is an exact match, the subscriber is opted out (e.g., if someone texts “Cancel subscription,” this removes SMS consent).
   - Recommended for: those who want to remain strictly compliant.

   |  |  |
   | --- | --- |
   | ![](https://cdn.sanity.io/images/6ct6b26e/help-center-dev/12157e7bbe0b8db639bf5a505e8d9ef517a1b71f-668x538.png) | ![](https://cdn.sanity.io/images/6ct6b26e/help-center-dev/08f204d50cf4df31445de63147d52e01031852ce-668x538.png) |
2. ****Exact match****

- When a message only contains an opt-out keyword and nothing else, the subscriber is opted out (e.g., someone must text “cancel” (not case-sensitive) for consent to be removed).
- Recommended for: subscription businesses for words like “cancel,” “unsubscribe,” “end,” and “quit.” (Customers may send these when discussing the subscription itself rather than their SMS consent. )

![](https://klaviyo.zendesk.com/hc/article_attachments/29154296049435)

Note that the network message always includes the word “stop” regardless of the opt-out keyword the subscriber actually texted.

## Change your opt-out keyword settings

For US subscribers, you cannot configure the settings for the STOP keyword.

1. Select your account name in the lower left corner.
2. Navigate to ****Settings > SMS > Keyword Responses****.
3. Click ****Edit**** next to the opt-out keywords.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/29154311168027)
4. Select the dropdown next to the opt-out keyword you want to configure (e.g., **CANCEL**).

   - This functionality is not available for the STOP keyword in the US.![](https://klaviyo.zendesk.com/hc/article_attachments/29158591823131)
5. Choose either:

   - ****Contains word**** (default)
     The opt-out keyword appears anywhere in an SMS.
   - ****Exact match****
     The opt-out keyword is the only word in the SMS.
6. Review the warning message about changing your opt-out keyword settings before saving.
7. Select ****Save**** to use this setting for an opt-keyword.