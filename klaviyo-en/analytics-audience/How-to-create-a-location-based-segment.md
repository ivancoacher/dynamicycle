---
id: 115005065887
title: "How to create a location-based segment"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005065887-How-to-create-a-location-based-segment"
section: "Segment examples and types"
category: "Audience"
category_slug: "analytics-audience"
klaviyo_updated: "2026-04-21T13:54:16Z"
language: en
---

## You will learn

Learn how to use location-based segments to send campaigns by region, target forms to customers in a particular area, or better understand a subset of your customers. Note that Klaviyo determines a profile's location when syncing a billing address for that contact or, if they have not yet purchased, by tracking their IP geolocation. Learn more about [how location is set on Klaviyo profiles](https://klaviyo.zendesk.com/hc/en-us/articles/115005073907).

## Create a location-based segment

When creating a location-based segment, use the condition of **Properties about someone.** Then, choose between country, state/region, zip code, or timezone to further define this segment.

When you choose ****Zip code****, the segment builder defaults to the operator "includes any of", which supports the selection of ****multiple zip codes****. You can select up to 500 zip codes from the dropdown, and you can click "****Add Zip Code****" to bulk add up to ****500**** zip codes at once.

![](https://klaviyo.zendesk.com/hc/article_attachments/47099137466779)

![](https://klaviyo.zendesk.com/hc/article_attachments/47099137469211)

![](https://klaviyo.zendesk.com/hc/article_attachments/47099146168987)
Another example is if you want to create an email targeting North Americans in colder climates, you could use the following segment definition:

****Properties about someone > Country > equals > Canada****

****OR****

****Properties about someone > State / Region > equals > Massachusetts****

****OR****

****Properties about someone > State / Region > equals > ...****

![A segment of profiles in Canada and New England](https://klaviyo.zendesk.com/hc/article_attachments/28720667010587)

Note that, by using the OR connector between these conditions, your segment will be more inclusive — so, someone can be from Canada but not from Massachusetts (and vice versa) and still make it into this segment. If you instead want to make your segment more exclusive, add conditions separated by an AND connector. In doing so, you're saying that all conditions must be true in order for someone to be included. For more information, head to our [AND vs. OR guide](https://klaviyo.zendesk.com/hc/en-us/articles/360036534631).

## Create a segment of profiles impacted by GDPR and UK GDPR

People located in the EU or UK are affected by certain data protection laws (GDPR and GDPR UK, respectively). To create a segment of profiles in these locations, use this definition:

****If someone is or is not within the EU (GDPR) > is within European Union****

****OR****

****Properties about someone > Country equals United Kingdom****

If you have profiles that contain multiple variations of “United Kingdom” stored in the location field (for example, “UK” or “united kingdom”), you should include all spellings in your segment.

Use this location-based segment if you only want to target your European customer base, or to exclude these customers from certain communication.

![A segment of customers impacted by GDPR](https://klaviyo.zendesk.com/hc/article_attachments/28720667016347)

## Segment by someone’s proximity to a location

You can also create location-based segments by focusing on profiles within a specific radius of a particular zip code (i.e., postal code). This functionality can only identify profiles in the:

- United States
- European Union
- United Kingdom
- Canada
- Australia
- New Zealand

For UK zip codes, we support filtering by outward code, not inward code or both outward and inward code (usually separated by a space). For example, if a person's full zip code is "SW1W 0NY," only the first piece ("SW1W") will work for these filters.

Let's say, for example, you have a popup shop in Boston and want to invite Boston-based customers who are in your email list. Create a segment with the following definition:

****Someone's proximity to a location > Person is within > 30 miles of > 02110 in > United States of America****

****AND****

****If someone can or cannot receive marketing > can receive email marketing > because person subscribed****

![A segment of profiles located near a certain zip code](https://klaviyo.zendesk.com/hc/article_attachments/28720667021467)

To segment on a profile's proximity to a location, a profile must have either the zip code and country properties set, or their [IP address captured for geolocation](https://help.klaviyo.com/hc/en-us/articles/115005073907).

## Additional resources

- [Getting started with segments](https://klaviyo.zendesk.com/hc/en-us/articles/115005237908)
- [Segment conditions reference](https://klaviyo.zendesk.com/hc/en-us/articles/115005062847)
- [Understanding when and how Klaviyo sets a profile's location](https://klaviyo.zendesk.com/hc/en-us/articles/115005073907)
- [Enhance restaurant guest relationships](https://academy.klaviyo.com/en-us/courses/enhance-restaurant-guest-relationships)