---
id: 17976334449947
title: "Understand role-based email addresses and their impact on deliverability"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/17976334449947-Understand-role-based-email-addresses-and-their-impact-on-deliverability"
section: "Getting started with email deliverability"
category: "Deliverability & compliance"
category_slug: "deliverability-compliance"
klaviyo_updated: "2026-04-21T13:54:31Z"
language: en
---

## You will learn

Learn about role-based email addresses, and how they can impact your deliverability.

## What are role-based addresses?

Role-based email addresses are shared email addresses, often used by groups within an organization rather than an individual. For example, a business’s support team may use an email address like [support@business.com](mailto:support@business.com) for customer communications.

## How do role-based email addresses impact my deliverability?

Role-based email addresses typically don’t opt-in to receive emails and generally have high spam complaint rates. They are more likely to bounce, and negatively impact your sender reputation and deliverability. Klaviyo automatically blocks certain role-based email addresses from receiving marketing emails to protect your deliverability.

Note that a if role-based email address is sent an email through a Klaviyo flow or campaign, they will be skipped with the reason **Invalid Email.**

## List of blocked role-based addresses

The list of role-based email addresses Klaviyo automatically blocks are:

- abuse@
- compliance@
- devnull@
- dns@
- domains@
- ftp@
- inoc@
- ispfeedback@
- ispsupport@
- list-request@
- list@
- maildaemon@
- noc@
- no-reply@
- noreply@
- null@
- paypal@
- phish@
- phishing@
- post@
- postmaster@
- privacy@
- registrar@
- root@
- spam@
- undisclosed-recipients@
- unsubscribe@
- usenet@
- uucp@
- www@

Klaviyo cannot remove blocks for any role-based email addresses.

## MM3 sends

MM3 messages are emails that result in communications with a cellular device (e.g., pagers and cell phones) in a non-email fashion such as a received text message.

The United States FCC maintains a do not email domain list [here](https://www.fcc.gov/consumer-governmental-affairs/about-bureau/consumer-policy-division/can-spam/domain-name-downloads). All domains listed on this FCC page are expected to result in some form of electronic communication with the end recipient being a cellular phone device or pager. Unsolicited marketing communications to these device types are expressly prohibited and Klaviyo will automatically block sends to these domains.

## Additional resources

[Understand email deliverability](https://help.klaviyo.com/hc/en-us/articles/115005247008)

[Understand bounced emails in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115005250408)

[Understand sender reputation](https://help.klaviyo.com/hc/en-us/articles/15332906406171)