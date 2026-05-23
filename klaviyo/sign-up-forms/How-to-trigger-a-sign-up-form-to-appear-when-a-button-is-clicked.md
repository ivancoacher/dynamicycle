---
id: 4418052317339
title: "How to trigger a sign-up form to appear when a button is clicked"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/4418052317339-How-to-trigger-a-sign-up-form-to-appear-when-a-button-is-clicked"
section: "Form best practices"
category: "Sign-up forms"
category_slug: "sign-up-forms"
klaviyo_updated: "2026-04-21T13:55:01Z"
language: en
---

## You will learn

Learn how to trigger a sign-up form to appear on your website when a visitor clicks on a certain button. This guide will walk you through adjusting your form to show on a custom trigger, creating and adding a new button to your site, and pasting a short code snippet into your site’s HTML so that clicking on the button triggers the sign-up form.

If you're a developer and want to custom-code a trigger for your sign-up form, head to our developer resource on how to [custom trigger a popup or flyout form](https://developers.klaviyo.com/en/docs/how_to_custom_trigger_a_popup_or_flyout_form).

Because pasting this code requires access to your site's HTML and ecommerce platform, our support team is unable to offer hands-on assistance. If you don't have a developer on your team and are not comfortable adding the code yourself, [consider reaching out to a Klaviyo Partner for assistance](https://klaviyo.partnerpage.io/).

## Create a new button

![](https://fast.wistia.com/embed/medias/gssdg2muww/swatch)

First, create a new button on your website that'll trigger the sign-up form to appear when it's clicked. You'll need to make sure your sign-up form is set up correctly in Klaviyo before adding the button to your site. To do so:

1. [Create a new sign-up form](https://help.klaviyo.com/hc/en-us/articles/360026474752-Guide-to-Creating-a-Signup-Form) to appear when the button is clicked, or choose a form that you've already created.
2. In the ****Styles**** tab, your **Form Type** should be set to either ****Popup,**** ****Flyout or Full Page****. Embedded forms cannot be triggered when a button is clicked.
3. In the ****Targeting & Behaviors**** tab, select  ****Only show on custom trigger**** under **Timing.**
   ![The Timing section of the Targeting and behaviors tab in the form editor showing the option to Show on a custom trigger selected.](https://klaviyo.zendesk.com/hc/article_attachments/28705664743067)
4. When you're satisfied with your form's design and content, click ****Publish.****
5. Next, open the editor for your form and choose the following settings
6. Copy the code below:

   ```
   <button class="klaviyo_form_trigger">Click here</button>
   ```
7. Paste the code into the HTML of any page on your website that you'd like the button to appear on. This button will use the default styles from your site’s template. If you would like to customize the button's appearance further, consult your developer or a [Klaviyo Partner](https://connect.klaviyo.com/).

Note that if you add multiple buttons to your site that each trigger different sign-up forms, you’ll need to use a unique name to classify each button (e.g., klaviyo\_form\_trigger1, klaviyo\_form\_trigger2).

## Set the button to trigger your sign-up form

![](https://fast.wistia.com/embed/medias/l2a8gcpnen/swatch)

Now that you've added a new button to your website, you'll next need to set up the trigger so your sign-up form appears when it's clicked. Set up the trigger by adding a small, custom JavaScript snippet to your site:

1. Copy the code snippet below:

   ```
   <script type="text/javascript">
   	document.querySelector('.klaviyo_form_trigger').addEventListener('click', function (){
   		window._klOnsite = window._klOnsite || [];
   		window._klOnsite.push(['openForm', 'FORM_ID']);
   	});
   </script>
   ```
2. Paste the code snippet directly below the button code that you added to your site in the last section.
3. In the snippet you just pasted, replace FORM\_ID with your sign-up form's ID.

   - To find form ID, navigate back to Klaviyo and open the form editor for your sign-up form. Copy the 6-digit code at the end of the URL to add in your code snippet; this is the Form ID.![The URL for an example sign-up form in the form editor with the six digit code at the end highlighted to show the unique Form ID.](https://klaviyo.zendesk.com/hc/article_attachments/28705637889691)
4. The completed code should include the new button code, and the sign-up form trigger with your unique form ID. Make sure to paste this on every page where you added the button code.

   - Here’s an example of the completed code in a Shopify page editor:![An example of the completed code showing the button code and form trigger in a Shopify page editor.](https://klaviyo.zendesk.com/hc/article_attachments/28705664741275)

   If you adjusted the button’s class in the last step (i.e., you replaced klaviyo\_form\_trigger with some other text or added a number), make sure to update this code with the text you used.
5. Save your changes.

## Test your button

Once you’ve saved all the changes to your site’s code, visit your site and click your new button. When you do, the sign-up form will appear.

Having trouble? Head to Klaviyo’s [Community Forum](https://community.klaviyo.com/) for guidance from other Klaviyo users.