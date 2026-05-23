---
id: 4408802445339
title: "How to use the content repeat feature"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/4408802445339-How-to-use-the-content-repeat-feature"
section: "Build and use templates"
category: "Content"
category_slug: "content"
klaviyo_updated: "2026-04-21T13:55:00Z"
language: en
---

## You will learn

Learn how to use the block repeat feature for a section or a block in a Klaviyo email template. This feature allows you to repeat the content of a block or section for each entry in an array (i.e., list) of data from a recipient’s event or profile data, or from a data feed.

## Before you begin

If you are unfamiliar with using event, profile, or catalog data in emails, check out our [message personalization reference](https://help.klaviyo.com/hc/en-us/articles/4408802648731) as a first step.

It will also be helpful to understand [data types in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115005237648-About-Data-Types), particularly lists (i.e., arrays). An array stores multiple pieces of data that are structured the same way. For example, a customer’s purchased items are stored as an array within a Placed Order event. The items array contains 1 entry per item ordered, and each entry contains the details for 1 item (e.g., item name, image URL, quantity, size, color, etc.).

## Content repeat feature use cases

To use the content repeat feature, you’ll need an array or list of data. The table below lists some examples of arrays of data that may exist in your Klaviyo account, along with sample use cases.

|  |  |
| --- | --- |
| ****Data source**** | ****Sample use case**** |
| The array of ordered items in a Placed Order event | Display a customer’s purchased items (including a product image, price, title, and variant information) in their order confirmation email. |
| A list of existing subscriptions for someone subscribed to recurring orders | Show a customer a list of their active subscriptions in a campaign. |
| A list of recent blog entries from a custom web feed | Provide an up-to-date list of your most recent blog posts in your welcome flow, including a link to the blog post and a preview of its content. |

You can use the content repeat feature with any array, whether it’s stored in a subscriber’s profile or event data, or in one of your [web feeds](https://klaviyo.zendesk.com/hc/en-us/articles/115005258768). The examples above are just a small sample of how this feature can be used.

## How to use the content repeat feature

To enable the content repeat feature, navigate to the section or block you’d like to repeat, then click ****Display Options****. In the **Content Repeat** section, click ****Create Content Repeat****.

You’ll see two fields appear: **Repeat for** and **Item alias**. To fill out these fields and set up your repeating content, follow the steps below:

1. [Identify your “repeat for”](#01FK124H745446BNHM34CE4J1Q)
2. [Choose your “item alias”](#01FK124H74R7GZSHJPWCR0QHQX)
3. [Build your repeating content](#01FK124H748C3S30TTNGD7EMWY)
4. [Preview your email](#01FK124H749B4585QNE6R6AP9T)

### Identify your “repeat for”

Add the name of the array you plan to iterate over to the **Repeat for** field.

To find the name of your array, view the data from your data source (i.e., profile data, event data, or a data feed). In this example, we’ll walk through finding the array from event data:

1. In your email template, click ****Preview and test****.
2. Click ****Event****.
3. Select the event that will trigger this flow email (e.g., Started Checkout).
4. Scroll through the preview data for your event until you find an array that contains the information you need. You can use the arrow icons on the left of the data to collapse sections you don’t need and make it easier to navigate.
   In this example, there are two arrays that store item information: In this case, you’d want to use the more detailed array, **line\_items**, since it contains the detailed information needed to display in the repeating block. To find the appropriate variable to set in the **Repeat for** field, find two variables within the first section of the array and copy them. In this example, we’ll copy the variables for **variant\_price** and **title**. Here are the two tags we copied: `{{ event.extra.line_items.0.variant_price }}{{ event.extra.line_items.0.title }}`
   ![navigate event data](https://klaviyo.zendesk.com/hc/article_attachments/28717812130459)

   - **Items**
     A top-level array and contains a simple list of each item’s name, but no other information
   - **Line\_items**
     Nested within the **extra** array, and contains more detail including each item’s title, price, SKU, and image URL![Two items subsections in event data](https://klaviyo.zendesk.com/hc/article_attachments/28717851792667)
5. Ignore the curly brackets and look at the variables within them. Note that the beginning of both variables are the same: `event.extra.line_items.0`. Use everything up to (but excluding) the dot and the number at the end of this portion of the variable as your **Repeat for**. In this example, the appropriate setting for the **Repeat for** field is `event.extra.line_items`.

![repeat for options](https://klaviyo.zendesk.com/hc/article_attachments/28717851791131)

### Choose your item alias

Your item alias can be any text you’d like to use (with no special characters or spaces). You’ll use this alias within your repeating block to identify variables that should be pulled from the array you selected above. Choose a simple but descriptive alias, so it’s easy to remember.

For example, if your block is repeating over a list of items in an abandoned cart, **item** is a good alias to use. If your block is repeating over a list of blog posts, then you could use **post** as your alias.

You can use any alias you’d like; just make sure to consistently use that alias in variables from your array (as outlined in the following steps).

![item alias](https://klaviyo.zendesk.com/hc/article_attachments/28717851789595)

Once you’ve filled out the **Repeat for** and **Item alias** fields, click ****Save Changes**** and start building your content.

### Build your repeating block/section

Once you’ve set your **Repeat for** and **Item alias** settings, add in personalization tags to the content block to iterate over. You can add any type of variable to this block, including profile and event data, but any tags that are pulled from your array (e.g., the list of items someone ordered) must be adjusted slightly.

The full title and variant price variables used in the example above were:

`{{ event.extra.line_items.0.variant_price }}`

`{{ event.extra.line_items.0.title }}`

If you add the variables above to the block, it will repeat the block once per item in your array, but every repetition will show the title and price of the ****first**** item in the array.

To show the title and price for each item, replace the text from the **Repeat for** setting (`event.extra.line_items`), plus the subsequent dot and number (`.0`) with your **Item alias** (`item`). The resulting variables for this example are:

`{{ item.variant_price }}`

`{{ item.title }}`

Repeat the process with any other variables you’d like to include from the array.

Everything in the block or section with the block repeat feature enabled will be repeated once per item in the array. If you have any content you’d like to appear just once, add it in a different block or section.

Additionally, the custom variables created through this process (e.g., `{{ item.title }}`) only work inside the block or section where the block repeat section is enabled. If you add these custom variables elsewhere, they will not render.

### Preview your email and troubleshoot

Once you’ve built your repeating block, preview your email. If the email references event data, select the same event you used to build the block (i.e., the event that will trigger this flow). If your block references profile data, select a profile that has the correct variables.

If the repeating block in your preview email appears blank or doesn’t contain all the content you expected, return to the steps above. Make sure your **Repeat for**, **Item alias**, and all custom variables are correctly configured following the steps above. Then, review the preview data you’re using: ensure that you’ve selected the correct event, and that the sample event you’ve chosen contains the data you need.

## Additional resources

- [Message personalization reference](https://klaviyo.zendesk.com/hc/en-us/articles/4408802648731)
- [Guide to the email template editor](https://klaviyo.zendesk.com/hc/en-us/articles/4407911841435)