<h1>How to use the Order Editing skill</h1>

## You will learn

- What the Order Editing skill does and how it works with Customer Hub.
- What prerequisites are needed for the skill to be active.
- How the agent guides customers through order modifications and cancellations.
- How to measure ticket deflection and resolution rate.

## Before you begin

You need the following before you can use the Order Editing skill:

- ****Customer Agent**** enabled on your account.
- ****Customer Hub**** active and configured. [How to set up Customer Hub]
- ****Shopify integration**** connected and syncing order data. [TBD: link to Shopify integration article]
- ****Knowledge base content**** about your order modification and cancellation policies uploaded to Customer Agent. [How to manage Customer Agent content]
- ****Admin or Owner role**** to configure the skill. All roles can view skill settings.

The Order Editing skill is available on ****webchat**** and ****SMS**** channels.

## Overview

The Order Editing skill lets Customer Agent handle order modification and cancellation requests automatically. When a customer asks to change or cancel an order, the agent:

1. Searches your knowledge base for your brand's order modification and cancellation policies.
2. Verifies the customer's identity by prompting them to sign in (if not already authenticated).
3. Retrieves the customer's profile and checks order status through your Shopify integration.
4. Determines whether the order is still editable (not yet fulfilled or shipped).
5. Directs the customer to the appropriate next step.

### What happens based on order status

| ****Order status**** | ****Agent behavior**** |
| --- | --- |
| ****Unfulfilled**** (editable) | Presents a direct link or button to edit the order in Customer Hub. |
| ****Partially fulfilled**** | Explains which items can still be modified and guides the customer accordingly. |
| ****Fulfilled / shipped**** | Informs the customer and redirects to the Returns & Exchanges skill. |

### Channel-specific behavior

- ****Webchat:**** Displays an order card with inline editing options and a direct link to Customer Hub.
- ****Text Messaging & WhatsApp:**** Sends a deep link to the Customer Hub order tab where the customer can make changes.
- ****Email:**** Sends a deep link to the Customer Hub order tab where the customer can make changes.

****Important:**** The agent does not directly edit orders. It guides customers to Customer Hub, where they complete the modification themselves. This ensures changes go through your standard order management workflow.

## Set it up

### Step 1: Verify your prerequisites

1. Confirm your Shopify integration is connected and syncing. Navigate to ****Integrations > Shopify**** and check for an active connection.
2. Confirm Customer Hub is active. Navigate to ****Customer Hub**** and verify the setup is complete.

### Step 2: Upload your order policies

1. Go to ****Customer Agent > Content****.
2. Upload or add knowledge base articles that cover:

   - Your order modification policy (e.g., time windows, eligible changes).
   - Your order cancellation policy (e.g., cutoff times, restocking fees).
   - Any product-specific exceptions.
3. Save your changes.

The agent uses this content to provide accurate, brand-specific answers. Without clear policies in your knowledge base, the agent may not be able to give customers definitive guidance.

### Step 3: Confirm the skill is active

1. Go to ****Customer Agent > Skills****.
2. Locate the ****Order Editing**** skill in the skills list. It is active by default when your prerequisites are met.
3. Confirm the status shows ****Live****. If it shows ****Unavailable****, check that Customer Hub is active and Shopify is connected.

### Step 4: Test the experience

1. Go to Customer Agent > Agent Preview to test your Customer Agent.
2. Send a test message like "Can I change the size on my recent order?" or "I need to cancel my order."
3. Verify the agent:

- Prompts you to sign in (if not authenticated).
- Retrieves the correct order.
- Presents a link or card to edit in Customer Hub.

## Best practices

### Write clear, specific order policies

The agent is only as helpful as the content in your knowledge base. Include:

- ****Modification windows.**** State clearly how long after placing an order a customer can make changes (e.g., "Orders can be modified within 1 hour of placement").
- ****Eligible modifications.**** Specify what can be changed: size, color, shipping address, quantity.
- ****Cancellation rules.**** Define cancellation cutoffs, any restocking fees, and refund timelines.
- ****Exceptions.**** Call out product categories or order types that cannot be modified (e.g., personalized items, pre-orders).

### Set expectations for edge cases

Add knowledge base content that addresses:

- What happens if an order is partially shipped.
- How to handle requests to add new items (requires a new order or contacting support).
- When the agent should hand off to a human agent.

### Configure handoffs for unsupported scenarios

If a customer's request falls outside what the Order Editing skill can handle, the agent performs a soft handoff to a human agent. Make sure your handoff configuration is up to date. [How to configure Customer Agent handoffs]

## Troubleshooting

### Agent does not reference your cancellation policy

****Symptom:**** The customer asks about canceling an order, and the agent provides generic guidance instead of your brand's specific policy.

****Likely cause:**** Your knowledge base does not contain cancellation policy content, or the content is not clearly structured for the agent to retrieve.

****Fix:****

1. Go to ****Customer Agent > Content****.
2. Search for your cancellation policy. If it does not exist, add it.
3. Use clear headings and direct language (e.g., "Order Cancellation Policy") so the agent can match the content to customer questions.

## FAQ

****Can the agent directly edit or cancel orders in Shopify?**** No. The agent guides customers to Customer Hub, where they can make changes themselves. The agent does not modify order data directly.

****What happens if a customer wants to add items to an existing order?**** The agent explains that adding items to an existing order is not supported through Customer Hub. It advises the customer to place a new order or contact support for assistance.

****Does Order Editing work without Customer Hub?**** No. Customer Hub is required for the self-service editing experience. Without Customer Hub, the agent performs a soft handoff to a human agent instead of guiding the customer to edit the order.

****Which channels support the Order Editing skill?**** Webchat and SMS. On webchat, the agent displays order cards with inline editing options. On SMS, the agent sends deep links to the Customer Hub order tab.

****Does the customer need to be signed in?**** Yes. The agent requires authentication before retrieving order data. If the customer is not signed in, the agent prompts them to sign in first. This ensures order data is only shared with the verified account holder.

****What if only part of the order has shipped?**** The agent checks fulfillment status at the line-item level. It explains which items can still be modified and which have already shipped. For shipped items, the agent redirects to the Returns & Exchanges skill.

## Next steps

- [****How to manage Customer Agent content****](https://help.klaviyo.com/hc/en-us/articles/37659457059739)
- [****How to set up Customer Hub****](https://help.klaviyo.com/hc/en-us/articles/33660324811675)
- [****Understanding Customer Agent skills****](https://help.klaviyo.com/hc/en-us/articles/45769973148571)
