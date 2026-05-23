---
id: 31583129959195
title: "How to ask for transactional SMS consent separately"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/31583129959195-How-to-ask-for-transactional-SMS-consent-separately"
section: "Build forms to grow your SMS list"
category: "SMS"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-21T13:54:38Z"
language: en
---

You must:

- Be an Owner, Admin, or Manager.
- Have set up SMS in Klaviyo.
- Are on a paid account.

## You will learn

Discover how to collect transactional SMS consent separately from promotional consent.

Specifying the type of consent is helpful if you plan to only send transactional messages, (such as for subscription-based business) or want to give your customers the choice of SMS messages.

For all other cases, you don’t need to specify the consent type. By default, it’s set to promotional consent, which allows you to send any type of SMS message.

## About the different types of SMS consent

In Klaviyo, there are 3 types of SMS consent:

- ****Promotional****
  Allows you to send any type of SMS message, including campaigns and all flows. With promotional consent, you can also send transactional messages.
- ****Transactional****
  Consent for all transactional messages, including order updates and other post-purchase flow messages.
- ****Order updates**** (Shopify only)
  The most limited type of SMS consent. This type of consent is linked to a specific purchase, and only permits sending SMS from post-purchase flows about this 1 order. Learn more about [SMS order updates for Shopify](https://help.klaviyo.com/hc/en-us/articles/18389135527323).

Visualize the SMS consent types as a hierarchy, similar to the image below. Promotional is the broadest category and includes transactional messages, which in turn includes order updates. For more information, please see [understanding transactional messages](https://help.klaviyo.com/hc/en-us/articles/26024442679835).

![Graph of different SMS consent types](https://klaviyo.zendesk.com/hc/article_attachments/34593429544731)

## Before you begin

Please note the following about collecting transactional consent:

- Transactional consent always uses single opt-in, meaning you cannot use:
  - Double opt-in for transactional.
  - Any 2-step consent collection method (like Smart Opt-in) for a form that includes transactional consent.
- Transactional-only subscribers are not added to lists, but transactional consent is shown on the profile.
- If you previously set up disclosure language in your account, you may need to edit it to mention transactional messages.

Note that you can collect transactional and promotional consent on the same page of a form or on 2 different steps. The choice is up to you (there’s no compliance considerations to be aware of).

## Collect transactional consent in a form

You only need to follow these steps if you require separate opt-in options for transactional and promotional consent (such as if you plan to [use a US short code](https://help.klaviyo.com/hc/en-us/articles/26886941270171)), or if you're exclusively collecting transactional consent. Otherwise, you can simply collect promotional consent, which is the default.

You can either add transactional consent to an existing form or build a new form.

Generally, it’s recommended that you use an existing form that already has your branding. However, note that you cannot use transactional consent with either Smart Opt-in or tap-to-text functionality, note that will be disabled. When you go to add transactional consent, it disables Smart Opt-in and tap-to-text.

Either open the dropdown below to find instructions for creating a new form with email, SMS transactional, and SMS promotional or skip ahead to learn how to add SMS transactional to an existing form for email and SMS promotional consent.

****Build a new form for email, SMS transactional, and SMS promotional****

1. Navigate to the ****Sign-up**** forms tab in Klaviyo.
2. Build a new form by clicking ****Create form**** in the upper right.
3. Name the form (e.g., Email & SMS).
4. Select the list this form should go to.

   - Recommendation: choose your main subscriber list (e.g., Newsletter).
   - Note that transactional-only subscribers will not be added to this list.
5. Choose the form type.

   - Recommendation: since this example collects multiple types of consent, a best practice is to use a popup, flyout, or full-page form.![Form creation modal showing the form type dropdown](https://klaviyo.zendesk.com/hc/article_attachments/31780026556955)
6. Recommendation: use a teaser for your form.
7. Select ****Save and design****.
8. Optional: change your [teaser settings](https://help.klaviyo.com/hc/en-us/articles/4411540984859).
9. Above the preview, in the center, select ****Email Opt-in****.
   ![Email Opt-in option in the form builder](https://klaviyo.zendesk.com/hc/article_attachments/31779971718171)
10. Design your email page. Tips:

    - At minimum, your form needs an email input field and button.
    - It’s recommended to add text input fields for first and last name.![Example of a form collecting email, first name, and last name](https://klaviyo.zendesk.com/hc/article_attachments/31779971723163)
11. Click the ****+ Step**** button.
    ![Add step button in the form builder](https://klaviyo.zendesk.com/hc/article_attachments/31779971725339)
12. In the resulting modal, select ****SMS opt-in****, then click ****Next****.
    ![Modal where showing the option to add a step to collect SMS consent](https://klaviyo.zendesk.com/hc/article_attachments/31780026568347)
13. Choose your SMS subscriber list.

    - Note that **Traditional SMS double opt-in** is automatically picked, but this will not apply to SMS transactional consent.![Modal to choose a list for SMS subscribers](https://klaviyo.zendesk.com/hc/article_attachments/31779971736347)
14. Click ****Add step****.
15. Select the phone number field.
    ![Form where the phone number field is selected](https://klaviyo.zendesk.com/hc/article_attachments/31780026572571)
16. In the left-hand panel, open the **SMS Consent** dropdown.
    ![SMS consent dropdown](https://klaviyo.zendesk.com/hc/article_attachments/34593404157979)
17. If you choose:

    - **Single step - Transactional & promotional**, this adds a checkbox for promotional consent.
      or
    - **Multi step - Transactional & promotional**, this adds a new step to the form.

    |  |  |
    | --- | --- |
    | ****Single step**** | ****Multi step**** |
    | ![Single step form with both transactional and promotional SMS consent](https://cdn.sanity.io/images/6ct6b26e/help-center-dev/bdf1272a97bb459a1c00d52b682a570fd2214909-882x796.png) | ![Step created to collect promotional consent when you select multi step transactional and promotional](https://cdn.sanity.io/images/6ct6b26e/help-center-dev/2429dd8ecb08a83cf190afd78b13e291c0192a0b-886x798.png) |
18. Update the disclosure language based on the consent you’re collecting:

    - Transactional only: exclusively mention transactional messages (e.g., order updates).
    - Transactional and promotional: include references to both transactional messages (e.g., order updates) and promotional messages (e.g., discounts, announcements, etc.).
19. Finish designing your form, and click ****Publish**** to set it live.

### Collect transactional consent from an existing form

Follow the steps below to learn how to create a form that gathers transactional SMS consent. Note that adding transactional consent to a form removes any Smart Opt-in or tap-to-text functionality, as these cannot be used together with transactional.

1. Navigate to the ****Sign-up**** forms tab in Klaviyo.
2. Select the 3 dots next to the form where you want to collect SMS consent, then clicking ****Edit form****.
3. Within the form editor, select the phone number field.
   ![Form where the phone number field is selected](https://klaviyo.zendesk.com/hc/article_attachments/31780026572571)
4. In the left-hand panel, open the **SMS Consent** dropdown.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/31780026577307)
5. If you choose:

   - **Single step - Transactional & promotional**, this adds a checkbox for promotional consent.
     or
   - **Multi step - Transactional & promotional**, this adds a new step to the form for promotional consent.

   |  |  |
   | --- | --- |
   | ****Single step**** | ****Multi step (promotional)**** |
   | ![Single step form with both transactional and promotional SMS consent](https://cdn.sanity.io/images/6ct6b26e/help-center-dev/bdf1272a97bb459a1c00d52b682a570fd2214909-882x796.png) | ![Step created to collect promotional consent when you select multi step transactional and promotional](https://cdn.sanity.io/images/6ct6b26e/help-center-dev/2429dd8ecb08a83cf190afd78b13e291c0192a0b-886x798.png) |
6. Recommendation: for single-step forms, make sure to label that the phone number field is for transactional SMS messages.
   ![Single-step form where the phone number field is labeled as being for transactional SMS](https://klaviyo.zendesk.com/hc/article_attachments/31781599736219)
7. Update the disclosure language based on the consent you’re collecting:

   - Transactional only: exclusively mention transactional messages (e.g., order updates).
   - Transactional and promotional: include references to both transactional messages (e.g., order updates) and promotional messages (e.g., discounts, announcements, etc.).
8. Once you’re satisfied with the form, select ****Publish****.

Once your form is live, you can start collecting transactional consent separately from promotional consent.

You’ll also be able to [view the consent type within a profile](https://help.klaviyo.com/hc/en-us/articles/360035056972).

## Collect transactional consent at checkout (Shopify only)

Shopify customers can collect transactional SMS consent on their thank you and order status pages via an app block and sync it to Klaviyo. Additionally, Shopify Plus customers can use app blocks to collect transactional SMS consent on their checkout pages. These app blocks are set up in Klaviyo and then installed in Shopify. Learn how to [collect transactional SMS consent on Shopify checkout pages](https://help.klaviyo.com/hc/en-us/articles/35067557759771).