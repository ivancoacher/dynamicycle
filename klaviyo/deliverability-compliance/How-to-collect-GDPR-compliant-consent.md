---
id: 360003536031
title: "How to collect GDPR-compliant consent"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360003536031-How-to-collect-GDPR-compliant-consent"
section: "GDPR and CCPA"
category: "Deliverability & compliance"
category_slug: "deliverability-compliance"
klaviyo_updated: "2026-05-11T11:07:32Z"
language: en
---

## You will learn

Learn how consent is stored in Klaviyo to help you be GDPR compliant, and how to collect GDPR to compliant consent.

GDPR (General Data Protection Regulation) is a law enacted by the European Commission in 2016 that went into effect on May 25, 2018. It’s designed to protect the privacy of all EU citizens, including when those citizens engage with businesses located outside of the EU, by imposing regulations around personal data. For more information on GDPR, [check out our blog series](https://www.klaviyo.com/blog/gdpr-for-ecommerce).

Because GDPR requires informed and freely given consent before you send marketing emails to a contact, having GDPR-compliant sign-up forms is critical. While we still recommend you contact legal counsel to review the language relayed on your forms, Klaviyo provides built-in GDPR-compliant forms as a starting point. If you have an existing list that you would like to import into Klaviyo and you have already collected consent, check out our [guide to applying consent properties to an existing list](https://help.klaviyo.com/hc/en-us/articles/115005078967-Create-and-Add-Contacts-to-a-New-List#upload-and-map-your-data).

The information provided in this guide is intended to be educational and should not be construed as legal advice. Klaviyo encourages all of our customers, and all ecommerce merchants, to seek legal advice for counsel on how they specifically should ensure that they are GDPR compliant.

## Use a GDPR-compliant form

After you [install Klaviyo sign-up forms on your site](https://help.klaviyo.com/hc/en-us/articles/360002035871-Install-Klaviyo-Signup-Forms), you can start building forms within the ****Sign-up forms**** tab of your account.

Click ****Create from Scratch****, then ****Enable Data Protection Fields**** to ensure that the default template includes GDPR-compliant language.

![Signup form creation modal with Enable Data Protection Fields checkbox](https://klaviyo.zendesk.com/hc/article_attachments/28716329606683)

You can edit the language of this form or add additional fields using checkboxes to suit your needs. Bear in mind that GDPR requires granular consent, which means that subscribers must have the option to subscribe to some, but not all, types of marketing. For example, a subscriber may want to receive emails from you, but not be retargeted by your business on social media. Using checkboxes allows subscribers to choose as many or as few types of marketing they would like to receive from you.

Any value that a subscriber selects will be stored as a **$consent** property on their profile. Consent is recorded as a [list data type](https://help.klaviyo.com/hc/en-us/articles/115005237648-Data-Types#list), and as such may contain any number of values.

![Signup form with email address field](https://klaviyo.zendesk.com/hc/article_attachments/28716329581339)

Once your form is styled to suit your needs and includes the necessary checkboxes, you can [publish it](https://help.klaviyo.com/hc/en-us/articles/360002049952) on your site so that, going forward, you collect and track consent as required by the GDPR.

Checkboxes should not be pre-checked and explicit user action is required. However, note that users who submit the form will be subscribed regardless of whether the checkbox is selected. In this case, you should [segment](https://help.klaviyo.com/hc/en-us/articles/360040841811) customers based on the [custom property](https://help.klaviyo.com/hc/en-us/articles/115005074627) associated with that checkbox, indicating the profile has consented to email.

Additionally, you may choose to only show this form to browsers located in the EU or who are **not** in the EU. To do this, navigate to ****Targeting &**** ****Behaviors > Targeting> By Location****. Here, you can specify where to show/hide a form to browsers in specific locations. Klaviyo determines a browser's location using their IP address.

![Behavior tab for signup to control visibility settings based on location](https://klaviyo.zendesk.com/hc/article_attachments/28716302267163)

## Use a GDPR-compliant embedded form

In addition to a popup or flyout, you may want to include a GDPR-compliant embedded form on your site. To do this, create a GDPR-compliant embedded form in the Sign-up Form Builder, as outlined above.

Alternatively, you can copy the code provided below and [install it on your site.](https://help.klaviyo.com/hc/en-us/articles/115005249588-Add-and-Customize-an-Embedded-Signup-Form) Note that you must replace each **LIST\_ID** value with your newsletter list's ID to ensure that contacts are added to the list. [Learn more about how to find the ID for a given list](https://help.klaviyo.com/hc/en-us/articles/115005078647-Find-a-List-ID).

```
<form id="email_signup" class="klaviyo_styling klaviyo_gdpr_embed_LIST_ID" action="//manage.kmail-lists.com/subscriptions/subscribe" data-ajax-submit="//manage.kmail-
lists.com/ajax/subscriptions/subscribe" method="GET"
target="_blank" novalidate="novalidate">

 <input type="hidden" name="g" value="LIST_ID">

 <input type="hidden" name="$fields" value="$consent">

 <input type="hidden" name="$list_fields" value="$consent">

 <div class="klaviyo_field_group">

 <label for="k_id_email">Newsletter Sign Up</label>

 <input class="" type="email" value="" name="email" id="k_id_email" placeholder="Your email"/>

 <div class="klaviyo_field_group klaviyo_form_actions">

 <div class="klaviyo_helptext"> How would you like to hear from us? (please select at least one option) </div>

 <input type="checkbox" name="$consent" id="consent-email" value="email">

 <label for="consent-email" >Email</label><br>

 <input type="checkbox" name="$consent" id="consent-web" value="web" >

 <label for="consent-web">Online advertisements</label>

 <div class="klaviyo_helptext klaviyo_gdpr_text"> We use email and targeted online advertising to send you product and services updates, promotional offers and other marketing communications based on the information we collect about you, such as your email address, general location, and purchase and website browsing history. <br>

<br>

 We process your personal data as stated in our Privacy Policy {Insert privacy policy link}. You may withdraw your consent or manage your preferences at any time by clicking the unsubscribe link at the bottom of any of our marketing emails, or by emailing us at {insert customer support email address}.</div>

 </div>

 </div>

 </div>

 <div class="klaviyo_messages">

 <div class="success_message" style="display:none;"></div>

 <div class="error_message" style="display:none;"></div>

 </div>
 <div class="klaviyo_form_actions">

 <button type="submit" class="klaviyo_submit_button">Subscribe</button>
 </div>

</form>
<style type="text/css">

.klaviyo_styling.klaviyo_gdpr_embed_LIST_ID,

.klaviyo_condensed_styling.klaviyo_gdpr_embed_LIST_ID {

 font-family: "Helvetica Neue", Arial;

}.klaviyo_styling.klaviyo_gdpr_embed_LIST_ID .klaviyo_helptext,

.klaviyo_condensed_styling.klaviyo_gdpr_embed_LIST_ID .klaviyo_helptext {

 font-family: "Helvetica Neue", Arial;

 padding-top: 10px;
 padding-bottom: 10px;

}
.klaviyo_styling.klaviyo_gdpr_embed_LIST_ID .klaviyo_gdpr_text,

.klaviyo_condensed_styling.klaviyo_gdpr_embed_LIST_ID .klaviyo_gdpr_text {

 font-size: 14px;

 line-height: 1.3;

}

.klaviyo_styling.klaviyo_gdpr_embed_LIST_ID label,

.klaviyo_condensed_styling.klaviyo_gdpr_embed_LIST_ID label {

 color:#222;

}

.klaviyo_styling .klaviyo_field_group .klaviyo_form_actions {

 text-align:left;

 }

.klaviyo_styling.klaviyo_gdpr_embed_LIST_ID input[type=checkbox] + label,

.klaviyo_condensed_styling.klaviyo_gdpr_embed_LIST_ID input[type=checkbox] + label {

 display: inline;

 font-weight:normal;

 padding-left:5px;

}.klaviyo_styling.klaviyo_gdpr_embed_LIST_ID input[type=text],

.klaviyo_styling.klaviyo_gdpr_embed_LIST_ID input[type=email],

.klaviyo_condensed_styling.klaviyo_gdpr_embed_LIST_ID input[type=text],

.klaviyo_condensed_styling.klaviyo_gdpr_embed_LIST_ID input[type=email] {

 border-radius: 2px;

}.klaviyo_styling.klaviyo_gdpr_embed_LIST_ID .klaviyo_submit_button,

.klaviyo_condensed_styling.klaviyo_gdpr_embed_LIST_ID .klaviyo_submit_button {

 background-color:#0064cd;

 border-radius: 2px;

}.klaviyo_styling.klaviyo_gdpr_embed_LIST_ID .klaviyo_submit_button:hover,

.klaviyo_condensed_styling.klaviyo_gdpr_embed_LIST_ID .klaviyo_submit_button:hover {

 background-color:#0064cd;

}

</style>

<script type="text/javascript" src="//www.klaviyo.com/media/js/public/klaviyo_subscribe.js"></script>

<script type="text/javascript">

 KlaviyoSubscribe.attachToForms('#email_signup', {

 hide_form_on_success: true,

 extra_properties: {

 $source: '$embed',

 $method_type: "Klaviyo Form",

 $method_id: 'embed',

 $consent_version: 'Embed default text'

 }

 });

</script>
```

## How consent is stored in Klaviyo

To find the [consent status](https://klaviyo.zendesk.com/hc/en-us/articles/360037101072) of a specific contact, head to their individual profile in Klaviyo.

![Profile with email consent](https://klaviyo.zendesk.com/hc/article_attachments/28716302288027)

When subscribers submit their consent through a form, Klaviyo stores several key custom properties on their profile:

- ****Form ID****This is the unique form ID that allows you to identify the specific form someone used to opt-in. Every form created in Klaviyo has a unique ID, which can be found in the URL of the form as a six-digit alphanumeric code.
  ![Form ID in browser URL](https://klaviyo.zendesk.com/hc/article_attachments/28716329592987)
- ****Method****This identifies the method that a subscriber used to opt-in. If you are using a Klaviyo sign-up form as outlined above, this will read **Klaviyo Form**.
- ****Form Version****This identifies the iteration of the form that a particular subscriber saw. Klaviyo keeps a record of the exact text and language that was used for each version of a form you create, which you can request from support if necessary. For example, if you see "2" as the consent version, this means that the subscriber signed up to the second variation you made of the form.
- ****Timestamp****This is a timestamp recording precisely when they submitted the form and granted consent.

## How to handle requests for data or deletion

Under GDPR, you may be required to provide a contact with all of their user data if they request it. Additionally, if a contact requests that their data is deleted, you may be required to delete certain information and to keep a record of this deletion to prove that the request was met.

Check out our guide on [Handling GDPR Requests](https://help.klaviyo.com/hc/en-us/articles/360004217631-How-to-Handle-GDPR-Requests) for specific instructions.

## Build a segment of EU contacts

To isolate a group of contacts in your account that are in the EU, create a segment with the following conditions:

![Segment condition for profiles in the EU](https://klaviyo.zendesk.com/hc/article_attachments/32061224864539)

## Filter EU contacts out of flows

For any non-transactional flows, you will want to add a filter to only include those who are consented (to email, SMS, or both depending on what you plan to send) or are not in the EU and UK.

Some common flows that will require this filter are:

- Browse abandonment
- Winback
- Upsell
- Cross-sell
- Product review

For more information on the difference between transactional and non-transactional flows, check out [this guide](https://help.klaviyo.com/hc/en-us/articles/360003165732). The one exception to this list may be abandoned cart emails. Many organizations take the view that you can still send abandoned cart emails without explicit consent for marketing communications under the basis of legitimate interest. You may be able to consider an abandoned cart email as a communication relevant to the explicit intent to complete a transaction with your business. Other triggered emails, like browse abandonment and winbacks, on the other hand, may not be permissible unless customers have previously consented to receive marketing emails from you in a GDPR-compliant fashion.

That said, the applicability of legitimate interests or any other legal basis will depend on the particular circumstances; for example, the number and frequency of emails and the amount of time that has elapsed since the cart was abandoned. We strongly recommend that you consult with your legal team about your campaigns and flows to confirm they are compliant with applicable law.

## Suppressing EU contacts who do not provide consent

Anyone in your EU subscriber segment who did not opt into a re-permissioning campaign by May 25, 2018 should be suppressed in your account to prevent you from accidentally emailing them. To ensure that you've filtered out any subscribers who provided consent, add the following condition to the EU segment outlined above.

![](https://klaviyo.zendesk.com/hc/article_attachments/33882741047067)

[Suppress this segment](https://help.klaviyo.com/hc/en-us/articles/115005073867-Bulk-Delete-or-Suppress-Contacts-in-Klaviyo#bulk-suppress-contacts-in-klaviyo) to ensure that you don’t inadvertently email these contacts. If they later decide to opt back in, they can resubscribe.

## Best practices

Once you have a GDPR-compliant sign-up framework in place, use segmentation and flow filters to ensure that you only send to profiles who have consented to receive marketing emails. The condition below outlines the filter that you would add to ensure that the group you're targeting has consented to receive emails.

![Condition for profiles that have consented to email marketing](https://klaviyo.zendesk.com/hc/article_attachments/32061211318811)

In order to maintain your GDPR compliance, you’ll also want to adhere to the following best practices:

- Display links to your Privacy Policy, Terms of Service, and cookie policy in all of your emails.
- Use [double opt-in](https://help.klaviyo.com/hc/en-us/articles/115005251108-Overview-of-the-Double-Opt-In-Process).
- Understand what consent means:
  - ****Freely given****. In other words, you can’t mislead or force someone into letting you use their information. They must be given a legitimate choice — and you can’t withhold a service or transaction on the basis of consent if that consent is not integral to the service or transaction.
  - ****Specific****. Consent to process personal data must include details around both the purpose of the processing and the type of processing.
  - ****Informed****. Closely tied to the idea of specific consent, informed consent simply means that the individual data subject must be told how their data is going to be used, the specific purpose their data is being used for, and the type of data processing you are using.
  - ****Unambiguous****. To go one step further, consent under GDPR must be obtained through clear language and indicated through affirmative action on the part of the data subject.
  - ****Easy to withdraw****. Though not called out in the definition of consent upfront, [Article 7](https://gdpr-info.eu/art-7-gdpr/) of the GDPR goes on to specify that consent must be as easy to withdraw as it is to grant.

## Additional resources

- [Understanding frequently asked questions about GDPR](https://help.klaviyo.com/hc/en-us/articles/360003211651-Frequently-Asked-Questions-About-GDPR)
- [How to handle GDPR and CCPA requests](https://help.klaviyo.com/hc/en-us/articles/360004217631-How-to-Handle-GDPR-and-CCPA-Requests)