---
id: 12414318812827
title: "Troubleshooting a list- or segment-triggered flow"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/12414318812827-Troubleshooting-a-list-or-segment-triggered-flow"
section: "Troubleshooting flows"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-04-21T13:56:41Z"
language: en
---

Learn how to troubleshoot a list-triggered or segment-triggered flow when you notice that it is behaving differently from expected.

Flows are highly customizable and can vary in complexity. The information in this guide is designed to be broad, and will mainly cover common issues that can apply to most Klaviyo accounts.

Please review the troubleshooting scenarios below to see if any are relevant to your issue before asking for assistance.

## How do I know if my flow is list- or segment-triggered?

Follow these steps to confirm whether your flow is a list- or segment-triggered:

1. Click on the trigger of the flow in the flow builder.
2. View the top section of the details sidebar to see if the flow is triggered by a list or a segment and the name of the list or segment.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/46897424418843)
3. Click on the name to view it in the **Lists & segments** tab.

Common list-triggered flows:

- Welcome series flow
- Contest or giveaway flow

Common segment-triggered flows:

- Sunset flow
- VIP segment flow

### Who can receive emails from my flow?

Before you begin troubleshooting, [understand consent in profiles](https://klaviyo.zendesk.com/hc/en-us/articles/360037101072). Consent status determines who can and cannot receive emails. Customers who have unsubscribed can't receive emails from a flow unless they are [marked as transactional](https://klaviyo.zendesk.com/hc/en-us/articles/360003165732).

## General troubleshooting steps

### Use pre-built flows to avoid issues

To avoid issues with common flow types, we recommend creating your first flows using the pre-built templates from our [flow library](https://help.klaviyo.com/hc/en-us/articles/115002774932-Getting-started-with-flows#choose-a-pre-built-flow-from-the-library3) and adjusting the content to match your branding.

### If flow messages are not sending, check the flow status

Make sure that your messages are set to **Live** status in order to start sending out to customers. If your messages are set to **Draft** they will not send nor will they queue profiles in a waiting list. If they are set to **Manual** status, the messages will queue profiles, but will not send out the messages until you manually send them.

If your messages are currently or were previously set to **Manual** status, follow these steps to send messages manually:

1. Click on a flow message that was previously manual.
2. In the **Performance**section of the details sidebar, click ****View details****.
3. Navigate to ****Recipient activity****> ****Needs Review****.
4. This will take you to a list of profiles that reached the message in the flow when it was set to **Manual** status.
5. You can individually preview, send, and/or cancel each email and SMS that requires your review.
6. If you have a lot of recipients that need review, you can bulk send and cancel messageswith the ****Send All**** and ****Cancel All**** buttons, respectively. If you send an email or SMS to a contact who is in Needs Review and no longer meets the filters for the flow, they will be skipped and will not receive the message.
   ![The Needs review tab.](https://klaviyo.zendesk.com/hc/article_attachments/39575759138459)
7. To send the message automatically moving forward, set it to **Live** status by clicking on the status dropdown for the message in the flow builder.
   ![Message status dropdown found when clicking on a message card.](https://klaviyo.zendesk.com/hc/article_attachments/39575783718811)

### For previously working flows, review the flow’s changelog

If your flow was working previously, but you have recently noticed changes in behavior, you should first look at the flow’s changelog. This is especially important for older flows and accounts with multiple users. If you notice that a flow’s behavior has changed after a certain date and time, the changelog will be able to tell you the following:

- What changed
- Who made the change
- When the change took place (date and time in your account’s timezone)

If changes coincide with when you started experiencing issues with your flow, it is likely that the change is the source of the issue.

Follow these steps to view a flow’s history:

1. In the header bar, click on the ****View flow history****icon button.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/46897446787995)
2. This will open the **Flow history** panel on the right-hand side of the screen.

Find out more about the Flow History panel in our article on [how to review the changelog for a flow](https://help.klaviyo.com/hc/en-us/articles/4402385748635).

### Understand flow skip reasons

If you are seeing a large number of skipped profiles in your flow, learn [why a flow message skipped a profile.](https://klaviyo.zendesk.com/hc/en-us/articles/1260805003210)

## Troubleshooting scenarios

### List- or segment-triggered flow is not sending to anyone

****Check that the trigger is set to the correct list or segment****

Since it is possible to create lists and segments with similar names, check that the flow is associated with the list or segment you intended.

1. In the flow builder, click on the trigger of the flow.
2. In the details sidebar, click the list name to view the list in the **Lists & segments** tab.
   ![Sidebar of the flow builder showing the list that triggers the flow.](https://klaviyo.zendesk.com/hc/article_attachments/39575783723803)
3. Confirm that the list or segment associated with your flow is the one that you originally intended.
4. If the list or segment is incorrect, and your flow should be associated with a different one, clone the flow in order to change the trigger. See our article on [how to change a flow trigger](https://help.klaviyo.com/hc/en-us/articles/115002775052-How-to-change-a-flow-trigger).

****Check that the list or segment is collecting new profiles****

You may need to confirm that profiles are entering the list or segment that triggers the list. Use the method described in step 4 above to view the list or segment within your account’s **Lists & segments** tab. If you confirm that the list is the one you intended, but no profiles are entering the list, check the following that apply:

1. Make sure that your ecommerce integration is installed and enabled. See the list of [ecommerce integration guides](https://help.klaviyo.com/hc/en-us/categories/115000032731) in our Help Center for reference.
2. Make sure that any sign-up forms you are using are published and not set to **Draft**.
3. Make sure that your sign-up forms are [associated with the correct list](https://help.klaviyo.com/hc/en-us/articles/360026474752) by clicking on the submit button.
4. For uploaded profiles, make sure to follow our the formatting in our guide on [how to create and add subscribers to a new list](https://help.klaviyo.com/hc/en-us/articles/115005078967-How-to-create-and-add-subscribers-to-a-new-list).
5. For segments, make sure that the conditions are set up as you intended, and that none of the conditions cancel each other out. This includes making sure to use OR connectors when being inclusive and AND connectors when being exclusive. See our [AND vs. OR Guide](https://help.klaviyo.com/hc/en-us/articles/360036534631-AND-vs-OR-Guide) for more details.

### List- or segment-triggered flow is only sending to part of the list or segment

If you have a lis-t or segment-triggered flow such as a welcome series flow or VIP flow, and this flow is only sending to some profiles in your list, check the following:

****Understand what will not trigger a flow****

There are ways that profiles can be added to a list or segment that won't trigger a flow, including:

- [Merging profiles](https://help.klaviyo.com/hc/en-us/articles/115005073847#h_01HCDC8PJ76QR9X311KFY815TY)
- [Merging lists](https://help.klaviyo.com/hc/en-us/articles/115005078887)
- Adding profiles to a list through an integration with backdated consent

If any of these actions took place in your account, this may be why some profiles in the related list or segment didn't enter the flow.

****Check your flow filters****

If you have any flow filters configured, make sure that they are filtering as intended by following these steps:

1. Click on the trigger of the flow in the flow builder.
2. Click ****Preview**** in the details sidebar.
   ![The Preview button](https://klaviyo.zendesk.com/hc/article_attachments/39575783724699)
3. The trigger preview will show whether or not profiles are passing the profile filters and why.
4. If there are profiles in the preview that are not passing the filters but should be, click the trigger again and click ****Edit**** in the **Profile filters** section of the details sidebar.
5. Make sure your profile filter conditions are checking the properties and events you intended.
6. Make sure none of your conditions are contradicting as they may be canceling each other out.

****If you're adding profiles manually, check how they are being added to the list****

Profiles who are added to a list through the "Add to list" option on a profile page will **not** trigger a flow.

![add to list](https://klaviyo.zendesk.com/hc/article_attachments/39575783727259)

If you want to trigger a flow by adding a single profile:

1. Navigate to ****Audience > Lists & segments****.
2. Click the name of the list you'd like to add someone to.
3. Click ****Quick add****and fill out the appropriate information. If you are adding an existing profile, only fill out the email field.
4. Click ****Add profile****. This will not trigger double opt-in, but it will add the profile to the list and trigger any flows associated with the list.

****If you are using an integration, check how subscribers are being added through the integration****

The integrations below have some limitations or settings related to list subscriptions:

- ****Mailchimp****
  It isn’t possible to trigger flows off of lists that are synced through Mailchimp. If you are syncing all of your subscriber lists from Mailchimp, you will not be able to configure flows to send to these subscribers as they opt in.
- ****Shopify****
  In order for people to trigger your welcome series flow when they subscribe through Shopify forms or checkout, you must select the option on the Shopify integration page to add subscribers to a list. Navigate to ****Integrations > Shopify > Sync settings**** and select a list for email and SMS susbcribers.
  ![Configuration page for the Shopify integration.](https://klaviyo.zendesk.com/hc/article_attachments/39575783729179)
- ****BigCommerce****
  In order for people to trigger your welcome series flow when they subscribe through BigCommerce forms or checkout, you must select the option on the BigCommerce integration page to **Collect email subscribers** and choose the appropriate list associated with your flow. For SMS, select the option to **Collect SMS Subscribers**.
  ![Bigcommerce list subscription settings](https://klaviyo.zendesk.com/hc/article_attachments/39575759147163)

### Sunset flow is not sending to anyone

If you created a sunset flow, but no one has been receiving messages from the flow, check the following:

****Make sure your sunset segment is configured properly****

Review our guide on how to create a sunset flow, particularly the section on [creating the sunset segment](https://help.klaviyo.com/hc/en-us/articles/360017518492#set-up-a-sunset-segment2)****.**** Make sure that the conditions and connectors match the example shown in the guide. It’s possible to mix up the [AND vs OR](https://help.klaviyo.com/hc/en-us/articles/360036534631) connectors, which will prevent the proper profiles from qualifying for your segment.

****Adjust your segment’s time requirement****

If you notice that profiles have not been added to your sunset segment, it may be possible that you don’t have any profiles that are old enough to be added. For example, if you configured your sunset segment to collect profiles that have been unengaged for 90 days, but your oldest profiles have only been in your account for 60 days, then no profiles will be added.

Try modifying the time requirement of your sunset segment to see if this causes profiles to be added.

****Try adding past profiles to your flow****

Segment-triggered flows will only trigger when someone is added to the segment organically. If a large amount of profiles were added to your sunset segment the moment you created the segment because they fit the conditions in the past, they will not automatically trigger your sunset flow. You can [add past profiles to the flow](https://help.klaviyo.com/hc/en-us/articles/360049924272) to manually add these profiles into the flow.

## Help us improve this article

If you believe helpful information is missing from the troubleshooting scenarios listed above, please provide feedback so that we can improve the Help Center experience and provide better support for you and other customers.

If you were not satisfied with the troubleshooting steps provided here, select ****No**** from the bottom of the article. The following form will ask you for more information which we can use to improve.

When providing feedback, please include the following:

1. What feature you are using and what you are trying to do (create a welcome flow, send an SMS campaign, edit a popup form, etc.).
2. What specific issue you are encountering that couldn't be resolved using the steps in this article.

## Reach out for assistance

If you are still encountering issues after consulting this article, please [create a post in our Community forums](https://community.klaviyo.com/got-a-question-1) or [reach out to our support team](https://help.klaviyo.com/hc/en-us/articles/115001002272-How-to-Contact-Support).