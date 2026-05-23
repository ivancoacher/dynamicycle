---
id: 43416386141467
title: "Klaviyo Helpdesk: Guide to Pinned Properties"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/43416386141467-Klaviyo-Helpdesk-Guide-to-Pinned-Properties"
section: "Team Workflow & Productivity"
category: "Helpdesk"
category_slug: "helpdesk"
klaviyo_updated: "2026-04-17T07:01:56Z"
language: en
---

## You will learn

With pinned profile properties, you can surface up to five of your most important customer attributes (e.g., Loyalty points, VIP tier, Birthday) directly inside the Helpdesk composer. Setting this up takes less than two minutes and helps your team:

- cut first-response time by removing the need to open the full profile
- reduce average handle time by keeping key context in view
- deliver faster, more accurate answers that boost customer satisfaction

## Before you begin

- Helpdesk must be enabled in your Klaviyo account.
- ****Roles:**** Owners, Admins, and Managers can edit Helpdesk settings.
- Choose only plain-text, number, or date properties. Nested or JSON properties are not supported.
- Time to complete: ≈ 2 minutes.

## Overview

Pinned profile properties are a Helpdesk setting that tells Klaviyo which up-to-five customer properties should always show in the ticket sidebar. This quick snapshot eliminates context switching and keeps agents focused on the conversation.

## Set it up

1. In Klaviyo, go to ****Helpdesk > Settings > Pinned properties****.
2. Click ****Add properties****. A search-as-you-type dropdown opens.
3. Start typing the name of a property (e.g., “Loyalty points”).

   - Select the property from the list.
   - The selected property appears as a chip under the search bar.
4. Repeat until you have added up to 5 properties.

   - ****Note:**** You cannot add duplicates.
   - ****Warning:**** Selecting a JSON property triggers the toast “JSON property types not supported yet.” Choose a plain property instead.
5. Click ****Save changes****

![](https://klaviyo.zendesk.com/hc/article_attachments/43416370396187)

## Review Properties

Once saved, go into any ticket and confirm the properties are now appearing on the right sidebar.

![](https://klaviyo.zendesk.com/hc/article_attachments/43416386136091)

## Best practices

- Choose properties that agents reference on most tickets (e.g., loyalty status, last order date, coupon code).

## Measure success

1. Go to ****Helpdesk > Reporting > Agent performance****.
2. Compare the following metrics before and after enabling pinned properties:

   - First response time
   - Average handle time
   - Ticket resolution time
3. If numbers don’t improve:

- Confirm agents know the panel exists and collapse/expand behavior.
- Replace rarely populated properties.
- Audit other workflow changes (e.g., new SLAs) that might offset gains.

## Troubleshooting

| ****Symptom**** | ****Likely cause**** | ****Fix**** |
| --- | --- | --- |
| Key properties panel is missing in composer | No properties have been saved | Navigate to ****Helpdesk > Settings > Pinned properties**** and add at least one field |
| A property shows “—” | Profile doesn’t have a value | Verify the customer’s profile or choose a property with broader coverage |
| Toast “JSON property types not supported yet” appears | Selected property is a nested/JSON field | Pin a plain-text, number, or date property instead |
| ****Save changes**** button is disabled | You already selected five properties | Remove a chip to free a slot |

## FAQ

****Can I pin more than five properties?****
Not at this time. The limit keeps the composer uncluttered and ensures optimal performance.

****Can different agents have different pinned properties?****
No. Pinned properties are global for the Helpdesk workspace so every agent sees the same context.

****Do pinned properties update on existing tickets?****
Yes. When you change the list in Settings, the composer refreshes for all tickets—open and new.