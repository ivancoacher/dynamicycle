---
id: 360039239172
title: "Understanding SMS failure reasons and resolution steps"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360039239172-Understanding-SMS-failure-reasons-and-resolution-steps"
section: "SMS deliverability best practices"
category: "SMS"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-21T13:54:47Z"
language: en
---

## You will learn

Learn reasons why SMS message delivery can fail and best practices for avoiding failures.

## Receiving an SMS error message

When sending SMS with Klaviyo, it is important to pay attention to your failed deliveries. Ideally, the failed delivery rate should be as low as possible. If you’re seeing a lot of failed deliveries, review the failure reasons and take action to prevent further delivery issues.

To view this information for a text message:

1. Navigate to the SMS flow or campaign you want to look at.
   - For flows, click on the SMS message and then click ****View all Analytics**** on the left-hand side.
   - For campaigns, go directly to step 2.
2. Select ****Recipient activity.****
3. Select the ****Other**** dropdown menu.
4. Choose ****Failed delivery.****
5. Review the reason for the message’s failure in the **Failed Reason** column.

![Failure reasons for SMS message in flow](https://klaviyo.zendesk.com/hc/article_attachments/28711677393051)

### Device disconnected

The **Device disconnected** failure indicates that the recipient’s device is no longer in service.

If these errors exceed 5% of the total send, take the following resolution steps:

- Implement an [SMS error segment](https://help.klaviyo.com/hc/en-us/articles/9821790118171) to ensure unreliable data is excluded from SMS sends.

### Device unreachable

The **Device unreachable** failure indicates that the recipient’s device is not in a service area, not accepting messages, or the device is off and cannot receive SMS.

If these errors exceed 5% of the total send, take the following resolution steps:

- Implement an [SMS error segment](https://help.klaviyo.com/hc/en-us/articles/9821790118171) to ensure unreliable data is excluded from SMS sends.

### Carrier violation

The **Carrier violation** failure reason indicates that your send is failing due to mobile carrier filtering.

Mobile carriers filter SMS messages for 2 main reasons:

- Protect their customers from receiving spam messages.
- Meet regulations for sending SMS to phones in a specific country or on a certain mobile network.

SMS message filtering can vary by country and across different mobile networks (e.g., Verizon, AT&T, etc.)

Carriers will filter messages that contain terms related to [sex, hate, alcohol, firearms, and tobacco (SHAFT)](https://help.klaviyo.com/hc/en-us/articles/4401822831771). SHAFT words are prohibited by the [CTIA](https://help.klaviyo.com/hc/en-us/articles/360035055312), the regulatory body which enforces guidelines for SMS messages. Further, terms that are considered or relate to profanity, controlled substances, or CBD are similarly filtered.

If you are seeing **Carrier violation** failures exceed 10% of your total send, take the following actions:

- Remove any prohibited content prior that is classified as [SHAFT or prohibited on SMS](https://help.klaviyo.com/hc/en-us/articles/4401822831771).
- Ensure that the SMS message content does not resemble spam (e.g.,contain many capital letters or includes any bitly, tinyurl, or other third-party shortened links).
- Review your recent SMS campaign unsubscribe rates in relation to our [campaign SMS and MMS benchmarks](https://help.klaviyo.com/hc/en-us/articles/360051110111). If your unsubscribe rates are increasing or high, learn how to [decrease your SMS unsubscribe rates](https://help.klaviyo.com/hc/en-us/articles/4404612542619).
- Enable [double opt-in](https://help.klaviyo.com/hc/en-us/articles/115005251108) to ensure users are aware of what they are subscribing to.
- Review [SMS disclosure language](https://help.klaviyo.com/hc/en-us/articles/4412878737051) to ensure consent is transparent to the end user.

Once you have completed the recommended resolution actions, test an SMS message through a preview.

Make sure to test this with a preview SMS, rather than a campaign.

If your delivery problems persist, you can reach out to Klaviyo’s [support team](https://help.klaviyo.com/hc/en-us/articles/115001002272).

### Message blocked

The **Message blocked** failure reason indicates that a wireless carrier, Klaviyo's system, or the recipient has blocked the message. Klaviyo will automatically suppress failures where the error is returned as **Message blocked**,so that these errors do not reoccur on the same number.

If a single number is repeatedly receiving **Message blocked** errors, it signifies a continual manual upload of numbers. The origin of those errors relates to the mobile provider observing a STOP from the recipient handset to sender, but there is an attempt to continue sending to the user in their opted out state.

If you are seeing **Message blocked** errors exceed 5% of your total send, take the following resolution steps:

- Implement an [SMS error segment](https://help.klaviyo.com/hc/en-us/articles/9821790118171) to ensure unreliable data is excluded from your sends.
- Enable [double opt-in](https://help.klaviyo.com/hc/en-us/articles/115005251108) to require customers to confirm subscriptions in order to prevent invalid numbers from entering subscriber lists.
- Refrain from uploading unknown SMS data.

### Device incapable of receiving SMS

The **Device incapable of receiving SMS** failure reason relates to landlines or other devices that cannot receive the SMS as they’re not designed to do so. Klaviyo will automatically suppress failures where the error is returned as **Device incapable of receiving SMS**.

If you are seeing **Device incapable of receiving SMS** failures exceed 5% of your total send, take the following resolution steps:

- Implement an [SMS error segment](https://help.klaviyo.com/hc/en-us/articles/9821790118171) to ensure unreliable data is excluded from your sends.
- Enable [double opt-in](https://help.klaviyo.com/hc/en-us/articles/115005251108) to require customers to confirm subscriptions in order to prevent landlines or ineligible numbers from joining subscriber lists.

### Toll-free number not registered or number not verified

The **Number not verified error** indicates that subscribers are not receiving messages to their device because your Sender ID has not been approved.

- Ensure that the sender ID is [**Verified**](https://help.klaviyo.com/hc/en-us/articles/4415873897499) or [**Approved**](https://help.klaviyo.com/hc/en-us/articles/14953787622427) from the SMS settings section of your Klaviyo account. Refrain from sending SMS via flows until applicable sender IDs are verified.

Once you have completed the recommended resolution actions, test an SMS message through a preview.

Make sure to test this with a preview SMS, rather than a campaign.

If delivery problems persist, reach out to Klaviyo’s [support team](https://help.klaviyo.com/hc/en-us/articles/115001002272).

### Invalid content type

The **Invalid content type**error includes when you send some content (e.g., image file type) that carriers don't support.

For instance, WebPfiles are not supported by mobile carriers. That file type is designed to work on internet browsers and while the user is online. It is not ideal for any use case outside of that, including being sent via mobile networks.

### Unknown errors

The **Unknown** failure reason indicates that the wireless carrier did not report why a message could not be delivered.

If you are seeing **Unknown** failures exceed 10% of your total send, you can reach out to Klaviyo’s [support team](https://help.klaviyo.com/hc/en-us/articles/115001002272).

## Best practices for not being filtered

To try and prevent from being filtered by mobile carriers or having sending failures, it’s important to follow best practices for SMS messaging. Make sure you are personalizing your messages and providing value to your subscribers.

See our [recommended SMS segments](https://help.klaviyo.com/hc/en-us/articles/360047879512) to better understand your audience and send more targeted messages with Klaviyo.

Following these best practices can also lead to better SMS delivery:

- Always provide a way for subscribers to easily opt out. Carriers heavily filter messages that don't include STOP language.
- Enable [double opt-in](https://help.klaviyo.com/hc/en-us/articles/115005251108) for SMS lists.
- Let subscribers know who is sending the message.
- Do not send SMS messages [early in the morning or late at night](https://help.klaviyo.com/hc/en-us/articles/4408737146651), as a text message from a business during off-hours may be seen as intrusive.
- Take advantage of [Smart Sending](https://help.klaviyo.com/hc/en-us/articles/115002779311) to avoid overloading SMS subscribers with messages.
- Use a personal tone to sound more human.
- Avoid SHAFT-related words.
- Use a trusted sending number, such as a short code or verified toll-free number.

## Additional resources

[Understanding SMS metrics](https://help.klaviyo.com/hc/en-us/articles/360035345572)

[Guide to writing SMS copy](https://academy.klaviyo.com/writing-sms-and-mms-copy)

[SMS and MMS prohibited content in the US](https://help.klaviyo.com/hc/en-us/articles/4401822831771)