<h1>Klaviyo Helpdesk:  Shopify Order Editing</h1>

## You will learn

In this article, you’ll learn how to remove items, adjust quantities, change addresses, or cancel a Shopify order — all without leaving Helpdesk. Completing edits in-place shortens average resolution time, reduces manual mistakes, and helps you provide a better customer experience.

## Before you begin, confirm:

- You have integrated Shopify with Klaviyo.
- You can see the ****Orders section**** inside conversations.
- Orders must be ****Open**** and not fully fulfilled. Locked orders cannot be edited.

## Overview

The ****Edit order**** modal lets you perform the most common mid-fulfillment fixes — change quantities, edit shipping addresses, or cancel an order. Because the modal writes directly to Shopify via the REST Admin API, edits are real-time. Use it whenever you need to correct an order while helping your customers.

![Screenshot 2025-10-23 at 6.29.03 PM.png](https://klaviyo.zendesk.com/hc/article_attachments/42876399554587)

## Set it up

1. In Helpdesk, open the conversation that contains the Shopify order you need to change.
2. In the ****Order card****, select ****Edit order****.

   - ****Expected outcome:**** The ****Edit order**** modal opens and fetches the latest order data from Shopify.
3. On the ****Items**** tab:
   1. To change quantity, use the ****+ / –**** controls next to the item.
   2. To remove an item, click the trashcan icon.
4. In the ****Address section,**** click the pencil icon to edit the address for orders which have not shipped yet.
   ![Screenshot 2025-10-23 at 6.28.49 PM.png](https://klaviyo.zendesk.com/hc/article_attachments/42876399555611)
5. Review changes, then select ****Edit Order**** to save your changes.****Success criteria:**** You see a green “Order updated” toast.

****Note****: If the ****Edit order**** button is greyed-out, hover to see why (order locked or permission denied).

## Best practices

- Keep the customer informed — send a quick confirmation message right after saving.
- Use the ****Undo**** option for quick reversals instead of editing twice.

## FAQ

****Can I issue a partial refund from the modal?****
Not yet. Refunds must be processed in Shopify.
