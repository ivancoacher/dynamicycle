---
id: 360001550572
title: "How to set up dedicated click tracking"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360001550572-How-to-set-up-dedicated-click-tracking"
section: "Warm and ramp your domain"
category: "Deliverability & compliance"
category_slug: "deliverability-compliance"
klaviyo_updated: "2026-04-21T13:54:41Z"
language: en
---

## You will learn

Learn how to set up dedicated click tracking and best practices when doing so. Dedicated click tracking allows you to show your own domain on click tracking links rather than the default Klaviyo domain.

## What is dedicated click tracking?

Dedicated click tracking allows you to display your own domain on click tracking links as opposed to the default Klaviyo encoding. Any company is eligible for dedicated click tracking.

### Why set up dedicated click tracking?

Dedicated click tracking is beneficial because it allows your customers to further trust the emails that come from your brand as the links will be easily recognizable. Instead of a long string of letters and numbers from a Klaviyo encoded link, they will see your brand’s name when hovering over links in your email. This may increase the chances that they will click on your links.

Additionally, many mailbox providers and filtering software consider the reputation of all domains used in your messaging. Using the same root domain in both your dedicated click tracking links and your [sending domain](https://help.klaviyo.com/hc/en-us/articles/115000357752) creates alignment across your brand.

Dedicated click tracking is also a prerequisite for using [universal links and App Links in email messages](https://help.klaviyo.com/hc/en-us/articles/41701832186523).

## Set up dedicated click tracking

You can manually configure dedicated click tracking by adding new DNS records, or you can contact Klaviyo to enable it automatically if you’re using a dynamic branded sending domain.

### Automatically set up dedicated click tracking

If you have a [dynamic branded sending domain](https://help.klaviyo.com/hc/en-us/articles/115000357752) configuration in Klaviyo, you can [reach out to Klaviyo’s support team](https://help.klaviyo.com/hc/en-us/articles/115001002272) to have a click tracking domain with SSL enabled for your account. You can also have a dedicated click tracking domain setup on your behalf if you are on a static configuration with the CNAME record pointing to **klaviyodns.com**, as shown below.

You must be on a paid account for Klaviyo to set up a click tracking domain on your behalf.

Klaviyo will set the following click tracking domain for your brand:

- **trk.send.yourbrandeddomain.com**

For example, if the branded sending domain is **send.klaviyo.com**, the dedicated click tracking domain would be **trk.send.klaviyo.com**.

In this example, **send** is the branded sending domain's subdomain, but the click tracking domain will reflect your own selection for the subdomain.

It is not possible for Klaviyo to create a custom click tracking domain on your behalf and the click tracking domain will always match the example above.

### Manually set up dedicated click tracking

Setting up dedicated click tracking requires adding additional CNAME records to your DNS settings with your hosting provider. We provide the records below, which you add into your DNS provider.

Add the following CNAME record to set up your dedicated click tracking domain:

| Type | Hostname | Value |
| --- | --- | --- |
| CNAME | `trk` | dct.klaviyodns.com |

Depending on your DNS provider, the name of the `Hostname` and `Value` fields in the example above may differ. For example, some DNS providers may call it `Hostname` and others `Name`. However, the records you need to enter are the same.

Check out our links below to the [documentation for some popular DNS providers](#h_01HQ3KN3Y0V723N3RAD8DSMNC6) if you're having trouble.

If your DNS provider allows you to proxy records, you will see issues with the setup of dedicated click tracking in Klaviyo with this feature enabled. This commonly happens with Cloudflare but is possible with other DNS providers too. You’ll need to disable the proxying of your records for them to resolve over the internet, and so their presence can be verified.

After you've updated your DNS records, [reach out to Klaviyo support](https://help.klaviyo.com/hc/en-us/articles/115001002272) from the relevant account to validate your records.

## SSL for dedicated click tracking

SSL certificates are highly recommended for dedicated click tracking domains.

SSL is an encryption-based internet security protocol used to ensure privacy, authentication, and data integrity over internet communications. Provisioning SSL certificates allows your URLs to begin with HTTPS instead of the HTTP, and your click tracking domain to point to your own content delivery network (CDN). This indicates to users clicking on your links that the connection with the associated domain is secure, thus increasing customer trust and security.

Klaviyo will automatically generate an SSL certificate for your subdomain if a click tracking domain was set up on your behalf dynamically, or if you manually set up a click tracking domain pointing to the **klaviyodns.com** domain via the DNS update. For the latter method, If your domain has a [CAA record](#h_01JHG3R2YKC01NT85Z6ZTNGVAG) and does not have the necessary requirements, you must update it accordingly.

## CAA records

CAA (certification authority authorization) records are a type of DNS record that reduce the risk of unauthorized certificate generation. If your brand has a CAA record, the record must include the following properties:

| Type | Domain name | Value |
| --- | --- | --- |
| CAA | `example.com` | 0 issue pki.goog |

This allows Klaviyo to generate certificates for your subdomain. This is only relevant for the manual setup method where a new DNS record pointing to **klaviyodns.com** is added.

## Tips for where to update your DNS records

You can update your DNS records wherever you have registered or currently manage your domain names. However, not all domain registration services allow you to edit all DNS records. If you cannot update the records above, contact your DNS provider for information on how to update these records.

The process of adding records to your DNS depends on what domain provider you are using. Below are links to documentation for common providers:

- [GoDaddy](https://www.godaddy.com/help/manage-dns-680)
- [Google Domains](https://support.google.com/a/answer/48090?hl=en)
- [Cloudflare](https://support.cloudflare.com/hc/en-us/articles/200169046-How-do-I-add-a-CNAME-record-)
- [Name.com](https://www.name.com/support/articles/115004895548-Adding-a-CNAME-Record)
- [Hostgator](http://support.hostgator.com/articles/hosting-guide/lets-get-started/dns-name-servers/manage-dns-records-with-hostgatorenom)
- [Hover](https://help.hover.com/hc/en-us/articles/217282457-Managing-DNS-records-)
- [Namecheap](https://www.namecheap.com/support/knowledgebase/article.aspx/9214/31/email-authentication-tool-in-cpanel-spf-records)
- [Squarespace](https://support.squarespace.com/hc/en-us/articles/205812348-Opening-Advanced-DNS-settings)

## Disable click tracking for individual URLs

If you'd like to disable click tracking for a specific link, you can do so using the following HTML tag:

```
<a clicktracking=off href="https://example.com">Klaviyo Homepage</a>
```

## Additional resources

- [Guide to Klaviyo onsite tracking](https://help.klaviyo.com/hc/en-us/articles/115005076767)