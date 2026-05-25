---
id: "8557592023451"
title: "Troubleshooting invalid format error messages"
source_url: "https://help.klaviyo.com/hc/en-us/articles/8557592023451-Troubleshooting-invalid-format-error-messages"
section: "List and segments troubleshooting"
category: "Audience"
category_slug: "analytics-audience"
klaviyo_updated: "2026-04-21T13:55:05Z"
language: "en"
---
## You will learn

Learn what `Invalid _ format` error messages mean and how to avoid these messages when uploading a list using a CSV file.

## About mismatched data types

When you import a list into Klaviyo, the field mapping page enables you to match any properties to their corresponding data type in Klaviyo. For example, **Email** always has a **Text** data type; whereas, if you upload a custom property for **Birthday**, you will want to set the data type to **Date**.

Review the data types, acceptable formats, and examples below.

- ****Text****
  Any text, or combination of text and numbers. If you are unsure what format your data is in, choose this option.
  - Examples:
    email@example.com
    Hello, world
    $5.00
- ****Numeric****
  All numbers. Do not include currency symbols in numeric fields.
  - Examples:
    2
    5.0031
    130.0
- ****Boolean****
  True or false values.
  - Examples:
    true
    false
- ****Date****
  Reference our guide to [acceptable date and timestamp formats for profile and event properties](https://help.klaviyo.com/hc/en-us/articles/115005253428) to learn about accepted date formats.
  - Example:
    2014-09-01 13:34:08
- ****List****
  Data must be formatted as a JSON array.
  - Examples:
    ["apples","bananas","oranges"]
    ["apples"]
- ****Consent****
  Consent is formatted as the channel (email, SMS, etc.) and the type of consent (if there are multiple types available in Klaviyo). The only option for email is **Email Marketing Consent**; for SMS, it would be either **SMS Marketing Consent** or **SMS Transactional Consent**; etc. The value of this field must be "Subscribe," "Never Subscribed," or "Unsubscribed."

For more information about what the different data types entail and which to select when importing your list, head to our guide on [understanding data types](https://help.klaviyo.com/hc/en-us/articles/115005237648).

## Error: invalid list format

In order to use the “list” data type, your data must be formatted as a JSON array. A JSON array is always surrounded by square brackets, and each list item is surrounded by quotation marks. Every list item except the last one must be followed by a comma.

Make sure to use straight quotes (" ") rather than curly quotes (“ ”).

Below are properly-formatted JSON arrays:

- ["apples","bananas","oranges"]
- ["apples"]

## Error: invalid boolean format

A boolean value must be either `true` or `false`. If your column of boolean values contains anything other than `true` or `false`, replace the values or upload the property as text instead.

## Error: invalid number format

The “number” data type accepts whole numbers (e.g., 1, 63) and floats (e.g., 1.5, 233.018). This data type does not allow any special characters, including currency symbols.

## Error: invalid email format

Klaviyo automatically skips email address entries that are not in a valid format. A valid email address, such as jane@example.com, is made up of a local part (jane), an @ symbol, and a case-insensitive domain part (example.com). If any of these required parts are missing, we consider the email invalid. If there are erroneous spaces in the email address, we will also consider the email invalid.

You can search your CSV for invalid emails. Highlight the list of email addresses and select ****Data > Filter****. Then, filter out any email addresses that do not contain symbols like "@" or "." Fix or remove these invalid emails before re-attempting your import.

![](https://fast.wistia.com/embed/medias/l4gja9eki9/swatch)

If your email addresses are all formatted correctly, but you still receive this error message, check for any line breaks within cells and remove them. Line breaks within a cell in your CSV will be interpreted as new rows in the upload, causing misalignment between the data and your headings.

![](https://fast.wistia.com/embed/medias/vkgvld5r5i/swatch)

## Error: phone number formatting issues

Phone numbers must include a country code or a separate column indicating their country, and must follow an accepted phone number format. Learn how to [properly format and upload phone numbers](https://help.klaviyo.com/hc/en-us/articles/360035428731).