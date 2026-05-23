---
id: 27843522951707
title: "How to use the preview panel for message personalization"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/27843522951707-How-to-use-the-preview-panel-for-message-personalization"
section: "Use variable syntax and tags"
category: "Content"
category_slug: "content"
klaviyo_updated: "2026-04-21T13:54:37Z"
language: en
---

## You will learn

Learn how to use the preview panel to understand the personalization data available for your messages and how to access personalization variables. Use the preview modal as your source of truth for personalization options.

## Preview panel for templates, campaigns, and flows

Open the preview panel for any message by clicking ****Preview & test****. Here, you have the option to choose your data source. Depending on where the message is, you’ll have slightly different options.

### Templates

If you edit a template by navigating to ****Content > Templates****, you can toggle between profile and event data. For profile data, you can select a specific profile. For event data, you can select a specific event.

Event personalization is only supported for flows triggered by that event. If you use a personalization tag from an event, but send that email another way (e.g., a campaign, a flow triggered by a different event, or a flow triggered by a list), the personalization will not render.

![](https://klaviyo.zendesk.com/hc/article_attachments/34449970392347)

### Campaigns

If you edit a campaign message, you’ll only have access to profile personalization, not event personalization. Event data is not supported for campaigns, because campaigns cannot be associated with a specific event.

### Flows

If you edit a message that is part of a flow triggered by a metric, price drop, low inventory, or back in stock, the preview panel will include both profile and event personalization tags. Profile personalization is supported in all flows; use the **Add personalization** button in a text block to add these tags.

## Choosing a profile to preview

When reviewing profile personalization options in the preview modal, the default profile is the user profile associated with your Klaviyo login. Note that this is different from the profile for your email in your own Klaviyo account, and has a very limited set of personalization tag options, like first and last name.

To see all the data available in a real customer account, select another profile.

Learn how to change the preview profile for different messages:

- ****Templates, campaigns, and flow messages (not event-triggered)****
  Use the **Search profiles** field in the preview modal.
  ![](https://klaviyo.zendesk.com/hc/article_attachments/34449986377627)
- ****Event-triggered flow messages****
  Profile data in event-triggered flow messages comes from the profiles that most recently took the trigger action. Use the arrows to toggle between up to 10 recent events and select the associated profile.
  ![](https://klaviyo.zendesk.com/hc/article_attachments/34449970406683)

## Choose an event to preview

When you edit an email by navigating to ****Content > Templates****, you have the option to select an event to preview. When you edit an event-triggered flow message, the event is selected automatically.

In both scenarios, you can toggle through the last 10 instances of the event to choose one to preview as. Use the arrows to navigate through them until you find one that you’d like to preview with.

## Basic personalization tags

Once you’ve selected a profile or event to preview as, hover over any piece of data to see the personalization tag. Click to copy it to your clipboard, then paste it into your message.

![](https://klaviyo.zendesk.com/hc/article_attachments/34449970410267)

These tags can be used as-is, or you can use [filters](https://help.klaviyo.com/hc/en-us/articles/360058907911) to adjust how they display. Every variable you copy from the preview modal includes the **default** filter, **|default:''**. You can delete this filter, leave it as-is, or fill it in to set a default value. Default values appear when no data is available for a particular recipient. If you don’t set a default value, the variable will not render if data is unavailable.

## Advanced personalization tags

If you’re looking at event data, there might be an overwhelming amount to sort through. Events often contain a large quantity of metadata, which is information about the action someone took to trigger the event.

Generally, some of this data is “nested,” which means it’s stored inside of another variable. Nested data is used to organize information that is related.

The **Placed Order** event is one event that uses nested data. The event’s metadata likely includes details about the person who ordered, as well as the items they ordered. Here’s an example of some of the data you might see:

- ****Address****
  The customer’s address details are nested under the **shipping\_address** heading, which contains their street address, city, state, and country.
  ![Nested event data](https://klaviyo.zendesk.com/hc/article_attachments/28717391600411)
- ****Purchased products****
  The items they purchased are listed under the **line\_items** heading. Immediately under the **line\_items** heading is another heading, **0**. Within the **0** heading are details about the first product ordered. If you scroll further, you might see a second heading, **1**, which represents the second ordered item. In numbered data like this, the structure of each entry is generally the same, but each entry will contain details about a different item (e.g., a product in their order).
  ![Complex nested event data](https://klaviyo.zendesk.com/hc/article_attachments/28717391602971)

Nested data is indicated by a small arrow icon. Click this icon to collapse an entry and hide its contents, to make the data easier to navigate.

The personalization tag always represents the path you use to find it within the data. For example, an unnested event variable will follow a structure like this: {{ event.source }}. However, a nested variable found by navigating to ****extra > customer > default\_address > address1**** would look like this: {{ event.extra.customer.default\_address.address1 }}.

### Iterating through nested variables

If you select a variable that contains a number, like {{ event.extra.line\_items.0.product.title }}, that means it is possible to iterate through each item in the list. You can iterate through list items with a [for loop](https://developers.klaviyo.com/en/docs/django_message_design#for-blocks), a [content repeat](https://help.klaviyo.com/hc/en-us/articles/4408802445339), or a [dynamic table block](https://help.klaviyo.com/hc/en-us/articles/4408802597659).

If you choose not to use one of these iteration tools, make sure to always use the first item in a list, as some recipients might only have one item. You can tell if a variable references the first list item by reviewing the number in the variable itself:

- {{ event.extra.line\_items.0.product.title }} is the variable for the title for the first item in an order.
- {{ event.extra.line\_items.1.product.title }} is the variable for the title for the second item in an order.
- {{ event.extra.line\_items.2.product.title }} is the variable for the title for the third item in an order.

We only recommend this process for technically savvy marketers, or for anyone who has access to a developer. While our product does support custom dynamic content, our support team cannot help you build out your custom templates beyond offering the general guidance covered in this documentation.

## Outcome

After reading this article and trying these steps in your own account, you should understand how to navigate the preview modal and find the personalization data you need for your messages.

## Additional resources

- [Message personalization reference](https://klaviyo.zendesk.com/hc/en-us/articles/4408802648731)
- [How to skip lines in a dynamic table block](https://klaviyo.zendesk.com/hc/en-us/articles/25825620314651)