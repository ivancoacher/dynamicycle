---
id: 17292871409947
title: "How to set up lead capture with Shop on a sign-up form"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/17292871409947-How-to-set-up-lead-capture-with-Shop-on-a-sign-up-form"
section: "Build and use forms"
category: "Sign-up forms"
category_slug: "sign-up-forms"
klaviyo_updated: "2026-04-21T13:54:30Z"
language: en
---

## You will learn

Learn how to set up lead capture with Shop on a Klaviyo sign-up form to recognize Shop Pay users, save and apply their discounts, and collect SMS consent. [Shop Pay](https://help.shopify.com/en/manual/payments/shop-pay) is an online checkout service offered by Shopify that allows 1-click checkout to improve the buying experience for your customers. Once a buyer uses Shop Pay for the first time, their information is saved for future purchases.

When you enable lead capture with Shop on a sign-up form, it will recognize site visitors with Shop Pay accounts once they enter their email. You can use their pre-saved information to incentivize a purchase by offering a discount, and also provide an easy SMS opt-in experience.

This feature is specific to Shopify, and will only be available to Klaviyo customers who use Shopify as their ecommerce platform.

## Before you begin

You will need to [activate Shop Pay on your Shopify store](https://help.shopify.com/en/manual/payments/shop-pay) before you can set up lead capture on a Klaviyo sign-up form.

There are certain requirements that make a sign-up form eligible to use lead capture with Shop. Your form must:

- Be a popup or flyout form

  This functionality is not available for embed or full page forms.
- Collect email consent on the first step
  - If you want to collect SMS consent also, you must use a multi-step form that collects email consent on the first step, followed by SMS consent on the 2nd step. Forms collecting solely SMS consent are not eligible for lead capture.

    If lead capture with Shop is enabled on your form, [Smart Opt-in](https://klaviyo.zendesk.com/hc/en-us/articles/24743883751451) is not supported. If you want all shoppers to go through a Smart Opt-in experience, disable lead capture with Shop.
- Include disclosure language if collecting SMS consent
- Have a coupon (static or unique) configured on the success step

## Enable lead capture with Shop on a sign-up form

Set up lead capture on a sign-up form:

1. Select ****Sign-up forms**** in Klaviyo’s main navigation****.****
2. Click on the form where you want to set up lead capture or choose to create a new one.
3. Click ****Edit Form**** to enter the editor.
4. Select ****Targeting and behavior****.
5. Under **Lead Capture with Shop**, toggle the switch on**.**
6. When you turn this on, any of your form’s unfulfilled requirements for using lead capture populate under the error message. For example, the form below is missing the coupon on the success step:

   To resolve this error, click ****Add block**** to [configure a unique or static coupon](https://help.klaviyo.com/hc/en-us/articles/6038674938523#set-up-a-static-coupon-in-your-form4) on the success step.
   ![The Lead capture with Shop section in the Targeting & behavior tab of the form builder with an arrow pointing to the “Add a coupon block” requirement.](https://klaviyo.zendesk.com/hc/article_attachments/28716056864283)

   If you’re using a multi-step form that collects SMS consent, you must include [disclosure language](https://help.klaviyo.com/hc/en-us/articles/360035285472#sms-opt-in-disclosure16) on the SMS opt-in step.
7. Click on **Success** in the menu bar to customize the success message that appears when new subscribers submit the form.

   It’s best practice to use generic language in your success step (e.g., “Hooray! Here is your coupon!”) to give subscribers a clear and consistent opt-in experience. This is because a subscriber may choose not to receive texts, so if the success message thanks them for opting into email and SMS, it could create a confusing experience for shoppers that did not give SMS consent.
8. Once you have fulfilled all requirements, you’ll see a green banner informing you that lead capture has successfully turned on.
9. When you’re satisfied with your form, click ****Publish****.

Once this form is live, any site visitors with Shop Pay accounts will be recognized when they submit the first step (their email address). A Shop Pay modal will appear asking them to authenticate their account.

![The Shop Pay authentication modal that appears in the top right corner of your site when Klaviyo recognizes a Shop Pay user.](https://klaviyo.zendesk.com/hc/article_attachments/28716056865307)

Note that shoppers who do not have Shop Pay accounts will go through the form steps as normal and the modal will not populate. Also, if your form has additional steps beyond the email and SMS step (e.g., a step asking for a shopper’s birthday), Shop Pay users who authenticate their accounts will skip these steps and only see the Shop Pay modal journey and your form’s success step.

The site visitor’s experience will differ depending on the type of form and how they choose to interact with the Shop Pay modal:

- If the shopper chooses not to authenticate their account and immediately closes the Shop Pay modal, your sign-up form will automatically show its next step, whether that is an SMS opt-in step or a success step.
- For an email-only sign-up form, if the shopper enters the code to authenticate their Shop Pay account, the modal will then show the success step with the coupon code, and will inform them that the discount will automatically apply to their next checkout.
- For a multi-step form, if the shopper enters the code to authenticate their Shop Pay account, the modal will next ask for SMS consent. The shopper’s phone number from their ShopPay profile will be pre-filled to create a seamless opt-in experience.
  ![The Shop Pay modal prompting an authenticated user to sign up for texts through a tap-to-text experience.](https://klaviyo.zendesk.com/hc/article_attachments/28716056867739)
- If the shopper gives SMS consent, it will prompt them through Shop Pay’s SMS opt-in experience to confirm their SMS consent, and then show the form’s success step with the coupon that’s automatically saved to their next checkout.
- If the shopper does not give SMS consent, the Shop Pay modal will disappear and they will see the form’s success step with the coupon that’s automatically saved to their next checkout.

## Next steps

Now that you have lead capture with Shop set up on your sign-up form, create a personal Shop Pay account to test the different shopper experiences described above.