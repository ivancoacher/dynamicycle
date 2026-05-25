---
id: "360034500652"
title: "How to use WooCommerce data in flows"
source_url: "https://help.klaviyo.com/hc/en-us/articles/360034500652-How-to-use-WooCommerce-data-in-flows"
section: "Getting started with WooCommerce"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:45Z"
language: "en"
---
## You will learn

Learn how to use data from Klaviyo's WooCommerce integration within your flow emails. When you integrate your WooCommerce account with Klaviyo, you'll have access to customer and purchase data that you can use to personalize your customers' experience.

To see what events we sync from WooCommerce, see our article on [reviewing your WooCommerce data](https://klaviyo.zendesk.com/hc/en-us/articles/360030732832).

## Pre-built flows

We offer a variety of pre-built flows in the Klaviyo flow library. To get there, head to ****Flows > Create Flow**** in Klaviyo. These flows include all the event data you'll need pre-filled in each template. Some of our most popular pre-built flows for WooCommerce are listed in the table below:

|  |  |  |
| --- | --- | --- |
| Flow Name / Link(s) | Flow Trigger | Notes |
| [Abandoned Cart Reminder (Standard, Email and SMS)](https://www.klaviyo.com/library/flows?object_id=VEgT68)  [Abandoned Cart Reminder (Standard, Email only)](https://www.klaviyo.com/library/flows?object_id=JDzXbb) | Started Checkout | Abandoned cart flows can use either **Started Checkout** or **Added to Cart** as the trigger; our standard flow uses **Started Checkout**. |
| [Abandoned Cart Reminder (Added to Cart trigger, Email and SMS)](https://www.klaviyo.com/library/flows?object_id=UrgZwA) | Added to Cart | Customers who've clicked **Added to Cart** but haven't started a checkout may have been browsing more casually. |
| [Browse Abandonment (Standard, Email and SMS)](https://www.klaviyo.com/library/flows?object_id=VGYirB)  [Browse Abandonment (Standard, Email Only)](https://www.klaviyo.com/library/flows?object_id=Lc85Du) | Viewed Product | Klaviyo is only able to track the browsing activity of "known browsers" which are browsers who have visited and engaged at least once before. There are two key ways we are able to identify a site visitor: if someone has clicked through a Klaviyo email to your website, or if someone has subscribed or opted-in through a Klaviyo form. |
| [Product Review / Cross-sell (Standard, Email only)](https://www.klaviyo.com/library/flows?object_id=HgTBs2) | Fulfilled Order | You can personalize your winback emails with catalog or product feeds. For more information review [Product Feeds and Recommendations](https://klaviyo.zendesk.com/hc/en-us/articles/115005082787). |
| [Customer Winback (Standard, Email only)](https://www.klaviyo.com/library/flows?object_id=Nsiv5N) | Placed Order | Consider [back-populating](https://help.klaviyo.com/hc/en-us/articles/115002779231-Back-Populate-a-Flow) your winback flow after setting it up to ensure that anyone who purchased a long time ago but hasn't purchased since can receive your winback series in a timely fashion. |

Note that to use pre-built flows utilizing SMS, you must first [set up Klaviyo SMS.](https://help.klaviyo.com/hc/en-us/articles/4404274419355-How-to-turn-on-SMS-in-Klaviyo)

## Build flows from scratch

1. To build a flow from scratch, navigate to the ****Flows**** tab in Klaviyo.
2. Click ****Create Flow****.
3. Select ****Build your own****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/33639117493147)
4. Name your flow, add any tags, and click ****Create Flow****.
5. Next, design your flow. You can trigger your flow based on any events synced from WooCommerce.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/33639088668315)
6. To learn more about flow triggers and filters, and adding steps to your flow, consult our [Getting started with flows guide](https://help.klaviyo.com/hc/en-us/articles/115002774932#h_01H9JGTZ8QEJ4GJ70BSKS4DNWQ).
7. Next, you'll create [flow email content](https://help.klaviyo.com/hc/en-us/articles/115002774992) (or SMS content if desired). Consult the section below to learn how to add personalization using WooCommerce event variables.
8. When you're done designing your flow emails, you're ready to learn how to [set your flow live](https://help.klaviyo.com/hc/en-us/articles/115002774932#h_01H9JGTZ8RVQANQHGVRJ6V4W63).

## How to find event variables

### Emails

To add event variables in a flow email:

1. Open the email in the flow editor.
2. Click ****Edit email****.
3. Click ****Preview & test****.
4. Click on a property name from the **Event Properties** menu to copy it.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28715969828763)
5. Paste the tag into your flow email.

This preview window will show all of the data available for that particular event metric. List entries are numbered starting at 0. For instance, if **{{ event.extra.line\_items.0.product.name }}** is the variable entry for an image, the 0 indicates that it is the first item in the array.

To use event variables, you must copy them exactly. Event variables are case-sensitive, and the slightest deviation from how it appears in the preview window could cause the variable not to work.

### SMS

1. In the flow builder, click the SMS or MMS you want to add an event variable to.
2. Next, click ****Configure Content****.
   ![Inside an SMS or MMS event variable in a flow, below the section for Content a button for Configure Content so you can add an event variable](https://klaviyo.zendesk.com/hc/article_attachments/28715969808411)
3. Click ****Configure Content**** to view where you can add text, emojis, static or [dynamic images](https://help.klaviyo.com/hc/en-us/articles/1260806102230), and GIFs to your message. Here, you can also insert profile personalization and event variables.
4. You can find event variables on the right-hand side of the screen in the **Previewing** tab. This tab shows the 10 most recent events that you can navigate between; e.g., for a post-purchase flow, the 10 most recent **Placed Order** events will show here.
5. The **Previewing** tab will also show all the associated event variables. To view the variables, click the ****View details**** button in the upper right-hand corner of the tab.
   ![When inside an SMS or MMS, navigate to the Previewing tab in the upper right-hand side and hovering on the info icon to see the View Details action](https://klaviyo.zendesk.com/hc/article_attachments/28715963229211)
6. This dropdown contains information on all of the variables for that event. By clicking any line item, you can automatically copy it to your clipboard, making it easy to add event variables into your message.
   ![Inside the Previewing tab in the upper-right-hand side, click on the info icon to expose the Event Properties details below in the modal](https://klaviyo.zendesk.com/hc/article_attachments/28715963233179)

### Common event variables for WooCommerce

The syntax for different event variables depends on both the integration and event metric. You can see the syntax for all of the available variables for a given event by scrolling through the preview window and clicking on the different entries.

Some common examples of variables by integration are listed below for a **Started Checkout** event. Keep in mind that the exact variable may differ depending on the metric used to trigger the flow.

|  |  |
| --- | --- |
| ****WooCommerce**** | |
| ****Product Name/Title**** | {{ event.extra.Items.0.Name }} |
| ****Product URL**** | {{ event.extra.Items.0.URL }} |
| ****Image**** | {{ event.extra.Items.0.Images.0.URL }} |
| ****Price for Product**** | {{ event.extra.Items.0.LineTotal }} |
| ****Quantity**** | {{ event.extra.Items.0.Quantity }} |
| ****Total**** | {{ event.extra.Items.0.TotalWithTax }} |

You can [rebuild carts from an abandoned cart flow in WooCommerce](https://help.klaviyo.com/hc/en-us/articles/115005255808#01H8KXY3BCY0H4YDBT43XHS3R4) by using the parameter `?wck_rebuild_cart={{ event.extra.CartRebuildKey }}`.

## Are you using Amazon Buy with Prime?

If you're using Buy with Prime to power payment and fulfillment for any of the products on your store, you'll need to make some additions to your flows (whether pre-built or scratch), and create some new flows. First:

- [Integrate Buy with Prime with Klaviyo](https://help.klaviyo.com/hc/en-us/articles/14708088221467) to bring Buy with Prime data into your Klaviyo account.

For your abandoned "Started Checkout" flow:

- Create two separate abandoned cart flows: one triggered by WooCommerce's checkout event (the pre-built flow listed above), and one triggered by Buy with Prime's checkout event. For your Buy with Prime flow, read [How to create an abandoned cart flow for Amazon Buy with Prime](https://help.klaviyo.com/hc/en-us/articles/14985388418331).
- For your WooCommerce abandoned cart flow, add the following flow filter to exclude customers who made purchases via Buy with Prime from receiving incorrect messaging:
  - **Placed Order** (Buy with Prime) **zero times since starting this flow.**

For your abandoned "Added to Cart" flow:

- Add the following flow filters to exclude customers who started checkouts or made purchases via Buy with Prime from receiving incorrect messaging:
  - **Started Checkout** (Buy with Prime) **zero times since starting this flow** AND
  - **Placed Order** (Buy with Prime) **zero times since starting this flow.**
- No second flow for Buy with Prime is needed, since Buy with Prime does not have an **Added to Cart** event.

For your browse abandonment flow:

- When you create your browse abandonment flow (you only need to create one flow, since it's triggered by the **Viewed Product** event) add the following flow filters to incorporate Buy with Prime data into your flow:
  - **Checkout Started** (Buy with Prime) **zero times since starting this flow**AND
  - **Placed Order**(Buy with Prime)**zero times since starting this flow**.

For your customer winback flow:

- Create two separate winback flows: one triggered by WooCommerce's **Placed Order** event (as listed above) and one triggered by Buy with Prime's **Placed Order** event to account for customers who placed their original order with Buy with Prime. For your Buy with Prime winback flow, read [How to create a winback flow for Amazon Buy with Prime](https://help.klaviyo.com/hc/en-us/articles/15156331062171).
- When you create your WooCommerce winback flow, add the following flow filter to exclude customers who made purchases via Buy with Prime from receiving incorrect messaging:
  - **Placed Order** (Buy with Prime) **zero times since starting this flow.**

## Additional resources

Learn more about WooCommerce:

- [WooCommerce data reference](https://klaviyo.zendesk.com/hc/en-us/articles/360030732832)
- [How to set up coupons for WooCommerce](https://klaviyo.zendesk.com/hc/en-us/articles/360031279471)
- [Troubleshooting Your WooCommerce Integration](https://klaviyo.zendesk.com/hc/en-us/articles/4515829067803)