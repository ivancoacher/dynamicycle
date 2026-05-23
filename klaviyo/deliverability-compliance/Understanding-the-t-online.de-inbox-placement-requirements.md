---
id: 1260804570090
title: "Understanding the t-online.de inbox placement requirements"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/1260804570090-Understanding-the-t-online-de-inbox-placement-requirements"
section: "Monitor deliverability and metrics"
category: "Deliverability & compliance"
category_slug: "deliverability-compliance"
klaviyo_updated: "2026-04-21T13:54:26Z"
language: en
---

## You will learn

Learn how to meet the t-online.de requirements delivery. T-online.de is an inbox provider predominantly used by German subscribers with unique requirements for delivery. As a result, you may see a rise in bounces from this provider, lowering your ability to reach these German recipients.

If you see a rise in bounces unrelated to the t-online.de requirements or are looking for additional guidance on this topic, head to our guide on [how to decrease bounce rates](https://klaviyo.zendesk.com/hc/en-us/articles/360057036052).

## Prerequisites

Before jumping in, check that you have already created a dedicated sending domain in Klaviyo.

1. To see if this is established in your account, click into the account dropdown in the upper right and select ****Settings****.
2. Then, navigate to ****Email > Domains****. Here, you will either see information about your established domain or you will see getting started information.
3. If you need to create your dedicated sending domain, click ****Get Started**** and follow the instructions outlined in our guide on [setting up a dedicated sending domain.](https://help.klaviyo.com/hc/en-us/articles/115000357752)
4. Then, proceed to the next step in this article to align with t-online.de best practices.

## t-online.de delivery requirements

t-online.de has the following requirements to reach any subscribers who use their inbox service:

- Enable double opt-in for your lists
- Your Sender Policy Framework (SPF), DomainKeys Identified Mail (DKIM), Reverse DNS (rDNS; i.e., your domain for dedicated IP), and your sender email domains in Klaviyo (the from-address for each email send) must all align

In the next few sections we will dive deeper into each of these requirements.

## Enable double opt-in

Lists are set to double opt-in by default in all Klaviyo accounts and we strongly suggest that you keep this setting enabled to avoid t-online.de blocking your emails. Double opt-in is the process through which a new subscriber must confirm their subscription via email before being added to your list. For more information, head to our [guide about the double opt-in process.](https://klaviyo.zendesk.com/hc/en-us/articles/115005251108)

## Align your sender identification

The next requirement for t-online.de inbox placement is to align your domains across all of the following sender identification tools:

- ****Sender Policy Framework (SPF)****
  The SPF domain will be your dedicated sending domain, setting up dedicated sending will automate this authentication measure.
- ****DomainKeys Identified Mail (DKIM)****
  The DKIM domain will also be established using the same dedicated sending domain as mentioned above.
- ****Reverse DNS (rDNS)****
  The rDNS domain is established when you have obtained a dedicated IP address.
- ****Sender Email Address****
  This is your from-address and can be adjusted for each campaign and flow email.

Each of these root domains must match each other exactly in order for your email to reach a t-online.de inbox. For example, your dedicated sending domain in Klaviyo will look something like this: **send.helloworld.com**. However, if you send an email to subscribers from: **personalemail@email.com**, then your message will be blocked from reaching t-online.de inboxes since your sender email address does not exactly match your dedciated sending domain.

The table below provides an example of when root domains align (which t-online.de will accept) and when they do not (which t-online.de will block from reaching inboxes).

|  |  |  |
| --- | --- | --- |
|  | ****Root domains align**** | ****Root domains**** ******do not****** ****align**** |
| ****Dedicated sending domain**** | send@****helloworld.com**** | send@****helloworld.com**** |
| ****Sender email address (from-address)**** | example@****helloworld.com**** | example@****helloearth.com**** |
| ****rDNS domain (for your dedicated IP)**** | XXX.send.****helloworld.com**** | XXX.send.****helloearth.co.uk**** |

It is crucial that, when you build out any campaigns and flows, you make sure that your sender email address directly matches your dedicated sending domain and dedicated IP rDNS domain. For campaigns and flows, you can edit your sender address in the box labeled **Sender email address**, as shown below. You may also edit your default sender address within your account settings using the instructions in [this guide](https://klaviyo.zendesk.com/hc/en-us/articles/360024994912).

![Inside the campaign editor with fields to setup sender name, email address, subject, and preview text](https://klaviyo.zendesk.com/hc/article_attachments/28720658999963)

If, after following these best practices, your emails to t-online.de continue to bounce, review the [t-online.de postmaster page](https://postmaster.t-online.de/index.en.html) to make sure that your current sending habits align with their recommendations.

## Additional resources

- [How to set up a dedicated sending domain](https://klaviyo.zendesk.com/hc/en-us/articles/115000357752)
- [How to choose a subdomain for dedicated sending](https://klaviyo.zendesk.com/hc/en-us/articles/360055457791)
- [Understanding bounced emails in Klaviyo](https://klaviyo.zendesk.com/hc/en-us/articles/115005250408)