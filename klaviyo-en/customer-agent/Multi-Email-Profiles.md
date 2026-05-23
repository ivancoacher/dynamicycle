---
id: 48920080799899
title: "Multi Email Profiles"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/48920080799899-Multi-Email-Profiles"
section: "Training"
category: "Customer Agent"
category_slug: "customer-agent"
klaviyo_updated: "2026-04-21T13:56:41Z"
language: en
---

Customers often interact using different email addresses — like a personal or work email address, or even one specific to ecommerce checkout. Traditionally, this creates duplicate profiles, broken journeys, and inconsistent consent data.

Multi-Email Profiles solve this by maintaining up to 5 email addresses per profile, unified under a single identity.

## How Klaviyo Chooses the Primary Email

The primary email is determined through three logical steps:

1. ****Check consent**** — Klaviyo selects the email that can actively receive marketing: the one that's opted in or subscribed.
2. ****Check activity**** — If multiple emails have consent, the one tied to the most recent Placed Order or non-bot Email Click becomes the primary.
3. ****Fallback**** — If there's no clear consent or engagement signal, Klaviyo uses the most recently added email.

## When Klaviyo Re-Evaluates the Primary Email

****Real-time triggers**** (within ~1 hour):

- A new email is added to the profile
- The current primary email unsubscribes, bounces, or is removed

****Nightly validation:**** Every 24 hours, Klaviyo re-checks all emails on a profile to confirm the correct primary is still active.

## When and How Profiles Merge

Klaviyo merges profiles when they share an identifier, such as External ID, indicating they represent the same person.

When a merge occurs, Klaviyo designates a ****destination profile****, which retains its primary email and identities. The other profiles contribute their:

- Additional emails
- Profile properties
- Event history and activity
- Consent and suppression records (each email retains its own consent and suppression status)

Flows, segments, and campaigns send to the ****primary email**** on the destination profile by default.

## Special Cases

Certain scenarios cause a message to be sent to a profile email other than the primary, or not sent at all.

****Event-triggered flows**** send to the email associated with the triggering event. For example, an Abandoned Cart flow sends to the checkout email used in that session. If that email is unsubscribed or unreachable, Klaviyo skips the send — it does not fall back to the primary email.

****List-triggered flows**** send to the email captured at list signup. If no list email is stored, Klaviyo falls back to the primary email. When profiles merge, list membership and email context are preserved.