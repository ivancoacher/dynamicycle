---
id: 4417768780827
title: "Troubleshooting branded sending domain issues"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/4417768780827-Troubleshooting-branded-sending-domain-issues"
section: "Monitor deliverability and metrics"
category: "Deliverability & compliance"
category_slug: "deliverability-compliance"
klaviyo_updated: "2026-04-21T13:56:57Z"
language: en
---

## You will learn

Learn how to diagnose verification issues when setting up your branded sending domain (also known as a dedicated sending domain) in Klaviyo.

A branded sending domain enables you to send emails that appear from your brand, rather than from Klaviyo’s shared domain. For setup instructions, visit our guide on [how to set up a branded sending domain](https://help.klaviyo.com/hc/en-us/articles/115000357752).

Google and Yahoo have announced new sender requirements that they are planning to start enforcing in February of 2024. While already best practice, setting up a branded sending domain will be a requirement for bulk senders to land in Gmail inboxes.

Google considers those who send 5000 or more emails to Google accounts per day to be "bulk senders." All traffic from a sender counts towards that 5000 email threshold, including transactional emails.

Learn more about [Gmail and Yahoo’s upcoming sender requirements.](https://www.klaviyo.com/blog/gmail-update)

## Before you begin

Before starting the troubleshooting steps below, confirm that you have attempted to verify your sending domain in Klaviyo and are seeing errors.

Note that Klaviyo will not automatically apply your domain after verification, as we want to ensure that you are ready to warm your sending infrastructure first if applicable. Once verified, you will need to click ****Apply domain****. We also recommend giving time for the DNS to propagate and for the cache to clear. Depending on your DNS provider, this process could take up to 48 hours.

## Troubleshooting using 3rd party tools

Klaviyo requires 3 CNAME or NS records for email authentication, and one TXT record for domain ownership verification. When setting up a branded domain in Klaviyo, you’ll see similar records presented based on your [subdomain](https://klaviyo.zendesk.com/hc/en-us/articles/360055457791) choice:

![NS records](https://klaviyo.zendesk.com/hc/article_attachments/28705664613147)

When setting your branded sending domain, selecting the **Dynamic** routing method requires adding NS records to your DNS provider, while the **Static** routing option requires CNAME records. Klaviyo recommends using the **Dynamic** routing option to best optimize your sends, but if your DNS provider does not support NS records consider using the **Static** routing option.

If your brand chooses to use a 2nd level subdomain like **example.send.klaviyo.com**, the root domain would be **send.example.com** and the sending domain would be **example.send.klaviyo.com.**

In an example where the intended sending domain is **send.klaviyo.com**, with “send” as the subdomain and “klaviyo.com**”** as the root domain, the expected DNS records would be the following:

For the **Dynamic** routing option:

|  |  |  |
| --- | --- | --- |
| ****Host**** | ****Value**** | ****Record Type**** |
| send.helloworld.com | ns1.klaviyo.com | NS |
| send.helloworld.com | ns2.klaviyo.com | NS |
| send.helloworld.com | ns3.klaviyo.com | NS |
| send.helloworld.com | ns4.klaviyo.com | NS |
| helloworld.com | klaviyo-site-verification=public\_API\_key | TXT |

For the **Static** routing option:

These are just examples and the actual CNAME record values for your account will be different. Make sure to use the values generated in your account.

|  |  |  |
| --- | --- | --- |
| ****Host**** | ****Value**** | ****Record Type**** |
| send.klaviyo.com | 1.klaviyodns.com | CNAME |
| kl.\_domainkey.klaviyo.com | kl1.domainkey.1.klaviyodns.com | CNAME |
| kl2.\_domainkey.klaviyo.com | kl2.domainkey.1.klaviyodns.com | CNAME |
| klaviyo.com | klaviyo-site-verification=public\_API\_key | TXT |

A helpful set of tools to check if your records are propagating correctly are MxToolbox's DNS lookups:

- [DNS lookup](https://mxtoolbox.com/SuperTool.aspx)
- [TXT lookup](https://mxtoolbox.com/TXTLookup.aspx)

You can use the DNS lookup tool to search the host for each of the CNAME and NS records, and the TXT lookup tool for the TXT record.

## NS and CNAME lookup examples

Use the DNS check option from the dropdown on MxToolbox:

![DNS check .jpg](https://klaviyo.zendesk.com/hc/article_attachments/28705664615835)

### NS records

![NS troubleshoot.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28705664614299)

### CNAME records

send.klaviyo.com:

![send.klaviyo.com.jpg](https://klaviyo.zendesk.com/hc/article_attachments/36642522069531)

kl.\_domainkey.klaviyo.com:

![kl._domainkey.klaviyo.com  .jpg](https://klaviyo.zendesk.com/hc/article_attachments/36642522076699)

kl2.\_domainkey.klaviyo.com:

![kl2._domainkey.klaviyo.com  .jpg](https://klaviyo.zendesk.com/hc/article_attachments/36642522084763)

### TXT lookup example

klaviyo.com:

![TXT lookup for klaviyo.com](https://klaviyo.zendesk.com/hc/article_attachments/28705664611739)

Based on whether you are seeing values returned by the queries, there are some common errors that may be the source of the issue.

## If queries are returning values

In order for your sending domain to be successfully verified in Klaviyo, the values returned by your queries must match those presented in Klaviyo exactly. Ensure that there are not any discrepancies between the values you are seeing returned, and those in Klaviyo.

### Root domain being appended to values automatically

Some DNS providers expect a period (.) at the end of the added value. Without this period, the DNS provider assumes that the entire value field is a subdomain of the domain being configured, and will automatically add the root domain. For example, if you entered **u161779.wl030.sendgrid** (with no period at the end), this would make the value **u161779.wl030.sendgrid.net.rootdomain.com** instead of just **u161779.wl030.sendgrid.net.**

## If queries are not returning values

### Root domain duplicated in the hostname

We also recommend checking if your DNS provider expects only the subdomains in the host name fields, and automatically appends the root domain. For example, if you add the CNAME record **send.domain.com** it would automatically become **send.domain.com.domain.com**.

Instead, you might need to only add the “send” subdomain in this instance for the record’s host name to be **send.domain.com.** Compare your other DNS records to see if you need to append it or if your provider automatically does this.

### Records being proxied

If your DNS provider allows you to proxy records, you will see issues with the setup of the branded domain in Klaviyo if this feature is enabled. This commonly happens with Cloudflare but is possible with other DNS providers too. You’ll need to disable the proxying of your records for them to resolve over the internet, and so their presence can be verified by the sending domain set up tool in Klaviyo. Record proxying will need to stay disabled after the set up process as well for emails to authenticate as expected.

## Other DNS provider issues

### DNS provider does not support @ symbol

In cases where a DNS provider does not support the symbol “@”, the root domain would need to be set as the hostname for the site verification record. The “@” symbol is the shorthand for the root domain (business.com), so you can use either option depending on what your DNS provider supports.

### DNS provider does not support underscores

Some DNS providers do not support underscores for CNAME records. However, in order for your sending domain to be functional within Klaviyo, these underscores are necessary.

If your DNS provider does not support underscores in your CNAME, we suggest first reaching out to your DNS provider’s support team and seeing if they can create the record for you. Often DNS providers will be able to manually adjust your CNAME to include the underscore if you reach out to them.

If your DNS provider ultimately cannot support underscores, [consider using another provider](https://www.hostinger.com/tutorials/how-to-change-domain-nameservers) as these will be necessary to your domain setup in Klaviyo.

### A TXT value already exists on the root domain

If there is an existing TXT record on your root domain, you can append the Klaviyo value to your existing field. As long as the Klaviyo requested value is present, the record will be successfully validated when setting up your branded domain in Klaviyo.

## DMARC

For emails to be [DMARC compliant](https://help.klaviyo.com/hc/en-us/articles/4402601857307), the root domain on your account needs to align with the from-address domain of your emails.

For example, if you send an email using **sales@example.com** as the from-address, where example.com is protected by DMARC, your account will need to use a branded sending domain like **send.example.com** for all emails sent from Klaviyo to meet DMARC authentication requirements.