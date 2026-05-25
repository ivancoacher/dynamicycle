---
id: "44483282667163"
title: "How to launch your Customer Agent"
source_url: "https://help.klaviyo.com/hc/en-us/articles/44483282667163-How-to-launch-your-Customer-Agent"
section: "Customer Agent"
category: "Conversations"
category_slug: "conversations"
klaviyo_updated: "2026-04-29T20:10:55Z"
language: "en"
---
## You will learn

How to launch Customer Agent across web chat and email, what to confirm before going live, and where to monitor performance once shoppers start interacting with it.

## Before you begin

You’ll need:

- An ****Owner****, ****Admin****, or ****Manager**** role
- For ****web chat****: web chat configured at [klaviyo.com/settings/webchat/general](https://www.klaviyo.com/settings/webchat/general)
- For ****email****: inbound email configured at [klaviyo.com/inbox/settings/email](https://www.klaviyo.com/inbox/settings/email)
- For ****SMS****: SMS configured at [klaviyo.com/settings/sms](https://www.klaviyo.com/settings/sms/), with a two-way SMS-enabled sender (see **How to launch Customer Agent on SMS**)
- For ****WhatsApp****: WhatsApp configured at [klaviyo.com/settings/whatsapp](https://www.klaviyo.com/settings/whatsapp/), with a verified Meta business account (see **How to launch Customer Agent on WhatsApp**)

You also want a clean test pass before launching. Run through **How to test your Customer Agent** if you haven’t yet.

## Pre-launch checklist

Before you turn on any channel, confirm:

- ****Content reviewed**** — auto-ingested storefront content looks right; major gaps filled
- ****Guidance set**** — brand summary, tone of voice, and at least a few comm style + escalation rules in place
- ****Active skills confirmed**** — see which skills are running and which fully custom skills you’ve enabled
- ****Handoff configured**** — see **Managing Customer Agent settings** for ticket-to-helpdesk or custom message handoff
- ****Tested in the test sidebar**** — sample questions return responses you’d want a shopper to see

If any of these are missing, the ****Turn on**** button will gray out for the affected channel.

## Set it up — web chat

1. Navigate to ****Customer Agent > Launch > Web chat****.
2. Review the ****audience**** for who Customer Agent should respond to:

   - ****Segments**** — include or exclude specific Klaviyo segments (e.g., only logged-in customers, exclude wholesale buyers)
   - ****Keywords**** — set exact-match keywords that should always or never trigger Customer Agent
3. Customize the ****intro**** — the greeting Customer Agent shows when a shopper opens web chat.
4. ****Review Skills**** — see which skills are active for your brand. Skills Customer Agent comes with activate automatically based on your integrations; you can disable any skill you don’t want active. Fully custom skills you’ve created are listed here too.
5. Confirm ****handoff settings**** — where conversations go when a human is needed.
6. ****Preview**** the experience to confirm rendering, tone, and intro look right.
7. Click ****Turn on****.

Customer Agent only responds to messages received **after** you turn it on. Conversations already in progress won’t be picked up.

## Set it up — email

1. Make sure inbound email is set up at [klaviyo.com/inbox/settings/email](https://www.klaviyo.com/inbox/settings/email). Customer Agent uses your inbound email configuration.
2. Navigate to ****Customer Agent > Launch > Email****.
3. Confirm the ****reply address**** Customer Agent will use.
4. Confirm ****handoff settings****.
5. ****Preview**** sample email responses.
6. Click ****Turn on****.

Web chat and email can be turned on independently — you don’t need to launch both at once.

## Set it up — SMS and WhatsApp

These channels have unique setup requirements (number provisioning, compliance, Meta verification, message templates). Each has its own guide:

- **How to launch Customer Agent on SMS**
- **How to launch Customer Agent on WhatsApp**

You can run any combination of channels simultaneously.

## Post-launch monitoring

Once Customer Agent is live, monitor it on the Performance dashboard. Key things to check in the first week:

- ****% resolved by AI**** — how often Customer Agent finishes the conversation without escalation
- ****AI-generated sales**** — ATC, link clicks, AOV from CA-driven conversations
- ****Escalation rate per rule**** — which escalation rules fire most, and whether they should
- ****Conversation outcomes**** — Resolved, Routed, Closed, Open

If something looks off — low resolution rate, unexpected escalations, weird tone — go back to the test sidebar to debug. Most issues trace back to content gaps, an over-broad escalation rule, or a skill’s “When to use this skill” being too narrow.

See **Understanding the performance dashboard** for what each metric means and how to act on it.

## Troubleshooting

****Symptom:**** The web chat widget isn’t appearing on my site.
****Likely cause:**** Web chat isn’t configured, or the embed isn’t loading on the page.
****Fix:**** Confirm web chat is configured at [klaviyo.com/settings/webchat/general](https://www.klaviyo.com/settings/webchat/general) and the chat widget is visible on your site. If using a custom site, verify the embed snippet is present.

****Symptom:**** Customer Agent isn’t replying to emails.
****Likely cause:**** Inbound email isn’t configured, the reply address isn’t set, or the channel hasn’t been turned on after setup.
****Fix:**** Confirm inbound email is configured at [klaviyo.com/inbox/settings/email](https://www.klaviyo.com/inbox/settings/email). Check the reply address in ****Customer Agent > Launch > Email****. Confirm the channel toggle is on.

****Symptom:**** The ****Turn on**** button is grayed out.
****Likely cause:**** A required prereq isn’t met — usually missing handoff settings, no SMS sender configured, or web chat not configured.
****Fix:**** Hover over the button to see which prereq is failing. Fix the gap and try again.

****Symptom:**** A new shopper message isn’t getting picked up.
****Likely cause:**** Conversation started before Customer Agent was turned on, or the shopper is in an excluded segment.
****Fix:**** Check audience settings — segments and keywords. New conversations from included audiences should pick up automatically.

## FAQ

****How fast can I turn Customer Agent off?****
Toggle the channel off on the Launch page. Customer Agent stops responding to new messages immediately.

****Can web chat, email, SMS, and WhatsApp run at the same time?****
Yes. Each channel is configured separately and they can run in any combination.

## Next steps

- ****Monitor performance**** on the Performance dashboard
- ****Iterate on content and Guidance**** based on what you see in real conversations
- ****Run a test pass**** any time you make a meaningful change