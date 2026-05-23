<h1>Understanding State Laws Limiting Frequency of Marketing Text Messages</h1>

Certain states — including Florida, Oklahoma, Oregon, and Maryland — have enacted regulations that limit how many promotional text messages a person can receive within a rolling 24-hour period. Klaviyo will now automatically enforce text message state law frequency limits for recipients in these states to help better protect your brand from potential violations.

This information is intended solely for educational and informational purposes and should ****not**** be construed as legal advice. The content provided is general in nature and may not reflect the most up-to-date information. Klaviyo strongly advises consulting with a qualified legal counsel to ensure your compliance with applicable laws and regulations in connection with your use of our services.

## How it works

State law frequency limits are:

- On by ****default**** for all accounts
- Enforced only for numbers whose area code corresponds with ****Florida, Oklahoma, Oregon, and Maryland****
- Applied only to promotional SMS, MMS, and RCS messages
- Evaluated on a rolling 24-hour basis per phone number

![](https://klaviyo.zendesk.com/hc/article_attachments/44511215691803)

For each recipient, Klaviyo evaluates promotional text messages using a ****rolling 24-hour window****. This means the system continuously looks back 24 hours from the moment a new message is about to send. If the recipient has already received ****three**** promotional messages (across both campaigns and flows) within that rolling window, any additional promotional messages are automatically skipped until enough time passes for one of the earlier messages to fall outside that 24-hour look-back period.

### ****Example: How a rolling 24-hour window works****

- SMS #1 is sent at ****10:00 AM****
- SMS #2 is sent at ****12:00 PM****
- SMS #3 is sent at ****4:00 PM****

If you attempt to send SMS #4 at ****8:00 PM****, it is skipped because all three previous messages occurred within the ****last 24 hours****.

However, if you attempt SMS #4 the ****next day at 10:01 AM****, SMS #1 has now fallen outside the rolling 24-hour window, so only SMS #2 and #3 count. The send is allowed because the recipient now has fewer than three messages in the current window.

### Which messages are affected

State law frequency limits apply to messages that advertise or market something (i.e., that are promotional in nature). This includes both:

- Promotional campaign messages
- Promotional flow messages

  It does **not** apply to:
- Transactional messages
- Compliance keyword responses (e.g., STOP, HELP)
- Custom subscribe keyword replies (e.g., JOIN)
- Help Center conversation messages
- AI or live agent replies
- Text message previews

## View or change this setting

State law frequency limits are ****on by default****, and we recommend leaving it enabled if you send text messages to U.S. subscribers in Florida, Oklahoma, Oregon or Maryland.

To view or change the setting:

1. Select your account name in the lower-left corner.
2. Click Settings
3. Navigate to the 'Text Message' tab.
4. Scroll to the the 'State law frequency limits'
5. Toggle On or Off, then click Save.

Turning this feature off may increase your compliance risk in those states.

## How skipped messages due to state law frequency limits appear in Klaviyo

When this feature prevents a message from sending:

- The message is logged as a Skipped Text Message
- You’ll see a skip reason 'Skipped: Unable to send SMS' in the recipient activity tab of a sent campaign
- This reason will explicitly reference State law frequency limits in future updates

## State law frequency limits vs. Smart Sending

State law frequency limits and Smart Sending both have the ability to skip messages, but they solve different problems:

| Feature | Main Purpose | Applies to | Configurable? |
| --- | --- | --- | --- |
| ****Smart Sending**** | Improve subscriber experience | Promotional messages | Yes |
| ****State law frequency limits**** | Legal compliance in specific states | Promotional messages | No (always 3 messages per 24 hours) |

Smart Sending and State law frequency limits operate independently, and ****either one can skip a message****.

In practice:

- If a message violates your ****Smart Sending window****, it will be skipped for Smart Sending.
- If a message would exceed the ****three-message limit in 24 hours a regulated state****, it will be skipped due to State law frequency limits.
- When a message qualifies for both Smart Sending and State law frequency limits, ****Smart Sending will block it first****. The message still counts toward both limits, but Smart Sending has priority in determining the skip reason.

#### ****Example 1: Smart Sending skips the message****

- Smart Sending window = 24 hours
- You send a promotional text message to a recipient
- You attempt another send 1 hour later

Result: Skipped for Smart Sending, because that rule is met before any frequency issue applies.

#### ****Example 2: State law frequency limits skip the message****

- Smart Sending window = 1 hour
- You send 3 promotional text messages spaced 1 hour apart to a recipient with a phone number area code corresponding to Oklahoma, Oregon, Maryland, or Florida
- You attempt a 4th send within 24 hours to the same recipients as above

Result: Skipped due to State law frequency limits, because the recipient already received 3 promotional messages in the last 24 hours.

#### ****Example 3: Both conditions could apply, but only one will show****

- Smart Sending window = 1 hour
- The recipient (with an Oklahoma, Oregon, Florida, or Maryland area code phone number) has already received 3 promotional text messages in the past 24 hours (which would normally trigger State law frequency limits)
- You attempt a 4th send within 24 hours to the same recipients as above

Result: Skipped for Smart Sending, because Smart Sending takes priority even though the send would also exceed State law frequency limits. The message still counts toward both limits.
