<h1>How to use flows to send transactional emails</h1>

## You will learn

Learn how to set up important transactional emails inside Klaviyo that are triggered when your subscribers purchase or interact with your brand. Customers expect these emails and will search for them in their inbox. For this reason, transactional emails are sent to almost all customers and should not contain any marketing content.

****Do suppressed profiles receive transactional emails?****

Yes, suppressed profiles still receive transactional emails.

The only exceptions are if the suppression reason was one of the following:

- Email had 7 consecutive soft [bounces](https://help.klaviyo.com/hc/en-us/articles/115005250408).
- Email had a hard bounce (includes profiles marked as suspicious).
- The customer previously marked a message as spam.

## Before you begin

Please note that transactional emails:

- Are only available for paid accounts.
- Are only available for metric-triggered flows (such as **Placed Order**).
  - Cannot be used in price drop flows.
- Must be approved by Klaviyo, which can take up to 24 hours (1 business day).
  - Note: editing a transactional message removes the transactional status, and the message will need to be re-submitted for approval.
- Cannot be imported from your ecommerce platform into Klaviyo.
- Are marked on a per-email basis, not per-flow.
  - You can have 1 email within a flow that is transactional, and have every other email in that flow be considered marketing content.
  - You cannot automatically mark an entire flow as transactional, though it is possible to create a flow in which all the emails are transactional.
- Do not appear any differently than marketing emails to your recipients (i.e., your customers won't know that an email is marked as transactional).
- Cannot be requested for a message that has had an A/B test set up for it.

Requests for transactional messages in list- or segment-triggered flows must be made through support, must strictly follow our guidelines for transactional content, and may take longer to be approved.

****What if I want to use a metric not synced to Klaviyo?****

If you want to use a metric to trigger a flow that isn't synced through your ecommerce or other integration, you will need to create a new custom metric.

You can use Klaviyo's APIs to set this up, namely the [Metrics API](https://developers.klaviyo.com/en/reference/metrics_api_overview) and [Events API](https://developers.klaviyo.com/en/reference/events_api_overview) for custom metrics & events. For example, a password reset email would need a corresponding **Password Reset** event, which would need to be configured as a custom metric.

Turn off any corresponding transactional emails in your ecommerce platform before sending with Klaviyo. Otherwise, you may be double-emailing people.

## Create a transactional email

When building out these emails, if the flow is triggered by an event that's synced through your ecommerce integration, like **Placed Order**, then you can use a post-purchase flow as a starting point in terms of the information that you will pull into the template (e.g., a link, image, and name of the item).

To instead build a flow from scratch:

1. Navigate to the ****Flows**** tab in Klaviyo.
2. Either:

   - Select an existing flow.
   - Click ****Create Flow**** in the upper right, then click ****Build your own****.
3. Design or edit your flow in the builder, then personalize your flow emails.

   - You can leverage our [guide to personalizing flows with dynamic data](https://help.klaviyo.com/hc/en-us/articles/115002779071) to learn how to pull event data into your email templates.
4. Click on the message you want to be marked transactional.Note: if you want multiple messages in a flow to be transactional, you must select them one at a time.
5. Check that the message is in **Manual** mode.
6. In the right sidebar, click ****Apply for transactional status****.
7. Wait up to 24 hours (i.e., 1 business day) to see if your message was approved. While waiting for approval:

   - You will not be able to edit the message content.
   - You cannot set up an A/B test. Messages that had an A/B test previously will not show the option to apply for transactional status.![Email while waiting to be reviewed for transactional status](https://klaviyo.zendesk.com/hc/article_attachments/28717850891547)
8. Within 24 hours, you will see whether your message has been accepted or rejected.

![Transactional email once it's been accepted](https://klaviyo.zendesk.com/hc/article_attachments/28717850893211)

If your message is accepted, note that any subsequent edits to the message content will remove the transactional status. If you want to edit the content, you must uncheck the transactional status, edit the content, and then resubmit the message for approval.

### What to do if the message was rejected

If your message was rejected you can:

- Keep the message as-is (and not have it be marked transactional).
- Edit the content and re-submit it for approval.
- Submit an appeal.

  For the appeal, you must submit a ticket to Klaviyo Support and include:
- “Transactional appeal” as the subject line/reason for the ticket
- Flow message ID
- Example (or 2) of the message you want to send
- Screenshot of your call to action (CTA)
- Estimate of how many times per month someone could receive this message
- Links to your privacy policy and terms of service
