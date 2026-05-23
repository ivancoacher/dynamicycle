---
id: 40116474536347
title: "About WhatsApp deliverability"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/40116474536347-About-WhatsApp-deliverability"
section: "Understand WhatsApp with Klaviyo"
category: "WhatsApp"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-20T16:50:30Z"
language: en
---

Learn about WhatsApp deliverability, including the factors that play a role in message delivery and reasons why your messages may not be delivered.

Before sending messages, you'll need to [connect your WhatsApp Business Account to Klaviyo](https://help.klaviyo.com/hc/en-us/articles/40111819732635).

## WhatsApp message delivery

****Delivery vs. deliverability****

Delivery and deliverability are 2 distinct concepts you may be familiar with. Deliverability refers to how likely your message is to land in the recipient's inbox, and is affected by things like recipient engagement. This concept is most relevant to email marketing, where inbox providers make decisions on how to sort your emails.

Meanwhile, delivery is more straightforward and refers to whether or not a message was successfully delivered. With WhatsApp, delivery is more relevant than deliverability as there are no intermediaries between Meta and recipients that determine where a message should be delivered.

There are a number of factors that play a role in whether your WhatsApp messages are successfully delivered to recipients.

### Message limits

Each sender on WhatsApp has [message limits](https://developers.facebook.com/docs/whatsapp/messaging-limits/) that control how many conversations you can initiate within a 24-hour period. Once you reach your account limit, you will no longer be able to initiate additional conversations until at least 1 active conversation has ended.

The message limit tiers are as follows:

- ****Tier 0**** Up to 250 business initiated conversations in a 24-hour period.
- ****Tier 1**** Up to 2,000 business initiated conversations in a 24-hour period.
- ****Tier 2**** Up to 10,000 business-initiated conversations in a 24-hour period.
- ****Tier 3**** Up to 100,000 business-initiated conversations in a 24-hour period.
- ****Tier 4**** Up to unlimited business-initiated conversations in a 24-hour period.

### Increasing your message limits

Business phone numbers are initially limited to 250 initiated conversations in a 24-hour rolling period. Following best practices and improving your quality rating can lead to an increase in the message limits.

You can increase your messaging limit to 1,000 business-initiated conversations in a 30-day period on your own using the following methods:

- Go through the [business verification process](https://www.facebook.com/business/help/2058515294227817?id=180505742745347).
- Go through the [identity verification process](https://www.facebook.com/business/help/587323819101032).
- Open 1,000 or more business-initiated conversations in a 30-day moving period using templates with a high quality rating.

If you have met these verification or sending requirements but are still limited to 250 business-initiated conversations, you can open a support ticket with Meta to request a limit increase.

### User consent

In order for your WhatsApp message to be delivered to a recipient, you must have collected [explicit consent](https://help.klaviyo.com/hc/en-us/articles/4404203889947) from them.

You can collect consent for WhatsApp messaging from profiles through:

- Sign-up forms
- Meta QR codes and subscribe links
- Subscribe keyword
- API

While not required, including disclosure language wherever you collect consent is a marketing best practice. You may want to update any disclosures like your terms of service and privacy policy to include information regarding what your brand will do with WhatsApp consent. Klaviyo cannot provide legal recommendations regarding these policies, and you should consult with your legal team.

****Examples of disclosure language****

These are just examples of disclosure language for collecting WhatsApp consent. You should work with your legal team to create a set of disclosure language for your brand.

****When marketing consent is being collected****

**By submitting this form, you consent to receive informational (e.g., order updates) and/or marketing messages (e.g., cart reminders) from [company name] including messages sent by autodialer. Consent is not a condition of purchase. Unsubscribe at any time by replying STOP.**

****When transactional consent is being collected****

**By submitting this form, you consent to receive informational (e.g., order updates) from [company name] including messages sent by the autodialer. Consent is not a condition of purchase. Unsubscribe at any time by replying STOP.**

### Template approval and best practices

WhatsApp only allows you to start conversations with customers using templates that have been approved by Meta in advance. Typically the approval process takes a few minutes, but can take up to 24 hours.

Once a template has been approved, you can begin sending it to customers. If a template is rejected, you’ll need to make edits and resubmit it for approval.

In general, you should aim to avoid vague or irrelevant messages, and personalize messages for specific recipients using placeholders. Make sure your messages are timely, and respect quiet hours. You should also avoid sending multiple messages to a single profile in a day.

Follow these [WhatsApp guidelines](https://developers.facebook.com/docs/whatsapp/message-templates/guidelines/) to increase your template’s chances of being approved:

- Use templates to initiate conversations and encourage end users to respond with quick replies.
- Avoid open-ended welcome or introductory messages.
- Clearly specify the purpose of each message, preferably within 5 lines.
- Keep messages concise and informative.
- Avoid abusive or threatening language.
- Select the appropriate message type and language.
- Replace the word "survey" with "feedback."
- Upload samples for media files, placeholders, and call-to-action buttons when registering templates.
- Include opt-out instructions.
- Avoid duplicate templates. If a template is submitted with the same wording in the body and footer of an existing template, the duplicate template will be rejected.
- Make sure the message template does not contain content that violates WhatsApp’s Business Policy.
- Do not request sensitive identifiers from users.
  - Do not ask people to share full-length payment card numbers, financial account numbers, and other sensitive identifiers. This also includes documents that might contain sensitive identifiers.
  - Requesting partial identifiers (e.g., the last 4 digits of their social security number) may be permitted.

****Other formatting guidelines for templates****

Be careful when using variable parameters:

- Do not start or end with a variable parameter.
- Avoid too many variable parameters relative to the message length.
- Avoid adjacent variable parameters (e.g., {{ person.first\_name }} {{ person.last\_name}}).
- Avoid variable parameters that are missing or have mismatched curly braces.
- Do not include special characters (such as a #, $, or %) in a variable parameter.
- Do not start newline characters (e.g., /n) with variable parameters.
- Avoid emojis or newline characters in the footer.
- Refrain from using emojis, asterisks, formatting markup, or **\n** in the header.
- Avoid grammatical or spelling errors.
- Only share URLs that include your brand name and avoid URLs with random characters.

## WhatsApp quality ratings

WhatsApp rates the quality of both your overall account, and the templates that you send. You can view the quality rating of both so you can monitor and make changes to templates that are negatively impacting your account level quality rating.

### Account quality rating

Your WhatsApp account is assigned a quality rating once you start sending messages, and this rating can impact your messaging limits. Improving your account quality rating can increase your message limits, while a drop in your quality rating can decrease your message limits.

The account quality rating is based on recipient engagement with your message over the past 7 days, with more recent messages impacting your rating more heavily. Meta uses factors like blocks, reports and the reasons users provide when they block a business when determining your rating. It is important to maintain a strong quality rating while scaling your message limits.

The [quality ratings for your account](https://www.facebook.com/business/help/896873687365001) in Meta:

- ****High****
- ****Medium****
- ****Low****
  - If the quality rating improves to **Medium** or **High** within 7 days, the status returns to **Connected** without any decrease in sender limits. This indicates your account is healthy and your message limits can be increased.
  - If the quality does not improve within 7 days, the sender status reverts to **Connected** but with the messaging limit reduced to the next lower tier. The minimum tier for verified businesses is Tier 1.

### Template quality ratings

Individual templates also have quality ratings assigned by Meta.

The [quality ratings for your templates](https://developers.facebook.com/docs/whatsapp/message-templates/guidelines/) are:

- High Quality
- Medium Quality
- Low Quality

  Templates will have a rating of **Quality pending** after first being approved.

  You also see the following statuses related to your template approval status:
- Pending
- Rejected
- Paused
- Disabled
- Appeal requested

You should reach out to Meta support if you have questions regarding a template’s approval.

## Troubleshooting WhatsApp delivery errors

As of April 1, 2025, Meta will block WhatsApp marketing messages sent to US phone numbers. Delivered to US recipients will fail with the error code 131049.

You may experience delivery errors when attempting to send to recipients via WhatsApp. Errors can be grouped into 4 different types:

- Authorization
- Integrity
- Throttling
- Other

Learn more about [resolution steps for specific errors and see associated error codes](https://developers.facebook.com/docs/whatsapp/cloud-api/support/error-codes/).

Beyond these, Meta may limit the number of marketing template messages a person receives from any business in a given period of time where users are less likely to be receptive and engage with them.

### Authorization errors

Authorization errors refer to issues with authentication or permissions in WhatsApp. Examples of authorization errors include expired access tokens and changes in permissions.

### Integrity errors

Integrity errors refer to violations of the WhatsApp platform policies. Examples of integrity errors include attempting to send to users in restricted countries or account blocks due to violations of the [WhatsApp Terms of Service](https://www.whatsapp.com/legal/terms-of-service).

### Throttling errors

Throttling errors refer to issues with the quantity or frequency of sends from your account. Some examples of throttling errors include sending too many messages to the same recipient’s phone number in a short period of time, or reaching spam rate limits because too many previous messages were blocked by users.

### Other errors

If an error does not fall into the **Authorization**, **Integrity,** or **Throttling** groups, they are classified as **Other**. This error group includes a variety of different issues, but some examples include the sender and recipient phone number being the same, WhatsApp services being temporarily down, or messages failing due to an unknown reason.

### Undisclosed errors

There are also some cases where a message appears as sent, but is not actually delivered. In these cases, Meta will not disclose the cause of the delivery error due to privacy and policy reasons.

Some reasons for these undisclosed errors include:

- The recipient did not come online during the 30 day window where Meta holds messages for offline customers.
- The customer has blocked the business phone number, or another business phone number owned by your business.
- The customer is in a restricted or sanctioned country.
- The message was not delivered as part of an experiment run by Meta.