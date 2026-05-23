<h1>Getting started with Zendesk</h1>

Learn how to integrate Zendesk with Klaviyo in order to improve your support experience for customers. This integration allows you to:

- Track and target customers based on their interactions with your support team.
- Respond to SMS and WhatsApp messages from within Zendesk.

Tickets, SMS messages, and WhatsApp messages can be synced on a per-brand basis. If you have more than one brand set up under a Zendesk Enterprise account, syncing one Zendesk brand per Klaviyo account makes it easy to use your ticket data and organize your SMS and WhatsApp conversations.

## Before you begin

You can use the Zendesk/Klaviyo integration to sync support ticket information, or to sync both ticket and SMS and WhatsApp message information. You cannot use the SMS or WhatsApp functionality without syncing support ticket information.

### SMS prerequisites

The following applies if you want to respond to SMS and WhatsApp messages from within Zendesk:

- You must have already [set up SMS in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/4404274419355).
- This functionality only works in countries where you have a toll-free number, long code, or short code.
  - Branded sender IDs (also called alphanumeric sender IDs) cannot receive text messages, so you cannot use this integration for subscribers in countries where you're using a branded sender ID. Learn more [about SMS sending numbers](https://help.klaviyo.com/hc/en-us/articles/6637671573403).
- When someone texts any of the following, it does not create a conversation:
  - Subscribe keyword (e.g., JOIN)
  - Compliance keyword (e.g., STOP or JOIN)
  - Trigger keywords for automations (conversational SMS)
- Make sure that you’ve reviewed our [best practices for two-way messaging (known as Klaviyo Inbox)](https://help.klaviyo.com/hc/en-us/articles/360059002271#h_01JMFEZW49YCGTZ5TPZ35ZYMZN), including your auto-responder setup.
- This integration is within the 'Support' agent workspace in Zendesk. It utilizes the Ticket API to create and comment on tickets and does not need the Zendesk ‘Talk’ call center workspace to function.

### WhatsApp prerequisites

You’ll need to [set up WhatsApp in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/40111819732635). This involves connecting your WhatsApp Business account to Klaviyo, getting a phone number, and verifying your account.

## Integrate Zendesk with Klaviyo

Follow the steps outlined below to integrate Zendesk with Klaviyo:

1. Log in to your Klaviyo account.
2. Select the ****Integrations**** tab.
3. Click ****Explore apps****, search for Zendesk, and click the card. Then, click ****Install****.
4. On the next page, enter your Zendesk URL and click ****Connect to Zendesk****.

![](https://klaviyo.zendesk.com/hc/article_attachments/36263452885147)

4. Log in to Zendesk if needed.

5. Review the permissions and approve them. You’ll then be brought back to Klaviyo.

6. Under **Tickets,** choose whether you want to sync Zendesk **Opened** and **Resolved** ticket metrics from all brands, or specific brands.

- If you select **Specific brands**, you’ll be prompted to choose the Zendesk brand(s) you’d like from a dropdown.

![](https://klaviyo.zendesk.com/hc/article_attachments/36263422312987)

7. If you want to reply to inbound SMS messages via Zendesk, check the box next to ****Sync SMS conversations****. If prompted, select the brand to create Zendesk tickets under.

![](https://klaviyo.zendesk.com/hc/article_attachments/36263422320795)

8. If you want to reply to inbound WhatsApp messages via Zendesk, check the box next to ****Sync WhatsApp conversations****. If prompted, select the brand to create Zendesk tickets under.

9. If you're using [Customer Hub](https://help.klaviyo.com/hc/en-us/articles/33660324811675) and AI Agent: You can hand off customer queries the AI Service Agent can't answer to your team in Zendesk. Click ****Manage setting**** to go to the AI Agent settings and elect Zendesk as your [agent handoff.](https://klaviyo.zendesk.com/hc/en-us/articles/37659474656027)

![](https://klaviyo.zendesk.com/hc/article_attachments/39896725334043)

10. When you’re done, click ****Complete setup****.

## Test SMS sending

You can test your integration by sending an SMS to your sending number (if you are already a consented subscriber, and the SMS does not contain a keyword other than HELP or INFO). Within your Zendesk admin, check that a ticket has been created, respond to it, then see if you receive an SMS.

If the profile that sends an SMS has the same email address as the agent replying from Zendesk, the response will not be sent. During the test, make sure the agent and customer (the profile texting in) do not share the same email address.

## Test WhatsApp sending

You can test your integration by sending a WhatsApp message to your WhatsApp business number (if the message does not contain a compliance, subscribe, or automation trigger keyword). Within your Zendesk admin, check that a ticket has been created, respond to it, then see if you receive a WhatsApp message back.

If the profile that sends a WhatsApp message has the same email address as the agent replying from Zendesk, the response will not be sent. During the test, make sure the agent and customer (the profile messaging in) do not share the same email address.

# How the Zendesk SMS integration works

After the SMS integration is set up, Klaviyo automatically creates a ticket in Zendesk whenever both of the following are true:

1. A [consented SMS subscriber](https://help.klaviyo.com/hc/en-us/articles/360035056972) texts a phone number associated with your account.
2. The text message does not contain a keyword (i.e., one of the [subscribe words](https://help.klaviyo.com/hc/en-us/articles/360050384091) listed in your SMS Settings page in Klaviyo). The 2 exceptions to this are HELP and INFO, which will both create a ticket.

SMS messages from [branded sender IDs](https://help.klaviyo.com/hc/en-us/articles/6637671573403#branded-sender-ids2) (also called alphanumeric sender IDs) are not shown, because these numbers cannot receive inbound messages.

The sync functions in the following way:

- Any replies in the ticket from a Zendesk agent will send an SMS message to the customer. Responses from within Zendesk will also appear in Klaviyo.
- If the ticket’s status is **Open**, a new customer message will be added to the ticket as a comment. If the ticket’s status is **Resolved**, a new customer message will reopen the ticket and add the message as a comment. If the ticket’s status is **Closed**, a new customer message will create a new ticket.
- Replies from Zendesk are sent via a phone number associated with your Klaviyo account; this sending number will be the one to which the inbound message was sent.
- Responses from within Zendesk will also appear in Klaviyo, but responses sent within the Klaviyo Inbox tab will not appear in Zendesk. For this reason, we recommend that you only reply to customers from one platform. Campaign and flow SMS messages sent by Klaviyo will also sync to Zendesk.
- Messages from Zendesk count toward your SMS billing plan like any other message.

## When the integration syncs

The SMS integration syncs in real time. As soon as an SMS subscriber texts you, that message will appear in Zendesk. **Opened Ticket** and **Resolved Ticket** metrics also sync in real time.

Note that there is no historic sync. SMS tickets ("conversations") won’t appear in Zendesk if a subscriber texted you before you set up this integration. However, all further messages will sync. If a subscriber texts you once before you enable the integration and once after, the message that comes in after you set up the integration will show in Zendesk.

If a customer sends an image or GIF with a text message, the image will not be displayed in Zendesk (or in Klaviyo). Similarly, you cannot send MMS messages from Zendesk.

# ****How the Zendesk WhatsApp integration works****

After the WhatsApp integration is set up, Klaviyo automatically creates a ticket in Zendesk whenever:

A customer sends an inbound message to your business on WhatsApp.

The message doesn't match compliance, subscribe, or automated conversation keywords. If the message doesn't match those keywords, Klaviyo will prompt the creation of a support ticket in Zendesk.

Your support agent can answer the customer in Zendesk, and the response will send via your WhatsApp business number.

In the Klaviyo channel side panel, you'll be able to see information about the message, including the channel (WhatsApp or SMS) and the consent status.

If the WhatsApp consent status is Expired, and you've enabled the follow-up template setting during setup, your agent can send the template to the customer to re-engage. If the customer responds, the 24-hour window resets and the conversation can continue.

If a customer sends an image or other media with a WhatsApp message, the image will not be displayed in Zendesk. Similarly, you cannot send images or other media messages from Zendesk via WhatsApp.

Responses from within Zendesk will also appear in Klaviyo, but responses sent within the Klaviyo Inbox tab will not appear in Zendesk. For this reason, we recommend that you only reply to customers from one platform. Campaign and flow WhatsApp messages sent by Klaviyo will also sync to Zendesk.

Messages from Zendesk count toward your WhatsApp billing plan like any other message.

## ****When the integration syncs****

The SMS and WhatsApp integrations sync in real time. As soon as an SMS subscriber texts you or a customer sends you a WhatsApp message, that message will appear in Zendesk. Opened Ticket and Resolved Ticket metrics also sync in real time.

Note that there is no historic sync. SMS and WhatsApp tickets ("conversations") won't appear in Zendesk if a subscriber messaged you before you set up this integration. However, all further messages will sync. If a subscriber messages you once before you enable the integration and once after, the message that comes in after you set up the integration will show in Zendesk.

If a customer sends an image or GIF with a text message or WhatsApp message, the image will not be displayed in Zendesk (or in Klaviyo). Similarly, you cannot send MMS messages or WhatsApp media messages from Zendesk.

## Metrics synced between Klaviyo and Zendesk

Klaviyo tracks 2 Zendesk metrics: **Opened Ticket** and **Resolved Ticket**. The metrics appear on an individual’s profile page and can be used in segments and flows. They sync in real time.

### Opened Ticket

This event is tracked when a new ticket is opened in Zendesk, and includes the following information about the new ticket:

- ****Assignee\_email****
  Email of the support agent assigned to the ticket in Zendesk
- ****Assignee\_name****
  Name of the support agent assigned to the ticket in Zendesk
- ****Channel****
  Information about the channel that the ticket came through, (e.g. email, web portal, SMS), populated when available
- ****Description****The body of the first message in the ticket
- ****Fields****Any custom fields from Zendesk
- ****Group\_name****Group field from Zendesk
- ****Priority****Priority field from Zendesk
- ****Subject****
  Subject of the ticket from Zendesk
- ****Tags****
  Tags associated with the ticket in Zendesk
- ****Ticket\_id****
  Ticket ID from Zendesk
- ****Type****
  Type field from Zendesk
- ****Via****
  Information about the source of the ticket, populated when available
- ****Zendesk\_url****URL of the ticket in Zendesk
- ****Status****Status of the ticket in Zendesk

### Resolved Ticket

This event is tracked when a ticket is marked as **Closed** in Zendesk. When a ticket is marked **Solved** in Zendesk, no event is sent to Klaviyo. Klaviyo's tracking of this event includes the following information about the resolved ticket email:

- ****Assignee\_email****
  Email of the support agent assigned to the ticket in Zendesk
- ****Assignee\_name****Name of the support agent assigned to the ticket in Zendesk
- ****Channel****Information about the channel that the ticket came through, (e.g. email, web portal, SMS), populated when available
- ****Description****The body of the first message in the ticket
- ****Fields****Any custom fields from Zendesk
- ****Group\_name****Group field from Zendesk
- ****Priority****Priority field from Zendesk
- ****Subject****Subject of the ticket from Zendesk
- ****Tags****
  Tags associated with the ticket in Zendesk
- ****Ticket\_id****Ticket ID from Zendesk
- ****Type****Type field from Zendesk
- ****Via****Information about the source of the ticket, populated when available
- ****Zendesk\_url****URL of the ticket in Zendesk
- ****Status****Status of the ticket in Zendesk

## Optional: Create an automation in Zendesk to mark SMS and WhatsApp tickets as "Closed" sooner

As stated above, a Resolved Ticket metric is sent to Klaviyo once the ticket is marked Closed in Zendesk (not when it is marked Solved). Tickets are marked as Closed in Zendesk via rules set at the account level.

If you use Zendesk with both messaging (SMS or WhatsApp) and email, you may want to mark messaging tickets as Closed sooner than email tickets, depending on your support response times and your time-to-resolution. This can be achieved via a Zendesk automation.

For example, you could create the following automation to mark SMS tickets as Closed after 24 hours:

1. Log in to Zendesk and navigate to your Admin Center.
2. Select ****Objects and rules****.
3. Select ****Business rules > Automations****.
4. Select ****Add Automation****.
5. Title your automation.
6. Under **Meet all of the following conditions**, select:

   - Ticket: Status / is / Solved
   - Ticket: Hours since solved / is / 24
   - Ticket: Tags / Contains at least one of the following / "sms"![](https://klaviyo.zendesk.com/hc/article_attachments/36263452896795)
7. Under **Perform these actions**, select:

   - Ticket: Status / Closed
8. Click ****Create automation****.

You've now created an automation to close SMS tickets after 24 hours.

## Optional: Create a view in Zendesk for Klaviyo SMS and WhatsApp

We recommend creating a view in Zendesk in order to organize your Klaviyo SMS and WhatsApp tickets.

This view will filter on the tag ‘SMS’ and 'WhatsApp'. Note that if you have tickets other than Klaviyo SMS/WhatsApp with this tag, they will also be included in the view.

1. From your Zendesk Admin Center, click the ****Workspaces**** dropdown.
2. Select ****Views**** under **Agent tools**.
3. Click ****Add view****.
4. Name your view, add a description, and select who has access.
5. Under **Tickets must meet all of these conditions to appear in the view**, add:
   Status > Is not > Closed
6. Under **Tickets must meet all of these conditions to appear in the view**, add:
   Tags > Contains at least one of the following > SMS
7. Edit any formatting settings to your specifications.
8. Click ****Save****.

You’ve now created a view to organize your Klaviyo SMS/WhatsApp tickets.

## Use cases for Zendesk metrics

Here are a few ways you might consider leveraging metrics synced from your Zendesk integration:

- Exclude users with open tickets from certain flows and campaigns, so your company doesn't risk seeming out of touch by sending promotional emails to those with pending issues.
- Proactively track customers in Klaviyo based on their interactions with your support team using your Zendesk data; for example, you can customize an abandoned cart email if you know someone didn't complete their order, but did open a support ticket.
- View trends around open and resolved tickets, including a cohort analysis, by using the detailed analytics reporting Klaviyo provides about the Zendesk metrics you've synced.
- Tweak your email strategy to reduce support tickets and increase lifetime value; with all your data in Klaviyo, you can build segments to view correlations and gain cross-metric insights.
