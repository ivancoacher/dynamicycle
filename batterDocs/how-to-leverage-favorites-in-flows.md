<h1>How to leverage favorites in flows</h1>

Discover how to use flows to automatically email shoppers about items they've favorited on your site. Whether you're sending a dedicated favorites reminder or filtering an existing flow — like a price drop alert — to prioritize customers who've favorited a product, these automated messages drive conversions by reaching the most interested shoppers at the right moment.

Customer Hub for Shopify currently supports standard storefronts and Shopify Headless. For WooCommerce, navigate to https://help.klaviyo.com/hc/en-us/articles/47792369863451

For feedback about Customer Hub functionality, email customerhub@klaviyo.com.

## Before you begin

To set up a favorites reminder flow, you must:

1. Have [Customer Hub live on your site](https://klaviyo.zendesk.com/hc/en-us/articles/33660324811675).
2. Have the [**Favorites** feature enabled in Klaviyo](https://klaviyo.zendesk.com/hc/en-us/articles/33660543083419).

## Filter by favorites status in flow triggers

For flows with product-based triggers (such as Price Drop), you can now filter entry into the flow based on whether a customer has favorited the item — no additional flow filters or workarounds needed.

Under the trigger settings, scroll to the ****Filter by favorites**** section and choose one of the following options:

- ****All customers**** — Any customer who meets the trigger conditions will enter the flow, regardless of favorites status
- ****Only if favorited**** — Only customers who have favorited the item will enter the flow
- ****Only if not favorited**** — Only customers who have **not** favorited the item will enter the flow

This is particularly useful for a price drop flow: by selecting ****Only if favorited****, you can ensure that price drop alerts are sent exclusively to customers who have expressed the strongest interest in that product, making the message more relevant and timely.

![Screenshot 2026-02-19 at 9.36.58 AM.png](https://klaviyo.zendesk.com/hc/article_attachments/48619956991515)

## About Klaviyo’s favorites reminder flow

Once you’ve installed favorites on your site, use a Klaviyo flow to remind and encourage shoppers to revisit their saved items. A prebuilt favorites reminder flow is available in Klaviyo’s flow library, titled: **Customer Hub Favorites Reminder**.

![favflow0.jpg](https://klaviyo.zendesk.com/hc/article_attachments/37006292191771)

This flow triggers off the **Customer Hub Add to Favorites** metric, which records when a shopper clicks a favorites button on an item. Each favorited item logs as a separate event. However, a shopper will only receive 1 reminder email per shopping session, even if they favorite multiple items. The email displays up to the 3 most recently favorited items from that session.

By default, the **Customer Hub Favorites Reminder** flow has the following profile filters applied:

- **Has not been in a flow in the past 1 day**
- **Customer Hub favorites has at least 1 item**

These filters use AND logic, which means that both criteria must be met in order for a profile to be eligible to enter the flow and receive the email. [Learn more about profile filters](https://help.klaviyo.com/hc/en-us/articles/115002779051#h_01HDAFKRKRJ7N44M7NWEQRSANP).

## Create a favorites reminder flow

1. In Klaviyo, navigate to the ****Flows**** tab.
2. Click ****Create flow****.
3. Search for “Favorites,” then select the ****Customer Hub Favorites Reminder**** flow template.
   ![favflow.5.jpg](https://klaviyo.zendesk.com/hc/article_attachments/37006297282843)
4. Click ****Use template****.
   ![favflow2.jpg](https://klaviyo.zendesk.com/hc/article_attachments/37006297285787)
5. Optional: Adjust the time delay and messaging as preferred. Click either one in the canvas to edit it.
   - The default pre-built flow sends a single email one day after a browsing session where at least one item was added to favorites. The email template automatically pulls your established Customer Hub styles and is pre-configured to display the shoppers’ recently favorited items from that session.

     If you adjust the time delay in the flow, you should also adjust the timeframe on the profile filter to ensure the intended delay between messages is maintained. By default, both are set to a 1-day delay.

     ![favflow3.jpg](https://klaviyo.zendesk.com/hc/article_attachments/37006297286043)
6. Click ****Review and turn on**** in the top right corner.
7. Choose ****Live**** from the dropdown.
8. Click ****Save****.

Once the flow is live, eligible shoppers automatically enter your flow to receive the favorites reminder email.

![favflow.jpg](https://klaviyo.zendesk.com/hc/article_attachments/37006297286171)

When recipients click the “View favorites” button in the email, they are directed back to your site with the Customer Hub interface open and displaying their favorited items, simplifying the path to purchase.

## Additional resources

- [How to show favorite buttons on your site and in Customer Hub](https://klaviyo.zendesk.com/hc/en-us/articles/33660543083419)
- [How to enable product recommendations for Customer Hub](https://klaviyo.zendesk.com/hc/en-us/articles/33660504643867)
- [How to create content blocks for Customer Hub](https://klaviyo.zendesk.com/hc/en-us/articles/33660517680795)
