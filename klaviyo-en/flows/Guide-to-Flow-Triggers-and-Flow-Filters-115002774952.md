---
id: "115002774952"
title: "Guide to Flow Triggers and Flow Filters"
source_url: "https://help.klaviyo.com/hc/en-us/articles/115002774952-Guide-to-Flow-Triggers-and-Flow-Filters"
section: "Set up flow filters and triggers"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-04-21T13:54:12Z"
language: "en"
---
## ![680827](https://klaviyo.zendesk.com/hc/article_attachments/28715968140699)The Flow Trigger

A flow can be triggered when someone takes an action that is tracked by Klaviyo, or when someone is added to a list or segment. When a user meets the trigger you set, they will enter your flow at that time.

![636305](https://klaviyo.zendesk.com/hc/article_attachments/28715968145563)

Here is a list of the three different types of triggers and when they might be used:

- ****Subscribes to a list:**** If you have a sign up form(s) or a subscribe page on your website, you likely have all new subscribers getting added to a specific list in Klaviyo. Using this "Subscribes to a list" trigger, you can ensure every new subscriber gets queued up for a specific flow. For example, you can use a Welcome Series flow to send a thank you email to someone once they sign up for your Newsletter list.
- ****Added to a segment:**** Segments are defined by a set of conditions, and will thus grow as new people meet the conditions and shrink when certain people no longer do; triggering a flow based on when someone new is added to a segment will allow you to ensure everyone meeting a certain set of conditions will get queued up for this flow. This can be useful for when you want to use multiple actions to trigger a flow. Keep in mind, however, that even if someone exits a segment when they don't meet the condition anymore and then enters the segment again a later date - segment-triggered flows cannot be sent to the same person more than once. So segment-triggered flows cannot be used to automate order-related follow up emails or any other emails you might want someone to receive more than once.
- ****Takes an action:**** This trigger option allows you to cue up people for a flow based on an action they have taken; this action can be any activity captured through an integration (i.e. started a checkout, placed an order, filled out a form). For example, an Abandoned Cart flow would trigger off the action "Checkout Started", with an added trigger filter to restrict the flow only to those that have also not yet completed this checkout.

After selecting **Subscribed to List** or **Added to a Segment**, you will be prompted to select a list/segment name and then see options to restrict further who gets emails from your flow.

After electing **Takes an Action**, you will be prompted to select an action metric to trigger the flow. You will then have the opportunity to add one or more filters to that action.

## Setting Trigger Filters

A trigger filter is useful for grabbing only certain events for your trigger metric. If you want to create an "Customer Thank You" flow that is targeted only to customers that have purchased a specific product, you can specify "Only certain events should trigger this flow" and establish that the flow should only trigger when the order placed includes this specific product.

This allows you to tailor different flows to send different emails to people who - for example - buy a red t-shirt versus those who buy a blue t-shirt, or to people whose orders are a certain size or value. There are many different Trigger Filters for each event metric in Klaviyo. The Trigger Filter will only get applied as someone enters a flow - as it applies directly to the trigger itself.

![636306](https://klaviyo.zendesk.com/hc/article_attachments/28715968149147)

## Setting Flow Filters

Flow filters are useful when you'd like to target specific behaviors with your flows.

Abandoned Carts flows, for example, are built on the action metric Checkout Started. The behavior we want to target, however, is when a customer starts a checkout and then abandons the process. This means we have to add a flow filter to target this specific behavior. The flow filter we need here is: has placed order zero times since starting this flow. This will make sure that people only receive a flow email after they started a checkout but did not go on to place an order. You can use multiple filters here if you'd like - the example below features a flow that would only send to people that have not placed an order since starting the flow and live in the United States.

![636308](https://klaviyo.zendesk.com/hc/article_attachments/28715968151323)

Here are a few examples of how Flow Filters can help you "level up" your automated emails to get highly targeted and personalized:

- For a Welcome Series, have Email #1 only send to subscribers that opted-in through a certain pop up on your website
- For an Abandoned Cart flow, create separate flows for products that are particularly popular, or for certain categories of products - this way, you can customize these emails to maximize their conversion potential
- For a Winback flow, you can send a "big spender" version of your winback series to customers that placed an order above a certain amount, or customize winback flows based on the category of products purchased
- For a New Customer Thank You flow, this is a great opportunity to "thank" your customers in different ways based on what they bought/how much they spent - you can create different Thank You flows based on any information you know about your customers, such as their gender, location etc.

## Should I use AND or OR when adding filter conditions?

Using the ****OR**** connector between a sequence of flow filter conditions will make a filter more ****inclusive****. We will check each condition in the sequence individually - if Joe meets one condition in the sequence but does not meet another, Joe will still be included in your flow.

In the following example, anyone that placed an order in the last 30 days OR was active on site in the last 30 days will get included:

![636310](https://klaviyo.zendesk.com/hc/article_attachments/28715961548315)

Using the ****AND**** connector between conditions will make a flow filter more ****exclusive****. We will check each condition separated by AND individually, but each condition must evaluate to true in order for someone to get included. If Joe meets one condition but doesn't meet another, Joe will be excluded from your flow.

In the following example, only those that placed an order in the last 30 days AND were active on site in the last 30 days will get included:

![636312](https://klaviyo.zendesk.com/hc/article_attachments/28715968155035)

## When are Flow Filters Applied?

The way a flow works, everyone captured by the initial trigger (i.e. Checkout Started) will get queued up to enter the flow. All trigger filters AND flow filters will be applied at this time as well, however:

- If someone fails the trigger and/or flow filters at this time, they will get filtered out and will not get queued up for any flow emails
- Everyone that passed the trigger and flow filters (initially) will enter the flow and get queued up for all emails at this time

When each email is scheduled to send, however, Klaviyo will apply your flow filters again (i.e. has Placed Order zero times since starting this flow) and skip anyone that fails your filters. This is why you may see people queued up for your flow in "Waiting" that you know shouldn't receive the flow's emails. Flow filters will always get applied again right before each email sends.

![636313](https://klaviyo.zendesk.com/hc/article_attachments/28715961565467)

If you explore the Recipient Activity for a flow email, by clicking on **Analytics (Last 30 Days) > Recipient Activity,** you will see the number of total recipients. If you click on the 'Other' dropdown, you will see the number of individuals falling into the "Skipped: Fails Flow Filters" bucket. This shows you those that entered the flow but failed the flow filters at email send time.