---
id: "37711720137755"
title: "Frequently asked questions about custom objects"
source_url: "https://help.klaviyo.com/hc/en-us/articles/37711720137755-Frequently-asked-questions-about-custom-objects"
section: "Getting started with objects"
category: "Content"
category_slug: "content"
klaviyo_updated: "2026-04-21T13:56:55Z"
language: "en"
---
## You will learn

Learn about frequently asked questions related to custom objects in Klaviyo. If you don’t see your question in the resource below, please reach out on our [Community forum](https://community.klaviyo.com/).

## General questions about objects

### Do I need a developer to create an object?

Yes, this feature depends on the use of [APIs](https://developers.klaviyo.com/en/reference/custom_objects_api_overview) to send data sources and ultimately create objects.

### Can I create custom objects using Klaviyo forms or CSV uploads?

Klaviyo currently requires accounts to create new custom objects by sending us data via API.

### When should I use a custom object versus a profile property or event?

You should use custom objects when you have a many-to-one relationship between the category that your custom object represents and your profiles. For example, if you want to keep information about your customer’s pets, and your customer may have more than one pet, representing these as a custom object works much better than profile properties or events.

When tracking items like a membership status, where a profile can only have one status at a time, profile property is a better fit. However, if you’d like to store other details about a profile’s membership as well, an object can work better.

When tracking something broad, like how many times a recipient has opened an email, we recommend using events.

### Can I update my custom object after creation?

Yes, you can always add additional, non-required properties to your custom object. For more, read about [updating a custom object](https://help.klaviyo.com/hc/en-us/articles/35105337172123).

### When should I emit an event versus updating the custom object’s properties?

Events are intended to trigger flows quickly, allowing you to send timely and relevant messaging. When the status of an object changes and you want to trigger a message as a result of this, you should update the object with the new information and send us an event to trigger the flow.

You can [personalize templates](https://help.klaviyo.com/hc/en-us/articles/35146367972763) with the object information in the event triggered flow. There are two ways to achieve this:

1. Use the `{{ event }}` tag to add relevant properties in your event’s metadata for use in your template. This works well when timeliness is important.
2. Include the object’s ID in the event’s metadata, which allows you to get the object in the template with the `{% customobject id={{ event.pet_id }} as pet %}`. However, it can take some time for the object to be updated with the latest properties so it is possible the flow triggered a message to send before the object was updated.

## Questions about sending object data

### How do I start sending my data for custom objects?

1. Create a new data source [using our API](https://developers.klaviyo.com/en/reference/create_data_source).
2. Define your data structure (see example JSON).
3. Send your data source records to Klaviyo via [API](https://developers.klaviyo.com/en/reference/bulk_create_data_source_records).
4. [Create](https://help.klaviyo.com/hc/en-us/articles/35105337172123#h_01JPSTEQJQYKW8Y4AEKSPQ6YSF) your custom object.
5. Create the relationship between your custom object and your profiles.

### How are data sources created and used?

Custom objects are created from data sources. Your developer will need to create a new data source using our [Custom Objects API](https://developers.klaviyo.com/en/reference/create_data_source).

After creating a new data source, Klaviyo will return a unique identifier as part of the response to your API request. This allows Klaviyo to identify data sources, especially in cases where an account has multiple data sources (e.g., 1 for each custom integration, data warehouse, or custom 3rd party integration that the brand relies on for their business).

With this unique identifier, your developer can then create data source records through [Klaviyo’s API](https://developers.klaviyo.com/en/reference/bulk_create_data_source_records).

### ****How should I format my data?****

Your developer will need to send JSON-formatted data to Klaviyo. We recommend sending your data as text with a comma separated list. You will be able to use segmentation and flow filtering’s “contains” operator to filter for the values in this comma separated string. See the [segment conditions reference](https://help.klaviyo.com/hc/en-us/articles/115005062847) for more information on filtering.

Supported [data types](https://help.klaviyo.com/hc/en-us/articles/115005237648) in custom objects:

- Text
- Integer
- Decimal
- [Date](https://help.klaviyo.com/hc/en-us/articles/115005237648#h_01J15GVP683H6QPWVMJDA9HGYM) - All datetimes are converted to UTC in our system. For example, if you upload “2025-04-03” it is converted to “2025-04-03 00:00:00”. For customers with time zones three hours ahead, the datetime would read “2025-04-02 21:00:00”.
- [Boolean](https://help.klaviyo.com/hc/en-us/articles/115005237648#h_01J15GVP68YBJZ962DJ3TRRR9H)

The list data type is not currently supported. For an example payload for the data source record API, see [Bulk Create Data Source Records](https://developers.klaviyo.com/en/reference/bulk_create_data_source_records).

When sending phone numbers, they must be in [E.164 format](https://help.klaviyo.com/hc/en-us/articles/360046055671). When sending dates, they must be in one of our [acceptable timestamp formats](https://developers.klaviyo.com/en/docs/acceptable_date_and_timestamp_formats_for_profile_and_event_properties).

### ****What are the data limits for custom objects?****

You can upload a maximum of 2 KB per property and 8 KB per total record.

### ****Can I map with nested data?****

We recommend defining your JSON object without nesting the properties you want to use for your custom object. If your source data is deeply nested or uses a list, you will need to manually enter the JSON path into the object manager. For lists, you can only map a property to a position within that list (e.g., the first or second value).

### ****Can I associate multiple identifiers with a profile?****

Yes, if you want to use 2 or more profile identifiers (e.g., email and phone number) to associate your custom object records to a profile, ensure you include both of those properties in every sync, even if the value of one of them is null.

## Questions about using objects with flows

### If my object didn’t trigger a flow and I don’t have an object id from an event, can I still personalize my messaging?

Yes, you can use [object filters](https://help.klaviyo.com/hc/en-us/articles/35146367972763#h_01JPTH5R8840K0Q3XWH2CFYWRY) to find the right object when personalizing your messaging.

### Can I preview flow messages when an object triggers a flow?

At this time, it is not possible to use the preview function in the app to view a message when you use the `{{ object }}` tag.

To test a flow message:

1. Create a [date-triggered flow](https://help.klaviyo.com/hc/en-us/articles/360002732652) and set it to live.
2. Create a profile with an object that has a date that will trigger in at least 24 hours.

### Can I update my objects using flow actions like webhooks and Klaviyo code?

At this time, we advise you to update your original data source first and then send the revised object back to Klaviyo in the permitted format. If these two systems fall out of sync, you risk sending an out of date record back to Klaviyo from your system, reverting it to the original value.