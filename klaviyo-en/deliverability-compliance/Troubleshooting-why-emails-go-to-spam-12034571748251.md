---
id: "12034571748251"
title: "Troubleshooting why emails go to spam"
source_url: "https://help.klaviyo.com/hc/en-us/articles/12034571748251-Troubleshooting-why-emails-go-to-spam"
section: "Deliverability best practices and tools"
category: "Deliverability & compliance"
category_slug: "deliverability-compliance"
klaviyo_updated: "2026-04-21T13:54:25Z"
language: "en"
---
## You will learn

Learn about common reasons for emails to go to the spam folder.

Understanding the elements of your email that increase your likelihood of being delivered to the spam folder can help your sender reputation and your subscriber engagement rates.

## Before you begin

Klaviyo is responsible for sending your emails, but once these emails are in the hands of the inbox provider (i.e. Gmail or Yahoo), the messages are filtered according to each provider’s rules. All inbox providers have a built-in system that scans incoming emails, and automatically sorts them using complex algorithms that are not made public.

For more information on email deliverability and best practices, see our guide on [understanding email deliverability.](https://help.klaviyo.com/hc/en-us/articles/115005247008)

While inbox providers do not report the specific reason an email was placed into spam, it is generally due to a low sending reputation, caused by sending to dormant subscribers.

## Sender reputation

Sender reputation is a measure of how inbox providers evaluate your trustworthiness as a sender. This determines how emails are sorted, and is crucial to any email marketer. With a poor sending reputation, inbox providers can send the sender’s email straight to spam.

When inbox providers determine the sender reputation for each domain or IP, each provider evaluates various metrics. Some of the main metrics that contribute to the score include:

- ****Engagement (e.g., open rates and click rates)****Engagement refers to how people are interacting with your emails after they receive them, and it is important to maintain high engagement rates for good deliverability.
- ****Sending volume and frequency****How many emails are being sent at once and how often they are being sent.
- ****Bounce rates****Bounce rate is a measurement of how often your emails bounce. A bounce occurs when an email is either not successfully delivered or is rejected by a recipient's inbox provider (like Gmail or Yahoo).
- ****Spam complaints****Spam complaint rate measures how often subscribers mark your emails as spam.
- ****Unsubscribe rates****Your unsubscribe rate measures how often subscribers opt-out of receiving your email marketing. An unsubscribe occurs when a profile clicks your unsubscribe link or adjusts their consent in your subscribe and manage preferences pages.

### Engagement

Sending to dormant subscribers over and over again, without a "sunset policy" can lead to a lower sending reputation over time. If your sending reputation gets low enough then you need to [perform list cleanup](https://help.klaviyo.com/hc/en-us/articles/115005078347#h_01HRFFZ0S08XSSNSDB2M8YBNSN) to resolve the issue.

If you are seeing your emails getting placed in spam or junk, we highly recommend creating and then suppressing a segment of those who have [never engaged](https://help.klaviyo.com/hc/en-us/articles/115005078347) (opened, clicked, or purchased).

### Spam complaints

[Spam complaint rates](https://help.klaviyo.com/hc/en-us/articles/360057985791) measure how often recipients mark your emails as spam. A high spam complaint rate is something to act upon immediately as this will hurt your deliverability performance and sender reputation, so it is important to [monitor this metric](https://help.klaviyo.com/hc/en-us/articles/115000201131) and take action to lower spam complaints. In general, you should aim to be under a 0.01% spam complaint rate.

See our guide on how to [decrease spam complaint](https://help.klaviyo.com/hc/en-us/articles/360057985791) rates if you are seeing issues with spam complaints on your account.

### Unsubscribe rates

[Unsubscribe rates](https://help.klaviyo.com/hc/en-us/articles/360057471831) inform you of how often customers unsubscribe from your emails. A high unsubscribe rate indicates that you’re either sending to those who do not wish to receive your marketing or you’re sending content that does not resonate with this audience.

Silver lining with this metric is a high unsubscribe rate is also a sign that your brand's emails are actually hitting the inbox, because recipients very rarely go into their Spam folder to unsubscribe.

Even so, unsubscribe rates also impact your deliverability reputation, so it is important to [monitor this metric](https://help.klaviyo.com/hc/en-us/articles/115000201131) and take action to lower unsubscribes. In general, you should aim to be under a 0.3% unsubscribe rate per email campaign.

See our guide on how to [decrease unsubscribe rates](https://help.klaviyo.com/hc/en-us/articles/360057471831) if you are seeing issues with unsubscribes on your account.

### Sending volume and frequency

Sending too many emails to a mail server during a short time frame can result in rejections and the placement of emails in spam. In general, any more than one email per inbox per day is risky. If you are experiencing an issue where emails are going to spam then you should strive to lower your brand's **emails per inbox per day** less than or equal to 1.

You may also want to create[a sending schedule based on customer engagement](https://help.klaviyo.com/hc/en-us/articles/360037527052) which is key to achieving strong open rates and maintaining a positive relationship with your subscribers. Sending too often to unengaged profiles will hurt your sender reputation, whereas sending too infrequently to engaged customers is leaving money on the table. It's best to achieve a happy medium through the use of segments and sending schedules.

### Bounce rates

One of the factors that inbox providers consider when determining how to place your emails, is the bounce rate associated with your brand. A bounce occurs when an email is either not successfully delivered or is rejected by the recipient's email provider. If your account has a high number of bounces, this can have a negative impact on your deliverability performance and your sender reputation. It is important to [monitor this metric](https://help.klaviyo.com/hc/en-us/articles/115000201131) and take action when you see a rise in this rate. You should aim to keep bounce rates under 1%.

See our guide on how to [decrease bounce rates](https://help.klaviyo.com/hc/en-us/articles/360057036052) if you are seeing issues with bounces on your account.

## Email content

Inbox providers use spam filters to determine whether or not your emails reach the inbox. While it’s possible to observe trends in spam filter behavior, spam filters are designed so that evading them can’t be perfected.

Here are a few ways you can be smart about your email content:

- ****Avoid “spammy” subject lines.****
  A lot of words can potentially trigger spam filters; thus, we’ve compiled some [dos and dont's](http://www.klaviyo.com/blog/the-ultimate-ecommerce-spam-trigger-word-list-guide) regarding subject line word choice. In general, avoid using all capital letters. [Studies show](http://www.radicati.com/wp/wp-content/uploads/2014/01/Email-Statistics-Report-2014-2018-Executive-Summary.pdf) that 85% of recipients prefer an all-lowercase subject line to one in all caps. Both all caps and excessive exclamation points can trigger spam filters. Avoid things like:

- Using ALL CAPS TO ADVERTISE SOMETHING
- Using a lot of symbols!!!!!\*\*\*\*\*\*\*\*
- Including just one large image in your email
- Implementing eye-catching or spam triggering phrases like "JUST THIS ONCE FOR A LIMITED TIME ONLY", "100% FREE!", "ACT NOW!"

- ****Find a balance between images and text.****
  Emails that consist solely of GIFs and images (or are very image-heavy) may trigger spam filters. Instead, emails should contain a combination of images and text. Spammers often use images to avoid spam trigger words, but inbox providers have evolved faster. [Email on Acid](https://www.emailonacid.com/blog/article/email-development/does_text_to_image_ratio_affect_deliverability) found that emails should contain at least 500 text characters to avoid being sent directly to spam. Including contact information, legal disclaimers, an unsubscribe link, and a company address in fine print at the bottom of your email is required by some regional laws, and can help increase character count. Also, include alt text for your images so subscribers can read a description if your images don’t load properly. Alt text is also crucial to ensure that your emails are accessible.
- ****Limit the number of URLs.****
  Large amounts of hyperlinked text can be considered a red flag for inbox providers. Spammers typically include as many links as possible, both hidden and overt. While including a few well-placed links probably won't cause any problems, consider only including necessary links and avoid overuse, especially if you link to sites other than your own.
- ****Avoid unnecessary code in your templates.****
  If you use our drag-and-drop template editor, we take care of this for you. If you're coding your own HTML templates or editing the source code of text blocks within our template editor, note that extra tags and poor code can trigger spam filters. Copy and pasting text from certain softwares like Microsoft Word can bring over styling that increases the code weight. To paste copied text without the associated styling, use **Ctrl + Shift + V** as a keyboard shortcut on Windows, and **Cmd + Shift + V** on Mac OS.
- ****Get personal in your messaging.****
  The more personalized your emails are, the more likely email clients are to deem them important and subscribers may be more inclined to open as well. If an email client determines that you likely know the person you're sending to, this significantly lowers the risk of your email ending up in spam. Klaviyo makes it easy to [insert a recipient's first name into the subject line and body of an email](https://help.klaviyo.com/hc/en-us/articles/11613154130843). You can also ask your contacts to add you to their address books, or try using plain text emails as opposed to formatted ones. When in doubt, run your email templates through free spam filter tools online like [Mail Tester](https://www.mail-tester.com/). This can help flag issues with your content that may cause email clients to flag your emails.
- ****Add 2 unsubscribe links or buttons.****
  Consider adding an unsubscribe link to the top of your email and to the bottom. Letting people opt out when they no longer want to receive emails will reduce spam complaints and increase open rates over time as you begin to send to a more engaged list overall. While you don't want high unsubscribe rates, you'd much rather someone unsubscribe than mark your email as spam.This will also help in cases where emails may be [clipped](https://help.klaviyo.com/hc/en-us/articles/115000591251) because they are too large.

## Email authentication issues

Mail servers use [email authentication protocols](https://help.klaviyo.com/hc/en-us/articles/4402601857307) to verify that incoming emails are from legitimate senders, protecting your brand and your customers from malicious actors. The most commonly used email authentication standards are [SPF, DKIM, and DMARC](https://help.klaviyo.com/hc/en-us/articles/360039295051-Deliverability-glossary).

If your emails fail this verification, it can cause your emails to be rejected or to be placed in spam. Determine if your brand is using a DMARC policy and make sure that it is valid.

In order to be DMARC compliant, you need to connect a branded sending domain (also known as a dedicated sending domain) to your account where the root domain of your DSD matches that of the root domain used in your sender email address (friendly-from address). For instance, if you send an email using **sales@example.com** as the from address and **example.com** is protected by DMARC, your account will need to use a branded sending domain like **send.example.com** to meet DMARC requirements.

In addition to preventing phishing and spoofing attempts, implementing these protocols can help improve deliverability, as mailbox providers will be able to confirm the identity of the sender.

## Gmail and Yahoo sender requirements

Google and Yahoo have announced new sender requirements that they are planning to start enforcing in February of 2024. If you are seeing emails go to spam, verify that you meet the following requirements set in place by Gmail and Yahoo:

- ****Remove Gmail or Yahoo from your friendly from-address****Don’t use Gmail or Yahoo email addresses in your friendly "from" address. If you are using @gmail.com or @yahoo in the “from” address of your emails, switch the "from" address over to a website domain you own.
- ****Setup a [branded sending domain](https://help.klaviyo.com/hc/en-us/articles/115000357752)****Branded sending domains (also known as dedicated sending domains) give you better control over your sender reputation. They also improve your branding in the "from" address in the inbox by removing the sent “via klaviyomail.com” disclaimer. Branded sending domains are a great deliverability best practice, and are a requirement for bulk senders who regularly email Google and Yahoo recipients starting in February.
- ****Setup a [DMARC policy](https://help.klaviyo.com/hc/en-us/articles/4402601857307) on your root domain****DMARC authentication is a protocol policy that servers use to make sure emails are coming from a legitimate sender. Brands use DMARC policies to protect the domain in their sender email address from unauthorized use by bad actors. DMARC authentication is set up in your DNS provider (e.g., GoDaddy or Cloudflare).
- ********Align your from-address domain with your branded sending domain********In order to be DMARC compliant, the domain in your friendly “from” address must align with the root domain in your branded sending domain.
- ****Make it easy to [unsubscribe](https://help.klaviyo.com/hc/en-us/articles/115005078267)****Audit your campaign templates and flow emails to ensure that you have an unsubscribe link somewhere in the body of your email (the footer is usually the most common).
- ********Keep [spam complaints low](https://help.klaviyo.com/hc/en-us/articles/360057985791)********
  Low spam complaints are a key way to show inbox providers that you are a legitimate sender who follows deliverability best practices. Visit the [deliverability hub](https://help.klaviyo.com/hc/en-us/articles/18378819907995) in Klaviyo to view your deliverability metrics, or try [Google Postmaster Tools](https://academy.klaviyo.com/use-google-postmaster-tools-to-monitor-your-spam-complaint-rate/1838637) to monitor how your sending strategy aligns with Google's requirements.

Some of these requirements only apply to bulk senders, or those that send 5,000 emails to Gmail recipients per day. Learn more about [Gmail and Yahoo’s upcoming sender requirements](https://academy.klaviyo.com/2024-new-sender-requirements-checklist/) for emails to land in inboxes successfully.

## Additional resources

- [How to repair your sending reputation](https://help.klaviyo.com/hc/en-us/articles/8983758025883)
- [Understanding and monitoring email deliverability performance](https://help.klaviyo.com/hc/en-us/articles/115000201131)
- [Understanding email deliverability](https://help.klaviyo.com/hc/en-us/articles/115005247008)