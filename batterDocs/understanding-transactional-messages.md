<h1>Understanding transactional messages</h1>

Learn what it means for a message to be considered transactional, including what to include (and not include) in the message.

## What is a transactional message?

A transactional message is an automated message that’s sent when an individual takes an action and contains information directly related to the action.

Transactional messages serve as operational touchpoints. Users expect to receive them, for example, after placing an order or when resetting their password.

### Transactional vs. promotional

Promotional (also known as marketing) messages are sale-driven and are initiated by the business, while transactional messages are user-driven.

Promotional messages are about promoting your business and growth. Some examples are product launch alerts, newsletters, surveys, etc. They aim to increase conversions, improve customer retention, get feedback, and meet other business goals.

Transactional messages are about giving the user information they need when prompted. For instance, if someone places an order, you can send transactional messages that confirm their order, share shipping updates, and confirm the delivery.

Below is a table listing examples of transactional and promotional messages.

|  |  |
| --- | --- |
| ****Transactional**** | ****Promotional**** |
| Account activation or deactivation | Any campaign message (newsletter, sales, product launch) |
| New device login alert | Abandoned cart or browse abandonment |
| Password reset | Product recommendation (cross-sell or up-sell) |
| Order confirmation or cancellation | Surveys or quizzes |
| Shipping or delivery alerts | Requests for ecommerce reviews |
| Booking or ticket confirmation | Replenishment message or order-renewal reminders |
| SMS responses to required keywords (e.g., HELP) | Referral requests |
|  | Birthday or anniversary notifications |

****What about a welcome series/subscribe confirmation message****

The short answer is that it depends.

First, there’s a difference between what’s considered transactional generally and what’s eligible for transactional approval in Klaviyo. In Klaviyo, welcome series messages cannot be marked as transactional.

Outside of Klaviyo, a subscribe confirmation message (i.e., the first message in a welcome series) might be considered transactional, but only in certain cases. If it contains any promotional content (such as a coupon or best-selling products), it’s not considered transactional. To be considered transactional, it can only confirm someone’s subscription.

Any follow-up messages in a welcome series are always considered promotional, never transactional.

## What to include in a transactional message

Besides general things like your company info or opt-out instructions, your transactional message should only include details about the action the user took.

Let’s use a shipping alert as an example. In this case, your transactional message may include details such as:

- Which products are in that shipment
- Shipping address
- Cost
- The tracking number and link
- Estimated delivery date.

Depending on which channel you’re using, you may include some or all of this information.

### What not to include

A transactional message cannot include anything unrelated to the action or any promotional content, including:

- Coupons
- Products that someone hasn’t bought
- Newsletter information
- Links to sign-up forms or subscribe pages
- Marketing call to actions (CTAs)

## Transactional consent for email, SMS, and mobile push

Getting consent before sending messages is always a best practice.

This goes for transactional too, with the only exception being email. A customer doesn’t need to explicitly opt in to receive transactional emails.

SMS and mobile push always require consent before you can send any transactional messages. However, you don't need to use double opt-in.

For mobile push, this is because promotional and transactional messages are treated exactly the same, with no differences between them.

As for SMS, it is because you need to clearly inform subscribers about the types of messages they’ll receive. If you plan to send transactional SMS, it’s important to include “transactional” in your [disclosure language](https://help.klaviyo.com/hc/en-us/articles/11644128409371) or, if possible, collect transactional and promotional SMS consent separately.

****Do suppressed profiles receive transactional emails?****

Yes, suppressed profiles still receive transactional emails.

The only exceptions are if the suppression reason was one of the following:

- Email had 7 consecutive soft [bounces](https://help.klaviyo.com/hc/en-us/articles/115005250408).
- Email had a hard bounce (includes profiles marked as suspicious).
- The customer previously marked an email as spam.
- Email is pending transactional status or in the process of being edited. In either instance, suppressed profiles will be skipped. To avoid automatic skipping, you can [set the flow to manual](https://help.klaviyo.com/hc/en-us/articles/115002779331).

## What can be marked as transactional in Klaviyo

In approved cases and with a paid account, you can mark SMS or email messages in flows as transactional. However, there are some limits:

- Email: only emails in metric-triggered flows can be marked transactional (does not include price drop flows).
- Text: only messages in metric-triggered flows can be marked transactional.
  - These messages will send to anyone who consented to SMS promotional, transactional, or Shopify order updates.

Requests for transactional messages in list- or segment-triggered flows must be made through support, must strictly follow our guidelines for transactional content, and may take longer to be approved.

Transactional status is not relevant for mobile push messages, and they cannot be marked as transactional in Klaviyo.

## What happens if your transactional request is rejected?

If your request to mark a message as transactional was rejected, this is because it didn't meet the criteria listed in this article. However, if you would like to make another request please do the following:

1. Review the message in question and correct or remove any content that doesn't meet the criteria above.
2. Submit an appeal by [reaching out to Klaviyo Support](https://klaviyo.zendesk.com/hc/en-us/articles/115001002272).
