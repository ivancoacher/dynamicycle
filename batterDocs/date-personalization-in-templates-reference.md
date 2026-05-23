<h1>Date personalization in templates reference</h1>

## You will learn

Learn how to dynamically populate and format dates in your Klaviyo templates. You can input dates from profile properties (e.g., birthday) into any message, or event metadata (e.g., placed order date) into flow messages triggered by that event.

## Populate current day, week, month, or year

Date tags give you a quick way to insert the time of a campaign into a message. The date is in the time zone of your account.

- ****Current day of month****: The current day of the month is {% current\_day %}.
  **The current day of the month is 5.**
- ****Current day of the week****: The current day of the week is {% current\_weekday %}.
  **The current day of the week is Friday.**
- ****Current month****: The current month is {% current\_month\_name %}.
  **The current month is September.**
- ****Current year****: The current year is {% current\_year %}.
  **The current year is 2021.**

Currently, we only support English names for months and days of the week.

To add a dynamic date to a message:

1. From any text field (e.g., text block in an email, SMS editor, push message editor), click the personalization icon.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/32002716115355)
2. From the ****All types**** menu, choose ****Date****.
3. Choose a date tag (e.g., Current date, current year, etc.).

Looking for a date profile property, like birthday? Choose ****Custom**** from the ****All types**** menu, then search or scroll to find the property. Date properties from events can be found in the preview window for a message in any event-based flow.

## Populate a dynamic date as event variable in flow email

Let's say you are sending a thank you email through a flow that triggers whenever a customer places an order. You may want to add a sentence that says, "Thank you for your order on \_\_\_\_\_" and specify the date of the placed order.

If you look at the [data Klaviyo receives along with an event](https://help.klaviyo.com/hc/en-us/articles/115002779071-Personalize-Flow-Emails-with-Dynamic-Data), like a **Placed Order** event, you should be able to find a variable there that represents the order date. Look for a property called "order date" or something similar, as the property name will vary depending on your data source.

Once you find this variable, you'll probably next notice that the format of this date is not ideal to use in a template -- it's a UTC timestamp that doesn't look great in an email, for example:

![A UTC formatted timestamp](https://klaviyo.zendesk.com/hc/article_attachments/28713335047835)

If you want to populate this date in a more customer-friendly format, you will need to apply a few filters. Klaviyo supports most of the filters used by the [Django template language](https://docs.djangoproject.com/en/4.0/ref/templates/builtins/). For this use case, you will need to use the following filters:

- ****Format\_date\_string****
  This filter parses and converts the string of characters sliced from the full UTC timestamp to an actual date; this is necessary so that you can use the date filter to format it.
- ****Date****This is where you get to choose how you want your date formatted; Django has a [chart](https://docs.djangoproject.com/en/4.2/ref/templates/builtins/#date) that outlines how to approach this.

To apply these filters, separate them with a pipe (|) and no spaces in between:

`{{ your_variable|format_date_string|date:'F d, o' }}`

The above would turn this:

`2016-02-11T16:46:08-05:00`

into this:

February 11, 2016

Below are some additional common date and time formats, along with the formatting used to display them.

|  |  |
| --- | --- |
| February 26, 2016 | {{ your\_variable|format\_date\_string|date:'F d, o' }} |
| 26 February 2016 | {{ your\_variable|format\_date\_string|date:'d F o' }} |
| 02-26-2016 | {{ your\_variable|format\_date\_string|date:'m-d-Y' }} |
| 26-02-2016 | {{ your\_variable|format\_date\_string|date:'d-m-Y' }} |
| 2/26/16 (no leading 0s) | {{ your\_variable|format\_date\_string|date:'n/j/y' }} |
| 26/2/16 (no leading 0s) | {{ your\_variable|format\_date\_string|date:'j/n/y' }} |
| Feb 11 | {{ your\_variable|format\_date\_string|date:'M d' }} |
| 11 Feb | {{ your\_variable|format\_date\_string|date:'d M' }} |
| 02-26-2016 4:46:08 | {{ your\_variable|format\_date\_string|date:'m-d-Y g:i:s' }} |
| 02-26-2016 4:46 p.m. | {{ your\_variable|format\_date\_string|date:'m-d-Y g:i a' }} |
| 02-26-2016 4:46 PM | {{ your\_variable|format\_date\_string|date:'m-d-Y g:i A' }} |

For a full list of date format options, reference [Django’s date format documentation](https://docs.djangoproject.com/en/4.2/ref/templates/builtins/#date).

## Using the “today” variable

The today variable allows you to display today’s date at the time a message is sent. To display today’s date, use this code:

`{% today "%Y-%m-%d" as today %} {{ today }}`

The date will display in this format: 2021-03-18

Make sure to use the entire line of code above. Your date variable will not render if you include one tag, but not the other (i.e., you cannot use the {{ today }} tag alone without the preceding tag {% today ... %}).

To apply different formatting, apply the filters from the section above to the `{{ today }}` variable. For example, `{% today '%Y-%m-%d' as today %} {{ today|format_date_string|date:'m/d/Y'
}}` would render using the format MM/DD/YYYY.

## Calculating a future date

If you’d like to display a future date relative to the day a message is sent, apply the days\_later filter to the today variable outlined above, like this:

`{% today "%Y-%m-%d" as today %} {{ today|days_later:5 }}`

This variable will display the date 5 days after a message is sent. So, if the message was sent on March 18, the date displayed would be 2021-03-23.

This filter can be combined with the formatting filters outlined above to use a different date format. Take this code as an example:

`{% today '%Y-%m-%d' as today %} {{ today|days_later:5|format_date_string|date:'M
d' }}`

If the message was sent on March 18, this would render as Mar 23.

## Additional resources

- [Message personalization reference](https://help.klaviyo.com/hc/en-us/articles/115005084927)
- [How to format dates for CSV files](https://help.klaviyo.com/hc/en-us/articles/360039859932-How-to-Format-Dates-for-CSV-Files)
- [How to use the preview panel for message personalization](https://klaviyo.zendesk.com/hc/en-us/articles/27843522951707)
