<h1>How to verify email authentication configurations</h1>

## You will learn

Learn how to verify that your emails are being successfully authenticated using SPF, DKIM, and DMARC records.

[Google and Yahoo](https://www.klaviyo.com/blog/gmail-update) have announced new sender requirements that they are planning to start enforcing in February of 2024. For brands sending more than 5000 daily emails, setting up DMARC authentication will be a key requirement in order to successfully land in Gmail and Yahoo inboxes. [Microsoft Outlook](https://techcommunity.microsoft.com/blog/microsoftdefenderforoffice365blog/strengthening-email-ecosystem-outlook%E2%80%99s-new-requirements-for-high%E2%80%90volume-senders/4399730) will also start enforcing these requirements beginning May 2025.

## Email authentication

“Email authentication” refers to the technical standards that allow for the verification of an email sender's identity. The most commonly used email authentication standards are SPF, DKIM, and DMARC. Mail servers use these authentication protocols to verify that incoming emails are from legitimate senders, protecting your brand and your customers from malicious actors. In addition to preventing phishing and spoofing attempts, implementing these protocols can help improve deliverability, as mailbox providers will be able to confirm the identity of the sender.

Learn about [email authentication](https://help.klaviyo.com/hc/en-us/articles/4402601857307) and set up DMARC before getting started.

## Verify authentication using email headers

### About email headers

An email header contains metadata about an email and the network path it has taken. This includes information like from-address, subject line, recipient, and key authentication details.

You can use the authentication information found in the header of an email sent by your brand to verify that SPF, DKIM, and DMARC are passing.

Learn how to [get your full email header](https://help.klaviyo.com/hc/en-us/articles/360002117891) on different inbox providers.

### Header summary

Some inbox providers, like Gmail, may provide a summary of the key authentication information in the email header.

This may look something like this:

![Gmail header summary](https://klaviyo.zendesk.com/hc/article_attachments/28711702459035)

### Full header

Within the full email header, the key authentication information may look like this:

```
Delivered-To: email@klaviyo.com
Received: by 2002:a59:9a44:0:b0:437:660e:55f2 with SMTP id a4csp4934052vqp;
    Sun, 10 Dec 2023 16:03:01 -0800 (PST)
Authentication-Results: mx.google.com;
    dkim=pass header.i=@klaviyo.com header.s=s1 header.b=kBByyR4j;
    spf=pass (google.com: domain of
bounces+27486840-770f-email=klaviyo.com@send.klaviyo.com designates 000.000.00.000
as permitted sender)
smtp.mailfrom="bounces+27486840-770f-email=klaviyo.com@send.klaviyo.com";
    dmarc=pass (p=REJECT sp=REJECT dis=NONE) header.from=klaviyo.com
```

The email header you see may vary by inbox provider, but the key authentication information should live in the section called **Authentication-Results**.

### SPF

Sender Policy Framework (SPF) is an email authentication method designed to detect forged sender addresses during the delivery of the email. SPF allows the receiving mail server to verify that emails coming from a specific domain were sent through an IP address authorized by that domain's administrators.

If your inbox provider has a header summary, you should see SPF along with a pass or fail value and the IP address the email was sent through.

![SPF pass highlighed in header summary](https://klaviyo.zendesk.com/hc/article_attachments/28711731439131)

Within the full email header you can see the SPF record is passing (spf=pass), indicating that the IP address used to send the email (i.e., 000.000.00.000) is permitted to send for the send.klaviyo.com sending domain (i.e., the SPF domain).

```
Authentication-Results: mx.google.com;
     dkim=pass header.i=@klaviyo.com header.s=s1 header.b=kBByyR4j;
     spf=pass (google.com: domain of
     bounces+27486840-770f-email=klaviyo.com@send.klaviyo.com designates 000.000.00.000
as permitted sender)
smtp.mailfrom="bounces+27486840-770f-email=klaviyo.com@send.klaviyo.com";
     dmarc=pass (p=REJECT sp=REJECT dis=NONE) header.from=klaviyo.com
```

### DKIM

DomainKeys Identified Mail (DKIM) acts as a digital signature that is added to the header of an email to further verify the identity of the sender. Receiving email servers will verify that the DKIM signature matches that of the associated sending domain.

If your inbox provider has a header summary, you should see DKIM along with a pass or fail value for the domain the email was sent from.

![DKIM pass highlighed in header summary](https://klaviyo.zendesk.com/hc/article_attachments/28711702472603)

Within the full email header, you can see the DKIM record is passing (dkim=pass), indicating that the digital signature set by DKIM matches that of the associated sending domain.

```
Authentication-Results: mx.google.com;
     dkim=pass header.i=@klaviyo.com header.s=s1 header.b=kBByyR4j;
     spf=pass (google.com: domain of
bounces+27486840-770f-email=klaviyo.com@send.klaviyo.com designates 000.000.00.000
as permitted sender) smtp.mailfrom="bounces+27486840-770f-email=klaviyo.com@send.klaviyo.com";
     dmarc=pass (p=REJECT sp=REJECT dis=NONE) header.from=klaviyo.com
```

### DMARC

DMARC stands for domain-based message authentication, reporting, and conformance. It is a protocol that uses SPF and DKIM to determine the authenticity of an email, giving domain owners the ability to protect their domain from unauthorized use.

DMARC provides instructions to receiving servers about how to handle incoming mail. In order to get delivered, messages need to pass DKIM and SPF alignment checks according to the requirements set by the DMARC policy. Messages that do not pass DMARC checks can be allowed, rejected, or placed in the spam folder.

If your inbox provider has a header summary, you should see DMARC along with a pass or fail value.
![DMARC pass highlighted in header summary](https://klaviyo.zendesk.com/hc/article_attachments/28711702474779)

Within the full email header, you can see DMARC is passing (dmarc=pass), indicating that the email passed the sending domain’s DMARC check. Additionally, you can see the specific DMARC policy that is set on the sending domain (i.e., p=reject).

```
Authentication-Results: mx.google.com;
     dkim=pass header.i=@klaviyo.com header.s=s1 header.b=kBByyR4j;
     spf=pass (google.com: domain of
bounces+27486840-770f-email=klaviyo.com@send.klaviyo.com designates 000.000.00.000
as permitted sender) smtp.mailfrom="bounces+27486840-770f-email=klaviyo.com@send.klaviyo.com";
     dmarc=pass (p=REJECT sp=REJECT dis=NONE) header.from=klaviyo.com
```

## Verify authentication using 3rd party tools

Another way to verify that your DMARC policy has been published successfully is using a 3rd party tool like the DMARC checker offered by EasyDMARC. With this tool, you can simply enter you brand's root domain and the DMARC record will be returned if one is set.

![Example lookup on EasyDMARC for the klaviyo.com domain](https://klaviyo.zendesk.com/hc/article_attachments/28711702480155)

If your DMARC policy is set to **p=none,** the **Status** will appear as **Warning** when using EasyDMARC. **Warning** appears with the **p=none** policy because it does not protect your domain from spoofing, and allows emails to land in the recipient's main inbox even if there is a misalignment between the sending domain and friendly from-address domain. Both a status of **Warning**and **Valid** on EasyDMARC indicate that your brand's DMARC policy meets Gmail and Yahoo sender requirements.

You can disregard the **EasyDMARC Reporting** results unless you are using EasyDMARC's reporting services.

## Additional resources

[Understanding email authentication](https://help.klaviyo.com/hc/en-us/articles/4402601857307)

[How to setup a branded sending domain](https://help.klaviyo.com/hc/en-us/articles/115000357752)
