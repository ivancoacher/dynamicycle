<h1>How to test your Customer Agent</h1>

## You will learn

How to test Customer Agent in the test sidebar, debug responses you don’t expect, and validate skills before shoppers see them.

## Before you begin

You’ll need:

- Customer Agent enabled
- Some content, Guidance, and skills configured (you can iterate, but testing without any setup won’t tell you much)

## Why testing matters

Customer Agent’s behavior comes from a stack of signals — your content, Guidance, skills, tools. A small change in any of those (rewriting your brand summary, adding a comm style rule, attaching a new tool) can ripple into responses you didn’t expect.

Test before launching, and re-test every time you make a meaningful change. Most brands run a thorough test pass before going live, then check in every 30 days, or any time they update content for a sale, a new product line, or a policy change.

## Set it up

### 1. Open the test sidebar

Open the test sidebar from anywhere inside Customer Agent. The sidebar simulates a real conversation — Customer Agent uses the same skills, tools, content, and Guidance it would use with a live shopper.

You can adjust:

- ****Page context**** — simulate the shopper being on a specific page (PDP, collection, cart, etc.)
- ****Channel**** — test how responses render on web chat, SMS, or email
- ****Profile**** — pick a Klaviyo profile so Customer Agent has order history, subscriptions, and other context to work with

### 2. Send sample questions

Run shopper-style messages. A starter set:

- “How do I care for it?” **(tests product question handling)**
- “What material is this made of?” **(tests product knowledge from your catalog)**
- “Where is my order?” **(tests the Order tracking skill)**
- “What’s your return policy?” **(tests content retrieval)**
- “Can I talk to a person?” **(tests handoff)**

Mix in questions specific to your brand — anything you’d expect a real shopper to ask.

### 3. Review what happened under the hood

After every response, you can inspect what Customer Agent did:

- ****Which skill**** Customer Agent picked
- ****Which tools**** ran and what they returned
- ****Which content**** was retrieved
- ****The final response**** and any escalation rules that matched

Use this to trace why Customer Agent responded the way it did. Most issues fall out from one of those four signals.

## Testing skills

If you’ve built a fully custom skill, focus your testing on three things:

- ****Router behavior**** — Send messages that should match your skill’s “When to use this skill.” Confirm your skill was actually picked.
- ****Response behavior**** — Walk through the sections in your skill’s “How to respond.” Make sure each section’s behavior happens — including tool usage and any handoff actions.
- ****Tool usage**** — If your skill uses tools, confirm they fire at the right step with the right parameters.

Iterate on “When to use this skill” if the router is picking it wrong, and on “How to respond” if the behavior is off.

## Debugging a bad response

When Customer Agent gives a response that doesn’t seem right, work through it in this order:

1. ****Was the right skill picked?**** If not, the issue is in the skill’s “When to use this skill.”
2. ****Was the right content retrieved?**** If Customer Agent used outdated or wrong content, fix the source — see **How to add and manage content**.
3. ****Did tools run correctly?**** Check the tool calls for missing parameters or unexpected returns.
4. ****Did Guidance shape the response correctly?**** Tone, communication style rules, and escalation rules all layer on top of skill output.

Fix at the source rather than patching downstream.

## Troubleshooting

****Symptom:**** Customer Agent picks the wrong skill.
****Likely cause:**** Skill descriptions overlap, or “When to use this skill” is too broad or too narrow on a fully custom skill.
****Fix:**** Tighten the skill’s “When to use this skill” content. Test multiple phrasings of the same intent.

****Symptom:**** Customer Agent doesn’t use a tool you expect.
****Likely cause:**** Tool isn’t attached to the skill, or “How to respond” doesn’t reference the tool at the right step.
****Fix:**** Confirm the tool is attached. In “How to respond,” insert the tool inline at the step where it should run.

****Symptom:**** Customer Agent uses the wrong content.
****Likely cause:**** Conflicting sources, or higher-quality content covering the same topic outranks the source you expected.
****Fix:**** Audit and consolidate conflicting content. Re-sync sources you’ve recently edited.

****Symptom:**** Response tone or style is off.
****Likely cause:**** Tone of voice or communication style rules need adjustment.
****Fix:**** Review Guidance settings. Iterate on tone or add a specific communication style rule.

## Coming soon: Simulations

Simulations are an upcoming feature for running Customer Agent against batches of shopper-style inputs and grading the responses at scale. Until simulations ship, the test sidebar is the main testing tool.
