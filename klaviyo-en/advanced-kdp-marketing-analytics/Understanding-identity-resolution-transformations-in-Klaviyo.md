---
id: 39729752384795
title: "Understanding identity resolution transformations in Klaviyo"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/39729752384795-Understanding-identity-resolution-transformations-in-Klaviyo"
section: "Transformation"
category: "Advanced KDP & Marketing Analytics"
category_slug: "advanced-kdp-marketing-analytics"
klaviyo_updated: "2026-05-11T12:54:43Z"
language: en
---

## You will learn

Learn about Klaviyo’s identity resolution functionality as part of Advanced KDP. This builds upon Klaviyo’s standard [identity resolution](https://help.klaviyo.com/hc/en-us/articles/12902308138011) functionality to enable more robust handling of duplicate profiles identified based on overlapping identifiers.

[Advanced KDP](https://help.klaviyo.com/hc/en-us/articles/17655007276059) is not included in Klaviyo’s standard marketing application, and a subscription is required to access the associated functionality. Head to our [billing guide](https://help.klaviyo.com/hc/en-us/articles/115000976672) to learn how to purchase this plan.

## Identity resolution transformations vs. identity resolution

Klaviyo natively offers [identity resolution](https://help.klaviyo.com/hc/en-us/articles/12902308138011) that consolidates customers’ interactions across multiple channels under a single record. This standard identity resolution in Klaviyo uses deterministic profile merging, resolving the identities of different profiles that share a common identifier—most often, a unique email address—based on the existing data in your account.

Meanwhile, the identity resolution transformations within Advanced KDP build upon this deterministic merging functionality by exploring profiles with different email addresses but other overlapping identifiers such as the same phone number.

## Identity resolution transformations

The first available identity resolution transformation offered as part of AKDP is aimed at reducing the number of duplicate profiles for a contact due to misspellings or typos in the email address. In the future, Klaviyo will offer additional merge logic, such as deduplicating profiles that exist due to the use of email aliases, as well as probabilistic merging based on shared first name, last name, address and more.

These transformations can be toggled on and off, but do not need to be further configured.

### Manage identity resolution transformations

****Profile merging is a permanent action.**** Any profiles merged from an identity resolution transformation cannot be un-merged.

To activate identity resolution transformations:

1. Navigate to the **Transformation** tab under ****Advanced KDP********>********Data management > Transformation****.
2. Select the ****Identity resolution**** tab.
3. Select ****Activate**** on the identity resolution transformation you'd like to enable.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/40442765151515)
4. We highly recommend you ****download a preview**** prior to activating any merge rule, to ensure you understand how profiles will be clustered and merged upon activation
5. Complete the confirmation prompt and select ****Activate****.

![](https://klaviyo.zendesk.com/hc/article_attachments/40442765166619)

Once activated, you’ll see an **Active** status for the transformation on the **Identity resolution** tab. By clicking into an active transformation, you can download a log of merges within the past 30 days using the ****Download merge log**** button or disable the transformation by selecting the ****Deactivate**** button.

![](https://klaviyo.zendesk.com/hc/article_attachments/40442773443995)

### Merge log

To view a record of the profile merges performed by the transformation, select the transformation and click the ****Download merge log**** button. This will export a CSV of merges in the last 30 days with the following information:

- ****Source profile ID****

  The [Klaviyo ID](https://help.klaviyo.com/hc/en-us/articles/115005247088#h_01H93XCYWWRTEWCFEMEADSYC0Q) of the source profile.
- ****Source email****
  The email address of the source profile.
- ****Source external ID****
  The external ID of the source profile.
- ****Source phone number****
  The phone number of the source profile.
- ****Destination profile ID****
  The [Klaviyo ID](https://help.klaviyo.com/hc/en-us/articles/115005247088#h_01H93XCYWWRTEWCFEMEADSYC0Q) of the destination profile.
- ****Destination email****
  The email address of the destination profile.
- ****Destination external ID****

  The external ID of the destination profile.
- ****Destination phone number****
  The phone number of the destination profile.
- ****Merged at****

The timestamp for the profile merge.

## Identity resolution transformation methods

Klaviyo supports the following transformation methods for identity resolution.

### ****Email typo merge****

Email typo merge identifies profiles that share the same phone number and appear to be duplicates due to a typo in an email address. For example, say 2 profiles have the same phone number but email addresses that are example@klaviyo.com and exampke@klaviyo.com. It is highly likely that these profiles belong to the same customer, but they made a typo when engaging with your brand in a specific context like signing up for a marketing list. The email typo merge transformation will automatically merge these profiles when activated.

****Merge logic****

For 2 profiles to be merged by the email typo deduplication transformation, they must meet the following conditions:

- The profiles must share the same phone number.
- The email addresses of the profiles differ only by 1 character.
- The difference between email addresses is either due to a typo in the domain name OR one profile is suppressed due to an invalid or bounced email (i.e. it is unreachable).

  If these conditions are all met, the merge will be performed in the following manner:
- If a profile has an invalid email address, the profile with the valid email address is retained (i.e., reachable and then no typo in domain name). Note that manually suppressed profiles without any other issues are considered reachable.
- If profile A and profile B are both unreachable, do not merge.
- If both profiles are reachable
  - If email A has a domain which is more standard (e.g., gmail vs. gnail), email A is retained.
  - If it is not possible to determine which email is more standard, do not merge.

Any email events associated with the invalid email address (e.g., **Received email**) will not be merged into the destination profile. However, other events (e.g., onsite events like **Viewed product**) will be merged into the destination profile.

### ****Email alias merge****

This feature is not yet released, but is coming soon.

Email alias merge identifies profiles that share the same phone number and appear to be duplicates due to a “+” used to create email aliases. Email aliases are alternative email addresses that forward emails to the primary email account's inbox.

For example, say 2 profiles have the same phone number but email addresses are example@klaviyo.com and example+marketing@klaviyo.com. Emails sent to [example+marketing@klaviyo.com](mailto:example+@klaviyo.com) will be forwarded to [example@klaviyo.com](mailto:example@klaviyo.com) or land in the same inbox and thus will always belong to the same customer.

With this transformation, the profile with an email address that is an alias (i.e., same email address with a “+” at the end) will be merged into the corresponding primary profile.