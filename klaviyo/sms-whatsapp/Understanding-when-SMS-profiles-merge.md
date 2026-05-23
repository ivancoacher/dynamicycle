---
id: 360035588012
title: "Understanding when SMS profiles merge"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360035588012-Understanding-when-SMS-profiles-merge"
section: "Manage your SMS profiles"
category: "SMS"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-21T13:56:51Z"
language: en
---

## You will learn

Learn how SMS affect profiles in Klaviyo, including how email and phone number contacts merge into one cohesive profile and what unique scenarios are cause for exceptions.

## How SMS profiles merge

In general, each customer will have one, unique profile in Klaviyo. Both email and SMS information will be found here so you can effectively streamline communication and store all data in one place.

### How profiles merge

If you use Klaviyo to send emails, then you likely already have a number of profiles in your account. When a subscriber opts in to receive SMS in addition to email, their profile will update automatically and their consent status will appear on their profile.

This means that, if you have someone's email address and they later provide their phone number as well, a duplicate profile will not be created (unless one of the scenarios outlined [below](#h_01EEBT4JDYSMTW6S45D9S4W8AT) occurs). Instead, one profile will house all of their contact information and provide a record that they consent to receive emails and text messages from your business.![Email and SMS consent associated with a single profile](https://klaviyo.zendesk.com/hc/article_attachments/28717992223771)

Profiles will also merge when Klaviyo learns that an email address and phone number are connected to the same profile. For instance, if a phone-only profile adds an email that matches an existing email-only profile, the two will merge.

If you use Klaviyo solely for SMS, your customer profiles will be uniquely identified by their phone numbers until you start collecting email addresses.

### Instances when profiles don't merge

Some scenarios in which a customer's contact information will not merge into one profile, or will merge in a way you may not expect, are listed below:

- If an email subscriber opts in to SMS with a phone number that does not already exist in Klaviyo in an [accepted format](https://help.klaviyo.com/hc/en-us/articles/360046055671-Accepted-Phone-Number-Formats-for-SMS-in-Klaviyo), but no email is attached to that action, a new profile is created.
  - Then, if they check out using their email (which already exists as a separate profile) and consents to SMS with that same phone number, the two profiles will not merge automatically.
- If a customer with SMS consent makes a purchase and inputs a different phone number at checkout, that new number will override the information from the previous number on file (if there was one).
  - If you don’t have consent for the new number, but had it for the previous one, it will wipe consent from that profile and replace the contact information with the newly established number. You will then need to regain consent with their new phone number.
- If a profile adds their phone number by subscribing via a keyword or a click-to-text banner in an email or targeted form.
  - Using an SMS subscribe link from a campaign will create a new profile that won't automatically merge with the email profile.

Keep these one-off situations in mind as you collect SMS information that will merge with email in a profile.

## Additional resources

- [Understand profiles in Klaviyo](https://klaviyo.zendesk.com/hc/en-us/articles/115005247088)
- [Understand how Klaviyo billing works](https://klaviyo.zendesk.com/hc/en-us/articles/115000976672)
- [How to clean SMS lists](https://help.klaviyo.com/hc/en-us/articles/6155416998555)