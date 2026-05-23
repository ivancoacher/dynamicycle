---
id: 25620771311643
title: "Email deliverability best practices reference"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/25620771311643-Email-deliverability-best-practices-reference"
section: "Getting started with email deliverability"
category: "Deliverability & compliance"
category_slug: "deliverability-compliance"
klaviyo_updated: "2026-05-11T13:47:26Z"
language: en
---

## You will learn

Learn about the different best practices for email deliverability. Following these best practices and recommendation actions is key to maintaining strong deliverability and successfully landing in customer inboxes.

Learn about [email deliverability and its importance](https://help.klaviyo.com/hc/en-us/articles/115005247008).

## Infrastructure setup

Email deliverability infrastructure refers to the different systems, tools, and domains that are used to deliver your emails to recipients.

Your infrastructure is an important consideration inbox providers use when determining your trustworthiness as a sender and determining how to place your emails. It is also a key part of protecting your domain and customers from malicious actors attempting to use your brand’s sending identity.

The main infrastructure components that are important to consider when sending emails in Klaviyo are the following:

****Branded sending domains****

Connecting a [branded sending domain](https://help.klaviyo.com/hc/en-us/articles/115000357752) is best practice and allows you to use your brand’s domain name to send emails instead of a shared Klaviyo domain. It also allows you to build a sending reputation on your brand’s own domain, and limit any negative impact to your domain reputation and deliverability from other companies using the same shared domains. In other words, you are the only one that will send from your domain and thus affect your reputation.

Additionally, connecting a branded sending domain allows you to take advantage of email security protocols like [DMARC](https://help.klaviyo.com/hc/en-us/articles/4402601857307). Mail servers use these protocols to verify that incoming emails are from legitimate senders, protecting your brand and your customers from malicious actors. In addition to preventing phishing and spoofing attempts, implementing these protocols can help improve deliverability, as mailbox providers will be able to more easily verify your sender identity.

Klaviyo advises all customers to set up a branded sending domain, as this record alignment between your root domain, sending domain, and friendly from-address is critical to supporting successful inbox placement.

Klaviyo recommends that accounts with a database size of more than 5000 profiles set up a branded sending domain with DMARC to avoid performance disruptions due to [Yahoo and Gmail’s sender requiremenets](https://academy.klaviyo.com/2024-new-sender-requirements-checklist/1817230).

Learn more about [branded sending domains](https://help.klaviyo.com/hc/en-us/articles/115000357752) and how to set one up for your account.

****Dedicated IPs****

In Klaviyo, you can send emails using a shared IP address, or your own [dedicated IP](https://help.klaviyo.com/hc/en-us/articles/7675517826587). Sending from a shared IP address means that you will send alongside several other Klaviyo customers, with a shared sending reputation.

It is recommended that if you consistently send over 1,000,000 emails per month, to use a dedicated IPs. Shared IPs are more effective for smaller senders that don’t have a regular sending schedule.

The main benefit of using a dedicated IP address is that the reputation of the IP address can only be influenced by the single account that is using it. As such, you have complete control over your own sender reputation. Similarly, you also have complete control over your sending volumes, and will not be affected by shared IP and potential volume spikes during busy times of year.

Not every Klaviyo account qualifies for a dedicated IP. Learn more about [dedicated IP addresses](https://help.klaviyo.com/hc/en-us/articles/7675517826587) and how to set one up for your account if applicable.

****Click tracking domains with SSL****

When a Klaviyo user sends an email with a link, the link goes through Klaviyo's domain to enable click tracking for your email. By default, Klaviyo uses a shared domain for click tracking, but it is a best practice to set up [dedicated click tracking](https://help.klaviyo.com/hc/en-us/articles/7676795223707). Dedicated click tracking is beneficial because it allows your customers to further trust the emails that come from your brand as links will be easily recognizable. Instead of a long string of letters and numbers from a Klaviyo encoded link (i.e., **trk.klaviyomail.com** or **trk.klclick.com**), they will see your brand’s name when hovering over links in your email. This can increase the chances that they will click on your links.

![Example of an email that shows when hovering over links as klaviyo link tracking](https://klaviyo.zendesk.com/hc/article_attachments/28711702864539)

Additionally, many mailbox providers and filtering softwares consider the reputation of all the domains used in your messaging. Using the same root domain in both your dedicated click tracking links and your sending domain creates alignment across your brand and causes your sends to look more trustworthy to inbox providers.

Learn more about [dedicated click tracking](https://help.klaviyo.com/hc/en-us/articles/7676795223707).

****Email authentication****

“[Email authentication](https://help.klaviyo.com/hc/en-us/articles/4402601857307)” refers to the technical standards that allow for the verification of an email sender's identity. The most commonly used email authentication standards are SPF and DKIM. DMARC is also a common security protocol that depends on these authentication methods. Mail servers use these authentication protocols to verify that incoming emails are from legitimate senders, protecting your brand and your customers from malicious actors. In addition to preventing phishing and spoofing attempts, implementing these protocols can help improve deliverability, as mailbox providers will be able to confirm the identity of the sender.

When you send from a shared sending domain, the domain already has SPF and DKIM records set. Similarly, when you set up a branded sending domain, the CNAME or NS records Klaviyo provides will fulfill DKIM and SPF requirements.

However, setting up DMARC is both a best practice for deliverability, and a requirement for some inbox providers like Google and Yahoo.

Learn more about [email authentication](https://help.klaviyo.com/hc/en-us/articles/4402601857307) and how to set it up for your domain.

## List acquisition

List acquisition refers to how to get subscribers and keep them. Building a list of valuable subscribers allows you to send to recipients that are genuinely interested in your brand and contact, leading to strong deliverability performance.

The best practices that you should follow in order for your list acquisition strategies to be a success are:

****Avoid purchasing lists****

Purchasing lists is not only against Klaviyo’s [acceptable use policy](https://www.klaviyo.com/legal/acceptable-use-policy), but leads to contact lists full of unengaged profiles that won’t engage with your sends and are more likely to mark your emails as spam. Profiles from purchased lists are a threat to your deliverability, and are unlikely to convert to customers.

Additionally, avoid the following practices:

- Renting lists
- Email affiliate marketing
- 3rd party party opt-in
- Sending to lists previously suppressed due to lack of engagement

****Use signup resources****

Klaviyo’s [sign-up forms](https://help.klaviyo.com/hc/en-us/articles/360026474752) are a great way to organically acquire new subscribers that have provided consent and a clear indication that they are interested in receiving communications from your brand.

Before you start building your sign-up form, consider your goals. A form can help you connect with potential customers, learn more about your audience, convert email subscribers to SMS subscribers, and more.

A simple popup that collects contact information from those who have visited your site, but never subscribed is a great place to start.

Additionally, make sure to:

- Make your value proposition clear
- Minimize the number of fields you use
- Let people choose their interests
- Create a [welcome series](https://help.klaviyo.com/hc/en-us/articles/115002775172) to set expectations

Learn more about [getting started with Klaviyo’s sign-up forms](https://help.klaviyo.com/hc/en-us/articles/360026474752).

****Secure forms****

To prevent invalid emails from form submissions accumulating on your lists, it is best practice to enable [double-opt](https://help.klaviyo.com/hc/en-us/articles/115005251108) in on your lists. Double opt-in is a process through which a new subscriber must confirm their subscription before being subscribed to a given list.

When you add a signup form to your site, you are not able to control who decides to take advantage of this form. Even if you add an extra level of validation, it isn’t always possible to ensure subscribers only submit valid or accurate email addresses and phone numbers. Well-intentioned subscribers could simply type their email or phone number incorrectly, but spam-bots could also find your form and flood it with fake email addresses or phone numbers.

Learn how to enable [double opt-in](https://help.klaviyo.com/hc/en-us/articles/115005251108) in Klaviyo.

****Nurture new subscribers****

Once you convert a potential customer into a subscriber, it is important to make use of a [welcome flow](https://help.klaviyo.com/hc/en-us/articles/115002775172) that initially onboards a customer to your email marketing program, and sets expectations. It is also common to include a discount as an incentive to sign-up for your emails.

Beyond email marketing, some methods to nurture your relationship with customers are:

- Social media ads
- Website affiliate marketing
- [Re-engage](https://help.klaviyo.com/hc/en-us/articles/115000931551) subscribers
- Increase search engine rankings through blogging

These methods can help nurture your relationship with your customers outside of consistent email communications, and can help increase the value and length of a customer’s lifecycle. Additionally, consider sending personalized communications at key moments in a customer’s lifecycle.

## Warming

Warming refers to the process of introducing a new or “cold” IP (i.e., an IP address that has not been used to send emails in the last 30 days) or new or “cold” root domain (i.e., a domain that has been registered in the last 30 days or has never been used to send emails). Warming is the period of time in which you are establishing a reputation as a legitimate or “good” email sender. This is an essential process when sending on new infrastructure, as sending too many emails before your infrastructure is warmed can cause deliverability issues.

****New customer warming****

As a new customer on Klaviyo, it is important to go through the [warming process](https://help.klaviyo.com/hc/en-us/articles/360025945671) to establish yourself as a good sender and have good deliverability.

Some warming best practices that are important to keep in mind as you warm are:

- ****Start slow****
  Start with a low volume of mail and slowly increase sends over time.
- ****Send consistently****
  Regularly send emails and sustain email volume day to day to keep the domain “warm” and build reputation faster****.****
- ****Email your best contacts first****
  Every positive engagement during the warming process benefits the sender’s reputation. Focus on sending high-quality mail to contacts who have recently engaged with email as they are more likely to open and click future messages.
- ****Monitor closely****
  Keep an eye on your deliverability performance throughout warming to quickly identify drops in engagement so you can adjust as necessary.

Additionally when warming, make sure to take the following actions:

- Suspend any 3rd-party affiliate marketing
- Suspend high-risk flows (e.g., sunset flows, winback flows, re-engagement flows)
- Clean up outdated subscriber lists and suppress unengaged profiles.
- Create and send only to engaged segments
- Follow [daily, weekly, and monthly sending plans](https://help.klaviyo.com/hc/en-us/articles/360037527052)
- Remove/import a suppression list of profiles that have previously bounced, unsubscribed, or marked an email as spam

Learn more about the [different warming processes](https://help.klaviyo.com/hc/en-us/articles/360025945671) in Klaviyo.

****Brand change warming****

Warming your sending infrastructure is a required step after renaming your sending domain. Even though you will still use the same Klaviyo account, inbox providers treat each new domain as an entirely separate entity. If you do not ease back into sending, you will risk damaging your deliverability. Prior to updating your domain name, review our guide on [understanding which warming process to use in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/360025945671) to make sure you are prepared for the warming process as soon as this change is in place.

If you are moving to a newly registered domain or have been sending with Klaviyo less than 30 days, you will need to warm your infrastructure. If you are an existing account with a 30-day send history and prior sends on the new domain you are moving to, you do not need to rewarm.

## Monitoring deliverability

In order to improve upon and maintain good deliverability, it is essential to continually monitor your email performance with Klaviyo. This allows you to solve issues quickly to avoid lasting deliverability problems. The best way to do so is to monitor your campaign and flow opens, clicks, bounces, and spam rates.

For complete information on how to do so, head to our article on [how to monitor deliverability performance](https://help.klaviyo.com/hc/en-us/articles/115000201131).

****Inboxing****

Klaviyo does not have any visibility towards how inbox providers like Gmail and Yahoo sort an email once it has been delivered. However, there are several factors that can be used as an indicator of whether your campaigns are landing in recipients’ main inbox or or in the spam folder.

Some key metrics to keep an eye on, including any significant drops compared to previous campaigns, include:

- Open rates
- Conversion rates
- Click rates

If you are seeing healthy engagement rates, it is likely customers are receiving your emails in their main inbox. However, low engagement rates may be an indicator that your [emails are going to spam](https://help.klaviyo.com/hc/en-us/articles/12034571748251).

****Delivery****

A "bounce" occurs when an email is either not successfully delivered or is rejected by the recipient's inbox provider. If your account has a high number of bounces, this can have a negative impact on your deliverability and sender reputation and cause inbox providers to send your emails to spam rather than to a recipient’s main inbox. High bounce rates signal to inbox providers that the sender does not regularly clean their list or follow deliverability best practices. It is crucial to be on the lookout for increases in bounce rates so that you can quickly resolve the issues before it becomes a larger problem.

There are two types of bounces:

- ****Hard bounces****
  Klaviyo defines a hard bounce as an email that cannot be delivered because the address is not valid. This could be caused by a variety of reasons, including a misspelled email. Klaviyo automatically suppresses any email address that hard bounces.

- ****Soft bounces****
  A soft bounce is always caused by a temporary reason, such as when a recipient's inbox is full or when their email server is momentarily down. If an email soft bounces 7 consecutive times, Klaviyo will suppress this address.

To monitor bounce rates, you can use the email deliverability hub in Klaviyo. The Bounce details page on the deliverability hub provides information around why your sends are bouncing. If you are seeing issues with bounces, you can analyze this data to take corrective action and improve your overall email deliverability. In the Bounce details section, you can see the following data:

- ****Top bounce categories****
  The **Top bounce category** card provides information about the types of bounces you are experiencing and volume for each category.
  ![Bounce categories report in deliverability hub](https://klaviyo.zendesk.com/hc/article_attachments/28711702856219)
- ****Bounce report****
  The **Bounce report** card shows a further breakdown of the bounces on your account.
  ![Bounce report in deliverability hub](https://klaviyo.zendesk.com/hc/article_attachments/28711731847451)

Learn more about how to monitor and troubleshoot [bounce rates](https://help.klaviyo.com/hc/en-us/articles/115005250408) in Klaviyo.

****Reputation****

Sender reputation refers to the trustworthiness of your brand as an email sender. Inbox providers determine your sender reputation based on multiple differently weighted factors, and consider this when sorting emails in a customer’s inbox. Senders with a positive sender reputation are more likely to have their emails delivered into customers’ inbox, while senders with a poor sender reputation are likely to see their emails placed into spam or not delivered at all. For these reasons, it is critical to maintain a strong sender reputation to be successful with email marketing and Klaviyo.

You can monitor your sender reputation in Klaviyo using the score shown in Klaviyo’s deliverability hub. The deliverability hub in Klaviyo allows you to analyze and diagnose your email and SMS deliverability health at the account level.

![Deliverability score in Klaviyo's deliverability hub](https://klaviyo.zendesk.com/hc/article_attachments/28711731858203)

Learn more about [sender reputation](https://help.klaviyo.com/hc/en-us/articles/15332906406171) and [Klaviyo’s deliverability hub](https://help.klaviyo.com/hc/en-us/articles/18378819907995).

****Key metrics****

The metrics that come together to determine your overall deliverability performance and show how successfully you reach your subscribers’ inboxes are:

### Open rates

Open rates refer to how many of your recipients are opening the emails they received. It is best practice to maintain open rates of at least 33%, regardless of your industry.

If you are seeing low open rates, it indicates that customers are generally not interested in the content you are sending, or you are sending to unengaged contacts that are unlikely to engage with your emails.

To help help increase open rates, try the following strategies:

- Create engaged segments
- Create targeted subject lines
- Clean your lists regularly
- Choose the right send time
- Continue to monitor performance

Learn more about how to [increase open rates](https://help.klaviyo.com/hc/en-us/articles/360042454031) and see more details about these key steps.

### Click rates

Click rates refer to how many of your recipients are actually clicking a URL in the emails they receive. It is best practice to maintain click rates of at least 1%, regardless of your industry.

If you are seeing customers open your emails, but are failing to click through, it indicates that customers may not have any incentive to click or the email design does not help to drive clicks.

To help help increase open rates, try the following strategies:

- Use segmentation to drive better personalization, and send content that is relevant for your different audiences.
- Use a clear call to action (CTA) so it is clear to recipients where they should click.
- Test different CTA’s to determine what works best for your audience.
- Drive recipients to your site.
- Include a CTA that offers something special for following you on social media or clicking through to your site.

Learn more about how to [increase click rates](https://help.klaviyo.com/hc/en-us/articles/360057459931).

### Bounce rates

A [bounce](https://help.klaviyo.com/hc/en-us/articles/115005250408) occurs when an email is either not successfully delivered or is rejected by the recipient's inbox provider. If your account has a high number of bounces, this can have a negative impact on your deliverability rate. It is best practice for bounce rates to stay below 1.0%.

There are several possible reasons why an email address may hard or soft bounce, including:

- Content
- Message length
- Message size
- Frequency or volume too high
- Reputation
- Invalid address
- Mailbox unavailable
- Technical

Some key strategies to decrease bounce rates include:

- Emailing real, consented profiles
- Enabling [double opt-in](https://help.klaviyo.com/hc/en-us/articles/115005251108)
- [Cleaning your lists](https://help.klaviyo.com/hc/en-us/articles/115005078347) regularly
- Removing profiles that soft bounce

Learn more about [decreasing bounce rates](https://help.klaviyo.com/hc/en-us/articles/360057036052) and [why emails bounce](https://help.klaviyo.com/hc/en-us/articles/115005250408).

### Unsubscribe rates

Unsubscribe rates refer to how many your recipients unsubscribe from further messaging from your brand after receiving an email. While it is important to give users the opportunity to easily unsubscribe, if too many people are unsubscribing, inbox providers may view this as a red flag. It is best practice to maintain unsubscribe rates under 0.3%.

If you are seeing elevated unsubscribe rate, it indicates that customers may be losing interest in your content due to a lack of value or content that does not meet their expectations, or they are receiving too many emails from your brand and are overwhelmed.

Some key strategies to decrease unsubscribe rates include:

- Set expectations upon signing up with a [welcome series](https://help.klaviyo.com/hc/en-us/articles/115002775172).
- Serve personalized content through segmentation.
- Provide value other than offers (e.g., educational content or humor that is relevant for your audience).

Learn more about how to [decrease unsubscribe rates](https://help.klaviyo.com/hc/en-us/articles/360057471831).

### Spam complaint rates

Spam complaint rates refer to how many people are reporting your messaging as spam. It is best practice to maintain spam complaint rates below 0.01%.

If you are seeing elevated spam complaint rates, it indicates that customers may be losing interest in your content due to a lack of value and content that does not meet their

expectations, or they are receiving too many emails from your brand and are overwhelmed.

Some key strategies to decrease spam complaint rates include:

- Make the unsubscribe method clear and easy to understand.
- Set clear expectations upon sign up so customers know what they signed up for.
- Ramp down sending frequency as recipients stop engaging.

Learn more about how to [decrease spam complaint rates](https://help.klaviyo.com/hc/en-us/articles/360057985791).

## Testing

Testing your content and is an important part of deliverability to identify content related spam triggers, and identify what content performs best with your audience to maintain high engagement rates and good deliverability.

****Content testing****

Testing your email content is the best way to find the content that is causing messages to go to the spam folder or being blocked when you have ruled out all other factors or it is only occurring on a specific message and no others is to do testing.

Learn how to [test your email content to identify spam triggers](https://help.klaviyo.com/hc/en-us/articles/25617578366491).

****Open rate and subject line testing****

Subject lines are the first part of your email that customers will see in their inbox, and can be the difference between customers opening your emails or not. Testing different subject lines to see the impact on open rates is a good practice to determine the subject lines that work best for your different audiences.

In Klaviyo, you can use A/B tests for [flow emails](https://help.klaviyo.com/hc/en-us/articles/6960371049115) and [campaigns](https://help.klaviyo.com/hc/en-us/articles/115005228148) to test different subject lines and measure their success. A/B testing can provide valuable insight into your audience, and Klaviyo makes it simple to determine what subject lines you should use in your sending. Not only will you know the winning variation for an A/B test, but also other important factors, like the win confidence percentage and winning metric details.

Learn how to A/B test [flow emails](https://help.klaviyo.com/hc/en-us/articles/6960371049115) and [campaigns](https://help.klaviyo.com/hc/en-us/articles/115005228148).

## Sending

Your sending practices are key to maintaining good deliverability and a positive sender reputation that allows you to land in customer inboxes.

Below are some of the key elements related to your sending that are most impactful towards your overall success:

****Blocklists****

A blocklist is a list of items, such as IP addresses, domain names, URLs, or usernames that are denied access to a certain system protocol. Email blocklists are real-time databases that use multiple criteria to determine if an IP is sending emails considered to be spam. There are blocklists for both IP addresses and domains that can severely impact reputation and deliverability. This is also known as a blacklist.

Blocklists can have different deliverability impacts based on the particular inbox provider. Gmail for example does not rely on blocklists, and uses Google’s own systems to evaluate sender reputation. However, other inbox providers may consider SpamHaus, as well as SORBS and SpamCop to a lesser extent. Any other blocklists are not relied upon by major inbox providers and will have little to no impact on deliverability.

Klaviyo closely monitors SpamHaus listings as this is the blocklist that can have the most impact on deliverability. SORBs and SpamCop are also monitored, but have much lower impact.

****Spam filtering****

Klaviyo is responsible for sending your emails, but once these emails are in the hands of the inbox provider (i.e. Gmail or Yahoo), the messages are filtered according to each provider’s rules. All inbox providers have a built-in system that scans incoming emails, and automatically sorts them using complex algorithms that are not made public.

Following email deliverability best practices is key for inbox providers to sort your emails into a recipient’s main inbox instead of the spam folder. Emails that go to spam are highly unlikely to be viewed by a recipient, and can negatively impact your revenue and success with Klaviyo.

If you are seeing emails go to spam, see our guide on [troubleshooting why emails go to spam](https://help.klaviyo.com/hc/en-us/articles/12034571748251).

****Inbox folders****

With [Gmail's tabbed inbox](https://help.klaviyo.com/hc/en-us/articles/115005078307), emails can land in any of the following tabs: **Primary**, **Social**, **Promotions**, **Updates**, or **Forums**.

Gmail's algorithms are designed to make it easier for users to sort through an otherwise crowded inbox, so important emails have high visibility. For email marketers, this can seem problematic if Gmail starts sorting your emails into a tab where they may be ignored.

[Studies done](https://returnpath.com/wp-content/uploads/2015/02/Return_Path_-_The_Tabbed_Inbox.pdf) on the topic show that open rates for marketing emails landing in the **Promotions** tab did not experience a rapid decline and the observable change was slight. In fact, marketers might even be better off because emails that now find a safe place in the **Promotions** tab may have otherwise been blocked or filtered to the spam folder prior to Gmail's tabbed inbox.

Gmail users themselves can alter the default sorting system by moving an email from one tab to another and electing to have Google always put messages from a specific sender in the tab of their choice. If this is important to you, you can make an appeal to your audience by asking them to drag your newsletters over to their **Primary** tab for easy access to your brand messaging. You cannot, however, pre-determine which tab your messages will fall into and Klaviyo has no control over inbox placement after an email is successfully delivered.

Typically, if emails are personalized, they will automatically be sorted in the Primary inbox. Fewer personalized emails tend to end up in the **Promotions** tab. Gmail's **Promotions** tab is truly designed to catch marketing emails, so consider the following:

- ****Watch your text to image ratio****
  Taking an image-heavy approach to email design can impact inbox placement. Spam filters are also suspicious of emails composed mostly of images.
- ****Avoid overuse of links****
  Avoid too many links in your emails and make sure no links are broken.
- ****Personalize****
  Klaviyo makes it easy to personalize your emails. For example, insert a first name into an email with a fallback if you don't have a name on file.

While there is no way to see which tab your emails are going to, 3rd party tools like [Litmus](https://www.litmus.com/) can help with testing as well.

****Transaction vs. marketing****

[Transactional emails](https://help.klaviyo.com/hc/en-us/articles/360003165732) are emails that a customer must receive in response to an action that they took. For example, an order confirmation message with details about an order the customer just placed.

While both transactional and marketing emails can be sent in response to an action a customer took, it is important to differentiate between the two. Generally, a trigger-based email that aims to relay essential information to the customer, rather than generating sales, can be considered a transactional email.
Common transactional emails include:

- Order confirmation
- Shipping confirmation
- Account created confirmation

Triggered emails that are not considered transactional emails include:

- Welcome series
- Abandoned cart
- Back in stock notifications

Another key distinction between marketing and transactional emails is the fact that transactional emails are not tied to whether or not someone has subscribed. Even if a customer has unsubscribed from marketing emails, they would still expect to receive transactional messages around orders or administrative account activity. Because of this, emails marked as transactional in Klaviyo will still be sent to suppressed recipients.

Learn more about [transactional emails](https://help.klaviyo.com/hc/en-us/articles/360003165732) in Klaviyo.

****Spam traps****

[Spam traps](https://help.klaviyo.com/hc/en-us/articles/360015537111) are fake email addresses that live on the web for the purpose of finding people who may be illegitimately acquiring contacts. Internet Service Providers (ISPs) flag a domain if it sends to a higher percentage than normal. Eliminating your risk of sending to spam traps will increase your likelihood of reaching the inbox, leading to more opens, clicks, and ultimately, more money. Klaviyo leverages this fact to identify any spam traps on your list or any other profiles in your account that have never engaged with your brand.

Inbox providers use spam traps to identify which emails they should place in the spam folder. In their eyes, sending to a spam trap is a sign that a sender is not obtaining emails legitimately and is not following email best practices.

Learn how to [identify and remove spam traps](https://help.klaviyo.com/hc/en-us/articles/360015537111) from your account.

## List hygiene

List hygiene is key for good deliverability, as it ensures that your email list is composed of active, engaged profiles that are more likely to interact with your sends. This ultimately leads to a strong sender reputation, making inbox providers more likely to view you as a good sender and sort your emails into main inboxes instead of spam.

****Re-engagement series****

Re-engaging your subscribers and, if re-engagement fails, removing those subscribers is a critical factor for a successful email program.

Make sure to provide compelling reasons for customers continue, and enforce the following best practices:

- Highlight benefits
- Include testimonials
- Provide opportunity to change email addresses
- Reflect your brand personality

Similarly, you can create a [winback flow](https://help.klaviyo.com/hc/en-us/articles/115002775192) in Klaviyo to nurture customers that have fallen out of their usual buying cycles.

Learn more about running a [re-engagement campaign](https://help.klaviyo.com/hc/en-us/articles/115000931551) in Klaviyo.

****Sunset flows****

A sunset flow is designed to phase out customers who are no longer engaging with your brand. You can use this flow as a last-ditch effort to win back their business, and then delete or suppress anyone who is not responsive. This will help you maintain a clean list and avoid having inactive customers contribute towards your Klaviyo billing plan, ultimately maximizing the value you get from your active profiles.

Learn how to [create a sunset flow](https://help.klaviyo.com/hc/en-us/articles/360017518492) in Klaviyo.

****Engagement based frequency sending****

Using a sending schedule based on email engagement is key to achieving strong open rates and maintaining a positive relationship with your subscribers. Sending too often to unengaged profiles will hurt your sender reputation, whereas sending too infrequently to engaged customers is leaving money on the table. It's best to achieve a happy medium through the use of segments and sending schedules.

Once you establish your tracks, begin sending campaigns that are targeted and well suited for the segments' specific email habits. You can choose to send email campaigns at the same time to all of the segments with smart sending toggled on, or you can send separate campaigns to each segment. If you choose to do the latter, this will enable you to visualize how much money you made from each campaign, and thus each engagement track.

Learn how to [create a sending schedule based on engagement and frequency](https://help.klaviyo.com/hc/en-us/articles/360037527052).

****Data quality****

Data quality is ensuring that data on your account is accurate, complete, and reliable. Data quality is vital to ensure accuracy in any decision-making process where such data is utilized.

Maintaining high-quality data on your account has the following benefits:

- Avoids problems caused by inaccurate data (duplicate messaging, etc)
- Helps you reach more people (reaching out at the right time to avoid burnout)
- Helps you reach the right people (provide relevant information to your subscribers)
- Improves customer relationships (quality data helps you understand your subscribers needs)

## Additional resources

[Understanding email deliverability](https://help.klaviyo.com/hc/en-us/articles/115005247008)

[Deliverability glossary](https://help.klaviyo.com/hc/en-us/articles/360039295051)

[Frequently asked questions about deliverability](https://help.klaviyo.com/hc/en-us/articles/16425927010075)