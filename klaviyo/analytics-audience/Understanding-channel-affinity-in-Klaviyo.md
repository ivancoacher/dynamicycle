---
id: 36211794270107
title: "Understanding channel affinity in Klaviyo"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/36211794270107-Understanding-channel-affinity-in-Klaviyo"
section: "Understand profiles"
category: "Audience"
category_slug: "analytics-audience"
klaviyo_updated: "2026-04-30T23:41:07Z"
language: en
---

Learn about using channel affinity to better personalize your marketing. Channel affinity gives you information on a profile’s expected engagement with different marketing channels.

## Before you begin

Criteria for channel affinity differs from other **Predictive Analytics** features, and you can qualify for it independently. You will only see channel affinity on profiles if your account meets the following conditions:

- You have at least 2 activated channels.
- You have at least 1,000 profiles with at least 1 delivery through each channel.
- You have at least 5,000 campaign deliveries on each channel in the last 6 months.
- You have at least 1 engagement with the delivered campaigns on each channel.
- For email, SMS and WhatsApp to be included in channel affinity, you must be on paid plans.

This does not refer to total profiles in your account, but rather the number of people who have opened or clicked a message.

Even if you have a channel activated on your account, if there is not enough data for it yet, it will not be included in the channel affinity model.

## About channel affinity

Channel affinity in Klaviyo is based on a machine learning model that predicts the likelihood of engaging with your next message through a specific channel.

Channel affinity properties are re-evaluated and updated every 2 weeks. The prediction model used to evaluate your account is updated every 4 weeks.

You can see a profile’s channel affinity preferences on the **Predictive analytics** card on their profile page.

![](https://klaviyo.zendesk.com/hc/article_attachments/37406042950811)

Channel affinity is only available for accounts with multiple channels enabled. Additionally, profiles will only have channel affinity data for channels they are currently consented to and can receive marketing on.

On this card, you can see:

- ****Channel****Any channel that you enabled and that the profile has consented to.
- ****Engagement preference****A ranking of channels for a profile based on expected engagement.

  ****What is expected engagement?****

  Expected engagement refers to the probability that a profile will engage through a particular channel. To identify a profile’s probability of engagement through a channel, Klaviyo considers:
- Campaign engagement counts and rates
- Active on site counts and recency
- Channel subscription recency

### Channel engagement preference

Channel engagement preference (i.e., the **Engagement** **preference** column) ranks channels based on expected engagement from the profile.

The possible values for this property are:

- ****First****The corresponding channel that a profile is expected to be most engaged with.
- ****Second****The corresponding channel that a profile is expected to have the 2nd most engagement with.
- ****Third****
  The corresponding channel that a profile is expected to third-highest engagement with.
- ****Fourth****
  The corresponding channel that a profile is expected to have the least engagement with.

## Using channel affinity properties

### Segment builder

You can build segments using **Engagement preference** to group customers based on their channel preferences.

To build a segment using these conditions:

1. Navigate to the **Lists & segments** page in Klaviyo.
2. Select ****Create new**** > ****Segment****.
3. Select ****Predictive analytics about someone**** > ****Predicted channel affinity**** > ******Engagement preference******.
4. Select a specific channel for these properties to evaluate and set your desired condition values.

![](https://klaviyo.zendesk.com/hc/article_attachments/37406567074843)

### Profile filters in flows

[Profile filters](https://help.klaviyo.com/hc/en-us/articles/115002779051#h_01HDAFKRKRESH9J6P9B098BAG3) are applied when people enter your flow, as well as before every message in the flow is sent. In this way, profile filters ensure that only people that still qualify continue moving through a flow. You can set up profile filters based on channel affinity properties.

To set profile filters for the entire flow:

1. Set your trigger, if you haven’t already.
2. Select your trigger and click the ****Add**** or ****Edit**** button next to the **Profile filter** option in the right sidebar.
3. Select ****Predictive analytics about someone**** > ****Predicted channel affinity**** > ****Engagement preference****.
4. Select a specific channel for these properties to evaluate and set your desired condition values.

   ![](https://klaviyo.zendesk.com/hc/article_attachments/37406567081627)

   To add profile filters to individual flow messages:
5. Select the individual flow message.
6. Add your condition under the **Additional filters** section in the right sidebar.
7. Select ****Predictive analytics about someone**** > ****Predicted channel affinity**** > ****Engagement preference.****
8. Select a specific channel for these properties to evaluate and set your desired condition values.

### Conditional splits in flows

You can also use channel affinity properties in conditional splits to send profiles down different paths in a flow based on their channel preferences.

To add a new conditional split into a flow series:

1. Drag the conditional split component from the left sidebar and drop it where you would like to create this split.
2. Click on the split to view the details panel.

   - Unconfigured splits display a yellow warning label.
   - Notice that **Yes** and **No** paths are automatically added below the split.
3. If you insert a conditional split midway into a flow, all components below that point are placed on the YES path by default.

   - If you'd like to automatically swap all components on the **Yes** and **No** paths of your split, click the settings icon (3 dots) and choose ****Flip split****.
4. In the details sidebar, define the logic for your conditional split.
5. Select ****Predictive analytics about someone**** > ****Predicted channel affinity**** > ****Engagement preference.****
6. Set your desired value for the channel affinity property you selected.

![](https://klaviyo.zendesk.com/hc/article_attachments/37406082235675)

## Frequently asked questions

### What happens when I activate a new channel?

When you add a new channel, your account will be evaluated for channel affinity eligibility.

- If you are eligible, Klaviyo will generate a prediction model and populate profiles with channel affinity properties. It can take up to 1 day to populate results.
- If you aren’t eligible yet, you may need to wait a week. Klaviyo checks for eligibility once a week at the beginning of each week.

### What happens when a profile subscribes to a new channel?

If you have channel affinity active for your account, profiles who have only provided consent for 1 channel will show that channel as their first preferences under **Engagement preference**.

- The new channel will be added to the profile’s properties. The new channel will have the first channel engagement preference.
- If multiple channels are added, they will be prioritized by SMS > WhatsApp > Email > Push.
- These channel affinity values for the channel will hold until the customer has received 7 messages on that channel or 30 days has passed, whichever comes first. This is checked every 2 weeks.

### How is channel engagement measured?

To measure engagement, Klaviyo's model considers the following information:

- Campaign engagement counts and rates (i.e. delivery/open/click counts and rates) over the past 7, 30, and 90 days.
- Count of **Active on site** events over the past 7, 30, and 90 days.
- Most recent **Active on site** event.
- Whether the customer subscribed to the channel in the past 30 days.

Machine opens and bot clicks are excluded from engagement measurements.