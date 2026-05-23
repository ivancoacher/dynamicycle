<h1>How to launch Customer Agent on WhatsApp</h1>

## You will learn

How to launch Customer Agent on WhatsApp, what Meta and template requirements you need to meet first, and how WhatsApp’s specific rules affect how Customer Agent responds to shoppers.

## Before you begin

You’ll need:

- An ****Owner****, ****Admin****, or ****Manager**** role
- A WhatsApp Business account verified with Meta
- WhatsApp configured in Klaviyo at [klaviyo.com/settings/whatsapp](https://www.klaviyo.com/settings/whatsapp/) — including a connected phone number and approved business profile
- Customer Agent enabled, with content and Guidance configured (run **How to test your Customer Agent** before launching)
- Handoff settings configured — see **Managing Customer Agent settings**

## How WhatsApp differs from other channels

WhatsApp has a few rules that affect how Customer Agent works:

- ****Rich messaging.**** WhatsApp supports rich content (images, buttons, lists). Customer Agent uses these where it adds clarity to a response.
- ****Regional availability.**** Customer Agent on WhatsApp is available wherever your WhatsApp Business account is approved to send.

## Set it up

### 1. Confirm WhatsApp is configured in Klaviyo

Navigate to [klaviyo.com/settings/whatsapp](https://www.klaviyo.com/settings/whatsapp/). Confirm:

- Your WhatsApp Business account is connected and verified
- A phone number is provisioned
- Your business display name and profile are approved

If you’re missing any of these, complete WhatsApp setup before continuing.

### 2. Open the Customer Agent Launch page

Navigate to ****Customer Agent > Launch > WhatsApp****.

### 3. Review audience settings

Choose who Customer Agent should respond to on WhatsApp:

- ****Segments**** — include or exclude specific Klaviyo segments
- ****Keywords**** — set exact-match keywords that should always or never trigger Customer Agent

### 4. Configure templates **(if applicable)**

If your brand uses Klaviyo to send WhatsApp templates that Customer Agent should respond to, confirm those templates are approved and active in your WhatsApp settings. Customer Agent reads from your existing template library — it doesn’t create templates on its own.

> **TBD: Confirm whether Customer Agent auto-generates response templates or only uses brand-authored ones at launch.**

### 5. Confirm handoff settings

When Customer Agent escalates on WhatsApp, the handoff follows your configured handoff destination (helpdesk ticket, etc.). Confirm those settings in ****Managing Customer Agent settings****.

### 6. Preview and turn on

Use ****Preview**** to check that your intro message and tone look right. When you’re ready, click ****Turn on****.

Customer Agent only responds to messages received **after** you turn it on.

## Template messages

WhatsApp distinguishes between two types of messages:

- ****Service window messages**** — Sent within 24 hours of the shopper’s last message. No template required. Customer Agent replies freely here.
- ****Outside-window messages**** — If more than 24 hours have passed since the shopper’s last message, WhatsApp requires a pre-approved template to respond. If a shopper sends a follow-up after the window expires, Customer Agent will use a template if one matches the situation.

Make sure your most common response patterns have approved templates if you expect Customer Agent to handle delayed follow-ups.

## Compliance and data handling

WhatsApp has its own consent and regional rules. A few things to be aware of:

- ****Consent**** — Shoppers must opt in to messaging from your business through Meta-compliant flows. Customer Agent doesn’t change consent requirements; it operates within whatever consent you’ve collected.
- ****Regional rules**** — WhatsApp business messaging is regulated by country. Confirm your messaging complies with local rules wherever your shoppers are.
- ****Data handling**** — Conversations are stored against the Klaviyo profile of the shopper, when one exists. See **Getting started with Customer Agent** for security details.

****This information is not legal advice. Consult your legal counsel for guidance on applicable laws.****

## Troubleshooting

****Symptom:**** Meta verification was rejected.
****Likely cause:**** Business profile information doesn’t match Meta’s requirements, or the phone number isn’t eligible.
****Fix:**** Review Meta’s [Business Verification requirements](https://www.facebook.com/business/help/2058515294227817). Update your business profile and resubmit. WhatsApp setup is handled in [klaviyo.com/settings/whatsapp](https://www.klaviyo.com/settings/whatsapp/).

****Symptom:**** A template wasn’t approved.
****Likely cause:**** Template content includes prohibited language, marketing copy, or doesn’t fit a recognized category.
****Fix:**** Review Meta’s template guidelines. Edit and resubmit.

****Symptom:**** Customer Agent isn’t replying on WhatsApp.
****Likely cause:**** Channel hasn’t been turned on, the shopper is in an excluded segment, or the conversation started before Customer Agent went live.
****Fix:**** Confirm the WhatsApp channel is on in ****Customer Agent > Launch > WhatsApp****. Check audience settings. Customer Agent only responds to messages received after activation.

****Symptom:**** Customer Agent responded but the message didn’t deliver to the shopper.
****Likely cause:**** Outside-window response without a matching template, or a delivery issue on Meta’s side.
****Fix:**** Confirm an approved template is available for the response type. Check WhatsApp delivery status in [klaviyo.com/settings/whatsapp](https://www.klaviyo.com/settings/whatsapp/).

## FAQ

****Can I use the same phone number as my existing business line?****
A WhatsApp Business number must be used exclusively with WhatsApp. You can’t share a number that’s actively used for voice calls or SMS in another system.

****Can Customer Agent on WhatsApp work alongside web chat, email, and SMS?****
Yes. Each channel is configured separately and they can run in any combination.

****What happens if a shopper messages outside business hours?****
Customer Agent responds 24/7. If you want different behavior outside business hours, configure handoff settings or escalation rules accordingly.

****Are there per-region message limits?****
Yes — Meta and your local regulations may impose limits. Check Meta’s WhatsApp Business policies for your region.

## Next steps

- ****Test on WhatsApp**** — send messages to your business number and confirm Customer Agent responds as expected
- ****Monitor performance**** on the Performance dashboard
- ****Iterate on Guidance and content**** based on what you see in real conversations
