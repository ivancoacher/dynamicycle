---
id: 115005247028
title: "Understanding the information section of a profile"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005247028-Understanding-the-information-section-of-a-profile"
section: "Understand profiles"
category: "Audience"
category_slug: "analytics-audience"
klaviyo_updated: "2026-05-11T12:54:50Z"
language: en
---

Learn about the information section of a profile in Klaviyo, which contains details such as when and how the profile found you and the last time they were active.

## What information is available

The **Information** section of a Klaviyo profile contains the following information:

- The Klaviyo-assigned **First Active** and **Last Active** dates
- How they found you
- Custom properties
- The date and time the profile was created
- The date and time the profile was updated

![Information section on profile](https://klaviyo.zendesk.com/hc/article_attachments/28711676186395)

## First active and last active

**First Active** and **Last Active** are dynamic properties that reflect when a profile interacted with your brand through a tracked active event.

The calculation provides consistent and reliable data for flows, segments, and the public APIs. The calculated values are refreshed frequently for all profiles that have an active event during that time window.

- First active: This is the timestamp of the earliest recorded active event for a profile.
- Last active: This is the timestamp of the most recent recorded active event for a profile.

### Active vs. passive events

The system distinguishes between events that represent direct customer engagement ("active") and those that reflect a system action or passive delivery ("passive").

#### Active events

Active events are used to calculate the first and last active dates. These include:

- All customer-defined event types.
- Klaviyo-defined events that represent a direct action (e.g., viewed product, added to cart, placed order).

#### Passive events (excluded)

Events that do not update the first active or last active properties include system-level and passive delivery events such as:

- Email delivery events (e.g., email delivered, email bounce).
- Messaging relay or receipt events (e.g., $received\_push, $received\_sms, $received\_whatsapp, $relayed\_sms, sent message).
- Bounce and failure notices (e.g., $bounced\_push\_send, $bounced\_silent\_push\_send, $received\_automated\_response\_sms).

  A few things to note: If someone is manually uploaded to a list, this does not set the first active date. Even if this person receives a message, this property is not created. This property is only set if the person either:
- Opens or clicks a message.
- Takes an action that is tracked by Klaviyo.

The first active date can be before their profile created date. This happens when someone first engaged with your organization before you created your Klaviyo account, but Klaviyo was able to sync historical activity through an integration (with your previous esp, for example). In this case, the first active date is set as the contact's earliest recorded activity.

## How they found you

Klaviyo only populates a profile with **How They Found You** information if [web tracking](https://klaviyo.zendesk.com/hc/en-us/articles/115005076767) is set up on your website.

The **Source** value represents how the contact ended up on your website when Klaviyo's web tracking JavaScript first saw them. The possible values are:

- ****Direct****
  The person either entered your site URL directly in their browser or, more likely, Klaviyo doesn't know where the person came from.
- ****Referral****
  The person came from another website by clicking a link on that site.
- ****Organic****
  The person either came to your site from a search engine or you'll see a custom value here if there was a "utm\_campaign" set in the URL the person landed on.
  ![How they found you section](https://klaviyo.zendesk.com/hc/article_attachments/28711697647771)

  In the example above, this particular contact was referred from Google, meaning they landed on the website after clicking through a Google search.

  **Campaign**, **Medium**, **Content**, and **Term** fields are populated if an individual landed on your website after clicking through a campaign where Google Analytics tracking was added to links within the email:
- ****Campaign, utm\_campaign****
  This is the name of the campaign.
- ****Medium, utm\_medium****
  The channel through which you sent this content; e.g., email or SMS.
- ****Term, utm\_term****
  This is an optional UTM parameter that marketers can set to track paid search terms.
- ****Content, utm\_content****
  This is an optional UTM parameter that marketers can set to differentiate between ads.

  Say you use Klaviyo to automatically add Google Analytics tracking to links within a campaign or flow, and someone clicks through one of these messages and lands on your website for the first time. In this case, Klaviyo also tracks **Source**, **Campaign**, and **Medium**:
- ****utm\_source****
  The name of the list or segment the campaign was sent to
- ****utm\_medium****
  The channel through which you sent the campaign or flow (e.g., email)
- ****utm\_campaign****
  The campaign name (campaign ID)

UTM values are not set on profiles if the campaign value is referral, direct, or organic.

The **First Page** property will contain the URL of the first page the contact visited after navigating to your website.

If you want to segment on **Source** within the **How they found you** section, use the **UTM Source** property in the segment builder. If you want to segment by **Campaign**, use **Initial Source** in the segment builder.

## Profile updated and profile created

The **Profile Created** date represents the date a profile was created. As explained [above](#h_01EEBECY7Q4P4H2G6FZY4WYV76), this date may or may not align with the **First Active** date:

- If someone engages with your organization for the very first time and this activity is synced in real time to Klaviyo, the **First Active** and **Profile Created** dates can be identical.
- The **Profile Created** date reflects the date this person's profile was created by Klaviyo.
  - However, if someone engages with your organization for the first time before you start using Klaviyo but you sync or import historic data, Klaviyo backdates a contact's **First Active** date (if this date is available).
- If someone is imported into Klaviyo but there's no tracked activity, there can be a **Profile Created** date but no **First Active** date.

The **Profile Updated** date and time indicates the last time the profile itself was updated, and the **Last Active** date and time matches the time of the latest event on the profile.