---
id: 4404189657755
title: "Understanding US guidelines for SMS cart abandonment flows"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/4404189657755-Understanding-US-guidelines-for-SMS-cart-abandonment-flows"
section: "North America: SMS compliance"
category: "SMS"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-21T13:54:58Z"
language: en
---

## You will learn

Learn about compliance best practice for SMS in shopping cart abandonment flows. Shopping cart abandonment flows include abandoned cart, abandoned checkout, and added to cart flows.

Cart abandonment flows are a great way for brands to obtain more subscribers and convert them into customers. However, certain carriers enforce a strict limit on how many SMS messages a brand can send in these flows. If you plan to use SMS for these purposes, there are a few things you may need to do to qualify.

This information is intended solely for educational and informational purposes and should ****not**** be construed as legal advice. The content provided is general in nature and may not reflect the most up-to-date information. Klaviyo strongly advises consulting with a qualified legal counsel to ensure your compliance with applicable laws and regulations in connection with your use of our services.

## Requirements for US SMS cart abandonment flows

The following are all required by the TCPA, CTIA, or carriers in the US:

- Have double opt-in turned on
- Use only 1 SMS per recipient in a cart abandonment flow
- Have the SMS send within 48 hours of the triggering event
- Have express consent for SMS and cart abandonment messages
- Add disclosures to your mobile terms of service and privacy policy

These requirements are for cart abandonment flows specifically, but following them is strongly recommended for other types of abandonment flows, such as browse abandonment.

****Consent/opt-in requirements****

There are 2 main requirements for consent in connection with cart abandonment messages:

- A recipient must explicitly agree to receive cart abandonment reminders
- The list they are sent to must have double opt-in enabled

For the first, as a part of the SMS opt-in process on your website, mention in the call-to-action that your SMS program includes abandonment reminders. Typically, this mention is part of the disclosure text written on a signup form.

In the US, wireless carriers require that all SMS subscribers must go through the [double opt-in process](https://help.klaviyo.com/hc/en-us/articles/115005251108) if you want to send them cart abandonment messages.

****Flow restrictions****

An SMS cart abandonment flow has 2 key restrictions:

- The flow is limited to 1 SMS message per recipient
- The message must be sent within 48 hours of the triggering event

Further, you cannot complete the transaction on behalf of the customer, collect payment information via text, or accept purchase via a keyword confirmation from the customer. The customer must complete the transaction themselves on your online store.

****Required disclosures****

If you plan to send cart abandonment reminders through your short code SMS program, it needs to be specified within your mobile program terms of service. The language below is an example of such a disclosure.

**“If you have opted in, the Service provides alerts, information, promotions, specials, and other marketing offers (e.g., cart reminders) from <Company Name>.”**

You must also address your cart abandonment program in your privacy policy. For instance, with abandoned carts, privacy policies must explicitly state how information is captured by the website to determine when a customer cart has been abandoned (website cookies, plugins, etc). The language below is an example.

**“The <website> uses cookies to help keep track of items you put into your shopping cart including when you have abandoned your cart and this information is used to determine when to send cart reminder messages via SMS.”**