---
id: 33660391549211
title: "Getting started with web chat"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/33660391549211-Getting-started-with-web-chat"
section: "Use web chat"
category: "Customer Hub"
category_slug: "customer-hub"
klaviyo_updated: "2026-04-21T13:54:39Z"
language: en
---

## You will learn

Learn about web chat, which is a 2-way communication channel you can add to your website. Web chat can be set up on its own for you to use with Customer Agent and Helpdesk, but it's also designed to be a seamless part of Customer Hub. Web chat allows your business to engage in live, personalized conversations with visitors on your website so they can easily get answers to their questions or assistance with issues.

## Before you begin

Web chat is a real-time communication channel that allows you to engage with visitors on your website. ****You can now use Web Chat as a standalone feature**** without enabling the full Customer Hub interface.

This allows you to quickly set up chat for your support team (via Helpdesk) or AI Service Agent without additional configuration. If you choose to use Customer Hub later, Web Chat will integrate seamlessly with it.

Web chat is also designed to work great with Customer Hub as the "chat" tab. [Learn more about Customer Hub](https://klaviyo.zendesk.com/hc/en-us/articles/33660324811675)

##

![Customer Hub open on an example brand's website showing a shopper messaging in the web chat tab.](https://klaviyo.zendesk.com/hc/article_attachments/34189526090139)

### Customer experience with web chat

When a signed-in site visitor opens web chat, their experience follows these steps:

- ****FAQs**** (if enabled):
  If you have [published FAQs](https://klaviyo.zendesk.com/hc/en-us/articles/36400427885979), these appear first in the chat thread as the initial touchpoint. Visitors can browse and select from your common questions to receive instant, automated answers.
- ****Welcome message****:
  If no FAQs are published, or if the visitor still needs help after viewing FAQs, they can proceed to start a live web chat session. They will automatically receive your web chat welcome message (e.g., "What do you need assistance with today?"), and can type their message.

Once the visitor sends their question, it becomes a ticket in Klaviyo Helpdesk for your support team to assist. When a support representative replies, the visitor receives the response instantly in the chat thread, creating a real-time, back-and-forth conversation.

Visitors can end the chat at any time. Once closed, the conversation cannot be reopened. The visitor must start a new web chat session for additional support.

If you have the [AI Customer Agent enabled](https://klaviyo.zendesk.com/hc/en-us/articles/37659268052635), the web chat experience is different. The AI Service agent serves as the first responder to all incoming web chat messages. It uses your site data and training to answer visitors' questions. If it cannot resolve an inquiry, it escalates the conversation to your support team using your configured handoff setting. For example, if your handoff selection is the Klaviyo Helpdesk, Customer Agent creates a ticket there for your team. If you use another handoff setting (e.g., Zendesk, Gorgias, or a custom message), the Customer Agent follows that workflow.

## Enable web chat

To enable web chat and configure your settings:

1. In Klaviyo, go to ****Settings > Web Chat**** (located in global settings next to other channels).
   ![](https://klaviyo.zendesk.com/hc/article_attachments/44158249084187)
   ![](https://klaviyo.zendesk.com/hc/article_attachments/44158249087643)
2. Toggle ****Enable web chat**** to ****on****.
3. ****Configure your design:**** Go to the "design" tab within the "web chat" settings. Here, you can custoimze the look of your chat as well as the floating onsite widget for customers to open web chat.

   Note: The onsite widget is turned on for all users by default when you enable Web Chat.

![A shopper's view of an ongoing web chat conversation in Customer Hub.](https://klaviyo.zendesk.com/hc/article_attachments/34189526093467)

If you have [Customer Hub](https://help.klaviyo.com/hc/en-us/articles/33660324811675) enabled, you will have access to more additional web chat settings under Customer Hub -> Extensions -> Web Chat, including a visibility setting. Under 'Login status' you can specify if you want web chat visible to all users or signed in users only.

![](https://klaviyo.zendesk.com/hc/article_attachments/45278466868635)

Klaviyo Helpdesk requires users to authenticate before creating a ticket. If you don't have Customer Agent live, every web chat interaction will go directly to a ticket and require users to sign in before your team can respond. You can [enable the Customer Agent](https://klaviyo.zendesk.com/hc/en-us/articles/37659268052635) to respond to anonymous users in real-time.

## Manage web chat messages in Klaviyo

Each inbound message you receive from a customer via web chat (whether from the chat directly or handed off by the AI Agent) creates a new ticket in Klaviyo Helpdesk, where a member of your team can reply.

Note that both SMS and web chat tickets feed into the Klaviyo Helpdesk, offering a consolidated place for managing these 2 direct communication channels. [Learn more about managing tickets in Helpdesk](https://help.klaviyo.com/hc/en-us/articles/360059002271).

### Web chat notifications

A notification badge appears next to the Helpdesk tab in Klaviyo's main navigation when you have new messages. In Helpdesk, new messages show a blue dot to indicate they’re unread, and display the sender’s name as well as a preview of their message.

![Screenshot 2025-09-23 at 3.55.56 PM.png](https://klaviyo.zendesk.com/hc/article_attachments/41373489747483)

Web chat messages also show a distinctive chat icon next to each ticket in **Helpdesk**, allowing for easy differentiation from SMS messages, which show an envelope icon.

A web chat ticket in Helpdesk can have 1 of 3 statuses:

- **Open**, to indicate an ongoing chat.
- **Snoozed**, which you can use to temporarily hide a ticket.
- **Closed**, to mark completed chats.

### Replying to web chat messages

Any member of your team can click on a message in Helpdesk to provide real-time support to the shopper, helping you manage customer queries efficiently.

In an open web chat ticket, your support agents can:

- View the message thread with the sender.
- See a summary of the profile details.
- Check the profile’s event history (whether they ordered a product, received an email, etc.).
  - Use [macros](https://klaviyo.zendesk.com/hc/en-us/articles/4995667413531) for quick replies
  - Use text, images, emojis in your reply
  - Send multiple messages in a row

  To reply to a web chat ticket:

  1. Open the ticket that you want to respond to.
  2. Click into the text box and create your response. You can:

![An example web chat ticket open in the Klaviyo inbox showing an active conversation and the profile details panel open.](https://klaviyo.zendesk.com/hc/article_attachments/36253663051547)

While communicating via web chat, agents can see read receipts, which show whether their messages have been seen by the profile. This ensures clarity in communication and aids in maintaining ongoing helpful dialogues. Replying to a web chat message automatically assigns it to you. Learn more about [ticket assignment for Helpdesk tickets](https://klaviyo.zendesk.com/hc/en-us/articles/35970894978075).

Note that the same profile can have an active web chat ticket and an SMS ticket in **Helpdesk**. Once the web chat ticket is closed, however, it cannot be reopened, and site visitors will have to start a new chat session. Each new conversation begins a new ticket.

## Web chat best practices

#### Using web chat with Customer Hub

If you also use ****Customer Hub****, web chat will appear as a "chat" tab within Customer Hub to deliver a more seamless experience. Your onsite widget will automatically unify to prevent conflicts.

- ****Appearance (Priority):**** If Customer Hub is active, its settings will control the ****visual appearance**** (color, icon, position) of the widget. The appearance settings in the Web Chat section will be disabled to avoid conflicts.
- ****Behavior:**** The Web Chat settings will still control chat-specific behavior, such as your ****Welcome Message****.

If you see a warning in your Web Chat design settings, it means Customer Hub is active and determining your widget's design.

#### Link your privacy policy and terms of service

As a compliance best practice, add links to your site’s privacy policy and terms of service so your customers are notified of the terms governing their interactions with web chat. These links will appear before a site visitor sends their first message. To do so:

1. Navigate to ****Customer Hub****.
2. Select ****Settings >General****.
3. Under **Terms and policy**, add your links for each.

![The general settings menu for Customer Hub showing example terms and conditions linked.](https://klaviyo.zendesk.com/hc/article_attachments/34189482193307)

#### Prioritize prompt responses

Customers anticipate quick replies when using chat tools. If your team can't provide immediate support, manage expectations by:

- [Set up office hours](https://help.klaviyo.com/hc/en-us/articles/38298315322907) so site visitors receive an automated reply when your support team is unavailable for web chat, and are informed of how they can expect to receive assistance from you.
- Enable [email notifications](https://help.klaviyo.com/hc/en-us/articles/360059002271#h_01JP5WNR28YD7777EWPGJ908G8) so your team is notified when you receive a new ticket in Helpdesk.

Additionally, if you are chatting with someone and need to take some time to investigate, ensure you regularly check back in. You don’t want to snooze the message or keep people waiting for long periods of time. Instead, make sure to touch base with them at least once every 3-5 minutes. Even a simple: “Still looking into this. Thank you for your patience” lets the user know you haven’t forgotten about them.

#### Consistently monitor your Helpdesk

Regularly check Helpdesk to ensure no messages are missed and all customer inquiries are addressed promptly, especially after resolving an issue.