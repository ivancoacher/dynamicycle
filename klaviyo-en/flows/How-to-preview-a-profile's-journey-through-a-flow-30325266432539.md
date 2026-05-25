---
id: "30325266432539"
title: "How to preview a profile's journey through a flow"
source_url: "https://help.klaviyo.com/hc/en-us/articles/30325266432539-How-to-preview-a-profile-s-journey-through-a-flow"
section: "Test and optimize flows"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-04-21T13:54:38Z"
language: "en"
---
## You will learn

Learn how to use the flow preview feature to see how specific profiles will move through a flow. This can help you check that a new flow will work the way you intend before setting it live or troubleshoot issues with an existing flow.

While in preview mode, you can choose specific profiles to learn:

- Whether or not they will enter the flow.
- Which path they will take for conditional and trigger splits.
- Which actions (e.g., messages) they will receive or skip.
- How long they will wait based on time delays.

You cannot edit a flow while in preview mode.

Some flow types are not available for preview:

- - Date-triggered flows
  - Price drop flows
  - Low inventory flows
  - Flows with greater than 500 actions (e.g., messages, notifications, profile property updates, etc.)

## Preview a flow

1. In the top right of the flow builder click ****Preview****.

   ![](https://klaviyo.zendesk.com/hc/article_attachments/46630034996123)

   You can also enter preview mode by clicking ****Update status**** ****> Preview****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/30760055291035)
2. On the right side, select a profile under **Suggested profiles** or search for a profile using the search bar. Suggested profiles are those that recently took an action that would trigger the flow.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/30760009918235)

## Understand the profile preview

The profile preview is based on what is currently known about the profile. Keep in mind that whether or not a profile will pass your flow filters can change as a person takes actions (e.g., placing orders or opening emails). Because of this, a profiles actual movement through a flow may differ from the preview if their profile data changes.

After selecting a profile, you will see the path the profile will take on the flow canvas. The actions that the profile will reach are highlighted and you can see a timeline of their path in the sidebar.

After selecting a profile, the timeline of the path the profile will take will show on the right. You can click on any of the action names on the timeline to center the relative action card on the canvas.

There are several actions you can take on the timeline:

- Click the email address of the profile at the top to open their profile page.
- Click ****View details**** under the trigger to see which filters the profile would pass or fail.
- Click ****Edit content**** under one of the messages to enter the corresponding editor.

  ![](https://klaviyo.zendesk.com/hc/article_attachments/46630005579803)

If a profile wouldn’t enter the flow, you’ll see the **Doesn’t enter** badgenext to the trigger in the timeline.

![](https://klaviyo.zendesk.com/hc/article_attachments/46630005585051)

Preview mode has a few limitations:

- The preview doesn't check subscription status. If a profile’s status is unsubscribed, the preview will still show how they'll move through the flow as if they resubscribed.
- Profile updates in the flow itself will not reflect in filters or splits within the preview. In other words, if you have an update profile property action in the flow and splits or filters based on that profile property, the preview cannot accurately reflect how the changes affect the profile's path.

## Additional resources

Learn more about testing your flow:

- [How to preview a flow trigger setup](https://help.klaviyo.com/hc/en-us/articles/360028374111)
- [How to test and preview flow messages](https://help.klaviyo.com/hc/en-us/articles/115002774972)