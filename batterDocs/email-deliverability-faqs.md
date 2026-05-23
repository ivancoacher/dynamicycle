<h1>Email deliverability FAQs</h1>

Get answers to frequently asked questions around email deliverability, including how they are placed in inboxes, about bounces, and more.

## Inbox placement

### Is there any way to know where an email lands (spam or junk folders/regular inbox/promotions tab in Gmail, etc) when it gets sent?

Klaviyo can confirm whether an email was delivered to the recipient’s inbox, but not where in the inbox it landed. Remember, the spam folder is still considered to be part of an inbox. Klaviyo is responsible for sending your emails, but once these emails are in the hands of the inbox provider (i.e. Gmail or Yahoo), the messages are filtered according to each provider’s rules. All inbox providers have a built-in system that scans incoming emails, and automatically sorts them using complex algorithms that are not made public.

### Do URLs that direct to a thirrd-party site impact deliverability?

3rd-party URLs in emails can impact inbox placement if inbox providers determine the links are suspicious or malicious. Factors like the reputation of the 3rd-party’s domain, and relevance to the content of the email can impact how inbox providers view emails with these URLs.

Note that Klaviyo’s [acceptable use policy](https://www.klaviyo.com/legal/acceptable-use-policy) does not allow for affiliate marketing.

### Why are emails to my internal team getting blocked?

If you are sending on Klaviyo’s shared sending domain and emails to internal team members are being blocked, you may have an internal filtering setup that is blocking the emails due to the From Address and sending domain misalignment. Inbox providers may view this as a spoofing attempt, and block the email to protect your brand.

If you are seeing this issue, [set up a branded sending domain](https://help.klaviyo.com/hc/en-us/articles/115000357752) (also known as a dedicated sending domain). If you are already on a branded sending domain and emails are still getting blocked, work with your IT team to allow-list your branded sending domain on your filtering software.

## Blocklists

### What blocklists have the most impact on Klaviyo’s deliverability and deliverability with different inbox service providers?

Blocklists can have different deliverability impacts based on the particular ISP. Gmail for example does not rely on blocklists, and uses Google’s own systems to evaluate sender reputation. However, other inbox providers may consider SpamHaus, as well as SORBS and SpamCop to a lesser extent. Any other blocklists are not relied upon by major ISPs and will have little to no impact on deliverability.

Klaviyo closely monitors SpamHaus listings as this is the blocklist that can have the most impact on deliverability. SORBs and SpamCop are also monitored but have much lower impact. Other blocklists are minor and do not have a measurable impact on deliverability.

## Open rates

### Why are the open rates on my account low?

Open rates allow you to measure customer engagement and monitor your deliverability and performance. If you are seeing low open rates, take the appropriate steps to improve your open rates in [campaigns](https://help.klaviyo.com/hc/en-us/articles/360042454031) or [flows](https://help.klaviyo.com/hc/en-us/articles/360058346111). In general, suppression of profiles that have Never Engaged is the best first step to addressing low open rates. Klaviyo makes it easy to [create a Never Engaged segment](https://help.klaviyo.com/hc/en-us/articles/115005078347) through the Deliverability Hub.

### Why did the open rates for a specific domain drop?

If you notice that your open rates only suffer for customers using a specific inbox provider or email domain, you can take steps to [improve your sender reputation for this group](https://help.klaviyo.com/hc/en-us/articles/115005250368). You can exclude low-performing email addresses from your sending lists, and isolate engaged subscribers from the low-performing domain with a segment.

## Compliance

### My account was disabled by compliance, what can I do?

To protect all our customers, Klaviyo has [anti-abuse measures](https://help.klaviyo.com/hc/en-us/articles/115000308972) in place and monitors campaign sends. Klaviyo will notify senders if their campaign performance suggests suspicious activity, and if there are continuous patterns that suggest potential abuse of the Klaviyo platform, the account may disabled.

Your account may also be temporarily disabled after being flagged by our verification and compliance team. This typically occurs when a new account attempts to send to an uploaded list of contacts for the first time.

For more information about the account review process, see our guide about the [account verification check](https://help.klaviyo.com/hc/en-us/articles/115000628331) or reach out to [Klaviyo’s support team](https://help.klaviyo.com/hc/en-us/articles/115001002272).

### What is a suspicious email address and how do I remove that flag?

When an email address [hard bounces](https://help.klaviyo.com/hc/en-us/articles/115005250408) at least once across the Klaviyo infrastructure, it is marked as suspicious. This means that even if they have not hard bounced in your account, they have previously hard bounced in another Klaviyo user's account.

Suspicious emails are automatically skipped from receiving emails. This is done in an effort to preserve your sending reputation, as well as the sending reputation of other Klaviyo customers since sending to invalid addresses can negatively impact both IP and domain reputation.

If you believe that a profile or profiles have been marked suspicious in error, please reach out to Klaviyo’s [support team](https://help.klaviyo.com/hc/en-us/articles/115001002272), and provide us with evidence of the email address still being valid. Make sure to include a screenshot of an email you received from the profile in question.

Please make sure that this screenshot clearly shows the following:

- The email address that has been marked suspicious.
- The timestamp of the email address being delivered on a date after the profile was marked suspicious.

### Can I remove the Reply-To email entirely or set up a way where recipients cannot respond to the email?

You cannot remove the Reply-To email in an email campaign. If you don’t want to receive replies, Klaviyo recommends that you set up a separate email that you do not monitor (i.e., [no-reply@domain.com](mailto:no-reply@domain.com)) and use it for your Reply-to email.

### Is cross-brand consent collection allowed on Klaviyo?

You can collect cross-brand consent (i.e for brand collaboration giveaways) as long as the language on the signup form explicitly and clearly states the brands that the visitor will be subscribing to, this is allowed. Here is an example of what such a signup form would look like:

![Example of form collecting consent for multiple brands](https://klaviyo.zendesk.com/hc/article_attachments/28717880716059)

If a customer consents to receive emails from another brand through your form, that brand can [upload the consented customers](https://help.klaviyo.com/hc/en-us/articles/115005251128) to their own lists and include them in sends.

## Transactional emails

### Can campaigns be marked as transactional?

Campaigns cannot be marked as transactional, as transactional emails must be sent in response to an action the customer took. If you need to send a one-time email campaign that contains transactional content, you can create a [list](https://help.klaviyo.com/hc/en-us/articles/360003031652) or [segment](https://help.klaviyo.com/hc/en-us/articles/360003040052) triggered flow to achieve this and [back-populate](https://help.klaviyo.com/hc/en-us/articles/360049924272) it.

## Bounced/blocked emails

### My sends have consistently been getting good open rates, but recently one of my campaigns had a high bounce rate. Why would this be happening?

If the impacted campaign has a much larger recipient count compared to your previous campaign sends, ISPs may be blocking the email because they see spikes in send volume as a red flag.

Additionally, check if there has been an elevated amount of unsubscribes and spam complaints. If there has been an increase in either one of these categories:

- [Clean your sending lists](https://help.klaviyo.com/hc/en-us/articles/115005078347)
- Implement [double opt-in](https://help.klaviyo.com/hc/en-us/articles/115005251108)
- Send to [engaged recipients](https://help.klaviyo.com/hc/en-us/articles/115000200072)

In general, suppression of profiles that have never engaged is the best first step to addressing a high bounce rate for recent campaigns. Klaviyo makes it easy to [create a Never Engaged segment](https://help.klaviyo.com/hc/en-us/articles/115005078347) through the Deliverability Hub.

### Do bounces affect deliverability?

A [hard bounce](https://help.klaviyo.com/hc/en-us/articles/115005250408) occurs when an email cannot be delivered due to a permanent reason, such as an email address being invalid. Hard bounces can negatively impact deliverability and your sender reputation in the eyes of inbox providers. Klaviyo automatically suppresses any email address that hard bounces.

A [soft bounce](https://help.klaviyo.com/hc/en-us/articles/115005250408) is always caused by a temporary reason, such as when a recipient's inbox is full or when their email server is momentarily down. Soft bounces have less of an impact on deliverability as they are generally out of the senders’ control.

### What are MM3 sends and why aren't my emails being delivered to some domains?

MM3 messages are emails that result in communications with a cellular device (e.g., pagers and cell phones) in a non-email fashion such as a received text message.

The United States FCC maintains a do not email domain list [here](https://www.fcc.gov/consumer-governmental-affairs/about-bureau/consumer-policy-division/can-spam/domain-name-downloads). All domains listed on this FCC page are expected to result in some form of electronic communication with the end recipient being a cellular phone device or pager. Unsolicited marketing communications to these device types are expressly prohibited and Klaviyo will block sends to these domains.

## Dedicated IPs

### What Klaviyo accounts qualify for a dedicated IP address?

Not all accounts qualify for a dedicated IP address. To learn if your account qualifies for a [dedicated IP](https://help.klaviyo.com/hc/en-us/articles/7675517826587) and more details about the warming process, please reach out to your Customer Success Manager for more information.

### Can more than one Klaviyo account share a dedicated IP address?

Multiple related Klaviyo accounts can all share and send from the same dedicated IP.

Note that the Klaviyo accounts sharing an IP address must be related (co-owned or under the same parent company) to each other. Different brands or unrelated accounts are not able to share a dedicated IP address in Klaviyo.

### Does Klaviyo offer dedicated IP addresses for transactional emails?

If your account qualifies for a dedicated IP address, Klaviyo offers dedicated transactional IP addresses for transactional emails as well.

### How can I view my dedicated IP addresses in Klaviyo?

If your account has one or more dedicated IPs, you can view them by navigating to Settings > Email > IP addresses. This tab only appears for accounts with dedicated IPs.

On this page, you can see each IP's address, email type (Marketing or Transactional), and current status (Warming, Active, or Inactive). If an IP is currently warming, click Review to view estimated warming progress.

## Dedicated sending domains

### Is it possible to send double opt-in emails from my branded sending domain?

Once you set up a branded sending domain on your Klaviyo account, your double opt-in emails will be sent from your branded sending domain.

### Can a domain be used with multiple different Klaviyo accounts? Does the new account need to warm up the domain again?

A branded sending domain can be shared by multiple Klaviyo accounts. If the domain has already been warmed, the new Klaviyo account does not need to warm up the domain again. However, it is important to note that the performance of all the Klaviyo accounts will impact the reputation of the branded sending domain.

### Can a single Klaviyo account have multiple branded sending domains?

A single account can only have one branded sending domain.

### Can I change my branded sending domain?

You can change your branded sending domain by adding Klaviyo’s CNAME records into the new domain’s DNS, and removing the existing branded sending domain from your account. After the new domain is applied to the account, you’ll need to go through [warming](https://help.klaviyo.com/hc/en-us/articles/360025945671) again.

Note that changing your branded sending domain due to deliverability concerns will not resolve them. If you are seeing deliverability issues on your branded sending domain, you should follow best practices to [improve your sender reputation](https://help.klaviyo.com/hc/en-us/articles/8983758025883)

### Will adding in Klaviyo’s CNAME and TXT record impact sending on other email service providers?

As long as the subdomain created for Klaviyo is different from the other ESP’s sending subdomain, then there would be no conflict. Klaviyo’s CNAME is mainly aimed towards Klaviyo to make use of the subdomain, and would not interfere with any sending on other ESPs.

## Click tracking domains

### My links are being blocked by uBlock Origin. What can I do about this?

If your account is using Klaviyo’s shared click tracking domain and you are seeing links being blocked, you should [set up dedicated click tracking](https://help.klaviyo.com/hc/en-us/articles/7676795223707).

## Warming

### How long does it take to warm up a branded sending domain?

Warming should be a minimum of 30 days with good performance to thoroughly warm your domain. Once you are seeing consistent open rates with a significant volume for a few weeks, you can begin to widen your sending practices (e.g., higher volume win-backs, etc.)

In general, suppression of profiles that have never engaged is the best first step to warming up your branded sending domain's reputation. If any deliverability issues come up associated with your domain then Klaviyo makes it easy to address this by [creating a Never Engaged segment](https://help.klaviyo.com/hc/en-us/articles/115005078347) through the Deliverability Hub.

### If I decide to pause sending, what is the maximum amount of time that a domain can go without sending and not having to re-warm?

Sending reputation during warming is heavily based on consistency between both sending volume and customer engagement. If you are trying to slow down sending, Klaviyo recommends using a more strict segment with fewer profiles instead of stopping overall.

However, if you stop sending campaigns entirely, you will need to rewarm the domain.

### Do new click tracking domains need to be warmed?

[Dedicated click tracking domains](https://help.klaviyo.com/hc/en-us/articles/7676795223707) do not have to be warmed.

## Email authentication

### What are SPF, DKIM, and DMARC records?

****SPF****

Sender Policy Framework (SPF) is an email authentication method designed to detect forged sender addresses during the delivery of the email. SPF allows the receiving mail server to verify that emails coming from a specific domain were sent through an IP address authorized by that domain's administrators.

When an email is sent from an IP address that has not been allowed through SPF, the receiving mail server may reject the email, or divert it away from the primary inbox. Without SPF records you could not authenticate IPs using your sending domain, allowing malicious actors to easily impersonate your brand.

****DKIM****

DomainKeys Identified Mail (DKIM) acts as a digital signature that is added to the header of an email to further verify the identity of the sender. Receiving email servers will verify that the DKIM signature matches that of the associated sending domain. Since the DKIM signature exists in the header of an email, it will also remain when an email is forwarded, unlike SPF authentication.

****DMARC****

DMARC stands for domain-based message authentication, reporting, and conformance. It is a protocol that uses SPF and DKIM to determine the authenticity of an email, giving domain owners the ability to protect their domain from unauthorized use.

DMARC provides instructions to receiving servers about how to handle incoming mail. In order to get delivered, messages need to pass DKIM and SPF alignment checks according to the requirements set by the DMARC policy. Messages that do not pass DMARC checks can be rejected, reported back to the domain owner, or placed in the spam folder.

Implementing a DMARC policy on your domain can help protect you from spoofing, limiting your brand’s and recipients' exposure to potentially fraudulent and harmful messages.

Learn more about [email authentication](https://help.klaviyo.com/hc/en-us/articles/4402601857307).

### What are Klaviyo’s SPF & DKIM records and how can I add them?

If your account is on a [shared sending domain](https://help.klaviyo.com/hc/en-us/articles/7674941873947), these records wouldn’t be necessary as your domain is not used for sending the email. The email is sent from a **klaviyomail.com** sending domain which already has the necessary SPF and DKIM records in place.

If your account is on a [branded sending domain](https://help.klaviyo.com/hc/en-us/articles/115000357752), the SPF and DKIM records are added automatically during setup through the CNAME records.

### What does misalignment mean?

Misalignment refers to the mismatch between the sending domain for your outgoing messages and your sender email address domain (i.e. your From Address). For example, if you send an email from **sales@example.com** and you are using Klaviyo’s shared sending domain of **klaviyomail.com,** these domains would be misaligned.

In this example, if **example.com** is protected by DMARC, your account will need to use a [branded sending domain](https://help.klaviyo.com/hc/en-us/articles/115000357752) like **send.example.com** to meet DMARC requirements.

### How does DMARC impact inbox placement?

The placement of your email in an inbox depends on the p-value of your domain’s DMARC policy.

The values are:

- p = none: even if emails fail SPF/DKIM, emails will still get placed into the inbox
- p = quarantine: if email fails either SPF/DKIM, it will be placed into the spam folder
- p = reject: if emails fail either SPF/DKIM, it will get blocked (never reaching the inbox or spam)

You cannot manage your domain’s DMARC policy through Klaviyo. Work with your IT team to implement DMARC or make changes to your domain’s DMARC policy.

## Gmail/G-Suite specific issues

### Why is Gmail showing a suspicious link warning on my emails?

This is often seen by poor senders that have a history of low open rates when their engagement starts to improve. Gmail is still suspicious of the emails being sent, but not enough to flag it as spam. Although the sender is doing the right thing to improve their deliverability, Google is uncertain about that on their end on whether the sender is taking the right steps for the right reason or if they are trying to game the system.

Other reasons can include a lack of of email authentication, or a suspicious link underneath the Klaviyo wrapper.

![Suspicous link warning in Gmail](https://klaviyo.zendesk.com/hc/article_attachments/28717853214875)

### Why is Gmail flagging my emails with a “Be careful with this message” banner?

Gmail can display this banner when using a shared sending domain to send emails to internal recipients, and the recipient's email address matches the From Address domain. While this only impacts users with email addresses that match your From Address, you can set up a [branded sending domain](https://help.klaviyo.com/hc/en-us/articles/115000357752) to prevent this.

If you are seeing this warning for a personal, non-enterprise inbox, it is likely the result of [DMARC](https://help.klaviyo.com/hc/en-us/articles/4402601857307) failing. In order to be DMARC compliant, you need to connect a branded sending domain to your account that matches the domain in your sender email address (i.e. your From Address).

![Gmail warning notifying user to be careful with message](https://klaviyo.zendesk.com/hc/article_attachments/28717880720667)

## Other common deliverability questions

### What is sender reputation?

Sender reputation refers to the trustworthiness of your brand as an email sender. It is most often associated with your branded sending domain. Inbox providers determine your sender reputation based on your sending practices, and consider this when sorting emails in a recipient’s inbox. Senders with a positive sender reputation are more likely to have their emails delivered into customers’ main inbox, while senders with a poor sender reputation are likely to see their emails placed into spam or worse, not delivered at all.

Any domain (e.g., From Address domain, branded sending domain, click tracking domain, etc.) and IP address you use for your email marketing has its own reputation that inbox providers consider when determining your overall sender reputation. It is important to maintain a good sender reputation on the domains and IP address to have strong email deliverability.

### How do IPs get blocked due to list bombing?

When Klaviyo sees a large number of form submissions within a certain amount of time coming in from a specific IP, it may be blocked to prevent [list bombing](https://help.klaviyo.com/hc/en-us/articles/9890182538011). List bombing is a malicious attack where the attacker exploits a signup form or checkout page by making a large number of fake submissions, filling the associated list with emails and phone numbers that have not consented or are invalid.

If you are seeing issues with form submissions coming from a specific IP address, reach out to Klaviyo’s [support team](https://help.klaviyo.com/hc/en-us/articles/115001002272).

### How long are double opt-in emails valid for after they’ve been sent?

Double opt-in emails are valid for 30 days after they have been sent. Customers will need to subscribe again if they would like to be added to your list and the 30 day window has elapsed.

### What are the key metrics that impact my deliverability?

Monitoring your deliverability performance is important to help mitigate potential deliverability issues and effectively reach your audience. The key deliverability metrics that impact your sender reputation and should be monitored are:

- ****Unique open rates****
  The number of individuals opening your email divided by the number of emails delivered (as opposed to total opens, which measures the total number of times emails are opened).
- ****Unique click rates****
  The number of individuals clicking a link in your email divided by the number of emails delivered.
- ****Bounce rates****
  The number of bounced addresses divided by the total number of emails sent.
- ****Unsubscribe rates****
  The number of recipients who unsubscribe divided by the total number of emails delivered. These rates are measured on a per campaign basis, or you can view the list growth report for a particular list.
- ****Spam complaint rates****
  The number of spam complaints about a particular email divided by the total number of emails delivered.

See our guide on [email deliverability monitoring and performance metrics](https://help.klaviyo.com/hc/en-us/articles/115000201131) for information on how to track your performance across these metrics in Klaviyo.

## Gmail and Yahoo sender requirements

### What are Gmail's and Yahoo's requirements for senders?

Beginning in February 2024, Gmail and Yahoo plan to start enforcing a set of requirements for senders. These requirements have long been recommended by inbox providers as best practices, but will now be requirements to successfully land in Gmail and Yahoo inboxes. These requirements are:

- ****Remove Gmail or Yahoo from your from-address.****
  Don’t use Gmail or Yahoo email addresses in your from-address address. If you are using **@gmail.com** or **@yahoo** in your sender email, switch over to a domain you own.
- ****Setup a branded sending domain****
  A branded sending domain allows you to send emails that appear to be coming from your brand and allows you to have better overall control of your sender reputation. If you are a bulk sender (i.e., you send to more than 5000 emails per day to Gmail recipients), learn how to setup a [branded sending domain.](https://help.klaviyo.com/hc/en-us/articles/115000357752)
- ****Setup a DMARC policy on your root domain****
  [‍DMARC authentication](https://help.klaviyo.com/hc/en-us/articles/4402601857307) is a protocol policy that servers use to make sure emails are coming from a legitimate sender. DMARC policies are good practice because they protect the sending domain from unauthorized use by bad actors, but are now a requirement for those using a branded sending domain to send to Gmail and Yahoo recipients.
- ****Align your from-address with your branded sending domain****
  The domain in your from-address must align with the root domain in your branded sending domain to pass DMARC authentication.
- ****Make it easy to unsubscribe****
  Gmail and Yahoo's sender requirements include that every email must include a one-click unsubscribe link. To help meet this new requirement, Klaviyo will automatically add a one-click unsubscribe link to the header of every email.
- ****Keep spam complaints low****
  Low spam complaints are a key way to show inbox providers that you are a legitimate sender who follows deliverability best practices. Gmail advises senders to stay under a 0.1% spam complaint threshold, and exceeding a spam complaint rate of 0.3% may result in blocked sends. Visit the [deliverability hub](https://help.klaviyo.com/hc/en-us/articles/18378819907995) in Klaviyo to view your deliverability metrics, or try [Google Postmaster Tools](https://academy.klaviyo.com/use-google-postmaster-tools-to-monitor-your-spam-complaint-rate/1838637) to monitor how your sending strategy aligns with Google's requirements.

Learn more about [Gmail and Yahoo's sender requirements](https://academy.klaviyo.com/2024-new-sender-requirements-checklist/1817230) and how to satisfy each requirement.

### Who is considered a bulk sender?

Some of Google's new sender requirements only apply to bulk senders, or those who send 5000 or more emails to Google accounts per day.

If you’re not sure if you meet the bulk sender threshold, consider that:

- Google will include personal accounts ending in **@gmail.com** and **@googlemail.com**.
- All traffic from a given sender will count towards the bulk sender threshold, including transactional emails.

There are 3 main requirements that you’ll need to satisfy if you meet the bulk sender threshold:

1. Set up a branded sending domain with DMARC authentication configured.
2. Align your from-address with your branded sending domain.
3. Make unsubscribing easier and clearer.
   - Your marketing emails must include a method to unsubscribe in just one step. Klaviyo will automatically add a one-click unsubscribe link to the header of every email.
   - There must also be an unsubscribe link in the message body, but that link does not have to be one click to unsubscribe.

### How can I monitor Gmail spam complaint rates?

Klaviyo strongly advises that you setup [Google Postmaster Tools](https://www.gmail.com/postmaster/) on your domain so you can monitor your domain reputation and spam complaint rates, as Gmail does not provide spam complaint feedback directly to ESPs (email service providers) like Klaviyo. Note that before setting up Google Postmaster tools on your domain, make sure you have connected a branded sending domain to your Klaviyo account.

Learn [how to use Google Postmaster Tools](https://academy.klaviyo.com/use-google-postmaster-tools-to-monitor-your-spam-complaint-rate/1838637) to monitor your spam complaint rate.

In general, suppression of profiles that have never engaged is the best first step to addressing a high spam complaint rate. Klaviyo makes it easy to [create a Never Engaged segment](https://help.klaviyo.com/hc/en-us/articles/115005078347) through the Deliverability Hub.

### Why isn't the unsubscribe button in the header appearing on emails?

Klaviyo includes code for a one-click unsubscribe button in the header (i.e., list-unsubscribe header) for all of your emails. However, displaying this is completely at the discretion of inbox providers. Even if the button does not appear, your email is still compliant in the eyes of Gmail, Yahoo, and other providers as the necessary code is automatically included.

![List-unsubscribe header in gmail](https://klaviyo.zendesk.com/hc/article_attachments/28717853219355)

Gmail's interface will not display this unsubscribe button if Google believes the sending domain's reputation is poor. The main reasons Gmail may consider a domain's reputation to be poor and hide this button are:

- You are sending from a brand new domain. Keep sending and as long as your customers engage it will start to show.
- Your domain has established a sender reputation with a high rate of spam complaints, and/or low engagement.

If your domain is no longer new and has an established sender reputation, you should take action to [improve your sender reputation](https://help.klaviyo.com/hc/en-us/articles/8983758025883).

In general, suppression of profiles that have never engaged is the best first step to addressing a low sending reputation indicated by an invisible unsubscribe button in Gmail. Klaviyo makes it easy to [create a Never Engaged segment](https://help.klaviyo.com/hc/en-us/articles/115005078347) through the Deliverability Hub.

## Additional resources

[Frequently asked questions about deliverability](https://help.klaviyo.com/hc/en-us/articles/16425927010075)

[How to clean your list to maintain good deliverability](https://help.klaviyo.com/hc/en-us/articles/115005078347)

[How to remove spam traps from your account](https://help.klaviyo.com/hc/en-us/articles/360015537111)

[Troubleshooting why emails go to spam](https://help.klaviyo.com/hc/en-us/articles/12034571748251)

[Understanding sender reputation](https://help.klaviyo.com/hc/en-us/articles/15332906406171)

[Understanding email deliverability](https://help.klaviyo.com/hc/en-us/articles/115005247008)
