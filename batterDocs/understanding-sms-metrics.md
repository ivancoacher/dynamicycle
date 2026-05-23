<h1>Understanding SMS metrics</h1>

## You will learn

Learn about the SMS metrics that are pulled into Klaviyo, such as what they are, where to find them, and what they mean.

## Before you begin

Klaviyo does not track open rates for SMS, because most recipients will open an SMS message that they receive. When it comes to SMS messages, the click rate is the metric that should be focused on, as clicks are more relevant to conversions.

Note that in order for Klaviyo to track clicks and conversions, you must have sent a link and used the Klaviyo link shortener in an SMS.

## Tracked SMS metrics

In ****Analytics >**** ****Metrics****, you can see the SMS events in your account. Let’s dive into what each metric means.

- ****Relayed SMS****
  When an SMS from a flow, campaign, or outbound conversation message is relayed (or sent) by Klaviyo to the next downstream platform (e.g., a wireless carrier).
- ****Received SMS****
  When an SMS from a flow, campaign, or outbound conversation message is recorded as delivered to the recipient (i.e., Klaviyo did not receive a failure). Within this metric, the **Carrier Delivery Status** provides additional information:
  - **Carrier Delivery Status: Delivered** indicates the wireless carrier provided an explicit confirmation of delivery (i.e., a [delivery receipt](https://help.klaviyo.com/hc/en-us/articles/1260806260849#h_01JQ4PA6HJTGGF13RTJ9TV15ZT) or report).
  - **Carrier Delivery Status: Sent** indicates the wireless carrier did not provide an explicit confirmation of delivery or a failure. This can happen more frequently with smaller, regional carriers; when sending MMS; and when demand is especially high (e.g., during Black Friday/Cyber Monday).
- ****Failed to Deliver SMS****
  When an SMS from a flow, campaign, or outbound conversation message is sent but not delivered to the recipient; there are a few reasons why this may happen:
  - **Device Disconnected** means that the device is no longer in service.
  - **Device Unreachable** means that the device is not in a service area, not accepting messages, or the device is off.
  - **Carrier Violation** means that the phone carrier filtered the message out.
  - **Message Blocked** means that a wireless carrier, Klaviyo's system, or the recipient has blocked the message.
  - **Device Incapable of Receiving SMS** means that the number is a landline or cannot receive SMS.
  - **Unknown** means that the wireless carrier did not report why a message was not delivered.
- ****Received Automated Response SMS****
  When an automated SMS response to a keyword or non-recognized keyword (e.g., the [auto-responder](https://help.klaviyo.com/hc/en-us/articles/360059002271#h_01JP5WNR28YD7777EWPGJ908G8) configured in Inbox) is delivered to the recipient. You can also review the **Carrier Delivery Status** for this metric.
- ****Failed to Deliver Automated Response SMS****
  When an automated response from a keyword or non-recognized keyword is sent but not delivered to the recipient.
- ****Sent SMS****When someone sends an inbound SMS (i.e., texts your sending number).
- ****Clicked SMS****
  When a recipient clicks on a link within an SMS message. Clicking an unsubscribe or company information link does not count toward this metric.
- ****Subscribed to SMS Marketing****
  When a recipient confirms that they want to receive your messages. Note that if a profile has already subscribed to SMS (even if they have been deleted and since returned), new **Subscribed to SMS Marketing** events will not be recorded.
- ****Unsubscribed from SMS Marketing****
  When a recipient texts unsubscribes from your SMS messages, either by clicking an unsubscribe link or texting an opt-out keyword (e.g., STOP).
- ****Toll-free number not verified****Indicates that your toll-free number has not been approved, so your subscribers are not receiving messages to their device. Ensure that the toll-free number is **Verified** or **Approved** in the SMS settings section of your Klaviyo account. Refrain from sending SMS via campaigns flows until your number is verified.
- ****Failed SMS Age Gate****
  When someone tries to sign up to receive SMS from an age-gated brand, but they are either underage or in a country where SMS age-gating is not available. This event shows the method as "age gate" and the individual's age gated DOB (MM/YYYY).

## Additional resources

- [How to increase SMS click rates](https://help.klaviyo.com/hc/en-us/articles/4404565738395)
- [Understand SMS filtering by wireless carriers](https://help.klaviyo.com/hc/en-us/articles/360039239172)
- [SMS marketing strategies for all levels [+12 Pro tips]](https://www.klaviyo.com/blog/sms-marketing-strategies)
