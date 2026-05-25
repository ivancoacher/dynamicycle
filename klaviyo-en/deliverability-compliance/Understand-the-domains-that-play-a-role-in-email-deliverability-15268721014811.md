---
id: "15268721014811"
title: "Understand the domains that play a role in email deliverability"
source_url: "https://help.klaviyo.com/hc/en-us/articles/15268721014811-Understand-the-domains-that-play-a-role-in-email-deliverability"
section: "Getting started with email deliverability"
category: "Deliverability & compliance"
category_slug: "deliverability-compliance"
klaviyo_updated: "2026-04-21T13:54:28Z"
language: "en"
---
## You will learn

Learn about the different domains that play a role in the delivery of your emails, as well as the importance of domain alignment.

## From Address domain

The From Address domain, also known as the “friendly from address domain,” refers to the domain associated with the email address that you are sending from.

This is the most important domain in your emails because your subscribers see this in their inbox. It represents your brand, and is the primary domain that email providers use to track your reputation.

 In a typical inbox, like Gmail, you will see the From Address here:

![domain after @ in friendly from address](https://klaviyo.zendesk.com/hc/article_attachments/28717994485659)

You can [set the From Address](https://help.klaviyo.com/hc/en-us/articles/360024994912) and the accompanying "From" name for any campaign in Klaviyo.

## Sending domain

A sending domain is the domain used to send emails, andshow subscribers where your emails are sent from. By default, most users will begin with sending from a shared Klaviyo domain. This domain will appear in the sender information at the top of an email message.

In the example below from Gmail, your recipients see that your sender email address includes "via klaviyomail.com” because you are using a shared sending domain.

![Via klaviyomail.com showing due to shared domain](https://klaviyo.zendesk.com/hc/article_attachments/28717994492315)

A [branded sending domain](https://help.klaviyo.com/hc/en-us/articles/7674941873947) allows you to send emails that appear to be coming from your brand to give you better control of your sender reputation. Moving to a branded sending domain will remove the "via klaviyomail.com" message displayed beside your sender email address. This also means that your emails will no longer be sent by a shared domain.

Google and Yahoo have announced new sender requirements that they are planning to start enforcing in February of 2024. While already best practice, setting up a branded sending domain will be a requirement for bulk senders to land in Gmail inboxes.

Google considers those who send 5000 or more emails to Google accounts per day to be "bulk senders." All traffic from a sender counts towards that 5000 email threshold, including transactional emails.

Learn more about [Gmail and Yahoo’s upcoming sender requirements.](https://www.klaviyo.com/blog/gmail-update)

## Return-Path domain

A Return-Path domain (also known as: Mail From, Envelope From, origin, bounce address, SPF domain, mailed-by, mail server domain) represents the domain name of the server that sent the email.

This domain is necessary for the delivery of your message; however, it's usually hidden from the recipient. For example, Gmail shows it in a hidden dropdown as the “mailed-by” domain. You can see this by clicking ****to me**** in your Gmail message.

![Mailed by domain in message details of inbox](https://klaviyo.zendesk.com/hc/article_attachments/28717994495387)

With Klaviyo, the Return-Path domain will be similar to **klaviyomail.com******.**** This domain is also where bounce notifications will go, and is managed by Klaviyo. If a message bounces, it will automatically log the event in your account.

When an inbox provider like Gmail receives a message, they check the Return-Path domain for the [SPF record](https://help.klaviyo.com/hc/en-us/articles/4402601857307). Since Klaviyo manages the Return-Path domain for you, SPF is functional by default. You do not need to modify any SPF records for Klaviyo.

SPF on the Return-Path will always pass with Klaviyo, but your reporting may show that it fails “alignment.” When this happens, the Return-Path domain is passing SPF, but it does not match the From Address domain. You might also see this in Google Postmaster Tools; however, this is not an issue unless you have set up [DMARC](https://help.klaviyo.com/hc/en-us/articles/4402601857307) without setting up and aligning DKIM with your sending domain.

## DKIM domain

A DKIM domain (also known as the “signed-by domain”, d= domain) cryptographically signs emails that you send, allowing the receiving mailbox provider to confirm that the owner of the domain sent the message. This domain does not have to match the From Address or the Return-Path, and is only used to sign the email.

By default, it will be a domain owned and operated by Klaviyo, like **klaviyomail**. This allows DKIM to work immediately when you start with Klaviyo.

Note that you can only DKIM-sign your messages with a domain you own. The DKIM domain is an important part of your overall sender reputation, and its own reputation has a major influence on whether the message is delivered.

The DKIM domain will appear after the “via” header and also as the “signed-by” within Gmail:

![DKIM domain shown for signed-by in message details](https://klaviyo.zendesk.com/hc/article_attachments/28718022231067)

When you set up a [branded sending domain](https://help.klaviyo.com/hc/en-us/articles/7674941873947), your email will be DKIM-signed by your own domain in addition to a shared domain.

## Click tracking domain

Click tracking domains are used to track clicks on the links you include in your content. When someone clicks a link, they will be redirected through a URL associated with the click tracking domain, and then immediately passed through to the original URL.

If you hover over a link in your inbox you will see the full tracking link:

![Dedicated click tracking domain shown on hover](https://klaviyo.zendesk.com/hc/article_attachments/28718022237211)

[Dedicated click tracking](https://help.klaviyo.com/hc/en-us/articles/7676795223707) allows you to display your own domain on click tracking links, rather than Klaviyo's. Having recognizable links in the emails coming from your brand will help you build trust with your customers that receive those emails. Instead of a long string of letters and numbers from a **trk.klaviyomail** encoded link, they will see your brand’s name when hovering over links in your email. This familiarity may increase the chances that they will click on your links.

Additionally, many mailbox providers and filtering software will consider the reputation of all domains used in your messaging. Using the same root domain in both your dedicated click tracking links and your sending domain creates alignment across your brand identity.

## Domain alignment for DMARC

In order to be DMARC compliant, you must have a branded sending domain that matches the domain in your sender email address (i.e. your From Address). For example, if you send an email using **sales@example.com** as the From Address and **example.com** is protected by DMARC, your account will need to use a branded sending domain like **send.example.com** to meet DMARC requirements.

DMARC is not required to send marketing emails on Klaviyo. To configure and implement a DMARC policy, we recommend working with your IT team and a 3rd-party DMARC service provider.

Note that neither the Return-path nor the DKIM domain will match your From Address when you start with Klaviyo. This is the default scenario for any new Klaviyo customer. Your domains don't need to align unless you have set up DMARC.

However, you can align the DKIM domain with your from-address by [setting up a branded sending domain](https://help.klaviyo.com/hc/en-us/articles/115000357752).

## Benefits of domain alignment

There are 2 major benefits of domain alignment:

1. Domain alignment allows DMARC to “pass." You will need to align either the DKIM domain to match with your From Address to achieve this.
2. Aligning as many domains as possible helps you further establish your domain reputation. Inbox providers and spam filters often consider domain alignment when deciding if you are a reputable. Recipients are more likely to trust you as a sender if your domains align (i.e., From Address domain matches click tracking domain, etc).

It is best practice to align all domains if possible. By setting up and aligning your sending and DKIM domain, click tracking domain, and From Address domain, inbox providers will more favorably determine your sending reputation.

## Additional resources

- [Understanding email authentication](https://help.klaviyo.com/hc/en-us/articles/4402601857307)
- [Understanding email deliverability](https://help.klaviyo.com/hc/en-us/articles/115005247008)