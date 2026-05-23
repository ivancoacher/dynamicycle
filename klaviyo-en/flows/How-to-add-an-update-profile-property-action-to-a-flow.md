---
id: 360001768432
title: "How to add an update profile property action to a flow"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360001768432-How-to-add-an-update-profile-property-action-to-a-flow"
section: "Add steps or actions to flows"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-04-21T13:54:41Z"
language: en
---

## You will learn

Learn how to add an update profile property action into a flow so that you can collect and track profile data.

This flow action allows you to:

- Update an existing profile property
- Remove an existing profile property
- Create and set a new profile property

This action can be used for several use cases such as:

- Collecting categories of interest
- Tagging a profile with a specific date
- Adding gender to a profile

Learn more about [update profile property action use cases.](https://help.klaviyo.com/hc/en-us/articles/360050420371)

If someone fails profile filters at some point in the flow before they reach the update profile property action, they will skip the action with the skip reason **Skipped: Fails Flow Conditions**.

## Add the update profile property action

1. Navigate to a specific flow.
2. Drag and drop an ****Profile property update**** action into the flow.
3. Click ****+ Add step****.
   ![Profile property dropdown with Add step button below](https://klaviyo.zendesk.com/hc/article_attachments/28717850779931)
4. Choose one of the following:
   - ****Update existing property****This option allows you to update the value of an existing custom property. If the property you select is a list of values, you can choose to add or remove a value from the list.
     - If the property doesn’t yet exist for a recipient profile, the property will first be created and then the value will be updated.
     - Klaviyo automatically detects and validates the data type of the property you choose. For example, if you have a property like "Age" and all the existing values are numbers, then you try to update the value to "tom" we'll display an error because "tom" is not a number.
     - If you want to add multiple values to a list property, create separate steps and add each value as an update.
       ![](https://klaviyo.zendesk.com/hc/article_attachments/34693858870939)
   - ****Create new property****
     This option allows you to create a brand new custom property and assign the value. If the property already exists for a given recipient profile, we’ll update the value. Here, you can also configure the data type for the new property:
     - ****Text****This is any regular string of text, like "Tom" or "Chocolate."
     - ****Number****This is any numeric value, like 0, 5, or 750.
     - ****List****This is a list of values, and we'll let you input all the values you want to be part of your new list.
     - ****Boolean****A boolean is a binary variable, having two possible values, “true” and “false." You can select true or false from a dropdown.
     - ****Date****
       This is a date property that must be in an [acceptable date format](https://developers.klaviyo.com/en/docs/acceptable_date_and_timestamp_formats_for_profile_and_event_properties).
   - ****Delete existing property****The option allows you to remove an existing custom property from a profile. This will not only clear a value, but fully remove the property from the profile.
5. (Optional) Click ****+Add step**** again to update several profile properties at once
   - There is no limit to the number of steps you can add.
   - Steps will occur in the order they appear.
   - It's possible to re-order steps.
6. Click ****Save****.

If you have multiple update profile property actions placed next to each other, add at least a one-minute time delay between them so the updates do not interfere with each other.

## View activity

You can see a summary of who is waiting and who has moved through this step in the righthand details sidebar.

If you click on a message step, in the **Performance** section on the right details sidebar, you will be able to see the following:

- Who is scheduled or in **Waiting**
- Who is in **Needs Review**(if the flow component is/was in manual mode)
- Who has successfully moved through the component and is in the **Yes** grouping
- Who was skipped or in the **No** grouping due to failing the flow filters or otherwise no longer qualifying at send time

![Performance details with waiting, no, and yes completed receiving message](https://klaviyo.zendesk.com/hc/article_attachments/28717850783131)

## Additional resources

- [Update profile property action use cases](https://help.klaviyo.com/hc/en-us/articles/360050420371)
- [How contacts move through a flow](https://help.klaviyo.com/hc/en-us/articles/360017706091)