<h1>Guide to Klaviyo Helpdesk</h1>

Only Owners, Admins, Managers, or Support roles can access this feature.

Learn about Klaviyo Helpdesk, which helps you manage support conversations across all channels, powered by the data you already have in Klaviyo.

## What is Klaviyo Helpdesk?

Klaviyo Helpdesk brings your support messages into 1 place. When customers reach out via one of your support channels, their message creates a “ticket,” which someone on your team can view and reply to directly from within Klaviyo.

### Who should use Helpdesk?

Use Helpdesk if:

- You have a dedicated person or team managing support inquiries.
- You want to manage support conversations from multiple channels in one place.
- You use Klaviyo and want to connect support messages to customer data (e.g., Klaviyo profiles, events, and ecommerce activity).

### Do I have to pay for Helpdesk to respond to my customers in Klaviyo?

No! If you complete your free trial and choose not to purchase, Klaviyo will downgrade your account to our free helpdesk, Inbox.

Inbox has more limited features, including:

- Macros
- Multi-Agent Support
- Full Channel support (email, text, WhatsApp, Social)
- Auto Responders
- Profile details in conversation view
- Spam Filtering

### Key terms

- ****Inbox****
  - Where customer tickets are displayed and organized by channel.
- ****Ticket****
  - A container for the 1-1 conversation between your team and a customer.
- ****Message thread****
  - The sequence of messages exchanged within a single ticket, including both customer and agent replies.
- ****Inbound message****
  - A message from a customer to your brand (e.g., an SMS subscriber texts “HELP” or a site visitor sends you a web chat message).
- ****Outbound message****
  - A message sent from your brand (e.g., ticket replies, flows, campaigns).

## Supported channels for Inbox

Inbox supports tickets from the following channels:

- Web chat
  - When you have [web chat enabled](https://help.klaviyo.com/hc/en-us/articles/33660391549211), messages sent from your customers via the chat tab of the Customer Hub interface route to Helpdesk as a new ticket.
- Email
  - When you set up email forwarding from your dedicated support email address (e.g., support@mycompany.com), incoming emails are converted into Helpdesk tickets.
- SMS
  - If you use Klaviyo SMS, any message sent to your number that doesn’t include a keyword appears as an Helpdesk ticket.
- Instagram
  - When you have [Instagram enabled](https://help.klaviyo.com/hc/en-us/articles/41741460845339), direct messages sent to your Instagram profile will create Helpdesk tickets.
- WhatsApp
  - If you use WhatsApp in Klaviyo Marketing, any message sent to your number that doesn't include a keyword appears as a Helpdesk ticket

## Ticket behavior by channel

How ticket reopening works by channel:

- Web chat:
  - Each conversation creates a new ticket, even for the same person.
  - Closed tickets do not reopen.
- Email:
  - Each email thread generates a new ticket.
  - If a customer replies to a closed ticket's email thread, the ticket will be reactivated regardless of how much time has passed.
- SMS:
  - Each individual gets 1 ticket when they message you.
  - Subsequent messages from the same person will reopen their existing ticket.
- Instagram:
  - When someone messages you on Instagram or replies to your story, Inbox will create a new ticket.
  - Subsequent messages from the same person or company will be added to the ticket unless it is closed. If there are no open tickets, a new ticket will be created.
- WhatsApp:
  - Each individual gets 1 ticket when they message you.
  - Subsequent messages from the same person will reopen their existing ticket.

    You can reply to any customer via web chat or email when they open a ticket. However, for SMS tickets, they must be an SMS marketing subscriber for you to reply. You can use the SMS auto-responder to notify non-subscribers that they need to opt in before receiving replies.

    When replying, you cannot:
- Open a ticket with a customer; they must message you first.
- Use Helpdesk with a branded sender ID (also called alphanumeric sender ID), as this type of number cannot receive inbound text messages.
- Reply to a non-consented profile.

## Navigating through Helpdesk

Access Inbox via ****Service > Helpdesk**** within Klaviyo.

Note that Klaviyo Helpdesk shows unread tickets with a badge and count on the **Helpdesk** navigation tab, representing unread tickets. You can disable this notification in Inbox [general settings under](https://www.klaviyo.com/inbox/settings/general) [**Unread conversation notification**](https://www.klaviyo.com/inbox/settings/general).

You can view tickets across 3 main views:

- ****My Inbox****
  - Open tickets assigned to you.
- ****All tickets****
  - All tickets in your Inbox, regardless of their status. You can sort tickets using various filters or perform bulk actions from this view.
- ****Unassigned****
  - New tickets not yet assigned.
- ****Spam****
  - Klaviyo will automatically scan incoming messages for spam, and place them in the spam view if they are not legitimate customer outreach messages. You can go in and mark as not spam as well.

You can also [create a custom ticket view](https://help.klaviyo.com/hc/en-us/articles/39691102278043) based on your own filters.

![Inboxviews.jpg](https://klaviyo.zendesk.com/hc/article_attachments/39926012908571)

### Ticket statuses

Within any view, you can filter by ticket status. A ticket can have 1 of 3 statuses:

- ****Open****
  - Conversation is active or awaiting action.
- ****Snoozed****
  - Temporarily hidden; you can choose when to be alerted again.
- ****Closed****
  - Conversation is complete and archived from the **My Inbox** and **Unassigned** views.

[Learn how to change the status of a chat](https://klaviyo.zendesk.com/hc/en-us/articles/4405329314331).

## Working with tickets

When viewing a ticket, you can:

- View the last 50 messages with the customer
- Use the **Overview** panel to see the following sections with information about the ticket and profile:
  - **Ticket**
    - ID number
    - Assignee
    - Date and time of ticket creation
    - Channel (email, SMS, or web chat)
    - Tags
  - **Predictive analytics** (available if your Klaviyo account meets the [qualifying criteria](https://help.klaviyo.com/hc/en-us/articles/360020919731))
    - Customer lifetime value
    - Number of orders
    - Churn risk
    - Predicted next order date
    - Number of tickets associated with the profile
  - **Activity**
    - Recent orders (Shopify only)
      - Clicking on ****# of orders**** brings you to a list view of the visitor’s recent purchases.

        Agents can edit or cancel a customer's order quantity directly from the order view. These changes will save to Shopify. To make these changes, click the 3 dots and select ****Edit**** or ****Cancel****.

        If an order agent edits or cancels an order's quantity, the customer will receive a new email from Shopify with either an updated invoice for payment or a confirmation of the cancelled order.
- Events taken by the profile
  - Clicking the ****# of events**** button on the right shows a list of recent events. You can filter this activity based on the metric you want to see, and can also [save a filtered view](https://help.klaviyo.com/hc/en-us/articles/36403236266139).

![helpdesk2.jpg](https://klaviyo.zendesk.com/hc/article_attachments/39926005322523)

## Helpdesk settings and customization

You can configure how Inbox behaves by going to ****Helpdesk > Settings****. There, you'll find options that apply globally, as well as settings specific to each support channel you use.

![Inboxsettings.jpg](https://klaviyo.zendesk.com/hc/article_attachments/39926012913563)

## Channel-specific settings

Depending on which support channels you’re using Inbox for, there’s settings you can configure via the corresponding channel tabs in the settings menu bar.

![helpdesk3.jpg](https://klaviyo.zendesk.com/hc/article_attachments/39926012916763)

### Email ticket settings

- Email support and forwarding
  - Converts incoming customer emails into Helpdesk tickets.
    - Recommendation: Set up email forwarding from your support address to route messages directly to Helpdesk. [Learn more about using Inbox for email support](https://help.klaviyo.com/hc/en-us/articles/38938328988827).

### SMS ticket settings

- SMS auto-responder
  - Sends automated replies when someone texts without using a keyword.
    - Recommendation: Set the auto-responder to send only to non-consented profiles, and update the message to something like: “{{Organization prefix}}: We can’t respond because you have not consented to receive SMS. For help, reach us at {{email}}.”
- Email notifications about new messages
  - Receive an email alert when you receive a new SMS message in Inbox.
    - Recommendation: Turn this setting on if you plan to use Helpdesk for customer support.
- Link shortening
  - Automatically shortens any link in your outbound SMS message to use fewer characters and allow revenue to be attributed within Klaviyo. [Learn more about the different types of shortened links available](https://help.klaviyo.com/hc/en-us/articles/17649677926299).
    - Recommendation: This setting is on by default and should remain enabled.

### Web chat ticket settings

- Support email address
  - Sends a single follow-up email to customers who go offline during a web chat session if more than 3 minutes pass after your last reply.
    - Recommendation: Use an email address that includes your domain name (e.g., support@yourbusiness.com) to reduce the risk of being flagged as spam.
- Office hours and web chat auto-responders
  - Defines your team’s availability for support via web chat and sends automated messages to customers based on that availability. [Learn how to configure office hours](https://help.klaviyo.com/hc/en-us/articles/38298315322907).
    - Recommendation: Set clear hours to manage expectations and use auto-responders to inform customers when your team is offline.

## Key Helpdesk features

- Edit Shopify Order or Recharge Subscription
  - Agents can edit and cancel Shopify orders, directly from the ticket. They can also skip, cancel, or edit recharge subscriptions.
- Segment and Tag Routing
  - Assign tickets to the right team based on the segment the customer is in, or the tag of the ticket
- AI Auto Tagging
  - Helpdesk will automatically tag inbound tickets with common ecommerce tags like Returns, Product Specific, and more
- Ticket auto-close
  - Automatically close tickets after a set period of no activity from the customer. [Learn about auto-close settings](https://klaviyo.zendesk.com/hc/en-us/articles/39689963719835).
- Round robin ticket assignment
  - Distribute new tickets evenly among available (“online”) team members. [Learn more about ticket assignment for Inbox tickets](https://help.klaviyo.com/hc/en-us/articles/35970894978075).
- Macros
  - Pre-written, reusable responses support agents can use to reply faster. [Learn how to create macros](https://help.klaviyo.com/hc/en-us/articles/4995667413531).
- Internal notes
  - Private comments within tickets that are only visible to your team, not customers. [Learn how to use internal notes](https://klaviyo.zendesk.com/hc/en-us/articles/35728181961499).

## Reporting

The reporting dashboard in Klaviyo Helpdesk summarizes your support activity and performance. Use it to track:

- Ticket volume
- First response time
- Resolution time
- Agent or tag performance

[Learn how to monitor the Inbox reporting dashboard](https://help.klaviyo.com/hc/en-us/articles/39478286954395).

****How are SMS tickets attributed?****

An SMS message in a ticket can be attributed to a specific campaign or flow. It works like this:

1. You send out an SMS campaign (or flow).
2. A customer texts back within seconds.

In this case, the customer’s message is attributed to the message you sent.

Note that:

- The customer must text within your [attribution window](https://help.klaviyo.com/hc/en-us/articles/1260804504250) (the default for SMS is 24 hours).
  - If a customer replies outside of this window (e.g., more than 24 hours later), their reply is not attributed to any message in Klaviyo.
- Only the first message is attributed.
  - Example: if a customer replies with several texts in quick succession, only the first is attributed. The other replies are not attributed to any message in Klaviyo.
- Attribution is based on the last message the customer received.
  - Example: say a subscriber receives a campaign and then a flow. In this case, the customer’s message is always attributed to the flow message.

## Image Support

Helpdesk support inbound and outbound media for email, text messaging, webchat, WhatsApp and Instagram DMs.
