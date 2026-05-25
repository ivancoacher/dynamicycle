---
id: "13325405718939"
title: "How to create a back in stock flow for Shopware"
source_url: "https://help.klaviyo.com/hc/en-us/articles/13325405718939-How-to-create-a-back-in-stock-flow-for-Shopware"
section: "Shopware"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:28Z"
language: "en"
---
## You will learn

Learn how to create a back in stock flow for Shopware 6 to alert customers about inventory. This flow will use the **Subscribed to Back in Stock** event synced from your Shopware store.

## Before you begin

Make sure to do the following:

- Integrate with Shopware 6 (see [Getting started with Shopware](https://help.klaviyo.com/hc/en-us/articles/13001662470939) to learn how). As part of the integration process, make sure you:

- Have **Track Back in Stock** toggled on in your extension settings, which will sync **Subscribed to Back in Stock** events to Klaviyo.
  ![Track Back in Stock setting toggled on to blue](https://klaviyo.zendesk.com/hc/article_attachments/28715965319451)
- Sync your Shopware 6 product catalog to Klaviyo.

## Customize your Back in Stock button and form in Shopware

The Back in Stock form appears on product detail pages only when the product is out of stock and marked for Clearance sale.

If you’re tracking back in stock (via your extension settings in Shopware), you’ll also be able to customize the “Notify me when back in stock” button (which appears for items that are out of stock) and form on your site. Customers must click the button and fill out the form to receive back in stock notifications.

To customize these elements:

1. Log in to your Shopware admin.
2. Navigate to ****Settings > Extensions > Klaviyo****.
3. Scroll down to **Back-In-Stock Pop-up styles**, where you can customize the text color and background of the Back in Stock pop-up opening button, pop-up close button, and subscribe button.
   ![Pop-up opening button settings with color set to white and background set to dark blue](https://klaviyo.zendesk.com/hc/article_attachments/28715965322267)
4. Click the square, then use the selector to choose a color, or, if you have the hex color codes for your brand’s colors, paste it in the corresponding box.
5. Under **Snippet names**, you’ll find a reference for how to refer to different back in stock components in HTML, if you wish to customize them within your site code.
   ![Snippet names for open button, close button, and email field label](https://klaviyo.zendesk.com/hc/article_attachments/28715971891739)
6. When you are finished, click ****Save****.

## Configure your back in stock settings in Klaviyo

Next, [configure your back in stock settings in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115003872251-How-to-build-a-back-in-stock-flow#back-in-stock-flow-settings2): both minimum inventory rules and customer notification rules.

- Minimum inventory rules refer to how many items need to be restocked before you notify subscribers.
- Customer notification rules allow you to choose how many customers to notify and how long to wait between notifications.

## Create the flow

1. In Klaviyo, select the ****Flows**** tab.
2. Click ****Create Flow****, then ****Create from Scratch****.
3. Name your flow, then click ****Create Flow****.
4. In the flow builder, choose the trigger option ****Metric****, then select the Klaviyo metric****Subscribed to Back in Stock****. Do not add any trigger or flow filters, and click ****Save****.
5. Directly after the trigger, drag in a Back in Stock Delay. Recipients who enter your flow will wait at this delay until their item of interest is restocked. After this occurs, they will move on to the next step in your flow, which in this case is an email message that you add after the delay.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28715965332123)
6. Design your back in stock email with dynamic variables to pull product information for this notification. [Learn how to personalize flows with dynamic event data](https://help.klaviyo.com/hc/en-us/articles/115002779071-Personalize-Flow-Emails-with-Dynamic-Event-Data).
7. Typically, you will only need a single message in this flow as a notification that the item is back. [Turn Smart Sending off](https://help.klaviyo.com/hc/en-us/articles/115002779311-Smart-Sending-for-Flows#how-to-disable-smart-sending) for this message to ensure everyone gets the alert.
8. You do not need to add any additional time delays to this series, as the back in stock delay will ensure each person that enters your flow waits until the item they subscribed to goes back in stock before moving forward.
9. To learn about flow statuses and how to set your flow live, read [Getting started with flows](https://help.klaviyo.com/hc/en-us/articles/115002774932-Getting-started-with-flows). For more guidance on back in stock flows, read [How to build a back in stock flow](https://help.klaviyo.com/hc/en-us/articles/115003872251).

## Outcome

You’ve created a back in stock flow for Shopware 6. Now, you can better personalize your customer communications and drive revenue.

## Additional resources

- [Understanding how back in stock flows work](https://help.klaviyo.com/hc/en-us/articles/360051612551-Understanding-how-back-in-stock-flows-work)
- [Shopware data reference](https://help.klaviyo.com/hc/en-us/articles/13006716790299)
- [How to personalize flows with dynamic event data](https://help.klaviyo.com/hc/en-us/articles/115002779071-Personalize-Flow-Emails-with-Dynamic-Event-Data)