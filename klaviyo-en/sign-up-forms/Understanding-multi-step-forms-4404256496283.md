---
id: "4404256496283"
title: "Understanding multi-step forms"
source_url: "https://help.klaviyo.com/hc/en-us/articles/4404256496283-Understanding-multi-step-forms"
section: "Build and use forms"
category: "Sign-up forms"
category_slug: "sign-up-forms"
klaviyo_updated: "2026-04-21T13:54:58Z"
language: "en"
---
## You will learn

Multi-step forms make it easy to learn about your subscribers and collect consent for multiple marketing channels without intimidating visitors with a large or clunky form. Use this feature to present just a few questions at a time, and capture as much information as your subscribers are willing to provide.

In this guide, you’ll learn about how multi-step forms work and some best practices for using them. If you’d like to learn how to create a multi-step form, head to our guide [how to create a multi-step form](https://help.klaviyo.com/hc/en-us/articles/4404213604251).

## Use cases for multi-step forms

### Grow your SMS list without slowing email growth

In general, sign-up forms that collect email consent have higher conversion rates than forms that collect phone numbers. When collecting phone number and email consent in a single form, you can inadvertently slow down the growth of your email list if you ask for a phone number at the same time.

To avoid this, use a multi-step form. Build a form that collects email addresses in the first step, then phone numbers in the second step. If a visitor only completes step 1, you’ll be able to reach them via email, and can encourage them to subscribe to SMS marketing in the future. Multi-step forms that collect email and SMS consent across multiple, different steps are best practice for list growth and maintaining compliance.

In order to build a multi-step form you can either:

- Choose a multi-step form template from the form library.
- Add additional steps to a sign-up form from within the form editor.

If you choose a multi-step form template from the form library, you can choose 2 different lists for your new email subscribers and SMS subscribers to submit to when they fill out the form. Klaviyo recommends using separate lists to help you honor your shoppers’ preferred channels, and keep track of email and SMS list growth.

![](https://klaviyo.zendesk.com/hc/article_attachments/34369916123291)

Note that if you do not already have an SMS subscribers list already, Klaviyo will create one for you automatically when you choose this option.

Alternatively, if you choose to add steps to a form from within the sign-up form editor, you can choose another list for SMS subscribers when you add an SMS step to your form.

![](https://fast.wistia.com/embed/medias/wm9sj34fju/swatch)

### Collect profile data

Detailed profile data, like a subscriber’s name, birthday, or interests, can help you target your marketing and provide a highly personalized experience to your subscribers. By adding a **Profile Information** step to a multi-step form, you can ask new subscribers to share this information without overwhelming them with a form that has too many questions on the first step.

To collect additional profile data in a multi-step form, add some basic fields to your form’s first page (e.g., first name, last name, and email address). Then add a second page with [other input fields](https://help.klaviyo.com/hc/en-us/articles/4413550187035#h_01HA2GG23YZM7MYV097K0DGKF0), like birthday or interests.

The button on the **Profile Information** step must have its **Action** set to ****Submit form**** in order for the properties to record on a subscriber's profile page. If the button's **Action** is set to "Close form" then the properties collected on this step will not be saved. .

Once subscribers have filled out the form, you can create segments to better target them, or use flows to send personalized messages (e.g., a [birthday flow](https://help.klaviyo.com/hc/en-us/articles/360054242492-Building-a-Birthday-Flow)).

![](https://fast.wistia.com/embed/medias/c0iuireny7/swatch)

### Add pre-engagement steps

If you’d prefer to get buy-in from your visitors before asking them for any information, create a sign-up form with a pre-engagement step. For example, create a form with its first step showing the message “Want 15% off your next order?” and a “Yes” button (and, optionally, a “No, thanks” button), but no input fields. Then, in the second step of the form, ask for an email address or phone number where the customer can receive the offer.

![](https://fast.wistia.com/embed/medias/d4d3bw7sos/swatch)

## How multi-step forms collect information

Klaviyo stores information from each step of your form as the visitor proceeds through it. This means that if someone only fills out 1 page, any information they submit from that page will be added to their Klaviyo profile.

If your form’s first page collects profile properties, but doesn’t collect an email or phone number, Klaviyo will hold the information until the visitor adds either an email or phone number. If an email or phone number is never provided, the information will not be added to a Klaviyo profile. Klaviyo does not track anonymous visitors.

## Targeting multi-step forms

A multi-step form offers the same targeting options as a single-page sign-up form. This means you can set a multi-step form to appear to users in certain locations, or who meet certain criteria.

Targeting based on lists and segments relies on Klaviyo’s cookies. To learn more, head to our [guide on cookies in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/360034666712-About-Cookies-in-Klaviyo).

If your multi-step form collects both email and SMS consent, consider setting the form to not appear for subscribers who have already signed up for either channel. To do so, click ****Targeting & Behaviors****. In the section labeled **Targeting**, select **visitors in a list or segment**, then choose **Show to specific profiles in a list or segment**. Choose to exclude your main email and SMS lists.

![The Targeting by visitors setting for an example form set to Show to specific profiles in a list or segment and exclude those already in a the Main list and SMS list.](https://klaviyo.zendesk.com/hc/article_attachments/28723544355867)

You can also create separate sign-up forms to target profiles that have subscribed to just 1 channel (email or SMS). For example, create a form to collect SMS consent, and set it to **Target by visitors** and then **Show to email subscribers only****.**

## Limitations of multi-step forms

Multi-step forms offer a linear path through a series of pages. It is not possible to skip a single page of a form for certain site visitors. However, you can clone your multi-step form, then target the 2 copies of the form to different audiences and customize them as desired.

The maximum number of pages in a form is 4, plus an optional success message.

Klaviyo’s forms cannot track information from anonymous visitors, so if someone fills out a form step but never provides a unique identifier (either an email or phone number), their information will not be available in your account.