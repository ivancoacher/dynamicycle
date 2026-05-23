---
id: 40939669530011
title: "Getting started with omnichannel campaigns"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/40939669530011-Getting-started-with-omnichannel-campaigns"
section: "Getting started with campaigns"
category: "Campaigns"
category_slug: "campaigns"
klaviyo_updated: "2026-04-20T16:50:37Z"
language: en
---

Learn how to create and send an omnichannel campaign, which is a campaign that contains multiple messages across one or more channels.

With an omnichannel campaign, you can send multiple messages related to a specific topic or event over a period of time. An omnichannel campaign can have multiple paths, sending different messages based on the audience. This way, you can tailor your messages for different groups, such as VIP customers, standard customers, churn risks, etc.

## Omnichannel campaigns vs. flows

Both omnichannel campaigns and flows can send multiple messages to your customers across different channels, but there are some key differences.

|  |  |  |
| --- | --- | --- |
|  | ****Omnichannel**** | ****Flows**** |
| ****Initiative**** | Proactive | Reactive |
| ****Reach**** | Wide | Specific |
| ****Complexity**** | Simple | Complex |
| ****Components**** | Messages only | Various actions |

For example, campaigns can be used to inform customers about an upcoming seasonal sale whereas flows can be used to send customers information about their order after they’ve made a purchase.

If you believe flows would be a better fit for your situation than an omnichannel campaign, learn more about [getting started with flows](https://help.klaviyo.com/hc/en-us/articles/115002774932).

****Omnichannel campaign benefits****

- ****Proactive****
  Messages are scheduled directly by you, typically to notify customers of an upcoming or ongoing promotional event, limited-time deal, or product release.
- ****Wide reaching****
  Messages can be sent across multiple lists or segments.
- ****Straightforward****
  You decide who to send to, how many messages, and when to send them.
- ****Message-driven****
  Campaigns can only contain messages.

****Flow benefits****

- ****Reactive****
  Flows are triggered based on your customers such as:
  - Actions your customers take like adding an item to their cart or placing an order.
  - When your customers enter a specific list or segment.
  - Date properties applied to your customers for events relevant to them such as birthdays or first purchase anniversaries.
- ****Specific****
  Messages are sent only to customers who have fulfilled specific criteria based on the trigger and filters.
- ****Potentially complex****
  While flows can be simple, they can also involve complex logic using filters and splits to determine which messages a customer should or shouldn’t receive based on properties about them or the event that triggered the flow.
- ****Versatile****
  Flows can do more than send messages to customers. They can be used to perform other actions such as adding or editing profile properties, changing list membership, or even sending internal alerts to you. These actions can be used alongside or without customer messages at all.

## Before you begin

If this is your first time sending a campaign in Klaviyo, it’s best to start with a single message campaign first. Learn the basics of the different types of campaigns below.

- [Email campaign](https://help.klaviyo.com/hc/en-us/articles/115005054847)
- [SMS campaign](https://help.klaviyo.com/hc/en-us/articles/360040039971)
- [Push notification campaign](https://help.klaviyo.com/hc/en-us/articles/360006653972)

If you plan on sending across multiple channels, make sure you have set up and collected consent for those channels.

### Which channels are available

You can send messages across all channels you’ve set up in your Klaviyo account:

- Email
- SMS
- WhatsApp
- Push notifications

Email is available to all Klaviyo accounts by default, but other channels must be enabled separately.

Messages can only be sent to recipients through a particular channel if they have provided consent for that channel.

## Omnichannel campaign components

An omnichannel campaign has more components than a single message campaign. These components include:

- ****Paths****
  Omnichannel campaigns can have up to 10 paths. Each path has a different audience and set of messages. This allows you to have a single campaign that sends different messages to separate groups of customers. One path is automatically added to the campaign by default.
- ****Audiences****
  Each path has its own audience. You can choose any lists and segments in your account to include or exclude as part of an audience.
- ****Messages****
  Each path can have multiple messages across different channels in your account. The number of messages and channels can be different per path. You can have up to 30 messages total for the campaign. Each path can have any number of messages so long as they are within the 30 message campaign limit.

## Start a new omnichannel campaign

Klaviyo’s campaign wizard guides you through the steps for creating your campaign.

1. Navigate to the ****Campaigns**** tab.
2. Click ****Create campaign.****
3. Name your campaign. This can be changed later.
4. Select ****Omnichannel.****
5. Click ****Continue****.

## Edit campaign details

You can change the name, tags, and description of a campaign at any time. These details help you organize campaigns in your account and are not visible to the campaign’s recipients.

To edit a campaign’s details:

1. Navigate to the ****Campaigns**** tab.
2. Click the action button (3 dots) to the right of the campaign you want to edit and select ****Edit details**** or click the name of the campaign and click the action button in the top right and select ****Edit details****.
3. Change the name, select tags, add a description, and change the calendar color. Other than the campaign name, all fields are optional.
4. Click ****Save****.

## Adjust sending settings

Sending settings can only be edited for campaigns that haven’t been scheduled. If 1 or more messages are scheduled, sending settings will be temporarily locked unless you revert all scheduled messages to drafts. Sending settings will be permanently locked for that campaign if 1 or messages are sent.

Determine what time zone to use for your campaign.

1. On the campaign canvas, click the action button (3 dots) in the top right and select ****Sending settings****.
2. Choose a specific timezone to send this campaign in or select ****Recipient’s Local Time Zone****.
3. If you select to send in the recipient’s local time zone, select when the campaign should send if the scheduled date and time of the campaign has already passed in the recipient’s timezone. For example, if you set a campaign message to send on July 1st but it is already July 2nd in some time zones, you can either have the message sent immediately or sent the following day for customers in those time zones.

## Choose your audience

Select your target audience for the campaign. A campaign message needs at least 1 recipient in order to send, otherwise it will be automatically canceled.

1. On the campaign canvas, click ****Select audience**** for a campaign path.
2. Name your audience if you’d like to differentiate it from the audiences of other paths.
3. In the **Send to** field, select lists and segments to make up your audience for messages in this path.
4. Optionally, in the **Don’t send to** field, select lists and segments to exclude from this path.
5. Click ****Save and return****. The amount of people in this path’s audience will display on the campaign canvas.
6. Repeat these steps for other campaign paths.

## Add messages

Add messages to each path of your campaign.

1. Click the plus (+) icon to the right of the audience of a path.
2. Select the channel of the message. Only channels set up in your account will be available.
3. If applicable, select a template. Edit the message content and sender details.
4. Click ****Save and return****.
5. On the campaign canvas, schedule the message through the right sidebar. If this sidebar isn’t visible, click on the message you want to schedule.
6. Choose a date and time to send the message. The timezone will be based on your sending settings. Messages will be ordered by send date on the campaign canvas with the earliest messages appearing on the left.
7. Click the ****Settings**** tab to change the name and tags of the message for organizational purposes, and turn on or off [Smart Sending](https://help.klaviyo.com/hc/en-us/articles/115002779311) and [UTM parameters](https://help.klaviyo.com/hc/en-us/articles/360053921252).
8. Click the ****Review**** tab to view warnings and errors that indicate potential issues with this message based on the audience content, and settings.

   - Errors are indicated by a red circle and are issues that prevent a campaign send.
   - Warnings are indicated by a yellow triangle and represent areas that can be improved but won’t stop the campaign from sending.
9. Click ****Edit**** to address any of the warnings. Otherwise, move to the next step.
10. Click ****Schedule****.
11. Select a scheduling option.

    - ****Fixed send time**** will send the message to all recipients at once.
    - ****Gradual send over several hours**** will send the message to a percentage of your audience each hour until it reaches 100%. Select a percentage per hour from 10%-50%.
12. Confirm the date and time then click ****Schedule message****.
13. Repeat these steps for each message in the campaign.

## Edit, clone, or delete messages

To edit, clone, or delete a message:

1. Click the action icon on the message card.
2. Choose an option:

- ****Edit message**** to enter the template editor.
- Click ****Clone**** and select the path you want to clone the message to.
- Click ****Delete**** and click ****Delete**** again to confirm.

Deleting a message is permanent. It cannot be restored after deletion.

## Add additional paths

If you’d like to send messages to different audiences, add another path to your campaign.

1. Either click ****Add path**** at the bottom of the campaign canvas or click the ****clone**** icon to the left of an existing path.
2. Click the arrows to the left of a path to reorder its place on the canvas.
3. Repeat these steps to add up to 10 paths.