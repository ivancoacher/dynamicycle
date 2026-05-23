<h1>How to use SMS in replenishment flows</h1>

Learn how to add SMS to your replenishment flow in Klaviyo to turn one-time customers into repeat buyers.

****Why use SMS for replenishment**** ****flows?****

Replenishment flows are a great use case for text message marketing.

SMS has an open rate of ~98%, and these messages are almost always seen immediately. Thus, SMS works best when you provide subscribers with time-sensitive information that they’re interested in.

This pairs well with replenishment flows, which (if you get the timing right) are seen as a welcome reminder rather than a pushy sales-driven message. Adding SMS to your replenishment flow gives you the opportunity to remind your customers to restock exactly when they need to.

## Before you begin

Before you can start adding SMS to any flow, [turn on SMS in your account settings](https://help.klaviyo.com/hc/en-us/articles/4404274419355).

## Add SMS to your replenishment flow

The next steps depend on your current setup.

****If you don’t have a replenishment flow, open this dropdown.****

1. Navigate to the ****Flows**** tab.
2. Click ****Create Flow****.
3. In the search bar, enter a term for a flow type you want to create such as “replenishment.”
   ![](https://klaviyo.zendesk.com/hc/article_attachments/41638797014683)
4. Choose the replenishment flow option with “Email & SMS” in the title if available.
   - If you don’t see an SMS option available, make sure you have SMS enabled in your account settings.
   - If SMS is turned on and you still don’t see a pre-built template, check out this [article on building your own replenishment flow](https://help.klaviyo.com/hc/en-us/articles/360003195232).
5. Click into the flow and then select ****Use template****.
6. Edit the flow’s messages to suit your needs.
7. When you’re ready to set the flow live, click ****Review and turn on**** in the upper right.
8. Choose ****Live**** and then click ****Save****.

Want to jump ahead? Skip to the section on [best practices for SMS replenishment flows](https://help.klaviyo.com/hc/en-us/articles/16318679373595#h_01HGXF39VFHKP3HDTWETE2VQKM).

For those with existing replenishment flows:

1. Go to the ****Flows**** tab.
2. Navigate to the replenishment flow where you want to add SMS.
3. After the first time delay, add a conditional split.
4. Set the split’s condition to: **If someone can or cannot receive marketing > can receive > sms marketing**.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/33086336285083)
5. On the YES path, place an SMS message.
6. Click ****Configure Content****.
7. Add in your message; for example: “Hey {{ first\_name|default:’there’ }}, running low? Reorder now! [LINK]”
8. On the NO path, rejoin the split under the SMS message.
9. Add a time delay below the rejoin and set it to 1 day.
10. Move your existing email to below the 1-day time delay.
    ![](https://klaviyo.zendesk.com/hc/article_attachments/33086336288539)
11. When you’re ready to publish, click ****Review and turn on**** in the top right of the flow builder.

## Best practices for replenishment flows

There are 3 key things to keep in mind when creating replenishment flows:

- ****Message timing****
  Timing is the most important part of replenishment flows. The key is to remind subscribers when they are low on the product, but not completely out. They also work better if you allow time for the product to ship and be delivered. For instance, if the buying cycle is 30 days, you may want to send the notification at around 20 days.
- ****Message content****Replenishment messages should focus on reminding customers about the product. Best practices for creating the content include:
  - Keep it simple and straightforward.
  - Remind recipients about the product.
    - Add the product name.
    - Link to the product page.
  - Consider adding a promotion, particularly for first-time flow recipients.
    - Provide free shipping.
    - Offer a 10% off coupon.
- ****Number of messages****Typically, replenishment flows don’t need many messages, at most 1–2 per recipient:.

## Optimize your replenishment flow

### Improve the message timing

To optimize the message timing, you need to test what works best for your audience:

1. Decrease the number of days in the initial time delay (e.g., from 25 to 20).
2. Under the split that separates your SMS subscribers, add another conditional split.
3. Set this new split to **Random sample** > **50%**.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/33086358749979)
4. Add a time delay to each path under the random sample.
5. Choose the timeframes you want to test (e.g., 1 day versus 5 days).
   ![](https://klaviyo.zendesk.com/hc/article_attachments/33086336293275)

Over time, check back on the results of each message for both the click rate and conversion rate. (Klaviyo can’t automatically pick a winner when using a split to A/B test.)

Repeat this experiment until you find the shortest timeframe with the highest performance.

### Order value split

For higher-priced items, customers may wait for discounts before re-buying or take more time before deciding. You may want to add an extra incentive, space out the replenishment messages, or change the phrasing to convince customers to restock more expensive items.

To split the flow based on order value:

1. Add a trigger split directly after the first time delay.
2. Set the split to **trigger $value > is at least > 100** (replace 100 with whatever order value you’d like to split based on).
3. In both the YES and NO paths, add conditional splits that check for SMS consent and add your email and SMS messages accordingly.
4. Edit the message(s) in the YES path to offer your incentive (e.g., a discount or free shipping), change the timing of messages, etc.
   ![Example of splitting a replenishment flow based on the order value](https://klaviyo.zendesk.com/hc/article_attachments/28723661928603)

### First-time flow recipients vs. repeat customers

Replenishment flows help people develop the habit of re-buying from you. To convert one-time customers to repeat customers, you may want to split the flow and its messages, maybe offer a discount.

1. Add a conditional split directly after the first time delay.
2. Set the split to **What someone has done (or not done) > Placed Order > is at least 2 > over all time**.
3. In both the YES and NO paths, add conditional splits that check for SMS consent and add your email and SMS messages accordingly.
4. Edit the message(s) in the NO path to customize your messaging for first-time flow recipients (e.g., offer an incentive).
   ![Example of splitting a replenishment flow for one-time customers versus repeat
       customers](https://klaviyo.zendesk.com/hc/article_attachments/28723661925531)

## Additional resources

Learn more about adding SMS in your flows:

- [Add SMS to a browse abandonment flow](https://help.klaviyo.com/hc/en-us/articles/15806802249883)
- [Add SMS to a thank you or order confirmation flow](https://help.klaviyo.com/hc/en-us/articles/15800790306715)
- [Create flows to respond to inbound SMS messages](https://help.klaviyo.com/hc/en-us/articles/360049930372)
