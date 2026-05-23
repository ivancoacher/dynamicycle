<h1>How to use the Loyalty skill</h1>

## You will learn

How the Loyalty skill lets Customer Agent answer loyalty and rewards questions automatically. Your customers can check their points balance, discover available rewards, and learn about your loyalty program — all without opening a support ticket. The Loyalty skill deflects repetitive loyalty inquiries, increases program engagement, and improves customer satisfaction by giving shoppers instant, self-service answers across webchat, text messaging, email, and WhatsApp.

## Before you begin

You need the following before you can use the Loyalty skill:

- ****Customer Agent**** enabled on your account.
- ****Customer Hub**** active with a connected loyalty provider (e.g., Yotpo or Smile.io).
- ****Knowledge base content**** about your loyalty program uploaded to Customer Agent (earning rules, redemption options, program tiers, FAQs).
- At least one active channel (****webchat****, ****text messaging****, ****email****, or ****WhatsApp****) configured for Customer Agent.
  > ****Note:**** Without Customer Hub or a connected loyalty provider, the agent searches for content you've uploaded about your loyalty program. For account-specific questions, the agent performs a soft handoff to a human agent.
- ****Availability:**** Available to all Customer Agent customers. Available on webchat, text messaging, email, and WhatsApp channels. All account roles can view the skill; ****Admins**** and ****Owners**** can configure it.
- ****Time to complete:**** ~5 minutes to enable the skill (assumes Customer Hub and loyalty provider are already connected).
- ****Important:**** The agent cannot redeem rewards directly on behalf of a customer. It provides deep links to the loyalty portal in Customer Hub where customers complete redemption themselves.

## Overview

The Loyalty skill lets Customer Agent answer loyalty and rewards questions automatically. It handles two categories of inquiries:

- ****General questions**** (no authentication required) — Program details, earning rules, redemption options, tier explanations, and how to join. The agent answers these from your uploaded knowledge base content.
- ****Account-specific questions**** (authentication required) — Points balance, enrollment status, and available rewards. After the customer signs in, the agent presents a loyalty card or deep link so the customer can view and manage their rewards.

  ****When to use this skill****

  Customer Agent uses the Loyalty skill when your customers ask questions like:
- "Do you have a rewards program?"
- "How many points do I have?"
- "How do I redeem my rewards?"
- "When do my points expire?"

  ****How it works by channel****
- ****Webchat:**** The agent displays a loyalty points card showing enrollment status, points balance, and redemption information.
- ****Text messaging & WhatsApp:**** The agent sends a deep link to the loyalty section in Customer Hub.
- ****Email:**** The agent sends a brief response with a deep link to the loyalty section in Customer Hub.

  ****How it differs from adjacent skills****
- ****Subscriptions skill**** — Handles subscription management (pause, cancel, update). The Loyalty skill focuses specifically on loyalty programs and rewards.
- ****General Q&A skill**** — Answers general brand questions from your knowledge base without requiring authentication. The Loyalty skill combines knowledge base answers with authenticated loyalty card presentation for account-specific data.

The Loyalty skill works alongside other Customer Agent skills. The agent automatically routes to the right skill based on the customer's question.

## Set it up

### Step 1: Verify prerequisites

1. Confirm that Customer Agent is enabled on your account.
2. Navigate to ****Customer Hub**** and confirm it is active.
3. Confirm that a loyalty provider (e.g., Yotpo or Smile.io) is connected in Customer Hub.

****Note:**** If Customer Hub is not active or no loyalty provider is connected, the skill shows ****Unavailable**** status and the agent performs a soft handoff to a human agent for loyalty questions instead of answering directly.

### Step 2: Upload loyalty program content

1. Navigate to ****Customer Agent Content****.
2. Click ****Add content****.
3. Upload or enter your loyalty program details. Include:

   - How to earn points (purchases, referrals, social shares, etc.)
   - How to redeem rewards (discount codes, free products, etc.)
   - Program tiers and benefits (if applicable)
   - Enrollment instructions
   - Point expiration policies
4. Click ****Save****.

> For detailed guidance, see [How to manage Customer Agent content](#).

****Tip:**** The more comprehensive your knowledge base content, the better the agent handles general loyalty questions without needing authentication.

### Step 3: Confirm the skill is active

1. Navigate to ****Customer Agent Skills****.
2. Locate the ****Loyalty**** skill in the skills list. It is active by default when your prerequisites are met.
3. Confirm the status shows ****Live****. If it shows ****Unavailable****, check that Customer Hub is active and a loyalty provider is connected.

### Step 4: Review skill details

1. Click the ****Loyalty**** skill to open the skill detail page.
2. Review the overview, response behavior, and connected tools.

### Step 5: Test the experience

1. Open your webchat widget or send a test message through text messaging, email, or WhatsApp.
2. Ask a loyalty question (e.g., "How do I earn points?" or "What's my points balance?").
3. Verify that the agent responds with loyalty information from your knowledge base and, after authentication, presents the loyalty card (webchat) or a deep link (text messaging, WhatsApp, email).

****Note:**** For account-specific questions, the customer must sign in. Once authenticated, the agent presents loyalty data including enrollment status, points balance, and available rewards via the loyalty card or a link to Customer Hub.

## Best practices

- ****Keep your knowledge base content up to date**** — Update earning rules, redemption options, and tier details whenever your loyalty program changes. Stale content leads to incorrect answers and frustrated customers. Impact: resolution rate, customer satisfaction.
- ****Upload detailed FAQ content about your loyalty program**** — Cover edge cases like expiration policies, how to combine discounts, and minimum redemption thresholds. Impact: ticket deflection, resolution rate.
- ****Promote Customer Hub enrollment**** — Encourage customers to create Customer Hub accounts so the agent can serve personalized loyalty data immediately. Impact: loyalty program engagement, resolution rate.
- ****Use multiple channels**** — Webchat displays rich loyalty cards; text messaging and WhatsApp send deep links; email sends links with a brief response. Offering multiple channels maximizes reach. Impact: ticket deflection, program engagement.

## Measure success

### Where to view results

Navigate to **Customer Agent Analytics** to view performance data. Click into the ****Loyalty**** skill on the **Customer Agent Skills** page to see skill-level metrics on the ****Performance**** tab.

### Key metrics to watch

| Metric | What it tells you |
| --- | --- |
| ****Resolution rate**** | Percentage of loyalty conversations the agent resolves without human handoff |
| ****Ticket deflection**** | Reduction in loyalty-related support tickets |
| ****Handoff rate**** | How often the agent escalates to a human agent — lower is better |
| ****Loyalty program engagement**** | In your loyalty portal's analytics: Increase in loyalty portal visits and redemptions driven by agent deep links. |

### If metrics are low, try these fixes

- ****Low ticket deflection**** — Review your knowledge base for gaps in loyalty content. Check which questions trigger handoffs and add content to cover them. Ensure Customer Hub is properly connected so account-specific questions resolve automatically.
- ****Low resolution rate**** — Expand knowledge base content with more detailed earning and redemption rules. Confirm your loyalty provider integration is syncing correctly. Check that handoff rules are not overly aggressive, causing unnecessary escalations.
- ****Low loyalty engagement**** — Add enrollment prompts to your knowledge base content for non-enrolled customers. Verify deep links to the loyalty portal are working correctly across all channels. Review conversation logs to ensure the agent is surfacing rewards and redemption options clearly.

## Troubleshooting

****Symptom:**** The agent does not answer loyalty questions and hands off to a human agent immediately.
****Likely cause:**** Customer Hub is not active or no loyalty provider is connected.
****Fix:**** Navigate to Customer Hub settings and confirm that a loyalty provider (e.g., Yotpo or Smile.io) is connected and active. Set up Customer Hub if it is not already active. Once both are in place, the Loyalty skill activates automatically and handles questions directly.

---

****Symptom:**** The agent answers general loyalty questions but cannot show a customer's points balance or rewards.
****Likely cause:**** The customer is not signed in, or the loyalty provider is not syncing profile data.
****Fix:**** Confirm the customer has signed in. The agent should prompt login for account-specific questions automatically. If the customer is signed in but data is missing, check your loyalty provider integration in Customer Hub to ensure profile data is syncing. If the issue persists, have the customer refresh the page and try again.

---

****Symptom:**** The agent provides incorrect or outdated loyalty program details (e.g., wrong earning rules or expired rewards).
****Likely cause:**** Knowledge base content is out of date.
****Fix:**** Update your loyalty program content in **Customer Agent Content**. Remove outdated articles and upload current program details, including earning rules, redemption options, and any recent program changes.

---

****Symptom:**** The loyalty points card does not appear in webchat conversations.
****Likely cause:**** The customer is not authenticated, or the loyalty data could not be retrieved from the provider.
****Fix:**** Ensure the customer is signed in. If they are signed in and the card still does not appear, verify that the loyalty provider integration is active and returning data. Check Customer Hub settings for connection errors. If the problem continues, contact support.

---

****Symptom:**** Deep links to the loyalty portal are not working on text messaging, WhatsApp, or email.
****Likely cause:**** Customer Hub deep links are misconfigured or the loyalty section is not enabled in Customer Hub.
****Fix:**** Verify that Customer Hub is active and the loyalty section is accessible. Test the deep link URL directly in a browser. Confirm that the relevant channel is enabled for Customer Agent.

## FAQ

****Q: Can the agent redeem rewards on behalf of a customer?****
****A:**** No. The agent provides information about available rewards and sends the customer a link to the loyalty portal in Customer Hub, where they can complete redemption themselves. This ensures the customer reviews and confirms any reward selection directly.

****Q: What happens if a customer asks about loyalty but is not signed in?****
****A:**** For general questions (e.g., "How do I earn points?"), the agent answers from your knowledge base without requiring authentication. For account-specific questions (e.g., "How many points do I have?"), the agent prompts the customer to sign in first, then presents their loyalty data via a card or link.

****Q: Which loyalty providers are supported?****
****A:**** The Loyalty skill works with loyalty providers connected through Customer Hub. Yotpo and Smile.io are supported providers. Check Customer Hub documentation for the latest list of supported integrations.

****Q: What happens if a customer is not enrolled in the loyalty program?****
****A:**** The agent provides information about the loyalty program and instructions on how to join. On webchat, it can include a link to the enrollment page in Customer Hub.

****Q: Does the Loyalty skill work on all channels?****
****A:**** Yes. On webchat, the agent displays a rich loyalty points card with enrollment status, points balance, and redemption information. On text messaging and WhatsApp, the agent sends deep links to the loyalty section in Customer Hub. On email, the agent sends a brief response with a deep link. Deep links are available for enrollment, points balance, and points redemption.

****Q: Do I need to create separate knowledge base content for loyalty, or does the agent pull everything from the loyalty provider?****
****A:**** You need both. The loyalty provider supplies account-specific data (points balance, enrollment status, available rewards) displayed via the loyalty card or deep link. Your knowledge base content supplies program details the agent uses to answer general questions — earning rules, redemption options, tier benefits, and FAQs. Upload comprehensive loyalty content for the best results.

## Next steps

- ****Set up Customer Hub**** — If you have not already, connect your loyalty provider and configure Customer Hub to power account-specific loyalty responses.
- ****Connect your loyalty provider**** — Ensure your Loyalty provider is connected to Customer Hub.
- ****Upload loyalty program content**** — Add detailed articles about your earning rules, redemption options, tiers, and FAQs to your Customer Agent knowledge base.
- ****Configure handoff settings**** — Set up handoff paths for edge cases the agent cannot resolve, like disputed balances or manual point adjustments.
- ****Review conversation logs**** — After launch, review loyalty conversations to identify gaps in your knowledge base and improve resolution rates.
