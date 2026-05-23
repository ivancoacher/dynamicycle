<h1>About BIMI</h1>

Learn how to display your brand’s logo in recipients’ inboxes next to your from address using Brand Indicators for Message Identification (BIMI). Implementing BIMI can increase brand recognition, legitimize your business, and boost deliverability by building trust with your recipients.

## What is BIMI?

BIMI uses your DNS settings to authenticate your visual brand identity in emails you send. This technology allows brands to control the logo used in inboxes when they send messages, in order to build trust and brand recognition. In addition, Gmail appends a blue check icon to senders who have completed verification. Gmail, Yahoo, and certain versions of Apple support BIMI. [See an up to date list of inboxes that support BIMI.](https://bimigroup.org/bimi-infographic/)

![An example of an email heading with a BIMI logo](https://klaviyo.zendesk.com/hc/article_attachments/28720772382875)

To add a brand logo in Outlook inboxes, use [Bing Pages](https://www.microsoft.com/en-us/bing/bing-pages-overview).

## Prepare your account for BIMI

[BIMI Group](https://bimigroup.org/) sets certain requirements to ensure BIMI is used appropriately and doesn’t mislead any recipients or allow a sender to impersonate another brand. In order to implement BIMI, your brand must take the following steps:

- In SVG (.svg) format
- Image is square, with a centered logo and no additional text
- Stored used HTTPS
- No larger than 32 kb

- [Implement SPF, DKIM, and DMARC.](https://help.klaviyo.com/hc/en-us/articles/4402601857307-Understanding-DMARC) Your DMARC policy must be set to p=quarantine OR p=reject.
- Prepare your logo image, ensuring it meets [BIMI Group’s logo criteria](https://bimigroup.org/creating-bimi-svg-logo-files/), including the following:
- Trademark your logo and obtain a [Verified Mark Certificate](https://support.google.com/a/answer/10911028?hl=en) (required when sending to Gmail addresses)

## Implement BIMI

Once you’ve completed all the prerequisites, follow the [BIMI implementation steps provided by Validity](https://help.returnpath.com/hc/en-us/articles/360029588491-How-to-implement-Brand-Indicators-for-Message-Identification-BIMI-on-my-emails). Note that Klaviyo has no direct control over the issuance of VMCs or implementation of BIMI. If you have questions or concerns about implementing BIMI, [refer to BIMI Group's FAQs](https://bimigroup.org/faqs-for-senders-esps/).

BIMI is only supported by [certain inboxes](https://bimigroup.org/bimi-infographic/). Implementing BIMI will not impact how your message appears to recipients using non-supported inboxes.
