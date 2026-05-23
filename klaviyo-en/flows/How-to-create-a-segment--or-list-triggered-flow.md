---
id: 360003040052
title: "How to create a segment- or list-triggered flow"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360003040052-How-to-create-a-segment-or-list-triggered-flow"
section: "Set up flow filters and triggers"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-04-21T13:54:42Z"
language: en
---

Learn how to create a segment- or list-triggered flow and about their re-entry setting.

Segment- and list-triggered flows start whenever someone newly joins a segment or list, respectively. With Klaviyo’s updated flow entry settings, you now have more control over whether (and how often) profiles can enter or re-enter these flows. This makes it easier to support lifecycle messaging, behavior-based automations, and recurring engagement campaigns.

## How segment- and list-triggered flows work

A profile triggers a segment or list-based flow when they newly qualify for the segment or list. For segments, this means:

- The profile was previously not in the segment
  AND
- A data change (such as profile properties or events) causes them to enter the segment organically.

For lists, it's when they first join the list, such as when they join via a form.

### List-specific details

Keep in mind that if you import profiles to a list, it will trigger any list-triggered flows. This means that if you set up a welcome series, and import a list of existing subscribers, those subscribers will enter the welcome series.

To avoid this, turn off any list-triggered flows before importing.

### Segment-specific details

For segments, there are a few important things to keep in mind:

- Manual edits to a segment’s definition do not trigger flows.
  - If you want to push all members of a segment into a connected flow after manually updating the definition, you will need to [add past profiles to the flow](https://help.klaviyo.com/hc/en-us/articles/115002779231).
- A flow triggers only when a profile’s data causes them to organically enter the segment.
- Duplicate activity (e.g., repeated events) will not re-trigger the flow unless segment membership actually changes.
- Recipients will only receive messages within a flow if they are still a member of the connected segment at send time.

## Create a segment- or list-triggered flow

1. Navigate to the ****Flows**** tab in Klaviyo.
2. Click ****Create flow**** and select ****Build your own****.
3. Name your flow and click ****Create flow****.
4. In the Flow Builder, choose ****Added to segment**** or ****Added to list**** as the trigger.
5. Select the segment or list that should initiate the flow.
6. Configure ****Re-entry criteria**** in the trigger settings panel.

## Re-entry settings

If you don't see this setting in your account, stay tuned! This setting will be available for everyone soon.

A segment- or list-triggered flow begins when a profile meets the definition of a segment or joins a list. Profiles can now enter these flows:

- One time only
- Whenever they re-qualify
- After a minimum time period has passed

These options are controlled by a new ****Re-entry criteria**** setting in the flow trigger.

![Re-entry settings for a flow](https://klaviyo.zendesk.com/hc/article_attachments/44565688213659)

You can control how often profiles can enter the flow by adjusting the ****Re-entry criteria**** in the trigger panel. Your options include:

|  |  |  |
| --- | --- | --- |
| Setting | Description | Use case |
| No re-entry | Profiles will enter the flow only once. | Welcome series  Legal or compliance notifications |
| Allow re-entry | Profiles will re-enter the flow whenever they newly qualify for the list or segment. | Lifecycle flows  Behavior-based-segment flows where messaging should repeat over time. |
| Allow re-entry after a time period | Profiles will re-trigger the flow when they newly qualify **and** the selected time period has elapsed since their last entry. | Retention flows  Winback flows. |

Re-entry criteria now serves as the single source of truth for flow entry behavior. You no longer need to add “has not been in flow” filters to control frequency.

### Default settings for new flows

When you create a new flow, Klaviyo applies default re-entry settings based on the trigger type:

|  |  |  |
| --- | --- | --- |
| ****Trigger type**** | ****Default re-entry setting**** | ****Notes**** |
| Segment | No re-entry | Customer can change to allow re-entry or time-based re-entry |
| List | No re-entry | Same defaults as segment |
| Metric (e.g., **Order Placed,** **Viewed Product**, **Price Drop**, L**ow Inventory**) | Allow re-entry | Includes Price Drop and Low Inventory |
| Date Property | Allow re-entry | Behavior unchanged; repeats when date updates or repeats annually |

You can adjust these defaults at any time.

### Paths that do not trigger re-entry

Re-entry only happens when a profile’s data causes segment or list membership to change. The following do not trigger a flow:

- Manual edits to segment rules
- Manually adding profiles to a list or segment
- Merging profiles or lists
- Duplicate subscription or event activity where the profile was already in the segment
- Integrations that intentionally add profiles without triggering flows

### FAQs

#### Does "Add Past Profiles: re-trigger the flow?

No. Adding past profiles does not count as new qualification and does not re-trigger the flow. Profiles must organically meet the segment conditions for the flow to run again.

#### Previously I could not re-trigger my flows. What happens with my existing Flows?

Existing flows retain behavior consistent with how they functioned before the new settings were introduced. Their configurations are automatically translated into the new system.

#### Existing behavior → New re-entry setting

- List or segment flow with no re-entry filters → ****No re-entry****
- Event (metric) flow with no re-entry filters → ****Allow re-entry****
- Metric flow with a “has not been in flow in all time” filter → ****No re-entry****
- Metric flow with a “has not been in flow in X days” filter → ****Allow re-entry after a time period (X days)****

#### Will this change how often my flow sends?

No, unless you adjust the re-entry criteria.

#### Can I restrict profiles to entering only once?

Yes. Set the re-entry criteria to ****No re-entry****.

#### Can I control re-entry for metric-triggered flows?

Yes. Re-entry is now managed the same way for all flow types directly in the trigger settings.

Learn about other flow types: