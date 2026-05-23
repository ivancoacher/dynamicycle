---
id: 115002779051
title: "Understanding flow triggers and filters"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115002779051-Understanding-flow-triggers-and-filters"
section: "Set up flow filters and triggers"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-04-21T13:54:13Z"
language: en
---

## You will learn

Learn more about Klaviyo filters which can be used to further narrow triggers or actions in flows. For example, if a flow triggers when someone places an order, a trigger filter could be added to limit this to specific product types. Trigger filters are evaluated alongside the trigger itself to only let certain people into a flow.

If you want to target a very specific behavior or group of people, you can use a more general profilefilter. Profile filters are applied when people enter your flow, as well as before every email in the flow is sent. In this way, profile filters ensure that only people that still qualify continue moving through a flow.

![](https://fast.wistia.com/embed/medias/8s56bimjlj/swatch)

## Flow trigger

A flow can be triggered:

- When someone takes an action (metric) that is tracked by Klaviyo, such as placing an order
- When someone is added to a list or segment
- Based on a date property attached to a contact's profile
- When an item someone viewed or started checkout with lowers in price by a certain amount or percent
- Based on a date property attached to custom object associated to a contact's profile

Someone will qualify to enter the flow as soon as they meet the trigger action.

![trigger1.jpg](https://klaviyo.zendesk.com/hc/article_attachments/39870603886747)

Here is a list of the 6 different types of triggers and when they might be used:

- [****Added to list****](https://help.klaviyo.com/hc/en-us/articles/360003031652-Create-a-List-Triggered-Flow)
  If you have a sign-up form(s) or a subscribe page on your website, you likely add all new subscribers to a list in Klaviyo. Using the list trigger, you can ensure every new subscriber is queued to receive a series of automated emails from you. For example, you can use a welcome series to send an email immediately when someone signs up and then automate 2 or 3 other emails, each a few days apart.
- [****Added to segment****](https://help.klaviyo.com/hc/en-us/articles/360003040052-Create-a-Segment-Triggered-Flow)
  Segments are defined by a set of conditions, and will thus grow as new people meet the conditions and shrink when certain people no longer do. Triggering a flow based on when someone new is added to a segment will allow you to ensure everyone who meets a certain set of conditions will be queued for this flow. This can be useful when you want to use multiple actions to trigger a flow.
- [****Metric****](https://help.klaviyo.com/hc/en-us/articles/360003057151-Create-a-Metric-Triggered-Flow)
  This trigger option allows you to queue people for a flow when they take a certain action. This action can be any event activity captured through an integration (e.g., started a checkout, placed an order, filled out a form) or events created via the Klaviyo API. For example, an abandoned cart flow would trigger off the**Started Checkout**event, with an additional profile filter to restrict the flow only to those who have not followed through with placing an order.

  Performance metrics such as **Opened Email** and **Clicked Email**cannot be used to trigger flows.
- [****Date property****](https://help.klaviyo.com/hc/en-us/articles/360002732652-Create-a-Date-Property-Triggered-Flow)
  You can build an automated flow that starts on a specific date, or you can instead choose to set a flow in motion before a specific date**.**A person will qualify to enter a date property-triggered flow whenever the date property is added or updated on their profile or a custom object associated to their profile. This can be useful if you're creating a flow that centers on a specific date, like a birthday or anniversary. Additionally, these flows can recur on a monthly or yearly basis.
- [****Price drop****](https://help.klaviyo.com/hc/en-us/articles/4404249033755)
  A price drop flow allows you alert people when an item they viewed or started checkout with drops in price. The price drop can either be a set amount (e.g., $10) or a certain percentage (e.g., 20%).
- [****Low inventory****](https://klaviyo.zendesk.com/hc/en-us/articles/21374913673243)
  A low inventory flow allows you alert people when an item they viewed or started checkout with is low in stock. The low inventory amount can be specified based on a specific product variant or the entire product stock.

Apple Mail Privacy Protection (MPP), which was released with iOS15 and updates to other Apple devices, may lead to inflated open rates due to changes in how we receive open rate data.

If you are triggering flows off of opens themselves, we suggest creating a [custom report](https://help.klaviyo.com/hc/en-us/articles/4416803987739) that includes an MPP property to review these affected opens. You can also identify these opens in your individual [subscriber segments](https://help.klaviyo.com/hc/en-us/articles/4416791883163).

After selecting the flow trigger, you will be prompted to choose the specific list, segment, event, or date property. You will then see options to restrict further who gets emails from your flow, which are the trigger and profile filter.

### Re-Entry for Flow Trigger Control

In addition to using filters to refine when people enter or continue through a flow, Klaviyo now offers Re-entry criteria directly in the flow trigger settings. This gives more intuitive and consistent control over how often profiles can enter (or re-enter) flows, without needing separate “has not been in flow” filters.

Key benefits:

- Control flow entry frequency across all trigger types (including segment and list triggers).
- Choose whether profiles:

  - Enter only once
  - Re-enter whenever they re-qualify
  - Re-enter after a minimum time period
- Simplifies flow behavior management by centralizing entry controls.

For full details, examples, and how to configure Re-entry in your flows, see: [How to create a segment- or list-triggered flow](https://help.klaviyo.com/hc/en-us/articles/360003040052#h_01KCSCGDJ87DQP0XM8P3A2BT0K)

## Setting filters

### Trigger filters

If you select a specific metric (e.g., **Started Checkout**, **Placed Order**, etc.) or a custom object (e.g., **Renewal Date, Appointment Date,** etc.) to trigger the flow, by default, everyone who completes this action or meets the flow's starting (for date-based object flows) will qualify to enter your flow. Similarly, price drop flows will alert everyone who looked at or began checkout with an item when it lowers by the amount you set.

You can use trigger filters to narrow the scope and target only a subset of these contacts. Trigger filters evaluate the data coming in from the event or the custom object that triggers the flow, and not profile properties, meaning only metric-based flows, custom object-based flows and price drop flows can have trigger filters.

Metric-based trigger filters are only checked when an individual first enters the flow. Custom Object trigger filters  are checked at every step in the flow. A trigger filter is useful for grabbing only certain events for your triggering metric. For example:

- ****Post-purchase cross-sell****
  You may have a particular category of items (Category A) that is often purchased alongside another category (Category B). To turn a post-purchase flow into a targeted cross-sell opportunity, use the **Placed Order**metric as your trigger, but then use a trigger filter so only orders that included Category A and **didn't include** Category B qualify for your flow.
- ****High-value item browse abandonment****
  Browse abandonment flows can help you convert casual window shoppers into customers by following up with those that view items on your site but never start a checkout or purchase. You may not want to trigger browse abandonment emails for every item in your catalog, however. You may want to limit the scope of this follow up for high-value products only. Trigger your flow using the **Viewed Product** metric, but use a trigger filter to specify that only items with a value over X amount with qualify for the series.
- ****Post-purchase thank you and tips****
  Certain items you sell may require some how-to instructions, or otherwise warrant a targeted post-purchase message. For a flow triggered by your **Placed Order** metric, use a trigger filter to target the purchase of just a specific item to give these customers the personalized follow-up they need.

![](https://klaviyo.zendesk.com/hc/article_attachments/28717810093723)

### Profile filters

Profile filters are useful when you'd like to target specific subscriber behaviors or attributes. Profile filters operate at the profile level, meaning they will evaluate whether or not someone qualifies based on properties about them or actions they have previously taken.

Profile filters are checked when someone first enters a flow and before each action takes place (e.g., before any email or SMS sends or a profile property is updated). If someone fails an element in a flow, they will continue to move through the flow, but they will be skipped from each step until they exit the flow. We will reevaluate them each time they hit another “actionable” element (i.e., email, SMS, and/or notification). If the subscriber fails the initial trigger, they will simply not start the flow itself.

The **Re-entry criteria** is only checked when someone enters the flow organically. Since it is checked only at the beginning, it does not check at every step. To see who entered the flow but failed the profile filter before an action, navigate to ****Analytics (Last 30 Days) > Recipient Activity >**** ****Other****. Here, you will find the **Skipped: Fails Profile Filters** bucket.

Abandoned cart flows, for example, are built on the **Started Checkout**metric. The behavior you want to target, however, is when a customer starts a checkout and then abandons the process. This means you have to add a profile filter to target this specific behavior: **Has placed order zero times since starting this flow**. This will ensure that people only receive a flow email after they started a checkout but did not place an order.

You can also use multiple filters if you'd like — the example below demonstrates a flow that would only send to people that have not placed an order since starting the flow and live in the United States.

![](https://klaviyo.zendesk.com/hc/article_attachments/28717849740315)

If someone is skipped due to failing profile filters, this person will still move forward and be scheduled for the next step. We do not remove someone from a flow completely if they fail the flow's filters at a single step; contacts will continue to be scheduled for the next step. Due to the nature of some profile filters, if someone is skipped once, they will continue to be skipped for all subsequent steps. However, this is not true for all profile filters. For some, the evaluation could change as someone moves through a flow. For this reason, to keep behavior consistent, we do not remove someone from a flow completely if they fail the flow's filters at a single step.

### Options for filter conditions

This dropdown menu for filters shows all the top-level properties available for a flow. After choosing a property, add your value. A value will only show up if it has synced to Klaviyo along with a tracked event (e.g., **Placed Order)** or that exists on someone's profile. If your desired value isn't displayed, copy and paste it into the empty valuebox. If the property value you paste is identical to the value that will eventually sync to Klaviyo, the flow will work as expected.

Filters look for exact keyword matches. In other words, when using "equals", "doesn't equal", "contains" or "doesn't contain" options, the followed dimension value must match what you're looking for exactly. For example, if you are filtering for **Language equals English**, then you must input "English". If you have "en" as a possible value, you can add a separate filter for this.

Only certain synced properties are available in a flow. For data management purposes, only the most important details of an event are synced as "top-level" properties, and only these top-level properties are available to filter a flow.

If you [view the raw data](https://help.klaviyo.com/hc/en-us/articles/115005076747) Klaviyo syncs for an event, you will see key data points for the event. A **Placed Order** event, for example, includes the top-level properties listed below:

- Value
- Collections / Categories
- Item Count
- Items
- Source Name

You will see an array labeled **Extra** or **Details**. You cannot use this data in a flow, although you can [insert it into an email template.](https://help.klaviyo.com/hc/en-us/articles/115005084927)

## Setting an additional filter for a single flow message

Adding additional filters to an email or SMS within a flow allows you to tailor specific messages after a person has set off a broader trigger. Additional filters are similar to profile filters in that they also operate at the profile level, meaning they will evaluate whether or not someone qualifies based on properties about them or actions they have previously taken. The crucial difference is that they only apply to a single message within the scope of the entire flow.

For example, you may want everyone to receive the first SMS in your welcome series after they sign up, but you may not want those who have made a purchase since starting the flow to receive the fifth email. Additional filters allow you to narrow your audience for a single message. If someone is skipped by this type of filter, they will continue in the flow.

1. Click on the message card.
2. In the email details panel, scroll down to the **additional filters** section.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28717849742235)
3. Set up the filter conditions the same way you would a profile filter.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28717849747099)
4. Click ****Save**** at the bottom of the panel.

Let's say you have a flow that sends to customers several weeks after their first purchase encouraging them to order again. Your first message might include, "We Missed You." This message may also provide a discount code or some other incentive to convince your customer to come back.

As you add more actions to this flow, you may want to consider sending certain messages only to those that have failed to open a prior message. This is a great way to resend a great offer or partially recycle a great design until you grab the attention of your customers.

As an example, for email, this additional filter will consist of one condition:
**What someone has done (or not done) > has Opened Email zero times over all time**
**> where Subject equals \_\_\_\_\_\_**

## Additional resources

- [Understand AND vs. OR](https://help.klaviyo.com/hc/en-us/articles/360036534631-AND-vs-OR-Guide)
- [How to preview a flow trigger setup](https://help.klaviyo.com/hc/en-us/articles/360028374111-Preview-a-Flow-Trigger-Setup)
- [How to change a flow trigger](https://help.klaviyo.com/hc/en-us/articles/115002775052-Change-a-Flow-Trigger)