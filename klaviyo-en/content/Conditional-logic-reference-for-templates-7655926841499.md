---
id: "7655926841499"
title: "Conditional logic reference for templates"
source_url: "https://help.klaviyo.com/hc/en-us/articles/7655926841499-Conditional-logic-reference-for-templates"
section: "Use variable syntax and tags"
category: "Content"
category_slug: "content"
klaviyo_updated: "2026-04-21T13:55:05Z"
language: "en"
---
## You will learn

Learn about all the available conditions you can use to dynamically display a block, section, or custom-coded piece of content only to certain recipients. To learn how to use these conditions in your templates, head to our article on [how to show or hide template blocks based on dynamic variables](https://help.klaviyo.com/hc/en-us/articles/7655965301531).

Learn how to use conditional logic:

- [Where you can use conditions](#h_01G90PC1GF28BCKX1H83E6W1GJ)
- [Tips for success](#h_01G90PEBD7E3H2Y9YSE41Q7FK9)
- [Condition structures](#h_01G90PC71XXASDF3ERB4F39QDK)
- [Build complex conditions](#h_01G90PE5WWGQETTSC7K9GY2SKX)

## Where you can use conditions

You can use conditions in:

- ****Emails****
  - Create show/hide logic to dynamically [display blocks or sections only to certain people](https://help.klaviyo.com/hc/en-us/articles/7655965301531).
    - If you prefer not to write code, use the [show/hide logic builder](https://klaviyo.zendesk.com/hc/en-us/articles/7655965301531) instead.
  - Write if/else conditionals to [create custom Django statements](https://developers.klaviyo.com/en/docs/use_conditionals_in_messages).
- ****Customer Hub****
  - Write if/else conditionals to [create custom Django statements](https://developers.klaviyo.com/en/docs/use_conditionals_in_messages) in content blocks

## Tips for success

When building out show/hide conditions, pay attention to the details. Show/hide conditions are case-sensitive, and spelling must exactly match your profile or event data.

Also, make sure to consider all possible viewers. For example, if you show a specific block only to residents of a certain state, cover all possible spellings of that state name (e.g., Massachusetts, massachusetts, mass, MA). Also take into consideration profiles who may not have the property set at all.

Once you’ve built the message and applied your conditions, [preview](https://help.klaviyo.com/hc/en-us/articles/115005081907-How-to-Preview-and-Send-Test-Emails-in-Klaviyo) using a variety of profiles to confirm that the message displays as you intended for all scenarios.

## Condition structures

Conditions should include 1-3 elements, depending on your goal for the block and the data you’re using. The condition must at least include a variable (e.g., **person|lookup:'Favorite Color'**). It may also include a comparison function, like = (equals) or > (greater than) and a value, which specifies a property value to look for. Additionally, certain conditions begin with **not**, if you’d like the block to only appear for profiles that do not meet a condition.

The chart below contains a complete list of possible structures a show/hide condition can follow.

|  |  |  |
| --- | --- | --- |
| ****Sample condition**** | ****Show the block if...**** | ****Acceptable data types**** |
| person|lookup:'Favorite Color' | The `Favorite Color` property is set (has any value) and is not the boolean **False** | Any |
| not person|lookup:'Favorite Color' | The `Favorite Color` property is not set (does not exist on the profile, or is empty), or is the boolean value **False** | Any |
| person|lookup:'Favorite Color' == 'green' | The `Favorite Color` property has the value `green` | Text, Number |
| person|lookup:'Favorite Color' != 'green' | The `Favorite Color` property does not have the value `green` | Text, Number |
| person|lookup:'Age' > 20 | The `Age` property contains a number greater than 20 | Number |
| person|lookup:'Age' >= 20 | The `Age` property contains a number greater than or equal to 20 | Number |
| person|lookup:'Age' < 20 | The `Age` property contains a number less than 20 | Number |
| person|lookup:'Age' <= 20 | The `Age` property contains a number less than or equal to 20 | Number |
| 'green' in person|lookup:'Favorite Colors' | The property `Favorite Colors` contains a list, and `green` is one of the list items, OR  The property `Favorite Colors` contains text, and `green` exists anywhere in the text | List, Text |
| not 'green' in person|lookup:'Favorite Colors' | The property `Favorite Colors` contains a list, and `green` is not one of the list items, OR  The property `Favorite Colors` contains text, and `green` does not exist anywhere in the text | List, Text |

### Conditions for booleans

If you are referencing data stored as a boolean, you’ll need to use 1 and 0 rather than “true” and “false” in your show/hide condition definition. Do not surround the 1 or 0 in quotes. Use the sample conditions below as a template.

|  |  |
| --- | --- |
| ****Sample condition**** | ****Show the block if...**** |
| person|lookup:'VIP' == 1 | The `VIP` property is set to the boolean value `true` |
| person|lookup:'VIP' == 0 | The `VIP` property is set to the boolean value `false` |

### Conditions for booleans stored as text

If your true/false data is stored as text, not as a boolean, use the sample conditions for text properties above. If you aren’t sure, or if you are referencing a property that contains both booleans and text, you can use these structures to cover all scenarios. Include all spellings and capitalizations that are present in your data.

|  |  |
| --- | --- |
| ****Sample condition**** | ****Show the block if...**** |
| person|lookup:'VIP' == 1 or person|lookup:'VIP' == 'true' or person|lookup:'VIP' == 'True' | The `VIP` property is set to the boolean value `true` or the strings `true` or `True` |
| person|lookup:'VIP' == 0 or person|lookup:'VIP' == 'false' or person|lookup:'VIP' == 'False' | The `VIP` property is set to the boolean value `false` or the strings `false` or `False` |

## Build complex conditions

If you would like your block to display to people who meet multiple criteria, or if you have a complex use case, you can use multiple show/hide conditions for one block. To do so, connect a series of conditions with AND or OR. For example, if you want to display a block to anyone in Massachusetts, but Massachusetts is spelled differently on some profiles, you can use a condition like this:

**person.location.region == 'Massachusetts' or person.location.region == 'massachusetts' or person.location.region == 'mass' or person.location.region == 'MA'**

If you only want to show a block to people whose favorite color is green, and who are also VIPs, you can use a condition like this:

**person|lookup:'Favorite Color' == 'green' and person|lookup:'VIP'== 1**

### Conditional statements and the inline text editor

When you add certain conditional statements to a text block, they may disappear from the inline text editor. The code is still present; it is just hidden. To view and edit conditional statements, open the text block's **Source code** field.

The following tags are only visible in a text block's **Source code** field:

- {% for ... %}
- {% endfor %}
- {% if ... %}
- {% elif ... %}
- {% else %}
- {% endif %}
- {% with ... %}
- {% endwith %}