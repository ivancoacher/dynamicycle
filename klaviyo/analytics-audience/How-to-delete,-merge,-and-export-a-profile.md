---
id: 115005073847
title: "How to delete, merge, and export a profile"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005073847-How-to-delete-merge-and-export-a-profile"
section: "Profile management"
category: "Audience"
category_slug: "analytics-audience"
klaviyo_updated: "2026-04-21T13:54:17Z"
language: en
---

## You will learn

Learn how to delete, merge, and export profiles in Klaviyo in order to keep your account organized. For general information about profiles, head to our article on [profiles in Klaviyo](https://klaviyo.zendesk.com/hc/en-us/articles/115005247088).

## Delete, merge, or export a profile

1. Navigate to a specific profile by entering their email address or name into the main search bar at the top of your account labeled **Search,** and select the **Search in profiles**options.
2. Once you are on the customer's profile, select the ****Profile actions**** button
   ![Profile actions button in header of profile.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28720667101211)

### Delete a profile

To delete a Klaviyo profile:

1. Click ****Delete Profile**** in the **Profile actions**dropdown.
2. In the popup that appears, select ****Delete Profile.****

Learn more about [recording GDPR deletion requests](https://help.klaviyo.com/hc/en-us/articles/360004217631-How-to-Handle-GDPR-Requests#record-gdpr-deletion-requests).

For a profile's event history, any customer-specific information is replaced with the word "redacted," and the customer's information is permanently deleted from Klaviyo.

For every recipient record associated with a profile, the profile's email address is replaced with a random email address that starts with the word "redacted." For example, redacted.11bab993-58bb-4cc9-a654-c152dbe009e1@example.com.

![A redacted email address](https://klaviyo.zendesk.com/hc/article_attachments/28720621746587)

If someone is removed from a list and then re-added to that same list, they will not re-enter any flows triggered by that list. Learn more about [profiles and list-triggered flows](https://help.klaviyo.com/hc/en-us/articles/360003031652-Guide-to-Creating-a-List-Triggered-Flow).

### Merge 2 profiles

There are a few cases when you may want to merge a profile with another. Example situations include:

- The same contact in your account has 2 different profiles with 2 different email addresses; merging these profiles will result in only 1 profile, with 1 email address for that contact.
- The same contact has 2 profiles where one includes a typo in their email address; merging will ensure that you only work with the active profile and consolidate data for the false profile.

To merge a profile:

1. Navigate to the profile and select ****Merge Profile****under **Profile actions.**
2. In the popup that appears, type the email address or name of the profile you want to merge into (keep), then use the Return or Enter button on your keyboard to search
3. Select a profile from your search results
   - If you don’t see the profile you’d like to merge into, make sure there are no typos in your search, then use the Return or Enter button to search again
4. Click ****Merge Profiles****

The merging process takes a few moments to complete. This action is permanent.

When merging profiles, events are replayed and show a **Record on** date later than the event timestamp.

![A user merges two Klaviyo profiles](https://fast.wistia.com/embed/medias/gmbodq21od/swatch)

Properties on the profile you keep will remain intact. Properties on the profile you remove will be added to the profile you keep only when they do not already exist on the remaining profile. There are 2 exceptions:

- ****Timezone****
  The timezone from the source profile will be kept
- ****Location****
  Location information is kept from the profile with most location info. For example, if the source profile has the full street address and the destination profile only has the city, the merged profile will have the full street address.

|  |  |  |
| --- | --- | --- |
| ****Merge this profile... (remove this profile)**** | ****...into this profile  (keep this profile)**** | ****Result**** |
| ****Contact****  **Email**: removeme@email.com  **First Name**: John  **Last Name**: Klaviyo  ****Custom Properties****  **Gender**: Male  **Favorite Color**: Red  **Shirt Size**: Medium | ****Contact****  **Email**: john.klaviyo@email.com  **First Name**: John  **Last Name**: Klaviyo  ****Custom Properties****  **Gender**: Male  **Favorite Color**: Klaviyo Green | ****Contact****  **Email**: john.klaviyo@email.com  **First Name**: John  **Last Name**: Klaviyo  ****Custom Properties****  **Gender**: Male  **Favorite Color**: Klaviyo Green  **Shirt Size**: Medium |

When merging profiles, all the event data for the source profile will be copied over to the destination profile as well.

If you merge a suppressed profile with an active profile, the resulting profile will be suppressed by default.

### Export a profile's data

1. Navigate to the profile you want to export and click ****Export profile****under the **Profile actions** dropdown.
2. In the modal that appears, click ****Start Export**** to export the profile data

A green callout will confirm that your profile data is available on your [**Downloads** page](https://www.klaviyo.com/downloads). From your **Downloads** page, click ****Download**** to export your profile data as a .zip file.

![Klaviyo's file download button](https://klaviyo.zendesk.com/hc/article_attachments/28720621743643)

## Additional resources

- [Guide to active email profiles](https://klaviyo.zendesk.com/hc/en-us/articles/115005246968)
- [Guide to list cleaning](https://klaviyo.zendesk.com/hc/en-us/articles/115005078347)
- [Guide to suppressed email profiles in Klaviyo](https://klaviyo.zendesk.com/hc/en-us/articles/115005246108)