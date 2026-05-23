<h1>How to create an SMS welcome flow</h1>

Learn how to create a welcome flow for your SMS subscribers.

As a best practice, your SMS welcome flow should be separate from your email welcome series.

****What is a flow?****

A flow is an automated series of actions or messages that sends after someone performs a specific action. For an SMS welcome flow (also called a welcome series), this means that after someone consents to SMS, they’ll automatically get messages welcoming them into your SMS program

****Why use a welcome series for SMS****

In a welcome flow, SMS messages offer you a way to make a more immediate impact on new subscribers.

On average, most text messages (~98%) are looked at within 90 seconds. In comparison, only 20% of emails are viewed, and it typically takes between 90 minutes and 3 hours for customers to view said emails.

The shorter time frame means you can reach SMS subscribers when their interest in your business is at its peak. It is a great chance to encourage them to move further down the funnel — driving them from being a subscriber to a customer.

## Before you begin

Before you send any messages from an SMS welcome series, you should have:

- [Set up SMS in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/4404274419355)
- Optional: created a coupon
- Optional: set up virtual contact cards (US and Canada only)

****Why do I need to set up SMS?****

You must have turned on SMS in Klaviyo before you can add SMS messages in your flows. Otherwise, you’ll be prompted to set up SMS while you’re trying to build your flow.

****Why should I have a coupon and how do I create one?****

When someone signs up for text messages, they are really giving you a direct line of communication. You’ll be able to reach them at any time almost instantly.

Due to how personal SMS is as a channel, it’s a best practice to reward anyone who subscribes to SMS. If you have not already created a coupon and want to know how to do so, click the name of your ecommerce platform from the list below:

- [BigCommerce](https://help.klaviyo.com/hc/en-us/articles/360022884472)
- [Magento 1](https://help.klaviyo.com/hc/en-us/articles/115005246547)
- [Magento 2](https://help.klaviyo.com/hc/en-us/articles/360041971851)
- [Shopify](https://help.klaviyo.com/hc/en-us/articles/115006155388-)
- [WooCommerce](https://help.klaviyo.com/hc/en-us/articles/360031279471)
- [PrestaShop](https://help.klaviyo.com/hc/en-us/articles/19655157461403)

****What are virtual contact cards and why should I set them up?****

Virtual contact cards allow recipients to save your contact information. This way, they’ll know when messages are coming from your brand and will recognize your SMS sending number.

These contact cards are particularly useful in welcome flows, as that’s the first text message someone will receive from your brand.

Note that these cards automatically turn your text into an MMS, and will count as more credits than an SMS. Further, because MMS is not available in the UK or Australia, virtual contact cards can only be sent to US and Canadian subscribers.

Before you can use virtual contact cards, you must [turn on this option](https://help.klaviyo.com/hc/en-us/articles/8458786130331) in your SMS settings page.

## Create an SMS welcome series

There are 2 ways you can build an SMS welcome series in Klaviyo:

1. Use a pre-built template (recommended).
2. Build it yourself without a template.

We go over both scenarios below.

### Use a pre-built template to build your SMS welcome series

This is the easiest and fastest way to create an SMS welcome series. We recommend using this approach, as you’ll be ready to start sending in less than 5 minutes.

The templates include placeholders for a coupon. If you have not already created a coupon, we recommend [doing that first](#h_01GBQJ3Y02HCBXT3TQ4WJVN5VQ).

To use a pre-built template for your welcome flow:

1. Click ****Flows****.
2. Click ****Create Flow**** in the upper right-hand corner.
3. Search “welcome” and select the text bubble icon to only show SMS flows.
   ![Browse Ideas searchbar with 'welcome' entered in](https://klaviyo.zendesk.com/hc/article_attachments/28722556966683)
4. Pick an SMS welcome flow.
   - Here, we chose the flow called “Unique Discount w/ Reminder.”
5. Name the flow.
6. Click ****Create Flow****.
7. Click into the first SMS.
8. Review the message text and replace any placeholder text (such as for a coupon code).
   ![Example of SMS message in the SMS editor with placeholder text](https://klaviyo.zendesk.com/hc/article_attachments/28722556972955)
9. Click into the second SMS in the flow.
10. Review the content and replace placeholder text with the coupon.
11. When you’re ready for the flow to be live, click ****Review and Turn On****.

## Build an SMS welcome series without a template

We strongly recommend using a template rather than building an SMS welcome series without one.

However, if you do decide to build the series yourself, follow the steps below to create a 1-message SMS welcome flow:

****How to build an SMS welcome flow without a template****

1. Click ****Flows****.
2. Click ****Create Flow**** in the upper right-hand corner.
3. Click ****Create From Scratch****.
4. Name the flow (e.g., SMS-only welcome).
   ![Create Flow modal with name 'SMS-only welcome' and tag 'welcome'](https://klaviyo.zendesk.com/hc/article_attachments/28722556970907)
5. Click ****Create Flow****.
6. Choose ****Metric**** as the trigger type.
7. Click into the flow trigger dropdown.
8. Select ****Subscribed to SMS Marketing****.
9. Click ****Flow Filters****.
10. Click ****Add a Flow Filter****.
11. From the dropdown, select ****Has not been in this flow****.
12. Leave the second dropdown as: ****at any time****.
    ![Trigger setup with configuration 'Has not been in this flow at any time'](https://klaviyo.zendesk.com/hc/article_attachments/28722556976667)
13. Click ****Save**** to save the flow filter.
14. Click ****Done**** to save the trigger setup.
15. Drag an SMS message directly after the trigger.
16. Click ****Edit****in the details sidebar.
17. Add your content.
    - It’s best if the message is short and to the point.
      - Example: Thanks for signing up! Enjoy 15% off your next purchase with code {% coupon\_code 'COUPON NAME' %} {{ organization.url }}
        ![SMS welcome series content.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28722556989211)
18. Click ****Save Content****.
19. Optional: add a virtual contact card.
    - Notes:
      - A virtual contact card turns the message into an MMS and counts as more credits in your billing plan.
      - MMS, and thus, virtual contact cards, are only available in the US and Canada.
    - Instructions
      1. Add a conditional split after the first SMS and set the condition to:
         **Properties about someone > Country equals United States**
         Or
         **Properties about someone > Country equals Canada
         ![Showing the conditional split after the first SMS](https://klaviyo.zendesk.com/hc/article_attachments/28722556980763)**
      2. Add a time delay on the YES path after the split.
      3. Set the time delay for 10 minutes.
      4. Add an SMS after the time delay.
      5. Click ****Edit****.
      6. Add in a message to subscribers asking them to save your contact information.
         1. Example: "Make sure to save our contact card to be notified about our latest deals!"
      7. Click the **Add Media** button (an image icon).
         ![Insert media button.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28722556990491)
      8. Select the ****Virtual Contact Card**** option.
      9. Click the ****Add Contact Card**** button to add the card to the SMS message.
20. Click ****Save Content****.
    ![Showing the welcome series after the virtual contact card is added](https://klaviyo.zendesk.com/hc/article_attachments/28722595361563)
21. Click ****Review and Turn On****.

## Personalize your SMS welcome series

The steps above outline how to create a simple SMS welcome series. This is great when you’re first getting started with SMS, but once you get more SMS subscribers, you may want to make the flow more personalized.

Consider splitting your welcome series based on:

- Repeat vs. first-time buyers
- Purchase history
- Profile and custom properties

****Repeat vs. first-time buyers****

If you know someone has been on your email list for a certain amount of time but has never made a purchase, you may want to offer them a discount (or greater discount) in the second or third message of your SMS welcome series.

Keep in mind that you will need to create a new coupon code to include in the message with the higher discount.

![Example conditional split with configuration 'Has Placed Order zero times over all time'](https://klaviyo.zendesk.com/hc/article_attachments/28722556982299)

****Purchase history****

Splitting your flow based on purchase history is a great way to offer more targeted calls to action (CTAs). For example, if you know that someone has already bought from a certain collection, you can show them a CTA related to a different collection.

![Example conditional split with configuration 'Has Placed Order zero times over all time where Collections contains Best Seller'](https://klaviyo.zendesk.com/hc/article_attachments/28722556987803)

****Profile and custom properties****

You can leverage any information you learned about a subscriber when they initially signed up or through any subsequent emails they may have received.

For example, let's say that in the first email of your email welcome series, you ask customers to select which category of products they're most interested in. You can then use this information to inform the CTA in your SMS welcome series.

It's important to have a default branch in case a subscriber has never indicated an interest in any of the options. In the example above, we're showing our best sellers to those who have never explicitly told us the types of items they're interested in.

![Multiple conditional splits based on different Interest property values](https://klaviyo.zendesk.com/hc/article_attachments/28722556985371)

## SMS welcome series best practices

There are a couple best practices to keep in mind when creating an SMS welcome series:

- Keep the series between 1 to 3 messages to not overload your subscribers.
- Make your messages short and to the point.
- Set up a [virtual contact card](https://klaviyo.zendesk.com/hc/en-us/articles/8458786130331) so your customers can add you as a trusted contact.
  - Note: virtual contact cards are treated as MMS messages.

You may want to turn off [quiet hours](https://help.klaviyo.com/hc/en-us/articles/4408737146651-) for the first SMS message in the welcome series. However, if you do so, you may need to remove all marketing material, including coupons, from the message.

##

## Additional resources

Want more information on flows? Check out [getting started with SMS flows](https://academy.klaviyo.com/en-us/courses/getting-started-with-sms-flows).

Learn about [SMS marketing strategies for all levels](https://www.klaviyo.com/blog/sms-marketing-strategies).

Now that you’ve set up your welcome series, take your next step:

1. [Create a mobile terms of service](https://klaviyo.zendesk.com/hc/en-us/articles/360049177511)
2. Update your [privacy policy](https://klaviyo.zendesk.com/hc/en-us/articles/4404199571867)
3. [Collect SMS subscribers](https://klaviyo.zendesk.com/hc/en-us/articles/360035056972)
