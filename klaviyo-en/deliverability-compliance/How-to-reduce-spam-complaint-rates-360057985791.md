---
id: "360057985791"
title: "How to reduce spam complaint rates"
source_url: "https://help.klaviyo.com/hc/en-us/articles/360057985791-How-to-reduce-spam-complaint-rates"
section: "Monitor deliverability and metrics"
category: "Deliverability & compliance"
category_slug: "deliverability-compliance"
klaviyo_updated: "2026-05-11T10:58:07Z"
language: "en"
---
## You will learn

Learn about spam complaint rates, and how you can reduce them.

Spam complaint rates measure how often recipients mark your messages as spam. A high rate needs immediate action, as it will hurt your deliverability and sender reputation.

This guide specifically focuses on email spam complaint rates. If you are instead focusing on SMS deliverability performance, head to [Campaign SMS and MMS Benchmarks](https://help.klaviyo.com/hc/en-us/articles/360051110111). You can also learn more about [SMS laws and regulations here](https://help.klaviyo.com/hc/en-us/articles/360035055312).

## What is a spam complaint rate?

Spam complaint rates measure how often subscribers mark your emails as spam. The formula for calculating spam complaint rate is:

- ****Spam complaint rate**** = (Number of people who mark your email as spam) / (Number of recipients)

Most inbox providers (especially Gmail) don’t share spam complaints with email service providers (ESPs) like Klaviyo. Because of this, few spam complaints are actually reported back to the sender. Therefore, even a very small percentage of spam complaints can indicate an issue.

Spam complaints might not appear on a customer’s profile in Klaviyo, depending on their inbox provider. For this reason, Google recommends [using Google Postmaster Tools to monitor your spam complaint rate for Gmail](https://academy.klaviyo.com/en-us/courses/use-google-postmaster-tools-to-monitor-your-spam-complaint-rate/1838637). Google Postmaster tools will give you insights into your total spam rate for all Gmail recipient

## Why spam complaint rates matter

When someone marks your emails as spam, this signals to inbox providers that you’re sending content to people who do not wish to receive it, and they will be more likely to send your emails directly to spam rather than an inbox in the future.

Spam complaints are more serious than when someone unsubscribes from your marketing, and a rise in spam complaints should not be taken lightly. To maintain a good sender reputation, monitor spam complaint rates closely, and when you see a rise, take action immediately to lower this metric.

An ideal spam complaint rate is as close to zero as possible, and trending downward if previously high.

For more information on what qualifies as good and bad for deliverability metrics, head to our guide on [monitoring email deliverability and performance metrics](https://help.klaviyo.com/hc/en-us/articles/115000201131).

## How to decrease spam complaint rates

Some key strategies to decrease spam complaint rates include:

1. [Optimize your sign-up pages and confirmation messages](#h_01JADS6GZHC6J66KXZY3HEK60H)
2. [Enable double opt-in](#h_01JADS6R3JH2ZS0N64S0250A6N)
3. [Make your unsubscribe link is easily accessible](#h_01JADRCBP8MZD97P4FRRK37WF2)
4. [Enable global unsubscribes](#h_01JADS7ZMSST0BSC6KD4ZFN0ZX)
5. [Try to avoid “spammy” or non-relevant subject lines](#h_01JADRCBP869WJYP48JTBJDVSA)
6. [Ensure your emails are easily discernible as coming from your brand](#h_01JADRCBP8XVSEY5YWEFZR9SQJ)
7. [Confirm that your emails render for all users](#h_01JADRCBP802CEX4HVYJ3NGRVG)
8. [Monitor and adjust your lists](#h_01JADRCBP8W1JEVTVB0Y2HQFEC)
9. [Evaluate sending frequency and segment by engagement](#h_01JADRCBP87AVF5DNEW2YXNSB0)

You can learn more about each of these strategies below.

### 1. Optimize your sign-up pages and confirmation messages

To reduce spam complaints, start by designing clear, well-branded sign-up pages.

Your sign-up forms should set clear expectations about what subscribers are signing up for, especially if you have sub-brands or different product lines they could receive emails from. Include details like:

- The channels you’ll contact them through (email/SMS)
- How their [information will be used](https://help.klaviyo.com/hc/en-us/articles/360037101072)
- The type of content they’ll receive

Consider using a [preference page](https://help.klaviyo.com/hc/en-us/articles/360002049952#preference-pages14) to let subscribers choose the types of content and frequency they prefer. This helps align what they expect with what you send.

In addition, you should always use a confirmation message to ensure that a subscriber understands that they just signed up to receive emails from your brand or need to confirm via email or text if you are using [double opt-in](https://help.klaviyo.com/hc/en-us/articles/115005251108).

Setting clear expectations reduces the likelihood of subscribers marking your emails as spam later on.

### 2. Enable double opt-In

[Double opt-in](https://help.klaviyo.com/hc/en-us/articles/115005251108) is the process through which a new subscriber must confirm their subscription before being added to your list. This is enabled by default for all Klaviyo lists, and it is highly recommended to keep it on unless you have a specific use case that calls for single opt-in.

To enable double opt-in:

1. Go to your list.
2. Select ****Settings****.
3. Scroll down to the **Opt-in Process** section and enable double opt-in.

![double opt in.jpg](https://klaviyo.zendesk.com/hc/article_attachments/30159866703643)

Learn more about the [double opt-in process](https://help.klaviyo.com/hc/en-us/articles/115005251108).

### 3. Ensure your unsubscribe link is easily accessible

Always include an easy to find [unsubscribe link](https://help.klaviyo.com/hc/en-us/articles/115006054267) in your emails. If someone can’t easily find this link to opt-out, they’re more likely to mark your email as spam, which has a larger negative impact than an unsubscribe.

Avoid hard-to-read unsubscribe links (e.g., light text on white background, or buried in text) Instead, place this link at the end of your emails, or at the beginning if you know you have a high mobile audience, and make the colors stand out for ease of reading and accessibility.

Additionally, ensure that your unsubscribe is working and easy to use. Do not place your unsubscribe link buried deep in your footer without room to click or tap easily. Make sure that your subscribers have enough room to click this and that it launches an active and working unsubscribe page.

It’s also helpful to allow users to adjust their communication preferences on the unsubscribe page (e.g., the types of emails they want or their desired frequency). If you include preference options on your unsubscribe page, ensure that you are not requiring your subscribers to make multiple clicks to find the options to unsubscribe from all emails if that’s what they ultimately want to do. It’s also important that if the subscriber adjusted their preferences instead of completely unsubscribing that you follow these requests when you send to them in the future.

Including an unsubscribe link in emails is mandatory. If Klaviyo detects ‌you do not have one, we will automatically include it in your email. However, you can edit this link and add it where you best see fit.

### 4. Enable global unsubscribes

We also highly recommend that you enable global unsubscribes for your lists in Klaviyo. When global unsubscribes are enabled, anyone who unsubscribes from an email will be globally unsubscribed and [suppressed](https://help.klaviyo.com/hc/en-us/articles/115005246108) from all lists.

To enable global unsubscribes:

1. Click into your desired list.
2. Select ****Settings.****
3. Scroll to **Unsubscribes** and enable global unsubscribes.

![global unsub.jpg](https://klaviyo.zendesk.com/hc/article_attachments/30159877849627)

Globally suppressed profiles will remain in your lists, but they will no longer receive emails. You can remove those suppressed emails from your lists by clicking ****Manage List > Remove Suppressed Profiles****.

If you do not have global unsubscribes on, then someone may unsubscribe from an email assuming they will never receive more communication from your brand; however, if they are on multiple lists or qualify for a flow, they can still be emailed and will be more likely to mark your content as spam. As a result, it is best to enable this within list settings.

You can access a direct link to a global unsubscribe page by selecting Account > ****Settings > Email****; then, scroll down to the **Consent** section of this page. Send this link to allow subscribers to opt-out of all future sends.

![unsub link.jpg](https://klaviyo.zendesk.com/hc/article_attachments/30159866714651)

Learn more about [unsubscribes](https://help.klaviyo.com/hc/en-us/articles/115005078267) in Klaviyo.

### 5. Try to avoid “spammy” or non-relevant subject lines

Another best practice to potentially lower spam complaint rates is to avoid subject lines that may sound like they come from spammers. Not only will this cause your recipients to think you are spam and mark your emails as such, but this may also raise suspicion among inbox providers.

Inbox providers have spam filters that automatically send suspicious emails to the spam folder rather than the inbox. In general, avoid the following spam-triggers:

- All capital letters (e.g., FREE MONEY NOW)
- Excessive special characters, symbols, or emojis (e.g., +++100% FREE MONEY!!)
- Ee-catching or spam-triggering phrases (e.g., JUST THIS ONCE FOR A LIMITED TIME ONLY or ACT NOW!!!)

Instead, craft subject lines that align with your audience's wants and needs. For example, using emojis that do not align with your brand or what a customer is expecting to receive information on, may be seen as spam. Additionally, misleading subject lines that do not align with what the customer originally signed up for or expected could lead to more spam complaints. Continue to A/B test, refine, and review your analytics data to see what subject lines resonate with each of your specific audiences.

### 6. Ensure your emails are easily discernible as coming from your brand

If you have set expectations correctly on your sign-up pages or forms, customers should be aware they will hear from your brand. With this in mind, you want to ensure that your email sender information is easily recognizable. While an email from an employee in your company may seem personal, especially for new subscribers, they may not know who this email is from and quickly delete it. If you are using personal names as your from-address, make sure that your subject lines or preview text clearly indicates your brand name.

If you would like to remove mention of your specific brand name from the sender information, preview, and subject line, you can do this later in a nurture sequences, after subscribers are familiar with you as a sender.

### 7. Confirm your emails render for all users

Always account for mobile and desktop displays of your emails. If there are issues on either layout, then customers who see the improperly rendered emails are more likely to mark them as spam, especially if they cannot access your unsubscribe link.

A higher-than-usual spam complaint rate may also signal [email clipping](https://help.klaviyo.com/hc/en-us/articles/115000591251). For example, Gmail clips emails that are greater than 102 KB in size. Be cognizant of this and adjust your email design accordingly to decrease the size and avoid frustrating recipients.

You can use third-party tools like [Litmus](https://www.litmus.com/) to preview your email across devices and inbox providers to avoid issues.

### 8. Monitor and adjust your lists

While refining your list growth and email marketing strategies are important, it’s also key to regularly clean your email lists to maintain healthy engagement.

Avoid emailing an old list that you have not contacted in a while (~over 3 months of no emails) or a list that you have never reached out to (and it’s older than ~6 months old). Instead take these old lists through 1-2 campaigns to reintroduce your brand. With these reintroduction emails, it's important to have your brand name prominent in your sender information as well as making your unsubscribe link easy to find. From these 1-2 campaigns, if any subscribers are still not engaging with your email, suppress or even delete these profiles.

Learn more about the [list cleaning process](https://help.klaviyo.com/hc/en-us/articles/115005078347).

### 9. Evaluate sending frequency and segment by engagement

Consider using a [sending schedule based on email engagement](https://help.klaviyo.com/hc/en-us/articles/360037527052). This is key to achieving strong open rates and maintaining a positive relationship with your subscribers.

Sending too often to unengaged profiles makes recipients more likely to mark messages as spam, whereas infrequent sends to engaged customers may miss opportunities.. It's best to achieve a happy medium through the use of segments and sending schedules.

## Additional resources

[Getting started with email deliverability monitoring and performance metrics](https://help.klaviyo.com/hc/en-us/articles/115000201131)

[Understanding email deliverability](https://help.klaviyo.com/hc/en-us/articles/115005247008)