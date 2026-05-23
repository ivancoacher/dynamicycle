<h1>Multi Email Profiles</h1>

# ****What is Multi-Email Profiles?****

Multi-Email Profiles (MEP) is a Klaviyo feature that lets you store and manage up to 5 email addresses on a single customer profile. Instead of your customers appearing as multiple separate profiles every time they use a different email, Klaviyo keeps everything in one place so you always have a complete, accurate picture of who they are.

This means better personalization, cleaner analytics, and more consistent experiences across every channel you use.

# ****Why does this matter?****

Your customers don't stick to one email address. They might sign up with their personal Gmail, check out with a work address, and click a link from a third address they use for shopping. Without MEP, each of those interactions creates a separate profile in Klaviyo, leading to:

- Duplicate profiles cluttering your account
- Broken automation flows and missed triggers
- Inconsistent consent and suppression records
- Fragmented data that makes personalization harder
- Inflated contact counts and skewed analytics

MEP solves this by unifying all of a customer's email addresses under one profile.

# ****How profiles get merged****

## ****What triggers a merge?****

Klaviyo merges profiles when it can confirm they belong to the same person. This happens when two profiles share an ****External ID**** a unique identifier your store or integration provides to Klaviyo, such as a customer ID from your ecommerce platform.

There are three ways to add email addresses to a profile:

- ****Automatic merge:**** When two profiles share an External ID, Klaviyo automatically merges them and combines their email addresses.
- ****Klaviyo UI:**** You can manually add secondary email addresses directly on the profile page in Klaviyo.
- ****PATCH API:**** Developers can use the PATCH API to add emails programmatically using Klaviyo's identity resolution rules.

## ****What carries over when profiles merge?****

When profiles merge, Klaviyo designates one as the ****destination profile**** — the one that keeps its Primary Email and identity. Everything from the other profiles is folded in:

- Additional email addresses (up to the 5-email cap)
- Profile properties
- Event history and activity
- Consent and suppression records

****Important:**** Each email address keeps its own consent and suppression status after a merge. Subscribing or unsubscribing one email does not affect the others.

## ****What happens when a profile already has 5 emails?****

Each profile can hold a maximum of 5 email addresses. If a 6th is added:

- The new address is added.
- The least recently updated address on the profile is automatically removed to stay within the limit.

# ****How Klaviyo picks the Primary Email****

Every profile has one ****Primary Email**** — the address Klaviyo uses by default when sending campaigns and flows. Here's how Klaviyo determines which address gets that role:

****Step 1 — Consent****

Klaviyo picks the email that's opted in or subscribed to marketing. An address that can actively and legally receive mail always comes first.

****Step 2 — Engagement****

If multiple emails have consent, the one tied to the most recent Placed Order or non-bot email click becomes the Primary. The most engaged address is the best choice for reaching your customer.

****Step 3 — Fallback****

If there's no clear consent or engagement signal, Klaviyo uses the most recently added email as a tiebreaker.

## ****When does the Primary Email update?****

The Primary Email isn't fixed — Klaviyo re-evaluates it automatically.

****In real time (within about an hour):****

- A new email address is added to the profile
- The current Primary Email unsubscribes, bounces, or is removed

****Every night:****

- Klaviyo runs a nightly check across all profiles to confirm the right Primary Email is still active and valid

# ****Which email address gets the message?****

| ****Send type**** | ****Which email gets the message**** |
| --- | --- |
| ****Campaigns and segments**** | When you send a campaign to a segment, every profile receives it at their Primary Email. Secondary emails are not included in campaign sends. |
| ****Event-triggered flows**** | For flows triggered by events (like an Abandoned Cart flow), Klaviyo sends to the email address associated with the triggering event — not necessarily the Primary Email. |

****Example: Abandoned Cart****

Your customer browses using their work email and leaves items in their cart. The Abandoned Cart event is linked to their work email, so Klaviyo sends the flow to that address — even if their Primary Email is different.

If that event email is unsubscribed or unreachable, Klaviyo skips the flow entirely. It will not fall back to the Primary Email or any other address on the profile.

# ****Frequently asked questions****

****How does MEP get created?****

Getting started with MEP is straightforward. There are three ways profiles get merged or have emails added:

- ****Automatic merge via External ID:**** When Klaviyo detects two profiles sharing the same External ID (typically a customer ID from your store), it automatically merges them into a single MEP. No manual step needed.
- ****Manually through the Klaviyo UI:**** You can add a secondary email directly on any profile page in Klaviyo.
- ****Via the PATCH API:**** Developers can use the PATCH API alongside Klaviyo's existing identity resolution rules to add emails programmatically.

Merges are fully automatic — neither you nor your customer needs to confirm or approve anything.

****Does having multiple emails on a profile affect my bill?****

Billing is based on profiles, not individual email addresses. A profile with 3 email addresses still counts as 1 contact toward your plan.

In fact, MEP can help reduce your billable contact count. If you previously had duplicate profiles for the same customer using different email addresses, merging them into one MEP profile removes those duplicates — meaning fewer contacts overall.

****What happens if the Primary Email is unsubscribed or unreachable at send time?****

****For campaigns:**** Klaviyo sends only to the Primary Email. If it's unsubscribed or unreachable at send time, that profile is skipped entirely. Klaviyo will not fall back to a secondary email.

****For event-triggered flows:**** Klaviyo sends to the email tied to the triggering event, which may differ from the Primary Email. If that event email is unsubscribed or unreachable, the flow is skipped. There is no fallback to the Primary Email or any other address on the profile.

****What happens if I try to add more than 5 emails to a Profile?****

If a CSV contains multiple rows for the same profile, each with a different email address, behavior depends on the ingestion method.

#### List Import UI / SFTP

The transform layer deduplicates rows before processing, so only the ****last row**** for a profile is retained (within the same chunk). Earlier email values are discarded.

To preserve multiple emails:

- ****SFTP:**** Use `append_emails` columns
- ****List Import UI:**** Map multiple email columns

Both approaches generate a `patch_identifiers` payload that appends all emails correctly.

#### Bulk API

All rows are sent to the profiles service, where `_merge_payloads()` combines updates for the same profile.

`patch_identifiers` uses a dedicated merge path (`_merge_patch_identifiers()`) that accumulates append/unappend operations instead of overwriting them, so all email addresses are preserved across rows.

#### UI Behavior

When manually adding emails in the UI, a banner will prompt you to delete an existing email before adding a new one.
