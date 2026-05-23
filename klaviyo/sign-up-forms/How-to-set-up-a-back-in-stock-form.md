---
id: 38767539287323
title: "How to set up a back in stock form"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/38767539287323-How-to-set-up-a-back-in-stock-form"
section: "Build and use forms"
category: "Sign-up forms"
category_slug: "sign-up-forms"
klaviyo_updated: "2026-04-21T13:56:55Z"
language: en
---

Learn how to set up and customize a back in stock sign-up form for your online store. Using Klaviyo’s form editor, you can customize both the “Notify me” button that appears when a product on your site is out of stock, and the form your customers use to sign up for back in stock notifications via email or SMS.

## Before you begin

Back in stock forms are only available for Shopify and BigCommerce. If you’re using a different platform, refer to our [back in stock flow installation guide](https://help.klaviyo.com/hc/en-us/articles/115003872251) instead.

In this article, you’ll learn how to:

- Remove any existing Klaviyo back in stock code from your Shopify or BigCommerce store (if applicable)
- Enable and customize your back in stock button and sign-up form

## How the back in stock form works on your storefront

After you publish a back in stock form, Klaviyo automatically displays a customizable “Notify me” button on any product page where inventory is out of stock. You can customize this button in the form editor, alongside the form itself. The button appears and disappears automatically based on your product inventory.

When a shopper clicks the “Notify me” button, your form appears, allowing them to choose how they want to be notified when the product is available again, depending on how you’ve configured your form:

- Email: If you include an email field, shoppers can enter their email address to receive a restock alert by email. You can also add an optional checkbox for shoppers to opt in to receive promotional marketing emails.
- Text messaging: If you include a phone number field, shoppers can enter their phone number to receive a restock alert by text message. In order to receive these text alerts, shoppers must provide explicit consent to receive promotional text messages. This consent is required and cannot be made optional, and your disclosure language must be present.

After a shopper submits the form, Klaviyo logs a **Subscribed to Back In Stoc**k event on their profile. This event is used to trigger your [back in stock flow](https://help.klaviyo.com/hc/en-us/articles/115003872251). Shoppers who subscribe will automatically enter the flow and will receive a notification when the product is restocked.

Note that A/B testing and non-traditional SMS opt-in methods (e.g., smart opt-in and tap-to-text) are not supported for back in stock forms.

## Remove existing back in stock code snippet

If you previously installed Klaviyo’s back in stock code snippet, you must first remove it to prevent duplicate buttons or forms.

Click one of the arrows below to expand the section below for instructions on removing the code from your store platform. If you’re unsure about which script or code to remove, contact your developer or refer to your original installation notes.

If you haven’t added any back in stock code before, skip ahead to the next section on creating your back in stock form.

****Remove back in stock code from a Shopify siteIn your Shopify Admin, go to Online Store > Themes.Next to your published theme, click the additional options menu (3 dots), then select Edit Code.Open the theme.liquid file.Use the find shortcut (Command+F on Mac or Control+F on Windows) to search the word “backinstock” within the file.Find and delete the following code snippet:<script src="https://a.klaviyo.com/media/js/onsite/onsite.js"></script>
<script>
var klaviyo = klaviyo || [];
klaviyo.init({
account: "PUBLIC\_API\_KEY",
platform: "shopify"
});
klaviyo.enable("backinstock",{
trigger: {
product\_page\_text: "Notify Me When Available",
product\_page\_class: "button",
product\_page\_text\_align: "center",
product\_page\_margin: "0px",
replace\_anchor: false
},
modal: {
headline: "{product\_name}",
body\_content: "Register to receive a notification when this item comes back in stock.",
email\_field\_label: "Email",
button\_label: "Notify me when available",
subscription\_success\_label: "You're in! We'll let you know when it's back.",
footer\_content: '',
additional\_styles: "@import url('https://fonts.googleapis.com/css?family=Helvetica+Neue');",
drop\_background\_color: "#000",
background\_color: "#fff",
text\_color: "#222",
button\_text\_color: "#fff",
button\_background\_color: "#439fdb",
close\_button\_color: "#ccc",
error\_background\_color: "#fcd6d7",
error\_text\_color: "#C72E2F",
success\_background\_color: "#d3efcd",
success\_text\_color: "#1B9500"
}
});
</script>Click Save.Return to your website and refresh a product page for an out-of-stock item. Verify that the "Notify me" button is no longer visible.****

****Remove back in stock code from a BigCommerce site****

1. In your BigCommerce admin, go to ****Storefront > Script Manager****.
2. Look for any scripts related to Klaviyo’s back in stock feature. These scripts may have a name like “Klaviyo Back in Stock” or be labeled according to your previous installation.
3. Next to the script, click the additional options (3 dots) menu, and choose ****Delete**** to remove the script.

   If you originally pasted the Klaviyo back in stock code directly into a theme file (e.g., in footer.html), you must manually remove the code from there. To do this, go to ****Storefront > Themes > Edit Theme Files****, find the file containing the script, and delete the code snippet.
4. Save your changes.
5. Return to your website and refresh a product page for an out-of-stock item. Verify that the "Notify me" button is no longer visible.

## Create a back in stock form

You can only have one back in stock form in your account at a time, whether it is published or in draft mode. If a back in stock form already exists, you must delete it before creating a new one.

1. In Klaviyo’s main navigation, select the ****Sign-up forms**** tab.
2. Click ****Create form****.
3. In the search bar, type “back in stock” and select a pre-built **Back in Stock** template to customize.
   ![Three Back in Stock popup form templates displayed for selection on the Create Form page.](https://klaviyo.zendesk.com/hc/article_attachments/38774168078875)

   - If you would prefer to start from a blank form, click ****Build a blank form**** and then choose ****Back in stock**** as the form type.
4. Choose what list(s) you want to collect email and SMS sign-ups to.
5. Click ****Create form****.
   ![Back in Stock Multi-step popup form setup screen with options for email and SMS subscriber lists.](https://klaviyo.zendesk.com/hc/article_attachments/38774168081435)
6. Select the ****Product display button**** step in the menu bar. Note that this must always be the first step of the form, and cannot be deleted.
7. In the editing menu on the left, choose where the button should appear on your product pages:

   - ****Replace add to cart button****: The "Notify me" button will replace the "Add to Cart" button for items that are out of stock.
   - ****Stacked****: The "Notify me" button will appear beneath the "Add to Cart" button (when it’s displayed as "Sold Out").![Product display button settings with options to replace or stack the ](https://klaviyo.zendesk.com/hc/article_attachments/38774134029979)

   If you want to place the "Notify me" button in a different location, see the section below on using the `klaviyo-bis-trigger` for custom button placement.
8. Use the options for **Text, Button style, Border,** and **Drop shadow** to update the label and styling of the "Notify me" button.
9. Switch to the ****Email opt-in**** step and use the ****Styles**** menu to adjust colors, fonts, and layout so your form matches your brand.
   ![Back in Stock form editor showing style customization options and a preview of the email opt-in popup.](https://klaviyo.zendesk.com/hc/article_attachments/38774168089371)
10. Apply the styling to each subsequent step in your form, such as SMS opt-in or Success steps, by clicking each step in the menu bar and repeating step 9.

    Every input step must include at least 1 email or SMS input field. If a step has both, you can remove 1. If a step has only 1 of the 2 inputs, it cannot be deleted from that step. You can, however, delete the entire step if you only want to collect 1 channel. Email marketing consent is optional and can be removed.
11. Shopify only (optional): To control where the "Notify me" button appears, go to ****Targeting and behavior > Targeting****, and use [Shopify tags](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/using-tags) to include or exclude specific products for which the button should appear.
    ![BiS12.jpg](https://klaviyo.zendesk.com/hc/article_attachments/39062525638939)
12. When you’re satisfied with your form, click ****Publish**** to set it live. Once your form is live, your product display button will automatically appear when an item on your site goes out of stock.
13. After publishing, you’ll see a prompt in the publish confirmation modal to set up your back in stock flow.

- If you already have a back in stock flow set up with the **Subscribed to Back in Stock** metric as the trigger, it will begin working with your new back in stock form automatically. You do not need to create another one; click ****Dismiss****.
- If not, click ****Exit and create flow****, then head to our guide on [How to set up a back in stock flow](https://help.klaviyo.com/hc/en-us/articles/115003872251#h_01HBBYWCR7VMA1Q70QTGAXQBGR).

![Modal with the message ](https://klaviyo.zendesk.com/hc/article_attachments/38774134032027)

## Analytics for back in stock forms

You can monitor metrics for your back in stock form on its analytics page, including **Back in stock submits** and **Marketing opt-ins**. Note that the **Submit rate** is calculated based on the number of back in stock subscriptions, not marketing consent.

![Analytics dashboard showing submit rate, back in stock submits, marketing opt-ins, and viewed form metrics.](https://klaviyo.zendesk.com/hc/article_attachments/38774168091291)

This page also includes graphs of the form’s data by step and by data collection type:

- **Engagement**: This refers to back in stock subscriptions (e.g., when a shopper signs up for email restock alerts).
- **Marketing opt-ins**: This refers to when shoppers provide consent to receive promotional messages, either by checking the marketing email opt-in box or by submitting a phone number, since text alerts always require promotional SMS consent.

## Troubleshooting back in stock

If your back in stock experience isn’t working as expected, review the following common issues.

### The "Notify me" button isn't appearing or is not in the right location

If the "Notify me" button is missing from your product page or you want to configure it to appear in a different, custom location, you can manually control its placement using the `klaviyo-bis-trigger` HTML attribute.

```
<a class="klaviyo-bis-trigger" href="#">Notify Me When Available</a>
```

Add this attribute to the specific HTML element where you want the "Notify me" button to be rendered, and Klaviyo will then display the button at that location instead of the default location. This solution can be helpful if you're using a custom or non-standard theme; however it will not always resolve a missing button issue. If you're having trouble configuring a custom button location, consult your developer.

### Compatibility with Shopify’s “Continue selling when out of stock” setting

Klaviyo’s back in stock feature does not work with Shopify’s “Continue selling when out of stock” setting. If this setting is enabled, the product always appears available, even with zero inventory. As a result:

- The “Notify Me” button and back in stock form will not appear.
- No back in stock emails will be sent, since Klaviyo cannot detect when inventory is restocked to trigger the flow.

To use Klaviyo’s back in stock feature, make sure “Continue selling when out of stock” is disabled for those products.

### Are you using a Retina theme?

The Retina theme (from Out of the Sandbox) comes with a "Notify Me" form built into the product page. You will need to disable the default button that comes with your theme in order for the Klaviyo code to function.

### Are you using a theme that hides a product if all variants are sold out?

If your Shopify theme hides a product when all the variants are sold out, you'll need to identify this area of the code in your product.liquid file and edit it to display all products, regardless of stock level.