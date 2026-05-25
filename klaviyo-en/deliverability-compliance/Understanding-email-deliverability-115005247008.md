---
id: "115005247008"
title: "Understanding email deliverability"
source_url: "https://help.klaviyo.com/hc/en-us/articles/115005247008-Understanding-email-deliverability"
section: "Getting started with email deliverability"
category: "Deliverability & compliance"
category_slug: "deliverability-compliance"
klaviyo_updated: "2026-04-21T13:54:22Z"
language: "en"
---
Learn about email deliverability, including the steps you can take to establish a strong [sender reputation](https://help.klaviyo.com/hc/en-us/articles/15332906406171) so that your emails are delivered to the inbox.

## What is email deliverability?

Email deliverability is a nuanced concept, and there are several factors that influence an email’s likelihood of being successfully delivered.

The 2 components that allow an email to successfully land in a recipient’s inbox are email delivery and email deliverability.

### Email delivery

Email delivery refers to when an email is successfully delivered to a recipient’s mail server. A [bounce](https://help.klaviyo.com/hc/en-us/articles/115005250408) occurs when an email is either not successfully delivered or is rejected by the recipient's email provider.

Factors that impact delivery include:

- ****The validity of the recipient’s email address****
  Attempting to send a message to an address that does not exist results in a rejection.
- ****Temporary issues on the receiving server’s end with accepting incoming emails****Temporary issues like a recipient's inbox being full, or when their email server is momentarily down, may result in message rejection.
- ****Email authentication****Mail servers use [authentication protocols](https://help.klaviyo.com/hc/en-us/articles/4402601857307) like SPF, DKIM, and DMARC to verify that incoming emails are from legitimate senders and can reject emails that fail.
- ****Throttling****Sending too many emails to a mail server during a short time frame can result in rejections.

### Email deliverability

Email deliverability refers to the placement of an email after it is successfully delivered to the recipient’s mail server. Good email deliverability allows your emails to land in your recipient's main inbox (including tabbed inboxes, such as Google’s Promotions tab). Deliverability is best measured through events that indicate real human engagement (e.g., opens, clicks, replies, forwards, or conversions).

It is possible to have good email delivery but poor deliverability if the majority of delivered messages don’t make it to the primary inbox and instead land in spam.

New to deliverability? Check out our [deliverability glossary](https://help.klaviyo.com/hc/en-us/articles/360039295051) to familiarize yourself with key terminology.

The 4 main points to consider that influence email deliverability and your reputation as a sender:

1. ****Who you send to and how they engage****The profiles that you send to and how engaged they are with your sends.
2. ****Your sending habits****How many emails are being sent at once and how often they are being sent.
3. ****The content of your email****Inbox providers use spam filters to determine whether or not your emails reach the inbox based on content like images, links, and subject lines.
4. ****Your sending infrastructure****The infrastructure you are sending from, like your sending domain, click tracking domain, and IP address.

## Email deliverability best practices

By following these deliverability best practices, you can set your brand up for success and ensure that more of your emails make it to your recipients’ primary inboxes.

### Warming and ramping

Any new sender must warm up their sending infrastructure when moving to a new email service provider like Klaviyo to initially establish a good sender reputation. If applicable make sure to [warm your sending infrastructure.](https://help.klaviyo.com/hc/en-us/articles/360025945671)

****Warming****All Klaviyo customers sending from new dedicated infrastructure (ie. a new dedicated IP or a newly registered root domain) must complete the correlating IP or domain warming. Warming occurs when you introduce a new or “cold” IP (i.e., an IP address that has not been used to send emails in the last 30 days) or new or “cold” root domain (i.e., a domain that has been registered in the last 30 days or has never been used to send emails). Warming is the period of time in which you are establishing a reputation as a legitimate or “good” email sender.

****Ramping****Ramping is a process that aids in the overall warming process to become a reputable sender, whether you are using a dedicated or shared IP. When ramping a dedicated IP, this will be part of your overall warming process as it relates to your new infrastructure. Ramping shared IP’s involves new customers needing to warm their reputation relative to their new relationship with Klaviyo IPs.

Ramping involves starting out with smaller volumes of email sends, and then gradually increasing that volume over time. Depending on the volume of email that you send, the entire warming process may continue after you have fully ramped or sent all of your emails. For example, ramping to a 100k email volume may take as little as 10 days, but your email service provider (ESP) or a mailbox provider (MBP) typically take up to 30 days to make an initial decision on your reputation. During this time, you may also note that your email performance (i.e., opens and clicks) can fluctuate for up to ~120 days while your reputation is validated.

Learn more about the [warming and ramping](https://help.klaviyo.com/hc/en-us/articles/7520811253275) processes with Klaviyo.

### Import clean lists

If you intend to [sync over existing email lists](https://help.klaviyo.com/hc/en-us/articles/115005078487) or manually import existing lists into Klaviyo, your deliverability may be at risk if you don't clean them first. Your former email service provider (ESP) most likely provides a way to analyze the engagement level of your main list using data points such as open rates, bounce rates, and more.

Before you migrate any existing lists into Klaviyo, we recommend using all data available to isolate and remove any invalid or [inactive emails](https://help.klaviyo.com/hc/en-us/articles/115005078347) from your list. Uploading these emails to Klaviyo will only bloat your sending and drag down your deliverability. It's imperative that this is done **in advance** of your first send with Klaviyo.

### Send to opted-in recipients only

Ensure that your main email list only contains individuals who have opted in and that you aren’t deliberately (or inadvertently) reaching out to those who never subscribed. We highly recommend that you keep customers and opted-in subscribers separate. A customer can become an email subscriber at any time, and a subscriber can become a customer at any time. However, while customers may have placed an order, this does not necessitate opting in to receive regular email communication. If you send regular campaigns to everyone in your account regardless of whether they signed up for marketing emails, you will see increased unsubscribe rates and decreased engagement — both negatively impact your deliverability.

It is best practice to have new subscribers confirm their email addresses when they first opt in. This double opt-in process helps you grow your list while minimizing abuse and preventing the accumulation of invalid or mistyped emails. Double opt in also results in a more engaged list. If you have disabled double opt in for one or more lists, you will need to be diligent about [list cleaning](https://help.klaviyo.com/hc/en-us/articles/115005078347) every month or so.

Learn more about the [double opt-in process](https://help.klaviyo.com/hc/en-us/articles/115005251108).

### Conduct regular list cleaning

Don't give email clients an excuse to flag you. Create [a segment like this one from the Deliverability Hub](https://help.klaviyo.com/hc/en-us/articles/360044054732#h_01JEREANGCF07WNS6CSNF2MRSS) to suppress the group of subscribers that never engage with your emails. Most major email clients (like Gmail and Yahoo) track how recipients interact with emails from your domain (e.g.,how many emails are marked as spam, how many are opened, how many bounce, etc). Therefore, continuing to send to these profiles with zero engagement can erode your sending reputation.

Mailbox Providers use this information to determine where your emails will be placed, whether it’s in the recipient’s inbox or their spam folder. Having a list that contains uninterested people or a high percentage of invalid emails will only hurt your efforts to reach those who actually do want to receive your emails. It is important to [conduct regular list cleaning](https://help.klaviyo.com/hc/en-us/articles/115005078347) to exclude these individuals from your sends.

### Create an engaged segment

Not only should you send to opted-in contacts, but you should also aim to send to engaged subscribers; otherwise, you risk hurting your deliverability performance. To isolate engaged subscribers, [create an engaged segment](https://help.klaviyo.com/hc/en-us/articles/115000200072); then, target this segment when sending campaigns.

With the release of iOS15, macOS Monterey, iPadOS 15, and WatchOS 8, Apple Mail Privacy Protection (MPP) changed the way that we receive open rate data on your emails by prefetching our tracking pixel. With this change, it’s important to understand that open rates will be inflated.

If your campaign analytics show a large number of iOS openers, we suggest identifying these affected opens in your individual [subscriber segments.](https://help.klaviyo.com/hc/en-us/articles/4416791883163)

For complete information on MPP opens, visit our guide on [iOS 15 and the changes you need to know about.](https://www.klaviyo.com/blog/apple-ios15-klaviyo)

### Configure your email sending infrastructure

When sending from Klaviyo, you have the option of sending from Klaviyo’s shared infrastructure or your own [dedicated infrastructure](https://help.klaviyo.com/hc/en-us/articles/7674941873947).

Klaviyo recommends you [set up a dedicated sending domain](https://help.klaviyo.com/hc/en-us/articles/115000357752) so you can use your brand’s domain name to send emails instead of a Klaviyo domain and develop a sending reputation on your own domain. Additionally, this enables [DKIM and SPF authentication](https://help.klaviyo.com/hc/en-us/articles/4402601857307), which recipients’ mail servers use to verify an email sender's identity.

For accounts that qualify, you can also set up a [dedicated IP address](https://help.klaviyo.com/hc/en-us/articles/7675517826587) in Klaviyo.

Make sure to take the following steps to ensure proper setup for good email delivery and deliverability:

1. Determine if your brand is using a [DMARC policy](https://help.klaviyo.com/hc/en-us/articles/4402601857307) and make sure that it is valid.
2. Confirm that you have domain alignment with your emails (i.e., your sender email address or friendly-from address root domain matches the root domain used in your dedicated sending domain).
3. [Connect a dedicated click tracking domain.](https://help.klaviyo.com/hc/en-us/articles/360001550572)

### Set up BIMI

[BIMI](https://bimigroup.org/) uses your DNS settings to authenticate your visual brand identity in emails you send by giving you control over the logo used in inboxes. Implementing BIMI can increase brand recognition, legitimize your business, and boost deliverability by building trust with your recipients and improving engagement rates. For information regarding how to configure this, see our guide [about BIMI.](https://help.klaviyo.com/hc/en-us/articles/4406592127515)

### Manage email preferences

Add fields to your sign-up form and subscribe/manage preference pages so subscribers can choose how often they would like to receive emails from you. You can then [segment based on these preferences](https://help.klaviyo.com/hc/en-us/articles/115000769631) and ensure your email sending considers the frequency preferences of your recipients.

According to [eMarketer](http://blog.hubspot.com/blog/tabid/6307/bid/13879/Segment-Your-Email-List-To-Increase-Open-Rates-Data.aspx#sm.0000w0p35x9y7fazyrg21vaugq2ih), 39% of email marketers that practice list segmentation see better open rates, 28% see lower opt-out and unsubscribe rates, and 24% see better email deliverability, increased sales leads, and greater revenue.

### Make it easy to unsubscribe

If you don't make it easy for recipients to opt out and decide if and when they want to stop receiving your emails, they are more likely to mark your email as spam. Spam complaints are serious and can significantly damage your email deliverability.

If your abuse rate hits even 0.05%, inbox providers (e.g., Gmail, Hotmail, Yahoo) will start to consider you a "bad sender" and take matters into their own hands. They may flag your emails as spam for all recipients. As a result, it is best practice to place an unsubscribe link near the top of your email, as well as the bottom, to ensure recipients know the best way to signal they'd like to opt out. A spam complaint is much graver than an unsubscribe.

You can also give subscribers the option to choose how often they'd like to receive emails from you. You can then segment based on these preferences and ensure your email sending takes into consideration the frequency preferences of those on the receiving end. As mentioned above, according to eMarketer, 39% of email marketers that practice segmentation see better open rates, 28% see lower opt-out and unsubscribe rates, and 24% see better email deliverability, increased sales leads, and greater revenue.

### Create engaging content

Inbox providers use spam filters to determine whether or not your emails reach the inbox. While it’s possible to observe trends in spam filter behavior, spam filters are designed so that evading them can’t be perfected.

Here are a few ways you can be smart about your email content:

- ****Avoid spammy subject lines.****
  A lot of words can potentially trigger spam filters; thus, we’ve compiled some [dos and dont's](http://www.klaviyo.com/blog/the-ultimate-ecommerce-spam-trigger-word-list-guide) regarding subject line word choice. In general, avoid using all capital letters. [Studies show](http://www.radicati.com/wp/wp-content/uploads/2014/01/Email-Statistics-Report-2014-2018-Executive-Summary.pdf) that 85% of recipients prefer an all-lowercase subject line to one in all caps. Both all caps and excessive exclamation points can trigger spam filters. Avoid things like:

- Using ALL CAPS TO ADVERTISE SOMETHING
- Using a lot of symbols!!!!!\*\*\*\*\*\*\*\*
- Including just one large image in your email
- Implementing eye-catching or spam triggering phrases like "JUST THIS ONCE FOR A LIMITED TIME ONLY", "100% FREE!", "ACT NOW!"

- ****Find a balance between images and text.****
  Emails that consist solely of images (or are very image-heavy) may trigger spam filters. Instead, emails should contain a combination of images and text. Spammers often use images to avoid spam trigger words, but inbox providers have evolved faster. [Email on Acid](https://www.emailonacid.com/blog/article/email-development/does_text_to_image_ratio_affect_deliverability) found that emails should contain at least 500 text characters to dodge spam filters. If this is an issue for you, consider including contact information, legal disclaimers, an unsubscribe link, or a company address in fine print at the bottom of your email. Also, include ALT text for your images so subscribers can read a description if your images don’t load properly. ALT text is also crucial to ensure that your emails are accessible.
- ****Limit the number of URLs.****
  Large amounts of hyperlinked text can be considered a red flag for inbox providers. Spammers typically include as many links as possible, both hidden and overt. While including a few well-placed links probably won't cause any problems, consider only including necessary links and avoid overuse, especially if you link to sites other than your own.
- ****Avoid unnecessary code in your templates.****
  If you use our drag-and-drop template editor, we take care of this for you. If you're coding your own HTML templates or editing the source code of text blocks within our template editor, note that extra tags and poor code can trigger spam filters.
- ****Get personal.****
  The more personalized your emails are, the more likely email clients are to deem them important. If an email client determines that you likely know the person you're sending to, this significantly lowers the risk of your email ending up in spam. Klaviyo makes it easy to [insert a recipient's first name into the subject line and body of an email](https://help.klaviyo.com/hc/en-us/articles/11613154130843). You can also ask your contacts to add you to their address books, or try using plain text emails as opposed to formatted ones. When in doubt, run your email templates through free spam filter tools online like [Mail Tester](https://www.mail-tester.com/). This can help flag issues with your content that may cause email clients to flag your emails.
- ****Add 2 unsubscribe buttons.****
  Consider adding one to the top of your email and one to the bottom. Letting people opt out when they no longer want to receive emails will reduce spam complaints and increase open rates over time as you begin to send to a more engaged list overall. While you don't want high unsubscribe rates, you'd much rather someone unsubscribe than mark your email as spam.

### Create a sending schedule

[Creating a sending schedule based on customer engagement](https://help.klaviyo.com/hc/en-us/articles/360037527052) is key to achieving strong open rates and maintaining a positive relationship with your subscribers. Sending too often to unengaged profiles will hurt your sender reputation, whereas sending too infrequently to engaged customers leaves money on the table. It's best to achieve a happy medium through the use of segments and sending schedules.

### Develop a sunset strategy

[Sunset flows](https://help.klaviyo.com/hc/en-us/articles/360017518492) are designed to phase out customers who are no longer engaging with your brand. You can use this flow as a last-ditch effort to win back their business, and then delete or suppress anyone who is not responsive. This will help you maintain a clean list, which can prevent you from sending to unengaged subscribers and possibly harming your deliverability.

You can also run a [re-engagement email campaign](https://help.klaviyo.com/hc/en-us/articles/115000931551) to target these inactive users.

## Monitoring deliverability

Monitoring your deliverability performance over time is key to understanding how inbox providers may view your brand as a sender, and how likely you are to land in recipients’ main inbox. Regularly monitoring deliverability can also help you quickly identify drops in performance, and mitigate potential deliverability issues before they have a large impact.

Key metrics include:

- Open rates
- Click rates
- Bounce rates
- Spam complaints

Your performance with these metrics impacts your sender reputation and ultimately inbox placement rates. These metrics will help you see the holistic view of your email campaign performance, allow you to identify any issues beforehand and take corrective measures to improve email deliverability. Keep your email list clean by regularly removing inactive subscribers and engaging with your audience through relevant and personalized content.

You can use the **Deliverability hub** in Klaviyo as a centralized space that allows you to analyze and diagnose your email deliverability health at the account level.

![Deliverability hub in Klaviyo](https://klaviyo.zendesk.com/hc/article_attachments/28705662765083)

Here, you’ll see a score that represents your overall deliverability performance and sender reputation, as well as your performance in the key deliverability metrics. You’ll also see an action center with recommended next steps, and a variety of reports that provide insight towards your performance with different inbox providers or email domains.

Learn more about [how to monitor deliverability](https://help.klaviyo.com/hc/en-us/articles/115000201131) in Klaviyo.

## Gmail and Yahoo sender requirements

Google and Yahoo have announced new sender requirements that they are planning to start enforcing in February of 2024. If you are seeing emails go to spam, verify that you meet the following requirements set in place by Gmail and Yahoo:

- ****Remove Gmail or Yahoo from your friendly from-address****Don’t use Gmail or Yahoo email addresses in your friendly "from" address. If you are using @gmail.com or @yahoo in the “from” address of your emails, switch the "from" address over to a website domain you own.
- ****Setup a [branded sending domain](https://help.klaviyo.com/hc/en-us/articles/115000357752)****Branded sending domains (also known as dedicated sending domains) give you better control over your sender reputation. They also improve your branding in the "from" address in the inbox by removing the sent “via klaviyomail.com” disclaimer. Branded sending domains are a great deliverability best practice, and are a requirement for bulk senders who regularly email Google and Yahoo recipients starting in February.
- ****Setup a [DMARC policy](https://help.klaviyo.com/hc/en-us/articles/4402601857307) on your root domain****DMARC authentication is a protocol policy that servers use to make sure emails are coming from a legitimate sender. Brands use DMARC policies to protect the domain in their sender email address from unauthorized use by bad actors. DMARC authentication is set up in your DNS provider (e.g., GoDaddy or Cloudflare).
- ****Align your from-address domain with your branded sending domain****In order to be DMARC compliant, the domain in your friendly “from” address must align with the root domain in your branded sending domain.
- ****Make it easy to [unsubscribe](https://help.klaviyo.com/hc/en-us/articles/115005078267)****Audit your campaign templates and flow emails to ensure that you have an unsubscribe link somewhere in the body of your email (the footer is usually the most common).
- ****Keep [spam complaints low](https://help.klaviyo.com/hc/en-us/articles/360057985791)****
  Low spam complaints are a key way to show inbox providers that you are a legitimate sender who follows deliverability best practices. Visit the [deliverability hub](https://help.klaviyo.com/hc/en-us/articles/18378819907995) in Klaviyo to view your deliverability metrics, or try [Google Postmaster Tools](https://academy.klaviyo.com/use-google-postmaster-tools-to-monitor-your-spam-complaint-rate/1838637) to monitor how your sending strategy aligns with Google's requirements.

Some of these requirements only apply to bulk senders, or those that send 5000 emails to Gmail recipients per day. Learn more about [Gmail and Yahoo’s upcoming sender requirements](https://academy.klaviyo.com/2024-new-sender-requirements-checklist/) for emails to land in inboxes successfully.

## Additional resources

- [Getting started with email deliverability monitoring and performance metrics](https://help.klaviyo.com/hc/en-us/articles/115000201131)
- [How to set up a dedicated sending domain](https://help.klaviyo.com/hc/en-us/articles/115000357752)
- [How to ramp and warm your sending infrastructure](https://help.klaviyo.com/hc/en-us/articles/360025945671)