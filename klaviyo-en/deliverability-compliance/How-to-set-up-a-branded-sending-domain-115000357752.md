---
id: "115000357752"
title: "How to set up a branded sending domain"
source_url: "https://help.klaviyo.com/hc/en-us/articles/115000357752-How-to-set-up-a-branded-sending-domain"
section: "Warm and ramp your domain"
category: "Deliverability & compliance"
category_slug: "deliverability-compliance"
klaviyo_updated: "2026-05-15T09:38:12Z"
language: "en"
---
## You will learn

Learn how to set up a branded sending domain (also known as a dedicated sending domain) so that when emails reach inbox providers, they will appear to come from your brand instead of Klaviyo.

If you are bringing over an existing branded sending domain from a prior email service provider (ESP), head to our detailed [migration guide](https://help.klaviyo.com/hc/en-us/articles/9042531198747).

![](https://fast.wistia.com/embed/medias/yuhwp4mwi2/swatch)

## What is a branded sending domain?

A branded sending domain allows you to send emails that appear to be coming from your brand and allows you to have better overall control of your sender reputation. Any company is eligible to create a branded sending domain.

By default, most users will start out sending from a shared IP and Klaviyo domain. This domain will appear in the sender information at the top of an email message as shown below (i.e., “sent on behalf of '' or “via klaviyomail.com”).

In the example below from Gmail, your recipients see that your sender email address includes "via klaviyomail.com” because you are using a shared sending domain.

![An example of an email with klaviyomail.com domain before it has been updated](https://klaviyo.zendesk.com/hc/article_attachments/28723622866075)

By moving to a branded sending domain, you will remove the "via klaviyomail.com" message that is displayed beside your sender email address. This also means that your emails will no longer be sent by a shared domain, allowing inbox providers to more easily verify your identity and pass [email authentication protocols like DMARC](https://help.klaviyo.com/hc/en-us/articles/4402601857307).

Google and Yahoo have announced new sender requirements that they are planning to start enforcing in February of 2024. While already best practice, setting up a branded sending domain will be a requirement for bulk senders to land in Gmail inboxes.

Google considers those who send 5000 or more emails to Google accounts per day to be "bulk senders." All traffic from a sender counts towards that 5000 email threshold, including transactional emails.

Learn more about [Gmail and Yahoo’s upcoming sender requirements.](https://www.klaviyo.com/blog/gmail-update)

## About generating domain name systems (DNS) with Klaviyo

A key part of connecting a branded sending domain is generating the required DNS records. To generate your records, you'll need to enter the information below when setting up your branded sending domain in Klaviyo.

- ****Root domain****
  This is the domain that you purchased or registered with a domain registrar, and it reflects your brand's website domain. You may also have email addresses that reflect this domain. For example, if your company is called **Hello World**, your brand's root domain may be **helloworld.com** and your friendly from-address may be **name@helloworld.com**.
- ****Branded sending domain****
  This is the domain that will be used to send emails from Klaviyo and will appear in your email headers. It's important to note that the branded sending domain must have a unique, unused subdomain so as not to interfere with any external email configurations on your root domain. The most commonly used subdomain name at Klaviyo is "send." Using the example above, Hello World's branded sending domain could be **send.helloworld.com**. However, you can use any subdomain that is not already in use.

Multiple companies, and thus multiple Klaviyo accounts, can use a given sending domain as long as all relevant DNS records are in place. If your company has multiple child brands with separate Klaviyo accounts, you can use the same branded sending domain in each account. In order to do this, you will need to connect the branded sending domain to each account and generate the unique DNS records required for each one.

## Dynamic vs. static routing

When setting up your branded sending domain, you can select whether you’d like to delegate your subdomain to Klaviyo so it can dynamically select the best sending provider option.

By delegating your subdomain, you are providing Klaviyo authorization to manage your brand's subdomain and create DNS records. These permissions are only used for tasks related to your sending, and subdomain delegation does not impact your brand's root domain or any other subdomains.

You can revoke the subdomain delegation at any point by removing the associated DNS records added during the branded sending domain setup process.

In Klaviyo, you can select the following routing options when setting up your branded domain:

- ****Dynamic****
  Delegate your subdomain to Klaviyo to dynamically select an email sending provider for optimal performance, reputation, and stability.
- ****Static****
  Allow Klaviyo to send email through a single, static email sending provider.

When generating DNS records, Klaviyo will create NS records for the **Dynamic** routing option, and CNAME records for the **Static** routing option.

Some DNS providers do not support NS records. If your DNS provider does not support NS records, you must use the **Static** routing option.

Klaviyo recommends selecting the **Dynamic** routing option to best optimize your sending performance.

If you are on a branded sending domain created prior to this feature, or decide you'd like to move from **Static** to **Dynamic**, remove your domain in Klaviyo and delete the existing CNAME records for the subdomain in your DNS provider. Once complete, go through the setup process with the **Dynamic** option. Note that record propagation can take up to 48 hours.

## Requirements for creating a branded sending domain

### Before you begin

Before starting this process, new Klaviyo accounts should make sure that you'll have time to [warm your infrastructure](https://help.klaviyo.com/hc/en-us/articles/360025945671).

Additionally, it is important that you own the domain you are using to send email, and you, or someone on your team, has access to the DNS host to create the required records.

Existing Klaviyo customers moving to a branded sending domain do not have to warm infrastructure again, as long as you have:

- A domain that has been registered for at least 30 days AND
- You’ve used the domain to send email already (e.g., you used this domain in the past with a prior email service provider or with Klaviyo in your from address).

Before applying any domain changes to your account, pause all sending. Once you have applied the change and tested, you can then resume flows and schedule any future campaigns.

### Checklist

1. Connect branded sending domain and generate DNS records.
2. Update DNS records with your DNS provider (note that this is not done within Klaviyo).
3. Verify and apply your domain.
4. New Klaviyo accounts can then warm their sending infrastructure. For existing Klaviyo accounts with at least a 30 day sending history, they can return to normal sending and do not have to warm their infrastructure again.

## Generate DNS records in Klaviyo

Klaviyo requires 3 CNAME or 4 NS records for email authentication, and one TXT record for domain ownership verification. The Dynamic routing option uses NS records, while the Static routing option uses CNAME records.

Only those with **Owner**, **Admin**, **Manager**, and **Campaign Coordinator**[user roles](https://help.klaviyo.com/hc/en-us/articles/115005231648) can set up a branded sending domain.

1. Click on your company name in the bottom left corner of your account.
2. Select ****Settings****.
   ![Klaviyo account menu in bottom left corner](https://klaviyo.zendesk.com/hc/article_attachments/28723628194843)
3. Choose ****Domains**** from the main tab.
4. Select ****Add Domain.****
5. Verify your brand's root domain is correct. Klaviyo automatically pulls the domain from your account.
   ![root domain.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28723622878235)
6. Click ****Next****.
7. Specify an arbitrary and unused subdomain (i.e., one that you do not currently have in use elsewhere in your marketing) under **Sending domain** (e.g., "send").
   ![](https://klaviyo.zendesk.com/hc/article_attachments/38091860756891)
8. Select your desired **Routing** type (i.e., **Dynamic** or **Static**).

   The **Dynamic** option is only available for domains that support a dynamic configuration.
9. Select whether you’d like to add a DMARC record to your domain (this is recommended to meet Gmail and Yahoo sender requirements). Only domains currently missing a DMARC record will see this option.
10. Select whether you want to connect a domain with Entri, or set it up manually.

![](https://klaviyo.zendesk.com/hc/article_attachments/38092031975067)

Only domains eligible for an integration with Entri will see the automatic setup option.

If you choose to manually set up your domain, the generated DNS records will be presented to you so you can manually add them to your DNS. With automatic configuration through Entri, the records will be added automatically on your behalf.

At this time it is not possible to use a static branded sending domain with dedicated click tracking on Sendgrid infrastructure. If you are using dedicated click tracking with Sendgrid, update your CNAME records to use Klaviyo infrastructure or set up a dynamic branded sending domain.

### DNS records

In an example where the intended sending domain is **send.helloworld.com**, with “send” as the subdomain and “helloworld.com” as the root domain, the generated DNS records will have the following structure.

These are just examples and the actual CNAME record values for your account will be different. Make sure to use the values generated in your account.

|  |  |  |
| --- | --- | --- |
| ****Host**** | ****Value**** | ****Record Type**** |
| send.helloworld.com | ns1.klaviyo.com | NS |
| send.helloworld.com | ns2.klaviyo.com | NS |
| send.helloworld.com | ns3.klaviyo.com | NS |
| send.helloworld.com | ns4.klaviyo.com | NS |
| helloworld.com | klaviyo-site-verification=public\_API\_key | TXT |

With the **Static** routing option that uses CNAME records, the records will look like:

|  |  |  |
| --- | --- | --- |
| ****Host**** | ****Value**** | ****Record Type**** |
| send.helloworld.com | 1.klaviyodns.com | CNAME |
| kl.\_domainkey.helloworld.com | kl1.domainkey.1.klaviyodns.com | CNAME |
| kl2.\_domainkey.helloworld.com | kl2.domainkey.1.klaviyodns.com | CNAME |
| helloworld.com | klaviyo-site-verification=public\_API\_key | TXT |

If your brand's intended sending domain has two subdomains, such as **send.mail.helloworld.com,** “send” would be used for the subdomain and “mail.helloworld.com” for the root domain. The expected DNS records would be the following:

|  |  |  |
| --- | --- | --- |
| ****Host**** | ****Value**** | ****Record Type**** |
| send.mail.helloworld.com | ns1.klaviyo.com | NS |
| send.mail.helloworld.com | ns2.klaviyo.com | NS |
| send.mail.helloworld.com | ns3.klaviyo.com | NS |
| send.mail.helloworld.com | ns4.klaviyo.com | NS |
| helloworld.com | klaviyo-site-verification=public\_API\_key | TXT |

With the **Static** routing option that uses CNAME records, the records will look like:

|  |  |  |
| --- | --- | --- |
| ****Host**** | ****Value**** | ****Record Type**** |
| send.mail.helloworld.com | 1.klaviyodns.com | CNAME |
| kl.\_domainkey.mail.helloworld.com | kl1.domainkey.1.klaviyodns.com | CNAME |
| kl2.\_domainkey.mail.helloworld.com | kl2.domainkey.1.klaviyodns.com | CNAME |
| helloworld.com | klaviyo-site-verification=public\_API\_key | TXT |

## DMARC

DMARC is an [email authentication](https://help.klaviyo.com/hc/en-us/articles/4402601857307) policy that allows inbox providers to verify the authenticity of an email, giving domain owners the ability to protect their domain from unauthorized use. A DMARC policy is also a [sender requirement](https://www.klaviyo.com/blog/gmail-update) established by Gmail and Yahoo to successfully land in inboxes.

If you’d like Klaviyo to generate a DMARC record, toggle on the Add DMARC record option when setting up your branded sending domain.

![Inner Wrapper.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28723622880923)

Klaviyo will generate the following DMARC record, which will not impact the delivery of your emails but satisfy Gmail and Yahoo sender requirements:

v=DMARC1; p=none;

## Update your DNS records

### Automatically publish records with Entri

To have Klaviyo automatically publish DNS records on your behalf, select the Connect with Entri option during the branded sending domain set up process.

When proceeding with this option, Klaviyo will analyze your domain to detect the DNS provider it is hosted with. Once identified, you will be prompted to login to your DNS provider with the appropriate credentials, giving Klaviyo access to publish records on your behalf.

If Klaviyo is not able to detect your DNS provider, you’ll need to manually set up your branded sending domain.

![login.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28723622903195)

If another member of your team manages your DNS settings, you can forward the login by selecting **Or forward login to someone else**. Additionally, you can view the records being added by selecting **Show added DNS** records.

Once signed in, Klaviyo will set the necessary records and your domain will be successfully configured for sending. You’ll see a confirmation once the configuration is complete.

![Entri Modal.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28723628222363)

### Set up your domain manually

If you choose to manually set up your branded sending domain, this step of the process requires you to complete tasks outside of Klaviyo. You will need to apply your new DNS records, which were generated in Klaviyo, to your domain. Note that you will need to go to your company’s DNS provider’s platform to make these changes. You may also need to consult your IT team on the below next steps.

You do not need to create your subdomain within your DNS settings. CNAME and NS records should be added to your brand's root domain, and automatically redirect the subdomain specified during the branded domain setup process to Klaviyo infrastructure via the records.

Not all domain registration services allow you to directly edit all DNS records. If you cannot update the records, contact your DNS provider for information on how to update them.

1. After selecting **Set up manually**, select your domain provider on the **Find your DNS zone file** page. Based on your domain provider, Klaviyo will show the steps to find the zone file in your DNS provider’s platform. The zone file is where you’ll add the generated DNS records to.
2. Select ****Next****.
3. Hover over and click the text to copy the generated DNS records to your clipboard so you can add them to your DNS zone file.
4. Add the records to your zone file in your DNS provider’s platform.

![Records.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28723628225307)

Some common DNS providers include:

- [GoDaddy](https://www.godaddy.com/help/manage-dns-zone-files-680)
- [Google Domains](https://support.google.com/a/answer/48090?hl=en)
- [Hostgator](https://www.hostgator.com/help/article/manage-dns-records-with-hostgatorenom)
- [Hover](https://help.hover.com/hc/en-us/articles/217282457-How-to-Edit-DNS-records-A-CNAME-MX-TXT-and-SRV-Updated-Aug-2015-)
- [Namecheap](https://www.namecheap.com/support/knowledgebase/article.aspx/9214/31/cpanel-email-deliverability-tool--spf-and-dkim-records/)
- [Squarespace](https://support.squarespace.com/hc/en-us/articles/205812348-Opening-Advanced-DNS-settings)
- [AWS](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-editing.html)
- [Cloudflare](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/)

****For BigCommerce Domains****

If you are a merchant using BigCommerce Domains as your DNS provider, the host values for your DNS records are slightly different from what you’ll see provided in Klaviyo.

You must use the **Static** routing option when setting up a branded sending domain as the NS records associated with the **Dynamic** option are not supported.

For the **Host** of the 3 CNAME records, you must append a period followed by your root domain name to the **Host** of the records provided in Klaviyo. For example, if your brand’s root domain is **helloworld.com**, the **Host** values you must enter into BigCommerce look like this:

These are just examples and the actual CNAME record values for your account will be different. Make sure to use the values generated in your account.

|  |  |  |
| --- | --- | --- |
| ****Host**** | ****Value**** | ****Record Type**** |
| send.helloworld.com | 1.klaviyodns.com | CNAME |
| kl.\_domainkey.helloworld.com | kl1.domainkey.1.klaviyodns.com | CNAME |
| kl2.\_domainkey.helloworld.com | kl2.domainkey.1.klaviyodns.com | CNAME |
| helloworld.com | klaviyo-site-verification=public\_API\_key | TXT |

If you use Google Domains as your DNS provider and are connecting a branded sending domain with the **Dynamic** routing option, add all the NS records [into a single record](https://community.klaviyo.com/analytics-and-deliverability-72/help-dns-record-for-google-domains-10653) with the "Add more to this record option."

If your DNS provider does not accept the "@" symbol during this process, then your TXT record will need to be added with your root domain as the hostname. The “@” symbol is just the shorthand method to achieve the same result (i.e., placement of a TXT record on the root domain). For example, the record will simply be:

`Type: TXT
Hostname: YOURWEBSITE.COM
Value: klaviyo-site-verification=YOUR_PUBLIC_API_KEY`

## Verify and apply your domain

You should only begin the steps below if you are ready to start sending with your domain. If you are connecting a new branded sending domain with no emailing history, you will need to first [warm this domain.](https://help.klaviyo.com/hc/en-us/articles/360025945671)

If you are an existing account who has at least a 30-day sending history with Klaviyo, you do not have to re-warm.

Select the Verify button to begin the verification process once you have added the generated records to your DNS. When first accessing the verify records step, it is expected to see the records have not been verified yet.

![verify.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28723622898203)

Review any message that appears. You will see one of the following messages:

- If a campaign is conflicting, you will see a notification that the deliverability may be impacted. To avoid any conflicting errors, a best practice is to make sure there are no campaigns actively sending or scheduled to go out soon. It is also best practice (but is not required) to pause flows and campaigns until after you apply and test your changes.
- If your records are valid, you will see a success message. This success message may indicate that you need to warm your infrastructure again. Note that this only applies to brand new Klaviyo accounts or newly registered domains (within the last 30 days). If you are an existing account who has at least a 30-day sending history with Klaviyo, you do not have to re-warm.
- If your records are not valid, you will see an error indicating what has not been set up correctly.

Once the records have been verified, select ****Apply Domain**** when you are ready to begin sending on your branded domain.

It can take up to 48 hours for DNS records to update after they are published in your DNS settings.

Klaviyo will now apply your branded sending domain to your account, and produce a success message when completed.

You should exclude the subdomain in your from-address that you use to send emails (e.g. **@send.yourbusiness.com**). If it is included in your from-address, you will not be able to receive responses from recipients to emails from your Klaviyo account. Instead, it is advised to just use the root domain alone for your from-address (e.g. **@yourbusiness.com**).

### Troubleshooting error messages

If for some reason the domain cannot be applied, an error message will appear instead, directing you to try again. We recommend that you first use a free, online DNS record checker to review your branded sending domain and attempt to diagnose the issue. The following services provide this quick check:

- <https://dmarcian.com/dkim-inspector/>
- <https://www.whatsmydns.net/>
- <https://dnschecker.org/>

[Discover additional guidance and tips on branded sending domain troubleshooting](https://help.klaviyo.com/hc/en-us/articles/4417768780827).

If the problem cannot be resolved using one of the above tools, please contact our Support Team for further assistance. After you have set up your domain, when you return to the **Domains** page, you will see these changes in place. You will also see the date on which these changes took place and instructions on how to warm your sending infrastructure in the next 2 to 4 weeks.

## Warm your sending infrastructure

If you are a new, qualifying Klaviyo account starting on a branded sending domain or using a newly registered domain (registered within the last 30 days), it is essential to [warm your sending infrastructure](https://help.klaviyo.com/hc/en-us/articles/360025945671) in the first 2 to 4 weeks after setting up your branded sending domain. Warming your domain strengthens your sender reputation. Depending on what data you are bringing over to Klaviyo and the use cases you have, you will need to follow the [warming or platform introduction process](https://help.klaviyo.com/hc/en-us/articles/360025945671-How-to-warm-your-sending-infrastructure) applicable to you.

Existing Klaviyo customers moving to a branded sending domain do not have to warm infrastructure again, as long as you have:

- A domain that has been registered for at least 30 days AND
- You’ve used the domain to send email already (e.g., you used this domain in the past with a prior email service provider or with Klaviyo in your from address).

## Disconnected sending domain alert

Branded sending domains become disconnected when the required DNS records are removed. In these cases, Klaviyo will notify you so that you can fix the necessary DNS records.

You'll receive the alert in your notification inbox in Klaviyo.

![](https://klaviyo.zendesk.com/hc/article_attachments/35380098109339)

Only users with the necessary [permissions](https://help.klaviyo.com/hc/en-us/articles/115005231648) to configure a branded sending domain will receive the alert.

## Outcome

Once you configure your branded sending domains, all your emails (i.e., marketing and transactional emails) will be sent through your brand's domain rather than Klaviyo's shared sending domain.