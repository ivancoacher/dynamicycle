---
id: 35146367972763
title: "How to use custom objects in templates"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/35146367972763-How-to-use-custom-objects-in-templates"
section: "Use objects in Klaviyo"
category: "Content"
category_slug: "content"
klaviyo_updated: "2026-04-21T13:54:40Z"
language: en
---

You must have access to [custom objects](https://help.klaviyo.com/hc/en-us/articles/35105337172123) to use this functionality.

## You will learn

Learn how to use custom objects in templates, so you can use object data in flow and campaign sends.

You must [create an object](https://help.klaviyo.com/hc/en-us/articles/35105337172123) first before you can use custom object data in templates.

## Accessing object data through the personalization menu

You can personalize text blocks in template editor using properties from a custom object, or the count of records for an object.

Learn [how to use Klaviyo's template editor](https://help.klaviyo.com/hc/en-us/articles/4407911841435).

To get started with adding object data into your templates:

1. Add a new text block or select an existing text block.
2. Double click in to the text block and then position your cursor where you want to insert your dynamic property.
3. Select the ****Personalization**** button in the top right.

![](https://klaviyo.zendesk.com/hc/article_attachments/35160309938075)

3. In the personalization modal, select ****Objects**** from the **All types** dropdown.

![](https://klaviyo.zendesk.com/hc/article_attachments/35160309944475)

4. Within **Objects**, you’ll see all the objects on your account that you can use to pull data into the template. Select the object that contains the data you’d like to use in the template.
5. Select the specific object property or [object filter](#h_01JPTH5R8840K0Q3XWH2CFYWRY) to include in the template. You can also create a new object filter here.
6. Set the default text and any styles for your text.

To specify the capitalization rules for object data, you'll need to manually set the rule in the personalization tag. For example:

- ****{{ object.full\_name|title|default:'value' }}****
  John Doe
- ****{{ object.full\_name|upper|default:'value' }}****
  JOHN DOE
- ****{{ object.full\_name|lower|default:'value' }}****
  john doe

Learn more about [modifying values with Django filters.](https://developers.klaviyo.com/en/docs/glossary_of_variable_filters)

## Accessing object data with personalization tags

You can use personalization tags in emails (including the email’s subject line), SMS/MMS messages, push notifications, and Customer Hub to display object data.

Learn [how to use personalization tags in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/18986347580827).

### Object personalization tag reference

You can use the following personalization tags with objects.

****Using the object that triggered a flow****

{{ object }} is only available when an object has triggered a flow. The {{ object }} template tag is only available in date triggered flows based on an object. This is similar to the {{ event }} template tag for event triggered flows.

These examples use the following:

- Object called **Pet**which is referenced with the **object** tag in the template.
- Object property called **Name**

|  |  |
| --- | --- |
| ****Structure**** | ****Example**** |
| {{ object.object\_property }} | {{ object.Name }} |
| {{ object | lookup:'object\_property' }} | {{ object | lookup:'Name' }} |

****Getting an object by ID****

These examples use the following:

- Object called **Pet**
- Object property called **Name**
- Event that triggered the flow with an object property called **pet\_id**. This field is the same as the object ID for the **Pet** object.

|  |  |
| --- | --- |
| ****Structure**** | ****Example**** |
| {% customobject event.object\_id  object\_type\_title="Title" as alias %} {{ alias.object\_property }} {% endcustomobject %} | {% customobject event.pet\_id  object\_type\_title="Pet" as pet %} {{ pet.Name }} {% endcustomobject %} |
| {% customobject event.object\_id  object\_type\_title="Title" as alias %} {{ alias | lookup:'object\_property' }} {% endcustomobject %} | {% customobject event.pet\_id  object\_type\_title="Pet" as pet %} {{ pet | lookup:'Name' }} {% endcustomobject %} |

****Return a single object from an object filter****

These examples use the following:

- An additional object filter called **oldest\_dog**
- Object property called **Name**

|  |  |
| --- | --- |
| ****Structure**** | ****Example**** |
| {{ object\_filter.object\_filter\_name.object\_property}} | {{ object\_filter.oldest\_dog.Name }} |
| {{ object\_filter.object\_filter\_name | lookup: 'object\_property' }} | {{ object\_filter.oldest\_dog | lookup: 'Name' }} |

****Return an integer from an object filter****

These examples use the following:

- An additional object filter called **count\_of\_dogs**

|  |  |
| --- | --- |
| ****Structure**** | ****Example**** |
| {{ object\_filter.object\_filter\_name }} | {{ object\_filter.count\_of\_dogs }} |

****Retrieve object records****

To retrieve the most recent object records for an object, you’ll need to loop through all the object records. This example uses the following:

- Object called **Pets**

|  |  |
| --- | --- |
| ****Structure**** | ****Example**** |
| {% customobjects object\_type\_title="Title" as alias %} {% for object\_instance in alias %} {{ object\_instance.record }} {% endfor %} {% endcustomobjects %} | {% customobjects object\_type\_title="Pet Profile" as pets %} {% for pet in pets %} {{ pet.name }} {% endfor %} {% endcustomobjects %} |

## Object data in subject lines

You can personalize your subject lines with any of the custom object tags:

- {% object\_filter %}
- {% object %}
- {% customobject %}

For example, you can use the {% object %} tag in the subject line of your message to display the name of a customers pet directly.

Draft view:

![](https://klaviyo.zendesk.com/hc/article_attachments/37963491682331)

Email preview:

![](https://klaviyo.zendesk.com/hc/article_attachments/37963491688475)

## Object data in show/hide logic

You can also configure whether to show or hide block in a template based on object data. Dynamically showing or hiding a block based on object data uses the same tags as the template builder. You can reference objects by ID, properties from object filters, or aggregates from object filters.

You must create object filters before you can reference them in show/hide logic.

For example, if you have a **Pet** object with a property called **Breed**, you can choose to only show a block to pet owners with a certain breed of dog using the **object.Breed** condition.

To set show/hide logic, click on the block you’d like to set the rules for and select ****Use code**** on the **Display** tab.

Enter the condition directly in the code editor. You can use object filters and the object template tag if it’s a message for a date-triggered flow based on object data.

![](https://klaviyo.zendesk.com/hc/article_attachments/37963491690267)

For more flexibility (e.g., making some information conditional on information returned by {% customobject %} or {% customobjects %}) then consider using [advanced conditional logic](https://help.klaviyo.com/hc/en-us/articles/7655926841499) with {% if … %} logic directly in a text block.

## Object filters

### What is an object filter?

Object filters enable you to limit the returned object records based on specific criteria you set so you can display records of a certain type.

### Create a new object filter

To get started with creating an object filter:

1. Add a new text block or edit the text in an existing text block in your template.
2. Select the ****Personalization**** button.

![](https://klaviyo.zendesk.com/hc/article_attachments/35160309938075)

3. Within the personalization model, select ****Objects**** from the **All types** dropdown.
4. Select the object that contains the data you’d like to set a filter for.
5. Select the object property you’d like to set a filter for.
6. Select ****Create new filter****.

On the **Create object filter** modal, set the following information:

- ****Name****
  Create a name for your object filter.
- ****Filter conditions****
  Define the rules an object must meet to be included in the text block.
- ****Behavior when multiple records meet the conditions****
  Define the behavior for cases where multiple records meet the conditions.

![](https://klaviyo.zendesk.com/hc/article_attachments/35305347554715)

Once your object filter is created, you can use it in show/hide logic and personalization tags to display specific object records based on the criteria you set.

## Additional resources

[Getting started with objects](https://help.klaviyo.com/hc/en-us/articles/35105337172123)

[Message personalization reference](https://help.klaviyo.com/hc/en-us/articles/4408802648731)

[How to use the preview panel for message personalization](https://help.klaviyo.com/hc/en-us/articles/27843522951707)