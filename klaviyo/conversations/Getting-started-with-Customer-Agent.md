---
id: 37659268052635
title: "Getting started with Customer Agent"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/37659268052635-Getting-started-with-Customer-Agent"
section: "Customer Agent"
category: "Conversations"
category_slug: "conversations"
klaviyo_updated: "2026-04-29T20:10:56Z"
language: en
---

## You will learn

What Customer Agent is, how it works, and the steps to get from setup to launch. By the end, you’ll know which building blocks shape Customer Agent’s behavior and where to go to configure each one.

## What is Customer Agent

Customer Agent is Klaviyo’s AI agent that resolves shopper inquiries on your behalf — across web chat, email, SMS, and WhatsApp. It can track orders, answer product and brand questions, recommend products, process returns and exchanges, manage subscriptions, and hand off to a human when something needs personal attention.

Customer Agent comes with skills and tools out of the box and is fully customizable. Creating fully custom skills and tools from scratch is currently in closed beta.

## Before you begin

You’ll need:

- A Klaviyo account with ****Owner****, ****Admin****, or ****Manager**** role
- For web chat: web chat configured at [klaviyo.com/settings/webchat/general](https://www.klaviyo.com/settings/webchat/general)
- For SMS: a two-way SMS-enabled sender
- English-language storefront (other languages coming soon)

## How Customer Agent works

When a shopper sends a message, Customer Agent runs through four steps:

1. ****Receives the message**** across whichever channel the shopper used.
2. ****Adds context**** — pulls in your brand summary, the shopper’s profile and history, and any active Guidance.
3. ****Routes**** — picks the right skill based on what the shopper is asking for.
4. ****Responds**** — the chosen skill uses content, tools, and Guidance to generate a reply (or hands off to a human if needed).

Customer Agent handles a wide range of shopper inquiries:

- Brand and product questions (“What’s your return policy?”, “Is this dairy-free?”)
- Product recommendations (“What do you suggest for sensitive skin?”)
- Order status and tracking (“Where is my order?”)
- Returns, exchanges, and order edits
- Subscription and loyalty management
- Small talk, greetings, and follow-ups

## The four building blocks

Customer Agent’s behavior comes from four building blocks. You’ll configure each of these as you set up.

### Skills

Skills are the things Customer Agent knows how to do — like Order tracking, Returns & exchanges, or Product Recommendations. Customer Agent comes with eight skills out of the box. Creating fully custom skills from scratch is currently in closed beta.

Skills are automatically active when their prerequisites are met (for example, Order tracking turns on when Shopify is connected).

### Tools

Tools are specific capabilities Customer Agent uses to fetch data or take actions during a conversation — like looking up an order, searching your catalog, or retrieving customer subscriptions. Customer Agent comes with a set of tools out of the box. Creating fully custom tools to connect to any HTTP endpoint is currently in closed beta.

### Content

Content is everything Customer Agent knows about your brand — your help articles, policies, product details, FAQs. Customer Agent automatically scrapes your storefront on setup, so most brands have hundreds of pages indexed before adding anything manually. You can add documents, webpages, and snippets directly in Customer Agent.

### Guidance

Guidance shapes how Customer Agent communicates and decides what to escalate. It has four levers: brand summary, tone of voice, communication style rules, and escalation rules. Guidance applies globally — every skill inherits your settings.

## Setup checklist

A typical Customer Agent setup looks like this:

1. ****Review your content.**** Customer Agent auto-ingests your storefront on setup. Check what’s there, fill gaps, and adjust anything outdated.
2. ****Configure Guidance.**** Write your brand summary, set tone of voice, and add a few communication style and escalation rules.
3. ****Confirm active skills.**** See which skills are running for your brand based on your integrations. Connect additional providers (Loop/Aftership for returns, Recharge/Skio for subscriptions, Yotpo/Smile.io for loyalty) to unlock more.
4. ****Test in the playground.**** Send sample messages, check responses, and iterate on content or Guidance until results meet your bar.
5. ****Launch.**** Turn on the channels you want — web chat, email, SMS, WhatsApp.

## Security and privacy

A few things worth knowing about how Customer Agent handles data:

- Customer data is ****never used**** to train large language models.
- ****Personally identifiable information**** (PII) is stripped from prompts where possible.
- All data is ****encrypted in transit****.
- Conversations are stored against the Klaviyo profile of the shopper, when one exists.

## Next steps

Each building block has its own deeper guide:

- ****Add and manage content**** for Customer Agent’s knowledge base
- ****Understanding skills**** for what Customer Agent can do out of the box
- ****Understanding Customer Agent Guidance**** to control how Customer Agent communicates
- ****How to test your Customer Agent**** before going live
- ****How to launch your Customer Agent**** to turn it on for your shoppers