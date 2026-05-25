---
id: "115005254188"
title: "How to create a hybrid email template"
source_url: "https://help.klaviyo.com/hc/en-us/articles/115005254188-How-to-create-a-hybrid-email-template"
section: "Advanced template design"
category: "Content"
category_slug: "content"
klaviyo_updated: "2026-04-21T13:54:24Z"
language: "en"
---
## You will learn

Learn how to create custom HTML templates that are compatible with Klaviyo’s drag-and-drop editor (i.e., hybrid templates). By following these steps, you can design a fully custom HTML email while maintaining access to features only available in the drag-and-drop editor (e.g., product blocks or universal content blocks).

We only recommend using custom HTML for technically savvy marketers, or for anyone who has access to a developer. While our product does support custom HTML, our support team is unable to help you build out your custom templates beyond offering the general guidance covered in this documentation. Need help? [Reach out to a Klaviyo Partner.](https://connect.klaviyo.com/)

To maintain the security of your data, Klaviyo's support team is not able to open your HTML files.

## Add a code snippet to your HTML template

Only add one of the code snippets outlined below per email template. One code snippet allows you to add multiple drag-and-drop blocks, so you don't need to add multiple code snippets.

For example, if you’d like to add an image and a table block using the drag-and-drop editor, just follow the [**Add a customizable image block**](https://help.klaviyo.com/hc/en-us/articles/115005254188#h_01HDH0B0301Y7FG9KGBM0RRWW0) steps below. Once you upload your template to Klaviyo and use it in a campaign or flow, you’ll be able to add blocks above or below the image block.

****Add an editable text block****

1. Create a custom HTML template using your preferred HTML editor.
2. Add the following code snippet to your HTML template. Place it wherever you’d like to add your text block in your template.

   ```
   <td align="center" data-klaviyo-region="true" data-klaviyo-region-width-pixels="600">
       <div class="klaviyo-block klaviyo-text-block">Hello world!</div>
   </td>
   ```
3. In Klaviyo, navigate to ****Content > Templates****.
4. Select the ****Email templates**** tab.
5. Click ****Import****.
6. Enter a name for your template, upload your HTML file, and import it.
7. If you open the template from your **Templates** tab, you’ll see your template’s code in Klaviyo’s HTML editor.
   ![A hybrid email template's html](https://klaviyo.zendesk.com/hc/article_attachments/28720656075931)
8. To access the template in Klaviyo’s drag-and-drop editor, add it to a campaign or flow.
9. Select ****Drag and drop**** as the template type.
   ![The drag and drop email option](https://klaviyo.zendesk.com/hc/article_attachments/28720667865243)
10. Note the text block that says **Hello world!** This is your editable text block.
11. Drag and drop additional blocks above or below the text block, as desired.

****Add a customizable image block****

1. Create a custom HTML template using your preferred HTML editor.
2. Add the following code snippet to your HTML template. Make sure to place it wherever you’d like to add your image block after importing your template.
   1. Optionally, you can add a preset image within the div. If you choose to do so, your code will look like this:

      ```
      <td align="center" data-klaviyo-region="true" data-klaviyo-region-width-pixels="600">
          <div class="klaviyo-block klaviyo-image-block">
              <a href="http://klaviyo.com><img src="example.com/my_image.png" alt="My Image" /></a>    </div>
      </td>
      ```

   ```
   <td align="center" data-klaviyo-region="true" data-klaviyo-region-width-pixels="600">
       <div class="klaviyo-block klaviyo-image-block"></div>
   </td>
   ```
3. In Klaviyo, navigate to ****Content > Templates****.
4. Select the ****Email templates**** tab.
5. Click ****Import****.
6. Enter a name for your template, upload your HTML file and import it.
7. If you open the template from your **Templates** tab, you’ll see your template’s code in Klaviyo’s HTML editor.
   ![The hybrid template's HTML](https://klaviyo.zendesk.com/hc/article_attachments/28720656075931)
8. To access the template in Klaviyo’s drag-and-drop editor, add it to a campaign or flow. In the content step, select the template you imported.
9. Note the image block, which will either contain a button to upload an image or the image you included.
10. Drag and drop additional blocks above or below the image block, as desired.

![Image blocks](https://klaviyo.zendesk.com/hc/article_attachments/28720656083611)

****Add a universal content block****

This process is supported for universal content blocks, ****not**** universal sections.

1. Create a custom HTML template using your preferred HTML editor.
2. Add the following code snippet to your HTML template. Make sure to place it wherever you’d like to add your image block after importing your template.

   ```
   <td data-klaviyo-region="true" data-klaviyo-region-width-pixels="600">     <div data-klaviyo-universal-block="block_id_1">&nbsp;<div></td>
   ```
3. Replace **block\_id\_1** with the ID of your universal content block. To find a universal content block's ID:
   1. Navigate to ****Content > Universal content****.
   2. Open a universal content block to edit it.
   3. The URL for this page will follow this format: **https://www.klaviyo.com/email-template-editor/universal/block/BLOCK\_ID**.
   4. Copy the block ID from the URL.
4. In Klaviyo, navigate to ****Content > Templates****.
5. Select the ****Email templates**** tab.
6. Click ****Import****.
7. Enter a name for your template, upload your HTML file and import it.
8. If you open the template from your **Templates** tab, you’ll see your template’s code in Klaviyo’s HTML editor.
   ![The hybrid template's HTML](https://klaviyo.zendesk.com/hc/article_attachments/28720656075931)
9. To access the template in Klaviyo’s drag-and-drop editor, add it to a campaign or flow. In the content step, select the template you imported.
10. Note the universal content block(s).

You can add multiple universal content blocks with a single code snippet. To do so, add another **div** element immediately after the first in the code snippet above, using a different block's ID.

****Add a block of another type (i.e., product block, table block)****

1. Create a custom HTML template using your preferred HTML editor.
2. Add the following code snippet to your HTML template. Place it wherever you’d like to add your block(s) after importing your template.

   ```
   <td align="center" data-klaviyo-region="true" data-klaviyo-region-width-pixels="600">
       <div class="klaviyo-block klaviyo-text-block">Hello world!</div>
   </td>
   ```
3. In Klaviyo, navigate to ****Content > Templates****.
4. Select the ****Email templates**** tab.
5. Click ****Import****.
6. Enter a name for your template, upload your HTML file and import it.
7. If you open the template from your **Templates** tab, you’ll see your template’s code in Klaviyo’s HTML editor.
   ![The template's html](https://klaviyo.zendesk.com/hc/article_attachments/28720656075931)
8. To access the template in Klaviyo’s drag-and-drop editor, add it to a campaign or flow. In the content step, select the template you imported.
9. Note the text block that says **Hello world!** Drag another block (e.g., a product block) below this block.
10. Delete the text block and add additional custom blocks, as desired.

![Add blocks](https://klaviyo.zendesk.com/hc/article_attachments/28720667866779)

## Sample hybrid email template code

The example below shows a functional HTML file with the hybrid code snippet for a text block. Use this code to test the hybrid editor functionality.

```
  <html>
  <head>
    <meta content="width=device-width, initial-scale=1.0" name="viewport" />
    <title>A simple hybrid email</title>
    <style>
      body {
        background-color: #f6f6f6;
        font-family: sans-serif;
        margin: 20px;
      }
      .main {
        background: #ffffff;
        border-radius: 3px;
        width: 100%;
      }
      .container {
        margin: 0 auto !important;
        width: 600px;
      }
      .wrapper {
        box-sizing: border-box;
        padding: 15px;
      }
      table {
        width: 100%;
      }
    </style>
  </head>
  <body>
    <div class="container">
      <table class="main">
        <tr>
          <td class="wrapper">This is a very simple HTML email</td>
        </tr>
        <tr>
          <td class="wrapper">
            <table>
              <tr>
                <td align="center" data-klaviyo-region="true" data-klaviyo-region-width-pixels="600">
                  <div class="klaviyo-block klaviyo-text-block">
                    Hello world!
                  </div>
                </td>
              </tr>
            </table>
          </td>
        </tr>
        <tr>
          <td class="wrapper">{% unsubscribe %}</td>
        </tr>
      </table>
    </div>
  </body>
</html>
```

## Emojis and hybrid email templates

As of February 2024, all emojis are supported in all Klaviyo email editors (i.e., the drag-and-drop editor, hybrid editor, text-only editor and custom HTML editor).

## Outcome

After completing these steps, you will be able to add and edit certain areas of a custom HTML template. Note that you cannot add or edit drag-and-drop blocks in any area of the custom template, except where the initial block was placed.