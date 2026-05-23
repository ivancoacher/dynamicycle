---
id: 7674941873947
title: "Understanding branded vs. shared sending domains"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/7674941873947-Understanding-branded-vs-shared-sending-domains"
section: "Getting started with email deliverability"
category: "Deliverability & compliance"
category_slug: "deliverability-compliance"
klaviyo_updated: "2026-04-21T13:55:05Z"
language: en
---

## You will learn

Learn more about branded sending domains (also known as dedicated sending domains), how they differ from shared sending domains, and when they may be beneficial for your business to use. In the world of email marketing, your sending infrastructure, including your sending domain, is very important. Sending domains are a key component of your email infrastructure, that to help build a positive reputation and promote [domain alignment](https://help.klaviyo.com/hc/en-us/articles/4402601857307).

If you're interested and ready to set up a branded sending domain, please see our resource on

- A domain that has been registered for at least 30 days AND
- You’ve used the domain to send email already (e.g., you used this domain in the past with a prior email service provider or with Klaviyo in your from address).

## Klaviyo’s default setup

When first onboarding onto the Klaviyo platform, the necessary records are automatically in place to ensure your emails will be delivered to your recipients. These records include your sending domain, or where your emails appear to be sent from. By default, users start out sending from a shared IP and shared Klaviyo domain. This domain will appear in the sender information at the top of an email message as shown below (e.g., **sent on behalf of** or **via klaviyomail.com**). In the example below from Gmail, your recipients see that your sender email address includes **via klaviyomail.com** because you are using a shared sending domain.

![Inside an email inbox showing an example of an email sent from the via klaviyo sending domain](https://klaviyo.zendesk.com/hc/article_attachments/28716066573595)

If you're interested in using a branded sending domain, please see our [setup resource](https://help.klaviyo.com/hc/en-us/articles/115000357752).

## What is a branded sending domain, and why would you use this?

In contrast, a branded sending domain allows you to send emails that appear to be coming from your brand instead of Klaviyo. Any company is eligible to create a branded sending domain. This changes (or removes entirely) the via klaviyomail.com message that is displayed beside your sender email address.

Google and Yahoo have announced sender requirements that they are planning to start enforcing in February of 2024. While already best practice, setting up a branded sending domain will be a requirement for bulk senders to land in Gmail inboxes.

Google considers those who send 5000 or more emails to Google accounts per day to be "bulk senders." All traffic from a sender counts towards that 5000 email threshold, including transactional emails. If you are a new brand on Klaviyo, but plan to send more than 5000 emails to Gmail recipients per day, you should setup a branded sending domain.

Learn more about [Gmail and Yahoo’s sender requirements.](https://www.klaviyo.com/blog/gmail-update)

### Benefits of a branded sending domain

Connecting a branded sending domain allows you to use your brand’s domain name to send emails instead of a shared Klaviyo domain. It also allows you to build a sending reputation on your brand’s own domain, and limit any negative impact to your domain reputation and deliverability from shared senders. In other words, you are the only one that will send from your domain and thus affect your reputation.

MBPs (mailbox providers) are always monitoring activity by reputation, including both domain and IP reputation. If these providers see that emails sent from a particular domain are often marked as spam, rarely opened, or quickly opened and then deleted, that domain may acquire a negative reputation over time.

If you are on a shared sending domain, this means that other Klaviyo customers will use the same sending domain. This could also mean that you will inherit these shared domains' reputations. Even though these domains are consistently reviewed and we work to ensure accounts are using healthy lists, you may want to take deliverability entirely into your own hands. With a branded domain you will have more control over your own sender reputation.

Additionally, connecting a branded sending domain allows you to take advantage of email [authentication protocols like DMARC](https://help.klaviyo.com/hc/en-us/articles/4402601857307). Mail servers use these authentication protocols to verify that incoming emails are from legitimate senders, protecting your brand and your customers from malicious actors. In addition to preventing phishing and spoofing attempts, implementing these protocols can help improve deliverability, as mailbox providers will be able to more easily verify your sender identity.

### Other branded sending domain considerations

If you have a brand new sending domain or are new to email marketing altogether, your domain will not have an email sending reputation yet. Mailbox providers and filter software may consider the age of your domain when determining your trustworthiness as a sender as they lack enough data to show you are reputable and follow [deliverability best practices](https://help.klaviyo.com/hc/en-us/articles/115005247008).

You can use a shared sending domain while you develop an email reputation on your brand's domain by using it in the "friendly from address" first. Once you have sent consistent messaging with positive results over 30 days you can safely set up your branded sending domain. It is still important to remember best practices by not sending to unengaged or purchased lists, as your domain is still young and this can ‌ quickly damage your sending reputation.

If you are considered a bulk sender by Gmail, you must set up a branded sending domain to successfully land in Gmail inboxes. If you do not have prior sending history on your sending domain, make sure to follow the [warming process](https://help.klaviyo.com/hc/en-us/articles/360025945671) to establish a strong initial sender reputation