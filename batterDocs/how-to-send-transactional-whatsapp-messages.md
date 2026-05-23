<h1>How to send transactional WhatsApp messages</h1>

Learn how to send transactional WhatsApp messages using approved utility templates.

Transactional WhatsApp messages let you send order confirmations, shipping updates, account alerts, and other non-promotional updates. These messages must use a Meta-approved template categorized as Utility/Transactional.

## Requirements

You must have WhatsApp enabled in your account and an approved WhatsApp template. Your WhatsApp Business account must be connected and approved by Meta.

## Create and categorize your WhatsApp template

Before sending a transactional WhatsApp message, you must create and submit a template for Meta approval.
[Learn how to create and submit a template.](https://help.klaviyo.com/hc/en-us/articles/40116644987675)

### How template categorization works

Meta determines whether your template is categorized as Utility or Marketing during review.

When you submit a template:

- Meta reviews the content.
- Meta assigns the template category.
- Meta may reassign your template to Marketing if it does not meet utility guidelines.

  [Review Meta’s official guidelines before submitting](https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/template-categorization#utility-template-guidelines).

### If your template is reassigned

If Meta reassigns your template to Marketing, you cannot use it for transactional messaging.

To resolve this:

- Create a new template with revised, non-promotional content.
- Submit the new template for review.
- Wait for Meta approval before using it in a transactional flow.

### If you edit an approved template

If you change the content of an approved template:

- You must resubmit it for Meta review.
- The template cannot be used until it is approved again.
- Meta may reassign the category during review.

## Create a transactional WhatsApp flow

Use a flow triggered by an event such as **Placed Order**, **Fulfilled Order**, or another account activity.

If your trigger event syncs through your ecommerce integration, use event data to personalize your template. For example, include:

- Order number
- Product name
- Tracking link
- Shipping status

### Build a flow from scratch

Follow these steps to create a transactional WhatsApp flow:

1. Navigate to the ****Flows**** tab.
2. Click ****Create Flow**** in the upper right.
3. Select ****Build your own****.
4. Choose your trigger event (for example, **Placed Order**).
5. Add a WhatsApp action to the flow.
6. Select your approved Utility template.
7. Map the template variables to event data such as order number or tracking URL.
8. Test the message to confirm variables populate correctly.
9. Set the WhatsApp message to live.

## Best practices for transactional WhatsApp messages

- Keep messages informational and non-promotional.
- Clearly reference the related transaction or account activity.
- Avoid discounts, urgency language, or sales-focused copy.
- Use dynamic event data for clarity and accuracy.

## Next steps

1. Confirm your template shows as approved in Meta.
2. Send a test message using a real event.
3. Monitor delivery and engagement metrics.
4. Review template performance before scaling volume.
