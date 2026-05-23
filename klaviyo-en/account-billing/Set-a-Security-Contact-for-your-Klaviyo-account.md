---
id: 50590445021083
title: "Set a Security Contact for your Klaviyo account"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/50590445021083-Set-a-Security-Contact-for-your-Klaviyo-account"
section: "Security"
category: "Account & billing"
category_slug: "account-billing"
klaviyo_updated: "2026-05-19T20:12:56Z"
language: en
---

## Overview

The Security Contact lets your company designate a specific account Admin as the primary point of contact for security-related communications from Klaviyo - such as breach alerts, suspicious activity warnings, and compliance requests.

By default, every Klaviyo account automatically has the account Owner set as the Security Contact. This means every account already has a Security Contact configured, even if you've never set one up yourself. If you'd like a different Admin to receive security communications, you can update this at any time.

## Who can be set as a Security Contact

A user can be designated as Security Contact if they meet all of the following criteria:

- Their role is Admin or Owner, or has Account Settings edit permission
- Their account is active
- They have logged in within the last 365 days
- They are not in a blocked staff role

There is no billing tier restriction - this feature is available on free and paid accounts.

## How to set a Security Contact

1. Navigate to ****Account > Settings > Security****.
2. Locate the ****Security Contact**** field.
3. Search for and select the Admin or Owner you want to designate.
4. Save your changes.

The Security Contact field is visible and editable by Admins and Owners. Users with lower roles will not see or be able to edit this field.

## What happens when the Security Contact changes

When a Security Contact is updated, both the previous contact and the newly assigned contact receive an email notification informing them of the change.

## Default behavior and automatic validation

Klaviyo automatically assigns the account Owner as the Security Contact on all new and existing accounts. If you have not manually configured a Security Contact, your Owner is already set as the default.

Klaviyo also runs periodic background checks to validate the assigned Security Contact. If the contact becomes invalid (for example, if their account is deactivated) Klaviyo will automatically revert the Security Contact to the account Owner.

## What to expect in the future

The Security Contact feature is new to the Klaviyo Platform. Currently, no specific notifications are sent to this contact. In the future, Klaviyo will begin routing specific security notifications to the Security Contact, including:

- Warnings of suspicious account activity
- Alerts for abnormal login attempts
- Prompts to take security actions, such as rotating exposed API keys