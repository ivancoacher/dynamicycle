---
id: "35146374047515"
title: "How to use custom objects in flows"
source_url: "https://help.klaviyo.com/hc/en-us/articles/35146374047515-How-to-use-custom-objects-in-flows"
section: "Use objects in Klaviyo"
category: "Content"
category_slug: "content"
klaviyo_updated: "2026-04-21T13:54:41Z"
language: "en"
---
You must have access to [custom objects](https://help.klaviyo.com/hc/en-us/articles/35105337172123) to use this functionality.

## You will learn

Learn how to use custom objects in flows, so you can use object data to create date-triggered flows and set up conditional splits.

Note that you must [create an object](https://help.klaviyo.com/hc/en-us/articles/35105337172123) first before you can use custom object data in flows.

## Date-triggered flows

Date-triggered flows enable you to automatically send messages based on date properties in an object (e.g., a child’s birthday, a pet’s adoption date, the expiration date of a product warranty, an upcoming restaurant reservation, etc.).

Learn [how to create a date-property triggered flow](https://help.klaviyo.com/hc/en-us/articles/360002732652) in Klaviyo.

![](https://klaviyo.zendesk.com/hc/article_attachments/35159460537243)

### Create a flow from the library

You can quickly get started with date-triggered flows based on object properties by selecting a flow from the flow library.

To select a flow from the library:

1. Navigate to the ****Flows**** tab.
2. Click ****Create flow****. This will take you to the flow library where you can find pre-built birthday and anniversary flows. You can find these flows by searching via the toolbar at the top of the library.
3. Select a pre-built flow that uses a date-trigger. For example, you can select a flow like the **First Purchase Anniversary**.
4. In the **Trigger** field, select the date-based object property you want to trigger your flow.

![](https://klaviyo.zendesk.com/hc/article_attachments/35159469077147)

### Create a flow from scratch

To create a date-triggered flow from scratch:

1. Navigate to the ****Flows**** tab.
2. Click ****Create flow****.
3. Click the ****Build your own**** button and choose the **Date property** option as the trigger.
4. Select your date-based object property for the flow trigger.

![](https://klaviyo.zendesk.com/hc/article_attachments/35159469080091)

### Configure the date trigger

To configure the date trigger for your flow, select whether the flow should start on or before the actual date. For example, an anniversary flow can start sending messages to a recipient leading up to their actual birthday. You can also have the flow begin after the date by adding a time delay.

Additionally, choose how often the flow will repeat:

- ****Monthly****
  Recipients will qualify to enter this flow on a monthly recurring basis on the same day each month; for example, a monthly subscription reminder series. Note that if you schedule this on the 31st, it will automatically pick up on the last day of the month for any month that has fewer than 31 days.
- ****Yearly****
  Recipients will qualify to enter this flow on a yearly recurring basis on the same month/day; for example, a yearly anniversary or birthday series.
- ****Should not repeat****
  Recipients will qualify to enter this flow only once when the full date matches (day, month, and year); for example, a wedding or pregnancy due date.

![](https://klaviyo.zendesk.com/hc/article_attachments/35159469084955)

## Flow filtering

You can also use custom object data within trigger filters, profile filters, and trigger splits in flows, allowing you to limit flows to certain customers, filter based on the specific object that started the flow, or send customers down different paths.

For example, say you have a Pet object. You can use a trigger filter to ensure a 'Pet Birthday' flow only sends if the specific pet having the birthday is a 'Dog'. You can also use a profile filter to limit that same flow to owners who have at least 2 records (i.e., multiple pets).

Alternatively, after a customer places an order, the conditional split can check if a customer has a dog with a known birthday. If this data is available, you can send them a standard order confirmation. However, if this data has not been collected you send them an order confirmation with a prompt to fill out a survey to collect their dog’s birthday.

You can set filters or splits to be based on:

- The count of object records associated with a profile.
  - Profile has 2 or more pet records in the **Pet** object
- The existence of an object’s records and values.
  - Example: Profile has an **Appointment** object record with a date property that hasn’t passed yet.
  - Example: Profile does not have any active subscription records in the **Subscription** object.
- The properties of the object that triggered the flow.
  - Example: The Pet object entering the flow has a Type property equal to 'Dog'.

### Trigger filters

Learn about [trigger filters and how to set them](https://help.klaviyo.com/hc/en-us/articles/115002779051#h_01HDAFKRKRESH9J6P9B098BAG3).

Trigger filters allow you to restrict who enters a flow based on data from the specific object instance that triggered it. Unlike profile filters, which look at all data associated with a person, trigger filters only evaluate the object (e.g., the specific Pet or Appointment) that started the flow.

To set trigger filters:

1. Select your trigger in the flow builder.
2. Click Trigger Filters in the left-side panel.
3. Define criteria using the triggering object's properties (e.g., Pet Type equals Dog).

### Profile filters

Learn about [profile filters and how to set them](https://help.klaviyo.com/hc/en-us/articles/115002779051#h_01HDAFKRKRESH9J6P9B098BAG3).

Profile filters are applied when people enter your flow, as well as before every email in the flow is sent. In this way, profile filters ensure that only people that still qualify continue moving through a flow. You can set up profile filters based on data from your objects.

To set profile filters for an entire flow:

1. Select your trigger once it has been set and click the ****Add**** or ****Edit**** button next to the **Profile filter** option in the right-side panel.
2. Select ****Properties about someone**** from the dropdown to choose your custom object.
3. Define the criteria for the split based on the available object properties.

To add profile filters to individual flow messages:

1. Select the individual flow message.
2. Add your condition under the **Additional filters** section on the right-side panel.
3. Select ****Properties about someone**** from the dropdown to choose your custom object.
4. Define the criteria for the split based on the available object properties.

### Create a trigger split using object data

While conditional splits look at a profile's total data (e.g., "Does this person have any active subscriptions?"), trigger splits look strictly at the specific object that started the flow.

For example, in a "Pet Birthday" flow, you can use a Trigger Split to send one email if the specific pet having the birthday is a "Dog," and a different email if it is a "Cat."

To add a trigger split into a flow series:

1. Drag the split component from the left sidebar and drop it where you would like to create this split.
2. Click on the split to view the details panel. Unconfigured splits will display a yellow warning label. Notice that Yes and No paths are automatically added below the split.
3. If you insert a conditional split midway into a flow, all components below that point will be placed on the YES path by default. If you'd like to automatically swap all components on the Yes and No paths of your split, click the settings icon (3 dots) and choose ****Flip split****.
4. In the details sidebar, you will be able to define the logic for your trigger split.
5. Select the specific property name, e.g., Breed from the dropdown.
6. Define the criteria for the split based on that object's available properties.

### Create a conditional split using object data

Learn [how to use conditional splits](https://help.klaviyo.com/hc/en-us/articles/115003872171) in flows.

To add a new conditional split into a flow series:

1. Drag the conditional split component from the left sidebar and drop it where you would like to create this split.
2. Click on the split to view the details panel. Unconfigured splits will display a yellow warning label. Notice that **Yes** and **No** paths are automatically added below the split.
3. If you insert a conditional split midway into a flow, all components below that point will be placed on the YES path by default. If you'd like to automatically swap all components on the **Yes** and **No** paths of your split, click the settings icon (3 dots) and choose ****Flip split****.
4. In the details sidebar, you will be able to define the logic for your conditional split.
5. Select ****Properties about someone**** from the dropdown to choose your custom object.
6. Define the criteria for the split based on the available object properties.

![](https://klaviyo.zendesk.com/hc/article_attachments/35159460556443)

You can set up to 5 additional **where** conditions for object conditions in a split.

## Additional resources

[Getting started with custom objects](https://help.klaviyo.com/hc/en-us/articles/35105337172123)

[Understanding flow triggers and filters](https://help.klaviyo.com/hc/en-us/articles/115002779051)

[Getting started with flows](https://help.klaviyo.com/hc/en-us/articles/115002774932)