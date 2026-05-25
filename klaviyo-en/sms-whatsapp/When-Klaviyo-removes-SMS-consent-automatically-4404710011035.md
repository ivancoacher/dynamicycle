---
id: "4404710011035"
title: "When Klaviyo removes SMS consent automatically"
source_url: "https://help.klaviyo.com/hc/en-us/articles/4404710011035-When-Klaviyo-removes-SMS-consent-automatically"
section: "Manage your SMS profiles"
category: "SMS"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-21T13:54:58Z"
language: "en"
---
## You will learn

Learn when Klaviyo will automatically remove consent from an SMS subscriber.

## Times when SMS consent is removed automatically

Usually, someone is automatically unsubscribed from SMS for the following reasons:

- [The subscriber has opted out](#h_01G9QQ97VS4S6X817TVHX54K97)
- [The subscriber changed phone numbers or carriers](#h_01G9QQ9YZ9Y13MQKSN8GQX02ZP)
- [The subscriber is a known litigator](#h_01HTG3BVNJM63NTPK30GM2HNFF)
- [Klaviyo detects a landline number](#h_01GRBRCJCJKXTPCYE55E1CT2D6)
- [Wireless carriers block a message](#h_01GRBRCXY8QG29J5AHQS7TYB2F)

## Subscriber opted out via a keyword

The most common reason why Klaviyo will remove SMS consent is when the subscriber opts out using one of the following keywords:

- STOP
- STOPALL
- UNSUBSCRIBE
- CANCEL
- END
- QUIT

At this point, the subscriber clearly communicated that they no longer wish to receive SMS messages from your brand. Thus, Klaviyo will make sure no new texts can be sent to this number until that individual resubscribes.

## Subscriber changed numbers or providers

Wireless carriers each have their own list of customers. The list is updated when someone:

- Gets a new number
- Leaves that wireless carrier

When either of these situations happens, consent for that number no longer applies, regardless of whether someone changes or keeps their number when they switch providers. Since carriers don’t track when someone gets a new number, continuing to send to someone after they change providers puts you at risk of messaging someone who wasn’t the original subscriber and who never opted in.

As of September 2021, Klaviyo receives daily reporting of numbers that carriers have identified as deactivated. A number must be deactivated for 45 days before it can be reassigned to a new user. Klaviyo processes deactivation lists on a daily basis and removes SMS consent for any profile associated with a number appearing on the deactivation list.

If this is the case, you’ll see the unsubscribe reason listed as: **Carrier Deactivation**.

### Maine phone number is on the RND list

Similarly, Klaviyo regularly checks the Reassigned Numbers Database (RND) for Maine numbers. As of July 2024, [Maine enacted specific legislation](https://legislature.maine.gov/legis/bills/getPDF.asp?paper=HP1433&item=1&snum=131) requiring telemarketers to remove consent from any Maine phone numbers on the RND.

This RND scrub is different from Klaviyo’s daily deactivation list scrubs. Carriers are only required to upload lists of deactivated numbers to the RND once a month. Klaviyo’s daily deactivation scrubs are intended to catch deactivated numbers before they even appear on the RND. Maine law, however, requires that callers query the RND directly in order to comply. As such, Klaviyo will be running monthly scrubs of the RND for Maine numbers.

This service is both automatic and free for every Klaviyo account. While the RND does charge by the number of phone number inquiries, you don’t have to pay Klaviyo an extra fee. Additionally, this is a compliance requirement for Maine, so you don’t need to opt in or toggle on any setting.

When this occurs, you’ll see the unsubscribe reason listed as: **Number Reassigned**.

## Subscriber is a known litigator

To safeguard accounts, Klaviyo helps prevent known litigators from becoming SMS subscribers.

As of April 4, 2024, Klaviyo will prevent anyone from subscribing to SMS if they are known or suspected to have threatened to sue, unless you opt out of this safeguard. Note that SMS Litigator Protection is based on the profile’s phone number.

Klaviyo will only remove SMS consent. If a profile is subscribed to another channel, consent for that other channel will not be removed.

SMS Litigator Protection is not a guarantee. While it is a safeguard against many known litigators, Klaviyo makes no representations that the use of this feature will prevent litigation entirely.

The unsubscribe reason is:

- **Known Litigator**

If you want to opt out from this feature (and allow known litigators to stay as SMS subscribers), navigate to ****Settings > SMS > Sender preferences**** and uncheck the box in the **Unsubscribe known SMS litigators** section.

****Why use SMS Litigator Protection?****

As text message marketing has grown more popular, so has the number of lawsuits under the TCPA, GDPR, and other laws that regulate SMS.

Klaviyo’s SMS Litigator Protection helps safeguard your brand from potential legal issues.

## Klaviyo detects a landline number

If anyone adds a landline number to a sign-up form or you try to import a landline number, Klaviyo will automatically remove consent. This way, you won't waste credits sending to a number that can't receive SMS messages.

- **Landline detected**

![mceclip0.png](https://klaviyo.zendesk.com/hc/article_attachments/28717383485851)

## Wireless carriers block a message

This case typically only applies to toll-free numbers after someone opts out and then tries to opt back in.

If one of your subscribers texted STOP to unsubscribe, they must use UNSTOP or START to resubscribe. If your customer tries to resubscribe using any other method (e.g., a sign-up form), wireless carriers won't deliver your messages.

If you have a toll-free number and someone previously texted "STOP," the only way for them to be resubscribed is for them to text the words "START" or "UNSTOP." This is required by wireless carriers in order for them to deliver messages.

For these keywords, you must also have a list titled: SMS Subscribers. (The capitalization must match exactly as shown here.)

In this case, Klaviyo receives a **Message Blocked** error from the carriers, and will remove SMS consent from that profile.