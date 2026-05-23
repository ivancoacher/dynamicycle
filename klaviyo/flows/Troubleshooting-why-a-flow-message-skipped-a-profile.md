---
id: 1260805003210
title: "Troubleshooting why a flow message skipped a profile"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/1260805003210-Troubleshooting-why-a-flow-message-skipped-a-profile"
section: "Troubleshooting flows"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-04-21T13:54:26Z"
language: en
---

## You will learn

Learn where to find the skipped reasons for why a flow message skipped a profile, as well as what each reason means. Knowing the skipped reason(s) for a message is key to measuring the performance of a flow. It can help you determine if your flow is set up correctly, if the message is in the right format, and if the right people are receiving your content.

Keep in mind that while a high number of skips can indicate a problem with your setup, that is not always the case. For instance, abandoned cart flows should always have a lot of skips, as everyone who begins to check out enters the flow, but those who then place an order are skipped due to the **Placed Order 0 times since starting this flow** filter.

Campaign skip reasons are slightly different from those used for flows. If you are troubleshooting why a campaign skipped profiles, see our article on [troubleshooting skipped profiles in email campaigns](https://klaviyo.zendesk.com/hc/en-us/articles/115005258268).

## Finding a flow message's skipped reason(s)

To view the skipped recipients for a flow:

1. Edit the flow you'd like to view.
2. Click on a message in the flow that has been skipped.
3. In the sidebar, click ****View details**** in the **Performance**section of the sidebar.
   ![Analytics section found in the left sidebar when you click on a message.](https://klaviyo.zendesk.com/hc/article_attachments/28720893739419)
4. Click on the **Recipient activity** tab.
5. Click the ****Skipped**** tab.
   ![Skipped reason dropdown found in the Recipient Activity tab.](https://klaviyo.zendesk.com/hc/article_attachments/28720893741851)
6. Click on the dropdown to filter for different skip reasons.
   ![Dropdown showing a list of different skip reasons](https://klaviyo.zendesk.com/hc/article_attachments/28720893736091)

## What each skipped reason means

The ****Skipped**** dropdown will show you exactly who has been skipped by the flow and why. There are a variety of possible skipped reasons that apply to both email and SMS messages:

- ****Smart Sending****
  Skipped because [Smart Sending](https://help.klaviyo.com/hc/en-us/articles/115002779311) is enabled and they received a message from the same channel (e.g., email or SMS) too recently
- ****Person No Longer in List****
  Skipped because they are no longer in the trigger list or segment
- ****Fails Flow Filters****
  Skipped because they don't meet the criteria in the flow filters at send time
- ****Fails Additional Filters****
  Skipped because they don't meet the criteria specific to this flow email or SMS at send time
- ****Person Deleted****Skipped because the profile no longer existed at send time
- ****Action Deleted****Skipped because the email, SMS, or update profile property action no longer existed at send time

### Email-only skipped reasons

Email-specific skipped reasons include:

- ****Missing Email****
  Skipped because there is no email address associated with their profile
- ****Person Suppressed****
  Skipped because they unsubscribed or hard bounced from all emails
- ****Email Syntax Error****
  Skipped because the email template contains a syntax error
- ****Catalog Item Unavailable****
  Skipped because a product in the rendered email content is currently out of stock or not available
- ****Over Email Limit****Skipped because you went over your account's sending limit
- ****Unable to Send Email****Skipped because we ran into an unexpected error at send time
- ****Invalid From Email****Skipped because the sender email address (i.e., your from address) is not a valid address
- ****Error Retrieving External Data****Skipped because there was an issue retrieving data from an external source (for example, a coupon code from Magento 2 or Shopify)
- ****Coupon Category Unavailable****Skipped because the email contains a placeholder to pull in a dynamic coupon restricted to a certain category, and the category was deleted
- ****Unable to Create Coupon****
  Skipped because we were unable to create the coupon due to an error in the coupon itself (e.g., referencing a URL that is no longer valid) or you are sending too many coupons out in a short amount of time. We suggest reviewing all elements of your coupon or adding coupon codes in advance to a campaign.
- ****No More Uploaded Coupons Remain****Skipped because the email contains a placeholder to pull in an uploaded coupon and no more uploaded coupons remain
- ****Coupon Code Doesn't Exist****Skipped because the coupon code you’re referencing in an email either doesn’t exist or doesn’t match the coupon code you created in your Coupons tab; coupon code names are case-sensitive
- ****Email Cancelled****Skipped because the email had been cancelled at or before send time
- ****Suspicious Email****Skipped because this email has hard bounced across the Klaviyo infrastructure
- ****Email Dropped****
  When an email was not sent because the email address is suspicious

### SMS-only skipped reasons

SMS-specific skipped reasons include:

- ****Unable to Send SMS****Skipped because we ran into an unexpected error at send time
- ****Missing SMS Consent****Skipped because there is no SMS consent timestamp
- ****Missing Phone Number****Skipped because the recipient does not have a phone number associated with their profile
- ****Phone Number is Not Valid****Skipped because the recipient does not have a valid phone number
- ****Phone Number is in Country Not Supported by SMS****Skipped because the recipient's phone number is not in a location [where Klaviyo SMS is available](https://help.klaviyo.com/hc/en-us/articles/4402914866843)
- ****No Sending Number****Skipped because there is no sending number associated with your account; you can add a sending number to your account in ****Settings > SMS****
- ****Not Enough Sends Available****Skipped because you went over your account's sending limit for SMS messages; you can upgrade your plan in ****Settings > Billing > Create your plan****

## Additional resources

- Learn more about [troubleshooting a flow](https://help.klaviyo.com/hc/en-us/articles/115002779471)
- Learn more about [flow triggers and filters](https://help.klaviyo.com/hc/en-us/articles/115002779051)