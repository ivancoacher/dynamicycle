---
id: 22981852783899
title: "Understanding bot clicks"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/22981852783899-Understanding-bot-clicks"
section: "Getting started with email deliverability"
category: "Deliverability & compliance"
category_slug: "deliverability-compliance"
klaviyo_updated: "2026-04-21T13:54:34Z"
language: en
---

## You will learn

Learn about bot clicks (also known as server-clicks), and why some of the clicks on your emails and SMS messages may not come from a human. Bot clicks can impact your marketing strategy, as profiles may appear to be more engaged than they actually are.

## What are bot clicks?

A bot click refers to an email or SMS click performed by a machine, often to verify the safety of a link or display a link preview.

Inbox providers, some 3rd-party security software, and carriers use bots to click links in emails before any human user. This helps the providers protect users from phishing by making sure the links are safe and not a malicious URL.

Bot clicks can impact your marketing because they give a false sense of engagement for a profile. It may appear that a customer clicked the link in an email because they were interested in the content, but in reality, a machine performed the click and the user did not perform the action.

Note that [Apple Privacy Opens](https://help.klaviyo.com/hc/en-us/articles/4416791883163) are a separate concept from bot clicks.

## Email bot clicks

### Identifying email bot clicks

Within the **Clicked Email** event in Klaviyo, you can find a piece of event data called **Bot Click**. The value for this can be set to either **true** or **false** based on whether the click was performed by a bot.

![Bot click event data within Clicked email event in Klaviyo](https://klaviyo.zendesk.com/hc/article_attachments/28723524314523)

Email bot-click event data is only available from January 1st, 2022.

### Preventing email bot clicks

[Dedicated click tracking](https://help.klaviyo.com/hc/en-us/articles/7676795223707) allows you to display your own domain on click-tracking links (instead of the default Klaviyo encoding).

Dedicated click tracking is beneficial because customers and inbox providers can easily recognize your brand, making the links in your email more trustworthy. Instead of a long string of letters and numbers from a Klaviyo-encoded link (i.e., **trk.klaviyomail.com** or **trk.klclick.com**), customers will see your brand’s name when hovering over links in your email. This increases the chances that they will click on your links, and makes links look safer in the eyes of inbox providers.

![Click tracking link shown on hover in email](https://klaviyo.zendesk.com/hc/article_attachments/28723524303387)

In addition to setting up dedicated click tracking, you should avoid linking to external websites and using link shorteners. These can cause email inbox providers to be suspicious of a link and validate its safety with a bot-click.

Lastly, maintaining a strong [sender reputation](https://help.klaviyo.com/hc/en-us/articles/15332906406171) and good overall deliverability shows inbox providers you are a reputable sender and makes them less likely to validate the safety of links in your sends.

There is no way to prevent bot clicks performed by inbox providers entirely. While these methods can make inbox providers less likely to verify the safety of links in your emails through an automated click, this does not guarantee that all bot clicks will be prevented.

## SMS bot clicks

SMS messages can also experience bot clicks. The biggest driver of bot clicks in SMS messages is link previewing functionality, which is a standard feature on most iOS and Android devices. In order for the link preview to be generated, devices must programmatically click the link to retrieve the preview image and present it in the user’s messaging app. The logic varies by device and operating system, but it is known to inflate click rates.

Additionally, bot clicks can also originate from carriers and providers that examine message content for compliance.

### Identifying SMS-bot clicks

Within the **Clicked SMS** event in Klaviyo, you can find an event property called **Bot Click**. The property’s value will be either **true** or **false** based on whether the click was performed by a bot.

![Bot click event data in Clicked SMS event](https://klaviyo.zendesk.com/hc/article_attachments/28723546244123)

## Impact of bot clicks

Bot clicks do not influence the cost of a campaign and do not impact conversions based on events such as **Active on Site**, **Placed order**, etc. However, they can impact attribution if the last click within the attribution window before a conversion is a bot click.

If you suspect you are experiencing high-levels of bot clicks with your emails or SMS messages, you can exclude bot clicks from tracking and reporting data or measure engagement using the **Active on site** rate instead of **Click rate**. Once a campaign is sent, from the overview page, you can select the conversion metric as the **Active on site** event to see this data.

## Monitoring bot clicks

### Segmentation

You can use bot click data as a filter when building segments to either see the number of profiles experiencing bot clicks, or to exclude the clicks to make sure you are only including real clicks performed by humans.

To exclude profiles that have only exhibited bot clicks, use the following filter for **Clicked Email** or **Clicked SMS** event conditions. This filter will make sure only profiles with a human click are included in your segment.

- Where **Bot Click equals False**

Note that a profile can have a mix of both human and bot clicks. Klaviyo uses a number of different factors to determine whether a click was performed by a bot, and is able to distinguish human and bot clicks from each other. A click performed by a human can be identified with the **Bot Click = false** event data.

Bot click data in segments is available from January 1st, 2022.

![segment.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28723524317339)

### Metric reports

You can also find data around the volume of email or SMS bot clicks in Klaviyo’s **Metrics** tab. To see this information, navigate to the **Clicked Email** or **Clicked SMS** event in Klaviyo’s **Metrics** tab. Once on the metric, you can set the timeline you’d like to analyze and the **By Bot Click** filter to view the volume of bot clicks you are experiencing.

![Metric report for Clicked SMS event with bot click filter](https://klaviyo.zendesk.com/hc/article_attachments/28723524306715)

Note that a profile can have a mix of both human and bot clicks. Klaviyo uses a number of different factors to determine whether a click was performed by a bot, and is able to distinguish human and bot clicks from each other. A click performed by a human can be identified with the **Bot Click = false** event data.

### Custom reports

Custom reports can be used to find data around bot clicks as well. Create a [Single Metric Deep Dive Report](https://help.klaviyo.com/hc/en-us/articles/360046242952) to analyze the number of bot clicks for the email or SMS channels.

To see the volume of bot clicks, select the **Clicked Email** or **Clicked SMS** event, along with the filter **Bot Click = true**. Similarly, you can exclude the filter **Bot Clicks = false** to exclude bot clicks from custom reports data.

Learn how to [configure custom reports to track bot clicks](https://help.klaviyo.com/hc/en-us/articles/27497646637979).

## Excluding bot clicks from attribution and certain reporting data

You can exclude bot clicks from both your account’s reporting data and attribution calculations. This way, your attribution windows for capturing actions align with your reporting data. Learn how to [remove bot clicks, Apple Privacy opens, and adjust your attribution windows](https://help.klaviyo.com/hc/en-us/articles/11118357030555#h_01J5X2K26S69K6ZGMY3NDBX2J6).

If you are an existing account prior to 8/27/24 and have already chosen to remove [bot clicks from your email settings](https://help.klaviyo.com/hc/en-us/articles/360004059711#h_01HFEZWHWN7AVGXQB8TGQT6BXG), ****those will apply to reporting only****. The new options on the **Attribution** page will remove them from ****both reporting and attribution**** at the same time. It is advised to select options on this page to apply them both.

## Impact of bot click feature on reporting

Once you enable the bot click feature, it will affect different areas of Klaviyo reporting or allow you further filtering capabilities. Additionally, some reporting will still include bot clicks regardless of the feature. Read more below about the specific impact per reporting surface.

### Metrics

The bot click reporting filter impacts how the following metrics on your account are calculated:

- **Click Rate**
- **Total Clicks**
- **Unique Clicks**

Other metrics on your account are not impacted.

### Reporting

With the bot click reporting feature enabled, any reports and dashboards showing click rates or counts of clicks over time will exclude bot clicks. These reports include:

- Applicable cards in the **Overview** dashboards
- Flow performance reporting (from within a specific flow)
- Campaign performance reporting (from within a specific campaign)
- SMS dashboard
- SMS and email benchmarks

  These reports will be updated retroactively to exclude bot clicks from January 1st, 2022.

  The following reports on your account will not be impacted by the bot click reporting filter:
- [Email campaigns trend report](https://help.klaviyo.com/hc/en-us/articles/115005089467)
- [Personal email reporting](https://help.klaviyo.com/hc/en-us/articles/115005246328)

Data in custom reports includes bot clicks by default but they can be excluded with the **Bot Click = false** filter.

### Benchmarks

The bot click reporting filter impacts the values you see in [email and SMS benchmarks](https://help.klaviyo.com/hc/en-us/articles/360050110072). Click rates in benchmark reporting will align with your setting selection as of May 2024 and include the previous month’s data.

Historical benchmarks before January 1st, 2022 are not impacted by the bot click reporting filter at this time.

### Experiments

If you are running A/B tests with **Click Rate** as a metric for your experiment, the bot click reporting filter can impact your results. The next time any live experiments are evaluated, only human clicks are used to evaluate the winner and bot clicks are excluded. This may cause a shift in the winning variation. Historical winners will not change and the winner was decided based on the data available at the time.

****Analyzing campaign A/B test results****

It is important to note that the **Continuous results and Test results** pages for [campaign A/B tests](https://help.klaviyo.com/hc/en-us/articles/360052794352) behave differently in regards to bot clicks.

The **Continuous results** page only shows in campaign A/B tests on less than 100% of the population (i.e. the winner is sent to the remaining recipients).

The **Continuous results** page always shows the click rates in adherence to your current bot click setting selection.

For example if you are currently excluding bot clicks from reporting, you may see the following results on the **Continuous results** page:

- Variation A = 3% click rate (winner)
- Variation B = 5% click rate

  Because the **Continuous results** page excludes bot clicks, the variation with a lower click rate may win after accounting for bot clicks.

  Meanwhile, the **Test results** page always shows the click rate based on your definition at the time that the winner was selected.

  For example, if bot clicks were included in reporting at the time the winner was selected, the **Test results** page may have the following results:
- Variation A = 15% click rate (winner)
- Variation B = 14% click rate

Because of the differences in behavior between the **Continuous results** and **Test results** pages, you may see conflicting results and the variation with a lower click rate declared the winner on the **Continuous results** page.

It’s not recommended to turn on the bot click setting while a live campaign or fixed date flow experiment is running.

### Attribution

The bot click reporting filter removes the impact of bot-clicks from attribution models for either the email and SMS channels. Conversions that follow a bot click are attributed if they occur in the attribution window. However, it is important to remember that bots cannot complete a purchase. Purchases occurring in the attribution window are real.