---
id: 21137997887771
title: "How to create an abandoned site flow with email and SMS"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/21137997887771-How-to-create-an-abandoned-site-flow-with-email-and-SMS"
section: "Browse abandonment flows"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-04-21T13:54:33Z"
language: en
---

## You will learn

Learn how to create an abandoned site flow with email and SMS. This flow is the first step in the customer journey, sending before even a browse abandonment flow. It includes anyone who visited your website, but didn’t look at or buy any products.

These site abandoners are likely on the search for deals or are browsing quickly. To convince them to come back, create a site abandonment flow to show these shoppers fantastic deals, share new arrivals, or provide assistance.

You can set up a similar flow for push notifications. However, you need a custom metric, such as **Opened app**, to set as the trigger.

## Before you begin

There are a few things to note before building a site abandonment flow (also called a site bounce flow):

- You must already have Klaviyo [onsite tracking](https://help.klaviyo.com/hc/en-us/articles/115005076767) for your website (which is automatically installed for most ecommerce stores).
- If using SMS, stay compliant by:
  - Only including 1 SMS per recipient in this flow.
  - Sending the SMS within 48 hours of someone abandoning the site.

## Create an abandoned site flow

1. 1. Navigate to ****Flows > Create Flow > Build your own****.
   2. In the modal that appears, name the flow (e.g., “Abandoned site”).
   3. Select ****Create flow****.
   4. In the flow builder, select ****Metric**** from either the **Recommended** or **All triggers** tab.
   5. To select the metric, open the dropdown menu and select ****Active on site****.
      ![Searching for the Active on site trigger](https://klaviyo.zendesk.com/hc/article_attachments/28720903363227)
   6. Click ****Add flow filter > Add flow filter****.
   7. Add the following filters:
      - **What someone has done (or not done) > Active On Site zero times since starting this flow**
      - **What someone has done (or not done) > Viewed Product zero times since starting this flow****AND**
      - **What someone has done (or not done) > Started Checkout zero times since starting this flow**
        **AND**
      - ****What someone has done (or not done) > Placed Order zero times since starting this flow****AND****
      - **Has not been in this flow > in the last 30 days** **![](https://klaviyo.zendesk.com/hc/article_attachments/30461643531675)**
   8. [Shopify](https://help.klaviyo.com/hc/en-us/articles/115001396711) and [BigCommerce](https://help.klaviyo.com/hc/en-us/articles/360024310292) users: if you enabled **Added to Cart** tracking, use the following filter, along with the **AND** condition.
      - **What someone has done (or not done) > Added to Cart zero times since starting this flow
        ![](https://klaviyo.zendesk.com/hc/article_attachments/30461643532059)**
   9. Select ****Save****.
   10. Put a time delay directly after the trigger and set it to wait 15 minutes.
   11. Add an email after the time delay.
       ![Example of an abandoned site flow after the first email has been added](https://klaviyo.zendesk.com/hc/article_attachments/28720898075931)
   12. Create the content for your message that incentivizes browsers to come back and buy something (e.g., “Want a great deal?”) as well as shows off new or popular products.
   13. Below the email, add a time delay that waits 1 day.
   14. Drag in a split below the 1-day time delay and set it to: **If someone is or is not consented to receive SMS > is**.
       ![How the flow looks once you added the consented to SMS split after the first email](https://klaviyo.zendesk.com/hc/article_attachments/28720903365147)
   15. On the YES path, add an SMS.
   16. Create the content for the SMS and remind the user of the incentive from the first email. (e.g., “Don’t miss out on your 15% off! Use code GET15 before it’s gone for good”).
   17. On the NO path, place an email.
       ![Showing the flow's configuration once the second email is added](https://klaviyo.zendesk.com/hc/article_attachments/28720903371419)
   18. In the second email, craft the content to remind recipients of the incentive from the first email and talk about your mission, offer assistance, etc.
   19. Select ****Review and turn on**** to set the flow live.

You’ll see a high number of skips from this flow. This is expected, as you don’t want this flow to send to anyone who views an item, adds it to their cart, or purchases. Instead, you’ll want those people to enter in your [browse abandonment](https://help.klaviyo.com/hc/en-us/articles/115002775252), [abandoned cart](https://help.klaviyo.com/hc/en-us/articles/115002779411), and [post-purchase flows](https://help.klaviyo.com/hc/en-us/articles/360028872611), respectively.

## Additional resources

- Learn how to create other flows:
  - [Product review](https://help.klaviyo.com/hc/en-us/articles/115002779391)
  - [Price drop](https://help.klaviyo.com/hc/en-us/articles/4404249033755)