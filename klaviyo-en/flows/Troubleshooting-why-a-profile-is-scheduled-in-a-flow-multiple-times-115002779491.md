---
id: "115002779491"
title: "Troubleshooting why a profile is scheduled in a flow multiple times"
source_url: "https://help.klaviyo.com/hc/en-us/articles/115002779491-Troubleshooting-why-a-profile-is-scheduled-in-a-flow-multiple-times"
section: "Troubleshooting flows"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-04-21T13:56:38Z"
language: "en"
---
## You will learn

Learn how to troubleshoot scenarios where you're seeing the same person queued to receive a flow multiple times. These profiles may have taken the trigger action multiple times. For example, someone could have made multiple purchases in a row or viewed multiple products in the same browsing session.

## Use Smart Sending to limit message frequency

[Smart Sending](https://help.klaviyo.com/hc/en-us/articles/115002779311-Smart-Sending-for-Flows-VFB-), when left enabled, will ensure nobody receives more than one email or SMS in the established Smart Sending period (16 and 24 hours by default, respectively). We highly recommend keeping Smart Sending enabled when your flow is triggered by commonly repeated behavior, like viewing a product or being active on site.

## Use additional filters to limit message frequency

If you want to disable Smart Sending for a flow and are concerned about multiple emails or texts sending to someone in a short period of time, you can also [use an Additional Filter to your message](https://help.klaviyo.com/hc/en-us/articles/115002779091-Add-an-Additional-Filter-to-a-Single-Flow-Email-VFB-) that limits how frequently someone can receive a message from the flow. This filter should be:

**What someone has done or not done > Received email > where > Subject > equals > INSERT\_EMAIL'S\_SUBJECT > Zero times > in the last > X days**

Make sure to replace INSERT\_EMAIL'S\_SUBJECT with the actual subject line of the email, replace X with the number of days you want to use.

![](https://klaviyo.zendesk.com/hc/article_attachments/34263477109019)

## Use profile filters to limit message frequency

Alternatively, you can add a filter to the entire flow to limit how frequently someone will enter it. To achieve this, add the following profile filter:

**Has not been in this flow > Skip anyone who has been in this flow in the last X days**

![](https://klaviyo.zendesk.com/hc/article_attachments/34263477113115)

Make sure to replace X with the number of days you want to use.

This option is not available for list- and segment-based flows, as they only trigger once per recipient.

## Additional resources

Learn more about flows:

- [How to preview a flow trigger setup](https://help.klaviyo.com/hc/en-us/articles/360028374111)
- [Understanding flow branching](https://help.klaviyo.com/hc/en-us/articles/115003883992)

Learn about [troubleshooting a flow](https://klaviyo.zendesk.com/hc/en-us/articles/115002779471).

Find out more about [Smart Sending in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115002779311).