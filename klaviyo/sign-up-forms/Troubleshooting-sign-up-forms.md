---
id: 115005249348
title: "Troubleshooting sign-up forms"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005249348-Troubleshooting-sign-up-forms"
section: "Troubleshooting sign-up forms"
category: "Sign-up forms"
category_slug: "sign-up-forms"
klaviyo_updated: "2026-04-21T13:54:23Z"
language: en
---

## You will learn

Learn troubleshooting tips for when a sign-up form in your Klaviyo account is not working as expected by reviewing common issues and solutions to these issues.

Check out our guide on [managing your sign-up forms](https://help.klaviyo.com/hc/en-us/articles/360002049952) to learn more about editing how your forms function.

## How to test your forms

After you publish a sign-up form, it's important to test that it looks and behaves the way you want it to. Testing your form can also help you narrow down the issue so you know how to troubleshoot.

When testing a sign-up form, use a unique email address (i.e., one that you haven’t used for this form before) for best results.

## Troubleshooting Klaviyo sign-up forms

Please note that sign-up forms will not render for browsers using Internet Explorer. [Custom-built sign-up forms](https://help.klaviyo.com/hc/en-us/articles/115005080327) will continue to render for those using any type of web browser.

If you have a Klaviyo's sign-up that's not functioning correctly, you may need to follow different troubleshooting steps. Below are common issues that can arise when you publish a sign-up form from Klaviyo's form editor. Click the dropdown for solutions for each issue.

****Sign-up form is not appearing on site****

If your form is published in Klaviyo but not displaying:

- Verify that your form is live. In the Sign-up forms tab, you should see "**Live**" with a green arrow under the **Status** column for your form.
  - As mentioned above, Klaviyo sign-up forms won't appear on Internet Explorer.
- Verify that you have followed all directions to [install and enable the Klaviyo.js onsite code snippet](https://klaviyo.zendesk.com/hc/en-us/articles/360002035871) (also known "Active on Site" tracking).
- If you're using an embedded form, verify that you have the correct [embed code](https://help.klaviyo.com/hc/en-us/articles/360006897412) installed within your site's code exactly as it appears in the installation model.
- Review the ****Targeting & Behaviors**** section in the sign-up form editor:
  - Under **Targeting,** ensure that the form is [configured to display on the URL](https://help.klaviyo.com/hc/en-us/articles/4413544555547) that you are viewing, or that you're using a unique email address (as described in the testing tip above).
  - Under **Display Timing,** ensure the display timing settings are not too restrictive. If the form is set to **Show based on rules**, then all criteria must be met in order for the form to appear. For example, if "Show when the visitor is exiting the page" and "Show after scrolling 60% of the page" are both selected, a visitor must scroll through 60% of the page and show exit intent in order for the form to appear.
- Re-run the test in incognito/private browsing mode in a new window. You may have already closed the popup, which is why it isn't displaying again. We cookie browsers for 1 year, so once someone closes a popup, they won’t see the same popup again for another year (unless they clear their cookies).
- If you are using an embedded form, confirm the form’s embed code has been added exactly as it appears in the installation modal, and that it is [pasted correctly within your site’s code](https://help.klaviyo.com/hc/en-us/articles/360006897412-Where-to-Paste-a-Form-s-Embed-Code).
- Confirm that only 1 Klaviyo account is integrated with your site. If you have multiple Klaviyo accounts for 1 store, uncheck the option to **Automatically add Klaviyo onsite javascript** in all but 1 account. If you’ve manually installed Klaviyo’s .js, make sure you’ve only installed the snippet from 1 account.
- For Shopify stores: Based on your Customer Privacy settings in Shopify, Klaviyo may not track onsite events (and thus, not apply certain types of form targeting) for visitors to your Shopify store in the EU, EEA, UK and Switzerland, unless they have provided consent.

  Overall, if a visitor hasn’t consented, and would otherwise have been included per the targeting requirements, they will not see the form because they will not be identified. Targeting for these visitors will apply as follows:

  - If you select “Don’t show to existing Klaviyo profiles,” the visitor will still see the form because they won’t be identified as an existing profile.
  - If you select “Target visitors in a list or segment,” the visitor will not see the form (even if they are otherwise in the list or segment) because they will not be identified. If you select “Show to all visitors,” the visitor will see it.
  - If you select "Show to existing profile," "Show to email subscribers only," or "Show to SMS subscribers only," the visitor will not see the form because they will only be identified as an existing profile, email, or SMS subscriber.
  - Certain custom triggers based on cookie information and user properties will not trigger due to a lack of identification.
  - Targeting by location is not affected.
  - Targeting to show on device type (desktop, mobile) is not affected.

****Sign-up form won't successfully submit****

If your form is not submitting when you click the **Submit** button:

- Verify that the list the form is connected to has not been deleted.
- Verify that the button is a [Submit button](https://help.klaviyo.com/hc/en-us/articles/4413550187035-Understanding-form-blocks-and-fields#button-block3), not a Close button. Click on the button in the form editor preview to see this.
- Check your inbox for a confirmation email. If your list is set to [double opt-in](https://help.klaviyo.com/hc/en-us/articles/115005251108-Overview-of-the-Double-Opt-In-Process), you will not be added to it until you confirm your subscription.

****Sign-up form looks different on my website****

Klaviyo sign-up forms should render on your website as they have been designed in the Klaviyo form editor. If it looks different, then your site’s CSS is overriding the styling of the form. To troubleshoot this:

- Look for !important tags in your CSS and remove these if possible.
- Your developer can also use your browser’s developer tools to inspect the site’s code and identify the problem CSS. If you are still having trouble, [find help here](https://help.klaviyo.com/hc/en-us/articles/115001002272-How-to-Contact-Support).

****Sign-up form is not adding people to list****

Keep in mind that all Klaviyo forms that collect email, SMS consent, or have a coupon featured have bot protections in place by default. If Klaviyo detects suspicious behavior or previous bot activity from a site visitor's IP address, they are prompted to solve a CAPTCHA before submitting the form.

If people are filling out your form, but you do not see them being added to the list your form is connected to:

- Click on the button in the form editor preview and make sure that you’ve selected a List to Submit.
- Check your list’s [opt-in settings](https://help.klaviyo.com/hc/en-us/articles/115005251108-Guide-to-The-Double-Opt-In-Process). If the list is set to double opt-in (recommended), then the missing subscribers likely did not complete the confirmation step.

If the number of form submissions doesn’t match the number of people in your list:

- Subscribers might not have completed the confirmation step (if your list is set to double opt-in).
- It could also reflect duplicate entries. If a subscriber fills out a form repeatedly, each entry will count as one “submission” in your form analytics, but they will only appear in your list 1 time.
- It’s also possible that some submissions came from bots or list bombers. Klaviyo has list bombing protections in place to protect you from these cyber attacks.

****Unable to detect installation****

You may receive the error message "**Unable to detect that sign-up forms are successfully installed on your site. Please view the installation documentation.**" but have correctly added the installation snippet to your website (or are using a prebuilt integration that does this automatically). This may appear if you are using a tag management platform (eg. Google Tag Manager) or some other method to deliver the snippet to your website when the page loads.

This message will not prevent you from publishing a form so if the snippet is correctly installed on the website you should be fine to ignore it. If you are still having trouble with this, please [contact us](https://klaviyo.zendesk.com/hc/en-us/articles/115001002272).

****Screen readers not detecting sign-up forms (JAWS)****

Please note that JAWS, a computer screen reader program for Microsoft Windows, may not be detecting sign-up forms on your website that were created in Klaviyo. To ensure that site visitors using JAWS can still interact with sign-up forms on your website, we suggest adding an extra snippet of code to your site that makes it more accessible to JAWS.

Copy the following code snippet and paste it into your site’s main theme file so that JAWS will detect and read your Klaviyo sign-up forms:

```

```

## Additional resources

- [How to manage sign-up forms](https://klaviyo.zendesk.com/hc/en-us/articles/360002049952)
- [Getting started with sign-up forms](https://help.klaviyo.com/hc/en-us/articles/360026474752)
- [Understanding sign-up form targeting and behavior](https://klaviyo.zendesk.com/hc/en-us/articles/4413544555547)
- Course: [Klaviyo practitioner certificate](https://academy.klaviyo.com/en-us/certificates/klaviyo-practitioner-certificate)