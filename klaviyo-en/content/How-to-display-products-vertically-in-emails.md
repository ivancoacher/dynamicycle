---
id: 19462923466651
title: "How to display products vertically in emails"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/19462923466651-How-to-display-products-vertically-in-emails"
section: "Advanced template design"
category: "Content"
category_slug: "content"
klaviyo_updated: "2026-04-21T13:54:32Z"
language: en
---

## You will learn

Learn how to display products in your abandoned cart and order confirmation flows vertically (i.e., with an image above product information, rather than beside).

## Create a vertical product block

The instructions below will help you convert an existing horizontal product block into a vertical product block. If you don’t yet have a flow email containing a dynamic content block, [find one in the flow library](https://help.klaviyo.com/hc/en-us/articles/115002779411).

1. Select ****Flows**** in the Klaviyo sidebar.
2. Navigate to your abandoned cart or order confirmation flow.
3. Click ****Update Action Statuses**** in the top right to set the flow to ****Manual**** while you edit.
4. Open an email in the flow containing your dynamic content block (i.e., the table block that displays the products from someone’s cart).
5. Add a new section immediately below the dynamic table block.
   ![Section block](https://klaviyo.zendesk.com/hc/article_attachments/28720660124699)
6. Add an image block and a table block to your new section.
7. Copy the values from ****Table settings > Row collection**** and ****Table settings > Row alias****.
8. Navigate to ****Display options**** and click ****Create Repeat Rules****.
   ![Create repeat rules](https://klaviyo.zendesk.com/hc/article_attachments/28720671860123)
9. Paste the values from your table block into the **Repeat For** and **Item alias** fields, respectively.
   ![old and new repeat for](https://klaviyo.zendesk.com/hc/article_attachments/28720671874203)
10. In your table block, click ****Replace**** under **Dynamic Image**.
    ![replace dynamic image button](https://klaviyo.zendesk.com/hc/article_attachments/28720671868699)
11. In the modal that appears, copy everything in the **Dynamic variable or dynamic URL** field.
    ![Dynamic image field](https://klaviyo.zendesk.com/hc/article_attachments/28720660071067)
12. Click the image block in your new section.
13. Click ****Browse Image Library****.
14. Select ****Dynamic Image**** and paste in the dynamic URL.
15. Click ****Save****.
16. Copy the tag that appears in the **Link address** field of your table block.
    ![Image link address](https://klaviyo.zendesk.com/hc/article_attachments/28720660051867)
17. Paste this tag into the **Link address** field of your new image block.
18. Copy the text content from your original table block.
    ![text content](https://klaviyo.zendesk.com/hc/article_attachments/28720660130459)
19. Paste the text into your new text block.
20. Preview your email to ensure all product information appears in the new section. If something appears incorrect, check that all elements (i.e., row collection, row alias, dynamic image URL, and text content) transferred correctly.
21. Once you’re happy with the new section, delete the original table block.
22. Optionally, save the new section as [universal content](https://help.klaviyo.com/hc/en-us/articles/115005413888) for use in other messages within the flow.

## Outcome

After following these steps, your email will contain a vertical product block (with images above the product information), rather than product images and information displayed horizontally.

![vertical product block](https://klaviyo.zendesk.com/hc/article_attachments/28720671837979)

## Additional resources

- [Dark mode email design best practices](https://klaviyo.zendesk.com/hc/en-us/articles/360049181631)
- [How to update your brand styles in Klaviyo](https://klaviyo.zendesk.com/hc/en-us/articles/4403537778331)