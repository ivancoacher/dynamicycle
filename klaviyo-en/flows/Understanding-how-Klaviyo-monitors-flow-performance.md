---
id: 15768091187227
title: "Understanding how Klaviyo monitors flow performance"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/15768091187227-Understanding-how-Klaviyo-monitors-flow-performance"
section: "Test and optimize flows"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-04-21T13:54:29Z"
language: en
---

## ****You will learn****

Learn how Klaviyo monitors and alerts you of unusual drops in performance for your flows. When a flow’s send rate significantly drops, you will be alerted so you can troubleshoot the potential issue. This type of monitoring is also known as anomaly detection.

## ****How flow performance monitoring works****

Klaviyo will alert you if your flow has a drop in volume of message received events compared to historical data for your account. This includes rates for the following message types:

- Email
- SMS

When an unusual drop in metric activity is detected, you will be notified in different ways:

- In-app notification on the home page![alert.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28720901910171)
- Notification banner on the metrics page for the specific message received event
  ![metric page.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28720901913755)

## ****Dismiss or suppress alerts****

If the drop in activity is expected or is already under investigation, you can dismiss or suppress alerts to prevent them from showing in your account.

- Dismissing an alert will cause the alert message to disappear until it is triggered again.
- Suppressing an alert will prevent the alert from triggering again for that metric until the amount of time specified.

To dismiss an alert:

1. If you are on the **Home** tab, navigate to the affected flow by clicking ****View metric**** on the alert. Find the affected metric by navigating to ****Analytics > Metrics**** and selecting ****Received Email**** or ****Received SMS**** from the main Klaviyo navigation.
2. On the top right of the alert card, click ****Dismiss****.

To suppress an alert:

1. If you are on the **Home** tab, navigate to the affected flow by clicking ****View metric**** on the alert. Find the affected metric by navigating to ****Analytics > Metrics**** and selecting ****Received Email**** or ****Received SMS**** from the main Klaviyo navigation.
2. Click the arrow next to the ****Dismiss**** button.
3. Click one of the following options:
   - ****Suppress for 30 days****
   - ****Suppress for 60 days****
   - ****Suppress for 120 days****
   - ****Suppress for 365 days****

After choosing a suppression option, a success message will appear with the date when the suppression expires. Once the suppression period is over, if drops in activity are still detected, alerts will continue to trigger until you suppress them again.

## ****Troubleshoot a sudden drop in performance****

While a sudden drop in activity can be alarming, there are some common explanations for this occurrence. Causes specific to your ecommerce store include:

- Maintenance on your store or its server
- Temporary server outages for your ecommerce platform

If your store is offline, your Klaviyo account will not receive new subscribers or metric activity so this will cause a drop in send rate. Check your store’s settings or internal logs for any scheduled maintenance. If you are hosted on a paid platform, such as Spotify or BigCommerce, check their status page for information on server outages and downtime.

For causes that are specific to Klaviyo, review the sections below. Click on the section title to see more information. In some cases, multiple scenarios may apply. If you are unsure which case applies to your issue, review them all.

### ****Have you changed any profile filters?****

First, check your filters to see if they are causing profiles to leave the flow. To do so, follow these steps:

1. Click on the trigger of your flow.
2. In the left sidebar, click ****Preview Trigger Setup****.
3. In the preview modal, review profiles that would trigger your flow and if they qualify for your profile filters.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28720896543899)
4. If you notice many profiles are failing your profile filters when they should be entering the flow, check your profile filters to make sure they are set up the way you intended.
5. If necessary, change your profile filters by clicking ****profile filters**** in the left sidebar when viewing the flow trigger.

If you are unsure if a change has been made to your flow, you can check the flow’s changelog. If the timestamp of the changes coincide with when you started experiencing issues with your flow, it is likely that the change is the source of the issue.

Follow these steps to view a flow’s history:

1. In the top bar, click the ****View flow history**** icon.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/46896468483995)
2. View the Flow history panel on the right-hand side of the screen.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/46896468487323)
3. Review the changelog to see if any of the flow’s filters have changed recently.

Find out more about the Flow History panel in our article on [how to review the changelog for a flow](https://help.klaviyo.com/hc/en-us/articles/4402385748635).

### ****Have you changed your sender address? (Email)****

Your sender address should match your website domain; otherwise, this can lead to issues with sending. For example, if your website URL is example.com, your sender email address should end in @example.com. Emails sent using a personal email address domain (such as @gmail.com, @yahoo.com, or @outlook.com) will be blocked from sending.

To check your sender address:

1. Click on an email in your flow.
2. Click ****Edit**** in the left sidebar.
3. Check the address entered in the ****Sender email address**** field.
   ![sender_info.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28720896539291)
4. Change this address if necessary.

### ****Have you updated your message content?****

If you have updated the content of your messages, make sure that the content abides by [email deliverability best practices](https://help.klaviyo.com/hc/en-us/articles/12034571748251) in order to avoid spam filters.

- Avoid spammy subject lines, such as "JUST THIS ONCE FOR A LIMITED TIME ONLY"
- Find a balance between images and text.
- Limit the number of URLs.
- Avoid adding unnecessary code to messages.
- Use dynamic variables to personalize messages.

Learn more about [deliverability best practices](https://help.klaviyo.com/hc/en-us/articles/115005247008/#email-deliverability-best-practices4).

### ****For welcome series or other list-triggered flows, are you still receiving new subscribers?****

Welcome series flows and other list-triggered flows are triggered when a subscriber joins a specified list.

To make sure your list is still receiving new subscribers:

1. Click on the trigger of the flow.
2. In the left sidebar, click the name of the list that triggers your flow.
3. In the **Date added** column, check the last time a profile was added.
4. If new profiles haven’t been added to your list in a long time, make sure any sign-up forms associated with your list are still visible on your website.

### ****Have you run out of coupon codes?****

If you are using Shopify or Magento, you can automatically generate new coupon codes to avoid running out. This issue only applies if you are using the option to upload coupon codes.

For flow messages that contain a dynamic coupon code, the message will not be sent if there are no more coupon codes left.

To check how many coupon codes you have left:

1. Using the main Klaviyo navigation bar, navigate to ****Content > Coupons****.
2. Click ****Uploaded Coupons****.
3. See the **Available/Total** column on the right of the coupon to check how many coupon codes are left.
4. If no codes remain, click the action button on the far right and choose ****Add Coupons**** to upload more.

Learn more from our article on [getting started with coupon codes](https://help.klaviyo.com/hc/en-us/articles/115005084727).

### ****For segment-triggered flows, have you changed your segment definition?****

If your flow is triggered by a segment, a change in the segment definition can prevent new profiles from entering the segment, thus causing a drop in flow sending.

To make sure your segment is still receiving new members:

1. Click on the trigger of the flow.
2. In the left sidebar, click the name of the segment that triggers your flow.
3. If there are profiles in the segment, check the **Date added** column to see the last time a profile was added.
4. If there are no profiles in the segment or new profiles haven’t been added in a long time, click ****Edit Definition**** to view the segment’s definition.
5. Make sure:
   1. The segment definition is configured to capture the people you intend.
   2. None of the segment conditions contradict each other like the example below. In this example, there’s a condition that checks if someone opened an email at least once as well as a condition that checks if someone has also never opened an email. Since someone can’t fulfill both conditions simultaneously, no one will enter the segment.
      ![segment.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28720896541851)
6. If necessary, change the segment definition and click ****Update Segment****.
7. Segment-triggered flows only trigger when people enter the segment organically. If people enter the segment due to a change in definition, you will have to [manually send older profiles through the flow](https://help.klaviyo.com/hc/en-us/articles/360049924272).

### ****See troubleshooting guides for specific flow types****

For more troubleshooting scenarios, please see these guides for specific flow types:

- [Troubleshooting a list- or segment-triggered flow](https://help.klaviyo.com/hc/en-us/articles/12414318812827-Troubleshooting-a-list-or-segment-triggered-flow)
- [Troubleshooting a metric-triggered flow](https://help.klaviyo.com/hc/en-us/articles/12278373016603-Troubleshooting-a-metric-triggered-flow)

## ****Reach out for assistance****

If none of the above scenarios apply to your issue, please post in our [community forums](https://community.klaviyo.com/) or reach out to [Klaviyo support](https://help.klaviyo.com/hc/en-us/articles/115001002272).

## ****Additional resources****

Learn how to troubleshoot specific types of flows:

- [Troubleshooting a list- or segment-triggered flow](https://help.klaviyo.com/hc/en-us/articles/12414318812827)
- [Troubleshooting a metric-triggered flow](https://help.klaviyo.com/hc/en-us/articles/12278373016603)