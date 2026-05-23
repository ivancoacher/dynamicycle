---
id: 360051127672
title: "Understanding the absolute flow timeline and rejoining splits"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360051127672-Understanding-the-absolute-flow-timeline-and-rejoining-splits"
section: "Add steps or actions to flows"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-04-21T13:54:50Z"
language: en
---

## You will learn

Learn why the timeline may not appear when there is a rejoined split through an example.

A flow's timeline is how long it will take a person to complete the flow. For instance, if you have a flow with a time delay of two days followed by an email, the absolute timeline hint will show two days, since that is how long it will take the flow to complete. However, this timeline may not always appear, particularly when flows contain a rejoined split.

## Timing and rejoining splits

There may be instances in which split paths have different time delays. In this case, when you rejoin the split, recipients coming from the YES and NO paths will experience different absolute timelines from the trigger.

In the below example, there are three paths that come together post-rejoin. For the two highlighted in green, they will receive the final discount email post-rejoin after two days, while those coming from the yellow highlighted path would receive the same email after four days due to the additional time delays set on this path.

![Example flow showing how conditional splits can be rejoined to a single path of the flow.](https://klaviyo.zendesk.com/hc/article_attachments/28704477341467)

Since the timeline is different for the yellow path, you will not see [an absolute timeline hint](https://help.klaviyo.com/hc/en-us/articles/115003885212) below the lower right-hand corner of the email card.

## Additional resources

- [How to rejoin and disconnect a flow split](https://help.klaviyo.com/hc/en-us/articles/360002419512)
- [Understanding time delays near splits](https://help.klaviyo.com/hc/en-us/articles/360050334651)