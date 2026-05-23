---
id: 115005252888
title: "How to integrate with Eventbrite"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005252888-How-to-integrate-with-Eventbrite"
section: "Eventbrite"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:23Z"
language: en
---

## You will learn

Learn how to integrate Eventbrite with Klaviyo. After completing these steps, you'll be able to personalize and target emails based on ticket purchase activity.

Klaviyo will sync a **Bought Ticket** event for each purchase made, and will automatically sync all details related to the purchase as well as the individual that placed the order.

## Enable the Eventbrite integration

The Eventbrite integration uses webhooks which will create a real-time exchange of data between Eventbrite and your Klaviyo account. First, you'll connect Eventbrite with Klaviyo. Then you'll designate an Organization so the appropriate webhooks can be created for your integration.

1. In Klaviyo, select the ****Integrations**** tab.
2. Click ****Explore apps****, search for **Eventbrite**, and click the card. Then, click ****Install****.
3. Click the ****Connect to Eventbrite****. You'll be redirected to an Eventbrite login page, where you will need to login to your Eventbrite account if you aren't already logged in.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28711676294299)
4. You'll be prompted to allow Klaviyo to access your Eventbrite account. Select ****Allow****here.
   ![Screen asking Allow Klaviyo by Klaviyo to access your Eventbrite account? with Allow with orange background and deny with white background](https://klaviyo.zendesk.com/hc/article_attachments/28711676282139)
5. Then, you'll be taken back to Klaviyo to finish integrating. Confirm that your username is correct, and select your organization(s) to sync with Klaviyo.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28711676298779)
6. Click ****Complete setup****. You should then receive a success message.

## Monitor your Eventbrite sync

After enabling Klaviyo's built-in Eventbrite integration, 2 things will happen:

- Klaviyo will run a one-time historical sync to pull all past Eventbrite **Bought Ticket** metrics into your Klaviyo account.
- Klaviyo will also begin to sync new Eventbrite metrics in real-time, through Eventbrite webhooks.

You should see historic Eventbrite **Bought Ticket** data populate your account, as well as begin to see new order events track live data.

To check on your Eventbrite integration:

1. Click the ****Analytics**** dropdown in Klaviyo and select the ****Metrics**** tab.
2. Click on one of the Eventbrite metrics displayed to verify that there is data populated as expected. For example, click on the ****Bought Ticket**** metric.
3. If you see purchase activity, all you need to do is wait until your initial historic Eventbrite integration sync has completed; this process can several hours depending on how much historical data you have in your account. You can watch new order events flow in by monitoring your Dashboard Activity Feed.
   ![Eventbrite Bought Ticket activity feed in Klaviyo with name of buyer censored](https://klaviyo.zendesk.com/hc/article_attachments/28711676285979)

## Events synced from Eventbrite

These are the event metrics synced from your Eventbrite integration:

- ****Bought Ticket****When someone buys a ticket for an event in Eventbrite.
- ****Checked In****When someone checks in to the event, usually while it is happening.
- ****Checked Out****When someone checks out of an event.
- ****Refunded Ticket****When an event is canceled and the ticket is refunded to the customer.
- ****Updated Ticket****When a ticket which has already been purchased is updated. For example, quantity or information on the ticket might be updated on a customer's ticket.

## The Bought Ticket metric

Klaviyo will sync a **Bought Ticket** event for each purchase made, and will automatically sync all details related to the purchase as well as the individual that placed the order:

### Customer Data

Klaviyo will sync the following for each ticket purchaser:

- First Name
- Last Name
- Email Address

### Order Data

Klaviyo will sync the following along with each order, if available:

- Total Value
- Event Name
- Event Description
- Ticket Type
- Ticket Description
- Ticket ID
- Attendee Quantity
- Attendee ID

![Single Bought Ticket metric in Klaviyo activity feed showing event details such as name, value, etc.](https://klaviyo.zendesk.com/hc/article_attachments/28711697751963)

## Update to our new Eventbrite integration

Having issues with your Eventbrite integration? You may be using our old integration which has been deprecated. Klaviyo has released a new Eventbrite integration to improve security and stability.

To update to the new integration, you need to re-authenticate Klaviyo with Eventbrite:

1. In Klaviyo, click the ****Integrations**** tab.
2. Select ****Eventbrite**** from the list of enabled integrations.
3. In the upper right corner, click ****Manage integration****.
4. Select ****Re-authenticate****.
5. Click ****Accept**** on the Eventbrite permissions page.

Your integration has now been updated.

## Outcome

You have now integrated with Eventbrite and reviewed your synced data.

## Additional resources

- [Integration FAQ reference](https://help.klaviyo.com/hc/en-us/articles/115005081007)