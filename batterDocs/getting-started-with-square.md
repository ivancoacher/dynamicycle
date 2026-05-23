<h1>Getting started with Square</h1>

## You will learn

Learn how to easily integrate Klaviyo with your Square Online site in order to sync customer profile, order, and catalog information to Klaviyo, along with order data from your Square Point of Sale (POS). With this data, you’ll be able to reach customers with targeted messaging through segmentation, automated flows, and campaigns.

## Before you begin

When you integrate Square with Klaviyo, only 1 Square account can be connected to your Klaviyo account. If you have multiple Square accounts you will need to integrate each with a separate Klaviyo account.

Square POS order events will sync to Klaviyo (and profiles will be created) if there is an email address and/or phone number associated with the order which the customer directly shared with your company.

Square events will have a property called **source name** that will show whether the event is from a POS or from online/web, so that you can [segment these events in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115005237908-Getting-started-with-segments).

## Integration video

Check out our step-by-step video on integrating with Square.

![](https://fast.wistia.com/embed/medias/5qlt7jxxy1/swatch)

## How to integrate with Square

1. In your Klaviyo account, select ****Integrations**** in the left-hand navigation.
2. Select ****Explore apps****, search for **Square**, and click the card. Then, click ****Install****.
3. Input your store URL in the box and click ****Connect to Square****.
   ![Screenshot 2025-09-23 at 8.10.01 PM.png](https://klaviyo.zendesk.com/hc/article_attachments/41382239155099)
4. You’ll be brought to your Square account and prompted to login (if you are not currently logged in).
5. Once you’ve logged in, review the permissions and click ****Allow**** to be brought back into Klaviyo.
6. Review your store URL setting to make sure that you’ve chosen the correct Square account to integrate with Klaviyo.
   ![Group 5.png](https://klaviyo.zendesk.com/hc/article_attachments/41382239156891)
7. The setting **Automatically add Klaviyo onsite JavaScript** is checked by default; leave it checked if you would like to enable Klaviyo’s **Active on Site** tracking and signup forms.
8. Click ****Complete setup****.
9. After a loading screen, you should see a success message reading **Your Square account is now connected to Klaviyo!**

   ![Screenshot 2025-09-23 at 8.11.28 PM.png](https://klaviyo.zendesk.com/hc/article_attachments/41382239158427)

   You’ve finished integrating and your historical Square data will start syncing to Klaviyo. Any new events from Square Online will start syncing to Klaviyo in real time, and events from Square POS will sync every 30 minutes.

   If you ever need to edit your Square settings:
10. In your Klaviyo account, select the ****Integrations**** tab.
11. Select ****Square**** on the list.
12. You’ll be brought to the integration settings page, where you can make changes.
13. Click ****Save****.

## Data synced from Square to Klaviyo

To check on the data sync from Square to Klaviyo:

1. In your Klaviyo account, select the ****Integrations**** tab.
2. Select ****Square**** on the list.
3. Select the ****Data**** tab at the top.

Here, you’ll see recent data synced from Square to Klaviyo, and a sync progress bar for your historical data sync.

![The Data page in Klaviyo showing Recent data from Square and the option to Re-import.](https://klaviyo.zendesk.com/hc/article_attachments/34458041320987)

If you are experiencing issues with your sync while it is ongoing, select ****Re-import**** here to restart the historical data sync.

The data synced from Square to Klaviyo includes:

- [Known site visitors](https://help.klaviyo.com/hc/en-us/articles/115005076767-Guide-to-Klaviyo-Onsite-Tracking#who-klaviyo-tracks5) tracked as **Active on Site** events (if you left the onsite JavaScript setting checked)
- Email unsubscribes
- Profile information associated with order events
- Your Square catalog (including POS-only items)
- The following order events:
  - Abandoned Checkout
  - Placed Order
  - Ordered Product
  - Refunded Order
  - Cancelled Order
  - Fulfilled Order
  - Fulfilled Partial Order

Square events will have a property called **source name** that will show whether the event is from a POS or from online/web, so that you can [segment these events in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115005237908-Getting-started-with-segments).

For more information on the properties associated with each event synced from Square, check out our article [Square data reference](https://help.klaviyo.com/hc/en-us/articles/11117271030555).

## Create a Klaviyo sign-up form for your Square site

Learn how to [create Klaviyo sign-up forms](https://help.klaviyo.com/hc/en-us/articles/360026474752-Getting-started-with-sign-up-forms) in order to collect email and SMS subscribers on your Square site. Once published, these forms will show up automatically on your site, given that you checked the **Automatically add Klaviyo onsite JavaScript** setting when you integrated.

You can create the following types of Klaviyo forms:

- Popup
- Flyout
- Full Page
- Embed ([make sure to follow our guide adding an embed form to a Square site](https://help.klaviyo.com/hc/en-us/articles/18229698831003))

## Create automated messaging with Square data

There are a number of pre-built flows for Square in Klaviyo’s flow library, which you can use to personalize customer messaging.

To access these flows:

1. Select the ****Flows**** tab in Klaviyo.
2. Click ****Browse Ideas**** in the upper right, or ****Create****, if this is not your first flow.
3. Select ****Square**** from the filter dropdown next to the search bar.

These pre-built flows include:

- Abandoned Checkout
- Customer Winback
- Shipping Confirmation
- Replenishment Reminder
- Repeat Purchase Nurture
- Abandoned Cart Reminder
- Customer Thank You
- Customer Winback
- Product Review / Cross Sell
- Abandoned Cart Reminder; High Value Cart vs. Low Value Cart
- Tag First Purchase Date
- Post-Purchase Bounce Back
- Delayed Fulfillment
- Fulfilled Partial Order
- Order Confirmation

## Outcome

You’ve integrated Square with Klaviyo and verified your synced data. Now, you can create automated flow messages, personalize campaigns, segment your lists, and more based on data synced from Square.
