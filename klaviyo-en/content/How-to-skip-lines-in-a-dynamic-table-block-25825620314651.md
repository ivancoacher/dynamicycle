---
id: "25825620314651"
title: "How to skip lines in a dynamic table block"
source_url: "https://help.klaviyo.com/hc/en-us/articles/25825620314651-How-to-skip-lines-in-a-dynamic-table-block"
section: "Use variable syntax and tags"
category: "Content"
category_slug: "content"
klaviyo_updated: "2026-04-21T13:54:36Z"
language: "en"
---
## You will learn

Learn how to skip rows (e.g., items) in a dynamic table block. The most common use case for this is hiding irrelevant items, like shipping insurance or free gift items, from an abandoned cart email. However, you can follow these steps for any email that uses a dynamic table block.

This process involves directly editing your email’s code. This is only recommended for technically savvy marketers or those who have access to a developer. Our support team cannot help you write custom code beyond the general guidance covered in this documentation. To maintain the security of your data, Klaviyo's support team is not able to open HTML files.

## Before you begin

This article covers how to hide items from existing dynamic table blocks. If you have not yet created a working dynamic table block (e.g., the products in an abandoned cart or order confirmation email), learn how to [create one from scratch](https://klaviyo.zendesk.com/hc/en-us/articles/4408802597659) or start with a message in our [flow library](https://klaviyo.zendesk.com/hc/en-us/articles/115002779411).

## Write your **if** statements

Before making changes to your template, create 2 code snippets using a text or code editor (somewhere you can copy and paste the snippets from later). Each code snippet will consist of 3 parts:

1. [An opening **if** tag](#h_01HY3CPMXG09XHJQTMZP0VJV82), `{% if … %}`, indicating which items should appear in your table block.
2. [Content](#h_01HY3CPMXGEPNZ4B9JC9SS91F2), like an image tag or text about the product.
3. [A closing tag](#h_01HY3CPMXGHQ358JG8EH463SGG), `{% endif %}`.

### Create the opening **if** tag

Here are some examples of opening **if** tags:

|  |  |
| --- | --- |
| ****Tag**** | ****Meaning**** |
| {% if item.price != 0 %} | If the item price (**item.price**) is anything other than 0. |
| {% if item.product.name != "Route Shipping Insurance" %} | If the item name (**item.product.name**) is anything other than “Route Shipping Insurance.” |
| {% if not "T-Shirt" in item.product.title %} | If the item’s title (**item.product.title**) does not contain “T-Shirt.” |
| {% if item.title %} | If the item’s title (**item.title**) is set (i.e., has any value). |

These tags are case sensitive and must match your data exactly. For example, if the variable for your item’s price is something other than **item.price** (e.g., **item.Price** or **item.details.line\_price**), update the code to match your data source.

### Create the content for the if statement

For content, follow these steps to use the existing content from your dynamic table block. Write this code snippet in a code or text editor; you’ll add it to your template in the next section.

1. Under **Cell Content** for the table block’s image, click ****Replace**** to view the image placeholder.
   ![Replace cell content button.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28717391398811)
2. Copy the entire code from the **Dynamic variable or dynamic URL** field. Note that this may be a simple dynamic variable, or it may be a longer code snippet; copy all of it, regardless of length.
   ![Abandoned cart product image variable.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28717418658971)
3. Replace the placeholder in this code snippet with the code you copied from the **Dynamic variable or dynamic URL** field.

   ```
   <img src="PLACEHOLDER" style="width: 200px; height: auto;" width="200">
   ```

If your existing table block has a simple dynamic variable for the image, the resulting content will look something like this:

```
<img src="{{item.product.variant.images.0.src}}" style="width: 200px; height: auto;" width="200">
```

If your existing table block contains a longer code snippet, the resulting content might look like this:

```
<img src="{% if item.product.variant.images.0.src %}{{item.product.variant.images.0.src}}{%else%}{{item.product.images.0.src|missing_product_image}}{%endif%}" style="width: 200px; height: auto;" width="200">
```

### Add your ending tag

Then, put all the content together: your opening if statement, then your content, and finally a closing `{% endif %}` tag.

### Repeat for the text content

Then, repeat this process with the content from the right side of your table block (e.g., the text content). Click ****</>**** to open the code editor and copy all of the HTML content, then wrap this content in the same if statement (steps 1 and 3) you used for the image content.

Here’s what everything looks like together:

|  |  |
| --- | --- |
| ****Code snippet 1 (product image)**** | ****Code snippet 2 (product details)**** |
| ``` {% if item.product.name != "Route Shipping Insurance" %} <img src="{% if item.product.variant.images.0.src %} {{item.product.variant.images.0.src}}{%else%} {{item.product.images.0.src|missing_product_image}} {%endif%}"style="width: 200px; height: auto;" width="200"> {% endif %} ``` | ``` {% if item.product.name != "Route Shipping Insurance" %} <h3><a href="{{ organization.url }}products/{{ item.product.url }}">    {{ item.product.name }} </a></h3> <p>    Quantity: {{ item.quantity|floatformat:0 }} —     Total: {% currency_format item.line_price|floatformat:2 %} </p> {% endif %} ``` |

And here’s a breakdown of those code snippets:

|  |  |
| --- | --- |
| ****Code snippet 1 (product image)**** | ****Code snippet 2 (product details)**** |
| ``` {% if CRITERIA %}    IMAGE PLACEHOLDER CONTENT {% endif %} ``` | ``` {% if CRITERIA %}    PRODUCT DESCRIPTION {% endif %} ``` |

When using these code snippets, make sure to use straight quotes (") rather than curly quotes (“) to ensure the code renders correctly.

Once you’ve written both code snippets, continue in the template editor following the steps below.

## Skip rows in a dynamic table block

Before editing your dynamic table block, consider saving the original block as universal content in case you need to reference it in future messages. Then unlink the block and edit it separately, so your edits aren’t saved to the universal content block.

1. If your email is part of a flow, set it to **Draft** or **Manual** so messages don’t send while you edit the flow message.
2. Make sure the **Cell Content** for both columns of the new table block are set to **Text**.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28717418651163)
3. Click ****</>**** to open the HTML editor for the left side of the table block.
4. Copy the product image code snippet you created in the previous section and paste it into the HTML field.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28717418647579)
5. Click ****Done**** in the upper left.
6. Navigate to the editor for the right side of the table block.
7. Click ****</>**** to open the HTML editor for the right side of the table block.
8. Copy the product details code snippet you created in the previous section and paste it into the HTML field, replacing all previous content.
9. Click ****Done****.
10. Preview the email to ensure it appears as expected: the skipped item should not appear, but all other items will appear normally. Make sure to preview with an event that contains the item you’re trying to hide, so you can ensure it is hidden.

### Conditional statements and the inline text editor

When you add certain conditional statements to a text block, they may disappear from the inline text editor. The code is still present; it is just hidden. To view and edit conditional statements, open the text block's **Source code** field.

The following tags are only visible in a text block's **Source code** field:

- {% for ... %}
- {% endfor %}
- {% if ... %}
- {% elif ... %}
- {% else %}
- {% endif %}
- {% with ... %}
- {% endwith %}

## Troubleshooting

****No items appear in the preview****

1. Make sure you are previewing with an event that matches the data source you used (e.g., **Started checkout** for an abandoned cart message).
2. Confirm the **Repeat for** and **Row alias** exactly match the **Row collection** and **Row alias** from the original block.

****The item that should be skipped is still appearing****

Check the spelling and capitalization of your if statement. If the product is still appearing, that means it meets the criteria in your if statement, so your if statement is not configured correctly. Learn more about [conditional logic in templates](https://help.klaviyo.com/hc/en-us/articles/7655926841499).

## Outcome

After following these steps, any items that don’t meet the criteria in your if statement will not appear in messages like abandoned cart or order confirmation emails.

## Additional resources

- [Message personalization reference](https://klaviyo.zendesk.com/hc/en-us/articles/4408802648731)
- [How to import a custom HTML template](https://klaviyo.zendesk.com/hc/en-us/articles/115005254068)