---
id: 4995667413531
title: "How to create and use macros for Helpdesk tickets"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/4995667413531-How-to-create-and-use-macros-for-Helpdesk-tickets"
section: "Team Workflow & Productivity"
category: "Helpdesk"
category_slug: "helpdesk"
klaviyo_updated: "2026-04-17T07:01:36Z"
language: en
---

Only Owners, Admins, Managers, or Support roles can access this feature.

## You will learn

Find out how to create and use macros (previously called “quick responses”) in tickets in Klaviyo Helpdesk. Macros are pre-written, reusable responses your support agents can insert into replies for SMS and web chat tickets.

## Before you begin

There are a few important things to remember before using macros:

1. Before you can add a macros, you need at least 1 active message in Klaviyo Helpdesk, either:

   - 1 web chat
   - 1 SMS from a subscriber
   - 1 Email message
   - 1 WhatsApp Message
   - 1 Instagram DM
2. Macros used in SMS tickets are billed the same as any other SMS message in your [billing plan](https://help.klaviyo.com/hc/en-us/articles/115000976672).

New to using tickets in the Klaviyo Helpdesk? Check out our [guide to the Klaviyo Helpdesk](https://help.klaviyo.com/hc/en-us/articles/360059002271) for more information.

## About macros

Macros are designed to save your support team time by eliminating the need to repeatedly type responses to common inquiries. They’re helpful when customers frequently ask similar questions, and for standardizing consistent messaging and tone.

You can create different macros for different types of support requests (e.g., shipping time, returns policy, or order status), and organize them by category. This makes it easy for your support team to quickly find and insert the right response for each customer ticket.

![Macro1.jpg](https://klaviyo.zendesk.com/hc/article_attachments/37189986358939)

### Personalization supported in macros

Additionally, the macros you create can include profile and order personalization variables, which act as placeholders that automatically insert customer data each time the macro is used. Personalization variables streamline the support workflow, so agents don’t need to search for or manually enter customer information in every reply.

Note that Klaviyo can only auto-populate customer data for the profile and order variables shown in the dropdown menus in the macro creation modal. These available options are listed and defined at the bottom of this guide in the [Personalization available for macros](http://help.klaviyo.com/hc/en-us/articles/4995667413531#h_01JVQ9YWSVHQGRAWM1SNKJ2ZTG) section.

****Example macros****

Title: Where’s my order?

Message: Hi {{first\_name}}! Thanks for reaching out. Let me check on the status of your {{order\_name}}.

Title: Order arrival

Message: Hi {{first\_name}}! So happy you purchased {{order\_id}}. Your order is arriving to {{shipping\_address}} and is estimated to arrive on estimated\_delivery\_at.

## Create a new macro

To add a macro:

1. Navigate to ****Service > Helpdesk****.
2. Click ****Settings**** along the left.
3. Select the ****Macros**** tab in the top menu bar.
4. Click ****Create macro****.
5. Click ****Add macro**** to open the creation modal.
   ![Inboxmacro1.jpg](https://klaviyo.zendesk.com/hc/article_attachments/39022621552155)
6. Under **Title**, enter a name that reflects the macro’s purpose (e.g., Refund request)
7. In the **Message** body text box, input your message content. To further customize your response, you can:

   - Click the smile icon to add emojis.
   - Select the person icon to insert profile personalization (e.g., first name).
   - Click the package icon to insert order personalization (e.g., Order ID).
8. Open the ****Category**** dropdown menu to select an existing tag or create a new one. Tags are used to group similar macros by topic, like putting all shipping-related responses together, to help your support team quickly find the right macro.
9. Under **Status**, choose either ****Active**** or ****Draft****.

   - **Active** means they can be inserted into messages from the quick insert menu in a ticket.
   - **Inactive** means they cannot be inserted into a ticket and are hidden from the quick insert menu. Inactive macros can only be accessed from the [Macros settings page](https://www.klaviyo.com/inbox/settings/quick-responses).![Macro4.jpg](https://klaviyo.zendesk.com/hc/article_attachments/37190015068059)
10. Click ****Add**** to save the macro.

All macros you create are stored on the [Macros settings page](https://www.klaviyo.com/inbox/settings/quick-responses). Note that macros with order and profile personalization appear as personalization tags on this page. However, when used in a ticket reply, these tags will be replaced with the relevant customer data.

## Insert a macro into a ticket

To use a macro in a ticket:

1. In Helpdesk, click into a ticket.
2. Click the lightning bolt icon below the reply field to open the macro quick insert menu.
   ![Macro5.jpg](https://klaviyo.zendesk.com/hc/article_attachments/37190015068571)
3. Select the macro you want to use.
   ![Macro6.jpg](https://klaviyo.zendesk.com/hc/article_attachments/37189986369819)
4. A preview modal appears when you select a macro, displaying any personalized content. If customer data for a personalization tag is unavailable, it will show as "No\_[personalization tag]".
5. Insert the macro into the reply box by pressing ****Enter**** or the forward arrow key. Be aware that macros lacking customer data for personalization will insert a blank space.
   ![Macro7.jpg](https://klaviyo.zendesk.com/hc/article_attachments/37189986370971)
6. Edit the response as needed in the reply field.
7. Click the send button.

## Personalization (dynamic content) available for macros

### Supported profile personalization

Profile personalization auto-populates properties from a user’s Klaviyo profile. The following profile personalization is supported in macros:

|  |  |
| --- | --- |
| Profile personalization | Description |
| first\_name | The person’s first name. |
| last\_name | The person’s last name. |
| email | The person’s email address. |
| phone\_number | The person’s phone number. |
| address | The person’s home address. |

### Supported order personalization

Order personalization in macros automatically fills in customer order details from Shopify. The following order data is supported in macros:

|  |  |
| --- | --- |
| Order personalization | Description |
| order\_id | The unique numeric identifier for the order. |
| order\_name | The human-readable name or number assigned to the order (e.g., "#1001"). |
| customer\_email | The email address of the customer who placed the order. |
| customer\_first\_name | The first name of the customer associated with the order. |
| customer\_display\_name | The display or full name of the customer (may include first and last name). |
| shipping\_address | The address where products in the order will be shipped. |
| payment\_info\_billing\_name | The name associated with the billing information used for payment. |
| price\_breakdown\_currency | The currency code (e.g., USD, EUR) used for the order. |
| price\_breakdown\_shipping | The total shipping cost for the order. |
| price\_breakdown\_total | The total price of the order, including all charges. |
| price\_breakdown\_tax | The total tax amount applied to the order. |
| price\_breakdown\_discount | The total discount applied to the order. |
| price\_breakdown\_subtotal | The subtotal price of the order before discounts, shipping, and taxes. |
| price\_breakdown\_totals\_before\_tax | The total amount of the order before taxes are applied. |
| updated\_at | The date and time the order was last updated. |
| status | The current fulfillment or payment status of the order. |
| estimated\_delivery\_at | The estimated date and time for delivery of the order. |
| latest\_fulfillment\_display\_status | The status of the most recent fulfillment event for the order. |

|  |  |
| --- | --- |
| latest\_fulfillment\_tracking\_url | The tracking URL for the latest fulfillment, if available. |
| latest\_fulfillment\_estimated\_delivery\_at | The estimated delivery date of the latest fulfillment. |
| is\_refunded | Indicates if the order has been fully refunded. |
| created\_at | The date and time when the order was created. |
| canceled\_at | The date and time the order was canceled, if applicable. |