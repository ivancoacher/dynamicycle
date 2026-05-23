<h1>Maintain a healthy email audience with Audience Optimization</h1>

## ****You will learn****

- What Audience Optimization is and how it differs fromSuppressions.
- How to set up a campaign with Audience Optimization.
- How to view and interpret Audience Optimization performance reports.
- Eligibility, supported channels, and current limitations.

[Advanced KDP](https://help.klaviyo.com/hc/en-us/articles/17655007276059) and [Marketing Analytics](https://help.klaviyo.com/hc/en-us/articles/33789259613595) are not included in Klaviyo’s standard marketing application, and a subscription is required to access the associated functionality. Head to our [billing guide](https://help.klaviyo.com/hc/en-us/articles/115000976672) to learn about how to purchase these plans.

## ****What is Audience Optimization?****

Audience Optimization for email campaigns uses a predictive model to identify recipients who are highly likely to unsubscribe and automatically removes those high risk recipients from sending.

The goal is to maintain a healthy email audience by avoiding sends to people who are likely to unsubscribe, while preserving reach to the rest of your engaged audience.

## ****Who can use Audience Optimization****

Audience Optimization is available with the following scope:

- ****Plans:**** Available to customers on the Marketing Analytics or Advanced Klaviyo Data Platform (Advanced KDP) packages.
- ****Channels:**** Only Email.

## ****How to use Audience Optimization in email campaigns****

### ****1. Create a campaign****

- Go to Campaigns and create a new email campaign or an omnichannel campaign.
- Choose your target audience (lists and/or segments) in the Audience step.

### ****2. Find the Audience Optimization toggle****

In the Audience step of a single channel email campaign or an omnichannel campaign, look for the Audience Optimization option once an audience has been selected.

![](https://klaviyo.zendesk.com/hc/article_attachments/48320682444827)

Note: The Audience Optimization toggle does not appear if your account is currently in Reputation Repair.

### ****3. Turn on Audience Optimization****

- Turn on the Audience optimization toggle.
- Note for single channel campaigns:
  - Klaviyo shows an estimate of recipients who are likely to unsubscribe Estimate how many recipients are likely to be removed from sending.
  - Update the Estimated recipients count to reflect the reduced audience size (base audience minus high‐risk recipients).

### ****4. Review and schedule your campaign****

- Continue to the review & schedule step.
- Schedule or send your campaign.

At the time Klaviyo determines the recipients for the campaign, the Audience Optimization model runs against the final set of eligible recipients and removes the highest risk profiles before the messages are delivered.

## ****How Audience Optimization works****

Audience Optimization uses a predictive model to estimate each recipient’s likelihood of unsubscribing. For the first release, unsubscribe likelihood is the primary decision factor. The model considers engagement events and rates, onsite activity, and several company-level features such as sends per profile and total number of profiles to make these predictions.

Profiles with high predicted unsubscribe risk are removed; all other eligible profiles remain in the send group.

To avoid permanently sidelining recipients, Audience Optimization includes a cool‐off safeguard:

- If a profile has not received any messages in the past 30 days, their unsubscribe risk is temporarily treated as very low, allowing them to receive messages again after a cooling period.
- This creates opportunities to re‐engage previously high‐risk profiles with more relevant content and lower frequency.

## ****Audience Optimization Analytics****

Audience Optimization includes analytics to help you understand who was excluded from a campaign and the overall impact of optimization on your performance.

### ****View analytics for a campaign****

Within each campaign, the Audience Optimization card provides a quick summary of how many recipients were excluded from each campaign send.

- Profiles removed: This number shows how many recipients were excluded by Audience Optimization for that specific campaign. These are profiles predicted to be less more likely to unsubscribe.

You can click on the Profiles removed number to view the full list of excluded recipients in the Recipient activity → Optimized tab.

To locate Audience Optimization analytics:

1. Navigate to a specific campaign.
2. On the campaign’s overview page, find the Audience Optimization card below the overall campaign metrics.

##

![](https://klaviyo.zendesk.com/hc/article_attachments/48320682447643)

### ****View excluded recipients for a campaign****

You can see which profiles were removed from a specific campaign due to Audience Optimization.

To access this list:

1. Navigate to a campaign’s Recipient activity tab.
2. Select the Optimized subtab.

This view shows the profiles that were removed by Audience Optimization for that send.

For quicker access, you can also:

- Go to the Campaigns overview page
- Locate the Audience Optimization card
- Click the number of profiles removed to open the full list of profiles removed.

### ****Understand aggregate impact****

To help you understand long-term impact, Klaviyo surfaces an account-level Audience Optimization performance view.

- For each campaign that uses Audience Optimization, a randomly selected portion of eligible recipients is automatically held out in a control group. These recipients receive the campaign without optimization, meaning they are not evaluated or excluded by the model.
- The remaining recipients are evaluated by Audience Optimization. Based on model predictions, some recipients may be excluded from receiving the campaign to improve overall performance.
- When reporting performance, we compare outcomes between:
  - The optimized group (where Audience Optimization is applied), and
  - The control group (where no optimization is applied)
- The control group size is automatically managed by Klaviyo and may change over time; you do not need to configure or maintain it.
- Metric impact (e.g., unsubscribe rate change) is calculated as the relative difference between the optimized group and the control group for a given metric. For example, if the unsubscribe rate is 0.07% for the optimized group and 0.08% for the control group, the change is calculated as (0.05% − 0.08%) ÷ 0.08% = −13%, indicating a reduction in unsubscribes.

  You can view the overall impact of Audience Optimization across your campaigns directly from the Audience Optimization card by expanding “View impact of audience optimization across all campaigns.”

  Metrics include:
- Unsubscribe rate change: Shows how Audience Optimization impacts unsubscribe rates across your campaigns. This is calculated using the control and treatment methodology explained above.
- Campaigns evaluated: The number of campaigns with Audience Optimization included in the aggregate analysis.
- Recipients removed: The percentage of recipients excluded by Audience Optimization across all evaluated campaigns.
- Total recipients evaluated: The total number of recipients considered by Audience Optimization across all evaluated campaigns.

![](https://klaviyo.zendesk.com/hc/article_attachments/48320682448667)

Campaigns are included in the performance view after a campaign has been finished for at least 24 hours. This buffer lets Klaviyo capture late data automatically, so you don’t need to take any extra steps before checking results.

## ****Identify Audience Optimization campaigns****

You can quickly identify and filter campaigns that used Audience Optimization from the campaign list.

- Campaigns sent with Audience Optimization are marked with a ⚡ (lightning bolt) icon in the Campaign type column.
  ![](https://cdn.sanity.io/images/6ct6b26e/help-center-prod/3d40ce570d11515b47ae55f192b0918543b7df31-448x344.png)
- You can also use the filters in the campaign list to view only campaigns that used Audience Optimization.

![](https://cdn.sanity.io/images/6ct6b26e/help-center-prod/5eed4d8bf97b68f7b88d10739043364ba407d88d-486x378.png)

## ****Audience Optimization FAQs****

### ****What does Audience Optimization optimize for?****

The first version of Audience Optimization optimizes for unsubscribe risk only: it removes recipients whose predicted likelihood of unsubscribing is high enough that sending is unlikely to be worth the risk.

Future releases will incorporate additional metrics like engagement and conversion, using a multi‐objective model rather than unsubscribe likelihood alone.

### ****Why don't I see the Audience Optimization option for a campaign?****

The Audience Optimization toggle can be hidden for several reasons:

- Your account is currently in Reputation Repair, in which case the option is suppressed until your deliverability status improves.
- No audience has been added yet; the option only appears after you select at least one list or segment.

### ****How is this different from suppression?****

- Suppression removes profiles from receiving any further campaigns or flows.
- Audience Optimization evaluates a single campaign and removes only the highest‐risk recipients for that send, based on modeled unsubscribe likelihood. Those same recipients might be eligible for different content or future sends.
