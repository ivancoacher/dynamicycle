---
id: 360006897412
title: "How to embed a sign-up form on your website"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360006897412-How-to-embed-a-sign-up-form-on-your-website"
section: "Build and use forms"
category: "Sign-up forms"
category_slug: "sign-up-forms"
klaviyo_updated: "2026-05-11T10:58:10Z"
language: en
---

## You will learn

Learn how to add an embed sign-up form onto a specific page or location of your website (e.g., the footer), so shoppers looking to learn more about your brand can easily sign up. Embedding a sign-up form in the footer of your site to work in tandem with your other published forms is a Klaviyo best practice for optimizing list growth.

To add an embed form to your site, you’ll need to:

1. Create and customize a new embed form in Klaviyo.
2. Copy the form’s embed code from the publish modal.
3. Paste the embed code into your site’s files.

Because pasting form code requires access to your site’s HTML and ecommerce platform, our support team is unable to offer hands-on assistance. If you don’t have a developer on your team, consider reaching out to a [Klaviyo partner](https://connect.klaviyo.com/) for assistance.

## Before you begin

Before creating your sign-up form, make sure that [sign-up form functionality is enabled in your Klaviyo account](https://help.klaviyo.com/hc/en-us/articles/360002035871). This ensures that forms published in Klaviyo display properly  on your site and sync all necessary data.

For embed forms to work, you’ll need:

- Sign-up form functionality enabled. This is also often referred to as “onsite tracking” installed.
- The embed code pasted on your site wherever you want the form to display.

Note that pasting the embed code is unique to embed forms. Popup, flyout, and full page forms do not require any pasting of code, and can be [published directly from Klaviyo’s form builder](https://help.klaviyo.com/hc/en-us/articles/360026474752)

Effective December 06, 2024: Klaviyo has improved the way views are calculated for embed forms to more accurately measure engagement. Views for embed forms will now only be recorded when the form is visible in the user's viewport. This change may result in a noticeable change in view counts and increase in submit rates, particularly for forms embedded in a site's footer, as these will only be counted if a visitor scrolls down enough for the form to partially enter their viewport.

## Add an embed form to your site

If you’re using Shopify, BigCommerce, or WooCommerce, subscribers who sign up through your platform’s embed form are automatically added to your Klaviyo list via the integration. Because of this, you do not need to replace your integration’s embed form with one from Klaviyo, though you can still create one in Klaviyo if you want subscribers to collect to a different list.

### Create and customize a new embed form in Klaviyo

1. Select the ****Sign-up forms**** tab from Klaviyo’s left-hand navigation.
2. Select ****Create form****. From here, you can either:
   - Customize a pre-built template from the form library. Click the dropdown next to **All Types**, then select ****Embed**** to filter the form library to show all pre-built embed form templates.
   - Begin with a blank embed form template by selecting ****Create new form**** in the top right corner.
3. On the creation modal that appears:
   - Name your form.
   - Choose which list new subscribers will join.
   - Confirm ****Embed**** as your form type.
     ![The Create sign-up form modal showing an example form being created with Embed seleected as the form type.](https://klaviyo.zendesk.com/hc/article_attachments/32014531739931)
4. Click ****Save and design****.
5. Use the editor to style your form and add any desired blocks or input fields. For guidance while customizing your form, see [getting started with sign-up forms](https://help.klaviyo.com/hc/en-us/articles/360026474752#h_01HAAJKYJ2G0D4XR17NQ0EN7RX).

   If you plan on embedding your form in the footer of your site, we recommend asking for email addresses only to improve the volume of opt-ins.
6. When you’re satisfied with your form, click ****Publish****. Note that the form will not appear on your site just yet; you must also paste the embed code on your site in order for it to be live.
7. In the **Published successfully** modal that appears, click ****Copy**** to copy the embed code to your clipboard. This is the code you’ll need to paste in your site files in the next section of this article.
   ![The Published successfully modal showing for a recently published form with the embed code highlighted to copy.](https://klaviyo.zendesk.com/hc/article_attachments/32014546750235)

Note that a form's embed code can also be found in the ****Targeting & behavior**** tab in the form editor.

![An example form's embed code being copied from within the display menu in the form editor.](https://klaviyo.zendesk.com/hc/article_attachments/35307068829979)

### Paste the embed code on your site

After publishing your form in Klaviyo and copying the embed code, you’ll need to paste this code into your website files for the form to display. The location for pasting the code depends on where you want the form to appear (e.g., in a theme file or specific page file), and may vary based on integration.

Find the platform that you use on the list below, then head to the article linked beneath it for a more specific guide on pasting the embed code for that integration.

If you do not see your platform, see the “Other” bullet point.

- Bigcommerce
  For BigCommerce, paste the embed code in your site’s files where you want it to appear.
  - Head to [Add the embed code to your Bigcommerce site](https://help.klaviyo.com/hc/en-us/articles/360022594552#adding-the-embed-code-to-your-site2).
- Shopify
  For Shopify, add the Klaviyo Embedded Form app to your page template and paste the form’s embed code.
  - Head to [Add the embed code to your Shopify site](https://help.klaviyo.com/hc/en-us/articles/32004602396443).
- Square
  For Square, paste the embed code in your site’s files where you want it to appear.
  - Head to [Add the embed code to your Square site](https://help.klaviyo.com/hc/en-us/articles/18229698831003#01H8MF2120D8BRT8SP5GFMHT93).
- WooCommerce
  For WooCommerce, paste the embed code in your site’s HTML.
  - Head to [Add the embed code to your WooCommerce site footer.](https://help.klaviyo.com/hc/en-us/articles/360030058772#add-the-embed-code-to-your-site2)
- Other platforms
  If your platform isn’t listed above, or you use a custom integration that does not natively integrate with Klaviyo, you’ll need to make sure that 2 code snippets are pasted on your site for the embed form to work:
  - Onsite tracking (also known as Klaviyo.js) to enable sign-up form functionality.
    - Note that many platforms automatically add onsite tracking to your site when you integrate (including Wix, Prestashop, Magento 1 and 2, etc.). Check your platform’s integration settings in Klaviyo to confirm this option is selected.
      - If your platform doesn’t have a native Klaviyo integration, you must [add onsite tracking manually.](https://help.klaviyo.com/hc/en-us/articles/115005076767#h_01GMEAQZXKADF4FR7P1FMNC7EB)
  - The specific form’s embed code
    - Once onsite tracking is enabled, you must paste your form’s embed code into your site’s HTML/source code wherever you’d like it to appear (e.g., the footer).
      - A form's embed code can be copied from the ****Targeting & behaviors**** tab within the form editor.

Make sure to save any changes made to your site. If you are not comfortable editing code on your site, consider [contacting a Klaviyo partner](https://klaviyo.partnerpage.io/) for assistance.

## Next steps

Once you have published your embed form in Klaviyo, pasted its embed code onto your site, and saved your changes, head to your website and refresh the page.

The embed form should appear on your site wherever you pasted the embed code.

## Troubleshooting embed forms

If your embed form is live in Klaviyo but not displaying on your site, consult the following troubleshooting tips:

- Refresh your browser cache.
- Verify that your website is properly [integrated with Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115000256472), and that your site is also live.
- Confirm that you have [enabled sign-up forms for your account](https://help.klaviyo.com/hc/en-us/articles/360002035871) (this is the same thing as enabling onsite tracking).
- Ensure that you saved the changes on your website after pasting the embed code.
- In Klaviyo’s sign-up form editor, navigate to the ****Targeting & behavior**** section and review the following:
  - In the ****Display**** section, verify that:
    - The embed code pasted on your site correctly matches the code provided by Klaviyo
    - The device settings in Klaviyo correspond to the device you’re using to view the form
  - In the ****Targeting**** section, verify that:
    - You meet any narrowed **Visitor** settings
    - The form is set to show on the URL you’re viewing, and includes any specified UTM parameters
    - Your location fits any geo-locating set for the form
    - Your cart meets any cart content requirements configured for the form
- Rerun the test on a new, incognito (“private”) browser window.
- Confirm that only 1 Klaviyo account is integrated with your site. [Learn more about integrations.](https://help.klaviyo.com/hc/en-us/articles/115005081007)

### Other potential reasons for form not appearing

- If you have custom CSS present on your site, this may be conflicting with Klaviyo’s onsite tracking snippet (“Klaviyo.js”) and interfering with your form. Have your developer use your browser’s developer tools to inspect the site’s code and identify the problem or [contact support](https://help.klaviyo.com/hc/en-us/articles/115001002272).
- If you’re using a single page application (“SPA”) site, your setup may be causing the form to appear intermittently. Consult your developer for assistance.

## Additional resources

- [How to contact support](https://klaviyo.zendesk.com/hc/en-us/articles/115001002272)
- [Troubleshooting sign-up forms](https://klaviyo.zendesk.com/hc/en-us/articles/115005249348)
- [Getting started with sign-up forms](https://klaviyo.zendesk.com/hc/en-us/articles/360026474752)