<h1>Understanding engagement reports for lists and segments</h1>

## You will learn

Learn how to analyze engagement reports for email lists and segments to understand how engaged your subscribers are. Engagement reporting can also help determine if you need to take additional steps, like [list cleaning](https://help.klaviyo.com/hc/en-us/articles/115005078347), to address engagement issues.

## Before you begin

You will first need to access or generate your engagement report for a list or segment. Head to our guide on [how to create an engagement report for a list or segment](https://help.klaviyo.com/hc/en-us/articles/15032210146715) to learn how to set up your report.

## The importance of engaged lists and segments

When it comes to generating revenue from email marketing, more profiles does not necessarily equal more revenue. It doesn't matter how many profiles you send to if your recipients are unengaged.

In fact, sending regularly to a group of [unengaged profiles](https://help.klaviyo.com/hc/en-us/articles/115000200072) will hurt your deliverability and [sender reputation](https://help.klaviyo.com/hc/en-us/articles/115005250368-Strengthen-Your-Sender-Reputation-to-Alleviate-Deliverability-Issues), as well as irritate subscribers. Sending to [engaged profiles](https://help.klaviyo.com/hc/en-us/articles/115000200072) will boost open rates, click rates, and revenue per recipient.

## Engagement report data and setup

### Domain view

The engagement report provides the ability to [review your data by all email domains or a specific domain](https://help.klaviyo.com/hc/en-us/articles/15032210146715).

Knowing which domains are engaging, or conversely not engaging, with your emails can help to diagnose potential deliverability issues to certain inboxes. From this data, you can then see where you need to [segment out problem domains](https://help.klaviyo.com/hc/en-us/articles/115005237908), [strengthen your reputation](https://help.klaviyo.com/hc/en-us/articles/115005250368), and then eventually increase engagement once again.

### Charts in the report

Engagement reports are broken down into 5 key areas:

1. Past 30 day averages
2. Engagement over the last 30 days
3. Engagement distribution over time
4. Open rate by age of profile
5. Number of engaged members by age of profile

Reports broken down by age of profile only consider the last 52 weeks. Profiles more than 52 weeks old are not displayed in these charts.

### Understanding key data points and differences

For these reports, **Open Rate** is defined as the total number of opens divided by total emails delivered. This differs from how Klaviyo calculates open rates for a per campaign basis, which is unique opens divided by the total deliveries of that specific campaign.

**Age of Profile** shows how long an email address has been in your Klaviyo account (i.e., not how long an email address has been in a list or segment). For example, if a user was added to your account 10 weeks ago but wasn't added to a segment until 1 week ago, they’d be listed in the "10 weeks" bucket in your chart.

### Past 30 day averages

At the top of your report is an area to view performance averages over the past 30 days at a glance.

![Chart showing memeber engagement over the past 30 days](https://klaviyo.zendesk.com/hc/article_attachments/28704476696987)

Here's how these values are calculated:

- ******Open rate******
  Total opens divided by total deliveries.
- ******Click rate******Total clicks divided by total deliveries.
- ******Average order value******
  Total placed order value divided by total placed order events.

Apple Mail Privacy Protection (MPP) has changed the way that we receive open rate data on your emails by pre-fetching our tracking pixel. With this change, it’s important to understand that open rates will be inflated.

To see if your opens are affected, we suggest creating a [custom report](https://help.klaviyo.com/hc/en-us/articles/4416803987739) that includes an MPP property. You can also identify these opens in your individual [subscriber segments](https://help.klaviyo.com/hc/en-us/articles/4416791883163).

### Engagement over the last 30 days chart

The member engagement chart shows engagement over the past 30 days.

![Hover over somewhat engaged group showing count](https://klaviyo.zendesk.com/hc/article_attachments/34178164392987)

You will see profiles organized into 5 buckets:

- ******Very engaged****** (dark blue in chart)
  Recipients who have a 50%+ open rate in the past 30 days.
- ******Somewhat engaged****** (green in chart)
  Recipients who have a 20-50% open rate in the past 30 days.
- ******Barely engaged****** (yellow in chart)
  Recipients who have an open rate that is greater than 0%, but less than 20% in the past 30 days.
- ******Not engaged****** (orange in chart)
  Recipients who haven't opened any emails in the past 30 days.
- ******Received no emails****** (light blue in chart) Recipients who haven't received any emails in the past 30 days, likely because they're suppressed or have recently been added to the list or segment.

Hover over any part of the chart to see the total number of subscribers who fall into each category.

![member engagement hover.jpg](https://klaviyo.zendesk.com/hc/article_attachments/34178206724635)

In general, more than half of your list should fall into the very engaged or somewhat engaged category. No more than a quarter of your list should fall into the not engaged section.

If you find that more than a quarter of your list is not engaged, consider a [re-engagement campaign](https://help.klaviyo.com/hc/en-us/articles/115000931551) or [flow](https://help.klaviyo.com/hc/en-us/articles/115002775292). You may also want to see if there are specific domain(s) related to this low engagement, and [segment out problem domains](https://help.klaviyo.com/hc/en-us/articles/115005237908) and build back [your reputation](https://help.klaviyo.com/hc/en-us/articles/115005250368-) with that particular domain(s).

### Engagement distribution over time

The engagement distribution chart shows the distribution of engaged profiles by age, meaning how long they have been in your Klaviyo account.

![engagement_over_time__engagement.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28704476704667)

Profiles are grouped by their weekly age, up to 52 weeks (1 year). This means that profiles grouped in the 8 weeks bucket were added to your account 8 weeks ago.

Each column shows the distribution of all profiles of that age in 3 buckets: **engaged**, **unengaged**, or **never received an email**. For this graph, engagement is based on all events over the lifetime of the profile. This means a 30-week-old profile will be assigned a bucket based on 30 weeks of data.

The buckets are defined as follows:

- ******Engaged******Total opens divided by total deliveries is greater than or equal to 20%.
- ******Unengaged******
  Total opens divided by total deliveries is less than 20%.
- ******Never Received Email******
  This profile never received any emails, either because they are suppressed or were only recently added to the list or segment.

Opens and deliveries are calculated across all deliveries, including campaigns and flows.

You can also hover over any point in the graph to see the specific week, and the breakdown of subscribers who engaged, did not engage, and those who never received the email.

![engagement_over_time__hover_engagement.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28704484853403)

Use this graph to see engagement across different cohorts of profiles. This will help you identify whether there’s a specific point in time when people start to disengage from your brand. If there is, use that information for your winback efforts. For example, set up a winback flow that targets customers with special offers or exclusive content.

### Open rate by age of profile

The open rate by age of profile graph shows how the age of a profile correlates with open rates. This information helps determine if any older or outdated email addresses are bringing down open rates.

![open_rate_by_age_of_profile__engagemet.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28704476708123)

Profiles are grouped by age on the horizontal axis and the overall open rate for that group is plotted on the chart above.

Open rates are calculated as total opens over all time for all profiles of that age, divided by total deliveries over all time for all profiles of that age. To drill down further, hover on 1 of the plot points to see the open rate for that particular week.

![open_rate_by_age__hover_engagement.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28704484856091)

If you look at where the lowest volume of open rates are, you can use this chart to figure out if you should use the age of a subscriber as criteria to segment and clean your list. For example, if you notice older profiles have lower open rates than newer profiles, you can segment on age to target newer profiles.

### Number of engaged members by age of profile

The number of engaged members by age of profile chart, like the Open rate by age of profile graph, shows a distribution of age of profiles and their engagement. However, in this chart, there is more granular data around engagement as well as unengagement across each profile age group.

![number_of_engaged_segments__engagement.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28704484859803)

Hover over any bar in the chart to see the engaged vs. unengaged subscriber numbers for that particular week.

![number_of_engaged__hover_engagement.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28704476712731)

If you look at where the highest volume of unengaged profiles are, you can use this chart to figure out if you should use the age of a subscriber as criteria to segment and clean your list. For example, if you notice that the older profiles are less engaged than newer profiles, you can segment based on the age of the profile to focus in on newer subscribers.

## Interpreting your results

Engagement is a critical component of successful email marketing. A key factor that influences engagement is the age of an email address. This is also why it's important to continuously grow your list; as older profiles detach from your brand, replace them with new, engaged subscribers.

If you notice a high volume of old, unengaged profiles, it's time to [clean your list](https://help.klaviyo.com/hc/en-us/articles/115005078347-A-Guide-to-List-Cleaning). You should completely remove subscribers who have never opened an email. If you have unengaged subscribers scattered across the board, reassess the relevance of your content or ask these profiles what kind of content they want to see. You may be sending content to your subscribers that is irrelevant or repetitive.

You may also want to segment out barely engaged profiles to funnel them into a [re-engagement flow](https://help.klaviyo.com/hc/en-us/articles/115002775192).

For more information on applying these reports to assess and restrategize segments, check out our resource on how to [use segment engagement reports to judge lead quality](https://help.klaviyo.com/hc/en-us/articles/360034785292).

## Additional resources

- [How to create an engaged segment](https://klaviyo.zendesk.com/hc/en-us/articles/115000200072)
- [How to create an unengaged segment](https://klaviyo.zendesk.com/hc/en-us/articles/360044054732)
- [How to troubleshoot decreasing KPIs](https://klaviyo.zendesk.com/hc/en-us/articles/360043802871)
