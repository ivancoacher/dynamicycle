---
id: 115002779351
title: "Understanding flow analytics"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115002779351-Understanding-flow-analytics"
section: "Understand flows"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-04-20T17:29:52Z"
language: en
---

## You will learn

Learn how to review the performance of your Klaviyo flow messages, including open, click, and conversion rates.

There are several ways you can review your flow messages, including the:

- 30-day analytics snapshot
- Visual canvas
- Flow message overview report
- Recipient activity tab
- Link activity tab

In this article, we explain what each of these options are and what they show.

Only Owners, Admins, Managers, and Analysts can view flow analytics. Learn more about Klaviyo's [user roles](https://help.klaviyo.com/hc/en-us/articles/115005231648).

## The 30-day analytics snapshot

When you click on any message card, you will see a snapshot of analytics from the last 30 days in the left-hand sidebar. This snapshot may show some of the fields below, depending on your setup (e.g., the marketing channel used, if a flow is currently live or not, if it's using a custom webhook, etc.).

- ****Waiting****
  If your flow message is scheduled to send after X number of hours/days, this is the number of people waiting to receive the scheduled messages will appear here.
- ****Needs review****
  If your flow message is (or was at some point) in manual mode, this is the total number of people who are ready to receive the message will appear here.
- ****Delivered****
  Here, you can observe the number of people that have received this message in the last 30 days.
- ****Skipped****
  Here, you can see the number of people who were skipped from receiving a message. Typically, this is because they failed the flow's filters at send time.
- ****Open rate**** **(email and push only)********\*******
  The average percentage of unique recipients who opened your message. This is calculated by taking the number of unique individuals who opened your message divided by the number of recipients.
- ****Click rate**** **(email and SMS only)********\*******
  The average percentage of unique recipients who clicked a link in your message. This is calculated by taking the number of unique individuals who clicked your email divided by the total number that received your email.
- ****Conversion rate****
  The average conversion rate for this email over the last 30 days -- by default, this is set to **Placed Order** rate.
- ****Revenue****
  Total revenue attributed to the email over the last 30 days.

Open and click rates for flows are counted as unique rates. Unlike tracking for single campaigns, it's the unique number of total opens or clicks that occurred divided by the number of recipients.

### Apple Mail and tracking

Apple Mail Privacy Protection (MPP), which was released with iOS15 and updates to other Apple devices, may lead to inflated open rates due to changes in how we receive open rate data.

If you are triggering flows off of opens themselves, we suggest creating a [custom report](https://help.klaviyo.com/hc/en-us/articles/4416803987739) that includes an MPP property to review these affected opens. You can also identify these opens in your individual [subscriber segments](https://help.klaviyo.com/hc/en-us/articles/4416791883163).

This 30-day snapshot gives you a quick look at how your flow is performing. If you click on ****View details****, it will take you to the full analytics overview for the message.

![](https://klaviyo.zendesk.com/hc/article_attachments/46629778555291)

## Show analytics on the visual canvas

In order to understand how a flow is performing overall, you'll want to view channel performance across your whole series. A powerful feature in the visual flow builder is the option to see analytics directly.

1. To enable this feature, click the ****Show Analytics**** icon button located on the bottom right toolbar

![](https://klaviyo.zendesk.com/hc/article_attachments/46629778565403)

When you enable this analytics feature, you will see all the sending action cards expand to show embedded performance analytics. You will also be able to adjust the time range of data you would like to see.

For each channel sending action, you will see the following analytics:

- ****Open rate**** **(email and push only)**
  The percentage of unique recipients who opened your message. This is calculated by taking the number of unique individuals who opened your message divided by the number of recipients.
- ****Click rate**** **(email and SMS only)**
  The percentage of unique recipients who clicked a link in your message. This is calculated by taking the number of unique individuals who clicked your email divided by the total number that received your email.
- ****Selected conversion metric rate****
  For the conversion metric you have selected for your account, Klaviyo will report the percentage of conversions over the timeframe you have selected.
- ****Selected conversion metric value****
  If your selected conversion metric has an associated value (e.g., revenue), we'll also show the attributed value generated over the timeframe you have selected.

This feature allows you to run through all important channel sending actions in your series at a glance to compare key performance indicators such as opens and attributed revenue. This also allows you to compare message performance in each message or split paths side-by-side.

![](https://klaviyo.zendesk.com/hc/article_attachments/46629824730523)

## Review the flow message overview report

To view the flow message overview report:

1. Click on a message in the flow builder.
2. Click ****View all Analytics****in a message's configuration sidebar. You will be taken directly to the **Overview** tab for your flow message.

![analytics overview page.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28716052301723)

#### Metric cards

At the top of this page are cards showcasing primary performance metrics including:

- ****Opens rate**** (**email and push only**)
- ****Click rate**** **(email and SMS only)**
- ****Conversion rate**** (**displayed as specific conversion metric**)

You can adjust the conversion metric displayed in the overview page for a message.

1. Click the ****Conversion metric**** dropdown found at the top of the page.
   ![Dropdown of different analytics timeframe options with This Week currently selected](https://klaviyo.zendesk.com/hc/article_attachments/28716052249755)
2. Select another metric from the dropdown to look at the performance of the email from another perspective. You can choose a metric from within Klaviyo or any potential integrations you have set up.

#### Engagement over time

The graph in the **Engagement over time** section of the page will always show daily activity over the last month for your message. You can toggle on/off the different metrics that populate this graph, choosing from delivered, opened (email only), clicked, and then a conversion metric of your choice. For SMS, the conversion metric will always be the placed order rate.

![Key for the performance analytics graph displaying Delivered, Opened, Clicked, and Ordered Product metrics](https://klaviyo.zendesk.com/hc/article_attachments/28716052246811)

#### Deliverability

The **Deliverability** section below the graph shows more detail around how recipients have engaged with your flow message. The columns include::

- ****Channel****
  The channel associated with the message, either email, SMS or push.
- ****Sent****
  The total number of messages sent.
- ****Unique recipients****
  The number of unique people who were targeted to receive the message.
- ****Delivery rate****
  The number of messages successfully delivered. The successful deliveries metric may take a few hours to update.
- ****Bounce rate**** (**email and push only**)
  The percentage of messages that were sent but resulted in a soft or hard bounce.
- ****Failed to deliver rate**** (**SMS only**)
  The percentage of SMS sent that failed to deliver.
- ****Spam complaint rate**** (**email only**)
  The percentage of messages that received a spam complaint from recipients. This number does not represent the percentage of messages that went to spam, but rather what percentage of people marked the message as spam after receiving it in their primary inbox.
- ****Unsubscribe rate****
  The percentage of people that unsubscribed after receiving the message.

If you notice that your successful delivery rate drops below 99%, and your failed deliveries/bounce rate is increasing above 1%, this suggests it's probably time to clean your lists.

Change the timeframe of this report by selecting a date range from the dropdown at the top of the page. View analytics across a range of different timeframes, and establish your own range by choosing custom dates.

![Dropdown of different analytics timeframe options with This Week currently selected](https://klaviyo.zendesk.com/hc/article_attachments/28716052254235)

## Review recipient activity

The **Recipient Activity** tab contains data about how people are interacting with your flow message. You can sort the data to easily find a particular email address/phone number or see who has opened/clicked your email the greatest number of times. This recipient data can be exported by clicking the ****Export CSV**** button.

You will only have the ability to export these contacts if you are an Owner, Admin, or Analyst.

![](https://klaviyo.zendesk.com/hc/article_attachments/44743014247451)

The recipient activity data available here includes:

- ****Waiting****
  If your flow message is scheduled to send after X number of hours/days, this the number of people waiting to receive scheduled messages will appear here.
- ****Needs review****
  If your flow message is (or was at some point) in manual mode, the individuals with messages that are ready to go out will appear here — from this tab, you can review and then choose to send/cancel these messages.
- ****Recipients****
  Every person targeted to receive the message (regardless of whether the message was successfully delivered).
- ****Delivered****
  Every person who successfully received the message.
- ****Opened**** **(email and push only)**
  The number of times a recipient opened the email or push message.
- ****Clicked**** **(email and SMS only)**
  The number of times a recipient opened the email or SMS message.
- ****Converted****
  Every person who completed the selected conversion metric after receiving the message.
- ****Bounced/failed delivery****
  When trying to send to these people, we received a delivery failure notification.
- ****Unsubscribed****
  Total people who unsubscribed through the unsubscribe link in your email.
- ****Marked as Spam**** **(Email only)**
  Total people who have marked this email as spam after receiving it.
- ****Skipped****
  This will include buckets for each reason people may have been skipped (as noted in the section below).

Engagement events for emails such as opens and clicks are attributed to the date the email was sent, not the date the opens and clicks occurred.

#### Check skipped reasons

The **Skipped** section of the **Recipient Activity** tab is very important. This is where you should look if you're concerned that individuals are not receiving your flow messages as expected. Common reasons why individuals may be getting skipped by a flow email include:

- ****Smart sending****
  If [Smart Sending](https://help.klaviyo.com/hc/en-us/articles/115005078227) is turned on for your flow message, individuals that have received another message of the same kind within your smart sending period will not receive the message.
- ****Missing email/phone number****
  If the email or phone number for a given contact is invalid or not assigned **(SMS only)**, this person will be skipped.
- ****Person suppressed****
  If someone is suppressed in your account, they will be skipped from all sends automatically.
- ****Fails flow filters****
  Klaviyo will apply flow filters when someone first enters your flow, but also again before each flow send -- those who fail the flow filters at send time will be skipped.
- ****Fails additional filters****
  If you apply additional filters to your flow message and individuals fail these filters at send time, they will be skipped.

  Email-specific skipped reasons include:
- ****Missing email****
  Skipped because there is no email address associated with their profile.
- ****Person suppressed****
  Skipped because they unsubscribed or hard bounced from all email.
- ****Email syntax error****
  Skipped because the email template contains a syntax error.
- ****Catalog item unavailable****
  Skipped because a product in the rendered email content is currently out of stock or not available.
- ****Over email limit****
  Skipped because you went over your account's sending limit.
- ****Unable to send email****
  Skipped because we ran into an unexpected error at send time.
- ****Invalid from email****
  Skipped because the From Email address is not a valid address.
- ****Error retrieving external data****
  Skipped because there was an issue retrieving data from an external source (for example a coupon code from Shopify).
- ****Duplicate email****
  Skipped because the same email to the same address was already sent.
- ****Coupon category unavailable****
  Skipped because the email contains a placeholder to pull in a dynamic coupon restricted to a certain category, and the category was deleted.
- ****No more uploaded coupons remain****
  Skipped because the email contains a placeholder to pull in an uploaded coupon and no more uploaded coupons remain.
- ****Coupon code doesn't exist****
  Skipped because the coupon code you’re referencing in an email either doesn’t exist or doesn’t match the coupon code you created in your Coupons tab. Coupon code names are case-sensitive.
- ****Email cancelled****
  Skipped because the email had been cancelled at or before send time.
- ****Suspicious email****
  Email addresses that have hard bounced across the Klaviyo infrastructure.

  SMS-specific skipped reasons include:
- ****Unable to send SMS****
  Skipped because we ran into an unexpected error at send time.
- ****Missing SMS consent****
  When someone triggers a flow and we have their phone number but no SMS consent timestamp, they will be skipped from receiving the SMS message.
- ****Missing phone number****
  Skipped because the recipient does not have a phone number associated with their profile.
- ****Phone number is not valid****
  Skipped because the recipient does not have a valid phone number.
- ****Phone number is in country not supported by SMS****
  Skipped because the recipient's phone number is not a US number. SMS sending is currently only available for US recipients.
- ****No sending number****
  Skipped because there is no sending number associated with your account. You can add a sending number to your account in ****Settings > SMS****.
- ****Not enough funds available****
  Skipped because you have insufficient funds in your account to send SMS messages. You can add funds in ****Billing > Create your plan****.

## Review conversions

To review your conversion performance (email, SMS, or push) against certain metrics, head to the **Conversions** tab. Here you will be able to choose the specific metric (e.g., **Placed Order**, **Ordered Product**, **Active on Site**, etc.), the number of said conversions, and how to classify this data (e.g., revenue, types of products, locations, successful deliveries, etc.).

1. First, choose the timeframe you would like to review via the **Date Rage** dropdown.
   ![data range dropdown.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28716062721051)
2. In the **Conversion metric** dropdown, choose the metric you want to review. This dropdown will contain all Klaviyo-specific, integration, and custom metrics you have set up.
   ![statistic dropdown.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28716052315931)
3. Choose how you would like your metric success displayed via the **Property** dropdown. In the example below using **Ordered Product**, you have the option to display **All** conversion success information or just by certain dimensions or types. For example, you may want to review conversion information by product types, where products are bought or shipped, types of customers that purchased, etc. Keep in mind that these properties will be relative to how you have them set up, the metric you are reviewing, and your integration.

![dimension dropdown-final.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28716062728347)

Once you have chosen your metric and how it will be measured and displayed, it will appear in section below. In the example below using **Ordered Product** and property as **SKU**, you can review specific conversions by SKU type.

![conversion example-final, flows.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28716062733339)

## Review link activity

The **Link Activity** tab contains analytics for the links tracked in your flow message. Klaviyo tracks the total unique people who have clicked, the total number of clicks (not unique), the average click per person, and the total people that did not click. For emails, below the analytics is a list of all links that have been included in your flow email if your email has dynamic content that populates unique links for each recipient. Otherwise, you will see a list of the top 25 links in each message, including the unique and total clicks. You can toggle your view here from ****Table**** view to ****Visual**** view.

If your flow email has a currently running or completed A/B test, you can view the separate activity for each variation as well.

## Review deliverability

You can analyze the deliverability performance of each flow message using the dedicated **Deliverability** tab.

![deliverability.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28716052256027)

This page displays data around your flow message's performance for key deliverability metrics, and an indicator showing whether your performance in these areas is **Healthy,****Room for improvement**, or **Needs Attention.**

These metrics include:

- [Open rate](https://help.klaviyo.com/hc/en-us/articles/360042454031)
- [Click rate](https://help.klaviyo.com/hc/en-us/articles/360057459931)
- [Bounce rate](https://help.klaviyo.com/hc/en-us/articles/360057036052)
- [Unsubscribe rate](https://help.klaviyo.com/hc/en-us/articles/360057471831)
- [Spam complaint rate](https://help.klaviyo.com/hc/en-us/articles/360057985791)

![Key deliverability metrics for your campaign](https://klaviyo.zendesk.com/hc/article_attachments/28716062669211)

### Deliverability performance targets

|  |  |  |  |
| --- | --- | --- | --- |
| ****Metric**** | ****Needs attention**** | ****Room for improvement**** | ****Healthy**** |
| Bounce rate | >2% | 1%-2% | < 1.0% |
| Spam complaint rate | >0.05 | 0.01%-0.05% | < 0.01% |
| Unsubscribe rate | >1% | 0.3%-1% | < 0.3% |
| Open rate | <27% | 27%-33% | > 33.0% |
| Click rate | <0.8% | 0.8%-1.2% | > 1.2% |

If your performance is labeled as **Room for improvement** or **Needs Attention** in any of these areas, see our guides on [troubleshooting declining performance.](https://help.klaviyo.com/hc/en-us/sections/360012800811-Campaign-flow-and-audience-analytics)

### Deliverability insights

The deliverability tab for flow messages displays information regarding:

#### Performance by inbox provider

This chart helps you identify whether your deliverability issues are isolated to a specific inbox provider. It shows key deliverability metrics across the inbox providers your customers are using so you can easily identify differences in performance.

The five default inbox providers that will appear upon load are those with the most messages received. If a particular inbox provider has a health status of **Needs Attention**, it will appear on load for visibility.

This information is broken down into two categories:

****Positive engagements****
When chosen, the graph will display:

- Open rate **(email only)**
- Click rate **(email only)**
  ![Performance by inbox provider chart showing postive engagements](https://klaviyo.zendesk.com/hc/article_attachments/28716052265627)

  ****Negative engagements****
  When chosen, the graph will display:
- Bounce rate
- Unsubscribe rate
- Spam complaint rate

![Performance by inbox provider chart showing negative engagements](https://klaviyo.zendesk.com/hc/article_attachments/28716062672923)

If you are seeing deliverability performance issues here, you can [strengthen your sender reputation for an inbox provider.](https://help.klaviyo.com/hc/en-us/articles/115005250368)

#### Performance by email domain

This chart helps you identify whether your deliverability issues are isolated to a specific email domain. It shows key deliverability metrics across the different email domains your customers are using so you can easily identify differences in performance.

The five default domains that will appear upon load are those with the most messages received. If a particular domain has a health status of **Needs Attention**, it will appear on load for visibility.

This information is broken down into two categories:

****Positive engagements****
When chosen, the graph will display:

- Open rate **(email and push only)**
- Click rate
  ![Performance by email domain showing positive enagegments](https://klaviyo.zendesk.com/hc/article_attachments/28716062665243)

  ****Negative engagements****
  When chosen, the graph will display:
- Bounce rate
- Unsubscribe rate
- Spam complaint rate

![Performance by email domain showing negative enagegments](https://klaviyo.zendesk.com/hc/article_attachments/28716052282651)

If you are seeing deliverability performance issues here, you can [strengthen your sender reputation for a specific domain.](https://help.klaviyo.com/hc/en-us/articles/115005250368)

#### Performance by country

This chart helps you to better understand your contact base through a performance breakdown by country. This can help you [optimize send times](https://help.klaviyo.com/hc/en-us/articles/360029794371) for your primary audience.

Learn more about how [location](https://help.klaviyo.com/hc/en-us/articles/115005073907) is set for profiles in Klaviyo.

The five default countries that will appear are those with the most messages received. If a particular country has a health status of **Needs Attention**, it will appear on load for visibility.

This information is broken down into two categories:

****Positive engagements****
When chosen, the graph will display:

- Open rate
- Click rate
  ![Performance by country showing positive enagegments](https://klaviyo.zendesk.com/hc/article_attachments/28716062684187)

  ****Negative engagements****
  When chosen, the graph will display:
- Bounce rate
- Unsubscribe rate
- Spam complaint rate

![country_negativefullsize.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28716052284443)

If you are seeing deliverability performance issues here, you can [strengthen your sender reputation for a specific country.](https://help.klaviyo.com/hc/en-us/articles/12995016978075)

#### Performance by email client

This chart helps you gain insight into how recipients are viewing your email. You can see a breakdown between desktop and mobile usage, and can use it to determine if you need to optimize for one device or the other. It shows the total opens and the breakdown of that total by device type.  To optimize email content between desktop and mobile, you can utilize third-party tools such as [Litmus](https://www.litmus.com/) or [Email on Acid](https://www.emailonacid.com/) to preview your emails on a wide variety of devices and inbox providers.

Learn more about [optimizing content for mobile](https://help.klaviyo.com/hc/en-us/articles/115005254428) in Klaviyo.

![Performance by email client report showing desktop and mobile users](https://klaviyo.zendesk.com/hc/article_attachments/28716052296475)

#### Dropdown health status

When a particular domain or country is experiencing very poor performance in any of the key deliverability metrics, a **Needs Attention** status will appear next to the field.

![Needs attention flag in drop down near low performing items](https://klaviyo.zendesk.com/hc/article_attachments/28716052287387)

This status will only be visible if two or more of the deliverability metrics are in the **Needs Attention** range, and the country or email domain makes up 5% or more of the total send volume for the flow message.