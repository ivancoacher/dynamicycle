---
id: 9042531198747
title: "How to migrate your branded sending domain from a previous email service provider (ESP) to Klaviyo"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/9042531198747-How-to-migrate-your-branded-sending-domain-from-a-previous-email-service-provider-ESP-to-Klaviyo"
section: "Warm and ramp your domain"
category: "Deliverability & compliance"
category_slug: "deliverability-compliance"
klaviyo_updated: "2026-04-21T13:55:06Z"
language: en
---

## You will learn

Learn how to migrate your existing branded sending domain (also known as a dedicated sending domain) from a previous email service provider (ESP) to Klaviyo.

## Before you begin

New Klaviyo accounts and those on domains that have been registered for less than 30 days should plan to [warm their sending infrastructure](https://help.klaviyo.com/hc/en-us/articles/360025945671) upon setting up a domain in Klaviyo. Warming is the period of time during which you establish a reputation as a legitimate or “good” email sender. Without proper warming, you can risk damaging your sender reputation.

To confirm whether warming is necessary for your account, head to our guide on [how to ramp and warm your sending infrastructure](https://help.klaviyo.com/hc/en-us/articles/360025945671).

Additionally, it is important that you own the domain you are using to send emails, and have the ability to access and update your DNS (domain name system) host records.

## Set up your dedicated infrastructure in Klaviyo

### Branded sending domain

When you are ready to start your sending domain with Klaviyo, [set up a branded sending domain](https://help.klaviyo.com/hc/en-us/articles/115000357752).

You’ll update your DNS settings to include the CNAME and TXT records generated through your Klaviyo account, which will allow you to send emails through your own branded sending domain rather than Klaviyo’s shared domain. Ensure that the [branded sending subdomain](https://help.klaviyo.com/hc/en-us/articles/360055457791) is not already being used within your DNS. If the branded sending subdomain is already being used within your DNS, this can cause conflict with existing records and disrupt other configurations on the domain.

Connecting a branded sending domain also enables DKIM and SPF authentication on sends from Klaviyo using the domain. Authentication is a common email best practice that helps to prevent and alleviate delivery issues, and improve deliverability.

### Dedicated click tracking

If you used a custom click tracking domain with your previous ESP, or would like to begin using one in Klaviyo, you can add additional CNAME records to your DNS settings. [Dedicated click tracking](https://help.klaviyo.com/hc/en-us/articles/360001550572) allows you to display your own domain on click tracking links as opposed to the default Klaviyo encoding, allowing your customers to further trust the emails that come from your brand as the links will be easily recognizable.

### Dedicated IP address

Most small businesses or those just starting out with Klaviyo will be on shared IPs. Depending on your email practices and volumes, this should suffice for your sending needs. The main benefit of using a [dedicated IP address](https://help.klaviyo.com/hc/en-us/articles/7675517826587) is that the reputation of the IP address can only be influenced by the single account that is using it. As such, you have complete control over your email sender reputation, especially if you have higher volumes of email sends.

Note that dedicated IPs are only available for accounts that qualify. To learn if you qualify for a dedicated IP, please reach out to your Customer Success Manager for more information.

## Deliverability factors

When migrating your branded sending domain from another ESP, it is important to be mindful of deliverability to ensure you successfully land in customers’ inboxes.

### Sender reputation

When you migrate your sending domain to Klaviyo from a prior ESP, the sender reputation associated with the domain will carry over as well. Your domain’s sending reputation is a key factor that mailbox providers (MBPs) consider when determining how to sort incoming emails.

If you are seeing deliverability issues with your pre-existing branded sending domain, follow [email deliverability best practices](https://help.klaviyo.com/hc/en-us/articles/115005247008) to improve your sender reputation and adjust your sending strategy. Deliverability issues will not automatically resolve by switching ESPs.

### DMARC

If the domain used in your sender email address (i.e., from-address) has a DMARC policy set, this can impact inbox placement when there is a misalignment between the branded sending domain and the from-address domain. [DMARC](https://help.klaviyo.com/hc/en-us/articles/4402601857307) is a protocol designed to give domain owners the ability to protect their domain from unauthorized users sending emails, commonly known as email spoofing.

With a branded sending domain, make sure that your domain and your from-address in Klaviyo align.

For example, if you send an email using **sales@example.com** as your from-address, where **example.com** is protected by DMARC, your account will need to use a branded sending domain like **send.example.com** for all emails sent from Klaviyo to meet DMARC authentication requirements. Accounts with branded sending domains may be impacted if there is not alignment with the sender email address.

Misalignments typically impact accounts using Klaviyo’s default shared sending domain to send emails that have a from-address domain with a DMARC policy on it. If you use Klaviyo’s shared domain, remove DMARC associated with the from-address domain to avoid this.

## Remove DNS records generated through prior ESP

Once you no longer need to send on your prior ESP, remove the associated records from your DNS. This requires you to complete tasks outside of Klaviyo, and you may need to consult your IT team on the below next steps.

Note that not all domain registration services allow you to directly edit all DNS records. If you cannot update the records, contact your DNS provider for information on how to update them.

Once the DNS records from your previous ESP are removed, emails will stop sending from your branded sending domain on that platform. Confirm that you no longer need your dedicated infrastructure on your prior ESP before removing the records.

1. Navigate to your applicable DNS provider. Common providers include:
   - [GoDaddy](https://www.godaddy.com/help/manage-dns-records-680)
   - [Google Domains](https://support.google.com/a/answer/48090?hl=en)
   - [Hostgator](https://www.hostgator.com/help/article/manage-dns-records-with-hostgatorenom)
   - [Hover](https://help.hover.com/hc/en-us/articles/217282457-How-to-Edit-DNS-records-A-CNAME-MX-TXT-and-SRV-Updated-Aug-2015-)
   - [Namecheap](https://www.namecheap.com/support/knowledgebase/article.aspx/9214/31/cpanel-email-deliverability-tool-spf-and-dkim-records/)
   - [Squarespace](https://support.squarespace.com/hc/en-us/articles/205812348-Opening-Advanced-DNS-settings)
   - [AWS](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-editing.html)
   - [Cloudflare](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/)
2. Delete any CNAME and TXT records in your DNS setting that were generated through your previous ESP. Some providers might also have MX records that were installed if the service handled reply management.

If you have other types of records in your DNS from your prior ESP, reach out to our [Support Team](https://help.klaviyo.com/hc/en-us/articles/115001002272).

## Important considerations

### Migrate unsubscribe and suppression data

When migrating your dedicated sending domain to Klaviyo, it is important to bring in all the data available on your previous ESP regarding permissions. This includes information such as subscription method and timestamp for email and SMS opt-ins, along with all unsubscribe and bounce data. By importing this data to Klaviyo, you can avoid sending to profiles that might harm your infrastructure’s deliverability.

For more information regarding migrating data from your previous provider, see our guide on [how to migrate existing email subscribers (and unsubscribes) into Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115005078487).

If you are [migrating from Mailchimp](https://help.klaviyo.com/hc/en-us/articles/115005254948), you should also suppress contacts with a 1 star rating in Mailchimp as sending to them can harm your deliverability.