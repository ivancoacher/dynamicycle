---
id: 40116568714523
title: "How to migrate from WhatsApp Business App to Klaviyo"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/40116568714523-How-to-migrate-from-WhatsApp-Business-App-to-Klaviyo"
section: "Migrate to Klaviyo"
category: "WhatsApp"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-05-11T12:54:21Z"
language: en
---

Learn how to migrate from WhatsApp Business App to Klaviyo.

If your WhatsApp number is associated with a WhatsApp Business App, then migrating to Klaviyo means you'll be moving to the WhatsApp Business API. Klaviyo can migrate your number, but you will be losing these two things:

- Access to the WhatsApp Business App UI on mobile.
- Chat history in the app (unless exported manually).

****How is the WhatsApp Business API different from the WhatsApp Business App?****

The ****WhatsApp Business App**** is designed for small businesses and runs on a phone, just like the regular WhatsApp app. It works best for one or two people managing customer chats directly. While it’s simple to use, it offers only limited automation and does not support advanced integrations.

The ****WhatsApp Business API**** (which Klaviyo uses) is built for medium to large businesses. It doesn’t run as a mobile app; instead, it connects to platforms like Klaviyo through the Cloud API. This setup supports automation, integrations, and scaling to larger support or marketing teams. The API is also required for sending template messages, such as order updates, reminders, or promotions.

## Before you begin

Before you begin migration, make sure:

- You have access to your WhatsApp Business App.
- You have access to receive a text on your phone number during the set up process.
- You’ve exported your chat history if you want to keep it.

Chat history will not transfer over to WhatsApp API and will be deleted once you deactivate your WhatsApp Business App. Chat history cannot be imported into Klaviyo, but it is recommended to export it for record keeping purposes.

## Migrate from WhatsApp Business App

### Deactivate your WhatsApp Business App

Deactivate your current WhatsApp Business App so that your number is free to transfer to WhatsApp API. See [Meta’s article on deactivating your account](https://faq.whatsapp.com/969230211289837).

### Disable two-factor authentication

To migrate to Klaviyo, you must disable the phone number's two-factor authentication (2FA) in your WhatsApp Business Account. If you’re unable or unsure how to do this, reach out to your current provider.

If you have access to WhatsApp Manager, you may be able to disable this yourself.

1. In Meta Business Suite, navigate to ****Business Settings****.
2. Select ****WhatsApp Accounts****.
3. Select the specific WhatsApp account you want to modify.
4. Click on ****WhatsApp Manager**** within the account settings.
5. Select the phone number associated with your account.
6. Click ****Settings**** for the selected phone number and select the ****Two-Step Verification**** tab.
7. Click ****Turn off two-step verification****. This will trigger a confirmation email.
8. Click the link in the email confirmation sent to you to confirm this change and disable 2FA.

### Connect your WhatsApp account to Klaviyo

1. In Klaviyo, go to ****Settings**** > ****WhatsApp****.
2. Click ****Connect to WhatsApp****.
3. Follow the instructions in the setup modal.
   1. Create a new WhatsApp Business Account.
   2. Use the same display name.
   3. Add the phone number you would like to migrate.
   4. Verify your account using the verification code sent to your number.

## Next steps

Congratulations! You have migrated to Klaviyo.

Learn about [import your WhatsApp](https://help.klaviyo.com/hc/en-us/articles/40116243735579) or see how to [set up a flow](https://help.klaviyo.com/hc/en-us/articles/40116763040411).