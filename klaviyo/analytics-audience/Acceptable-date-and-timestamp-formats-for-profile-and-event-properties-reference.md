---
id: 115005253428
title: "Acceptable date and timestamp formats for profile and event properties reference"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005253428-Acceptable-date-and-timestamp-formats-for-profile-and-event-properties-reference"
section: "Profile management"
category: "Audience"
category_slug: "analytics-audience"
klaviyo_updated: "2026-04-21T13:54:23Z"
language: en
---

## You will learn

Learn which date and time formats Klaviyo recognizes in event and profile data sent through our APIs or in a CSV upload. Note that this does not apply to an event timestamp sent via the Track API, which must be unix time in seconds.

## Acceptable date and timestamp formats

See the example below for information around formatting your date and timestamps in a CSV file. Note that, you must format dates as either YYYY-MM-DD or MM/DD/YYYY. If there's no time of day associated with your date, you can set it to midnight by using the HH:MM:SS value 00:00:00.

If you do not include seconds on your timestamps they will default to 0. For example, a timestamp of `2014-09-30 13:34` would be submitted to Klaviyo as `2014-09-30 13:34:00`

For example, the date September 30, 2014, at 1:34:08 pm should be formatted using one of the following supported formats:

`2014-09-30 13:34:08`

`2014-09-30 13:34:08+00:00`

`09/30/2014 13:34:08`

`09/30/14 13:34:08`

`09/30/2014 13:34`

`09/30/14 13:34`

`2014-09-30T13:34:08`

`2014-09-30 13:34:08.000001`

`2014-09-30T13:34:08.000001`

`2014-09-30 13:34:08.000001-04:00`

`1412098448` (Unix)

If you need help reformatting your dates in a spreadsheet before converting it to a CSV file, head to our article, [Formatting dates for CSV files](https://klaviyo.zendesk.com/hc/en-us/articles/360039859932).

Below is an example of what this CSV file may look like as you upload it with the correct date/time formats.

![2018-06-13_21-47-57.gif](https://klaviyo.zendesk.com/hc/article_attachments/28722594609819)

Note that, when you import dates with timestamps, this field maps to the date data type. However, when you import a date without a timestamp, a default time of midnight UTC is applied to this date when mapped to the date data type. This may cause [date-property triggered flows](https://klaviyo.zendesk.com/hc/en-us/articles/360002732652) to send a day early or late depending on the account’s timezone. For that reason, if you only have the date (no timestamp) to upload, then map it to the text data type.

For more information on uploading a CSV file to Klaviyo, head to our article on [how to add subscribers to an existing list](https://klaviyo.zendesk.com/hc/en-us/articles/115005251128).

## Additional resources

- [Formatting dates for CSV files reference](https://klaviyo.zendesk.com/hc/en-us/articles/360039859932)
- [Klaviyo's default lists and segments reference](https://klaviyo.zendesk.com/hc/en-us/articles/360024538231)