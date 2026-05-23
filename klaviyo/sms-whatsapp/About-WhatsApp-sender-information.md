---
id: 44479363197083
title: "About WhatsApp sender information"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/44479363197083-About-WhatsApp-sender-information"
section: "Getting started with WhatsApp"
category: "WhatsApp"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-20T16:50:53Z"
language: en
---

Admin or Owner permissions required to manage WhatsApp sender settings.

Learn how to view and manage your WhatsApp Business Account (WABA) and phone numbers in Klaviyo. Managing your sender information ensures your WhatsApp integration stays connected and messages send correctly.

## WhatsApp Business Account

The Sender Information tab in your WhatsApp settings is where you manage your connected WhatsApp Business Account (WABA). From here, you can view your account status, manage numbers, adjust your primary sending number, and troubleshoot connection issues.

### What you’ll see

For each WABA, Klaviyo shows the following information:

- Account name.
- Messaging limit (24-hour window).
- Connection status and any required actions.

### Disconnecting your WABA

You can disconnect your WABA from Klaviyo at any time.

Disconnecting your WABA removes your integration with Klaviyo. You will not be able to send through Klaviyo until you reconnect.

## WhatsApp phone numbers

Within the ****WhatsApp phone numbers**** section, you can see all numbers associated with your connected WABA.

### Managing existing numbers

For each number, Klaviyo shows the following:

- Phone number.
- Quality score (**High**, **Medium**, **Low**, **Unknown**).
- Connection status.
- Available actions (such as ****Set as primary**** or ****Resubmit****).

### Primary sending number

You can have one primary sending number at a time. This number is used for all outgoing WhatsApp messages unless otherwise specified. You can switch the primary number at any time.

### Adding a new WhatsApp number

When adding a new number, you go through Meta’s Embedded Signup process.

#### Important step: select the correct WABA

During signup, Meta asks you to choose a WhatsApp Business Account. Make sure you select the same WABA that is already connected to Klaviyo. Otherwise, the number cannot be associated correctly and setup fails.

### Pending numbers

If your newly added number shows **Pending**, take the following actions:

- Complete any follow-up steps in Meta.
- Click ****Resubmit**** in Klaviyo to retry linking the number after resolving the issue.

## Troubleshooting common issues

If your WABA or phone number shows an error, use these steps to resolve it.

### Your WhatsApp account is already connected to another provider

WhatsApp numbers and WABAs cannot be connected to multiple platforms at the same time.

****Fix:**** Disconnect the WABA from the previous provider. If the previous provider cannot be reused or you want a clean setup, create and connect a new WABA during Meta’s setup flow.

### Meta has disabled your account

Meta may disable WABAs for policy or security reasons.

****Fix:**** Log in to your Facebook Business Manager and submit an appeal to Meta. Once the account is reinstated, return to Klaviyo and refresh your connection.

### Display name rejected

Phone numbers require an approved display name.

****Fix:**** Open the number in your WABA and resubmit the display name for review. Then click ****Resubmit**** in Klaviyo once Meta approves it.

### Klaviyo could not associate its credit line

If the WABA cannot be linked to Klaviyo’s credit line, sending fails.

****Fix:**** Disconnect your WABA from Klaviyo and go through the set up flow again. Choose to create a new WABA during signup.

### Two-step verification (2FA) enabled on previous provider

If two-step verification is still turned on for a number from a prior provider, Meta prevents Klaviyo from connecting.

****Fix:**** In your old provider or Meta Business Manager, turn off two-step verification for that number. Then return to Klaviyo and click ****Resubmit****.