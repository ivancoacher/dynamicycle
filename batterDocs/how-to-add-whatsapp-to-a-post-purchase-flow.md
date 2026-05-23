<h1>How to add WhatsApp to a post-purchase flow</h1>

Learn how to add WhatsApp messages to your thank you or order confirmation flow.

Adding WhatsApp to your post-purchase flow lets you reach customers immediately after they buy. You can confirm their order, set expectations, and strengthen engagement using a different channel than email.

## What is a post-purchase flow?

A post-purchase flow sends after someone makes a purchase. This is a broad category that includes:

- Thank you
- Order confirmation
- Cross-sell
- Up-sell
- Product review
- Replenishment

## Before you begin

Before adding WhatsApp to a flow:

- Make sure WhatsApp is set up in your account.
- Create a thank you or order confirmation flow if you do not already have one.

## Add a WhatsApp message to an existing flow

Follow these steps to add WhatsApp to your post-purchase flow without restructuring your email path.

1. Navigate to the ****Flows**** tab.
2. Click the name of the thank you or order confirmation flow where you want to include WhatsApp.
3. In the flow builder, place a conditional split after the first time delay (if there is one) or directly after the trigger.
4. Configure the split to check for WhatsApp consent. This allows you to add WhatsApp to the flow without rearranging your existing email path.
5. On the NO path, add a WhatsApp message.
6. Click ****Configure Content**** in the left sidebar.
7. Add your message content. For example:

   “Hey {{ first\_name|title|default:'there' }}, thank you for your purchase. We hope you're getting excited for your order to arrive.”
8. Drag the rejoin icon below the WhatsApp message onto the email path after the first email. This allows customers to continue receiving emails after the WhatsApp message.
9. Set the WhatsApp message to live.

## Best practices for thank you and order confirmation flows

### Message content

Keep your WhatsApp messages short and clear. Thank the customer directly and include relevant order information.

Avoid overusing emojis. One or two emojis can work well, but repeated emojis are often associated with spam.

### Number of WhatsApp messages

For thank you and order confirmation flows, use only one WhatsApp message. Typically, a single message per recipient is enough.

If you want to send multiple follow-ups, send WhatsApp first and then use email for additional messages.

### Message timing

Send the first WhatsApp message immediately after the purchase.

If you plan to send another message:

- Message 1: No delay
- Message 2: 3 days

Do not send email and WhatsApp messages at the same time. Too many messages at once can overwhelm customers and increase unsubscribes. Alternate between channels instead.

## Enhance your WhatsApp post-purchase flow

You can customize your flow using splits to tailor messaging.

### Order value split

Add a trigger split with the condition **$value > is at least > 100**. Replace 100 with your preferred threshold.

In both the YES and NO paths, add conditional splits to check for WhatsApp consent. Then add your email and WhatsApp messages accordingly.

### Order collection split

Add a trigger split with the condition **Collections > contains > CollectionName**. Replace “CollectionName” with the collection you want to target. You can add multiple splits for different collections.

In both the YES and NO paths, add conditional splits to check for WhatsApp consent. Then add your email and WhatsApp messages accordingly.

### New vs. returning customers

Add a conditional split with the condition **What someone has done (or not done) > Placed Order > Zero Times > over all time**.

In both the YES and NO paths, add conditional splits to check for WhatsApp consent. Then add your email and WhatsApp messages accordingly.

## Next steps

After adding WhatsApp to your post-purchase flow:

1. Test the flow to confirm messages send as expected.
2. Review timing and spacing between WhatsApp and email messages.
3. Personalize your WhatsApp content using profile properties to improve engagement.
