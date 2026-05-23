---
id: 360031724251
title: "How to embed a sign-up form on your BigCommerce order confirmation page"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360031724251-How-to-embed-a-sign-up-form-on-your-BigCommerce-order-confirmation-page"
section: "BigCommerce best practices"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:56:51Z"
language: en
---

## You will learn

Learn how to embed a sign-up form on your BigCommerce confirmation page to collect additional information from customers after they finish the checkout process. These recent customers are already interested in your brand, so the confirmation presents a great opportunity to further engage with them.

## Before you begin

Make sure that you've [integrated with BigCommerce](https://help.klaviyo.com/hc/en-us/articles/115005082547) and checked the setting **Automatically add Klaviyo onsite JavaScript**.

## Build your form

You can create a sign-up form and embed it on your confirmation page to ask relevent questions of your customers after they checkout. For example, you could ask questions to learn more about how often a customer uses your products, or what potential new products they might be interested in buying.

To build your sign-up form:

1. In Klaviyo, navigate to ****Sign-up forms > Create Sign-up form > Build from scratch****.
2. In the menu that appears, name your form and select a list for new subscribers to submit to.
3. Select ****Embed**** as the form type.
   ![embed form .jpg](https://klaviyo.zendesk.com/hc/article_attachments/34409763651355)
4. Click ****Save and  design****.
5. This will bring you into the form editor where you can edit the following styles:
   - **Styles**: Edit the appearance of your form to match your brand, such as form or input field styles and font type. You can also edit any text by clicking on it and replacing the default language with your own.
   - **Add blocks**: Here you can add content to your form in order to collect information, such as a text box for a question or a date field for a birthday. Make sure to set a [profile property](https://help.klaviyo.com/hc/en-us/articles/115005074627-Profile-properties-reference) with each field you add, and to not overwhelm customers with too many questions.
   - **Targeting and behavior**: Choose whether you want the form to appear on desktop, mobile, or both. Keep your form set to either ****Show to all visitors**** or ****Don't show to existing Klaviyo profiles.****
6. In the menu bar, select ****Success**** to edit the page that displays after someone submits your form.
7. When you're satisfied with your form's design, click ****Publish****.
8. From the modal that appears, copy your embed code so that you have it ready to paste.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/34409763654299)
9. Click ****Publish****.

Your form will not appear on your site until you've pasted the embed code in your site code.

Verify the [opt-in settings](https://help.klaviyo.com/hc/en-us/articles/115005251108-The-Double-Opt-In-Process) for that list so that the customer experience is seamless. If the list is double opt-in, you will want to edit the confirmation pages. All Klaviyo lists are set to double opt-in by default.

## Add the embed to your BigCommerce site

1. Navigate to your BigCommerce admin.
2. Go to ****Storefront > Script Manager**** and click ****Create a Script.****
3. Name the script and configure it with the following:
   - Location: Head
   - Description (optional): Describe the purpose of the script
   - Pages where the script will be added: Order confirmation
   - Script type: Script
     ![The Create a Script page in BigCommerce where you can fill in the location, description, pages where the script will be added, and script type.](https://klaviyo.zendesk.com/hc/article_attachments/28704485135131)
4. Delete the script contents and instead paste the following code to add klaviyo.js to your confirmation page. Note that you need to do this even if you previously installed klaviyo.js on your website:

   ```
     <script src="https://static.klaviyo.com/onsite/js/PUBLIC_API_KEY/klaviyo.js" async=""></script>
     <script>
        document.addEventListener("DOMContentLoaded", function() {
          var elem = document.createElement('div');
        elem.className = 'klaviyo-form-FORM_ID'
        document.body.appendChild(elem);
        });</script>
   ```
5. In the snippet above, replace `PUBLIC_API_KEY` with [your site's public API key.](https://klaviyo.zendesk.com/hc/en-us/articles/115005062267)
6. In the snippet above, replace `FORM_ID` with your form's ID. To find your form ID, navigate to the embedded form in your Klaviyo account. The form ID is the 6 letter code at the end of the URL.
   ![Confirms3.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28704477015963)
7. When you have filled in all the details for the script, click ****Save****.

Your embed form will now display at the bottom of the page after someone places an order. Depending on your theme, you may want to edit the border, padding, or size of your form in the **Styles** section to ensure that it matches the look and feel of your order confirmation page; publish any changes you make to see them reflected.

## Next steps

After you start collecting responses with your embedded form, each submission will be stored on the customer's profile as a [custom property](https://help.klaviyo.com/hc/en-us/articles/115005074627-Add-Custom-Properties-to-a-Contact-Profile#how-to-use-custom-properties5), available to use in segments, flows, and email templates.

Based on the responses, you can branch the [post-purchase](https://help.klaviyo.com/hc/en-us/articles/360028872611-Guide-to-Creating-a-Post-Purchase-Flow) experience. You may also want to branch your [welcome series](https://help.klaviyo.com/hc/en-us/articles/115002775172-Guide-to-Creating-a-Welcome-Series) based on this data or [create relevant segments](https://help.klaviyo.com/hc/en-us/articles/115005237908-Guide-to-Creating-Segments#segment-conditions2) to send campaigns to. For example, let's say we decide to release a new mascara. Since we're collecting product interest data on this embedded form, we can notify anyone who told us they were interested in mascara in the product release.

## Additional resources

- [Getting started with sign-up forms](https://help.klaviyo.com/hc/en-us/articles/360026474752)
- [How to embed a sign-up form on your website](https://help.klaviyo.com/hc/en-us/articles/360006897412)