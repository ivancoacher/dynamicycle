<h1>Klaviyo Helpdesk: Round Robin Assignment</h1>

## You will learn

Enable round-robin ticket assignment to automatically distribute new conversations to available agents. This setup eliminates manual triage, shortens time to first response, and keeps workloads fair—especially during busy seasons.

## Before you begin

- Prerequisites
  - Helpdesk is installed and connected to at least one support channel.
  - Office hours are configured (Inbox > Settings > Office hours).
  - Each agent has a Klaviyo user seat with the ****Agent**** role or higher.
- Feature availability
  - Works for email, chat, SMS, and social channels routed through Helpdesk.
- Permissions
  - ****Owners, Admins, and Managers**** can turn round robin on or off.

## Overview

Round robin automatically assigns the next inbound ticket to the next ****active**** agent in a rotating order. Agents mark themselves ****Online**** or ****Offline**** from the Inbox header. Tickets are only auto-assigned during scheduled office hours for webchat, anything that arrives after hours stays unassigned until the next business day.

For non webchat channels, round robin will assign to the user whenever they are online and a ticket comes in.

Use round robin when you want a simple, fair split of workload. For skill-based or rules-based routing, see ****“Team Based routing”****.

## Set it up

1. Go to ****Helpdesk > Settings > Inbound Messages****
2. Set ****Round robin assignment**** to ****On****, and press save..
3. (If webchat is enabled) Confirm office hours are correct under ****Helpdesk > Settings > Webchat****
4. Ask each agent to set their status when they are ready to begin helping customers

## Best practices

- Encourage agents to turn ****Offline**** during breaks to avoid silent backlogs.
- For single-agent teams, still use round robin so Inbox auto-assigns and tracks ownership.

## Measure success

View metrics in ****Helpdesk > Reporting:****

- ****Time to first reply (TTFR)**** — should drop after enabling.
- ****Tickets assigned per agent**** — should be nearly equal across active agents.

  If a metric is low:
- Check that enough agents are marked ****Online**** during peak hours.
- Shorten response macros for common questions.
- Revisit office hours; mis-aligned hours create overnight backlogs.
- Audit the ****Unassigned**** queue for spikes that point to channel surges.

## FAQ

****Does round robin re-balance existing tickets if an agent goes offline?****
No. Only new tickets are distributed.However, you can bulk assign tickets to a team, which will round robin assign those tickets to all members of the team who are online.

****Can I set different round robin pools for chat vs. email?****
Not yet—round robin currently uses one global pool of active agents.

****What happens if only one agent is online?****
All tickets are assigned to that agent until another agent toggles ****Online****.

****Are email notifications sent when a ticket is assigned?****
Inbox shows in-app toasts only. Email notifications will be added in a later version.

****Will agents automatically toggle online at the start of office hours?****
No. Agents must intentionally toggle ****Online**** each day.
