---
id: "20016490907163"
title: "Changes to flow filtering on consent reference"
source_url: "https://help.klaviyo.com/hc/en-us/articles/20016490907163-Changes-to-flow-filtering-on-consent-reference"
section: "Understand flows"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-04-21T13:56:45Z"
language: "en"
---
## You will learn

Learn about the updates to Klaviyo’s profile filtering in flows that enables you to filter on consent records.

## Email consent condition changes

With Klaviyo’s updates to profile filtering in flows, the following email consent conditions are impacted:

****To identify profiles that are not suppressed****

Old filter condition:

- If someone is or is not suppressed for email >
  Person is not suppressed
  ![Old profile filter for 'person is not suppressed'](https://klaviyo.zendesk.com/hc/article_attachments/28722611148699)

New filtering condition:

- If someone can or cannot receive marketing >
  Person can receive email marketing
  ![New profile filter for 'person can receive email marketing'](https://klaviyo.zendesk.com/hc/article_attachments/28722611161371)

****To identify profiles that are suppressed****

Old filter condition:

- If someone is or is not suppressed for email >
  Person is suppressed
  ![Old filter for 'person is suppressed'](https://klaviyo.zendesk.com/hc/article_attachments/28722599205275)

New filter condition:

- If someone can or cannot receive marketing >
  Person cannot receive email marketing
  ![New filter for 'person cannot receive email marketing'](https://klaviyo.zendesk.com/hc/article_attachments/28722599228827)

****To identify profiles that are subscribed and not suppressed****

Old condition:

- If someone is or is not suppressed for email >
  Person is not suppressed

AND

- If someone is or is not in a list >
  Person is in [subscriber list name]
  ![Old filters for 'person is not suppressed' AND 'pers is in list'](https://klaviyo.zendesk.com/hc/article_attachments/28722611151387)

New condition:

- If someone can or cannot receive marketing >
  Person can receive email marketing >
  Because person subscribed to email marketing
  ![New filter for 'person can receive email marketing' with a filter for 'person subscribed'](https://klaviyo.zendesk.com/hc/article_attachments/28722611164315)

## SMS consent condition changes

With Klaviyo’s updates to profile filters, the following SMS consent conditions are impacted:

****To identify profiles that are consented to SMS****

Old condition:

- If someone is or is not consented to receive SMS >
  Person is consented to receive SMS
  ![Old filter for 'person is consented to receive SMS'](https://klaviyo.zendesk.com/hc/article_attachments/28722611153435)

New condition:

- If someone can or cannot receive marketing >
  Person can receive SMS marketing
  ![New filter for 'person can receive SMS marketing'](https://klaviyo.zendesk.com/hc/article_attachments/28722611166235)

****To identify profiles that are not consented to SMS****

Old condition:

- If someone is or is not consented to receive SMS >
  Person is not consented to receive SMS
  ![Old filter for 'person is not consented to receive SMS'](https://klaviyo.zendesk.com/hc/article_attachments/28722611155867)

New condition:

- If someone can or cannot receive marketing >
  Person cannot receive SMS marketing
  ![New filter for 'person cannot receive SMS marketing'](https://klaviyo.zendesk.com/hc/article_attachments/28722599234075)

## Mobile push consent condition changes

With Klaviyo’s updates to profile filters, the following push notification consent conditions are impacted:

****To identify profiles that have a mobile push token****

Old condition:

- If someone has a push token >
  Person has push token
  ![Old filter for 'person has push token'](https://klaviyo.zendesk.com/hc/article_attachments/28722599220251)

New condition:

- If someone can or cannot receive marketing >
  Person can receive mobile push marketing
  ![New filter for 'person can receive mobile push marketing'](https://klaviyo.zendesk.com/hc/article_attachments/28722611170203)

****To identify profiles that do not have a mobile push token****

Old condition:

- If someone has a push token >
  Person does not have push token
  ![Old filter for 'person does not have push token'](https://klaviyo.zendesk.com/hc/article_attachments/28722611160091)

New condition:

- If someone can or cannot receive marketing >
  Person cannot receive mobile push marketing
  ![New filter for 'person cannot receive mobile push marketing'](https://klaviyo.zendesk.com/hc/article_attachments/28722599243419)

## New functionality

With the updates to profile filtering, you can also filter on how a profile became subscribed or unsubscribed, and their reason for being suppressed (email only).

****To identify profiles that have subscribed through a specific method (email)****

- If someone can or cannot receive marketing >
  Person can receive email marketing >
  Because person subscribed to email marketing >
  And subscribe method is Klaviyo form [form name]
  ![Filter for 'person cannot receive email marketing' with subscribe method](https://klaviyo.zendesk.com/hc/article_attachments/28722599247899)

With this condition, you are also able to filter on:

- Subscribe method
- Method detail
- Custom method detail
- Subscribe date
- If profile is double opted in

****To identify profiles that have subscribed through a specific method (SMS)****

- If someone can or cannot receive marketing >
  Person can receive SMS marketing >
  and subscribe method is Klaviyo form
  ![Filter for 'persn can receive SMS marketing' and subscribe method](https://klaviyo.zendesk.com/hc/article_attachments/28722611186843)

****To identify profiles that have a status of never subscribed (email)****

- If someone can or cannot receive marketing >
  Person can receive email marketing >
  Because person never subscribed to email marketing
  ![Filter for 'person can receive email marketing' and never subscribed](https://klaviyo.zendesk.com/hc/article_attachments/28722611208731)

****To identify profiles that have have a status of never subscribed (SMS)****

- If someone can or cannot receive marketing >
  Person cannot receive SMS marketing >
  Because person never subscribed to SMS marketing
  ![Filter for 'person cannot receive SMS marketing' and never subscribed](https://klaviyo.zendesk.com/hc/article_attachments/28722599252635)

****To identify profiles that unsubscribed due to a specific reason****

- If someone can or cannot receive marketing >
  Person cannot receive email marketing >
  Because person unsubscribed to email marketing >
  And unsubscribe method is unsubscribe page
  ![Filter for 'person cannot receive email marketing' and unsubscribe method](https://klaviyo.zendesk.com/hc/article_attachments/28722599261083)

You are also able to filter on:

- Unsubscribe method
- Method detail
- Unsubscribe date

****To identify profiles that are suppressed due to a specific reason****

- If someone can or cannot receive email marketing >
  Person cannot receive email marketing >
  Because person is manually suppressed from email marketing
  ![filter for 'person cannot receive email marketing' because person is manually suppressed](https://klaviyo.zendesk.com/hc/article_attachments/28722611198363)

You able to filter for suppression due to:

- Unsubscribed
- Manual suppression
- Invalid email
- Hard bounced email

## Additional resources

[Understand consent in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/360037101072)