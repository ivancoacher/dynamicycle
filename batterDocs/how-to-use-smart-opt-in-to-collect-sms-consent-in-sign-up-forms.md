<h1>How to use Smart Opt-in to collect SMS consent in sign-up forms</h1>

To use Smart Opt-in, you must have:

- A paid SMS plan.
- Set up SMS in your account.

Learn how to enable Smart Opt-in in a sign-up form to easily collect and verify SMS consent from site visitors. When a shopper inputs their phone number into a form with Smart Opt-in enabled, they’ll receive a one-time code that they can click to autofill on iOS and Android browsers to confirm their consent for SMS marketing.

SMS sign-up forms with Smart Opt-in reduce the friction of shoppers needing to take action in their messages app, and minimize distractions since shoppers can opt in without needing to leave your site. They can also help you avoid list bombing when using a branded sender ID.

## Before you begin

This feature is not currently supported when [lead capture with Shop](https://klaviyo.zendesk.com/hc/en-us/articles/17292871409947) is enabled, and cannot be used in any form that collects [transactional SMS consent](https://help.klaviyo.com/hc/en-us/articles/26024442679835).

Note that if you downgrade to a free SMS plan after creating 1 or more Smart Opt-in sign-up forms, these forms will no longer work. You will either need to republish the forms without the Smart Opt-in step, or resume your paid SMS plan so that they function properly.

## How Smart Opt-in works

The process for collecting SMS consent in a sign-up form through Smart Opt-in works as follows:

1. A site visitor inputs their phone number in a form with Smart Opt-in configured.
2. The site visitor receives a text at that phone number with a one-time code (e.g., 123456).

   The one-time code will not send from your brand’s regular sending number; it will send from a short code managed by Klaviyo, so this message will not be on the same thread as your regular, promotional messages.
3. The site visitor sees an additional form step asking for a one-time authentication code.
4. Based on their device type, the site visitor enters the code and submits the form to confirm their opt-in status.

- If the visitor is viewing the form on a mobile device, they can click to autofill the one-time code on any iOS or Android browser.
- If the visitor is viewing the form on desktop, they must manually copy the code from their SMS messages into the form.

Collecting SMS consent via Smart Opt-in is similar to the double opt-in process in that visitors take 2 steps to opt in: entering their phone number, and then inputting the one-time code that they receive. Double opt-in is strongly recommended when collecting SMS consent, and in the US it is required if you plan to add SMS to your abandoned cart flows.

To learn about how Smart Opt-in compares to other SMS consent collection methods (e.g., tap-to-text), check out our [SMS opt-in methods reference](https://help.klaviyo.com/hc/en-us/articles/27902671291419).

## Configure Smart Opt-in in a sign-up form

To begin, navigate to ****Sign-up forms**** in Klaviyo’s left-hand navigation. From here, you can either:

- Customize a pre-built template that has Smart Opt-in already configured
- Configure Smart Opt-in on one of your existing forms

To ensure that subscribers can receive the one-time code, only display your Smart Opt-in forms in countries where you have an active sending number. You can use the same form across all of your supported countries (e.g., target the form by location to display in the United States, United Kingdom, France, etc.), but avoid showing it in regions where you don't have a sending number and Klaviyo SMS is not available.

### Customize a template with Smart Opt-in pre-configured

To update a template where Smart Opt-in is already setup:

1. In the top right corner, select ****Create form****.
2. Open the ****All Categories**** dropdown, then check the box for ****Smart Opt-in**** to filter the form library.
   ![The form library category filter options showing Smart Opt-in selected to only show only Smart Opt-in pre-built form templates. ](https://klaviyo.zendesk.com/hc/article_attachments/29340509127579)
3. Choose a pre-built template from the filtered options. These options have Smart Opt-in already configured by default.
4. On the preview modal:

   - Name your form
   - Choose the list that new subscribers will submit to
   - Select whether to include a form teaser![](https://klaviyo.zendesk.com/hc/article_attachments/34223289440411)
5. Select ****Create form**** to enter the form editor.
6. Select ****Targeting and behavior****, then click ****Targeting****.
7. Under **Location**, click ****Show to visitors in certain locations****, then select the countries where you have an active sending number from the dropdown (e.g., United States, United Kingdom, etc.). Targeting your form to these countries ensures that only site visitors who can receive the one-time code will see it.
   ![SOIcallout.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28722599741467)
8. Customize the content, design, and behavior of your form to fit your brand and goals. See [getting started with sign-up forms](https://help.klaviyo.com/hc/en-us/articles/360026474752#h_01HAAJKYJ2G0D4XR17NQ0EN7RX) for more guidance on editing your form.

![](https://klaviyo.zendesk.com/hc/article_attachments/46173021391771)

Be sure to customize each step of your form, including the ****One-time code**** step and ****Success**** step.

All Smart Opt-in templates have an **SMS Opt-in step** followed by a **One-time code** step. All steps include a submit button, and the **One-time code** step additionally includes a **Resend Code** button. Klaviyo will pre-configure the buttons on each of the form’s steps with the appropriate action settings, so you do not need to adjust them manually. Note that some pre-built Smart Opt-in templates may also include an **Email Opt-in** step before or on the same step as the **SMS Opt-in**.

When you’re finished customizing your sign-up form, click ****Publish****. Then, see [the SMS messaging details for Smart Opt-in section](https://help.klaviyo.com/hc/en-us/articles/24743883751451#h_01HWPA08MD3Q0E18AN2RXGEGAN) for SMS billing information.

### Configure Smart Opt-in on an existing form

You can configure Smart Opt-in on an existing, email-only form, or alternatively, you can change an existing SMS opt-in form to use Smart Opt-in. The following sections will outline each option.

#### Add Smart Opt-in to an existing email-only form

If you have an existing form that collects email consent only, add an SMS step and configure Smart Opt-in:

1. Next to the form you’d like to add Smart Opt-in to, select the ****3 dots > Edit****.
2. Click ****(+) Step**** in the menu bar to add a step.
   ![The (+) Step button selected in the form editor for an example email-only form.](https://klaviyo.zendesk.com/hc/article_attachments/28722611697819)
3. Select ****SMS Opt-in > Next****.
   ![The Add Step modal showing the SMS Opt-in option selected.](https://klaviyo.zendesk.com/hc/article_attachments/28722599729435)
4. Choose the list that new SMS subscribers will join, then select ****Smart Opt-in****.
5. Click ****Add step****.
   ![The second Add step modal showing the Smart Opt-in option selected and an example SMS Subscribers list chosen from the list dropdown.](https://klaviyo.zendesk.com/hc/article_attachments/28722611702683)
6. Customize the design and content on the newly added ****SMS Opt-in**** step and the ****One-time code**** step to match the rest of the form.
7. Select ****Targeting and behavior****, then click ****Targeting****.
8. Under **Location**, click ****Show to visitors in certain locations****, then select the countries where you have an active sending number from the dropdown (e.g., United States, United Kingdom, etc.). Targeting your form to these countries ensures that only site visitors who can receive the one-time code will see it.
   ![The Location section on the Targeting tab showing an example form set to Only show in the United States and United Kingdom.](https://klaviyo.zendesk.com/hc/article_attachments/28722599741467)
9. Verify that you do not have any active alerts in the ****Form alerts**** tab in the lower left corner of the editor.
10. Click ****Publish changes****.
11. See [the SMS messaging details for Smart Opt-in section](https://help.klaviyo.com/hc/en-us/articles/24743883751451#h_01HWPA08MD3Q0E18AN2RXGEGAN) for more information.

#### Change an existing SMS form to use Smart Opt-in

If you have an existing SMS sign-up form, change the opt-in method to use Smart Opt-in:

1. Click on the phone number input block in the preview.
2. Under **SMS opt-in method** in the left-hand menu, select ****Enable****.
   ![The Phone number menu in the form editor showing the SMS Opt-in Method section highlighted.](https://klaviyo.zendesk.com/hc/article_attachments/28722599736219)
3. Click ****Smart Opt-in > Add step****.
   ![The Add Step modal showing the Smart Opt-in option selected.](https://klaviyo.zendesk.com/hc/article_attachments/28722599733403)
4. Customize the design and content of the ****One-time code**** step and ****Success**** steps to match the rest of the form.
   ![The One-time code step selected in the menu bar of the form editor.](https://klaviyo.zendesk.com/hc/article_attachments/28722599724699)
5. Select the ****Targeting and behaviors**** tab, then click ****Targeting****.
6. Under **Location**, click ****Show to visitors in certain locations****, then select the countries where you have an active sending number from the dropdown (e.g., United States, United Kingdom, etc.). Targeting your form to these countries ensures that only site visitors who can receive the one-time code will see it.
   ![The Location section on the Targeting tab showing an example form set to Only show in the United States and United Kingdom.](https://klaviyo.zendesk.com/hc/article_attachments/28722599741467)
7. Verify that you do not have any active alerts in the ****Form alerts**** tab.
8. Click ****Publish changes****.
9. See [SMS messaging details for Smart Opt-in section](https://help.klaviyo.com/hc/en-us/articles/24743883751451#h_01HWPA08MD3Q0E18AN2RXGEGAN) for more information on messaging with Smart Opt-in.

## SMS messaging details for Smart Opt-in

Once published, site visitors who submit their phone number on the **SMS Opt-in step** will receive an SMS message containing a one-time code. The message will read as follows:

“Your {SMS Organizational Prefix} verification code is: 123456”

Klaviyo will automatically translate this message to the appropriate language based on the recipient’s country code. This message will not count against your brand’s SMS credits, even if a shopper requests multiple authentication codes. Similarly, Klaviyo will not record a **Received SMS** event on the recipient’s profile for this message.

[SMS organizational prefixes](https://help.klaviyo.com/hc/en-us/articles/360035285472#01H8PSCKBZSJXZZHKGDV5C3TK4) must be 30 characters or less and not include any special characters. If you have not manually set up an organizational prefix, it defaults to the company name associated with your Klaviyo account. Due to compliance reasons, messages sent to Canadian recipients will not contain an organizational prefix.

The respective code will auto-detect on iOS and Android browsers, so site visitors can easily click to auto-fill the code in the form to verify their opt-in status without ever needing to leave your site. If a shopper is browsing on a desktop, they’ll need to manually copy the code from their mobile device.

Once a site visitor adds the code and submits the **One-time code** step, they will see the form’s **Success** step and their Klaviyo profile will reflect a **Subscribed** consent status for SMS marketing. Additionally, a **Subscribed to SMS Marketing** event will log on the subscriber's Klaviyo profile with the date and time of their opt in.

![An example Klaviyo profile showing a Subscribed to SMS Marketing event logged, as well as a Subscribed consent status next to SMS.](https://klaviyo.zendesk.com/hc/article_attachments/28722599739035)

If a site visitor inputs an incorrect code into the form, they’ll see an error alerting them of an invalid code, and the option to re-enter the code or request a new one.

See [getting started with form analytics](https://help.klaviyo.com/hc/en-us/articles/360015960712) for guidance on tracking performance metrics for your form, including submit rates per step so you can see where potential subscribers are abandoning the opt-in experience within your form.

## Troubleshooting Smart Opt-in

Delivery of messages containing the one-time code is dependent upon the end carrier, so delays and message failures can still occur in the case of an outage.

As a best practice for protecting against these instances, consider adding an [SMS subscribe link](https://help.klaviyo.com/hc/en-us/articles/14104388043931) in a smaller font at the bottom of your **One-time code** step in case someone has difficulty with the one-time code. Alternatively, if you have [two-way messaging capabilities](https://help.klaviyo.com/hc/en-us/articles/360059002271), you can also add additional text to your form with instructions for sending your subscribe keyword to your sending number (e.g., “Having trouble with the code? Instead, text JOIN to ### to subscribe.”).

If you include a backup opt-in method on the One-time code step, ensure that the required disclosures are included for that method (e.g., [subscribe link](https://help.klaviyo.com/hc/en-us/articles/14104388043931), [tap-to-text](https://help.klaviyo.com/hc/en-us/articles/4412878737051), etc.).

Note that Klaviyo's Smart Opt-In is also not support on age-gated forms as a visitor must be double opted in BEFORE being messaged by your brand.
