---
id: 41066240307483
title: "Getting started with RCS"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/41066240307483-Getting-started-with-RCS"
section: "RCS"
category: "SMS"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-21T13:56:56Z"
language: en
---

Once an ****RCS agent**** is activated in your Klaviyo account, RCS becomes the ****default message format**** for all text messages in the countries where you have an active agent.

This means that any text messages sent via ****campaigns, flows, or conversations**** will automatically be delivered over RCS to RCS-capable devices. Recipients who are not RCS-capable will instead receive the SMS fallback.

## ****Why we make RCS the default****

RCS delivers a better messaging experience for both brands and customers; and in most countries, you can send text only messages over RCS at the same rate as SMS while gaining the advantages of a richer and more reliable channel.

Benefits of RCS over SMS include:

- ****Verified branded sender ID (SID):**** Messages are sent from your verified brand name, building trust and improving recognition with customers.
- ****Modern data networks:**** RCS is delivered over IP-based networks, which improves deliverability and throughput compared with legacy SMS channels.
- ****Open receipts:**** You gain visibility into when messages are opened, something not possible with SMS.
- ****Single-threaded communication:**** All customer conversations are maintained in one branded thread, instead of fragmented across multiple threads.
- ****Special character support****: RCS supports special characters without reducing your character limit, allowing you to use emojis, symbols, and accented characters without impacting your character count.
- ****No message add-ons****: RCS messages don’t require an organisation prefix or opt-out instructions within the message body, giving you more room for your actual message.

Additionally, if you use both RCS and SMS, messages will appear in separate threads; and any SMS messages sent from unbranded numeric senders may be mistaken for spam, as customers will recognise your verified RCS agent as the legitimate source.

## ****Why we don’t include message add-ons in RCS****

#### ****Org-Prefix****

RCS messages are sent from a verified branded sender ID, which displays your brand name and logo to recipients. This makes org-prefixes unnecessary.

#### ****Opt-out Instructions****

RCS messages do not require opt-out instructions to be appended to every message. This is because RCS includes native opt-out functionality via the agent information page, where recipients can click 'block sender' to stop receiving messages.

Brands may choose to append opt-out instructions manually, but Klaviyo will not automatically append this to every RCS message.

****Note****. If a recipient replies STOP or other equivalents, Klaviyo will always process the opt-out across both RCS and SMS.

#### Best practice:

Include a short instruction in your initial welcome message, such as “**Opt out at any time by replying STOP**”, and remind recipients occasionally. Because RCS provides built-in opt-out options, and we will always process STOP and other equivalents, there’s no need to include instructions in every message.

## ****Supported SMS Functionality****

All features available for SMS in Klaviyo also apply to RCS. For details, see our [SMS Help Center articles](https://help.klaviyo.com/hc/en-us/categories/29173800271259).

## ****SMS fallback****

Because not all carriers and devices support RCS, every RCS message includes an ****SMS fallback****. This ensures:

- RCS-capable recipients get the RCS version
- Everyone else still receives your message as an SMS

You can customise your SMS fallback separately to optimize for SMS and reduce costs (e.g. by removing special characters or media.

## ****Compliance and consent****

All ****SMS regulations also apply to RCS**** since both channels are delivered via carrier-managed networks and appear in the same inbox on a mobile device.

This means:

- ****SMS consent applies to RCS, and vice versa.**** You can send RCS messages to your existing SMS list without re-obtaining consent.
- ****Opt-outs apply across both channels.**** If a recipient opts out of RCS, you cannot revert to sending them SMS. They have opted out of **all** text messaging.

Always follow local SMS compliance requirements (e.g. opt-in rules, prohibited content etc.) when sending RCS.

## ****Plain text URLs****

Plain text URLs are not clickable in RCS rich cards. This affects both scheduled campaigns and existing flows with images.

#### ****Scheduled campaigns****

For scheduled campaigns, Klaviyo copies the SMS content into the RCS version. If the message includes an image, it will be formatted as a rich card, and any plain text URLs in the message will not be clickable. Before sending campaigns with images, move any URLs behind a button to ensure your links remain interactive.

#### ****Existing flows****

When RCS is activated, Klaviyo copies your existing SMS copy into the RCS version of each flow message so your messages continue to reach all recipients.

However, if a flow message includes an image, we will ****not copy the image across to the RCS version**** until you edit that flow. This is because images in RCS must be sent using rich cards, and rich cards do not support plain text URLs. We do this to avoid sending messages with links that do not work and to ensure you can choose the right label for the button containing your link.

Once RCS is activated, review any flow messages with images, and move any URLs behind a button if you wish to include the image in the RCS version.

## ****Contact Cards****

Contact cards are a specific MMS message type and therefore not supported in RCS. Instead of a contact card message, RCS supports a robust contact page which is commonly referred to as your RCS agent "contact card". When a subscriber received an RCS message and taps on the contact profile picture they are directed to your contact page within their messaging app.

Ability to save an RCS contact depends on a users mobile device and messaging app.

For more information on how to ensure your messages stay in the primary inbox, see [Understanding Unknown Senders filtering on iOS and how it affects RCS](https://klaviyo.zendesk.com/hc/en-us/articles/42318061895579).

#### ****Existing flows****

Review any existing flows that include contact cards and update the RCS version to remove mention of the contact card or use a [conditional split](https://klaviyo.zendesk.com/hc/en-us/articles/41072989967515) to avoid sending the message to RCS-capable devices.

## ****Pausing RCS****

If you want to stop sending RCS messages, you can ****deactivate your RCS agents****. Once deactivated, all text messages will revert back to SMS delivery.

- In the future, you’ll be able to do this directly in ****Klaviyo settings****.
- For now, if you want to pause RCS in a specific country, please ****reach out to Klaviyo Support****.

****Note****. When you pause RCS sending, RCS features such as the RCS editor and historical open event data will remain visible in your account.

## ****Best practices when getting started****

- ****Review scheduled campaigns:**** If your campaign includes an image, move any URLs behind a button to ensure links remain clickable in the RCS version.
- ****Review existing flows:****
  - For any flow messages with images, edit the message to copy the image across and move any URLs behind a button to ensure links remain clickable in the RCS version.
  - For any flow messages with contact cards, update the RCS version to remove mention of the contact card or use a conditional split to avoid sending the message to RCS-capable devices.
- ****Monitor performance:**** Use open receipts to track engagement, but note that read receipts are off by default on iOS and on by default on Android. This means read receipts are not a fully accurate measure of who has viewed your message, since most iOS devices will not return read data.
- ****Segment if needed:**** If you prefer to send only to RCS-capable recipients, use the [RCS capability property](https://klaviyo.zendesk.com/hc/en-us/articles/41072989967515) in segmentation.
- ****Check billing forecasts:**** While text-only RCS usually matches SMS pricing, adding rich content (images, buttons, carousels) will increase credit usage. Always review your billing forecast before sending.

## ****Known iOS rendering issues****

When sending rich RCS messages, please note that iOS devices do not always render content consistently. Known issues include:

- Images in rich cards may be cropped more aggressively on iOS than on Android, especially when card titles or descriptions are long (refer to [How to create rich interactive RCS messages in Klaviyo](https://klaviyo.zendesk.com/hc/en-us/articles/41072788661531) for more details).
- GIFs will display as static images on iOS (no animation).

  ****Recommendations:****
- Keep card titles and descriptions roughly the same length across cards to improve layout consistency on iOS.
- Avoid embedding critical content or text at the edges of your images, since cropping is more aggressive on iOS.
- Preview messages on both Android and iOS before sending to confirm acceptable rendering across devices.

## ****FAQs****

****Do I need to enable RCS manually in each campaign or flow?****

No. Once your RCS agent is activated, RCS automatically becomes the default text message format. All text message campaigns, flows, and conversations will use RCS for RCS-capable recipients.

****What happens if a recipient’s carrier or device doesn’t support RCS?****

They will automatically receive the SMS fallback. You don’t need to take any action to ensure message delivery.

****Can I choose to send messages only through RCS or only through SMS?****

Yes. While RCS will always deliver to RCS-capable devices by default, you can choose to target only RCS-capable or only SMS-capable recipients using the [RCS capability property](https://klaviyo.zendesk.com/hc/en-us/articles/41072989967515):

- ****Segmentation****: Build an audience of either RCS-capable or non-RCS-capable contacts and send your campaign to just that group.
- ****Conditional splits in flows****: Use the RCS capability property to create a conditional split in a flow.

This lets you run RCS-only or SMS-only campaigns and flows when you want to separate your strategy for each audience.

****Does RCS cost more than SMS?****

For basic text-only messages, RCS generally costs the same as SMS in most countries. However, for rich messages (e.g. rich cards), costs are usually higher

For pricing, please contact our [Sales team](mailto:sales@klaviyo.com).

****Can I stop using RCS after it’s been enabled?****

Yes. You can deactivate your RCS agent and all messages will revert back to SMS. For now, this requires contacting Klaviyo Support, but in future you’ll be able to manage this in settings.

****Are contact cards supported in RCS?****

No. Contact cards cannot be sent via RCS since you cannot save an RCS agent as a contact. If any of your existing messages include them, update the RCS version to remove mention of the contact card or use a conditional split to avoid sending the message to RCS-capable devices.

For more information on how to ensure your messages stay in the primary inbox, see [Understanding the Unknown Senders inbox on iOS and how it affects RCS](https://klaviyo.zendesk.com/hc/en-us/articles/42318061895579).

****Do I need separate consent for RCS?****

No. SMS and RCS share the same consent requirements. If you have already obtained SMS consent, you can send RCS to that profile. However, if someone opts out of RCS, that opt-out applies to all text messaging, and you cannot switch back to sending them SMS.