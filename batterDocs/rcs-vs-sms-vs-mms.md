<h1>RCS vs SMS vs MMS</h1>

RCS, SMS, and MMS are all mobile messaging channels, but they differ significantly in capabilities, user experience, tracking, and performance measurement.

This article explains how each channel works, when to use them, and what to expect when comparing performance.

## ****Overview****

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ****SMS**** | ****MMS**** | ****Basic RCS**** | ****Single RCS**** |
| ****Delivery Receipts**** | Yes | Yes | Yes | Yes |
| ****Read Receipts**** | No | No | Yes | Yes |
| ****Click Tracking**** | Yes (via shortened links) | Yes (via shortened links) | Yes | Yes |
| ****Encryption**** | No | No | Yes | Yes |
| ****Character Limit**** | 160 (reduced to 70 with non-GSM characters such as emojis) | 1,600 (reduced to 1,000 with non-GSM characters) | 160 | 3,072 (text-only) or 2,000 (with media) |
| ****Media**** | No | Yes, but with size restrictions (one media file per message up to 600 KB) | No | High-quality media (one media file per message up to 100 MB) |
| ****Interactive Elements**** | No | No | Partial (quick actions in the US only) | Yes (cards, buttons, quick actions etc.) |
| ****Location Sharing**** | No | No | No | Yes  **not yet supported in Klaviyo** |
| ****Payment & App Integrations**** | No | No | Yes | Yes  **not yet supported in Klaviyo** |
| ****Device Reach**** | All mobile phones with a network connection | All mobile phones with a network connection | RCS-capable devices only (Android 5.0+ or iOS 18+ on supported networks) | RCS-capable devices only (Android 5.0+ or iOS 18+ on supported networks) |
| ****Verified Senders**** | No | No | Yes | Yes |
| ****Branded Senders**** | Partial (for alphanumeric senders only) | No | Yes (company logo & info page) | Yes (company logo & info page) |
| ****Message History**** | No | No | Yes | Yes |
| ****Throughput**** | Uses SS7 signalling via SMSCs, limited by payload and latency | Uses SS7 signalling + WAP/HTTP for multimedia, typically slower than SMS | Uses modern IP networks (LTE, 5G, Wi-Fi) for fast, efficient delivery | Uses modern IP networks (LTE, 5G, Wi-Fi) for fast, efficient delivery |

## ****Performance Metrics****

When comparing performance across channels, it is important to understand structural differences in how performance metrics are measured.

#### ****Delivery rates****

When comparing delivery performance across channels, it is important to understand how delivery is reported differently for SMS and RCS.

****SMS delivery reporting****

With SMS, delivery reporting is not always deterministic. Carriers do not consistently return a delivery receipt or a failure. For every message send via SMS, we receive either:

- A confirmed delivery receipt
- A failure event, or
- No explicit event is returned

  In a small percentage of cases (less than 3%) where no explicit event is received after 12 hours, the message is assumed to be delivered.

  ****RCS delivery reporting****

  With RCS, delivery reporting is deterministic. For every message sent via RCS, we receive either:
- A confirmed delivery receipt, or
- A failure event

  There are no assumed deliveries. Every message has a definitive status.

  ****RCS failure categories****
- ****Device unreachable**** - Delivery was attempted for up to 24 hours without success. After this window, the message is marked as failed and categorized as '****Device unreachable****'.
- ****Device not capable -**** The recipient’s handset cannot receive RCS. This may be due to RCS being disabled, an unsupported network, or an unsupported operating system. The message is marked as failed and categorised as '****Device not RCS capable****'.

If a failure is due to the device being incapable of receiving RCS, Klaviyo updates the phone number's metadata so that future text messages default to SMS for that recipient.

#### ****Click rates****

Note: if you have chosen not to exclude bot clicks from your reporting, RCS click rates may appear lower than SMS click rates. RCS experiences significantly fewer bot clicks due to how links and clicks are handled within the RCS ecosystem. As a result, RCS click rates are generally more reflective of genuine human engagement.

****Removing bot clicks in reporting****

Klaviyo recommends excluding bot clicks from both your account’s reporting data and attribution calculations. This way, your attribution windows for capturing actions align with your reporting data. Learn how to [remove bot clicks](https://help.klaviyo.com/hc/en-us/articles/11118357030555#h_01J5X2K26S69K6ZGMY3NDBX2J6).

****Note****. Even with bot filtering enabled, not all bot traffic can be removed from SMS reporting. As a result SMS click rates may appear higher than RCS.

****What to compare instead****

Rather than comparing raw click rates, we recommend focusing on:

- Conversion rate (placed order rate)
- KAV
- Revenue per recipient

These metrics better reflect real customer behaviour and true business impact.

#### ****Opt-outs****

Opt outs are separate from delivery failures and are handled differently across SMS and RCS.

****SMS opt outs****

An SMS opt out occurs when a recipient:

- Replies with a recognised keyword such as STOP (two way SIDs such as TFNs, LCs, or SCs), or
- Clicks an unsubscribe link (one way SIDs such as Alphas)

  In both cases:
- The recipient’s text messaging marketing consent is removed
- Future RCS and SMS messages cannot be sent unless the recipient opts in again

  ****Important****: If a recipient blocks a phone number directly on their device, this does not generate an event back to Klaviyo. Messages may continue to be technically delivered but will not be seen by the recipient.

  ****RCS opt outs****

  With RCS, recipients can opt out in two primary ways:
- Replying with STOP (or equivalent), or
- Clicking “Block this sender” within the RCS agent information screen

  In both cases:
- The recipient’s text messaging marketing consent is removed
- Future RCS and SMS messages cannot be sent unless the recipient opts in again

****Important****: If a recipient has iOS Unknown Senders filtering enabled and has not marked your RCS agent as known, messages may be routed to the Unknown Senders inbox and may not be actively seen. For more information, see [Understanding Unknown Senders filtering on iOS and how it affects RCS.](https://klaviyo.zendesk.com/hc/en-us/articles/42318061895579)
