---
id: 45373923808155
title: "Getting started with Landing Pages"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/45373923808155-Getting-started-with-Landing-Pages"
section: "Getting started with sign-up forms"
category: "Sign-up forms"
category_slug: "sign-up-forms"
klaviyo_updated: "2026-04-21T13:55:02Z"
language: en
---

## ****You will learn****

Learn how to create and customize landing pages in Klaviyo so you can share a dedicated, hosted page in your campaigns, collect email and phone number subscribers, and measure performance.

You will:

- Confirm that landing pages are available in your account
- Set a goal for your landing page
- Create a landing page from scratch
- Design the page and form
- Publish your landing page and share its URL
- View basic performance (views, submits, submit rate)

## ****Before you begin****

Before you create a landing page:

- Confirm you have at least one ****email or SMS list**** for new subscribers.
- (Optional) Set up a ****custom hosted pages domain**** if you want landing pages on your own domain (for example, pages.yourbrand.com) rather than a Klaviyo domain.

## ****Best practices for landing pages****

If you are not sure where to start, use landing pages for:

- ****Campaign‐specific list growth**** – send ad or social traffic to a landing page that collects email and SMS.
- ****Launches and promotions**** – create a page that explains the offer and includes a form and optional coupon.
- ****Waitlists**** – collect email plus one or two key preferences for upcoming products.

  ****Set a goal for your landing page****

  Before building, decide what you want this landing page to achieve. For example:
- Grow your email and SMS/WhatsApp lists from paid traffic
- Convert social followers into subscribers
- Collect interest for a product waitlist
- Capture answers to a short questionnaire alongside an opt‐in

Once you choose a goal, you are ready to create the page.

## ****Create a basic landing page****

To create a new landing page:

1. In Klaviyo, go to ****Website****.
2. Select ****Landing pages****.
3. Click ****Create landing page****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/45373914244763)

   In the details modal:
4. Enter a ****name**** for your landing page (internal only).
5. Enter a ****title**** (shown in the browser tab and used for search).
6. (Optional) Choose the ****email list**** and ****SMS list**** that new subscribers should join when they submit the form.

![](https://klaviyo.zendesk.com/hc/article_attachments/45373923794715)

Click ****Create landing page**** to open the landing page editor.

## ****Design your landing page****

You design both the ****page**** and the ****embedded form**** in a tailored version of the form editor.

If you plan to ask for multiple pieces of information (for example, email, phone, and preferences), create a ****multi‐step form**** by adding an extra step. Multi‐step forms prevent visitors from seeing too many fields at once.

On landing pages:

- The form is always ****embedded**** in the page.
- Pop‐ups, teasers, timing rules, frequency rules, and on‐site behavioral targeting are not used. People reach the page directly via its URL.

## ****Share your landing page****

When your page and form are ready:

1. Click ****Publish****.
2. Copy the ****landing page URL**** from the publish screen or from the landing pages list view.

![](https://klaviyo.zendesk.com/hc/article_attachments/45373914252443)

### URL format

By default, your landing page uses a Klaviyo‐managed domain such as:

- company\_name.myklpages.com/l/random\_id

  If you have a custom hosted pages domain, that domain will be used instead.

  Share the landing page URL in:
- Email, SMS and WhatsApp campaigns
- Paid ads
- Social posts
- QR codes or other off‐site placements

### UTM Parameters

When someone visits your landing page with UTM parameters in the URL (for example, ?utm\_source=facebook&utm\_campaign=spring\_launch), Klaviyo:

- Captures those UTM values for landing page analytics
- By default, ****forwards the same UTM parameters to any “Go to URL” buttons****

This means that when a visitor clicks a button on your landing page (for example, a “Shop now” button on the success step), the destination URL also includes the original UTM parameters so your third‐party analytics tools can attribute the visit correctly.

If you do ****not**** want UTMs automatically forwarded to your site, turn off the UTM forwarding setting in your landing page settings. When this setting is off, Klaviyo will not append UTM parameters to your button URLs unless you add them yourself.

![](https://klaviyo.zendesk.com/hc/article_attachments/45753029290011)

## View performance

In the landing pages list view, you see:

- ****Hits**** – number of page views
- ****Submits**** – number of form submissions
- ****Submit rate**** – submits divided by hits

  From the Actions menu, you can:
- Edit the landing page
- View its analytics
- Clone it
- Rename it
- Copy the link
- Delete it

  The analytics view shows:
- A ****traffic source table****, using UTM parameters on the URL
- ****Multi‐step form analytics****, similar to sign‐up form analytics

## Troubleshooting

****Unpublishing a Landing Page****

If you unpublish a landing page and do not have a redirect URL set up, visitors to your URL will get a 404 Not Found page. To set a redirect URL, go to the landing page settings.

![](https://klaviyo.zendesk.com/hc/article_attachments/45753023902619)

## ****Next steps****

After your landing page is live, you can:

- Test different offers, copy, or layouts by cloning a landing page and comparing performance over time.
- Use the landing page URL in ****campaigns, flows, and ads**** to drive traffic.
- Build segments or flows that target subscribers who joined from that landing page. Use the ****Subscribed to List**** or ****Form Submitted by Profile**** event and filter by the ****source**** value associated with that landing page.

![](https://klaviyo.zendesk.com/hc/article_attachments/45753023903899)