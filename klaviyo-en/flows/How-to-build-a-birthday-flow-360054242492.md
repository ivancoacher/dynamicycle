---
id: "360054242492"
title: "How to build a birthday flow"
source_url: "https://help.klaviyo.com/hc/en-us/articles/360054242492-How-to-build-a-birthday-flow"
section: "Lifecycle flows"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-04-21T13:54:51Z"
language: "en"
---
## You will learn

Learn how to create a flow that sends out messages on a customer's birthday in order to show how much you care about your customers. After all, who doesn’t like being wished a happy birthday?

A birthday flow can be made a number of different ways:

- Containing only 1 message
- Include many splits for enhanced personalization
- Be both a half-birthday and birthday flow

In this article, you’ll learn how to create a birthday flow and see examples of what this flow can look like.

![](https://fast.wistia.com/embed/medias/hoxiwgq9n4/swatch)

## Before you begin

Before you can use a birthday flow, you must collect birthdays as a profile property on your customers' profiles. There are several ways to do this.

- Add a date field to a [sign-up form](https://klaviyo.zendesk.com/hc/en-us/articles/360026474752) for subscribers to fill out their birthday.
- Manually import birthdays using a [CSV file](https://klaviyo.zendesk.com/hc/en-us/articles/1260806293150).
- Ecommerce integrations will import birthdays as a profile property if it exists as a property within the ecommerce platform.

## Create a birthday flow

1. From the ****Flows**** tab, create a [date property-triggered flow](https://help.klaviyo.com/hc/en-us/articles/360002732652).
   ![In the list of flow triggers, the Date Property option can be found at the bottom](https://klaviyo.zendesk.com/hc/article_attachments/28720670182171)
2. In the dropdown, choose the property you used to collect subscribers’ birthdays. You need at least 1 profile to have this property in order for it to appear in the dropdown. If you don’t see any listed, check that profiles’ birthdays are in 1 of the [accepted date formats](https://help.klaviyo.com/hc/en-us/articles/115005253428).
   ![From the Trigger Setup menu, you can choose a date property from the dropdown such as a Birthday property if it exists in your account](https://klaviyo.zendesk.com/hc/article_attachments/28720670191387)
3. Choose when you want to start the flow: on or before the person’s birthday.
4. Then, choose the time of day for the target date delay. For birthday flows, we recommend setting this to earlier in the day and using **Recipient’s Local Timezone**. Here, we set the delay to 9 am. For how often you want the flow to repeat, choose ****Yearly****.
   ![The Yearly option should be selected from the 'When should this flow repeat' section](https://klaviyo.zendesk.com/hc/article_attachments/28720670196123)
5. Once you configure the settings for the trigger, click ****Save****.
6. If you choose for the flow to begin before the date, a target date delay will appear. This point represents the day of someone’s birthday and you can add actions before or after this point.
   ![In the flow editor, the trigger will display its configuration](https://klaviyo.zendesk.com/hc/article_attachments/28720658443163)
7. Next, begin adding your messages. Make sure to add a message on the profile’s actual birthday. Below is a single-message example.
   ![Messages can be added immediately after the flow trigger such as a 'Happy Birthday' message](https://klaviyo.zendesk.com/hc/article_attachments/28720670198555)

## Birthday flow examples

### Starting slightly before a birthday

Setting the flow to start before a birthday is useful when you’re providing an in-person offer or discount, as it gives them time to plan when they want to use it. You can then follow up on the day-of to wish them a happy birthday and remind them of your offer.

In the following example, a flow email is sent a week before the recipient’s birthday. On their actual birthday, they will then receive either an SMS or WhatsApp message (if they have opted in to one of those channels) or an email.

![](https://klaviyo.zendesk.com/hc/article_attachments/34362688300187)

### Sending a half-birthday message

Many people expect to get birthday wishes from businesses on or around their birthday, but it’s not the same for their half-birthday. Wishing your subscribers a happy half-birthday is a nice gesture and a way to remind them about your brand.

Using the same setup as above, you can also send half-birthday messages. Set the flow to start 6 months before someone’s birthday and then add your email, SMS, or WhatsApp message.

![You can set the trigger to start 6 months before someone's birthday and send a 'Happy 1/2 Birthday' message](https://klaviyo.zendesk.com/hc/article_attachments/28720670202523)

[RAREFORM](https://www.rareform.com/) uses a similar concept in their half-birthday flow. Their flow contains only 1 message, shown below, which contains a lighthearted message and discount for recipients.

![Example of a half birthday message from RAREFORM](https://klaviyo.zendesk.com/hc/article_attachments/28720670177051)

## Personalize your birthday flow

As you grow and gain more information about your subscribers, consider adding more personalization into your birthday and half-birthday flows. For instance, you can use conditional splits based on profile properties to show products/styles you know they love.

![Example of a birthday flow with conditional splits based on customer preferences using profile properties](https://klaviyo.zendesk.com/hc/article_attachments/28720670207259)

## Additional resources

See the [date and timestamp formats that Klaviyo accepts](https://help.klaviyo.com/hc/en-us/articles/115005253428).

Read more about date property-triggered flows:

- [How to create a date property-triggered flow](https://help.klaviyo.com/hc/en-us/articles/360002732652)
- [Understanding how date-based flows schedule recipients](https://help.klaviyo.com/hc/en-us/articles/360054240252)
- [Understanding time delays in date property flows](https://help.klaviyo.com/hc/en-us/articles/360054705431)