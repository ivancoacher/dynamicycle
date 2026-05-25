---
id: "32908976218779"
title: "How to use a table block in an email"
source_url: "https://help.klaviyo.com/hc/en-us/articles/32908976218779-How-to-use-a-table-block-in-an-email"
section: "Build and use templates"
category: "Content"
category_slug: "content"
klaviyo_updated: "2026-04-21T13:56:48Z"
language: "en"
---
## You will learn

Learn how to use a table block in an email. These blocks can display images and text side by side. Table blocks can also be dynamic, iterating over data to personalize the email to each recipient.

## Understanding table blocks

There are 2 types of table blocks:

- [****Static****](#h_01JHTHB3XW47TKKGRFRKB23GZ8)
  This type of table block displays the exact number of rows and columns you select. Each recipient sees the same table layout, but the content could vary if you use personalization, event, catalog, or other tags.
- [****Dynamic****](#h_01JHTHB3XX74DSMF9VTDS0H07M)
  These table blocks allow you to iterate over a list of data (e.g., a list of items in an abandoned cart or order confirmation flow). The number of rows is determined by the number of list items: if someone ordered 1 item, they will have 1 row; if they ordered 5 items, they’ll have 5 rows.

The most common use case for a dynamic table block is highlighting products in an abandoned cart message. This uses a dynamic block to display multiple rows with images, product names, and prices of each abandoned item.

### When to use table blocks

A table block is one of several ways to put 2 or more pieces of content side by side. Alternatives include split blocks and columns.

Learn more about the different options to place content side by side in the table below.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ****Content layout**** | ****Number of columns**** | ****Width options**** | ****Allowed content types**** | ****Can columns stack on mobile view?**** |
| ****Split block**** | 2 | Precise control (Use **Split settings > Column widths**) | Image or text only | Yes |
| ****Columns**** | 1-4 | Limited selection | Any type of content block (e.g., text block, image block, review quote block) | Yes |
| ****Table block**** | Any number | Precise control (Use **Column width** > **Manual**) | Image or text only | No |

Tables can be challenging for accessibility, as screen readers have a hard time parsing them.

## Static table blocks

The word “static” here simply means the content and number of rows in the table stays the same for every recipient. The only time the content changes is if you add dynamic content, like personalization, date, and catalog tags, within a static table block.

### Use cases for static table blocks

Use a static table block to:

- Show a specific item, such as for flash sales or product launches.
- Always include the same number of items (e.g., show the most recently viewed item in a browse abandonment message.
- Create a flow message where the event data only contains 1 item, which includes:
  - Abandoned cart flows (added to cart trigger)
  - Browse abandonment flows
  - Back in stock and price drop flows
- You’d like to place static text and images side-by-side

### How to create a static table block

1. Navigate to an email (i.e., a campaign email, template, or flow email).
2. From the **Blocks** menu, drag a ****Table**** block into the canvas.
   ![The table block icon](https://klaviyo.zendesk.com/hc/article_attachments/32908976160539)
3. Open the ****Styles**** menu for the block. Note that ****Static**** is already selected, as this is the default setting for table blocks.
   ![The block's styles menu](https://klaviyo.zendesk.com/hc/article_attachments/32908976180891)
4. Under **Columns**, click ****Add column**** to add additional columns.
   ![The Add columns option](https://klaviyo.zendesk.com/hc/article_attachments/32908976186139)
5. Under **Rows**, click ****Add row**** to add additional rows.
   ![The Add row option](https://klaviyo.zendesk.com/hc/article_attachments/32908961551387)
6. Return to the block’s ****Content**** tab.
7. Use the **Cell selector** area to choose which cell you’d like to edit.
   ![The Cell selection area](https://klaviyo.zendesk.com/hc/article_attachments/32908976200091)
8. Choose whether that cell should be text or an image using the **Cell content** menu. Repeat for each cell.
9. Add content (i.e., text or an image) below the **Cell content** menu.
10. Once you’ve added content to every cell, click the back arrow to return to the main **Content** menu and continue building your email.
    ![The main Content menu](https://klaviyo.zendesk.com/hc/article_attachments/32909413261083)

## Dynamic table blocks

If your ecommerce platform has a standard integration with Klaviyo, you do not need to build a dynamic table block. Instead, use the table blocks found in the default abandoned cart or placed order flows found in the [flow library](https://help.klaviyo.com/hc/en-us/articles/115002774932#h_01H9JGTZ8Q0PAF1FY71QDZBJ7M).

Dynamic table blocks iterate over a data set to repeat content based on the number of entries within it. The block iterates until it reaches the end of the list. For example, you can show the exact number of products in someone’s cart.

In order to use a dynamic block, you must reference data formatted as a nested list, where each list entry follows the same format. The most common use case is product information found in a flow’s trigger event (e.g., started checkout, placed order), but you can also use a [web feed](https://help.klaviyo.com/hc/en-us/articles/115005258768) to list blog posts, or reference profile data that’s formatted as a list.

### Elements of a dynamic table block

Creating a dynamic content block requires 3 elements:

- ****Row collection****
  The location of the data to iterate over. When looking at your source data (e.g., the items in a **Started Checkout** event’s metadata), this is the portion of the relevant template tags that is the same for every tag.
- ****Row alias****
  A shorthand way to reference your row collection as the table iterates through your data set. The row alias is usually **item**, but you can use any text.
- ****Dynamic content****
  The content that will appear in every row. For example, you may want to display an image, product name, price, and variant information for every item someone left in their cart.

### Use cases for dynamic table blocks

Use a dynamic table block if you’re dynamically referencing a list of data and every entry in the list is formatted in the same way. This includes:

- Abandoned cart flows (checkout started trigger)
- Order confirmation flows
- Up- or cross-sell flows

### How to create a dynamic table block

All tags used in these instructions are examples, and likely differ from the correct tags for your account. The correct tags for your message depend on your data’s source and structure (often an ecommerce platform), which is different for many Klaviyo accounts.

This section covers dynamic table blocks at a high level. For more detailed instructions on this process, learn [how to build dynamic blocks in a flow email](https://help.klaviyo.com/hc/en-us/articles/4408802597659).

1. Navigate to the editor for an email. If you are using event data (e.g., abandoned cart details), navigate to an email within a flow triggered by the relevant event.
2. From the **Blocks** menu, drag a ****Table**** block into the canvas.
   ![The table block option](https://klaviyo.zendesk.com/hc/article_attachments/32908976160539)
3. Open the ****Styles**** menu for the block and select ****Dynamic****.
   ![The Styles menu within a table block](https://klaviyo.zendesk.com/hc/article_attachments/32908976202779)
4. Set your **Row collection**: use the portion of the personalization tag that is consistent across each item you’d like to display.
   - For example, if **{{ event.products.0.imageURL }}** is the tag for the first item’s image, and **{{ event.products.1.name }}** is the tag for the second item’s name, then your row collection should be **event.products**.
   - The row collection will almost always be the portion of the tag preceding the first number (e.g., **event.extra.line\_items** if the full tag is **{{ event.extra.line\_items.0.product.name }}**).
5. Set your **Row alias** as **item**.
6. Return to the block’s ****Content**** tab.
   - Add content to each cell of the table. Generally, the cell on the left is an image, and the cell on the right is text containing dynamic tags with product information.
7. Replace everything preceding the first number in each tag in your table with your row alias (i.e., “item”). For example:
   - {{ event.extra.line\_items.0.imageURL }} becomes {{ item.imageURL }}
   - {{ event.items.0.product.name }} becomes {{ item.product.name }}
8. Click ****Preview & test**** to preview your email.
   - Make sure you are previewing using the right data (e.g., if this is an abandoned cart message, preview using the **Started checkout** event) or the table won’t display anything.

This process allows developers and code-savvy marketers to create highly customized content. If you don't have a developer on your team and are not comfortable creating this block yourself, consider reaching out to a [Klaviyo Partner](https://connect.klaviyo.com/) for assistance.

Learn more about creating an [abandoned cart flow](https://help.klaviyo.com/hc/en-us/articles/115002779411) or [using event data to personalize email and SMS flows](https://help.klaviyo.com/hc/en-us/articles/115002779071).

### How dynamic table blocks work

Dynamic table blocks work exactly like a **for** loop in most programming languages.

- The **Row collection** identifies the portion of the data to loop through.
- The **Row alias** is an alias to identify where dynamic content appears.
- Every tag that uses the **Row alias** will reference the correct line within the event data, based on which row it appears in.

When the email is rendered, Klaviyo loops through each item in the data set. The first time, the row alias is replaced with **[row collection].0.**, referencing the first item in the data set. The second time, the row alias is replaced with **[row collection].1.**, indicating the second item in the data set. This process then continues until no items remain, and there is one row for every item in the data set.

## Additional resources

- Course: [Customize and personalize emails using Django](https://academy.klaviyo.com/en-us/courses/customize-and-personalize-emails-using-django/1865943)
- [How to display products vertically in emails](https://help.klaviyo.com/hc/en-us/articles/19462923466651)