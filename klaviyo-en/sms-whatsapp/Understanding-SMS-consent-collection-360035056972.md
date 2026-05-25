---
id: "360035056972"
title: "Understanding SMS consent collection"
source_url: "https://help.klaviyo.com/hc/en-us/articles/360035056972-Understanding-SMS-consent-collection"
section: "About collecting SMS consent"
category: "SMS"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-21T13:54:45Z"
language: "en"
---
## You will learn

Learn about SMS consent, including what counts as SMS consent, how you can collect it, and how resubscribes work. SMS consent refers to whether someone is opted in (i.e., if they have agreed to receive marketing text messages from your brand).

For information on how to tell if a profile is consented to SMS, see this article on [how Klaviyo stores consent](https://help.klaviyo.com/hc/en-us/articles/360037101072).

## Before you begin

In Klaviyo, you must have 2 things before you can collect SMS consent:

- [SMS turned on](https://help.klaviyo.com/hc/en-us/articles/4404274419355).
- An active [sending number](https://help.klaviyo.com/hc/en-us/articles/6637671573403) in the country where you want to collect SMS consent. The number may also need to be verified or registered.

If you haven't enabled SMS, or don't have a sending number for that country, you cannot collect SMS consent.

You can only gather subscribers in [countries where Klaviyo SMS is available](https://help.klaviyo.com/hc/en-us/articles/4402914866843).

## What counts as SMS consent

SMS is more regulated than most other marketing channels. Due to this, there are stricter requirements on what counts as proper SMS consent. Below, we break down what you need to do for SMS.

### Individuals must explicitly agree to receive SMS messages

Someone must agree to receive SMS messages from your brand, regardless of whether you're sending marketing or transactional messages. Typically, someone subscribes by checking a box at checkout or signing up through a form.

SMS consent also must be collected separately from any other marketing channel. For instance, while you can collect both email and SMS consent in the same form, you must make it clear that SMS is optional (usually via a separate checkbox or button).

A single consent cannot be provided to multiple brands or organizations. Customers must provide consent to receive messages from your company explicitly. Lead generation, affiliate related, or purchased lists are not valid SMS consent.

### You cannot force SMS consent

It’s illegal to force someone to sign up for SMS in order to make a purchase.

Additionally, providing consent for SMS cannot **appear** as if it’s required. Even if giving SMS consent is optional for your customers, you may face fines or compliance issues if SMS consent **seems** required. For instance, collecting both SMS and email consent on the same step of a sign-up form is not recommended, as customers may think they have to sign up for SMS if they want to sign up for email.

### Use disclosure language wherever you collect SMS consent

SMS subscribers must understand what they’re agreeing to **before** they sign up. To make this clear, include [disclosure language](https://klaviyo.zendesk.com/hc/en-us/articles/4412878737051) wherever you collect SMS consent, whether that is on a checkout page, form, banner in an email, social media post, or a third-party quiz or form (when using APIs to send consent).

This goes for all opt-in methods, from sign-up forms to subscribe keywords. Any potential subscriber should understand what they're signing up before they click submit or text in a keyword.

![Tap-to-text form highlighting the disclosure language](https://klaviyo.zendesk.com/hc/article_attachments/28720771282459)

****Where should the disclosure language go in a form?****

You should put the disclosure language above the SMS consent checkbox or button. That way, people see the disclosure language before they opt in.

### Use double opt-in if using cart abandonment messages (US)

While double opt-in is always recommended, it's also a carrier requirement in the US for any shopping cart abandonment flow (e.g., abandoned cart, added to cart, etc.).

With double opt-in, someone must take 2 actions before they're added as a subscriber in your account, such as entering their phone number and then confirming via text or clicking a button and then texting a keyword.

### FAQs

****Does having someone’s phone number count as consent for SMS?****

No. If someone gave you their phone number, that does not mean they gave you permission to send them SMS. While you do need a phone number to text someone, they also must explicitly say they want to receive marketing text messages.

****Does having consent for email count as consent for SMS?****

No. Having consent for email does not mean you have consent for SMS. Individuals must opt in to SMS marketing specifically; opting in to any other marketing channel (including email) does not count as consent for SMS.

****Should I use the same opt-in checkbox or button for both email and SMS?****

No. You risk falling out of compliance if you, for example, have a single checkbox to gather consent for both email and SMS. As a best practice, you should always use a separate checkbox or button for SMS consent.

****Can I use a general “agree to marketing” checkbox or button for SMS?****

No. It’s best to have a checkbox or button specifically for SMS. A general “agree to marketing” option is not considered sufficient for SMS in most countries.

****Should I use a single-page or multi-step form when collecting both email and SMS consent?****

Multi-step forms that collect email consent on one step, followed by phone numbers on another step, are the best option for collecting both email and SMS consent because they allow you to collect consent separately for each channel.

Single-step forms may be used, but only with double opt-in and when SMS consent is clearly optional. In addition to simply not requiring SMS consent, you should also have a label saying it's optional (e.g., "Phone number to receive SMS marketing (optional)").

## How to collect consent

There are several different ways you can collect SMS consent.

A few of these options should be done when you first start with SMS, while others can be left for later or only in certain scenarios. Because of this, we’ll break them down into 3 categories:

1. Basic (what everyone should do as soon as they start with SMS)
2. Intermediate (what you can leave for later)
3. Advanced (what only select users should do)

We'll briefly cover the different methods for collecting SMS consent in this article and link to other, more detailed articles for step-by-step instructions for when you're ready to build your consent channels!

### Basic methods

These are actions everyone should take when they first set up SMS. There 2 basic forms of collecting SMS consent:

1. Create sign-up forms that target new subscribers and your current email subscribers (estimated time: 10–15 minutes).
   - Generally, the most efficient type of form is [Smart Opt-in](https://help.klaviyo.com/hc/en-us/articles/24743883751451); however, this isn't available for forms that collect SMS transactional consent.
2. Collect SMS consent at checkout for your ecommerce store: (estimated time: 10 minutes).
   - [Shopify](https://help.klaviyo.com/hc/en-us/articles/360056824732)
   - [WooCommerce](https://help.klaviyo.com/hc/en-us/articles/360057745791)
   - [BigCommerce](https://help.klaviyo.com/hc/en-us/articles/360058194032)
   - [Magento 2](https://help.klaviyo.com/hc/en-us/articles/360058698511)
   - [PrestaShop](https://help.klaviyo.com/hc/en-us/articles/26534999577243)

![Example of a popup form for SMS](https://klaviyo.zendesk.com/hc/article_attachments/28720771280923)

****Why use sign-up forms?****

[Creating forms that collect SMS consent](https://help.klaviyo.com/hc/en-us/articles/27902671291419#h_01J472TF8016NMR0QED2C51BZ9) makes it easy for anyone visiting your website to sign up. Popups are one of the most common ways of gathering subscribers, and you can use them to target those who are brand new or already email subscribers. You can also create a form with [Smart Opt-in](https://klaviyo.zendesk.com/hc/en-us/articles/24743883751451) to easily collect SMS consent on both desktop and mobile devices.

We strongly recommend using a multi-step form if you’re collecting email consent at the same time as SMS consent.

****Why collect SMS consent at checkout?****

One of the quickest and easiest ways to grow your SMS list is by collecting consent at checkout. Consent at checkout offers you a non-intrusive, streamlined, and easy way for customers to sign up. With Klaviyo’s integrations, you can leverage this approach and reach a wider audience with your SMS marketing.

### Intermediate methods

These consent methods don’t need to be done as soon as you set up SMS. Instead, wait until you have finished setting up the basic consent collection steps, key SMS flows, such as your SMS [welcome](https://help.klaviyo.com/hc/en-us/articles/360036122291), [abandoned cart,](https://help.klaviyo.com/hc/en-us/articles/9352115400219) and post-purchase flows; and the rest of the steps recommended in our [Getting started with SMS course](https://academy.klaviyo.com/en-us/collections/getting-started-with-sms).

1. [Use emails to collect SMS consent](https://help.klaviyo.com/hc/en-us/articles/8185730542235) (estimated time: 10 minutes).
2. [Create a subscribe link for sharing in ads or on social media](https://help.klaviyo.com/hc/en-us/articles/14104388043931) (estimated time: 5–10 minutes).
   - [Collect SMS consent via Instagram stickers](https://help.klaviyo.com/hc/en-us/articles/360059544911) (estimated time: 5 minutes).
     Note that these steps are only for businesses who are already using Instagram.

****How can you use email to collect SMS consent?****

If you have a current list of email-only subscribers, you can ask this group to sign up for SMS as well. In particular, your highly engaged subscribers and your VIPs are great groups to target. It's also useful to advertise your SMS program (and how to sign up) in post-purchase flows. Another strategy is using a plain-text email in your winback flow to ask people if they'd rather hear from you via SMS.

There are 2 approaches to using email to gather SMS subscribers.

1. Link to an embedded form within the email.
2. Create a click-to-text banner to use in the email.
   Note that these banners would only work if the recipient opens the email on a mobile device and is not using Gmail or Outlook.

Both approaches are discussed in our article on [how to use an email to collect SMS consent](https://help.klaviyo.com/hc/en-us/articles/8185730542235).

****How can you use a subscribe link to gather subscribers?****

You can [create a subscribe link](https://klaviyo.zendesk.com/hc/en-us/articles/14104388043931) to grow your SMS list via ads, social media posts, and more. The subscribe link provide an easy, tap-to-text experience for those on mobile devices, and a subscribe page for those on desktop.

You can then post this link as part of an Instagram sticker. Thus, you can more easily gather consent from anyone who sees it.

![Example of an Instagram sticker with a link to collect SMS consent](https://klaviyo.zendesk.com/hc/article_attachments/28720759412123)

### Advanced methods

Advanced consent collection methods require a developer or someone experienced with making API calls. By making API calls, you can transfer SMS consent into Klaviyo from a third-party sign-up form or information from a quiz.

For details, see our Developer Portal [article on collecting email and SMS consent via API](https://developers.klaviyo.com/en/docs/collect_email_and_sms_consent_via_api#relevant-endpoints).

With some third parties (including [Privy](https://help.privy.com/hc/en-us/articles/360038080413#Synctootherproviders) and [Justuno](https://support.justuno.com/en/collect-more-information-with-klaviyo-sms-integration)), you don’t need to set up the API call yourself, as they will sync SMS consent to Klaviyo via an integration.

Note that you still need proper disclosure language wherever you collect consent, including if you’re using the API.

## Resubscribing to SMS

Note that for the UNSTOP and START [keywords](https://klaviyo.zendesk.com/hc/en-us/articles/360050384091), you must have an "SMS Subscribers" list, titled and capitalized exactly as shown.

Depending on how someone opted out, they may need to resubscribe in a certain way. If you have a toll-free number and someone previously texted STOP, the only way for them to be resubscribed is for them to text the words START or UNSTOP. This is required by wireless carriers in order for them to deliver messages. If they use some other method to resubscribe, the profile will show the individual as opted in, but wireless carriers will not deliver any messages to that recipient until they text the word START or UNSTOP.

If your customer did not opt out via the STOP keyword, and instead used an unsubscribe link, they can resubscribe using forms, START or UNSTOP, or via checkout. Similarly, if you have a short code, your customers can resubscribe by any method.

## Additional resources

- Want more information on SMS? Check out:
  - [Basics of SMS compliance](https://help.klaviyo.com/hc/en-us/articles/7956171032091)
  - [Create popups to collect SMS consent](https://help.klaviyo.com/hc/en-us/articles/9351341171995)
- [Understanding consent in profiles](https://help.klaviyo.com/hc/en-us/articles/360037101072)
- See tips on [mobile form design](https://help.klaviyo.com/hc/en-us/articles/15763867466395)