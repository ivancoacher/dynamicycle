<h1>How to upload a list of WhatsApp contacts</h1>

To import WhatsApp consent, you must be an Owner or Admin.

See how to upload a CSV of your WhatsApp subscribers into Klaviyo. Importing WhatsApp consent is an essential part of migrating providers and consolidating your marketing tech stack. Once this consent is in Klaviyo, you can start messaging your WhatsApp audience from around the globe.

## Before you begin

To import a list of WhatsApp contacts with consent, you should:

- [Set up WhatsApp in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/40111819732635).
- Turn off any welcome flows (those triggered by the **Subscribed to WhatsApp marketing** or **Subscribed to WhatsApp transactional** metric or the list you’re importing to).
  - Wait at least 2 hours after importing before you turn your flow live again.

****Why do I need to set up WhatsApp first?****

If you don’t set up WhatsApp up first, the import can add in the profiles and their phone numbers, but it won’t add consent for WhatsApp. Consent also won’t be added retroactively if you connect to WhatsApp later.

****Why should I turn off welcome flows?****

If you don’t, every new contact from the uploaded CSV will be added to any relevant welcome flow. Thus, you should set your welcome flows to manual mode before importing. Welcome flows include those triggered by either:

- The **Subscribed to WhatsApp marketing** or **Subscribed to WhatsApp transactional** metric
- The list you’re uploading to.

You should also wait at least 2 hours after the import finishes to turn these flows live again.

## Prepare your CSV for importing

### Include a phone number as the first or second column

Klaviyo uses either email or phone number as a profile’s unique identifier.

When importing:

- Use email as the first column if you have an email address for each person.
- Otherwise, use phone number as the first column.

Unlike with SMS, you don’t need to [include the subscriber’s country](https://help.klaviyo.com/hc/en-us/articles/5306587861531) when importing WhatsApp consent. (The only exception is if you want to import both SMS and WhatsApp consent.)

### Optional: indicate if consent is for marketing or utility WhatsApp messages

Currently, you can import consent for either marketing or utility (also called “transactional” in Klaviyo) WhatsApp messages.

If your CSV contains a mix of both, you can indicate the type of consent by adding 2 columns and labeling them:

- ****WhatsApp Marketing Consent****
- Marketing consent allows you to send any type of WhatsApp: both promotional (product announcement, abandonment reminder, etc.) and transactional messages. This is required if you want to import profiles with only marketing consent.
- ****WhatsApp Transactional Consent****
- WhatsApp transactional consent means you can only send Meta-approved utility messages.

### Optional: add consent status (subscribe, unsubscribed, never subscribed)

Including the consent status is recommended if your CSV includes a mix of either:

- Subscribed and unsubscribed subscribers
- Marketing- and transactional-only subscribers

  There are 3 consent statuses available:
- ****Subscribe****
  Person is opted in to receive messages.
- ****Unsubscribed****
  Person used to be subscribed but has since opted out. You cannot send messages if they are unsubscribed for that channel (e.g., you cannot send an SMS to someone who’s unsubscribed, but you may be able to send an email).
- ****Never subscribed****
  Person never consented to receiving messages. This is also the default value if a cell in a consent column is blank. You cannot send mobile (SMS, push, etc.) messages to people marked as never subscribed; however, you can send emails and these are considered active profiles.

Klaviyo will not apply consent if someone is marked as either unsubscribed or never subscribed.

### Optional: add consent timestamp

While optional, the timestamp is usually good to include if it’s available. To do so, check that:

- The timestamp is in an accepted date/time format.
- The column is labeled either:
  - WhatsApp Marketing Timestamp
  - WhatsApp Transactional Timestamp (if also importing transactional consent)

If you choose not to include the timestamp, you will need to check a box to confirm that all profiles are currently opted in.

Adding the consent timestamp is not recommended in certain cases. Mostly, this occurs if you try to re-upload consent for a profile and the opt-out date is more recent than the consent timestamp. In this case, consent won't be re-added to the profile.

## Import a list of phone numbers with WhatsApp consent

1. Navigate to ****Audience > Lists & segments****.
   ![Lists and segments tab](https://klaviyo.zendesk.com/hc/article_attachments/40852251492635)
2. Select the list you want to add your contacts to (e.g., WhatsApp Subscribers).
3. Open the ****Manage List**** dropdown in the upper right.
4. Choose ****Import contacts**** from the dropdown.

   - Note that you must be an Owner or Admin to see this option.![Import contacts from the Manage List dropdown](https://klaviyo.zendesk.com/hc/article_attachments/40852251496475)
5. Click ****Upload**** and select your CSV file of WhatsApp subscribers.
6. Click ****Next****.
7. Map each column from your CSV to an appropriate property in Klaviyo, then click ****Next****.
8. If your CSV includes columns indicating the type of consent or includes the consent timestamp, the import will add the consent accordingly.

   - Example: if you include an **WhatsApp Transactional Consent** column (but not one for marketing consent).
     - Profiles marked as “Subscribe” are imported with only WhatsApp transactional consent.
     - All other profiles (those marked as “Unsubscribed” or “Never subscribed”) are imported without consent.
9. If you have neither a consent timestamp or any column indicating consent (e.g., **WhatsApp Marketing Consent**), complete the following:
   1. Under **Did these contacts subscribe to messaging**, select ****Yes**** to add consent.
      ![Modal to confirm that contacts have explicitly consented to receiving email, SMS, or WhatsApp messages](https://klaviyo.zendesk.com/hc/article_attachments/40938964688667)
   2. Check the boxes for the types of consent to apply: WhatsApp, Email, SMS, or all.
   3. Choose the type of consent to apply. The option you pick depends on the consent types in your CSV:

      - If every profile is consented only to WhatsApp transactional, choose ****Only transactional messages****.
      - If every profile should be consented to both marketing and transactional, choose ****Marketing and transactional messages****.
      - To import only WhatsApp marketing, you must format your CSV so that it includes a column labeled **WhatsApp Marketing Consent**, then re-upload the CSV.
10. When ready to proceed, click ****Import****.

The import process can take up to a couple of hours to complete.

Once all the numbers are imported, Klaviyo will either create a new profile or associate the data to an existing profile. For instance, if you import a phone-number-only CSV, Klaviyo will look for profiles with the same phone number, update that profile's SMS consent status, and include any other profile properties attributed to that contact.

## Next steps

[Collect WhatsApp consent](https://help.klaviyo.com/hc/en-us/articles/40111819732635)

[About WhatsApp deliverability](https://help.klaviyo.com/hc/en-us/articles/40116474536347)

[How to create a WhatsApp template](https://help.klaviyo.com/hc/en-us/articles/40116644987675)
