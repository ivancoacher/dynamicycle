<h1>How to create a post-purchase flow</h1>

## You will learn

Learn how to set up a post-purchase flow in Klaviyo as well as best practices for doing so. A post-purchase flow triggers after a customer has placed an order while your ecommerce platform is integrated with Klaviyo. Sending post-purchase emails builds relationships and brand loyalty with your customers and makes them more likely to purchase again.

![](https://fast.wistia.com/embed/medias/2xl49cevtg/swatch)

## About post-purchase flows

Sending post-purchase emails is essential for growing your brand. They turn a shopper into a loyal and repeat customer. According to our research, post-purchase messaging sees a 217% higher open rate, over 500% higher click rate, and 90% higher revenue per recipient than your average email campaign.

Post-purchase flows are any flow that send after someone makes a purchase. This is a broad category that includes:

- Thank you flows
- Cross-sell flows
- Upsell flows
- Product review flows

## Create a post-purchase flow

Below, we explain how to set up a basic post-purchase flow.

1. Navigate to the ****Flows****tab.
2. Click ****Create flow.****
3. Select ****Build your own****.
4. Name the flow and click ****Create flow****.
5. From the trigger selection menu, choose ****Placed order****.
6. Click ****Save**** > ****Confirm and save****.
7. Include time delays, if applicable:
   - Recommended for product review, cross-sell, and upsell flows
   - Not recommended for thank you flows
8. Add in splits to target customers based on aspects such as:
   - New versus returning customer (**Placed Order at equals 1 over all time**)
   - Amount paid (**Value is greater than ****X******)
9. Add in your initial message(s).
10. Add in time delays before any following splits or messages.
    - Tip: consider when other messages regarding a customer's order may go out, such as any order fulfillment flow message
11. Click the ****Update status**** when you're ready for the flow to start sending.
12. Choose ****Live****from the dropdown.
13. Click ****Save****.

****![Example flow with Placed Order trigger and a conditional split that checks 'Has Placed Order equals 1 over all time'](https://klaviyo.zendesk.com/hc/article_attachments/28716054944667)****

### Target customers using splits

![Video showing how to create a splits to check for first-time buyers or for product value](https://fast.wistia.com/embed/medias/vh1agbsbj7/swatch)

Personalizing your messaging is a great way to get customers to return to your brand and complete another purchase. The wants of a first-time buyer or a repeat purchaser are different, and your messaging should reflect that. With a first-time buyer, you can encourage them to sign up for your email list or join a loyalty program. You can thank a repeat purchaser for their continued business, update them on their loyalty status, or reach out to find more information about them. To create this split within a flow, you can add in a conditional split contingent upon having a previous **Placed Order** event.

![Example of a conditional split that checks 'Has Placed Order equals 1 over all time'](https://klaviyo.zendesk.com/hc/article_attachments/28716065499803)

Additionally, you can split based on if someone has purchased a more expensive product. You can encourage your potential VIPs by showing them the privileges that you have within your VIP program. To segment your customers further, you can add in a trigger split based on $value and set whatever threshold you deem as a significant purchase for your business.

![Example of trigger split that checks '$value is greater than 100'](https://klaviyo.zendesk.com/hc/article_attachments/28716054951579)

### Check your overall messaging

While you’re working out how your customers are segmented within your flow itself, you’ll want to make sure they aren’t overwhelmed with emails. You should ask yourself a few questions:

- Could a customer also be subscribed to your email list?
- If they are subscribed, would they be receiving a welcome series?
- If a customer makes a purchase and abandons a cart the next day, will they be added to an abandoned cart flow?

To make sure you’re not inundating your customers with emails, use [Smart Sending](https://help.klaviyo.com/hc/en-us/articles/115002779311) to automatically limit the number of messages someone can receive in a set period of time.

### Consider the content and schedule

![Video explaining the difference between transactional, thank you, review requests, and cross-sell emails](https://fast.wistia.com/embed/medias/gp4doafpud/swatch)

Once you’ve decided how you want to segment your flow, iron out the schedule and content of your emails. To start, just like with every bit of your messaging, you’ll want to make sure that your tone, styling, and colors are consistent across all of your communication. When trying to figure out the content of your post-purchase emails you can start by looking at the four different types of emails that you can send post-purchase — transactional, thank yous, review requests, and cross sells.

While you can send these in any order of your choosing, below is an example flow that you could use as inspiration. This flow is for a company that, on average, takes 9 days from the order being placed until it’s shipped. The shipment email is excluded from the below flow because the company would want to use another flow triggered off of the shipment to make sure that the email is properly timed.
![Example flow that splits based on first time purchase and whether or not the other has been fulfilled on time within 10 days](https://klaviyo.zendesk.com/hc/article_attachments/28716054953883)

## Examples of post-purchase emails

### Email #1: transactional email

Transactional emails let the customer know that their order has been processed and items have been shipped. While this is the trigger that starts the post-purchase flow, it's best to keep your transactional flows, both the order and shipping confirmation emails, in separate flows to ensure that all your customers receive the information they need as soon as possible. For an email to be considered a transactional email, it cannot have any marketing effort inside it. This is just sent to let the customer know that you have received their order and should go to everyone who has placed an order.

### Email #2: thank you email

Next up, a thank you email. Thank yous help build your relationship with your customers by thanking them, welcoming them to the family if it is their first purchase, or letting someone know about a loyalty program. This is a good place to split your flow based on if someone has purchased from you before so you can change your language within the email. For your new customers, you can welcome them into your brand’s community and encourage them to sign up for your email list, if you haven’t already. For returning customers, you can thank them for being loyal to your brand and update them on their loyalty rewards incentives. Further, if you’ve added another split by order value, this is a good place to offer VIP messaging to those of your customers that have spent more with you.

### Optional email: instructions

If you have an item that’s particularly difficult to use or requires some instruction, you can include an instructional email right before the item arrives. Make sure this email is well timed to your shipping window, as you don’t want your customer to get your email too early that they forget about the email or after the product arrives. You can create a flow dedicated only to sending your customer instructions, especially if you're using a [third-party tool like ShipStation or Aftership](https://help.klaviyo.com/hc/en-us/sections/14515580344859).

### Email #3: review request email

Review requests encourage customers to write a review either on social media or on your site itself. While you cannot incentivize a customer to write a good review for you, it’s important that you get them to review so other customers can return. Review request emails are essential. You can devote an entire flow dedicated to just review requests. For information on how to do that, check out our article on [Creating a product review flow](https://klaviyo.zendesk.com/hc/en-us/articles/115002779391).

### Email #4: cross-sell email

Lastly, cross-sell emails encourage another purchase from a customer by recommending something they are also likely to purchase. You’ll want to include your most popular products if you’re trying to get someone to purchase again. Not to worry, if someone has purchased an item, it won’t populate in their email. Like the review request email, you can create a whole flow dedicated to just cross-sell items. For more information head to our article on [Creating an upsell or cross-sell flow](https://klaviyo.zendesk.com/hc/en-us/articles/115002775212).

### Additional resources

- [Understanding flow triggers and filters](https://klaviyo.zendesk.com/hc/en-us/articles/115002779051)
- [How to use event data to personalize email and SMS flows](https://klaviyo.zendesk.com/hc/en-us/articles/115002779071)
