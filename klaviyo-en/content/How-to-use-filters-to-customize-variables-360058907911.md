---
id: "360058907911"
title: "How to use filters to customize variables"
source_url: "https://help.klaviyo.com/hc/en-us/articles/360058907911-How-to-use-filters-to-customize-variables"
section: "Use variable syntax and tags"
category: "Content"
category_slug: "content"
klaviyo_updated: "2026-04-21T13:54:53Z"
language: "en"
---
## You will learn

Learn how filters work and how to use them to customize variables. Filters allow you to customize the format and content of variables (i.e., personalization tags) in your messages. For a list of filters available to use in the template editor, reference Klaviyo's [variable filters glossary](https://help.klaviyo.com/hc/en-us/articles/360058466052).

## Before you begin

Before you get started, become familiar with  [how personalization works in Klaviyo](https://klaviyo.zendesk.com/hc/en-us/articles/4408802648731). In order to use filters, you’ll need to be able to identify the correct base variables and add them to your template.

## How filters work

Filters are applied to personalization tags to adjust the output that displays. Some possible use cases are:

- Apply consistent capitalization to a piece of text (for example, you can use the **upper** filter to take any variable and make it all uppercase).
- Show the price for an item after a promotion has been applied using the **multiply** filter.
- Set the number of decimal places to display for a number variable using the **floatformat** filter.

For a list of supported filters, reference our  [variable filters glossary](https://help.klaviyo.com/hc/en-us/articles/360058466052).

## Apply a filter to a variable

To apply a filter to a variable:

1. Identify your personalization tag (e.g., `{{ item.price }}`).
2. Add a pipe symbol ( | ) after the variable name.
3. Add a filter name, like **floatformat**, to specify the number of decimals to display.
4. If the filter takes any arguments (i.e., additional parameters or inputs), add a colon, followed by the argument(s).

Do not add in any additional spaces. Here is an example of a variable with a filter applied:

`{{ item.price|floatformat:2 }}`

In this example, `item.price` is the variable name, `floatformat` is the filter, and `2` is the argument required by the filter.

If the argument is a piece of text, it needs to be surrounded by straight single quotation marks (i.e., ', not ‘). Quotation marks are not needed if the argument is a number. Reference Klaviyo’s  [variable filters glossary](https://help.klaviyo.com/hc/en-us/articles/360058466052)  for examples.

## Tips for using filters

If you’re copying filters and pasting them into your template, make sure to paste as plain text to avoid pasting in formatting along with the filter itself. Use the paste as plain text keyboard shortcut (Ctrl+Shift+V or Cmd+Shift+V).

It’s important to ensure the data referenced in your variables is appropriate for the filter being used. Some filters can only be applied to text [data types](https://help.klaviyo.com/hc/en-us/articles/115005237648), while others only work on lists or numbers. If the filter isn’t working as expected, review the event or profile data you’re using to ensure it is the correct type.

## Applying multiple filters

If needed, you can apply multiple filters to a single variable. To do so, connect each filter using a pipe symbol ( | ), and consider that the filters will generally be applied in order (from first to last). Here are some examples of variables with multiple filters applied:

`{{ first_name|title|default:'there' }}`

The first filter applies title casing to the recipient’s first name, and the second filter supplies a default word to be used if no first name has been provided.

`{{ item.price|multiply:.8|floatformat:2 }}`

The first filter multiplies the base item price by .8 (to show the price if a 20% off coupon has been applied), and the second filter specifies that two decimal places should appear.

## Additional resources

- [Glossary of variable filters](https://help.klaviyo.com/hc/en-us/articles/360058466052)
- [Date variables in templates reference](https://help.klaviyo.com/hc/en-us/articles/115005257788-How-to-Format-Date-Variables-in-Templates)
- [Message personalization reference](https://klaviyo.zendesk.com/hc/en-us/articles/4408802648731)