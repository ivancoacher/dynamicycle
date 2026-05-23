---
id: 360002419512
title: "How to rejoin and disconnect a flow split"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360002419512-How-to-rejoin-and-disconnect-a-flow-split"
section: "Add steps or actions to flows"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-04-21T13:54:42Z"
language: en
---

## You will learn

Learn how to use [trigger and conditional split components](https://help.klaviyo.com/hc/en-us/articles/115003883992-Introduction-to-Flow-Branching) in the flow builder to create targeted customer journeys stemming from the same initial trigger. However, as you start to branch your flows, there may be instances when you'd like to bring these separate journeys back together down the same path.

For example, you may have a welcome series with an initial split for those who sign up for your list through Meta Lead Ads and those who sign up directly on your website. Let's say you offer a different welcome discount to each of these groups, but in the final email, you want to send them the same content. Rejoining split paths allows you to accomplish this.

## Rejoining split paths

When you drag a split into a flow, you must define the conditions that will branch recipients and send them down unique paths. Below the exit point for each path, there is a "rejoin" icon.

To rejoin a split:

1. Click the ****Rejoin**** icon below either the YES or NO path of the split.
2. Drag the rejoin icon onto the other path to rejoin a split. Locations available as rejoin points will turn into a grey block once the rejoin icon is dragged over them.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/34336057659931)

You can rejoin splits anywhere you see a grey drop-point — rejoins don't necessarily have to be at the end of each branch. One thing to note is that it is only possible to rejoin the YES and NO paths within a single split.

## Disconnect a rejoined split

After you rejoin a split, you can also choose to disconnect the split and return it to the original state by clicking the ****Unjoin**** icon.

![The unjoin button](https://klaviyo.zendesk.com/hc/article_attachments/28723630084251)

When you disconnect a rejoined split, the "point of rejoin" will be removed and the split will once again have separate YES and NO paths that each end in an exit.

If you have multiple rejoined splits in a flow, you must start from the bottom and move upwards if you'd like to disconnect them. You cannot disconnect a split that's nested within a rejoined flow.

When you click to disconnect a split, if there are no components (emails, time delays, etc.) beneath the point of rejoining, the split will disconnect immediately. If there are components below the point of rejoining, you'll need to decide where to place them once the single rejoined path is once again replaced by separate YES and NO paths. You will have two options here:

- Shift these components to the end of the YES path.
- Shift these components to the end of the NO path.

![The option to shift the following flow elements to the yes or no path](https://klaviyo.zendesk.com/hc/article_attachments/28723630073115)

If you select the YES path, all components formerly after the rejoin will shift beneath the YES side of the split when you click ****Disconnect****.

If you select the NO path, the opposite is true — all components formerly after the rejoin will shift beneath the NO side of the split when you click ****Disconnect****.

****![A user disconnects a joined split](https://klaviyo.zendesk.com/hc/article_attachments/28723624751899)****

## Additional resources

- [Understanding the absolute flow timeline and rejoining splits](https://help.klaviyo.com/hc/en-us/articles/360051127672)
- [Understanding time delays near splits](https://help.klaviyo.com/hc/en-us/articles/360050334651)
- [Understanding how contacts move through a flow](https://help.klaviyo.com/hc/en-us/articles/360017706091)