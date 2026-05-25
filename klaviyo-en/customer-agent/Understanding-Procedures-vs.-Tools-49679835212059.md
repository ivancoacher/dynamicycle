---
id: "49679835212059"
title: "Understanding Procedures vs. Tools"
source_url: "https://help.klaviyo.com/hc/en-us/articles/49679835212059-Understanding-Procedures-vs-Tools"
section: "Skills"
category: "Customer Agent"
category_slug: "customer-agent"
klaviyo_updated: "2026-04-28T02:34:24Z"
language: "en"
---
## You will learn

The difference between procedures and tools in Customer Agent, when to reach for each, and how they work together. By the end, you’ll know which primitive to use when you want Customer Agent to do something new.

## The short version

|  |  |  |
| --- | --- | --- |
|  | ****Procedure**** | ****Tool**** |
| ****What it is**** | A way Customer Agent handles a type of request | A specific capability Customer Agent can use mid-response |
| ****Defines**** | **What** Customer Agent handles | **How** Customer Agent acts |
| ****Examples**** | Order tracking, Returns & exchanges, General Q&A, a custom Warranty Claim procedure | Get Customer Orders, Search Shop Catalog, Search Company Knowledge, a custom "check inventory" tool |
| ****Runs on its own?**** | Yes — a procedure is picked by the router when a matching request comes in | No — tools only run when a procedure uses them |
| ****Reusable?**** | A procedure is used once per matching request | A tool can be used by many procedures |

## What a procedure is

A ****procedure**** is a way Customer Agent handles a specific type of shopper request. When a message comes in, Customer Agent’s router picks the best procedure for the request based on each procedure’s description.

Each procedure has its own behavior — what to say, what to check, when to escalate. Customer Agent comes with procedures out of the box. Creating fully custom procedures from scratch is currently in closed beta.

## What a tool is

A ****tool**** is a specific capability Customer Agent can use during a conversation — to fetch data or take an action. Tools only run when a procedure uses them.

For example, the Get Customer Orders tool looks up a shopper’s orders in Shopify. It’s used by the Order tracking procedure, the Order editing procedure, and the Returns & exchanges procedure.

## How they work together

Procedures and tools combine. Most procedures use at least one tool, and a tool can be used by any number of procedures.

A few common patterns, with examples:

- ****Content-only procedure**** — A procedure that answers from your knowledge base. For example, the General Q&A procedure uses the Search Company Knowledge tool to look up answers in your indexed webpages, uploaded files, and snippets.
- ****Procedure with a dedicated tool**** — A procedure built around a single external action. For example, a custom Warranty Claim procedure paired with a fully custom tool that calls your warranty system’s API.
- ****Tool used by multiple procedures**** — One tool that powers several procedures. For example, Get Customer Orders is used by Order tracking, Order editing, and Returns & exchanges.

## How to decide

A quick decision guide:

- ****“I want Customer Agent to handle a new type of request.”**** → Build a procedure.
- ****“I want Customer Agent to fetch data or take an action in an external system.”**** → Build a tool. You’ll attach it to a procedure so it can actually run.
- ****“I want Customer Agent to handle a new type of request**** ******and****** ****call my API.”**** → Build both — the procedure scopes what to handle, and the tool handles the API call.
- ****“I want to change how Customer Agent writes or when it escalates.”**** → You’re looking for Guidance, not a procedure or tool. Head to Customer Agent Guidance to adjust tone, communication style rules, or escalation rules.
- ****“I want Customer Agent to know a fact I can write down.”**** → That’s content. Add it to your content library and Customer Agent will use it when answering questions.

## Examples

****Shopper asks about returns.****
The Returns & exchanges procedure handles the request. It uses several tools: Get Customer Orders to look up the order, plus a returns-provider tool (e.g., Loop) to create the return.

****Shopper asks a product recommendation question.****
The Product Recommendations procedure handles it. It uses the Get Product Recommendations tool to surface personalized picks and the Search Shop Catalog tool to look up specific products.

****Brand wants Customer Agent to book restaurant reservations.****
Build a Reservation Booking procedure (a fully custom procedure) plus a fully custom tool that calls the reservation system’s API. The procedure decides when to book; the tool does the booking.

****Brand wants Customer Agent to use a more casual tone.****
No procedure or tool needed. That’s a Guidance setting — adjust tone of voice in Customer Agent Guidance.