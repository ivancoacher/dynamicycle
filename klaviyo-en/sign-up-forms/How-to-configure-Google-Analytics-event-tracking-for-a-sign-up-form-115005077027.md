---
id: "115005077027"
title: "How to configure Google Analytics event tracking for a sign-up form"
source_url: "https://help.klaviyo.com/hc/en-us/articles/115005077027-How-to-configure-Google-Analytics-event-tracking-for-a-sign-up-form"
section: "Build and use forms"
category: "Sign-up forms"
category_slug: "sign-up-forms"
klaviyo_updated: "2026-04-21T13:54:17Z"
language: "en"
---
## You will learn

Learn how to set up Google Analytics event tracking for your Klaviyo sign-up forms to gain insights about important user actions with your forms. You can measure form activity by marking the Klaviyo events (e.g., form\_open, form\_close, form\_submit) as conversions in Google Analytics. Set this up by following this 2 step process:

1. Add a code snippet to your website to send Klaviyo sign-up form data to Google Analytics.
2. Mark your events as conversions in Google Analytics.

Please note that Google Analytics event tracking can take 24-48 hours to update. This guide covers configuring tracking activity for Klaviyo sign-up forms in Google Analytics 4.

## Before you begin

Configuring event tracking for your sign-up forms in Google Analytics requires pasting a snippet of code on your site. If you are not comfortable with pasting code and do not have a developer to assist, Klaviyo has a vast network of partners in our [Partner Directory](https://connect.klaviyo.com/).

## Track sign-ups submitted using a Klaviyo form

You can track Klaviyo forms activity in Google Analytics by adding an event listener to the [klaviyoForms event](https://developers.klaviyo.com/en/v1-2/docs/track-klaviyo-form-activity-using-javascript) and then executing different GA tracking calls for each type of event. This code must be pasted in the main theme file of your site.

- If you're using Shopify, paste the snippet into your theme.liquid file on a new line above the closing </body> tag. Note that if you are using custom product pages, you may need to add this snippet to a different theme file, or to your individual custom product pages.
- If you’re using Shopify 2.0, add the code to a Custom Liquid block.
- If you're using BigCommerce, navigate to ****Storefront > Footer Scripts**** from your BigCommerce Admin panel and paste the snippet into the Footer code box on a new line.

Below is the generic code for tracking all klaviyoForms event types in Google Analytics. This code should also be used if you use [gtag.js](https://developers.google.com/tag-platform/gtagjs) to load Google Analytics:

```
<script>
  window.addEventListener("klaviyoForms", function(e) {
    if (e.detail.type == 'open' || e.detail.type == 'embedOpen') {
      gtag('event', 'form_open', {'form': 'Klaviyo form', 'form_id': e.detail.formId});
    }
    if (e.detail.type == 'submit') {
      gtag('event', 'form_submit', {'form': 'Klaviyo form', 'form_id': e.detail.formId});
    }
    if (e.detail.type == 'stepSubmit') {
      gtag('event', 'form_step_submit', {'form': 'Klaviyo form', 'step_name': e.detail.metaData.$step_name});
    }
    if (e.detail.type == 'redirectedToUrl') {
      gtag('event', 'form_url_redirect', {'form': 'Klaviyo form', 'form_id': e.detail.formId});
    }
    if (e.detail.type == 'close') {
      gtag('event', 'form_close', {'form': 'Klaviyo form', 'form_id': e.detail.formId});
    }
  });
</script>
```

If you want to track different form versions or variations, modify your code snippet to

```
gtag('event', 'form_open', {'form': 'Klaviyo form', 'form_id': e.detail.formId, 'form_version_id': e.detail.formVersionId })
```

with the relevant `form_id` instead of

```
gtag('event', 'form_open', {'form': 'Klaviyo form', 'form_id': e.detail.formId })
```

If you are tracking form submits for a multi-step form, note that only 1 `submit` event will fire each time the form is filled out. The submit event will fire in the following circumstances:

- For forms with email or SMS subscription actions, submitting an email or phone triggers a submit event.
- For forms containing both email and SMS fields across multiple steps, submitting whichever appears first in the form triggers a submit event.
- For forms without an email or SMS subscription action (e.g., a form containing only text fields), clicking a button with the **Action** set to ****Submit Form**** triggers a submit event.

The `stepSubmit` event will fire when each step is submitted.

## Test your tracking code

Once you’ve installed the tracking code on your site, you can test it to ensure data is being tracked. To test your code:

1. Navigate to your website and interact with your form (e.g., submit or close it).
2. Open Google Analytics and open ****Reports > Realtime.****
3. Under **Event count by Event name**, you should see a breakdown of the data your form has tracked. The metrics for each event should reflect an accurate count based on the action that you took (e.g., if you closed the form, you'll see this reflected in the **Event Count** for form\_close).

![GA222.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28716301162779)

If you don’t see your events, make sure Google Analytics is set up correctly, and that the code snippet you used is correct. Also note that your events will only be visible in Realtime for 30 minutes. See [[GA4] Realtime report](https://support.google.com/analytics/answer/9271392) for more details.

## Configure events to be marked as conversions

After you have set up tracking for new sign-up events in Google Analytics, you can configure the corresponding events to be marked as conversions to help you monitor how users interact with your forms.

From the **Existing events table** in Google Analytics (****Admin > Events****), toggle the switch to **Mark as conversion** for any events that you'd like to track. If an event is not in the existing list, you'll need to [create a new event and mark it as a conversion](https://support.google.com/analytics/answer/12966437?sjid=13312267381996017623-NA). If you only want your event to be marked as a conversion when a certain condition is met (e.g., a specific form ID), you'll need to [configure a conversion based on the values of your event's parameters](https://support.google.com/analytics/answer/11053133?hl=en#zippy=%2Cin-this-article).

When you mark an event as a conversion, Google Analytics will register a conversion every time it sees your event\_name (e.g., form\_open). Track the conversions form your Klaviyo form data on the **Conversions report**.

Note that conversions for your event may not appear for 24-48 hours after you begin tracking klaviyoForms events.

## Additional resources

- [How to add Klaviyo web tracking using Google Tag Manager](https://help.klaviyo.com/hc/en-us/articles/360015392131)
- [Understanding UTM tracking in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115005247808)
- [Track Klaviyo form activity using Javascript](https://developers.klaviyo.com/en/docs/track_klaviyo_form_activity_using_javascript)
- Course: [Capture new subscribers with strategic sign-up forms](https://academy.klaviyo.com/create-strategic-sign-up-forms)