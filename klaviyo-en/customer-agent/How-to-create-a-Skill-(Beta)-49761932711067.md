---
id: "49761932711067"
title: "How to create a Skill (Beta)"
source_url: "https://help.klaviyo.com/hc/en-us/articles/49761932711067-How-to-create-a-Skill-Beta"
section: "Skills"
category: "Customer Agent"
category_slug: "customer-agent"
klaviyo_updated: "2026-04-29T20:13:58Z"
language: "en"
---
> ****Beta feature.**** Creating fully custom skills from scratch is currently in a closed managed beta. If you don’t see the option to create a skill, your account doesn’t have beta access yet.

## You will learn

How to build a fully custom skill from scratch, write a description and instructions that make Customer Agent use your skill at the right time, and test it before shoppers see it. This article also covers how to customize the skills Customer Agent comes with.

## Before you begin

You’ll need:

- Customer Agent enabled and beta access for creating fully custom skills
- A clear idea of what your skill should handle — the type of question, situation, or workflow
- Any tools your skill will use — either tools that come with Customer Agent or fully custom tools you’ve built

If you want Customer Agent to do something specific (look up data in your system, take an action in another platform), create the tool first or alongside your skill.

## What a skill is

A ****skill**** is a scoped capability that lets Customer Agent handle a specific type of shopper request. Customer Agent comes with skills out of the box, and creating fully custom skills from scratch is currently in closed beta.

A skill has a ****Title****, a ****When to use this skill**** section (how Customer Agent knows this skill should handle a given request), and a ****How to respond**** section (how Customer Agent should behave once the skill is picked). You can also attach tools and content scopes.

For the underlying concepts, see the Understanding Customer Agent tools article and the Understanding skills vs. tools article.

## When to create a fully custom skill

Build a fully custom skill when:

- ****The skills Customer Agent comes with don’t cover your use case**** — you have a workflow or question type Customer Agent doesn’t handle out of the box
- ****Your business has industry-specific behavior**** — specialized rules, unique product configurations, domain language
- ****You want a multi-step custom process**** — for example, a quiz, a guided troubleshooter, or a workflow that chains several tools together
- ****You want to use a fully custom tool**** — fully custom tools only do something when attached to a skill

## Set it up

### 1. Open the Skills page

Navigate to ****Customer Agent > Skills****, then click ****Create skill****.

### 2. Add a Title

A short identifier like “Size Guide” or “Warranty Claim.” The title is mainly for your reference and for organization — it isn’t used to decide when the skill fires.

### 3. Write “When to use this skill”

****When to use this skill**** tells Customer Agent’s router when your skill should handle a request. Use natural language. Be specific about what this skill handles and, where useful, what it does **not** handle. Including example shopper questions helps the router recognize matching intent.

****Good examples:****

**Size Guide skill:**

> Use this skill when the shopper asks about finding the right size for apparel or footwear — including sizing charts, fit advice, and size exchanges. Example questions: “What size should I get for this dress?”, “Do your shoes run small?”, “How do I know if this will fit?”, “Can I exchange for a different size?”. Do not use this skill for out-of-stock questions; those go to general support.

****Vague example (avoid):****

> For questions about sizing and other product stuff.

The vague version doesn’t tell the router when to pick this skill over any other, and doesn’t show any concrete shopper questions it should match.

### 4. Write “How to respond”

****How to respond**** tells Customer Agent how to behave once your skill is picked. Think of it as a short playbook. The field is a rich text editor — you can type freely, and you can also type `/` to insert specific elements (headings, lists, tools, or handoff actions).

Good “How to respond” content:

- Is specific and scoped to what this skill handles
- Describes how Customer Agent should approach the request — broken into clear topical sections (not numbered steps)
- Inserts tools via `/` at the point where each tool should run
- Inserts handoff actions via `/` where escalation applies
- Calls out what to do when data is missing or the request is out of scope

  Keep it concise. Long, meandering guidance hurts performance more than it helps.

  ****What you can insert via**** `/`****:****
- ****Formatting**** — Text, Heading 1/2/3, Bullet list, Numbered list. Use these to structure the instructions so they’re easy to read and edit.
- ****Actions**** — Two handoff actions:
  - **Offer to hand off** — Customer Agent offers the shopper the option to connect with a human before handing off.
  - **Hand off immediately** — Customer Agent hands off without asking.
- ****Tools**** — Every tool attached to this skill shows up here. Insert a tool inline at the point where you want Customer Agent to use it.

### 5. Attach tools (optional)

If your skill needs to fetch data or take an action, attach the tools it should use. A skill can use multiple tools. The “How to respond” section should tell Customer Agent when to use which tool.

See the How to create a tool article for building your own.

### 6. Attach content scopes (optional)

If your skill should only use specific content (for example, only a dedicated sizing guide rather than your entire knowledge base), set a content scope. Leave this blank to use all available content.

### 7. Test in the playground

Click ****Test**** to open the playground. Send test messages that would normally route to your skill, and check:

- ****Router behavior**** — does Customer Agent actually pick your skill for the test message? If not, “When to use this skill” needs work.
- ****Response behavior**** — does Customer Agent follow the steps you described in “How to respond”?
- ****Tools**** — if the skill should use a tool, does it? With the right parameters?
- ****Response quality**** — is the output what a shopper would expect?

Iterate on “When to use this skill” and “How to respond” based on what you see.

### 8. Enable the skill

When you’re satisfied with playground testing, enable the skill. It will start handling live conversations that match “When to use this skill.”

## Writing a good “When to use this skill”

This is the most important field on a skill. The router uses it — and only it — to decide when your skill should handle a request. A good “When to use this skill”:

- ****Describes what the skill handles**** in plain language
- ****Is specific enough**** that the router won’t pick it for unrelated requests
- ****Is broad enough**** that the router picks it for all the requests it should handle
- ****Calls out edge cases**** where useful — what this skill does **not** handle

Iterate with playground tests. If your skill fires when it shouldn’t, tighten “When to use this skill.” If it doesn’t fire when it should, broaden it or add examples.

## Writing a good “How to respond”

This tells Customer Agent how to handle the request once the skill is picked. Good “How to respond” content:

- ****Is scoped**** to what this skill does — don’t try to cover everything
- ****Breaks the response into clear topical sections**** using headings (not numbered steps)
- ****Inserts tools inline**** at the point where each tool should run — type `/` and pick the tool from the menu
- ****Inserts handoff actions inline**** — type `/` and pick **Offer to hand off** or **Hand off immediately** where it applies
- ****Handles fallback cases**** — “If the data is missing, apologize and offer to hand off”
- ****Shows the shape of a good response**** — formatting, tone, what to include

****Example (“How to respond” for an order-tracking skill):****

> ****Identify shopper and order****
> If the shopper isn’t signed in, let them know they’ll need to log in to locate their order. Once signed in, locate the customer’s profile using their email or phone number to find their recent orders with /Get Profile.

> ****Check shipment status****
> Retrieve the real-time status, tracking URL, and estimated delivery date for the specific order using /Order Status.

> ****Provide update****
> Communicate the current status clearly (e.g., Processing, Shipped, Delivered). If shipped, always provide the clickable tracking link.

## Customizing existing skills

You can disable any skill Customer Agent comes with from the Skills page — useful if you don’t want Customer Agent handling a particular type of request.

Editing existing skills (changing instructions, swapping tools) is coming soon. When it ships, this article will cover that flow.

## Troubleshooting

****Symptom:**** The skill never gets used.
****Likely cause:**** “When to use this skill” is too vague, or the router doesn’t recognize matching requests.
****Fix:**** Rewrite “When to use this skill” to be more specific about what the skill handles. Add example request types. Test with real shopper-style messages in the playground.

****Symptom:**** The skill gets used at the wrong time.
****Likely cause:**** “When to use this skill” is too broad, or it overlaps with another skill.
****Fix:**** Narrow “When to use this skill.” Call out what the skill does **not** handle. Check if another skill should handle those requests instead.

****Symptom:**** The skill doesn’t use its tool.
****Likely cause:**** The tool isn’t attached, or “How to respond” doesn’t insert the tool at the right step.
****Fix:**** Confirm the tool is attached to the skill. In “How to respond,” type `/` and insert the tool at the step where it should run.

****Symptom:**** The skill ignores “How to respond.”
****Likely cause:**** “How to respond” is too long, contradictory, or unclear.
****Fix:**** Tighten it. Remove unrelated guidance. Break it into clear topical sections with headings. Test changes in the playground.

## FAQ

****Can a fully custom skill use the tools Customer Agent comes with?****
Yes. Attach any tool to your skill.

****How do I disable a skill?****
Toggle the skill off on the Skills page. You can re-enable it at any time. This works for both skills Customer Agent comes with and fully custom skills you’ve built.

****How do I monitor how my skill is performing?****
The Performance dashboard breaks down resolution by skill. See Understanding the performance dashboard for details.

## Next steps

- Build tools your skill will use
- Test your skill thoroughly in the playground
- Monitor the skill’s performance after it goes live