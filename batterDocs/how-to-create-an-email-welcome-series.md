<h1>How to create an email welcome series</h1>

## You will learn

Learn how to create a sequence of emails sent directly after someone subscribes to hear from your brand. This is a critical moment in the customer lifecycle because it's your opportunity to introduce new, interested prospects to your business and product offering. With a welcome series, you should capitalize on this display of interest.

Your email welcome series should be separate from your SMS welcome series flow, since subscribers may sign up for email and SMS at separate times and can only enter a single welcome flow once. An SMS welcome series is also recommended for using features such as virtual contact cards and coupons in SMS messages. Learn more in our article on [creating an SMS welcome series](https://klaviyo.zendesk.com/hc/en-us/articles/360036122291).

A welcome series is a crucial automation, and Klaviyo provides a pre-built welcome series out-of-the-box. You will find an example welcome series flow listed in the ****Flows**** tab of your account. If you want a more advanced welcome flow, you can browse different ideas in our [flow library](https://www.klaviyo.com/library/flows).

#### Need assistance with your flow?

If you already have a welcome flow set up and are looking for ways to troubleshoot an issue, learn how to [troubleshoot a list-triggered flow](https://help.klaviyo.com/hc/en-us/articles/12414318812827?utm_source=welcome&utm_medium=hc&utm_campaign=troubleshooting).

![](https://fast.wistia.com/embed/medias/pzzv1q34ua/swatch)

### Understand how contacts are added to a list

Before setting up a welcome series, you must connect it to a list of your choosing. After creating your account, an empty list titled **Email List** is pre-populated into your ****List & segments**** tab. You can use this for your welcome series flow or [create a new list](https://help.klaviyo.com/hc/en-us/articles/115005078967).

Whichever list you choose should be the list new subscribers are added to when they sign up. There are four key ways new contacts can be added to a list to trigger a welcome series:

1. By signing up through a sign-up form
2. By signing up through a subscribe page
3. By being manually added to a list
4. Via the [Lists API](https://developers.klaviyo.com/en/reference/create_list_relationships) or via the [Subscribe API](https://developers.klaviyo.com/en/reference/subscribe_profiles)

### Pause your welcome series if you are importing a list

If you have already set your welcome series live and want to import a list, you must first set the series to manual. If not, everyone who was imported will be scheduled for the first message in the series, even if they subscribed months ago.

Follow these steps to import:

1. Open your welcome series flow associated with your main list.
2. In the top right of the flow builder, click ****Update Action Statuses****.
3. In the dropdown, select ****Manual****.
4. Click ****Update Statuses****.
5. Follow our guide on how to [import contacts into a list](https://help.klaviyo.com/hc/en-us/articles/115005251128).
6. Repeat steps 1-2, then set your flow back to ****Live****.

After the import is complete, you can manually send welcome messages to older contacts you imported.

1. Open the flow builder for your welcome flow.
2. Click on the first message.
3. In the **Performance** section of the sidebar, click ****View details.****
4. Click into the ****Recipient Activity**** tab.
5. Click ****Needs Review****.
6. For any imported contacts you’d like to send welcome emails, click ****Send**** next to the email in the **Needs Review** list.
7. Alternatively, you can click ****Cancel All**** to prevent these contacts from receiving the message.
8. Repeat this step for any other messages in the flow.

You may want to ensure that contacts who subscribe through your ecommerce integration are being added to the correct list. For example, many Shopify themes have a default newsletter sign-up form in the footer. While this is not a Klaviyo form, contacts who sign up using this form can still be added to a list in Klaviyo.

To verify if contacts who subscribe through your integration are being added to a list, and which list they are being added to, follow these steps:

1. In the bottom left of the main Klaviyo navigation, click the name of your account.
2. Click ****Integrations****.
3. Click on the name of your ecommerce integration.
4. In the integration settings, if you're able to sync contacts to a particular list with your integration, make sure to select the same list you're using for your welcome series. See this example for Shopify:
   ![Integration settings page for Shopify showing the dropdown for selecting a list to sync subscribers.](https://klaviyo.zendesk.com/hc/article_attachments/28716300736027)
5. Additionally, if you have any live Klaviyo sign-up forms, [ensure these forms are also pointing to the same list](https://help.klaviyo.com/hc/en-us/articles/360002049952#change-the-list-a-form-submits-to3).

### Understand double vs. single opt-in lists

By default, every list in Klaviyo is double opt-in. This is to protect your deliverability and ensure contacts who are added to your lists have a valid email address or phone number. We recommend leaving this setting on for your main list.

The workflow for a double opt-in list is as follows:

1. A contact signs up.
2. The contact receives a confirmation text or email.
3. Once they confirm their subscription, they are brought to the opt-in confirmed page.
4. The contact is added to the list.
5. The contact triggers the welcome series.
6. If the first welcome message is set to send immediately, they will receive the first message.

Learn how to enable single opt-in and more in our guide on the [double opt-in process](https://help.klaviyo.com/hc/en-us/articles/115005251108).

## Use Klaviyo's standard welcome flow

When you create a Klaviyo account, you can easily add a pre-built welcome flow titled "Welcome Series" into your account.

To set up this flow:

1. Navigate to the [Flows](https://www.klaviyo.com/flows) tab in your Klaviyo account.
2. On this page, click ****Create welcome series****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/47039104340763)
   If you have no flows in your account, this will be the main view of the Flows page. If you already have a flow in your account, you can view the different cards for pre-built flows below the list of flows.
3. You will be brought to a walkthrough of setting up your Welcome Series flow
   ![](https://klaviyo.zendesk.com/hc/article_attachments/47039100638619)

Before turning an email live within our pre-built welcome series, personalize the email templates with your own content and branding.

1. Click on a message in the flow builder.
2. In the details panel, edit the subject line and sender details if desired.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/47039104352539)
3. In the **Template** section, click ****Edit**** to edit the email template.
4. Use the email template editor to change the content of the message to match your branding.
5. Repeat these steps for the other messages in the flow.

A welcome series flow is a great way to introduce yourself after someone signs up to your email list. The welcome series featured above contains three emails:

1. ****Email #1, send immediately****
   Introduce new subscribers to your brand and collect their email preferences. To send subscribers an email immediately after they opt-in, add an email directly after your flow's trigger with no time delay before it.
2. ****Email #2, after 3 days****
   Three days after they sign up, encourage your subscribers to like or follow you on social media
3. ****Email #3, after 4 days****
   Four days after someone signs up, showcase your best-selling products.

You can customize or change the goals of any of these emails based on your particular use case. You can also add more to this flow, such as splits and SMS messages.

## Create an advanced welcome series flow

If you want a more advanced welcome flow:

1. Navigate to the ****Flows**** tab.
2. Click ****Create Flow**** in the top right to view the flow library.
3. In the search bar, enter “welcome series” to view different variations of pre-built welcome series flows.

Towards the end of this guide there are some examples of ways to make your welcome series flow more advanced. See the [advanced techniques section](#01GTW9ADC2KCHYDGKRFJ541K78).

## Build a welcome flow from scratch

It is possible to build your own welcome series by following these steps:

1. Navigate to the ****Flows**** tab.
2. Click ****Create Flow**** in the top right.
3. Click ****Build your own**** in the top right.
4. Name your flow.
5. Click ****Create Flow****.
6. In the flow builder, select ****Added to list**** from either the **Recommended** or **All triggers** tab.
7. Choose your main subscriber list.
8. Click ****Done****.
9. Drag an email action into your flow.
10. Click the message and click ****Configure Content**** to begin editing it.
11. Once you’ve edited the message to fit your brand, drag a time delay and additional messages as needed.

Every flow requires a trigger event and then supports optional flow filters which can add additional restrictions on who can receive the flow email.

For this welcome series example, we'll configure the flow to send to all new subscribers in our email list, so no flow filters are needed.

Note that someone can only receive messages in a list-triggered flow once. This means if someone subscribes, goes through your welcome flow, and then unsubscribes, they will not receive these messages again if they resubscribe later.

### How to time your welcome series and how many emails to include

When building out your welcome series, you may wonder how many emails to include and how much time to configure between emails. For a standard welcome series, we recommend sending 3 emails over the course of a week with the following cadence used in our pre-built flow:

1. Email #1, send immediately
2. Email #2, after 3 days
3. Email #3, after 4 days

Each audience is unique, and the best way to find what works for your business is to test and iterate. Klaviyo offers A/B testing features which allow you to branch your flow into different paths containing different time delays and messages if you’d like to test different strategies. Learn more in our article on [how to A/B test flow branches](https://help.klaviyo.com/hc/en-us/articles/360049849432).

## Content to include in your welcome series

Your welcome series is new subscribers’ first interaction with your brand, so it’s important to put your best foot forward. A welcome series can have a couple of different types of goals. Keep your goal in mind when creating the content for your welcome series flow.

Here are some examples:

- ****Share your brand’s story and mission****
  You may have a story-focused welcome series aimed at introducing new subscribers to your brand’s mission rather than pushing your first sale. In this case, it is best practice to have a longer welcome series with personal anecdotes from your brand’s founder discussing why they started the company and what you’re looking to accomplish.
- ****Offer promotions and coupons****
  If you offer an incentive on your sign-up form, include this in the first email of your welcome series. Learn about [how to include coupons in emails](https://klaviyo.zendesk.com/hc/en-us/articles/115005084727).
- ****Market your content****
  If the main goal of your welcome series is to turn subscribers into customers, display your most eye-catching products. Use product blocks to showcase trending or best-selling products to maximize the chance that someone will see something they like and use their discount to make their first purchase.
- ****Promote social media****
  You can use your welcome series to promote your brand’s social media channels to build customer relationships and brand awareness.

From a design standpoint, because a welcome series is subscribers’ first interaction with your brand, take the time to ensure your email templates exemplify the tone and aesthetic you want to present. We have a number of pre-built email templates in the template library you can use as a starting point, but it’s also important to make sure that your email design is consistent with the design on your website. As for your text messages, make sure your content is concise and provides value, and any images or GIFs are high quality.

## Advanced techniques

You can find several different types of welcome series in the flow library. These contain out-of-the-box best practices around discounting and targeting customers vs. non-customers.

Below are some ways you can modify your welcome series to target specific types of contacts.

### Target subscribers who have never purchased before

Many businesses offer a discount on a subscriber's first purchase if they sign up to their email list.

1. Drag a conditional split beneath the flow trigger.
2. Configure the conditional split to “Has Placed Order at least once over all time.” People who have never placed an order before will go down the NO path.
   ![Conditional split configured to 'Has Placed Order at least once over all time.'](https://klaviyo.zendesk.com/hc/article_attachments/28716328130075)

### Target subscribers who haven't purchased since signing up

If you don't want to offer a discount up front in your welcome series, you can target people with a coupon code after giving them the opportunity to purchase in the first few messages of your welcome series. This will help you avoid giving out discounts unnecessarily.

1. Drag a conditional split beneath the flow trigger.
2. Configure the conditional split to “Has Placed Order at least once since starting this flow.”
   ![Conditional split configured to 'Has Placed Order at least once since starting this flow.'](https://klaviyo.zendesk.com/hc/article_attachments/28716328136603)

### Encourage SMS sign-ups

It’s important to keep your email and [SMS welcome flows](https://help.klaviyo.com/hc/en-us/articles/360036122291) separate. However, you can use your email flow to encourage people to subscribe to SMS.

In your email welcome flow:

1. Drag a conditional split below the first time delay.
2. Set the split to **can receive SMS marketing**.
3. On the YES path, add any message you’d like for the second message of your series.
4. On the NO path, add an email.
5. For the email’s content, highlight the benefits of signing up for text messages. Then, include a [link to where people can subscribe to SMS](https://help.klaviyo.com/hc/en-us/articles/14104388043931).
6. Add a time delay to the NO path.
   ![Beginning of a welcome flow with a split to see if someone is consented to SMS](https://klaviyo.zendesk.com/hc/article_attachments/28716328138651)
7. Below the time delay, add another split for **Is consented to SMS**.
8. Clone the email from the first YES path and drag the clone to this YES path.
9. On the NO path, add another email.
   ![End of a flow that encourages SMS sign-ups](https://klaviyo.zendesk.com/hc/article_attachments/28716300750747)
10. In the email, include a way to subscribe to SMS as well as why recipients should do so.

## Additional resources

- Learn how to create an [SMS welcome series](https://klaviyo.zendesk.com/hc/en-us/articles/360036122291).
- Learn how to [troubleshoot a list-triggered flow.](https://klaviyo.zendesk.com/hc/en-us/articles/12414318812827)
- Check out this blog post on [your guide to welcome email automation excellence.](https://www.klaviyo.com/blog/resources-welcome-series)
