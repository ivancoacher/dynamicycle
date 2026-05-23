<h1>How to decrease bounce rates</h1>

## You will learn

Learn more about bounce rates and how to decrease them over time. Bounce rates inform you of how often customers' email addresses bounce when you send to your subscriber list. A high bounce rate has a negative effect on your deliverability performance, and thus, on your sender reputation. It is important to monitor this metric and take action when you see a rise in this rate.

This article specifically focuses on email bounce rates. If you are instead focusing on SMS deliverability rates, learn more in [campaign SMS and MMS benchmarks](https://klaviyo.zendesk.com/hc/en-us/articles/360051110111) for guidance.

## What is a bounce rate?

Bounce rate is a measurement of how often your emails bounce. A bounce occurs when an email is either not successfully delivered or is rejected by a recipient's inbox provider (like Gmail or Yahoo).

There are two types of bounces that are included in your bounce rate:

- ****Hard bounces****Emails that cannot be delivered due to a permanent reason, such as a fake or spam email address. Klaviyo will automatically suppress a profile that hard bounces.
- ****Soft bounces****Emails that cannot be delivered due to a temporary reason, such as a full inbox. If an email soft bounces more than 7 consecutive times, Klaviyo will suppress this address. If you want to manually suppress these profiles before reaching the 7 count bounce limit, learn more in [removing soft bounces](https://help.klaviyo.com/hc/en-us/articles/360057036052#h_01GMJ1QRQMEXDVT6SVA7KVBZYN).

The calculation for bounce rate is as follows:

- ****Bounce rate****
  The number of [bounced emails](https://help.klaviyo.com/hc/en-us/articles/115005250408) divided by the total number of emails sent.

## Why bounce rates matter

If your account has a high number of bounces, this can have a negative impact on your deliverability and sender reputation. As your reputation diminishes, inbox providers may begin sending your emails to spam rather than to a recipient’s inbox. This is because it signals to inbox providers that you do not regularly clean your list or follow list acquisition best practices. Therefore, it’s crucial to be on the lookout for an increase in bounce rates so that you can quickly amend the situation before it becomes a problem.

## How to decrease bounce rates

Some key strategies to decrease bounce rates include:

1. [Emailing real, consented profiles](#h_01GMJ1E512MXC5R65E4907FRRE)
2. [Enabling double opt-in](#h_01GMJ1FYY30D9CJM1MRTPC5EP9)
3. [Cleaning your lists regularly](#h_01EZAAG28B388PMCJE6AYWMTYE)
4. [Removing soft bounces](#h_01GMJ1QRQMEXDVT6SVA7KVBZYN)

### 1. Emailing real, consented profiles

Sending to real subscribers who have directly consented to your marketing is crucial. You should aim to build a strong reputation, not only with inbox providers, but also with the recipients you send to by only emailing real subscribers who actively want to hear from you.

It is never okay to buy lists or message individuals who have not opted-in to receive your brand communication. This will have a negative impact on your deliverability and can damage your sender reputation with inbox providers, raising the likelihood that your emails will be sent to spam.

Moreover, if you offer a lot of on-site giveaways or contests that sync profiles to your main list, you may acquire unengaged and fake emails. For example, someone may subscribe for the sole purpose of a giveaway. Even if their contact information is real, it may include an email address they rarely use; if their inbox reaches capacity, then your emails will start to bounce. As a result, consider focusing on other ways to acquire subscribers (e.g., free shipping or a discount on their first purchase) or creating a separate list for new subscribers who enter your account via promotional contests and giveaways. If you do sync these subscribers to your main list, then [list cleaning](#h_01EZAAG28B388PMCJE6AYWMTYE) is crucial to manage this influx of contacts and ensure that only those who actively engage with your content remain on your subscriber list.

It is best practice to send primarily to [engaged subscribers](https://klaviyo.zendesk.com/hc/en-us/articles/115000200072) who have interacted with your emails recently.

### 2. Enabling double opt-In

Lists are set to double opt-in by default in all Klaviyo accounts and we strongly suggest that you keep this setting enabled. Double opt-in is a process through which a new subscriber must confirm their subscription via email before being added to your list.

It is strongly cautioned against using single opt-in on any of your lists unless you have a specific use case that calls for it. If you have a list set to single opt-in and see a rise in bounce rates, it is best practice to toggle on double opt-in in your list settings.

![Opt in settings showing double opt-in toggled on](https://klaviyo.zendesk.com/hc/article_attachments/28705664088091)

Learn more about the [double opt-in process](https://klaviyo.zendesk.com/hc/en-us/articles/115005251108).

### 3. Cleaning your lists regularly

List cleaning removes any unengaged, misspelled, fake, or spam email addresses that you may collect over time. Doing so will decrease your bounce rates as you weed out any profiles who should no longer receive your messaging, many of whom may be soft bouncing each time you send. Bounces negatively impact your deliverability, so proactive list cleaning and suppressing profiles who are unengaged will improve your sender reputation over time.

Review step-by-step instructions on [how to clean your lists](https://klaviyo.zendesk.com/hc/en-us/articles/115005078347).

### 4. Removing soft bounces

If you have a very high bounce rate, proactively removing soft bounces can help you boost your deliverability performance. Klaviyo automatically suppresses profiles that soft bounce seven consecutive times; however, each time an email bounces, your deliverability is affected. As a result, it's a good idea to exclude, and even suppress, email addresses that have recently soft bounced from your campaigns.

To remove these emails, review instructions on [managing email suppressions and deleting profiles in bulk](https://help.klaviyo.com/hc/en-us/articles/24312135764251) and [excluding lists or segments from a campaign send](https://help.klaviyo.com/hc/en-us/articles/360007016571).

To find these profiles, create a segment that identifies chronic soft bounces. When building out your segment, include anyone with at least four bounced emails in the last 90 days, and who can receive email marketing. An example of this segment is shown below.

![](https://klaviyo.zendesk.com/hc/article_attachments/37028158634651)

## Additional resources

- [How to monitor email deliverability performance](https://klaviyo.zendesk.com/hc/en-us/articles/115000201131)
- [Troubleshooting decreasing KPIs](https://klaviyo.zendesk.com/hc/en-us/articles/360043802871)
- [Understanding bounced emails in Klaviyo](https://klaviyo.zendesk.com/hc/en-us/articles/115005250408)
