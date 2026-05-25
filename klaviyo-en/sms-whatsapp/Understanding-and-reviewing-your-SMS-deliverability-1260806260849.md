---
id: "1260806260849"
title: "Understanding and reviewing your SMS deliverability"
source_url: "https://help.klaviyo.com/hc/en-us/articles/1260806260849-Understanding-and-reviewing-your-SMS-deliverability"
section: "SMS deliverability best practices"
category: "SMS"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-05-11T10:58:01Z"
language: "en"
---
## You will learn

Learn the important aspects of SMS deliverability, including how to evaluate it and best practices.

For SMS, deliverability is defined as whether or not a text message successfully made it to a recipient’s mobile device. Regularly reviewing SMS performance is key to maximizing your ROI, maintaining high customer engagement rates, and avoiding carrier filtering.

## The importance of SMS consent

Before we jump into deliverability, it’s important to understand SMS consent. Most countries require you to get explicit consent from subscribers. This means that:

- You must make it clear that providing a phone number means agreeing to receive SMS marketing messages
- Other forms of consent (like opting into email) do not count as consent for SMS

In Klaviyo, someone must be opted in to receive a text message from your brand. If there’s no SMS consent on the customer profile, the phone number will be skipped automatically.

## How a text message is delivered

There are three contributors involved in whether or not your recipients receive a text message:

1. Your SMS marketing platform (e.g., Klaviyo)
2. The wireless carrier (e.g., AT&T, T-Mobile, Verizon, etc.)
3. The individual’s phone or mobile device

****SMS marketing platform****

The SMS marketing platform is where you create and send your messages. The platform may perform certain checks before a message goes out to recipients. Klaviyo, for instance, will prevent you from sending to anyone who hasn’t consented to SMS. Klaviyo will also check the content of the message to see if it contains any non-compliant terms, specifically those related to sex, hate, alcohol, firearms, or tobacco (SHAFT) as well as illegal activity or substances, like CBD or hemp.

****Wireless carriers****

If the message passes the SMS marketing platform’s checks, it moves on to the wireless carriers. The carriers will perform their own checks, again looking for SHAFT/illegal terms in the message, URL, or linked landing page as well as what type of sender you are (e.g., your sending number type, engagement rate, unsubscribe rate, etc.) Each carrier has its own criteria for these checks and will [filter SMS and MMS messages](https://help.klaviyo.com/hc/en-us/articles/360039239172) as they see fit. Carriers will sometimes provide a reason for a failed delivery, but this is not always the case. They sometimes don’t confirm delivery or failure at all to prevent people from learning more about their checks and how to get around them.

****Individual's mobile device****

The final component to deliverability is the recipient’s device. Once the wireless carrier approves, the message should arrive to the individual’s phone. However, it could still not be delivered if, say, the phone is off or in a location without service. Android devices can also filter messages into a spam folder, rather than showing them in the main SMS inbox.

### SMS delivery receipts

Most of the time, wireless carriers provide a delivery receipt (DLR), also called delivery report, within minutes of a text message succeeding or failing.

However, for a small percentage of messages, carriers can be extremely delayed in issuing DLRs or never provide them at all (even in cases when the recipient did, in fact, receive your message). This is more common with small regional carriers, when sending MMS, or during peak sending hours (e.g., during Black Friday/Cyber Monday).

You can know whether Klaviyo received a delivery report by looking at the **Received SMS**metric. The **Carrier Delivery Status**for that metric shows as either:

- **Delivered**, when carriers explicitly confirmed that an SMS was delivered.
- **Sent**, if carriers did not confirm the delivery or issue a failure.

## How to evaluate SMS deliverability in Klaviyo

For SMS, deliverability is defined as whether or not a text message successfully made it to a recipient’s mobile device.

Regularly reviewing SMS performance is key to maximizing your ROI, maintaining high customer engagement rates, and avoiding carrier filtering.

### Review your campaigns

Monitor your rates to make sure subscribers are engaging with your audience.

If your rates are not where you want, leverage [segments](https://help.klaviyo.com/hc/en-us/articles/360047879512) to target the right audience for messages. Also, examine the content and timing of your message, asking yourself the following questions:

- Have I made it clear to recipients who this message came from?
- Am I sending to the right audience?
- Am I sending too often/not often enough?
- Does the message contain a URL? Is it working correctly?
- Do recipients know what to expect from the URL?
- How easy is it for recipients to unsubscribe?

We also recommend using a short code, if available, as carriers less likely to filter messages from this [number type](https://help.klaviyo.com/hc/en-us/articles/6637671573403).

### Review your flows

With SMS flows, review performance on a per-message basis. As with your campaigns, examine the content of the message, including the link, opt-out text, call to action, etc.

Further, look at the surrounding [splits and time delays](https://help.klaviyo.com/hc/en-us/articles/360050334651) to make sure that the right group got your message when they were meant to. Also, consider whether or not to use Smart Sending by asking yourself how important it is for subscribers to see the message.

### Evaluate your failed deliveries

Pay attention to your failed deliveries. Ideally, the failed delivery rate should be as low as possible. If you’re seeing a lot of failed deliveries, review the failure reasons:

- **Device Disconnected** means that the device is no longer in service, which can mean:
  - The destination number is unknown or no longer exists.
  - The device you are trying to reach does not have sufficient signal.
  - There is an issue with the mobile carrier.
- **Device Unreachable** means that the device is not in a service area, not accepting messages, or the device is off. It’s similar to a [soft bounce for email](https://help.klaviyo.com/hc/en-us/articles/115005250408).
- **Carrier Violation** means that the phone carrier filtered the message out.
- **Message Blocked** means that a wireless carrier, Klaviyo's system, or the recipient has blocked the message.
- **Device Incapable of Receiving SMS** means that the number is a landline or cannot receive SMS. Klaviyo will automatically unsubscribe the phone number if this is the failure reason.
- **Unknown** means that the wireless carrier did not report why a message was not delivered.

For **Device Disconnected** or **Device Incapable of Receiving SMS**, you may want to turn on [double opt-in](https://help.klaviyo.com/hc/en-us/articles/115005251108) for your SMS list, if it isn’t on already, to prevent non-working numbers from joining your lists.

If you’re seeing **Carrier Violation** or **Message Blocked**, review your message, link, and landing page so that there are no references to SHAFT, CBD, etc. Check that you are following all [best practices for your SMS messages](https://help.klaviyo.com/hc/en-us/articles/360035661191).

The same is true if the failure reason is **Unknown**, since the carrier hasn’t provided more information.

## Best practices for SMS deliverability

There are several ways to improve or maintain your SMS deliverability:

- Send at least 2–6 SMS messages per month.
  - Implement [engagement segments](https://help.klaviyo.com/hc/en-us/articles/360044556071) so you text your full list regularly.
    - For unengaged subscribers, text them at least once a month.
  - Create other [targeted segments](https://help.klaviyo.com/hc/en-us/articles/360047879512) to personalize your messages. Generally, the more personalized a message is, the better it performs.
- If you want the most trusted number, use a short code.
  - Otherwise, make sure your number is verified or registered, depending on the country.
- Follow [compliance guidelines](https://help.klaviyo.com/hc/en-us/articles/7956171032091), as these rules are essentially the enforcement of best practices. This includes:
  - Identifying your brand in your SMS, so recipients know who the message is coming from.
  - Never using or linking to SHAFT-related terms or other prohibited content.
  - Never sending during [SMS quiet hours](https://help.klaviyo.com/hc/en-us/articles/4408737146651); usually this is before 9 a.m. or after 8 p.m., but the exact hours vary by country.

## Additional resources

- [How to increase SMS click rates](https://help.klaviyo.com/hc/en-us/articles/4404565738395)
- [Filtering by wireless carriers](https://help.klaviyo.com/hc/en-us/articles/360039239172)
- [SMS marketing strategies for all levels [+12 Pro tips]](https://www.klaviyo.com/blog/sms-marketing-strategies)