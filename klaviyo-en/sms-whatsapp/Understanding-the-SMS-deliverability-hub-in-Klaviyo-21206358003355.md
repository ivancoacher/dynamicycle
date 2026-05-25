---
id: "21206358003355"
title: "Understanding the SMS deliverability hub in Klaviyo"
source_url: "https://help.klaviyo.com/hc/en-us/articles/21206358003355-Understanding-the-SMS-deliverability-hub-in-Klaviyo"
section: "SMS deliverability best practices"
category: "SMS"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-21T13:54:33Z"
language: "en"
---
## You will learn

Learn about Klaviyo’s account-level SMS deliverability reporting. The **SMS** tab in Klaviyo’s deliverability hub is a centralized space that allows you to analyze and diagnose your SMS deliverability health across all your sends.

## The account deliverability hub

The **Deliverability** hub in Klaviyo allows you to analyze and diagnose your email and SMS deliverability health at the account level.

To access the page, navigate to the **Deliverability** tab under **Analytics**.

![SMS hub interface in Klaviyo](https://klaviyo.zendesk.com/hc/article_attachments/28723546085915)

To analyze your SMS deliverability, select the ****SMS**** tab.

## SMS deliverability hub content

### Filters

At the top of the deliverability hub’s **SMS** tab, you can set filters that apply to all the SMS reports.

![Available filters in the SMS deliverability hub](https://klaviyo.zendesk.com/hc/article_attachments/28723546098331)

The following filters are available:

- Last 7 days
- Last 30 days
- Last 90 days
- Custom

- Time period
- Message type (i.e., campaign or flow)
- Message format (i.e., SMS, MMS, or both)

### Alerts

The **Alerts** section is a collapsable card that appears when an SMS deliverability issue has been identified on your account. Each alert indicates a key deliverability metric is experiencing poor performance, and provides details about the issue with a link to a troubleshooting guide for resolution steps.

Alerts are based on data from the last 7 days.

You’ll see alerts in the following situations:

- **Device Disconnected** failures exceed 5% of the total send
- **Device Unreachable** failures exceed 5% of the total send
- **Carrier Violation** errors exceed 10% of the total send
- **Message Blocked** errors exceed 5% of the total send
- **Device Incapable of Receiving SMS** errors exceed 5% of the total send
- **Toll Free Number not registered** / **Number not Verified**
- **Unknown errors** exceed 10% of the total send
- Click rate below 6.0%
- Unsubscribe rate above 1.3%

![SMS deliverability alerts](https://klaviyo.zendesk.com/hc/article_attachments/28723524156827)

Learn more about the different [SMS failure reasons and how to resolve them](https://help.klaviyo.com/hc/en-us/articles/360039239172).

### Key metrics

On the **Key metrics** card, you’ll see an overview of the key SMS deliverability health metrics and your performance for each one.

These metrics are:

- Delivery rate
- Fail rate
- Click rate
- Unsubscribe rate

Beneath each metric is a badge showing you how your performance changed since the last time period. Additionally, you can toggle between **Rate** and **Count** to view your metrics as a percentage or a total count.

![Key rates of metrics impacting SMS deliverability score ](https://klaviyo.zendesk.com/hc/article_attachments/28723524142747)

![Key counts metrics impacting SMS deliverability score](https://klaviyo.zendesk.com/hc/article_attachments/28723546078363)

Compare your performance to [Klaviyo’s SMS benchmarks](https://help.klaviyo.com/hc/en-us/articles/360051110111).

### Fail details

The **Fail details** chart provides insight towards why your messages are failing to be delivered to recipients.

You view this information through the segmented bar chart showing the volume of each failure reason.

![Segmented bar chart showing SMS failure reports](https://klaviyo.zendesk.com/hc/article_attachments/28723524149915)

Alternatively, you can toggle the view to the line graph that shows your performance for the different failure reason over time.

![Line graph showing SMS failures in Klaviyo](https://klaviyo.zendesk.com/hc/article_attachments/28723546075931)

### Recent campaigns performance

The **Recent** c**ampaign performance** card shows you the recent SMS campaigns on your account that have the most impact on your overall deliverability.

![Campaign performance report contributing to SMS deliverability](https://klaviyo.zendesk.com/hc/article_attachments/28723546093083)

You can toggle between campaigns that have a **Healthy** status and campaigns that have a **Needs attention** status. The **Healthy** toggle shows the 5 most recent campaigns that have all metrics in a healthy zone. When the **Needs attention** toggle is chosen, the 5 most recent campaigns that have at least 2 metrics in the **Needs attention** range will be shown.

### Flows performance

The **Recent****f****lows performance** card shows you the flows on your account that have the most impact on your overall deliverability.

![Flows performance report contributing to SMS deliverability](https://klaviyo.zendesk.com/hc/article_attachments/28723546089883)

You can toggle between flows that have a **Healthy** status and flows that have a **Needs attention** status. The **Healthy** toggle shows the 5 most recent flows that have all metrics in a healthy zone. When the **Needs attention** toggle is chosen, the 5 most recent flows that have at least 2 metrics in the **Needs attention** range will be shown.