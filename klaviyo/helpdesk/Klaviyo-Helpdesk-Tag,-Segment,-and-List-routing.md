---
id: 40813502166171
title: "Klaviyo Helpdesk: Tag, Segment, and List routing"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/40813502166171-Klaviyo-Helpdesk-Tag-Segment-and-List-routing"
section: "Team Workflow & Productivity"
category: "Helpdesk"
category_slug: "helpdesk"
klaviyo_updated: "2026-04-17T06:59:06Z"
language: en
---

## You will learn

Use Smart Routing to automatically send each new ticket to the right team. By routing on ticket tags, and group (list or segment) membership, you will:

- Cut manual triage time and keep reassignment rates low
- Respond faster
- Give agents fewer touches per ticket and clearer ownership

## Before you begin

- ****Role required**** — Owners, Admins, and Managers can create or edit routing rules.
- ****Prerequisites****
  - At least one ****Team**** and one ****Agent**** set to **Active**
  - Topic tagging turned on (Settings > Helpdesk > Tagging) for tag-based rules
  - For segment rules, the segments or lists must already exist in ****Audience > Lists & segments****
- ****Time to complete**** — ≈ 10 minutes for a basic setup; < 5 minutes to add each new rule.

## Overview

Smart Inbox Routing replaces one-size-fits-all Round-Robin assignment with a rule-based engine: Rules are evaluated ****top-down, first match wins****. Tickets that match no rule fall back to your existing Round-Robin queue.

## Set it up

### 1. Open the Routing Builder

1. Go to ****Settings > Teams****
2. Click the tri-tip button and select “edit team”.
3. Click the ****Tags**** or ****Groups**** dropdowns
4. Select one or more items to assign to the team

****Expected outcome**** — Any new email or webchat ticket tagged **Shipping** is auto-assigned to the Logistics Team.

## FAQ

****Q: How many tags, lists, or segments can I assign to a team?****
A: Up to 20 per team. Contact Klaviyo Support to increase the limit.

****Q: What happens if two rules match?****
A: If two rules match, we will alternate teams to receive the ticket.

****Q: Does routing respect agent availability?****
A: Yes. If the target agent is set to **Away**, the ticket goes to the team queue; Round-Robin assigns the next available agent.

****Q: Do routing changes apply to open tickets?****
A: No. Rules apply only to tickets created after you save the change.