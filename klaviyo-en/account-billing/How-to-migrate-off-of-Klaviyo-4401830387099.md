---
id: "4401830387099"
title: "How to migrate off of Klaviyo"
source_url: "https://help.klaviyo.com/hc/en-us/articles/4401830387099-How-to-migrate-off-of-Klaviyo"
section: "Account troubleshooting"
category: "Account & billing"
category_slug: "account-billing"
klaviyo_updated: "2026-04-21T13:54:57Z"
language: "en"
---
## You will learn

Learn which steps to take when you're migrating off of Klaviyo, regardless of whether you're changing to another provider for SMS, email, or both.

If you cancel your SMS plan but continue to use Klaviyo for email, only follow the steps outlined in the SMS section below. If you are migrating away from Klaviyo entirely (for both SMS and email) follow all steps outlined in this document.

## How to migrate off Klaviyo

1. Turn off or update your flows
2. Cancel your scheduled campaigns
3. Turn off or update your signup forms
4. Export your contacts

   - SMS subscribers
   - Email list
   - Email suppression list
   - All SMS or email segment
5. SMS: remove or port your number to your new provider
6. SMS: audit your custom keywords
7. Email: export your templates
8. Remove or update your hosted pages
9. Remove code snippets
10. Disable your integrations
11. Export your analytics
12. Cancel your account

## Turn off or update your flows

If you would like to continue using Klaviyo for email but not SMS or vice versa, you must check each flow and remove either all the SMS messages or all the emails. You can either delete these messages or set the messages to Draft. Audit each of your flows and update all flow [filters](https://help.klaviyo.com/hc/en-us/articles/115002779051#setting-trigger-filters3), [branches](https://help.klaviyo.com/hc/en-us/articles/115003883992#the-trigger-split-and-conditional-split1), and [message statuses](https://help.klaviyo.com/hc/en-us/articles/360035014492#change-an-sms-message-s-sending-status4).

If you are migrating away from Klaviyo completely (i.e., stopping both email and SMS), turn off any flows you have live by deleting them or by turning them to draft. We recommend turning the flows to draft mode, as you cannot recover flows (or their data) once they're deleted.

To turn a flow to draft:

1. Click into the flow
2. Click ****Manage Flow > Update All Action Statuses**** to set your flow to Draft.

## Cancel your scheduled campaigns

If you have any scheduled campaigns that you would like to cancel:

1. Head to the ****Campaigns**** tab.
2. Filter by the status **Scheduled.**
3. Individually delete the campaigns in the dropdown.

## Turn off or update your signup forms

If you plan to continue using Klaviyo for one channel (SMS but not email or vice versa), make sure to edit your signup forms to no longer collect email or consent for phone numbers, if applicable. If you have email- or SMS-only forms, delete them or set them to draft.

If you are migrating away from Klaviyo completely, you can turn off your signup forms by either setting them to draft or deleting them. Note that deleting your forms will permanently erase all data about them.

## Export your contacts

Below are the lists and segments, you'll want to make sure to bring with you to you new platform. To export any list or segment:

1. Click into the list or segment (under ****Audience > Lists & Segments****).
2. Select the ****Manage List**** dropdown.
3. Choose ****Export List to CSV****.

   - If you do not see this option, it means your role doesn't have the correct permissions to do so; only Owner, Admin, and Analyst users can export lists and segment.
4. Choose the properties you want to export.
5. Navigate to ****Settings**** ****> Other > Downloads**** to access exports from the last 30 days.

### SMS subscribers

In order to bring your SMS contacts over to your new platform and maintain a full audit trail, you’ll need to export them from Klaviyo.

We recommend exporting the SMS consent timestamp and phone number for each contact, along with any other fields you choose. Upload this CSV file containing your SMS consent data to your new provider per the new provider’s instructions.

### Email list

When migrating to a new platform, it will be helpful to have all your email contacts in one place.

### Email suppression list

You may want to export your [suppression list](https://help.klaviyo.com/hc/en-us/articles/115005246108) from Klaviyo in order to upload it to your new platform. To export your suppression list:

1. Navigate to ****Audience >********Profiles****
2. Click ****Suppressed Profiles**** in the upper right corner.
3. Click ****Export CSV****.

![Exporting your email suppressions](https://klaviyo.zendesk.com/hc/article_attachments/28720848875419)

### Other SMS or email segments

Check on your other lists and segments. For instance, you may want to export your [engaged](https://help.klaviyo.com/hc/en-us/articles/115000200072) or [VIP](https://help.klaviyo.com/hc/en-us/articles/115005065707) segments.

## SMS: remove or port your number to your new provider

### Port your number

If you wish to keep the sending number you use with Klaviyo, you will need to port this number over to your new SMS provider. In order to export a number from Klaviyo, please contact your new SMS provider to initiate the porting request. Then, if you need any information about your SMS phone number or Klaviyo account in order to complete your porting request with your new provider, please [reach out to support](https://help.klaviyo.com/hc/en-us/articles/115001002272).

Porting is not available for branded sender IDs. However, you can use simply create the same sender ID with your new SMS provider. This way, your messages will still show as coming from your brand.

### Remove your number

If you do not wish to keep your sending number, you can remove it. When you remove a number, you are releasing it, so you won't still receive texts.

Note that removing a number is permanent and irreversible.

To remove your number:

1. Click your account name in the bottom left.
2. Navigate to ****Settings > SMS****.
3. Click the 3-dot dropdown menu.
4. Select ****Remove****.

![](https://klaviyo.zendesk.com/hc/article_attachments/30673605908763)

## SMS: audit your custom keywords

Audit any existing [custom keywords](https://help.klaviyo.com/hc/en-us/articles/360050384091#update-a-custom-keyword3) you’ve configured within Klaviyo and remove any reference to those keywords on your website, email banners, or any in-store advertisements.

## Email: export your templates

To export the HTML of any of your email templates for future use:

1. Navigate to ****Content > Templates****.
2. Locate the template you want to export.
3. Click additional options menu on the right.
4. Click ****Export****.

## Remove or update your hosted pages

If you plan to continue using Klaviyo for a single channel (email or SMS), edit your [custom hosted pages](https://help.klaviyo.com/hc/en-us/articles/360057676272), such as subscribe and manage preference pages, to reflect your migration away from Klaviyo for that channel. For instance, if you keep email but migrate SMS providers, you'll want to remove mention of collecting SMS consent.

If you are migrating away from Klaviyo completely, remove any links on your site to [custom hosted pages](https://help.klaviyo.com/hc/en-us/articles/360057676272) you've set up in Klaviyo.

## Remove code snippets

This is only if you are migrating away from Klaviyo for both email and SMS. If you still plan to use Klaviyo for one of these channels, [skip to the next section](#h_01GJJM8NTJ73KKQR3SVN94DG7S).

You can remove Klaviyo’s web tracking snippets from your site since you’ll no longer need them. This is recommended because leaving them in place could unnecessarily slow site performance. These two snippets are Klaviyo’s **Active on Site** tracking and **Viewed Product** tracking. When you originally integrated your ecommerce platform with Klaviyo, you either added the snippets to your site manually, or they were added automatically, depending on your platform.

If the snippets were automatically added with your ecommerce integration, they should be automatically deleted when you remove it.

If you added them manually, you can learn more about where these snippets live on your site in our [Guide to Klaviyo onsite tracking](https://help.klaviyo.com/hc/en-us/articles/115005076767), and thus where to go to delete them from your site. You should also remove any other Klaviyo javascript that you manually added to your site.

## Export your analytics

To save any analytics from your Klaviyo account, such as custom reports or flow analytics, you can export them via the ****Analytics**** and ****Flows**** tabs respectively. For more information, see the following articles:

- [Understand custom reports in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/360047725651)
- [How to export flow analytics](https://help.klaviyo.com/hc/en-us/articles/115002779371)

## Disable your integrations

This is only if you are migrating away from Klaviyo for both email and SMS. If you still plan to use Klaviyo for one of these channels, [skip to the next section](#h_01GJJM8NTJ73KKQR3SVN94DG7S).

Klaviyo recommends that you remove your ecommerce platform integration before canceling your account. This will make sure that new data isn’t synced to Klaviyo and that any automatically added javascript is removed from your site.

1. Click your account name in the bottom left corner.
2. Click ****Integrations****.
3. Under ****Enabled Integrations****, find your ecommerce platform.
4. Click ****View Settings**** > ****Remove****.
5. Repeat for any other integrations you have.

## Cancel your plan or account

If you want to cancel one or both of your plans, follow the process outlined in [How to cancel your account.](https://help.klaviyo.com/hc/en-us/articles/1260805595309#cancelling-your-account2)