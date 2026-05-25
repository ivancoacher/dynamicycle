---
id: "8983758025883"
title: "How to repair your sender reputation"
source_url: "https://help.klaviyo.com/hc/en-us/articles/8983758025883-How-to-repair-your-sender-reputation"
section: "Deliverability best practices and tools"
category: "Deliverability & compliance"
category_slug: "deliverability-compliance"
klaviyo_updated: "2026-05-11T12:54:45Z"
language: "en"
---
## You will learn

Learn steps you can take to repair your sender reputation if you are facing email deliverability issues and seeing a dip in performance. Sender reputation refers to your ability to successfully land in your customers' inboxes.

## Disable lower-engagement flows

[Winback](https://help.klaviyo.com/hc/en-us/articles/115002775192), [re-engagement](https://help.klaviyo.com/hc/en-us/articles/115000931551), and [sunset](https://help.klaviyo.com/hc/en-us/articles/360017518492) flows can be riskier flows to have enabled if you are working to improve your sender reputation, as they typically see lower engagement rates. It is not recommended to have these flows enabled when you are repairing your sender reputation. If you have these flows active, you can [set them to draft mode](https://help.klaviyo.com/hc/en-us/articles/360048376172) during the repair process.

## Discontinue any 3rd party marketing

While repairing your sender reputation, you’ll want to discontinue any 3rd party marketing being done for your brand, whether it is through Klaviyo or another marketing group or ESP.

Klaviyo gives you everything you need to collect, analyze, and build campaigns or flows using first-party data collected through straightforward methods like forms for email address capture.

## Send following the appropriate re-warm schedule

When repairing your sender reputation, it is important to make sure you are contacting the right engagement cohort based on your preferred sending frequency. Keep in mind the frequency does not include flows that are sent in response to an action taken by the subscriber.

Select the appropriate schedule for your sending frequency to determine the timeframe and count of engagements on your [engaged segments](https://help.klaviyo.com/hc/en-us/articles/115000200072). You’ll want to avoid going beyond the recommended engagement window for your sending frequency.

The structure of the segment will remain the same for all the options, based on the number of clicks or opens within the relevant engagement window:

![Structure for segment to repair sender reputation](https://klaviyo.zendesk.com/hc/article_attachments/28720671460251)

****If you send daily****

****Week 1****

Send to very highly engaged users with 5 or more engagements in the last 30 days

****Week 2****

Send to highly engaged users with 3 or more engagements in the last 30 days

****Week 3****

Send to engaged users with 1 or more engagements in the last 30 days

****If you send 3 times per week****

****Week 1****

Send to very highly engaged users with 5 or more engagements in the last 60 days

****Week 2****

Send to highly engaged users with 3 or more engagements in the last 60 days

****Week 3****

Send to engaged users with 1 or more engagements in the last 60 days

****If you send 2 times per week****

****Week 1****

Send to very highly engaged users with 5 or more engagements in the last 90 days

****Week 2****

Send to highly engaged users with 3 or more engagements in the last 90 days

****Week 3****

Send to engaged users with 1 or more engagements in the last 90 days

****If you send weekly****

****Week 1****

Send to very highly engaged users with 5 or more engagements in the last 180 days

****Week 2****

Send to highly engaged users with 3 or more engagements in the last 180 days

****Week 3****

Send to engaged users with 1 or more engagements in the last 180 days

****If you send monthly****

****Week 1****

Send to very highly engaged users with 5 or more engagements in the last 275 days

****Week 2****

Send to highly engaged users with 3 or more engagements in the last 275 days

****Week 3****

Send to engaged users with 1 or more engagements in the last 275 days

Going forward, if you do see a drop in opens again, you’ll need to go back to sending to highly or very highly engaged users immediately to repair your reputation again.

## Remove unengaged subscribers

When repairing your sender reputation, it is important to [identify your least engaged email subscribers](https://help.klaviyo.com/hc/en-us/articles/360044054732) so you can avoid contacting them. Once you've identified your unengaged subscribers, consider excluding them from your marketing initiatives, or [suppressing](https://help.klaviyo.com/hc/en-us/articles/115005073867) them during list cleaning.

Additionally, confirm all subscribers that have not opened or clicked a message in 365 days have been archived from their list, and do not send to them unless they resubscribe. Never attempt to re-engage subscribers after 365 days of non-engagement.

## Setup dedicated infrastructure

### Branded sending domain setup and warming

A [branded sending domain](https://help.klaviyo.com/hc/en-us/articles/7674941873947) (also known as a dedicated sending domain) allows you to send emails that appear to be coming from your brand and have better overall control of your sender reputation. It also allows you to build a sending reputation on your domain to limit any negative impact to your deliverability from other senders on a shared domain.

If you are on a new Klaviyo account starting with a branded sending domain, or are setting up a newly registered domain (registered within the last 30 days), it is essential to [warm your sending infrastructure](https://help.klaviyo.com/hc/en-us/articles/360025945671) in the first 2 to 4 weeks after applying your sending domain. Warming your domain strengthens your sender reputation. Depending on what data you are bringing over to Klaviyo and the use cases you have, you will need to follow the warming or platform introduction process applicable to you.

### Dedicated IP

Most small businesses or those just starting out with Klaviyo will be on shared IPs. Depending on your email practices and volumes, a shared IP should suffice for your sending and reputation needs. However, if you use a [dedicated IP address](https://help.klaviyo.com/hc/en-us/articles/7675517826587), the associated sender reputation will only be influenced by the single account that is using it. As such, you have complete control over your email sender reputation, especially if you have higher volumes of email. Relatedly, a dedicated IP address gives you complete control over sending volumes, so you will not be affected by potential volume spikes on a shared IP during busy times of year. In addition, if you encounter deliverability issues, you can more easily pinpoint the root causes with a dedicated IP address.

### Dedicated click tracking

[Dedicated click tracking](https://help.klaviyo.com/hc/en-us/articles/360001550572-How-to-Set-Up-Dedicated-Click-Tracking) allows you to display your own domain on click tracking links rather than the default Klaviyo encoding.

This is beneficial because it allows your customers to further trust the emails coming from your brand, as the links will be easily recognizable. Instead of a long string of letters and numbers from a **trk.klaviyomail** encoded link, they will see your brand’s name when hovering over links in your email. This can increase the chances that they will click on your links.

It is also good practice to set up [SSL for dedicated click tracking](https://help.klaviyo.com/hc/en-us/articles/360052205052), so you can secure and authenticate your own domain for tracking clicks.

## Domain alignment

If the root domain used in your sender email address (i.e friendly-from address), does not align with the root domain used in the branded sending domain, this can impact inbox placement.

[DMARC](https://help.klaviyo.com/hc/en-us/articles/4402601857307) is a protocol designed to give domain owners the ability to protect their domain from unauthorized users sending emails, commonly known as email spoofing.

Misalignments typically impact accounts using Klaviyo’s default shared sending domain to send emails that have a from-address domain with a DMARC policy on it. You’ll want to make sure that there is alignment between your sending domain, and your from-address in Klaviyo. For example, if you send an email using **sales@example.com** as the from-address, where **example.com** is protected by DMARC, your account will need to use a branded sending domain like **send.example.com** for all emails sent from Klaviyo to meet DMARC authentication requirements. That said, accounts with branded sending domains may also be impacted if there is not alignment with the sender email address.

Without DMARC your brand is more vulnerable to email fraud, but it is important to ensure alignment to prevent deliverability issues.

## BIMI

If your brand has a DMARC policy, you can also set up [BIMI](https://bimigroup.org/) (Brand Indicators for Message Identification). BIMI uses your DNS settings to authenticate your visual brand identity in emails you send. Implementing this technology can increase brand recognition, legitimize your business, and boost deliverability by building trust with your recipients and improving engagement rates. For information regarding how to configure this, see our guide [about BIMI.](https://help.klaviyo.com/hc/en-us/articles/4406592127515)

## Monitor performance

As you continue to send to subscribers after completing the warming, you’ll want to [monitor your performance for key email metrics](https://help.klaviyo.com/hc/en-us/articles/115000201131) to make sure your sending audience is engaged and you are maintaining good deliverability.

You can compare the performance of your own sends against key ranges for these metrics. If you find that your performance is declining or needs improvement, you can adjust your strategy accordingly.

If you are not seeing an improvement after 4 weeks, please reach out on our [Community](https://community.klaviyo.com/) or to our [Support Team.](https://help.klaviyo.com/hc/en-us/articles/115001002272)