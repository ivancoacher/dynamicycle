---
id: "49761952891163"
title: "How to configure communication style rules"
source_url: "https://help.klaviyo.com/hc/en-us/articles/49761952891163-How-to-configure-communication-style-rules"
section: "Guidance"
category: "Customer Agent"
category_slug: "customer-agent"
klaviyo_updated: "2026-04-29T20:13:41Z"
language: "en"
---
## You will learn

What communication style rules are, what they can and can’t do, and how to write rules that meaningfully shape how Customer Agent writes.

## Before you begin

You’ll need:

- An ****Owner****, ****Admin****, or ****Manager**** role
- Tone of voice set (recommended — rules layer on top of tone)

## What communication style rules are

****Communication style rules**** are specific writing guidelines that apply to every Customer Agent response, across every skill and channel. Where tone sets the overall vibe, communication style rules handle the mechanics — sentence length, formatting, specific word choices, phrases to avoid.

You can create up to ****20 rules****. Most brands need only 3-5.

### What rules can do

- Replace specific words (“never say ‘unfortunately’”)
- Enforce vocabulary (“call it a ‘ride’ not a ‘trip’”)
- Forbid specific phrases
- Add disclaimers (e.g., “always remind shoppers to consult a doctor”)
- Set formatting (sentence length, bullet lists, emoji use)

### What rules cannot do

This is the most common confusion — communication style rules are about **how** Customer Agent writes, not **what** it does. Rules ****cannot****:

- Look up customer data
- Check inventory or order status
- Take actions in external systems
- Decide which skill handles a request

If you need any of those behaviors, you need a skill or a tool, not a rule.

## Set it up

1. Navigate to ****Customer Agent > Guidance > Communication style****.
2. Click ****Add rule****.
3. Write a ****Title**** (up to 100 characters) — short and descriptive.
4. Write a ****Description**** (up to 500 characters) — the actual rule and any context Customer Agent needs to follow it.
5. Click ****Save****.
6. Test the rule in the playground.

## Writing good rules

Good rules are:

- ****Specific**** — “Keep responses under three sentences” beats “be concise”
- ****Actionable**** — phrased as something Customer Agent can clearly do or not do
- ****Single-purpose**** — one rule per concept, so they’re easy to enable, disable, and debug

Vague rules (“be helpful,” “make customers happy”) don’t change behavior. They duplicate what tone already does.

## Examples

Five rules that meaningfully change behavior:

- ****Use emojis sparingly**** — At most one emoji per response, and only when it adds warmth. Never use emojis in apologies or escalations.
- ****Keep responses under three sentences**** — Long responses overwhelm shoppers in chat. Lead with the answer; offer details on request.
- ****Never say “unfortunately”**** — It signals a no-answer. Reframe to lead with what we can do.
- ****Always end with a question when the inquiry is open-ended**** — Keeps the conversation going and surfaces the next need.
- ****Don’t apologize for things outside our control**** — Don’t apologize for shipping delays caused by carriers, weather, or order timing. State the situation and offer a path forward.

## Editing and disabling rules

You can toggle any rule on or off without deleting it. Useful for:

- Temporarily disabling a seasonal rule
- Pausing a rule that’s producing unexpected results in the playground

To delete a rule entirely, click the trash icon next to it.

## When to use a rule vs. something else

If you’re not sure where new behavior belongs:

- ****Want to change the**** ******vibe****** ****of every response?**** → Update tone of voice.
- ****Want a specific writing rule applied everywhere?**** → Add a communication style rule.
- ****Want Customer Agent to do something new (look up data, take an action)?**** → Build a skill or tool.
- ****Want Customer Agent to escalate in a specific situation?**** → Add an escalation rule.

## FAQ

****How many rules can I have?****
Up to 20. Most brands use 3-5; more than that and rules tend to conflict.

****Do rules apply to all skills?****
Yes. Rules are global — they apply to every response across every skill and channel.

****What if two rules conflict?****
Customer Agent will try to follow both, but conflicting rules produce inconsistent results. Review your rules periodically and consolidate or remove conflicts.

## Next steps

- ****Configure escalation rules**** for situations that need a human
- ****Test in the playground**** to see how your rules shape responses