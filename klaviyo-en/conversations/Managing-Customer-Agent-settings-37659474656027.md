---
id: "37659474656027"
title: "Managing Customer Agent settings"
source_url: "https://help.klaviyo.com/hc/en-us/articles/37659474656027-Managing-Customer-Agent-settings"
section: "Customer Agent"
category: "Conversations"
category_slug: "conversations"
klaviyo_updated: "2026-04-28T02:59:56Z"
language: "en"
---
## You will learn

Where to configure Customer Agent’s handoff behavior, channel-level settings, agent name and greeting, and permissions for who can edit the agent.

## Before you begin

You’ll need:

- An ****Owner****, ****Admin****, or ****Manager**** role
- Customer Agent enabled

## Overview

Settings control how Customer Agent operates outside of conversation behavior — things like how it hands off to a human, which channels are active, and how the agent identifies itself to shoppers.

If you’re looking to change how Customer Agent **talks** (tone, communication style) or **escalates** (escalation rules), that’s Guidance. See **Understanding Customer Agent Guidance**.

## Configure handoff

Handoff settings control what happens when Customer Agent can’t resolve a conversation — either because an escalation rule fired or because the shopper asked for a human.

Two methods:

- ****Send a ticket to your helpdesk**** — Customer Agent creates a ticket and continues to manage the shopper experience based on which helpdesk you use.
- ****Don’t hand off**** — Customer Agent shows a custom message instead of handing off. Use this if you don’t have a helpdesk integration but still want to give shoppers a clear next step.

### Helpdesk options

Behavior varies by helpdesk:

- ****Klaviyo Helpdesk**** — Conversation lands in Inbox. The shopper continues the conversation through web chat with your team.
- ****Zendesk**** — A Zendesk ticket is created. Web chat continues to be available to the shopper while the ticket is open.
- ****Gorgias**** — A Gorgias ticket is created. The conversation transfers to email; web chat closes after handoff.

Each helpdesk receives the conversation transcript, timestamps, the visitor’s email address, and the Klaviyo profile ID with the ticket.

### Web chat handoff requires authenticated customers

Handoffs to a human agent on web chat require the shopper to be signed into an authenticated customer account. Anonymous shoppers won’t be able to continue the conversation with a human via web chat — they’ll need to provide an email address or sign in.

### Per-channel handoff

Web chat, email, SMS, and WhatsApp are configured separately. You can use different handoff destinations per channel — for example, web chat handoffs go to Klaviyo Helpdesk and SMS handoffs go to Zendesk.

## Configure channels

Each channel has its own toggle and configuration. From this section, you can:

- See which channels are active
- Toggle a channel on or off
- Open a channel’s setup (which redirects to the relevant settings page — for example, [klaviyo.com/settings/sms](https://www.klaviyo.com/settings/sms/) for SMS, [klaviyo.com/settings/whatsapp](https://www.klaviyo.com/settings/whatsapp/) for WhatsApp)

To launch a channel from scratch, see **How to launch your Customer Agent**.

## Configure general settings

A few brand-level settings live here:

- ****Agent name**** — How Customer Agent introduces itself to shoppers (e.g., “Maya” or “Hammerhead Help”). Affects the greeting and any places Customer Agent refers to itself by name.
- ****Greeting**** — The opening message Customer Agent shows when a shopper opens a conversation.
- ****Avatar**** — The image shoppers see in the chat widget. Upload a logo or branded illustration.

## Permissions

Customer Agent settings are role-gated:

- ****Owner****, ****Admin****, ****Manager**** — Can view and edit all settings.
- ****Other roles**** — Can view conversation data and reporting, but can’t edit settings.

If you need to change who can edit, update the user’s role in your Klaviyo account settings.

## Troubleshooting

****Symptom:**** Handoff emails aren’t sending to my helpdesk.
****Likely cause:**** Helpdesk integration isn’t connected, or the connection has expired.
****Fix:**** Open your helpdesk integration in Klaviyo. Reconnect if expired. Test by escalating a sample conversation in the test sidebar.

****Symptom:**** A channel toggle doesn’t take effect.
****Likely cause:**** A required prereq for the channel isn’t met (e.g., no two-way SMS sender configured), or the change hasn’t propagated yet.
****Fix:**** Check the channel’s setup page. Confirm prereqs. If the toggle stays in the same state, refresh the page.

****Symptom:**** Web chat handoff isn’t reaching a human agent.
****Likely cause:**** The shopper isn’t signed in, or no human agents are available in the helpdesk.
****Fix:**** Confirm shoppers can sign in or provide an email address before handoff. Check helpdesk staffing for the relevant queue.

## FAQ

****Can different channels have different handoff destinations?****
Yes. Each channel’s handoff is configured separately.

****What happens to in-progress conversations when I change handoff settings?****
Changes apply to new handoffs going forward. Conversations already escalated stay routed where they were sent originally.

****Can I temporarily disable handoff?****
Set the handoff method to “Don’t hand off” and provide a custom message. Customer Agent will show that message instead of escalating.

## Next steps

- ****Configure escalation rules**** to control **when** Customer Agent hands off
- ****Test in the test sidebar**** to confirm handoff works as expected
- ****Monitor escalation rates**** on the Performance dashboard