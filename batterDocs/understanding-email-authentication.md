<h1>Understanding email authentication</h1>

## You will learn

Learn about email authentication protocols that are used to build your sender reputation, validate emails are coming from a legitimate sender, and protect against email abuse.

[Google and Yahoo](https://www.klaviyo.com/blog/gmail-update) have announced new sender requirements that they are planning to start enforcing in February of 2024. For brands sending more than 5000 daily emails, setting up DMARC authentication will be a key requirement in order to successfully land in Gmail and Yahoo inboxes. [Microsoft Outlook](https://techcommunity.microsoft.com/blog/microsoftdefenderforoffice365blog/strengthening-email-ecosystem-outlook%E2%80%99s-new-requirements-for-high%E2%80%90volume-senders/4399730) will also start enforcing these requirements beginning May 2025.

## About email authentication

“Email authentication” refers to the technical standards that allow for the verification of an email sender's identity. The most commonly used email authentication standards are SPF, DKIM, and DMARC. Mail servers use these authentication protocols to verify that incoming emails are from legitimate senders, protecting your brand and your customers from malicious actors. In addition to preventing phishing and spoofing attempts, implementing these protocols can help improve deliverability, as mailbox providers will be able to confirm the identity of the sender.

## SPF

Sender Policy Framework (SPF) is an email authentication method designed to detect forged sender addresses during the delivery of the email. SPF allows the receiving mail server to verify that emails coming from a specific domain were sent through an IP address authorized by that domain's administrators.

When an email is sent from an IP address that has not been allowed through SPF, the receiving mail server may reject the email, or divert it away from the primary inbox. Without SPF records you could not authenticate IPs using your sending domain, allowing malicious actors to easily impersonate your brand.

On Klaviyo's shared sending domain, emails are automatically authenticated through SPF. If you are using your own [branded sending domain](https://help.klaviyo.com/hc/en-us/articles/115000357752) in Klaviyo, the necessary SPF record is automatically added through the CNAME or NS records added during setup.

## DKIM

DomainKeys Identified Mail (DKIM) acts as a digital signature that is added to the header of an email to further verify the identity of the sender. Receiving email servers will verify that the DKIM signature matches that of the associated sending domain. Since the DKIM signature exists in the header of an email, it will also remain when an email is forwarded, unlike SPF authentication.

On Klaviyo's shared sending domain, emails are automatically authenticated through DKIM. If you are using your own [branded sending domain](https://help.klaviyo.com/hc/en-us/articles/115000357752) in Klaviyo, the necessary DKIM record is automatically added through the CNAME or NS records added during setup.

## DMARC

DMARC stands for domain-based message authentication, reporting, and conformance. It is a protocol that uses SPF and DKIM to determine the authenticity of an email, giving domain owners the ability to protect their domain from unauthorized use.

![](https://fast.wistia.com/embed/medias/1xamzihlg0/swatch)

DMARC provides instructions to receiving servers about how to handle incoming mail. In order to get delivered, messages need to pass DKIM and SPF alignment checks according to the requirements set by the DMARC policy. Messages that do not pass DMARC checks can be allowed, rejected, or placed in the spam folder.

Implementing a DMARC policy on your domain can help protect you from spoofing, limiting your brand’s and recipients' exposure to potentially fraudulent and harmful messages.

****Example DMARC policy****

DMARC is an email authentication, policy, and reporting protocol that impacts any email sending from your brand, beyond just Klaviyo. Please note that it is important to work with your IT team or a 3rd party professional to implement a DMARC policy that best suits your brand’s needs.

Below is an example of what a simple DMARC record may look like, and how different records impact email delivery.

`v=DMARC1; p=none; rua=mailto:dmarc-reports@yourbrand.com`

It is common for the **sp** tag to be omitted in a DMARC record, in which case the **sp** tag defaults to the value of the **p** tag.

While DMARC policies can have a number of tags with different functions, the **p** and **sp** policy tags are the most important when it comes to Klaviyo and your email marketing.

The values of these two tags tell the inbox providers how they should react when the alignment checks fail. When used in from-email addresses, the **p** tag applies to the root domain (e.g., **@yourbrand.com**) while the **sp** tag applies to the [subdomains](https://help.klaviyo.com/hc/en-us/articles/360055457791) (e.g.,**@shop.yourbrand.com**).

Meanwhile, the **rua** tag in the example determines the inbox DMARC reports will be mailed to. This tag is recommended, but not required.

Make sure to swap out the placeholder email address above (i.e., [**dmarc-reports@yourbrand.com**](mailto:dmarc-reports@yourbrand.com)) with an inbox that is prepared to receive DMARC reports if you plan to use the **rua** tag.

|  |  |
| --- | --- |
| ****Value for p/sp tag**** | ****What inbox providers do with misaligned email**** |
| p=none | Accept email normally, despite the misalignment. |
| p=quarantine | Accept the email but display a warning and place the email in spam. |
| p=reject | Block the misaligned email. |

A DMARC policy is placed as a TXT record on a domain's DNS control panel, but needs to follow specific syntax rules.

### How **p** and **sp** tags impact sending on Klaviyo

When sending on a shared sending domain, emails will always have a misalignment between your from-address (e.g., **marketing@yourbrand.com**) and the actual sending domain of the email (e.g., **ksdn.klaviyomail.com**). Klaviyo’s own shared sending domain has a DMARC policy set to **p=none**, so that your emails can land in customer inboxes despite the misalignment.

When you make use of a branded sending domain, a domain owned by your brand, the from-address domain aligns with the sending domain. As a result, DMARC checks will pass.

### **rua** tags and DMARC reporting

The **rua** tag in a DMARC record allows for the associated email address to receive DMARC reports in .xml format. These reports are difficult and tedious to interpret, so Klaviyo recommends working with a DMARC service provider if you plan to use the **rua** tag for DMARC reporting. These providers help to process the .xml DMARC reports, and present them so your brand can more easily gather insights.

The domain of the email address set in the **rua** tag to receive DMARC reports must match the root domain of the DMARC record. To receive DMARC reports through a different domain, you'll need to add a TXT record provided by the domain owner to your brand's root domain.

****Example DMARC report****

[“Example](https://www.napkin.io/api/embed/7121123fc84f4509)

Some examples of DMARC providers Klaviyo recommends are:

- [Valimail](https://www.valimail.com/google-and-yahoo-compliance-check/?utm_source=klaviyo&utm_medium=partner%20generated)
- [EasyDMARC](https://easydmarc.com/)
- [Dmarcian](https://dmarcian.com/)

## Configuring email authentication

When sending emails with Klaviyo, you do not need to add your own SPF and DKIM records. If you are sending on Klaviyo’s shared sending domain, the necessary records have already been set to pass authentication. With a branded sending domain (also known as a dedicated sending domain), the Klaviyo NS or CNAME records added during setup automatically enable DKIM and SPF authentication.

However, setting up DMARC is an external process performed outside of Klaviyo with your DNS provider. The DMARC policy you set determines how to handle messages that fail SPF and DKIM authentication. DMARC policies can either quarantine unauthenticated emails and send them to the recipient's spam folder, allow them to land in inboxes despite the misalignment, or reject them entirely and block the delivery to the recipient.

If your brand currently does not have a DMARC policy, configuring **p=none** is a great first step to fulfill [Gmail and Yahoo’s requirements](https://www.klaviyo.com/blog/gmail-update). However, Klaviyo highly recommends working with your IT team or a 3rd party professional if you’d like to configure a stricter DMARC policy that prevents spoofing and allows for reporting about alignment failures.

Klaviyo cannot implement DMARC on your behalf because the process impacts your brand’s security and sending outside of Klaviyo. Additionally, implementing DMARC requires access to and control over your brand’s DNS settings. Klaviyo cannot make such DNS changes for your brand in order to protect your security and ownership over your domain.

## Setting up DMARC in your DNS

Setting up DMARC is a process performed outside of Klaviyo in your DNS provider. There are a large number of different DNS providers, but the steps below describe how DMARC is generally implemented.

To set up DMARC, your network administrator for the domain will need to log into the domain’s DNS settings to add a DMARC record, like the one shown below. Once logged in to your DNS provider, create a new record with the following information.

- ****Type****: TXT
- ****Host****: \_dmarc
- ****Value****: v=DMARC1; p=none

  The **rua** tag is an optional tag that used for DMARC reporting. If plan to use the reports and would like to receive them to an inbox, the DMARC record value is: `v=DMARC1; p=none; rua=mailto:email@yourbrand.com`

  The names of fields, interfaces, and processes to create a new record can vary across DNS providers. Some examples of DNS providers include GoDaddy and Namecheap, but there are many others.

  For further instructions on how to set up DMARC for your domain, we recommend the following resources and services, or reaching out to your DNS provider.
- [Understand how DMARC protects your domain reputation](https://academy.klaviyo.com/understand-how-dmarc-protects-your-domain-reputation/1832471)
- [MXToolBox: How to setup DMARC](https://mxtoolbox.com/dmarc/details/how-to-setup-dmarc)
- [DMARCian: Getting started with DMARC](https://dmarcian.com/getting-started-with-dmarc/)
- [Valimail](https://www.valimail.com/)

## Making your Klaviyo emails DMARC compliant

In order to be DMARC compliant, you need to connect a branded sending domain to your account that matches the root domain in your friendly-from email address (i.e., your from-address). For example, if you send an email using **sales@yourbrand.com** as the from-address and **yourbrand.com** is protected by DMARC, your account will need to use a branded sending domain like **send.yourbrand.com** to meet DMARC requirements.

Learn how to [update your sender email address](https://help.klaviyo.com/hc/en-us/articles/360024994912) to align it with your branded sending domain.

### Internal recipients

When using a shared domain to send emails to internal recipients, inbox providers may display a warning message and place emails in spam when the recipient's email address matches the from address domain.

For example, on Gmail:

![gmailwarningjpg.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28713383110683)

While this only impacts users with email addresses that match your own from address domain, you can set up a branded sending domain to prevent this.

If you are seeing this warning for a personal, non-enterprise inbox, it is likely the result of DMARC failing. In order to be DMARC compliant, you need to connect a branded sending domain to your account that matches the domain in your sender email address (i.e. your from-address).

## Verifying your email authentication configuration

To verify that the record has been published successfully, you can input your domain into the DMARC checker offered by [EasyDMARC](https://easydmarc.com/tools/dmarc-lookup). With this tool, a status of **Warning** or **Valid** is compliant with Gmail and Yahoo’s sender requirements.

![easydmarcklaviyo.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28713383120027)

Alternatively, you can verify that your email authentication is setup correctly using the header of an email sent by your brand.

An email header contains metadata about an email and the network path it has taken. This includes information like from-address, subject line, recipient, and key authentication details such as whether SPF, DKIM, and DMARC are passing.

Learn how to [verify email authentication configurations using email headers.](https://help.klaviyo.com/hc/en-us/articles/21330028699419)

![Header summary in Gmail](https://klaviyo.zendesk.com/hc/article_attachments/28713338438811)

## Moving to a more secure DMARC policy

While a DMARC policy of **p=none** is enough to meet initial sender requirements set in place by Gmail and Yahoo, moving to a more secure policy can better protect your business from malicious actors.

### Benefits of more secure policies

The main benefit of using **p=quarantine** or **p=reject** is that they will prevent misaligned emails (i.e., emails sent from a sending domain that does not match your brand’s root domain) from landing in a recipient's main inbox. **P=none** does not impact inbox placement in cases where an email is sent from a misaligned domain, so recipients can still receive emails from a malicious actor trying to impersonate your brand. If a user ends up viewing a spoofed email that appears to have been sent from your brand, this can cause strain on the trust a customer has in your brand’s email.

Meanwhile, when using a policy of **p=quarantine** or **p=reject**, misaligned emails will be blocked or sent to the spam folder for recipients. Inbox providers will know to avoid showing the email to the recipient, and spoofed emails will not make it to the primary inbox.

### Other considerations

It is important to note that DMARC applies to any email sent from your brand, including those sent outside of Klaviyo. With a policy of **p=none**, your sends will not be impacted as emails will still land in the primary inbox. However, the stricter DMARC policies can cause emails to not get delivered if your domains aren’t aligned across your business’s entire email sending infrastructure and use cases.

For this reason, Klaviyo recommends working with your IT team or a DMARC service provider to implement a policy that best fits the needs of your brand.
