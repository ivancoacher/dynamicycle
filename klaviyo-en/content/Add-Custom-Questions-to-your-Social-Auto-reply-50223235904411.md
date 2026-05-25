---
id: "50223235904411"
title: "Add Custom Questions to your Social Auto-reply"
source_url: "https://help.klaviyo.com/hc/en-us/articles/50223235904411-Add-Custom-Questions-to-your-Social-Auto-reply"
section: "Social Auto-replies"
category: "Social Marketing"
category_slug: "content"
klaviyo_updated: "2026-05-12T20:51:56Z"
language: "en"
---
****Premium feature.**** Available on the paid Klaviyo Social Marketing plan.

Custom Questions extend the Social Auto-reply flow beyond email and phone collection. Before or after an Instagram user submits their contact information, you can ask them custom questions and store their answers as Klaviyo profile properties. You can then use those properties in segments and flows just like any other profile data.

This article walks through adding Custom Questions to an Auto-reply, where answers land on the profile, and how to put those answers to work.

## When to use Custom Questions

Custom Questions are useful any time you want richer zero-party data on a subscriber, going beyond their email or phone alone. Common patterns:

- Size, fit, or style preferences for apparel brands
- Pet name and breed for pet brands
- Goals or use cases for fitness and wellness brands
- Birthday month

## Add a Custom Question to your Social Auto-reply

1. In Klaviyo, open ****Social**** in the left navigation and select ****Auto-replies****.
2. Open the Auto-reply you want to add questions to (or create a new one following the steps in [Create a Social Auto-reply](https://help.klaviyo.com/hc/en-us/articles/41741460845339)).
3. After the email or phone collection step, add a ****Custom Question****.
4. Configure the question:

   - ****Answer type:**** ****Quick reply**** (the customer picks from options you define) or ****Open ended**** (the customer types any response)
   - ****Question text:**** The question posed in the DM (for example, "Are you a dog or cat person?")
   - ****Profile property:**** the Klaviyo profile property where the answer will be saved.
   - For Quick reply, set a ****Label**** (what the customer sees in the DM, emojis allowed) and a ****Value**** (what's saved to the profile property).
     - For example, show "Dog 🐶" as the label, but save "dog" as the value.
5. Add additional Custom Questions in sequence if needed, up to a maximum of ****5 custom questions per Auto-reply****. Each question runs after the previous one is answered.
6. Save the Auto-reply.

![Software interface for creating an auto-reply custom question with a "dog or cat person" question and quick reply options, displayed next to a mobile chat preview of the auto-reply in action.](https://cdn.sanity.io/images/6ct6b26e/help-center-prod/b5c99eea1ff84c94cded639e9aae2be353762e92-3024x1574.png)

## How customers experience Custom Questions

- For ****Quick reply**** questions, Klaviyo presents the options in the Instagram DM and the customer picks one.
- For ****Open-ended**** questions, Klaviyo accepts whatever the customer types as their answer.
- There's no built-in skip option. Customers move through the sequence by responding to each question.
- If a customer abandons the conversation midway through Custom Questions, any answers they've already submitted are saved to their profile, but only if they have already provided their email address or phone number in that conversation. If the customer abandons before submitting their email or phone, no Custom Question answers are saved.

## Where answers land on the profile

Each Custom Question maps to a Klaviyo profile property under the Custom Properties section of the profile. You can create a new profile property or select an existing profile property during the Auto-reply configuration. When a customer answers the custom question, Klaviyo saves their answer to that property on their profile.

Custom Question properties behave the same as any other profile property in Klaviyo. You can:

- Filter segments by them
- Reference them in flow conditional splits
- Use them as personalization tokens in email and SMS content
- Export them with the rest of your profile data

## Use Custom Questions in segments

A few example segments built on Custom Question data:

- ****Fitness goals.**** Targeted product launches or content based on the goals of your audience.
- ****Birthday in the next 30 days.**** Feeds a birthday discount campaign.
- ****Product preferences.**** Targeted promotions based on product preferences, eg. dressy vs casual.

To build a segment, create a new segment with the condition ****Properties about someone**** and choose the profile property your Custom Question writes to.

## Use Custom Questions in flows

Custom Question answers can drive flow logic. A few patterns:

- ****Trigger / Conditional split:**** branch a welcome flow based on the customer's answer (for example, send different product picks to "Pet: dog" vs "Pet: cat").
- ****Conditional content:**** use the answer as a personalization token in the email body, subject line, or SMS message.
- ****Filter the flow:**** prevent customers from entering a flow unless they've answered a specific question.

You can update the property later through other channels (forms, profile updates, additional auto-replies) without breaking these flows.

## Things to know

- If the customer drops off before providing their email address or phone number, no answers are saved.
- You can add up to 5 Custom Questions per auto-reply.
- Answer types are ****quick reply**** or ****open ended****. Other formats (number, date, multi-select) are not available at this time.