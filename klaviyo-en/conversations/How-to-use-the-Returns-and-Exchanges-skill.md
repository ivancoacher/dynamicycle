---
id: 46881399074331
title: "How to use the Returns and Exchanges skill"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/46881399074331-How-to-use-the-Returns-and-Exchanges-skill"
section: "Customer Agent"
category: "Conversations"
category_slug: "conversations"
klaviyo_updated: "2026-04-21T13:55:02Z"
language: en
---

## You will learn

How the Returns & Exchanges skill lets Customer Agent guide shoppers through return and exchange requests automatically. When your prerequisites are in place, the agent answers policy questions, checks order eligibility, and deep-links customers directly into your returns portal. This reduces support ticket volume, improves resolution rate, and delivers a faster post-purchase experience that raises CSAT.

## Before you begin

You need the following before you can use the Returns & Exchanges skill:

- ****Customer Agent**** enabled on your account.
- ****Customer Hub**** active and configured.
- A ****connected returns provider**** (e.g., Loop or Aftership) integrated through Customer Hub.
- ****Knowledge base content**** about your return and exchange policies uploaded to Customer Agent content.
- At least one active channel (****webchat****, ****test messaging****, ****email****, or ****WhatsApp****) configured for Customer Agent.

****Note:**** Without Customer Hub or a connected returns provider, the agent searches for content you've uploaded about your return policy.

## Overview

The Returns & Exchanges skill lets Customer Agent handle the most common post-purchase support requests without human intervention. When a customer asks about a return, exchange, or refund, the agent:

1. Searches your content for return and exchange policy answers.
2. Authenticates the customer and retrieves their profile.
3. Checks order status to confirm eligibility.
4. Presents a direct link or action card so the customer can start the return or exchange in your connected returns portal.

****When to use this skill****

This skill is ideal if your brand receives a high volume of return and exchange inquiries and you want to:

- Deflect repetitive tickets from your support team.
- Give customers instant, 24/7 access to return and exchange workflows.
- Improve resolution rate by removing friction between the question and the action.

  ****How it works by channel****
- ****Webchat:**** The agent displays an order card with a ****Start a Return**** button that deep-links to the returns portal.
- ****Text messaging & WhatsApp:**** The agent sends a deep link to the returns portal via Customer Hub.
- ****Email:**** The agent sends a deep link to the returns portal via Customer Hub.

## Set it up

### Step 1: Verify prerequisites

1. Confirm that Customer Agent is enabled on your account.
2. Navigate to ****Customer Hub**** and confirm it is active.
3. Confirm that a returns provider (e.g., Loop or Aftership) is connected in Customer Hub.

### Step 2: Upload return and exchange policy content

1. Navigate to ****Customer Agent > Content****.
2. Click ****Add content****.
3. Upload or enter your return and exchange policies. Include details such as return window, eligible items, exchange process, and refund timelines.
4. Note: if this information is already on your website, the Agent may have access to it already. You can verify by asking questions in the ****Agent Preview**** tab.
5. Click ****Save****.

For detailed guidance, see [How to manage Customer Agent content](https://help.klaviyo.com/hc/en-us/articles/37659457059739).

### Step 3: Confirm the skill is active

1. Navigate to ****Customer Agent > Skills****.
2. Locate the ****Returns & Exchanges**** skill in the skills list. It is active by default when your prerequisites are met.
3. Confirm the status shows ****Live****. If it shows ****Unavailable****, check that Customer Hub is active and a returns provider is connected.

![](https://klaviyo.zendesk.com/hc/article_attachments/46881389434779)

### Step 4: Review skill details

1. Click on the ****Returns & Exchanges**** skill to open its detail page.
2. Review the overview, response behavior, and connected tools.

![](https://klaviyo.zendesk.com/hc/article_attachments/46881389437211)

### Step 5: Test the experience

1. Navigate to the ****Agent Preview**** tab to test your Customer Agent.
2. Ask a returns-related question, such as "How do I start a return?" or "What's your return policy?"
3. Verify that the agent responds with policy information and, after authentication, presents the order card or deep link.

## Best practices

- ****Keep your return policy content up to date.**** The agent pulls answers directly from your knowledge base. Outdated content leads to incorrect responses and erodes customer trust.
- ****Include edge cases in your knowledge base.**** Add content covering non-returnable items, final sale categories, and international return procedures so the agent can handle these questions without a handoff.
- ****Set clear return window expectations.**** Specify the exact return window (e.g., 30 days from delivery) in your policy content so the agent can accurately determine eligibility.
- ****Configure handoff messages thoughtfully.**** When the agent cannot complete a request (e.g., no returns provider connected), a well-written handoff message reassures the customer that a human agent will follow up.
- ****Monitor resolution rate weekly.**** A drop in resolution rate may indicate policy content gaps or configuration issues. Check your knowledge base and returns provider connection if you see a decline.
- ****Use both webchat and SMS channels.**** Enabling both channels maximizes coverage and lets customers use whichever channel they prefer.

## Troubleshooting

****Symptom:**** The agent hands off to a human agent immediately instead of answering the return question.

****Likely cause:**** Customer Hub is not active or no returns provider is connected.

****Fix:**** Navigate to ****Customer Hub**** and confirm it is active with a connected returns provider (e.g., Loop or Aftership). If Customer Hub is not available, the agent will always perform a soft handoff.

****Symptom:**** The agent cannot access order details for the customer.

****Likely cause:**** The customer is not signed in, or the sign-in flow is not configured.

****Fix:**** Confirm that Customer Hub sign-in is enabled. The agent prompts customers to log in before accessing order-specific information. If the prompt is not appearing, check your Customer Hub authentication settings.

****Symptom:**** The agent says the order is not eligible for return, but the customer believes it should be.

****Likely cause:**** The order is outside the return window configured in your returns provider, or the item category is excluded.

****Fix:**** Check the order in your returns provider dashboard to confirm eligibility. Update your return policy content in ****Customer Agent > Content**** if the policy has changed. The agent uses both the knowledge base and order status to determine eligibility.

****Symptom:**** The "Start a Return" button or deep link does not appear after the agent confirms eligibility.

****Likely cause:**** The returns provider integration may be misconfigured, or the order ID could not be validated against the customer's profile.

****Fix:**** Verify the returns provider connection in Customer Hub. Confirm that the Shopify order data is syncing correctly. Test with a known valid order.

****Symptom:**** The agent provides incorrect policy information.

****Likely cause:**** The knowledge base content is outdated or missing key policy details.

****Fix:**** Navigate to ****Customer Agent > Content**** and update your return and exchange policy documents. The agent can only answer based on what is in your knowledge base.

## FAQ

****Does the agent process returns directly?**** No. The agent guides customers to your returns portal by providing direct links and action cards. The actual return or exchange is processed through your connected returns provider (e.g., Loop or Aftership).

****What happens if a customer asks about a refund status?**** Refund status inquiries are routed to the Returns & Exchanges skill. The agent checks the order and return status in your connected systems and provides the customer with the latest information.

****Can I use this skill without Customer Hub?**** The skill is available without Customer Hub, but it operates in a limited mode. Without Customer Hub, the agent shares policy information from your knowledge base and then performs a soft handoff to a human agent for any account-specific actions.

****Which returns providers are supported?**** Customer Hub supports Loop and Aftership as returns providers. Connect your provider through Customer Hub to enable the full self-service returns flow.

****Is the customer's data secure during this process?**** Yes. The customer must authenticate before the agent accesses any order-specific information. Order IDs are validated against the customer's profile to prevent unauthorized access.

****Does this skill work on all channels?**** The Returns & Exchanges skill is available on webchat and SMS. On webchat, the agent displays an order card with an action button. On SMS, the agent sends a deep link to the returns portal.

## Next steps

- [Understanding Customer Agent skills](https://help.klaviyo.com/hc/en-us/articles/45769973148571)
- [How to set up Customer Hub](https://help.klaviyo.com/hc/en-us/articles/33660324811675)
- [How to manage Customer Agent content](https://help.klaviyo.com/hc/en-us/articles/37659457059739)