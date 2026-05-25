---
id: "26855536897691"
title: "How to localize sign-up forms for multiple regional domains"
source_url: "https://help.klaviyo.com/hc/en-us/articles/26855536897691-How-to-localize-sign-up-forms-for-multiple-regional-domains"
section: "Form best practices"
category: "Sign-up forms"
category_slug: "sign-up-forms"
klaviyo_updated: "2026-04-21T13:54:37Z"
language: "en"
---
## You will learn

Learn how to use the multi-account cloning feature to set up language-specific sign-up forms if you have a website with multiple regional domains. For instance, if you have different domains for the United States, France, and Spain, they appear as:

- https://swak-lip-care.myshopify.com
- https://swak-lip-care.myshopify.fr
- https://swak-lip-care.myshopify.es

## Before you begin

Note that a Klaviyo account can only be connected to 1 website URL (or “domain”). If you have multiple international domains, then you must have multiple Klaviyo accounts. If you have not already set up an account for each domain, see [how to create and manage multiple accounts](https://help.klaviyo.com/hc/en-us/articles/360002165611).

Tip: To easily analyze your performance, billing, and more across accounts, you can [create a portfolio](https://help.klaviyo.com/hc/en-us/articles/24656917054747).

Only Owners, Admins, and Managers can clone sign-up forms. You must have the appropriate user permissions both in the account you’re cloning from and the account(s) you’re cloning to. For instance, say you’re an Admin in accounts A and B, but a Content Creator in account C. In this case, you can clone a flow from account A to B (or vice versa), but cannot clone a flow to or from account C.

## How localizing for multiple regional domains works

To set up language-specific sign-up forms for multinational domains:

1. Create a Klaviyo sign-up form for 1 of your regional domains, in the language of the account's domain (e.g., English for a US Klaviyo account).
2. Target the form to only appear on the associated domain (e.g., US domain:<https://swak-lip-care.myshopify.com>).
3. Clone the form across multiple accounts.
4. If necessary, adjust the language for each cloned form to match its domain (e.g., translate to French for a French Klaviyo account).
5. Target each cloned form to appear only on its respective domain (e.g., FR domain:<https://swak-lip-care.myshopify.fr>).

If you’re collecting SMS consent via tap-to-text, you’ll also need to choose the appropriate sending number for the account’s domain in each cloned form.

## Create language-specific sign-up forms for multiple domains

### Create a sign-up form for 1 of your regional domains

1. Navigate to the ****Sign-up forms**** tab in Klaviyo’s left-hand navigation.
2. Select ****Create Sign-up Form****.
3. Click ****Create new sign-up form****, or choose a pre-built template from the form library. For this example, we’ll use a template called “Multi-step email & SMS.”
4. Choose a name for your form and a list for new subscribers to collect to. Note that if you’re collecting both email and phone number, you can choose 2 separate lists.
5. Click ****Create Form****.
6. In the form editor, customize the content, design, and behavior of your form to fit your brand and goals. Keep in mind that this form’s language should align with the account’s domain (e.g., English for a US Klaviyo account). Click on any text in the preview to edit it.

- See [getting started with sign-up forms](https://help.klaviyo.com/hc/en-us/articles/360026474752#h_01HAAJKYJ2G0D4XR17NQ0EN7RX) for more guidance on editing your form.

7. Select ****Targeting & behavior > Targeting****.
8. You’ll need to target your form so that it can display on any page within this account’s domain (e.g., homepage, product pages, etc.), and cannot display on any of your other regional domains. To set this up:

- Under **URLs**, click ****Only show on certain URLs****. Next, choose ****Containing****, and enter the website URL associated with this Klaviyo account (e.g., <https://swak-lip-care.myshopify.com>).
- Under **URLs**, click ****Don’t show on certain URLs****. Next, choose ****Containing****, and enter the other regional domain (e.g., <https://swak-lip-care.myshopify.fr>). If you have multiple other regional domains, click ****Add a URL**** and enter each one.

9. Note: while we recommend using [Smart Opt-in](https://help.klaviyo.com/hc/en-us/articles/24743883751451) to collect SMS consent, an alternative opt-in method is [tap-to-text](https://help.klaviyo.com/hc/en-us/articles/9351341171995). However, if you use tap-to-text, you additionally must choose the correct sending region for your form. To do so:

- Navigate to the ****SMS Opt-in**** step at the top.
- Select the ****Subscribe via SMS**** button in the preview.
- Under **Sending Region**, choose the appropriate number for the region you’d like to target with the form (e.g., Canada, United States).

10. When you’re satisfied with your form, click ****Publish****.

### Clone your form across multiple accounts for each domain

1. Once you’ve published your form, navigate back to the ****Sign-up forms**** tab.
2. Next to the form you just created, select the ****3 dots > Clone****.
3. Choose ****Clone to multiple accounts > Continue****.
4. Check the account(s) you’d like to copy your form to, then click ****Next****. Note that you can select up to 100 accounts.
5. Optional: edit the name of the cloned form for each account.
6. Click ****Next****.
7. Review and fix any of the following errors so your form is set up correctly:

- Destination list.
- Targeting settings (optional).
- Age-gating block (if needed).
- SMS settings (if needed).

8. Click ****Next****.
9. Review the information in each account to confirm it’s correct.
10. Select ****Distribute form****.

### Adjust the cloned form for a different regional domain

Once your sign-up forms have successfully cloned and the page refreshes:

1. Click on your account name in the bottom left corner.
2. Select the account that you cloned your form to.
3. Navigate to the ****Sign-up forms**** tab, then select the cloned form.
4. In the form editor, click on any of the text in the preview to edit and translate it. Keep in mind that this form’s language should align with the account’s domain (e.g., French for a FR Klaviyo account).

   Note that you can also customize the **Required text** and **Invalid text** for input fields in your form.
5. Select ****Targeting & behavior > Targeting****.
6. Under **URLs**, click ****Only show on certain URLs****.
7. Choose ****Containing****, then enter the website URL associated with this Klaviyo account (e.g., [https://swak-lip-care.myshopify.fr](https://swak-lip-care.myshopify.com)).
8. Note: while we recommend using [Smart Opt-in](https://help.klaviyo.com/hc/en-us/articles/24743883751451) to collect SMS consent, an alternative opt-in method is [tap-to-text](https://help.klaviyo.com/hc/en-us/articles/9351341171995). However, if you use tap-to-text, you additionally must choose the correct sending region for your form. To do so:

- Navigate to the ****SMS Opt-in**** step at the top.
- Select the ****Subscribe via SMS**** button in the preview.
- Under **Sending Region**, choose the appropriate number for the region you’d like to target with the form (e.g., France).

9. When you’re satisfied with your form, click ****Publish****.
10. Repeat steps 12-16 for any other accounts that you cloned the form to.

You’ll now have language-specific sign-up forms designated for each of your regional domains.

## Next steps

Create a separate email and SMS welcome series in each account to thank people who sign up for each channel. To do so quickly, you can [use the multi-account cloning feature](https://help.klaviyo.com/hc/en-us/articles/24898429283739) like we did here.

## Additional resources

- [Getting started with portfolios](https://klaviyo.zendesk.com/hc/en-us/articles/24656917054747)
- [How to change the language for your account](https://klaviyo.zendesk.com/hc/en-us/articles/25956849989531)
- [Basics: multi-national SMS sending with Klaviyo](https://klaviyo.zendesk.com/hc/en-us/articles/23740503987099)