---
id: "49994508239131"
title: "Understanding Tools"
source_url: "https://help.klaviyo.com/hc/en-us/articles/49994508239131-Understanding-Tools"
section: "Tools"
category: "Customer Agent"
category_slug: "customer-agent"
klaviyo_updated: "2026-05-05T20:40:57Z"
language: "en"
---
## You will learn

What tools are, what they do, and how they fit alongside skills and content. By the end, you’ll know when a tool is the right building block and when to reach for something else.

****Note:**** Customer Agent comes with tools out of the box. Creating fully custom tools from scratch is currently in closed beta. If you’re not in the beta, you won’t see a dedicated Tools page — but the tools that come with Customer Agent still run behind the scenes when skills use them. You can see the tools a skill uses by clicking into the skill’s details.

## What a tool is

A ****tool**** is a specific capability Customer Agent can use during a conversation to fetch data or take an action. If skills are what Customer Agent knows how to **handle**, tools are the concrete things it can **do**.

For example, when a shopper asks “Where is my order?”, Customer Agent uses the Get Customer Orders tool to pull that shopper’s order data from Shopify, then responds with the tracking info.

## What tools do

Tools fall into three categories:

- ****Fetch data**** — Look up an order, search your product catalog, pull a customer’s subscriptions or coupons
- ****Take action**** — Cancel a subscription, apply a discount, create a support ticket (via fully custom tools)
- ****Integrate with external systems**** — Call your OMS, CRM, loyalty platform, or any HTTP endpoint (via fully custom tools)

## Tools vs. content

Content is ****static knowledge**** Customer Agent uses to answer questions — your shipping policy, product descriptions, FAQs. Tools are ****dynamic actions**** that fetch real-time data or change something.

A good test: if the answer is the same for every customer, it belongs in content. If the answer depends on **who** is asking or **what** they’ve done, it needs a tool.

## Tools vs. skills

Skills define ****what Customer Agent handles****. Tools define ****how it acts**** during that handling.

A single skill can use multiple tools. A single tool can be used by multiple skills. For example, `Get Customer Orders` is used by Order Tracking, Order Editing, and Returns & Exchanges.

For a deeper decision framework, see [[Understanding skills vs. tools]].

## Tools that come with Customer Agent

Customer Agent comes with a set of tools out of the box that skills use. You don’t set them up — they run when a skill needs them. Examples:

|  |  |
| --- | --- |
| ****Tool**** | ****What it does**** |
| Get Customer Orders | Fetches recent customer orders from Shopify. |
| Search Shop Catalog | Searches for products from the online store, hosted on Shopify. |
| Search Company Knowledge | Looks up company knowledge across indexed webpages, uploaded files, and snippets of text. |
| Get Customer Coupons | Fetches customer coupons for the provided profile ID. |
| Get Customer Subscriptions | Fetches subscriptions for the provided profile ID. |
| Get Product Recommendations | Fetches personalized product recommendations based on customer preferences and interests. |
| Get Profile | Fetches customer profile data. |

If you’re in the beta for creating fully custom tools, you can see the full list on the Tools page. If you’re not, you can view which tools a skill uses by clicking into that skill’s details.

## Fully custom tools 🏷️ BETA

Creating fully custom tools from scratch lets you connect Customer Agent to any HTTP endpoint — your OMS, CRM, loyalty platform, or anything else with an API. Use a fully custom tool when the tools Customer Agent comes with don’t cover what you need.

Access is limited to brands in the managed beta. See [[How to create a tool]] to build one.

## How tools get used

Tools are attached to skills. A skill’s instructions tell Customer Agent which tools are available and when to use them.

The flow inside a single conversation:

1. Shopper sends a message
2. Router picks a skill based on intent
3. Skill’s instructions decide whether a tool is needed
4. Customer Agent uses the tool to fetch data or take an action
5. Customer Agent generates a response using what the tool returned

## Anatomy of a tool

Every tool has these parts:

- ****Name**** — Short identifier (e.g., `Get Customer Orders`)
- ****Description**** — Natural-language explanation of what the tool does. This matters: it drives whether Customer Agent decides to use the tool for a given request.
- ****Input schema**** — The parameters the tool takes (e.g., `profile_id`, `order_id`)
- ****HTTP config**** **(fully custom tools only)** — The method, URL, headers, and body

A good tool description is specific and unambiguous. Vague descriptions cause Customer Agent to skip a tool when it shouldn’t use one, or use a tool when it shouldn’t.