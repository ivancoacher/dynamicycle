---
id: 360054240252
title: "Understanding how date-based flows schedule recipients"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360054240252-Understanding-how-date-based-flows-schedule-recipients"
section: "Lifecycle flows"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-04-21T13:54:51Z"
language: en
---

## You will learn

Learn how profiles enter date-based flows and what happens when a date is added or changed. For instance, what happens if someone is about to enter the flow, but the date is suddenly changed or deleted altogether? This article runs through what happens for date property-triggered flows when dates are added, updated, or deleted from a profile.

## How profiles qualify for date-based flows

Klaviyo checks if someone qualifies for a flow daily via a check that runs a full day in advance. In addition, Klaviyo will check if someone qualifies for a flow whenever a date is added or updated on a profile. During this time, Klaviyo determines if a profile should enter a flow based on whether that date falls within the flow’s full timeline. A person will only be added to a flow if the day, month, and year fall within a flow’s timeline, so if a date is in the future (e.g., 12/1/2030), they won’t be added to a flow before that time. Additionally, if it's a reoccurring flow (e.g., monthly or weekly), that person will be scheduled for that flow and enter during the repeated date.

Date-based flows will only schedule recipients for messages that are set to **Live** or **Manual** status.

Because the flow checks a full day in advance, this means that once the flow is set to live or manual, it will only schedule recipients whose date property is a full day after its status changed.

For example, if you change a birthday flow from draft to live on March 1st:

- Someone whose birthday is on March 1st won't enter the flow.
- Someone whose birthday is on March 2nd might not enter the flow depending on what time it was set live.
- Someone whose birthday is on March 3rd or later will enter the flow.

The above applies to profiles with an existing and unchanged date property. If a date property is modified or added to a profile the same day it goes live, they will still enter the flow since the property change causes them to be checked. However, they may not receive the first email if they entered the flow after the email was scheduled to send.

### Date properties with time

Sometimes date properties have a timestamp. For example: 2025-04-30 17:08:06. For the purposes of flow triggering, the attached time is ignored.

When Klaviyo triggers a flow, only the date that the profile should enter the flow is considered. After the date a profile should enter is known, any "start time restrictions" configured in the trigger settings are applied (start at 9 a.m., etc).

### Timezones

Date flows are always triggered from the point of view of the profile. This means that Klaviyo determines the date a profile should enter a flow based on its timezone. If the profile does not have a timezone assigned to it, the account's timezone will be used.

### Yearly repetition

If a date-triggered flow is set to repeat yearly, Klaviyo will evaluate whether the profile enters the flow based on the day and month rather than the exact year. For example, if a flow is set to repeat yearly on someone's birthday and their birthday is set to 01/01/1990, the flow will trigger every year on 01/01 (January 1st), regardless of the exact year.

This also applies to properties with a future date. If a profile property is set as 01/01/2030, and the flow is set to repeat yearly, it will trigger every year on 01/01, including years prior to 2030.

## What happens when a date is added for a same-day send

When a date is added on the same day that a message is scheduled to go out, the subscriber will get the message only if they added it before the message’s send time.

For instance, let's say you have a birthday flow with an email that goes out at 12 p.m. in the recipient’s local time, and Sarah adds her birthday at 10 a.m. Since this is before the email is scheduled to go out, Sarah will get the message.

As for Jane, she adds her birthday at 1 p.m. — an hour after the email sent out. In this case, Jane won’t receive the email that was already sent. However, Jane will continue in the flow if:

1. There are more messages or steps in the flow
2. The messages or steps are scheduled for later than when they added the birthday (e.g., if another email is scheduled to go out a week later)

## What happens when the date falls within a flow’s timeline

If the date falls within the timeline of the flow, Klaviyo will pull the profile into the flow and insert them at the appropriate point based on the timing established within the series, as illustrated in the example below.

![Example of a date property-triggered flow that triggers 9 months before a person's wedding.](https://klaviyo.zendesk.com/hc/article_attachments/28717388845595)

Say you have a wedding flow that starts nine months before someone's wedding. Every month leading up to their wedding date, you share content and products that may interest the bride or groom.

![Example of a date property-triggered flow with time delays that wait 7 and 6 months before someone's wedding.](https://klaviyo.zendesk.com/hc/article_attachments/28717382519963)

If on February 1, you receive Jane Smith’s wedding date, and it's 7 months away. Klaviyo will automatically insert Jane at the **Wait until 7 Months before person's Wedding** point in time. She will immediately be scheduled to receive the appropriate content; here, the “What to do 7 months before the wedding” email.

## What happens when the date falls outside the flow’s timeline

If the date falls outside the timeline of a flow, or is deleted entirely, the profile will not be added to the flow at this time.

For instance, say you have a birthday flow that sends out a message on the actual date and then ends. In this case, the timeline for the entire flow is one day.

![Example of a conditional split that checks for SMS consent..](https://klaviyo.zendesk.com/hc/article_attachments/28717382524315)

If on February 1, Sarah Smith submits a form that lets you know that her birthday is June 1; Sarah will not enter the birthday flow immediately. Instead, she will only enter into the flow on her actual birthday in June.

## What happens when a date is updated in the middle of a flow

Before every action in a flow (e.g., before every email or SMS that goes out), Klaviyo verifies that the date used to trigger the flow is still the same. This means that if someone is in a date-based flow but changes the date such that it falls outside the flow’s timeline, they will not be sent any further messages.

For instance, say that Jane from the example above is in the middle of a wedding flow.

![Example of a date property-triggered flow that triggers 9 months before a person's wedding.](https://klaviyo.zendesk.com/hc/article_attachments/28717382525979)

Originally, her wedding date is 5/1/2025 and she just passed the “Wait until 7 Months before person's Wedding” point and received the associated message. If she changes her date to 6/1/2025, she will exit the flow and not receive the subsequent messages at this time.

Klaviyo will also automatically reschedule the person based on the updated date. This is particularly helpful for appointment-focused flows — if someone's appointment is rescheduled, all messages are automatically rescheduled around the new date.

For the case above, Jane will automatically re-enter the flow from the beginning when her new wedding date approaches. This may mean she receives the same messages twice; however, this is a good thing, as the content will be personalized to where she is currently in wedding planning and she won’t need to comb through her emails for the previous messages.

## Additional resources

Learn more about date-based flows:

- [How to create a date property-triggered flow](https://help.klaviyo.com/hc/en-us/articles/360002732652)
- [How to build a birthday flow](https://help.klaviyo.com/hc/en-us/articles/360054242492)
- [Understanding time delays in date property flows](https://help.klaviyo.com/hc/en-us/articles/360054705431)