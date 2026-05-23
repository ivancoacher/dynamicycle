---
id: 360002732652
title: "How to create a date property-triggered flow"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360002732652-How-to-create-a-date-property-triggered-flow"
section: "Lifecycle flows"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-04-21T13:54:42Z"
language: en
---

## You will learn

Learn how to set up a date property to trigger a flow, which is a great way to set up a flow sequence around key dates you collect from subscribers. Common examples of date property-triggered flows include:

- Birthday
- Anniversary
- Appointment
- Subscription date
- Wedding date
- Pregnancy due date
- Reorder product

In this article, we go over date property-triggered flows, including how they work and how to set one up.

## Accepted date formats

Date-based flows are triggered by a date that is stored as a property within a profile. For example, a birth date can be stored as a [custom property](https://help.klaviyo.com/hc/en-us/articles/115005074627) that you name as “birthday.”

When collecting date properties from your customers, the date needs to be in one of [Klaviyo’s accepted date/time formats](https://help.klaviyo.com/hc/en-us/articles/115005253428) in order to trigger a flow; e.g., YYYY-MM-DD or MM/DD/YYYY. If the date is not in the correct date/time format or is listed in the text format, it will not appear as an option in, for example, a date-triggered flow. The easiest way to collect date properties in a valid format is to use Klaviyo [sign-up forms](https://klaviyo.zendesk.com/hc/en-us/articles/360026474752).

You can use a sign-up form to collect dates in DD-MM-YYYY or DD/MM/YYYY format, and they will be automatically converted to an accepted date format.

When you don't see the date you want, this likely means that either there are no profiles with that property yet or the dates are improperly formatted. Check that at least one profile has that date and that it is formatted correctly.

If no profiles have that property yet, try adding it to a test profile. If that doesn’t work, or you see profiles with the correct date property already, please contact Klaviyo support to resolve this issue.

## Create a date-based flow

To create a date property-triggered flow:

1. Navigate to the ****Flows**** tab.
2. Click ****Create flow****. This will take you to the flow library where you can find pre-built birthday and anniversary flows. You can find these flows by searching via the toolbar at the top of the library.
3. Either select a pre-built flow or create one from scratch. To build it yourself, click ****Build your own**** and choose the ****Date property**** option as the trigger.
   ![In the list of flow triggers, the Date Property option can be found at the bottom](https://klaviyo.zendesk.com/hc/article_attachments/28720892293915)

When you first choose the date property trigger, you will be prompted to select which specific property you would like to trigger the flow. All date-based profile properties in your account will appear in the dropdown menu for selection.

After you configure an initial date property trigger, you cannot edit the date property you selected. To update the flow with a new date trigger, you will need to [clone the flow](https://klaviyo.zendesk.com/hc/en-us/articles/24898429283739).

![From the Trigger Setup menu, you can choose a date property from the dropdown such as a Birthday property if it exists in your account](https://klaviyo.zendesk.com/hc/article_attachments/28720847149851)

## Pick when the flow will start

After selecting a date-based profile property, you will need to choose when the flow should start: on or before the actual date. For example, a birthday flow can start sending messages to a recipient two weeks before their actual birthday. You can also have the flow begin after the date; for this, start the flow on the date and then add a time delay.

If you choose to start the flow before the date, you can select any number of days, weeks, or months in advance. This will automatically produce an anchor point (called the target date delay component) on the actual date. The anchor point works similarly to a time delay component except that instead of delaying for a certain amount of time, it delays until a certain date. This point also helps you keep track of where in the flow the date falls.

![The Yearly option should be selected from the 'When should this flow repeat' section](https://klaviyo.zendesk.com/hc/article_attachments/28720892295451)

There can only be one target date anchor point in a date-based flow. Because of this, and because these flows are designed to reach the target date, any conditional split placed before this anchor point will be automatically rejoined. You will also not be able to disconnect any paths for a split that is before the anchor point.

![A conditional split placed before a 'wait until person's Birthday' anchor point is rejoined before the anchor point.](https://klaviyo.zendesk.com/hc/article_attachments/28720892297499)

## Choose how often the flow will repeat

The final step to setting up a date-based flow is to choose how often the flow should repeat:

- ****Monthly****
  Recipients will qualify to enter this flow on a monthly recurring basis on the same day each month; for example, a monthly subscription reminder series. Note that if you schedule this on the 31st, it will automatically pick up on the last day of the month for any month that has fewer than 31 days.
- ****Yearly****
  Recipients will qualify to enter this flow on a yearly recurring basis on the same month/day; for example, a yearly anniversary or birthday series.
- ****Should not repeat****
  Recipients will qualify to enter this flow only once when the full date matches (day, month, and year); for example, a wedding or pregnancy due date.

## Add flow filters

You can also choose to apply a flow filter during your initial setup to restrict the flow to only certain people, and you can add or adjust these filters at any time. For instance, if you want to have two wedding date flows — one for brides and the other for bridesmaids — you can exclude the brides from the bridesmaids’ flow and vice versa.

![A trigger with the configuration 'Start 9 months before person's Wedding at 12:00p' has the filter 'Interest equals Bride'.](https://klaviyo.zendesk.com/hc/article_attachments/28720892300059)

## Drag in messages and time delays

Next, add any time delays and emails or SMS messages to your flows. Both can go before and after the date anchor point.

![After the anchor point, any other flow components can be added such as a conditional split.](https://klaviyo.zendesk.com/hc/article_attachments/28720892292123)

Note that when using time delays in date-based flows, the component will look different depending on if it’s placed before or after the date anchor point. For more details, read this explanation on [using time delays in date property-triggered flows](https://help.klaviyo.com/hc/en-us/articles/360054705431).

## Set the flow to manual or live

When you’ve set up the flow and configured all the messages, turn the flow to [manual or live](https://help.klaviyo.com/hc/en-us/articles/115002774932#the-flow-action-status9). You can do so via a component-by-component basis or by [bulk updating the statuses for every flow action](https://help.klaviyo.com/hc/en-us/articles/360048376172).

When at least one message is in manual or live mode, Klaviyo will begin to check whether recipients should be added to the flow. Klaviyo checks all profiles in your account daily (and whenever a date is added, updated, or deleted) to ensure that anyone who is due to enter a date-based flow is [queued for the date-based flow](https://help.klaviyo.com/hc/en-us/articles/360054240252). This check runs a full day ahead of time so that no recipients miss out, regardless of what timezone they're in.

## Additional resources

Read more about date-based flows:

- [Understand how date-based flows queue recipients](https://help.klaviyo.com/hc/en-us/articles/360054240252)
- [Understand time delays in date property flows](https://help.klaviyo.com/hc/en-us/articles/360054705431)
- [Building a birthday flow](https://help.klaviyo.com/hc/en-us/articles/360054242492)