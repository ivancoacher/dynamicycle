---
id: "115005081607"
title: "How to integrate with Help Scout"
source_url: "https://help.klaviyo.com/hc/en-us/articles/115005081607-How-to-integrate-with-Help-Scout"
section: "Help Scout"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:19Z"
language: "en"
---
## You will learn

Learn how to integrate Help Scout with Klaviyo to sync import metrics about your Help Scout conversations into your Klaviyo account, which can help with targeted messaging. Klaviyo's built-in Help Scout integration fully supports Help Scout's Mailbox API 2.0. The Help Scout integration syncs with Klaviyo every hour.

## Enable the Help Scout integration

1. Log in to Klaviyo and select the ****Integrations**** tab.
2. Select ****Explore apps****, search for **Help Scout**, then select the card.
3. Then, click ****Install****.
4. Click ****Connect to Help Scout****. You may then be prompted to log into your Help Scout account to complete the connection.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28723505995291)
5. Once you're connected, you'll receive a success message.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28723505992091)

## How to view data synced from Help Scout

To view the Help Scout metrics are syncing into your Klaviyo account, click the ****Analytics**** dropdown in Klaviyo, then select the ****Metrics**** tab. Select **Help Scout** from the dropdown to view all the associated events.

![](https://klaviyo.zendesk.com/hc/article_attachments/36559164400155)

You can click on any metric to view event details. Delve deeper into the data by selecting any of the following:

- ****Charts****Shows you the data in graph form
- ****Activity Feed****Shows you a timeline of events, and allows you to drill into the metadata by clicking on any timestamp
- ****Cohorts****
- ****Best People****

All data can be exported by clicking ****Export to CSV****.

## Help Scout metrics

The following metrics are synced from Help Scout into your Klaviyo account:

- Closed Conversation
- Received Reply
- Sent Message
- Started Conversation

### Closed Conversation

Tracked when a conversation with a customer is closed. The event Klaviyo tracks will include the subject of the email, which mailbox the email was delivered to, and which tags are present on the conversation in Help Scout. You can filter and target **Closed Conversation** events based on the following:

- ****Mailbox****The name of the mailbox in Help Scout of this conversation
- ****Tags****The Help Scout tags listed on each conversation

### Received Reply

Tracked when a customer receives a reply to a Help Scout ticket from your mailbox. The **Received Reply** event includes the subject and body of the email. You can trigger flows and segments based on whether or not someone has received a reply, or when they last received a reply.

### Sent Message

Tracked any time a customer sends an email to your Help Scout mailbox. The **Sent Message** event includes the subject and body of the email. You can trigger flows and segments based on whether or not someone has sent a message, how many messages they have sent, or when they last sent a message.

### Started Conversation

Tracked when a customer starts a new conversation. The event Klaviyo tracks will include the subject of the email, which mailbox the email was delivered to, and which tags are present on the conversation in Help Scout. You can filter and target **Started Conversation** events based on the following:

- ****Mailbox****The name of the mailbox in Help Scout of this conversation
- ****Tags****The Help Scout tags listed on each conversation

## Monitor the Help Scout sync

There are a few places you can check to ensure that your Help Scout + Klaviyo integration is enabled.

1. Navigate to your [Integrations tab](https://www.klaviyo.com/integrations) and look for your Help Scout integration. You'll know your integration is fully synced when you see a green border around your Help Scout integration.
2. Click the ****Analytics**** dropdown in Klaviyo and select ****Metrics****. Find Help Scout's **Sent Message** metric and click on the ****Activity Feed**** icon.
   ![Klaviyo activity feed for Sent Message metric with list of timestamps and identifying information blurred](https://klaviyo.zendesk.com/hc/article_attachments/28723505989403)
   If your data integration sync has started, you will see messages in your activity feed. These are the messages sent through your Help Scout mailboxes.

## Additional resources

- [How often integrations sync](https://help.klaviyo.com/hc/en-us/articles/115005253208)
- [Types of Information Exchanged Between Klaviyo and Apps](https://help.klaviyo.com/hc/en-us/articles/360030696012)