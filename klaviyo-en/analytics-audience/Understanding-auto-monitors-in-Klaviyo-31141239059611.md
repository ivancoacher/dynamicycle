---
id: "31141239059611"
title: "Understanding auto-monitors in Klaviyo"
source_url: "https://help.klaviyo.com/hc/en-us/articles/31141239059611-Understanding-auto-monitors-in-Klaviyo"
section: "Getting started with Klaviyo reporting"
category: "Analytics"
category_slug: "analytics-audience"
klaviyo_updated: "2026-04-21T13:54:38Z"
language: "en"
---
## You will learn

Learn about auto-monitors in Klaviyo. Klaviyo automatically monitors your account performance for anomalies with key objects such as flows and campaigns. This allows you to quickly identify and resolve performance issues before they have larger implications.

## Before you begin

If you are an [Advanced KDP](https://help.klaviyo.com/hc/en-us/articles/17655007276059) customer, you also have access to the [custom monitors](https://help.klaviyo.com/hc/en-us/articles/27160071187739) functionality.

## Available auto monitors

Klaviyo automatically monitors the following objects in your account to alert you about the following performance issues:

- ****Flow triggers****
  Anomalies in the number of events associated with metric-triggered flows (i.e., a drop in the number of times a flow is triggered).
- ****Flow messages sent****
  Anomalies in the number of messages sent in a flow (i.e., a drop in the number of emails, SMS, or push notifications sent by a flow).
- ****Deliverability rates per email provider for campaigns****
  Anomalies in bounce rates associated for each inbox provider (e.g., Gmail and Yahoo). Note that only bounces due to content or reputation issues are monitored.

Flow objects are checked every 24 hours, and campaign deliverability monitors are visible for 3 days after sending.

## Monitor alerts

To view your auto-monitors, navigate to ****Account**** > ****Settings**** > ****Monitors**** in the bottom-left corner of your account.

![Monitors tab on Settings page](https://klaviyo.zendesk.com/hc/article_attachments/31528813661595)

If you are an Advanced KDP customer, you can view both your custom monitors and auto-monitors on the same page.

### Monitors list

On the main **Monitors** page, you’ll see a list view of your existing auto-monitors. Next to each auto-monitor, you’ll see the following information:

- ****Monitor name****
  The name of the Klaviyo object being monitored (i.e., the flow, campaign, or segment).
- ****Status****
  The status of the auto-monitor. These can be:
  - ****Active****
    The monitor is enabled and an alert was not triggered during the previous check.
  - ****Alert****
    The monitor is enabled and the alert was triggered during the previous check. The next check will be in 24 hours.
- ****Monitor type****
  The monitor type itself (e.g., flow trigger, flow messages sent, campaign deliverability).
- ****Alert rule****
  A preview of the alert rule set for the associated monitor. This will show the metric being monitored and whether there was a deviation from the expected number of events.
- ****Notifications****
  Notifications for auto-monitors are always enabled.

![Auto-monitors list](https://klaviyo.zendesk.com/hc/article_attachments/31528813666587)

### Monitor summary

If you click into a monitor on the list view, you will be brought to the **Monitor summary**, where you can find more information about the monitor. You’ll see:

- ****Description of key information****
  A summary of the key details of the monitor.
- ****Metric preview****
  A preview of the metric over time that can be grouped by day, week, or month.
- ****Activity log****
  A timeline of the most recent alerts created by your monitor.

![](https://klaviyo.zendesk.com/hc/article_attachments/31529635552667)

### Alert log

To view logs of alerts sent through auto-monitors, select the ****Alert log**** button.

![Monitor summary](https://klaviyo.zendesk.com/hc/article_attachments/31528813668379)

Here, you can see a timeline of the alerts that were triggered for your auto-monitors. If you expand an event on the alert log timeline, you can see more information about the alert, including:

- The Klaviyo object with the anomaly that triggered the alert
- The associated metric
- The rule that was broken resulting in the alert

![Alert log page](https://klaviyo.zendesk.com/hc/article_attachments/31528861612699)

### Notifications

By default, the **Owner**, **Admin**, **Manager**, and **Analyst** user roles will receive [notifications on Klaviyo’s home page](https://help.klaviyo.com/hc/en-us/articles/360049968412).

Additionally, the account owner will receive email notifications regarding alerts from auto-monitors.