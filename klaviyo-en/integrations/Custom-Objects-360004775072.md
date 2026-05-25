---
id: "360004775072"
title: "Custom Objects"
source_url: "https://help.klaviyo.com/hc/en-us/articles/360004775072-Custom-Objects"
section: "Custom integrations"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:42Z"
language: "en"
---
## Overview

Custom Objects are Klaviyo objects that can accept any schema and that can include a foreign-key reference to any Klaviyo profile object. While our other record types (profiles, events, campaigns, etc.) have fixed schemas (eg, a profile has first name, last name, email, location, accepts marketing, etc.), and while some, like profiles, can accept custom fields (favorite color, pet type), there is a limited amount of flexibility to accept alternative data structures. Custom Objects are a flexible alternative.

#### Warning

This is an advanced feature reserved for customers who have access to a developer or developer support. To enable this feature you must [reach out to our Customer Success team](https://help.klaviyo.com/hc/en-us/requests/new).

## What's a Schema?

A schema is the structure that defines a database table. You can think of a schema as the column headers in an excel spreadsheet: it tells you what each field is named, and what kind of data it will hold, such as dates, string (text), numeric, boolean (true/false), etc.

For example, the following is a standard profile stored in Klaviyo.

![](https://klaviyo.zendesk.com/hc/article_attachments/28713335502747)

If we look how the data is stored in Klaviyo, we can see the structure (or schema) in JSON format.

```
{
 "created": "2018-07-10 13:28:25",
 "updated": "2018-07-10 13:28:26",
 "object": "person",
 "id": "Lwxf3r",
 "$email": "klaviyogreen@gmail.com",
 "$first_name": "John",
 "$last_name": "Smith",
}
```

## What Do Custom Objects Let You Do?

Custom objects allow you to define a schema for a new database object. This object can have a foreign key relationship (that is, it can point to) any other existing profile object within Klaviyo.

This is helpful when you have profiles with multiple related records that all share the same schema. For example, if your business model uses gift cards, a single customer can have zero, one, or hundreds of gift cards associated with their profile.

Other examples include the following:

- Survey responses (where a customer fills out the same survey several times
- Event attendance
- Conversations with your clients
- Product reviews

## How Can You Use Custom Object Data in Klaviyo?

Custom object data can be used to build segments within Klaviyo and to pass data into an email.

### Segmenting with Custom Object Data

Segmentation currently works only on date fields (before / after / on / between dates) and number fields (more than, less than, equal to, between).

Let's say you've created a custom object that stores gift card information for your customers. Using the data from your custom objects you can build a segment that includes all profiles with one or more gift card worth less than $50 or more.

![](https://klaviyo.zendesk.com/hc/article_attachments/28713329823003)

If you're passing date information, you could build a segment that includes all profiles who attended an event between March 1, 2018 and March 31, 2018.

### Passing Custom Object Data into an Email

Any field within a custom object can be pulled into the body of an email. For example, you can use a template tag to insert a variable that shows the gift card code, the current value of the gift card, and the expiration date.

The tag can loop over all records related to a profile and display values from all of them. If a customer has eight different gift cards, you can show all of their codes in a text block, with the current value next to them.

![](https://klaviyo.zendesk.com/hc/article_attachments/28713329825947)

The tag can sum up or perform other basic operations (min, max) on numeric data from custom object records. For example, you can add up the value of all eight gift cards and display it in the subject line of your email. Reference our guide to [Template Tags and Variable Syntax](https://help.klaviyo.com/hc/en-us/articles/115005084927-Template-Tags-and-Variable-Syntax) for more information.

## How Do I Set It Up?

After reaching out to our customer support team, your first step is to map your existing datasource to the schema framework for creating a Klaviyo Custom object.

Below is an example of the data from a single custom object inside Klaviyo.

```
"config": {
    "602": {
        "desired_fields": [
            "custrecord_gc_shopify_gc_internal_id",
            "custrecord_gc_remaining_balance",
            "custrecord_gc_initial_balance",
            "custrecord_gc_disabled",
            "custrecord_gc_gift_card_type",
            "custrecord_gc_sales_order",
            "custrecord_gc_customer",
            "custrecord_gc_retrieve_balance",
            "custrecord_gc_gift_card_number"
        ],
        "desired_fields_mapping": {
            "custrecord_gc_gift_card_number": "code",
            "custrecord_gc_gift_card_type": "type",
            "custrecord_gc_remaining_balance": "value",
            "custrecord_gc_sales_order": "shopify_order_number"
        },
        "email_field": "custrecord_gc_customer",
        "emails_separate": 1,
        "fields_to_display": [
            "custrecord_gc_sales_order",
            "created_external",
            "custrecord_gc_gift_card_type",
            "custrecord_gc_initial_balance",
            "custrecord_gc_remaining_balance"
        ],
        "index_on": [
            "custrecord_gc_gift_card_type",
            [
                "klaviyo_customer_id",
                "custrecord_gc_gift_card_number",
                "custrecord_gc_remaining_balance"
            ]
        ],
        "mapping": "gift_card",
        "parsers": {
            "custrecord_gc_sales_order": [
                "Sales Order #",
                "after"
            ]
        }
    }
}
```

We can use this example data to breakdown Klaviyo's custom object schema framework.

```
"config": {
    "602": {
        "desired_fields": [],
        "desired_fields_mapping": {},
        "email_field": "custrecord_gc_customer",
        "emails_separate": 1,
        "fields_to_display": [],
        "index_on": [
            "custrecord_gc_gift_card_type",
            [
                "klaviyo_customer_id",
                "custrecord_gc_gift_card_number",
                "custrecord_gc_remaining_balance"
            ]
        ],
        "mapping": "gift_card",
        "parsers": {
            "custrecord_gc_sales_order": [
                "Sales Order #",
                "after"
            ]
        }
    }
}
```

|  |  |
| --- | --- |
| Key | Value |
| ****602**** | The object ID from the datasource. Your datasource should have some unique identifier for each object. |
| ****desired\_fields**** | Which fields should Klaviyo retrieve from the source object? We need to define each field we want access to in Klaviyo. |
| ****desired\_fields\_mapping**** | What are the human-readable labels you want to apply to these fields?  The source field will be named something like "custrecord\_gc\_remaining\_balance" in the source system, which can be condensed to "value" in the field mapping (which is later used in the template tag). |
| ****email\_field**** | What field is the foreign-key reference to the profile object, which uses email as a lookup? (This will be configured by an engineer.)  Works in conjuction with ****emails\_separate****. |
| ****emails\_separate**** | Does the email value exist on this object in the source system? Works in conjunction with ****email\_field****. |
| ****fields\_to\_display**** | Which fields do you want to see in the profile block for custom objects?  Customers want to be able to check to make sure that the right profiles are being included in segments, and this lets them determine which fields to display.  Some fields contain sensitive data you will not want to display, such as the remaining balance on one of your customer's gift cards. |
| ****index\_on**** | What fields should we use as indexes for this data?  What fields are we going to be using to query and retrieve data frequently?  Indexing on a field makes retrieving data faster, so if you are going to use a field for segmentation or to pull data into an email, it's helpful to add an index on it.  This can also be reconfigured after the initial integration, so it's not an issue if you need to add additional index fields later. |
| ****mapping**** | Similar to ****desired\_fields\_mapping****, this lets us assign a user friendly name for this object in Klaviyo to use in segmentation interfaces and in template tags. |
| ****parsers**** | This lets us trim characters from specified fields, so that we can use the data within them in different ways.  In this example, the Shopify Sales Order Number was stored in the datasource as "Sales Order # 100000".  This meant that we couldn't cross-reference it with our existing Shopify Sales Order number field, which only stored the value 100000.  Therefore, we needed to trim out "Sales Order #". |

Once you've defined your schema to match Klaviyo's custom object framework, you'll work with Klaviyo engineers to implement a method to send your data to Klaviyo.

#### Note

We currently do not have a public facing API for custom objects. For sending custom object data to Klaviyo you will need to contact us and work with our engineering team.