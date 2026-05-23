<h1>How to create a Tool (Beta)</h1>

> ****Beta feature.**** Creating fully custom tools from scratch is currently in a closed managed beta. If you don’t see a Tools page in Customer Agent, your account doesn’t have beta access yet.

## You will learn

How to connect Customer Agent to any HTTP endpoint using a fully custom tool, write a tool description that Customer Agent will actually use, and test your tool before attaching it to a skill.

## Before you begin

You’ll need:

- Customer Agent enabled and beta access for creating fully custom tools
- An HTTP endpoint you want Customer Agent to call — ****one that does not require secret credentials (API keys, bearer tokens, etc.) to access today**** (authenticated endpoints coming soon, see warning below)
- A skill to attach the tool to — either a skill Customer Agent comes with or a fully custom skill you’ve created

If you haven’t set up a skill yet, create one first. Tools don’t do anything on their own — they have to be attached to a skill.

> ****Warning:**** Secure storage for API keys and other secrets is coming soon. Until it ships, don’t put API keys, bearer tokens, or other sensitive credentials into fully custom tools — tool configuration is not a secure place to store them yet. For now, only use tools with endpoints that are safe to call without secret auth (e.g., internal endpoints behind IP allowlisting, or endpoints that accept non-sensitive identifiers). Support for authenticated endpoints is on the way.

## What a fully custom tool is

A fully custom tool is an HTTP request Customer Agent can make during a conversation. Creating fully custom tools is in beta and available to a limited set of brands while we expand the feature. Use one when the tools Customer Agent comes with don’t cover what you need — for example, looking up an order in your own order management system instead of Shopify, checking inventory in a custom warehouse system, or creating a ticket in a helpdesk Klaviyo doesn’t natively integrate with.

For the underlying concept, see the Understanding Customer Agent tools article.

## When to create a fully custom tool

Reach for a fully custom tool when:

- ****You need real-time data**** from a system Klaviyo doesn’t already integrate with
- ****You want Customer Agent to take an action**** in an external system (cancel a subscription in your proprietary system, create a ticket, update a record)
- ****An existing tool doesn’t fit**** — for example, you use a custom OMS instead of Shopify for orders

If the information doesn’t change often and is the same for every customer, add it as content instead. Tools are for dynamic, per-customer data and actions.

## Set it up

### 1. Open the Tools page

Navigate to ****Customer Agent > Tools****, then click ****Create tool****.

### 2. Name and describe the tool

- ****Name**** — A short identifier like “Get Inventory” or “Create Return Ticket.”
- ****Description**** — Natural language explaining what the tool does and when to use it. Customer Agent reads this description to decide whether to use the tool for a given request. Be specific.

A good description example:

> Fetches real-time inventory count for a given product SKU from the warehouse system. Use when a shopper asks whether a specific product is in stock.

A vague description example (avoid):

> Gets product info.

### 3. Configure the HTTP request

- ****Method**** — GET, POST, PUT, DELETE, or PATCH.
- ****URL**** — The full endpoint URL. You can include placeholders for dynamic values (see Step 5).
- ****Headers**** — Any headers your endpoint requires, including `Content-Type` and authentication headers.

### 4. Configure the request body (for POST, PUT, PATCH)

Provide a JSON body. Use placeholders for values Customer Agent should fill in at runtime.

Example body:

{
"customer\_id": "{{profile\_id}}",
"sku": "{{product\_sku}}"
}

### 5. Use placeholders for dynamic values

Customer Agent can fill in values at runtime using placeholders. Common placeholders:

- `{{profile_id}}` — The Klaviyo profile ID of the customer in the conversation
- `{{conversation_id}}` — The current conversation ID
- Any parameter you define in your input schema (e.g., `{{product_sku}}`, `{{order_id}}`)

Placeholders work in the URL, headers, and body.

### 6. Authentication

Support for authenticated endpoints is coming soon. Until then, don’t put API keys, bearer tokens, or other secrets into a fully custom tool. Only use endpoints that are safe to call without secret credentials — for example, internal endpoints protected by IP allowlisting, or public endpoints that accept non-sensitive identifiers.

Secure secret storage is on the way, and will unlock authenticated endpoints.

### 7. Test the tool

Click ****Test tool****. Provide sample values for any input parameters. Check that:

- The response comes back successfully
- The response format is what Customer Agent expects
- Any error cases are handled

### 8. Save and attach to a skill

Click ****Save****. To make Customer Agent actually use the tool, open the skill you want to use it and add the tool there.

## Writing a good tool description

The description is the most important field. Customer Agent picks which tool to use based entirely on the description — not the name. Good descriptions:

- Say ****what the tool does**** in one sentence
- Say ****when to use it**** in one sentence
- Are specific about the data returned or action taken

Bad descriptions are vague (“Gets customer info”), too broad (“Handles anything related to orders”), or tell Customer Agent how to behave rather than what the tool does.

## Security considerations

- ****Don’t use fully custom tools for endpoints that require secret credentials yet.**** Support for authenticated endpoints is coming soon. Until it ships, only use endpoints that are safe to call without secret auth.
- ****Use IP allowlisting where possible.**** If your endpoint is internal, restrict access to Klaviyo IP ranges rather than relying on secrets.
- ****Be aware of what data you send.**** Customer Agent passes customer data into the tool based on what the skill instructions tell it to. Review what fields your endpoint receives.
- ****Rate limits.**** If your endpoint has rate limits, make sure they’re high enough to handle your expected conversation volume.

## Troubleshooting

****Symptom:**** Customer Agent never uses the tool.
****Likely cause:**** The description is too vague, or the tool isn’t attached to the skill that would use it.
****Fix:**** Rewrite the description to specifically describe when it should be used. Confirm the tool appears in the skill’s tool list.

****Symptom:**** The tool returns an error during testing.
****Likely cause:**** Wrong URL, malformed body, or a payload your endpoint doesn’t accept.
****Fix:**** Use the Test tool feature to check the raw request and response. Verify URL and body format against your endpoint’s expected input.

****Symptom:**** Customer Agent uses the tool but passes wrong parameters.
****Likely cause:**** The placeholder names don’t match the schema, or the skill instructions are unclear about what to pass.
****Fix:**** Check placeholder names match exactly. Update skill instructions to be explicit about when to use the tool and what parameters to provide.

****Symptom:**** The tool is slow, causing delays in responses.
****Likely cause:**** Endpoint latency.
****Fix:**** Optimize your endpoint. Check whether you can cache results on your side.

## FAQ

****Can one tool be used by multiple skills?****
Yes. Once created, a tool can be attached to any number of skills.

****What auth methods are supported?****
Support for authenticated endpoints is coming soon. For now, use endpoints that don’t require secret credentials (internal endpoints with IP allowlisting, or public endpoints with non-sensitive identifiers).

****What happens if my endpoint is down or returns an error?****
Error handling for fully custom tools isn’t built out yet. If your endpoint fails, Customer Agent may produce a degraded or confusing response. Until error handling ships, only use endpoints you’re confident in — and monitor tool behavior closely.

****Can I edit a tool after creating it?****
Yes. You can edit the name, description, configuration, and attached skills at any time.

****Can I version a tool?****
Versioning isn’t supported yet. Edits to a tool take effect immediately across every skill that uses it.
