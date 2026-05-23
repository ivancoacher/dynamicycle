---
id: 35575786638107
title: "April 11 SMS opt-out compliance change"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/35575786638107-April-11-SMS-opt-out-compliance-change"
section: "North America: SMS compliance"
category: "SMS"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-21T13:54:41Z"
language: en
---

Find out about the FCC’s revocation rules that go into effect on April 11, 2025, and what updates Klaviyo made in response.

This information is intended solely for educational and informational purposes and should ****not**** be construed as legal advice. The content provided is general in nature and may not reflect the most up-to-date information. Klaviyo strongly advises consulting with a qualified legal counsel to ensure your compliance with applicable laws and regulations in connection with your use of our services.

## What are the key changes?

The [FCC’s ‘Revocation of consent’ ruling](https://docs.fcc.gov/public/attachments/FCC-24-24A1.pdf) gives consumers more ways to unsubscribe from SMS marketing programs.

The main highlights of these rules are that brands:

- Honor all of the following opt-out keywords:
  - STOP
  - QUIT
  - END
  - CANCEL
  - UNSUBSCRIBE
  - REVOKE
  - OPT OUT
- Action unsubscribe requests made by any “reasonable means” within 10 business days.
  - This means that consumers may opt out of SMS by sending a message expressing an intent to opt out, even if that message does not contain one of the above keywords.
- Honor unsubscribe requests made by consumers via telephone call or sent to a brand’s email address.
- May send 1 text confirming the opt-out as long as this acknowledgement is:
  - Sent within 5 minutes of the unsubscribe request.
  - Does not contain any marketing or promotional information.

To summarize, this new regulation significantly expands on the ways subscribers can opt out of SMS marketing.

## How is Klaviyo solving for the new revocation rules?

### Prior to April 11, 2025

Before April 11, 2025, Klaviyo supported the keywords STOP, QUIT, END, CANCEL, and UNSUBSCRIBE.

Additionally, you could choose when an opt-out [keyword would trigger an opt out](https://help.klaviyo.com/hc/en-us/articles/29109965092251). By setting a keyword to either “contains” or “exact match,” Klaviyo would unsubscribe someone when the opt-out keyword:

- Contains: appeared within a longer message (“Quit sending me texts”)
- Exact match: was the entire message (“Quit”)

You also have the ability to [manually remove consent](https://help.klaviyo.com/hc/en-us/articles/360051013832) at any time, such as if someone requests an unsubscribe without a keyword.

### As of April 11, 2025

Klaviyo is adding:

- An unsubscribe detection feature, which unsubscribes someone if their message likely contains a request to opt out.
  - Currently, this feature is only available for messages received from devices with a United States country code.
- 2 new unsubscribe keywords:
  - REVOKE
  - OPT OUT

****More about the unsubscribe detection feature****

The unsubscribe detection feature is on by default. You can turn it off, but this is not recommended if sending to anyone in the United States.

With this feature, Klaviyo looks for things like typos and alternate spellings as well as evaluating the overall message itself. So even if one of the listed keywords isn’t used, Klaviyo may still unsubscribe someone if the confidence is high enough that the message is conveying an intent to opt out.

For example, inbound messages such as “remove me,” “do not contact,” or “remove this number” would be categorized as an unsubscribe request. Thus, SMS consent from those profiles is automatically removed.

Additionally, you should make sure to review inbound messages at regular intervals to confirm the classifications made by the unsubscribe detection feature. It is ultimately your responsibility to comply with the FCC’s new regulations.