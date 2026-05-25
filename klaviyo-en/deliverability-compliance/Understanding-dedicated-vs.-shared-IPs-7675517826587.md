---
id: "7675517826587"
title: "Understanding dedicated vs. shared IPs"
source_url: "https://help.klaviyo.com/hc/en-us/articles/7675517826587-Understanding-dedicated-vs-shared-IPs"
section: "Getting started with email deliverability"
category: "Deliverability & compliance"
category_slug: "deliverability-compliance"
klaviyo_updated: "2026-04-21T13:55:05Z"
language: "en"
---
## You will learn

Learn more about dedicated vs. shared IPs, their benefits and drawbacks, and how IPs are used in your sending infrastructure.

Note that dedicated IPs are only available to accounts that qualify. To learn if you qualify for a dedicated IP, please reach out to your Customer Success Manager for more information. For more information on plans and success support, learn more in our article, [How free and paid plans differ](https://help.klaviyo.com/hc/en-us/articles/360050759151-How-Free-and-Paid-Plans-Differ#talk-with-customer-success-managers-and-onboarding-specialists4).

## Dedicated vs. shared IPs

Mailbox providers look at your overall reputation, including your IP's, when determining where to place an email (inbox, spam, etc). The IP reputation, domain reputation, recipient positive and negative engagements are just a few of the factors that influence your [overall deliverability](https://help.klaviyo.com/hc/en-us/articles/115005247008).

Sending from a shared IP address means that you will send alongside several other Klaviyo customers, which also means a shared sending reputation. Moving to a dedicated IP address (not to be confused with [branded sending domains](https://help.klaviyo.com/hc/en-us/articles/7674941873947)), will allow you to take full ownership over the IPs reputation as you will be the only one using it for email traffic.

## Staying on a shared IP

****Benefits of keeping the default shared IP****
Most small businesses or those just starting out with Klaviyo, will be on shared IPs. Depending on your email practices and volumes, this should suffice for your sending and reputation needs. Klaviyo automatically assigns shared IP addresses to most new accounts. With shared IPs, you can benefit from other senders keeping the IP pool reputation up and warm with overall volume. Klaviyo constantly monitors these IP’s and removes any harmful senders.

****Drawbacks of staying on a shared IP****
Shared IPs are intended for use by small senders that don't send on a regular cadence. The reasoning for this is that the small senders can band together to create a reputation. Therefore, if you send high volumes at a regular frequency to warrant a dedicated IP, you are going to be controlling the reputation in the shared pool anyway. During holidays and other high traffic periods, volumes can fluctuate and it can affect your performance. If you qualify for a dedicated IP it is best to move to using one.

## Moving to a dedicated IP

****Benefits of moving to a dedicated IP****
The main benefit of using a dedicated IP address is that the reputation of the IP address can only be influenced by the single account that is using it. As such, you have complete control over your own sender reputation. Similarly, you also have complete control over your sending volumes, and will not be affected by shared IP and potential volume spikes during busy times of year. In addition, if you encounter deliverability issues, you can more easily pinpoint the root causes since it’s only your messaging. When several senders use the same IP, it's hard to figure out where an issue originated from and how to fix it. By using a dedicated IP, you’re only maintaining your own sends and IP address. Even though you are solely responsible for the dedicated IPs reputation, if you ‌see deliverability issues, our Support Team can better help you identify the cause and provide solution options.

****Drawbacks of moving to a dedicated IP****
The potential negative of using a dedicated IP address is that you must send at a consistent cadence with a high volume. This helps ensure ‌you can maintain a healthy sender reputation for deliverability and are seen as a reputable sender by mailbox providers.

Additionally, you will need to update your DNS records and warm your infrastructure in a different, more engagement-focused way. [Learn more about dedicated IP warming](https://help.klaviyo.com/hc/en-us/articles/7521152741403).

## Dedicated IP warming

When getting started on a new IP address, you must go through the [warming process](https://help.klaviyo.com/hc/en-us/articles/7521152741403) to establish a healthy sender reputation that inbox providers trust. During the warming process, emails must be sent gradually to avoid being blocked by inbox providers that have not previously seen activity from that IP.

Klaviyo initially sends a small portion of emails through the dedicated IP while routing the rest through shared IPs. Over time, the proportion of emails sent via the dedicated IP increases progressively until all traffic is sent through the dedicated IP.

There are few key aspects to note about dedicated IP warming:

- The duration of the warming period depends on sending volume but typically lasts about 30-40 days.
- Sending volume on the dedicated IP(s) during warming increases on a non-linear curve, with most of the sending volume increase occurring towards the end of warming.
- The segmentation recommendations provided by our customer support team during warming are to create a strong sending reputation for the new IPs, and are not concerned with the total volume.