<h1>How to add SMS to your abandoned cart flow</h1>

## You will learn

Learn how to add SMS to your abandoned cart flow as well as compliance requirements and best practices.

## Before you begin

Note that using quiet hours is highly encouraged for SMS abandoned cart reminders. This is on by default in Klaviyo for SMS, and we do not recommend turning it off.

The US has certain requirements for anyone sending SMS messages in abandoned cart flows. If you are sending to US recipients, the following are all required:

- Use double opt-in when collecting SMS consent.
- Only send 1 SMS per recipient.
- Send within 48 hours of someone abandoning a cart.

## Create an SMS abandoned cart flow

Here, we walk you through how to add SMS to your existing abandoned cart flow.

Please read the Before you begin section before setting up your SMS abandoned cart flow, as it contains critical information on SMS compliance and best practices.

****Don’t already have an abandoned cart flow? Open this section.****

1. Navigate to ****Flows****.
2. Click ****Browse Ideas**** in the upper right corner.
3. Search for “abandoned cart” and click the icon for email and SMS.
   ![Searching for an abandoned cart template with both email          and SMS](https://klaviyo.zendesk.com/hc/article_attachments/28722597618843)
4. Pick an abandoned cart flow template.
   1. Here, we choose the template named “Standard (Email & SMS).”
5. Name the flow (e.g., “Abandoned Cart Reminder”).
   ![Preview of an abandoned cart flow template where you can          name the flow](https://klaviyo.zendesk.com/hc/article_attachments/28722559225499)
6. Click ****Create Flow****.
7. If you're using [Amazon Buy with Prime and have integrated it with Klaviyo](https://klaviyo.zendesk.com/hc/en-us/articles/14708088221467), add the following flow filter to exclude customers who made purchases via Buy with Prime from receiving incorrect messaging:

   - **Placed Order** (Buy with Prime) **zero times since starting this flow.**
8. Go into each message and edit the text

   1. Dynamic variables must be formatted exactly right or they won’t work.
   2. Copying the block allows you to make changes without the risk of breaking them.

   - Note: Before changing anything about the dynamic variables, copy the variable or block of variables.
9. Save your changes.
10. Do not turn off quiet hours for the SMS message.
11. Click ****Update Action Statuses**** in the upper right.
12. Open the dropdown menu and select ****Live****.
13. Click ****Update Statuses****.

### Add SMS to an abandoned cart flow

1. Navigate to ****Flows****.
2. Find the abandoned cart flow where you want to include SMS.
3. In the flow, place a conditional split after the first time delay.
   1. Note: the time delay must be within 48 hours of when the flow triggers.
4. Use the following condition.
   **If someone can or cannot receive marketing >** Person **cannot receive > sms marketing.**
   ![Placing a conditional split after the first time delay in an abandoned cart    flow](https://klaviyo.zendesk.com/hc/article_attachments/28722597626011)
5. On the No path, add an SMS message.
   ![Adding an SMS to the No path for a conditional split](https://klaviyo.zendesk.com/hc/article_attachments/28722559236763)
6. Click on the SMS message card.
7. Click ****Edit**** in the details panel.
8. Add in your message.
   “Hey {{ person|lookup:"first\_name"|default:'there' }}, your cart is about to expire! Did you want to check it out? [LINK]”
9. Recommended: Include a discount to encourage people to buy.
   “Hey {{ person|lookup:"first\_name"|default:'there' }}, your cart is about to expire! Get 10% off now with code {% coupon\_code 'YOUR\_COUPON' %} [LINK]”
   ![Example of an abandoned cart flow message that includes a 10% coupon](https://klaviyo.zendesk.com/hc/article_attachments/28722597622811)
10. Rejoin the split after the SMS to after the first email.
    ![Rejoining the split after the first email and SMS in an abandoned cart    flow](https://klaviyo.zendesk.com/hc/article_attachments/28722597634331)
11. Set the SMS message to live.

![Changing an SMS message from draft to live](https://klaviyo.zendesk.com/hc/article_attachments/28722559231515)

## Improve your SMS abandoned cart flow

Above we detail a basic SMS and email abandoned cart flow. However, there are ways you can customize this flow.

While you cannot send more than 1 SMS per recipient as an abandoned cart reminder, you can have more than 1 SMS in this flow by further targeting your audience.

See examples below.

****Skip SMS if product isn't available****

- It keeps the SMS short and concise.
- Unlike with email, an SMS doesn't have a way to dynamically populate the exact number of items someone abandoned.

For that reason, SMS abandonment messages should only show the first item from someone's cart. But what if that product is out of stock?

|  |  |
| --- | --- |
| ****Format**** | ****Example**** |
| `{% catalog event.ProductID unpublished="cancel" %}`  Your message reminding someone of their abandoned cart...  [Link to product]  `{% endcatalog %}` | `{% catalog event.ProductID unpublished="cancel" %}`  Hi Friend!  Did you still want this? Click to shop now:   `{{ event.URL }}`  `{% endcatalog %}` |

****Value split****

![Using a trigger split to send different SMS message to those with carts  below $100](https://klaviyo.zendesk.com/hc/article_attachments/28722559248027)

****Product collection split****

![Using a trigger split to send different SMS message to those purchasing  from a certain collection](https://klaviyo.zendesk.com/hc/article_attachments/28722597641115)

****New purchaser vs. returning customer split****

![Using a conditional split to send different SMS message to new purchasers  versus returning customers](https://klaviyo.zendesk.com/hc/article_attachments/28722597631899)

****Frequent purchaser split****

![Using a conditional split to send different SMS message to more frequent  purchasers](https://klaviyo.zendesk.com/hc/article_attachments/28722597655707)

## Additional resources

- Learn more about [abandoned cart flows](https://help.klaviyo.com/hc/en-us/articles/115002779411-)
- See how to create other SMS flows:
  - [Add SMS to your browse abandonment flow](https://help.klaviyo.com/hc/en-us/articles/15806802249883)
  - [Add SMS to your thank you flow](https://help.klaviyo.com/hc/en-us/articles/15800790306715)
