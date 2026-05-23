<h1>Understanding data types</h1>

## You will learn

Learn about the different options available for storing your data in Klaviyo, and how to use each one. Klaviyo allows you to harness the data collected about your customers to power data-driven marketing choices that will grow your brand. That being said, it's important to understand the data that's being pulled into your account.

## Where data types appear in Klaviyo

When creating a segment or configuring a flow filter using **Properties about someone**, you will notice a dropdown menu that appears after you choose a dimension for your condition. This dropdown menu relates to the data type of the value you input.

![Data type dropdown in segments](https://klaviyo.zendesk.com/hc/article_attachments/34356876375579)

The following data types are available to select:

- Text
- Number
- Date
- Boolean
- List

## Text

A text input is any finite sequence of characters (i.e., letters, symbols, and punctuation marks). It is always used to represent plain text, even when it includes numbers or is formatted like a date. Use the text data type for:

- Names
- Numerals that are mixed with other characters (e.g., a currency symbol)
- Street addresses
- Short or long-form answers to a question (e.g., shopping preferences, favorite color)

Additionally, text is the default data type when the intended data type is unclear.

You can think of a text input as what might appear within quotation marks in a paragraph. Regardless of content in the quotation marks, whatever is inside of the quotation marks exists as a finite sequence of characters. Below is a sign-up form that gathers preference information that will be translated into text properties.

![A signup form collecting multiple types of data](https://klaviyo.zendesk.com/hc/article_attachments/28716053736091)

## Number

A number is a numeric value without a decimal. When you import numeric values, Klaviyo automatically recognizes the value as a number, rather than text.

Number inputs could reference someone’s age, the number of emails received, or how many times a customer has purchased from you. Below is a segment that shows customer engagement by interaction with the number of emails that have been clicked on or opened in the last month.

![Numbers data type being used in segment conditions](https://klaviyo.zendesk.com/hc/article_attachments/34356876382107)

## Date

A date is used for any date-time value. Unlike a number, Klaviyo will only automatically recognize a date value as a date if it is [formatted](https://developers.klaviyo.com/en/docs/acceptable_date_and_timestamp_formats_for_profile_and_event_properties) a certain way (i.e., YYYY-MM-DD HH:MM:SS).

Dates could reference someone’s birthday, the day they first signed up for your newsletter, or an anniversary with a partner. Below is a sign-up form collecting birthday information as a date.

![](https://klaviyo.zendesk.com/hc/article_attachments/38342176407835)

## Boolean

The boolean data type can only represent two values: true or false. An example of boolean data is the property stored when someone has accepted marketing from you. Below is an example of a customer profile who consented to marketing.

![Binary data type for property](https://klaviyo.zendesk.com/hc/article_attachments/34356906949147)

Accepted **true** values are:

`True`, `"1"`, `1`, `"true"`, `"t"`, `"yes"`, `"y"`

Accepted **false** values are:

`False`, `"0"`, `0`, `"false"`, `"f"`, `"no"`, `"n"`, `None`

All string values (those surrounded by quotes) are not case-sensitive.

If you're using a CSV to upload a boolean value to Klaviyo or sending [custom object](https://help.klaviyo.com/hc/en-us/articles/35105337172123) data via API, use `True` and `False`.

## List

A list is any array of values; for example ["Offer1","Offer2"]. In Klaviyo, lists are used when the goal is to collect an array of words or phrases where every single item in the array can be identified individually.

One common use case for this is when different tags are being collected under a single property, such as the **Shopify Tags** property. When Klaviyo stores a property as a list, this allows you to use the property in a segment or filter and then include as many available tags as you'd like. You have the ability to choose from any value stored as part of the list.

Another common use case is when Klaviyo captures a **Placed Order** metric through an integration and the data we receive along with this placed order includes an **Items** property. This single **Items** property will need to include all items purchased in the order.

![List data type being used in event data](https://klaviyo.zendesk.com/hc/article_attachments/34356876391835)

To achieve this, the property is always synced and stored as an array (a list) in Klaviyo. This allows us to store the **Items** property while including a series of values (i.e., each item purchased in the single order), where each value in the array can be identified individually.

When uploading a CSV that includes a list property, include the full list formatting within the cell. Make sure every entry in the column follows the list format, even if a particular person’s list contains only one item.

![A CSV file with list data ready to upload](https://klaviyo.zendesk.com/hc/article_attachments/28716053749403)

## String (during list uploads)

When uploading a list of profiles into Klaviyo, there's one other data type that may appear; string.

String is the same as the [text data type.](#h_01ENR9PD67WK686H8Z5SHCVK59) When creating a segment, you can segment based on string data using the text data type.

## Additional resources

- [Getting started with segments](https://klaviyo.zendesk.com/hc/en-us/articles/115005237908)
- [About the information section of a profile](https://klaviyo.zendesk.com/hc/en-us/articles/115005247028)
- [How to use links to collect information about your recipients](https://klaviyo.zendesk.com/hc/en-us/articles/115005255248)
- [How to embed a form on your order confirmation page](https://klaviyo.zendesk.com/hc/en-us/articles/360031724251)
