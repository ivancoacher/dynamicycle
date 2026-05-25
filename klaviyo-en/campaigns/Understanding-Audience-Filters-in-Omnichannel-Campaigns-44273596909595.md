---
id: "44273596909595"
title: "Understanding Audience Filters in Omnichannel Campaigns"
source_url: "https://help.klaviyo.com/hc/en-us/articles/44273596909595-Understanding-Audience-Filters-in-Omnichannel-Campaigns"
section: "Build and send email campaigns"
category: "Campaigns"
category_slug: "campaigns"
klaviyo_updated: "2026-04-20T16:50:51Z"
language: "en"
---
## You will learn

Learn how audience filters allow you to target specific customer sub-segments for each message in your omnichannel campaign. By targeting these specific groups, you deliver the right message at the right time and on the right channel. As a result, your campaigns become more personalized and will drive engagement over time.

## Before you begin

This article covers how to set up exit criteria for omnichannel campaigns. If this is your first time creating a campaign, [learn how to create and send an email campaign](https://help.klaviyo.com/hc/en-us/articles/115005054847).

## How it works

****Audience Hierarchy and Targeting****

Audience filters take the audience you selected, and narrow it down to target a specific subset of that larger group.

A profile must meet two criteria to receive the message:

1. It must qualify for the main ****Campaign Audience**** defined at the top level.
2. It must qualify for the specific ****Audience Filter**** configured for that message.

If a profile doesn’t meet one, they’re excluded from that message.

****Filter Logic and Processing****

Filters are calculated immediately before the message send time. This ensures accuracy by using the profile's most recent activity and attribute changes.

(For more details on calculating recipients at send time, read more about [Understanding campaign schedule and send options](https://help.klaviyo.com/hc/en-us/articles/360050216012).)

To create more precise targeting, you can combine multiple conditions with:

- ****AND Logic:**** Requires a profile to meet all conditions.
- ****OR Logic:**** Requires a profile to meet at least one condition.

****Locking and Unlocking****

Audience filters are locked when the message is scheduled. If the message is reverted to draft status, the filters become unlocked and can be reconfigured. Once the message starts sending, the filter configuration becomes permanent.

## Configuring audience filters

- Click the message to open the message details panel
  ![](https://klaviyo.zendesk.com/hc/article_attachments/44273551226139)
- Click the ****Settings**** tab
  ![](https://klaviyo.zendesk.com/hc/article_attachments/44273551226523)
- In the Audience filter section, click ****Add filter conditions****
  ![](https://klaviyo.zendesk.com/hc/article_attachments/44273551227035)
- Next, define your filter conditions. Note that the audience shown at the top is the overall, top-level audience; the conditions you add will narrow down this group into a smaller, targeted subset.
  ![](https://klaviyo.zendesk.com/hc/article_attachments/44273551227419)
- Click ****Add condition**** to chain additional filter conditions. Use AND or OR operators to link the conditions.

  ![](https://klaviyo.zendesk.com/hc/article_attachments/44273551229339)
  ![](https://klaviyo.zendesk.com/hc/article_attachments/44273596900891)
- Click ****Save**** and review the applied conditions in the message details panel.

  ![](https://klaviyo.zendesk.com/hc/article_attachments/44273551230363)
  ![](https://klaviyo.zendesk.com/hc/article_attachments/44273596901403)
- To confirm filter impact, click the ****Review**** tab and check the estimated recipients. This updated number reflects the audience subset that meets the filter criteria.

![](https://klaviyo.zendesk.com/hc/article_attachments/44273551231259)

## Audience filter examples

****Engagement filters****

- Has clicked on a specific message
  ![](https://klaviyo.zendesk.com/hc/article_attachments/44273596902555)
- Has not opened a message in last 24 hours
  ![](https://klaviyo.zendesk.com/hc/article_attachments/44273551234587)

  ****Channel affinity filters****
- Engagement preference is email first
  ![](https://klaviyo.zendesk.com/hc/article_attachments/44273596904731)
- For more details on channel affinity and engagement preference, read more about  [Understanding channel affinity in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/36211794270107).

  ****Combined filters****
- Has clicked on a specific message and engagement preference is email first

![](https://klaviyo.zendesk.com/hc/article_attachments/44273596905371)

## Troubleshooting

If you encounter unexpected recipient counts or messaging issues when using audience filters, review these common scenarios:

****Profiles Are Receiving No Messages or Too Many Messages****

Audience filters are applied to each message independently and do not interact with filters set on other messages in the campaign path. This can lead to two issues:

- Profiles are excluded (receive no message):
  - Cause: The combined filters for all messages are not comprehensive enough to cover the entire primary audience.
  - Solution: Review your filter logic (AND/OR chaining) to ensure every profile is eligible for at least one message. Alternatively, set one message with no filter to serve as a catch-all.
- Profiles receive multiple messages:
  - Cause: You created overlapping filters across different messages (e.g., Message A targets "Location = CA" and Message B targets "Gender = Female").
  - Solution: Review all message filters and define mutually exclusive groups. You may need to add exclusion criteria (e.g., exclude profiles who received Message A) to prevent duplicate messaging.

    ****Recipient Count Shows Zero****

    This occurs if you use a future engagement condition in your filter (e.g., "Clicked Message A" or "Opened Message B") and the corresponding message has not yet been sent.
- Cause: The filter cannot find profiles that qualify because the required action (like clicking the message) has not occurred yet.
- Solution: This is expected behavior during the drafting phase. The actual audience is calculated precisely at send time, including only profiles that have performed the engagement action. You can proceed with launching your campaign.