---
id: 115005078887
title: "How to combine 2 or more lists in Klaviyo"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005078887-How-to-combine-2-or-more-lists-in-Klaviyo"
section: "Build and use lists"
category: "Audience"
category_slug: "analytics-audience"
klaviyo_updated: "2026-04-21T13:54:18Z"
language: en
---

## You will learn

Learn how to merge 2 or more lists in Klaviyo. We recommend maintaining 1 list per channel to streamline list cleaning, stay organized, and better understand your audience. Merging lists allows you to clean up your account and remove unnecessary lists without sacrificing data.

## Key terms

- ****Source list****
  The list of contacts that will be merged into the destination list.
- ****Destination list****
  The primary list that contacts will be merged into. Use this list as your source of truth for subscribed contacts moving forward.

## Before you begin

Before merging lists, disconnect your source list(s) from any data sources or key actions:

- Change the “submit list” for any sign-up forms.
- Edit any flow filters or segment conditions that reference the source list.
- Update any integrations that sync contacts to the source list.

## Merge 2 or more lists

1. Navigate to ****Audience > Lists & segments****.
2. Select your intended source list (the list you want to move contacts away from).
3. Open the ****Manage List**** dropdown.
4. Select ****Merge lists****.
   ![Merge lists option in the Manage List dropdown](https://klaviyo.zendesk.com/hc/article_attachments/34257952032027)
5. If desired, select additional source lists (max of 5 lists).
6. Choose a destination list. All contacts from your source list(s) will be added to the destination list.
7. Choose whether to keep or delete your source list(s).
   - If you keep your source lists, contacts added to them after the merge will ****not**** be added to the destination list.
   - If you choose to delete the source lists, no profile data will be lost.
     ![Merge lists modal, where you select up to 5 source lists and the intended destination list](https://klaviyo.zendesk.com/hc/article_attachments/34257952036891)
8. Click ****Merge****.

The merging process may take several minutes.

## Frequently asked questions

### Why can’t I select my list?

Only lists, not segments, can be merged. If you don’t see a list name in the source or destination list dropdown, that means it is a segment.

To convert a segment into a list, click ****Manage Segment > Convert to list****. This action is permanent, and the list will no longer dynamically update as contacts meet the former segment’s criteria. Note that converting a segment to a list will not update any members' consent or send double opt-in messages.

### What happens if a profile is on more than 1 of the lists being merged?

During the merge, Klaviyo de-duplicates your lists and ensures each contact only appears once. All profile and event data is maintained during the merge.

Once the merge is complete, every contact from both the source and destination lists will appear in the destination list exactly once.

### What if I want to merge more than 5 lists?

The list merge tool has a maximum of 5 source lists. To merge more lists, complete the first merge with 5 lists, then repeat the merge process with any additional lists.

### Will merging lists trigger my welcome flow?

No, merging lists will not trigger the welcome flow (or any list-triggered flows) for any profiles that get added to that list. Use the ****Add past profiles**** button to [send the flow to these contacts](https://klaviyo.zendesk.com/hc/en-us/articles/360049924272).

### How can I undo a merge?

Merging lists is permanent. Once you take this action, merged contacts cannot be removed from the destination list. If you choose to delete your source list(s), they cannot be recovered.

### What happens if a list is deleted while a campaign is scheduled to send to that list?

If you schedule a campaign to send to a list, and that list is deleted, then the deleted list will be excluded from that campaign send. In that way, it functions no differently than a normal list delete action.

For example, a campaign is scheduled to send to List A, List B, and Segment C. Before the scheduled send time, List A is deleted in the merge process. At send time, the campaign will only send to profiles in List B and Segment C. If a list is deleted while the campaign sending is in progress, it may be partially sent to people on that list.

## Additional resources

- [Understanding the benefits of having a main list for each marketing channel](https://help.klaviyo.com/hc/en-us/articles/360043947571)
- [Getting started with segments](https://klaviyo.zendesk.com/hc/en-us/articles/115005237908)
- [Email list hygiene: Best practices for a clean subscriber list](https://www.klaviyo.com/blog/maintain-email-list-hygiene)