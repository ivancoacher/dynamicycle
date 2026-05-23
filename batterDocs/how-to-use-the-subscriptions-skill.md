<h1>How to use the Subscriptions skill</h1>

## You will learn

In this article, you will learn how the Subscriptions skill works for Customer Agent and what you need to get it running. This skill lets your customers pause, cancel, or update their subscription delivery preferences through self-service -- reducing support ticket volume, improving resolution rates, and helping you retain subscribers by making account management frictionless.

## Before you begin

Before you set up the Subscriptions skill, confirm the following:

- ****Customer Agent**** is enabled on your account.
- ****Customer Hub**** is active and configured for your storefront.
- A ****subscription provider**** is connected (e.g., Recharge, Skio). Ordergroove support is planned as a follow-up.
- You have uploaded ****knowledge base content**** about your subscription policies (cancellation rules, modification options, FAQs) in Customer Agent content settings.
- ****Availability:**** The Subscriptions skill works on ****webchat****, ****text messaging****, ****email****, and ****WhatsApp**** channels. All roles can view the skill; ****Admins**** and ****Owners**** can configure it.
- ****Time to complete:**** ~5-10 minutes if prerequisites are in place.

****Important:**** The agent does not directly modify subscriptions. It guides customers to your subscription portal with the right context and links. Without Customer Hub or a connected subscription provider, the agent will perform a soft handoff to a human agent.

****Note:**** The subscription data visible to the agent depends on your provider. Recharge returns active, paused, and canceled subscriptions. Skio returns ****active subscriptions only**** — paused and canceled subscriptions are not available through Skio's API. See [Subscription visibility by provider](#subscription-visibility-by-provider) for details.

## Overview

The Subscriptions skill enables Customer Agent to handle subscription-related inquiries end to end -- from answering policy questions to surfacing authenticated self-service links. Instead of waiting for a human agent, customers can get immediate guidance on how to pause, cancel, change frequency, swap products, or update payment and shipping details.

### When to use this skill

Customer Agent will use the Subscriptions skill when your customers ask questions like:

- "How do I cancel my subscription?"
- "I want to update my delivery frequency."
- "Is my subscription still active?"
- "Can I change the products in my subscription?"
- "How do I update my payment info?"

### How it differs from adjacent skills

- ****Returns and Exchanges skill**** -- Handles post-purchase return and exchange requests for one-time orders. The Subscriptions skill focuses specifically on recurring subscription management.
- ****Order Editing skill**** -- Handles changes to one-time orders before fulfillment. The Subscriptions skill covers ongoing subscription modifications.
- ****General Q&A skill**** -- Answers general brand questions from your knowledge base without requiring authentication. The Subscriptions skill combines knowledge base answers with authenticated, account-specific subscription data.

### Subscription visibility by provider

The agent surfaces all subscription statuses it receives from your provider. However, each provider's API returns different data:

| Provider | Active | Paused | Canceled |
| --- | --- | --- | --- |
| ****Recharge**** | Yes | Yes | Yes |
| ****Skio**** | Yes | No | No |
| ****Ordergroove**** | Planned | Planned | Planned |

- ****Recharge**** returns active, paused, and canceled subscriptions. The agent can answer questions about all subscription states and display cards for each.
- ****Skio**** returns ****active subscriptions only****. If a customer asks about a paused or canceled subscription, the agent cannot retrieve it and may report that no subscription was found. Consider adding knowledge base content that explains how customers can contact support for questions about non-active Skio subscriptions.
- ****Ordergroove**** integration is planned as a follow-up.

### How the agent handles a subscription inquiry

1. A customer asks about subscriptions (e.g., "How do I pause my subscription?").
2. The agent searches your knowledge base for subscription policies using ****Klaviyo - Search content****.
3. If the question is account-specific, the agent checks whether the customer is signed in. If not, it prompts the customer to log in.
4. Once signed in, the agent retrieves the customer's profile using ****Klaviyo - Get profile****.
5. The agent makes a read-only tool call to check subscription status, confirming enrollment and current plan details. This prevents the agent from rendering empty subscription cards for customers without active subscriptions.
6. The agent presents a direct link or button to manage the subscription:

   - ****On webchat:**** A subscription card or carousel displaying subscription details and a link to the subscription portal.
   - ****On text messaging and WhatsApp:**** A link to the Customer Hub "For You" page where the customer can manage their subscription.
   - ****On email:**** A link to the Customer Hub "For You" page with a brief response.
7. The agent clearly communicates the available actions (pause, cancel, update frequency, change products, edit payment or shipping details).

## Set it up

### Step 1: Connect your subscription provider

1. From **Settings Integrations**, confirm that your subscription provider (e.g., Recharge or Skio) is connected and active. Expected result: The integration status shows ****Connected****.

****Note:**** If you do not have a subscription provider connected, the Subscriptions skill will not be available. The agent will instead perform a soft handoff to a human agent for subscription inquiries.

### Step 2: Verify Customer Hub is active

1. From **Customer Hub Settings**, confirm that Customer Hub is enabled and your storefront is connected. Expected result: Customer Hub status shows ****Active****.

[Screenshot: Customer Hub settings page showing active status]

### Step 3: Upload subscription knowledge base content

1. Navigate to **Customer Agent Content**.
2. Upload or verify that your subscription policy documents are included. These should cover:

- Cancellation policies and any required notice periods
- Pause and skip options
- Frequency change rules
- Product swap or add-on policies
- Payment and shipping update procedures

Expected result: Your subscription-related content appears in the content library and is available for the agent to search.

****Tip:**** The more specific and complete your subscription policy content is, the better the agent can answer questions before needing to route customers to the portal.

### Step 4: Confirm the skill is active

1. Navigate to **Customer Agent Skills**.
2. Locate the ****Subscriptions**** skill in the skills list. It is active by default when your prerequisites are met.
3. Confirm the status shows ****Live****. If it shows ****Unavailable****, check that Customer Hub is active and a subscription provider is connected.

Expected result: The Subscriptions skill shows ****Live**** status in your skills overview.

[Screenshot: Skills overview page showing Subscriptions skill with Live status]

### Step 5: Test the skill

1. Open a test conversation on your webchat, text messaging, email, or WhatsApp channel.
2. Ask a subscription-related question (e.g., "How do I cancel my subscription?").
3. Verify that the agent responds with policy information and, after sign-in, presents a subscription card (webchat) or a link to Customer Hub (text messaging, WhatsApp, email).

Expected result: The agent provides accurate policy information and a working link to manage subscriptions.

[Screenshot: Webchat showing subscription card with subscription details and manage link]

## Best practices

- ****Keep subscription policy content up to date**** -- Review and refresh your knowledge base content whenever you change subscription terms. Outdated policies lead to incorrect agent responses and customer frustration. Impact: resolution rate, customer satisfaction.
- ****Cover all common scenarios in your knowledge base**** -- Include content for pausing, canceling, frequency changes, product swaps, and payment updates. The more scenarios the agent can answer from content alone, the fewer escalations to human agents. Impact: ticket deflection, resolution rate.
- ****Configure handoff messaging for edge cases**** -- Set clear handoff instructions so that when the agent cannot resolve a subscription issue (e.g., no subscription provider connected), the customer receives a helpful message and a smooth transition to a human agent. Impact: customer satisfaction.
- ****Use the skill alongside Returns and Exchanges**** -- Customers who want to cancel a subscription may actually prefer a pause or product swap. Both skills activate automatically when their prerequisites are met, so the agent can suggest alternatives. Impact: subscription retention.
- ****Promote self-service in proactive messaging**** -- Let subscribers know they can manage their subscription through any of your Customer Agent channels (webchat, text messaging, email, or WhatsApp). Include a note in subscription confirmation emails or renewal reminders. Impact: ticket deflection, customer satisfaction.

## Measure success

### Where to view results

- Navigate to **Customer Agent Performance** to see conversation volume, resolution rate, and handoff rate for subscription-related inquiries.
- Review ticket deflection trends in your helpdesk or support platform by comparing subscription-related ticket volume before and after enabling the skill.

### Key metrics to watch

| Metric | What it tells you |
| --- | --- |
| ****Resolution rate**** | Percentage of subscription inquiries the agent resolves without human handoff |
| ****Ticket deflection**** | Reduction in subscription-related support tickets |
| ****Subscription retention**** | Whether self-service management reduces churn vs. increases cancellations |
| ****Handoff rate**** | How often the agent escalates to a human agent -- lower is better |

### If metrics are low, try these fixes

- ****Low resolution rate**** -- Add more detailed subscription policy content to your knowledge base. Check that your subscription provider integration is active and returning data correctly.
- ****High handoff rate**** -- Review handoff triggers. Ensure Customer Hub and your subscription provider are properly connected so the agent can serve self-service links.
- ****No change in ticket deflection**** -- Promote the self-service channel to existing subscribers. Check that your webchat, text messaging, email, or WhatsApp channels are accessible from the pages where customers typically seek subscription help.

## Troubleshooting

****Symptom:**** The agent does not display subscription details and hands off to a human agent immediately.
****Likely cause:**** Customer Hub is not active, or no subscription provider is connected.
****Fix:**** Navigate to **Customer Hub Settings** and confirm Customer Hub is enabled. Then check **Settings Integrations** to verify your subscription provider (e.g., Recharge) shows a ****Connected**** status. Once both are active, the Subscriptions skill will automatically become available.

---

****Symptom:**** The agent says "No active subscription found" even though the customer has a subscription.
****Likely cause:**** The customer is not signed in, or the customer's email in Klaviyo does not match the email associated with the subscription provider account.
****Fix:**** Ensure the customer completes the sign-in flow. Verify that the email address on the Klaviyo profile matches the subscription provider account. If there is a mismatch, the customer may need to update their email in one of the systems, or a human agent can assist.

---

****Symptom:**** A customer asks about a paused or canceled subscription, but the agent says no subscription was found.
****Likely cause:**** Your account uses Skio as a subscription provider. Skio's API only returns active subscriptions — paused and canceled subscriptions are not available to the agent.
****Fix:**** This is a known limitation of Skio's API. Add knowledge base content that instructs the agent to direct customers with paused or canceled Skio subscriptions to contact your support team or visit the subscription portal directly. If you need full visibility into all subscription states, Recharge provides active, paused, and canceled subscription data.

---

****Symptom:**** The subscription portal link in the agent response leads to a broken page or 404 error.
****Likely cause:**** The subscription portal URL configured in Customer Hub is incorrect or outdated.
****Fix:**** Navigate to **Customer Hub Settings** and verify the subscription portal URL. Test the link directly in a browser to confirm it resolves. Update the URL if your subscription provider has changed their portal path.

---

****Symptom:**** The agent answers subscription policy questions but never prompts the customer to sign in or shows a subscription card.
****Likely cause:**** The agent is treating the inquiry as a general knowledge base question rather than an account-specific subscription request.
****Fix:**** Review the customer's message phrasing. The agent distinguishes between general policy questions ("What is your cancellation policy?") and account-specific requests ("I want to cancel my subscription"). For account-specific requests, the agent should prompt sign-in. If it does not, check that the Subscriptions skill shows ****Live**** status in **Customer Agent Skills** and that your subscription provider is connected.

---

****Symptom:**** On text messaging or WhatsApp, the customer receives a text-only response with no link to Customer Hub.
****Likely cause:**** The customer is not signed in, or Customer Hub is not configured for your account.
****Fix:**** Confirm that Customer Hub is active and supports your subscription provider. Ensure the customer completes authentication before the agent attempts to retrieve subscription data. On text messaging and WhatsApp, the agent links to the Customer Hub "For You" page when subscriptions are found.

## FAQ

****Q: Can the agent directly cancel or pause a subscription on behalf of the customer?****
****A:**** No. The agent provides read-only access to subscription data and guides customers to the subscription portal where they can take action themselves. This design ensures that subscription modifications go through the provider's standard workflow, preserving any confirmation steps or retention offers you have configured.

****Q: Which subscription providers are supported?****
****A:**** Recharge and Skio are supported at launch. Ordergroove integration is planned as a follow-up. Your subscription provider must be connected through Klaviyo's integrations and linked to Customer Hub.

****Q: Can the agent see paused and canceled subscriptions?****
****A:**** It depends on your provider. Recharge returns active, paused, and canceled subscriptions, so the agent can surface all of them. Skio only returns active subscriptions through its API — the agent cannot retrieve paused or canceled Skio subscriptions. If you use Skio, add knowledge base content to help the agent guide customers with non-active subscriptions to your support team or portal.

****Q: Does the customer need to be signed in for the agent to help with subscriptions?****
****A:**** For general policy questions (e.g., "What is your cancellation policy?"), no sign-in is required -- the agent answers from your knowledge base. For account-specific requests (e.g., "I want to pause my subscription"), the agent prompts the customer to sign in so it can retrieve their subscription details and provide a personalized self-service link.

****Q: What happens if a customer asks about subscriptions but does not have one?****
****A:**** After the customer signs in, the agent checks for active subscriptions. If none are found, the agent informs the customer that no active subscription is associated with their account and offers to help with other questions.

****Q: Is the Subscriptions skill available on all channels?****
****A:**** The Subscriptions skill is available on ****webchat****, ****text messaging****, ****email****, and ****WhatsApp****. On webchat, the agent displays a subscription card or carousel with details and a manage link. On text messaging and WhatsApp, the agent provides a link to the Customer Hub "For You" page. On email, the agent sends a brief response with a link to Customer Hub.

****Q: What data does the agent access when checking subscriptions?****
****A:**** The agent makes a read-only API call to retrieve subscription status, plan details, and enrollment information. It does not have write access and cannot modify any subscription data. The customer must authenticate before any account-specific data is accessed.

## Next steps

- ****Set up Customer Hub**** to ensure your customers have a self-service portal for managing subscriptions, orders, and account details.
- ****Connect your returns provider**** so the Returns and Exchanges skill activates and the agent can handle a broader range of post-purchase inquiries alongside subscriptions.
- ****Upload comprehensive knowledge base content**** covering all subscription scenarios to maximize the agent's resolution rate.
- ****Configure Customer Agent handoffs**** to define how and when subscription inquiries escalate to human agents.
- ****Review your subscription analytics**** after one to two weeks to identify gaps in content or configuration.

## Additional resources

- Understanding Customer Agent skills
- How to set up Customer Hub
- How to manage Customer Agent content
- How to use the Returns and Exchanges skill
- How to configure Customer Agent handoffs
- Getting started with Customer Agent
