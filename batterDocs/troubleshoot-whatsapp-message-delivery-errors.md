<h1>Troubleshoot WhatsApp message delivery errors</h1>

WhatsApp must be enabled in your Klaviyo account to access delivery data.

Identify and fix WhatsApp delivery errors to improve message performance and protect your sender reputation.

## Before you begin

Follow these steps to check your WhatsApp delivery results:

1. Open your WhatsApp message in the ****Campaigns**** or ****Flows****.
2. Review the **Deliverability** section.
3. Click into failed messages to view vendor error codes.

If your delivery rate is below 90%, or you see repeated error codes, review the table below and set up the WhatsApp error segment.

## Common WhatsApp error codes

Use the following table to identify common WhatsApp error codes and how to resolve them.

| Error code | Description | Recommended action |
| --- | --- | --- |
| 131026 – Message undeliverable | WhatsApp couldn’t deliver the message. Common causes include invalid WhatsApp numbers, missing country codes, or outdated Terms of Service. | • Verify phone number format and country code.  • Ask users to update WhatsApp and accept the latest Terms.  • Remove invalid or inactive numbers. |
| 131053 – Media upload error | The media file in your message couldn’t be uploaded. | • Check file format and compression.  • Supported formats: Images (8-bit RGB/RGBA), Videos (H.264 + AAC), Documents (PDF for template headers). |
| 130472 – Number in experiment | WhatsApp is running experiments that may limit marketing messages to certain users. | • Contact users through another channel and ask them to message your business on WhatsApp.  • Resume marketing messages within 24 hours once they respond. |
| 131049 – Maintain healthy ecosystem engagement | WhatsApp blocked delivery due to low engagement or frequent marketing messages. | • Avoid immediate retries.  • Reduce frequency and send to engaged users.  • Personalize messages to encourage replies. |
| 131050 – Recipient opted out | The user unsubscribed from WhatsApp messages. | • Do not resend messages.  • Suppress this contact from future campaigns.  • Re-opt in via another channel if appropriate. |
| 131000 – Unknown error | Temporary or general delivery failure. | • Retry later.  • Contact Klaviyo Support if it persists. |

## Why use the WhatsApp error segment

Repeated delivery failures reduce performance, waste credits, and damage your sender reputation. The WhatsApp error segment automatically excludes contacts that repeatedly fail message delivery.

This segment must be added manually. It is not automatically applied to campaigns.

## When to use it

- Delivery rates are below 90%.
- Errors like 131049, 131026, or 130472 appear frequently.

## How to create the WhatsApp error segment

Create a new segment in Klaviyo.

1. Create a new segment in Klaviyo.
2. Set conditions:

   - **Person can receive WhatsApp marketing**
   - **Has failed to deliver WhatsApp** with the following filters:
     - At least once in the last 16 days → **Error code 131049**
     - At least once over all time → **Error code 131026**
     - More than 2 times over all time → **Error codes 130472 or 131049**
3. Add this segment as an excluded list in your WhatsApp campaign setup.

![Creating segment conditions in Klaviyo](https://klaviyo.zendesk.com/hc/article_attachments/42141066953883)

## Best practices

- Always exclude the WhatsApp error segment before you send a campaign.
- Regularly review delivery performance and error trends.
- Remove invalid or inactive contacts from your lists.
- Focus on engaged users to maintain a strong sender reputation.
