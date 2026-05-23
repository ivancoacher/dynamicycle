<h1>Frequently asked questions about identity resolution in Klaviyo</h1>

## You will learn

Learn about frequently asked questions related to identity resolution in Klaviyo. If you don’t see your question in the resource below, please reach out on our [Community](https://community.klaviyo.com/) forum.

## What is identity resolution?

Identity resolution refers to the ability to maintain a single customer record, even when a customer uses different combinations of identifiers and channels over time. This provides a unified view of your customers regardless of how they interact with your brand.

A common example of this is when a customer that has an email profile in your Klaviyo account later subscribes to SMS through a method that is not associated with their email, like a [keyword opt-in](https://help.klaviyo.com/hc/en-us/articles/360050384091). This customer action results in a separate profile for receiving SMS messages and a separate profile for receiving emails. However, if this customer later takes an action (like making a purchase) where they submit both their phone and email; Klaviyo recognizes that both the phone and email belong to the same customer and merges the profiles.

Klaviyo’s identity resolution functionality has 2 key components:

- ****Identity capture****
  Klaviyo’s identity capture functionality automatically cookies and identifies users that click through your email or submit a Klaviyo form, allowing you to capture your customer’s activity on your website.
- ****Deterministic profile merge****
  Klaviyo resolves customer identities through a proactive check that merges 2 separate profiles when an [action](#h_01GVZT1MQTSY5TWF22SA9D1GAX) occurs linking an email address, phone number, or device ID (currently, iOS) together. This allows you to manage omnichannel customer data effectively.

## How profiles are merged

### What is deterministic merging and how is it different from probabilistic merging?

Probabilistic merging is another type of profile merging that ties engagements made by a single user across multiple devices to a unified customer profile. Probabilistic merging uses predictive algorithms to link information, such as IP address, operating system, location, Wi-Fi network, and behavioral data to an individual. This type of merging is often applicable to one-to-many communications and marketing.

Meanwhile, deterministic merging leverages first-party data that customers have provided and unifies their engagements. Engagements are only linked based on information that your customers provide to you directly, prioritizing the accuracy of your customer profiles. This type of merging is critical for one-to-one communication and personalization.

### What triggers a profile merge?

For Klaviyo to identify that multiple profiles belong to the same customer and merge them, the identifiers associated with each profile need to be recognized together. Often, this information comes in the form of an event, where the event data includes multiple identifiers like email and phone number.

A common example is a **Started checkout** event, where the customer provides both their email address and phone number. If there is a separate phone-only profile from a previous action the customer took (e.g., submitting a phone-only form or texting a keyword), Klaviyo will recognize these belong to the same customer and merge them under the profile with the stronger identifier. For more information on identifier precedence, see our guide to [understanding identity resolution in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/12902308138011).

In addition to merging based on event data, Klaviyo checks if there is an opportunity to merge when customers provide their information through an opt-in method, like a form with phone number and email fields.

Klaviyo also checks for opportunities to merge profiles based on information submitted implicitly through [cookie tracking](https://help.klaviyo.com/hc/en-us/articles/360034666712), which associates an activity to an email profile. For example, if an email profile submits a phone-only form with their cookie present, then the phone number they provided will be appended to their pre-existing profile.

Additional examples that would result in a profile merge:

- A phone-only profile provides an email address which matches an existing profile.
- An email-only profile provides a phone number which matches an existing phone-only profile.
- A customer with a separate email-only profile and phone-only profile clicks on a button in an email that directs to a form embedded on your store’s website, and submits their phone number there.
- An email-only profile being tracked through the Klaviyo cookie clicks on an SMS shortened link on the same device and browser.
- A customer with an email-only profile is targeted with an SMS consent form or emailed a link to an SMS consent form. Their form submission can be then traced to their email via cookie, and the phone number will be appended to the pre-existing profile.

### What types of events will not trigger a profile merge?

Actions related to tap-to-text (e.g., a [tap-to-text banner in an email](https://help.klaviyo.com/hc/en-us/articles/8185730542235) or [form](https://help.klaviyo.com/hc/en-us/articles/9351341171995)) and [keywords](https://help.klaviyo.com/hc/en-us/articles/360050384091) will generally not result in a merge based on cookie tracking. This is because the cookie trail is lost across applications (web to SMS) and Klaviyo cannot be certain that the 2 actions were taken by the same person.

Examples of cases where profiles would not merge :

- A customer with an email-only profile and phone-only profile clicks-to-text from an email or targeted form.
- A customer with an email-only profile and phone-only profile sees a keyword call-to-action on an email or targeted banner and texts the keyword.

### If separate profiles take cookied actions on the same device and browser, will the profiles be merged?

If a customer with an email-only and a phone-only profile meets both of the following conditions, the profiles will be merged:

- Has a browser session open from a link in an SMS message
- Clicks a link in an email in the same browser and device

### Is it possible the source profile will get re-created if both email addresses are still present in an ecommerce integration?

When a pair of profiles are merged, the source profile is essentially deleted. If a source profile is merged into a destination profile, and Klaviyo then receives another event with the email address from the original source profile, a new profile is created with that email address.

### What is a destination vs. source profile?

During the merge process, there are 2 profiles that are consolidated together. One profile is preserved and the other is merged. These profiles are called the “destination” and “source profiles.”

- ****Destination profile****
  The profile that is preserved during a merge is the destination profile. This profile has the [higher-ranking identifier](https://help.klaviyo.com/hc/en-us/articles/12902308138011) of the pair of profiles involved in a merge.
- ****Source profile****
  The profile that has its data merged into the destination profile is the source profile. This source profile has the [lower-ranking identifier](https://help.klaviyo.com/hc/en-us/articles/12902308138011) of the pair of profiles involved in a merge.

## Profile data

### What happens to the data on the source profile when it is part of a merge?

When a source profile has merged into a destination profile, a **Merged profile** event is added to the destination profile. All events from the source profile will migrate into the destination profile as well.

Events appear in the timeline with the original timestamp and are attributed to the destination profile. The destination profile also inherits the list memberships of the merged profile. Note that the destination profile may not meet the same segment criteria as the source profile.

### How are profile properties handled when a profile is merged?

Profile properties are added to the destination profile unless each profile has the same property but with different values. In that case, the destination profile’s properties take higher precedence.

There are 2 exceptions:

1. Timezone: Klaviyo uses the timezone from the source profile only.
2. Location: Klaviyo will use the location of the source profile if it has more location data (address, city, country, etc.).

### Will a profile’s skipped messages be merged as well?

A profile’s [skipped messages](https://help.klaviyo.com/hc/en-us/articles/1260805003210) will merge for both flow and campaign messages and be visible in the **Messages** tab of the destination profile.

### How are consent and exclusion records treated during a profile merge?

For exclusion records (i.e., hard bounces, unsubscribes, or spam complaints):

- If the destination profile has no exclusion record and the source profile does, Klaviyo uses the record from the source profile.
- If both the destination profile and source profiles have exclusion records:

- If they have the same exclusion record, Klaviyo uses whichever date is older.
- If they have different exclusion records, Klaviyo uses the record from the source profile for the destination profile.

For [consent records](https://help.klaviyo.com/hc/en-us/articles/360037101072):

- If the destination profile has no consent record and the source profile does, Klaviyo uses the record from the source profile.
- If both profiles have consent records, updates happen in the following ways:

- If the 2 profiles have the same consent status and the source consent record is older than the destination consent record, the source profile’s record is used on the destination profile.
- If the records do not have the same consent status and the destination record is older than or the same age as the source record, the source profile’s consent record is used.

Here are some examples that illustrate these cases:

|  |  |  |
| --- | --- | --- |
| ****Source profile**** | ****Destination profile**** | ****Final merged profile**** |
| Shows as "subscribed" for email marketing, dated 05/01/2021 | Shows as "subscribed" for email marketing, dated 06/01/2021 | Destination profile updates subscribed date to 05/01/2021 |
| Shows as "subscribed" for email marketing, dated 05/01/2021 | Shows as "unsubscribed" for email marketing, dated 06/01/2021 | Klaviyo does not update the destination profile record. It would stay as "unsubscribed" dated 06/01/2021. |
| Shows as "subscribed" for email marketing, dated 05/01/2021 | Shows as "unsubscribed" for email marketing, dated 04/01/2021 | Destination profile updated to "subscribed," dated 05/01/2021 |
| Shows as "unsubscribed" for email marketing, dated 05/01/2021 | Shows as "subscribed" for email marketing, dated 05/01/2021 | Destination profile updated to "unsubscribed," dated 05/01/2021 |

Consent is never added to a phone number without explicit consent from that specific phone number.

### Would active coupons under the source profile merge over to the destination profile?

The assignment of coupon codes to customer profiles is not altered during a profile merge, so active coupons on the source profile would not be valid codes for the destination profile.

## ****Flows****

### How does profile merging impact flows?

If either the source or destination profile has already completed or canceled the flow, the remaining flow messages are canceled. If both sources are still pending, the source profile’s flow is canceled, and the destination profile continues uninterrupted in the flow.

If the source profile is in a flow that the destination profile is not in, the destination profile takes the place of the source profile in the flow.

### How are date-triggered flows affected?

The source profile is merged into the destination profile and the date value that exists on the destination profile would remain. The destination profile then continues to move through the date-triggered flow like normal.

### Can a profile still qualify for a list-triggered flow if the merged profile already went through that flow?

When merging profiles, Klaviyo copies flow evaluations from the source profile to the destination profile, which prevents this from happening.

The full logic for this step is:

1. If the source profile is in the flow, but the destination profile is not, the destination profile takes the place of the source profile in the flow.
2. If the destination profile is in the flow, but the source profile is not, the destination profile continues through the flow uninterrupted.
3. If both profiles are in the flow:

- Klaviyo cancels the flow for the source profile. The source profile record is deleted on merge and the destination profile continues in the flow uninterrupted.
- If the source profile is in a flow and the destination profile has completed or been skipped for the flow, the flow is canceled for the source profile.
- If the source profile has completed a flow and the destination profile is in the flow at the time of merge, the flow is canceled for the destination profile.

## Additional resources

- [Understanding profiles in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115005247088)
- [Understanding when SMS profiles merge](https://help.klaviyo.com/hc/en-us/articles/360035588012)
- [Understanding identity resolution in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/12902308138011)
