---
id: "43415280821403"
title: "Use Customer sentiment analysis to route and prioritize support in Helpdesk"
source_url: "https://help.klaviyo.com/hc/en-us/articles/43415280821403-Use-Customer-sentiment-analysis-to-route-and-prioritize-support-in-Helpdesk"
section: "Optimization & Analytics"
category: "Helpdesk"
category_slug: "helpdesk"
klaviyo_updated: "2026-04-17T07:02:17Z"
language: "en"
---
## You will learn

In this article, you will learn how to use customer sentiment to automatically spot angry customers, route urgent issues to the right agent, and surface promoters for follow-up campaigns. Acting on sentiment helps you reduce churn, shorten resolution time, and protect revenue.

## Before you begin

- Plan availability — Sentiment analysis is included in the ****Helpdesk**** paid tier; no extra setup or credits required.
- Supported channels — Email, SMS, and Web Chat tickets created in ****Helpdesk**** (including agent hand-offs) all receive a sentiment score.
- Permissions — Any ****Owner, Admin, Manager, or Agent**** can filter by sentiment or include it in a ****Routing Rule****.

## Overview

Klaviyo Helpdesk analyzes every new conversation with a large-language model (LLM) and assigns:

- A numeric score from ****0 (very negative) to 10 (very positive)****
- A categorical label: ****Urgent****, ****Promoter****, ****Negative****, ****Neutral****, or ****Positive****

  The score is stored as the ticket property ****Sentiment****. You can:
- Filter or sort ticket queues to answer upset customers first
- Build ****Routing Rules**** that auto-assign urgent tickets to senior reps

## Set it up

### 1. View sentiment inside a ticket

1. Go to ****Service > Helpdesk****.
2. Open any ticket.
3. In the right-hand ****Properties**** panel, review the sentiment value which is above the channel and tags section.

- Expected outcome — You see sentiment label (e.g., “Urgent”).

![Screenshot 2025-11-17 at 3.46.24 PM.png](https://klaviyo.zendesk.com/hc/article_attachments/43415280818203)

### 2. Create a custom view for angry customers

1. In Helpdesk, click ****All Tickets > Create view****.
2. Name your view “Upset customers”.
3. Under ****Filters****, choose ****Sentiment****.
4. Set ****Label**** to ****Urgent**** OR ****Negative****.
5. Click ****Save view****.

![Screenshot 2025-11-17 at 3.44.28 PM.png](https://klaviyo.zendesk.com/hc/article_attachments/43415280819867)

## Best practices

- Prioritize negative tickets within one business hour to prevent churn.
- Send promoters a follow-up message asking for a review or referral.
- Combine ****Sentiment**** with ****Recent order value**** in Routing Rules to handle high-value, unhappy customers first.
- Review weekly sentiment reports with your product team to address systemic issues.
- Keep response templates warm and empathetic; a positive tone can quickly flip neutral customers to promoters.

## FAQ

****Does sentiment work on historical tickets?****
No. Sentiment is applied only at ticket creation or agent hand-off after the feature launch.

****Can I edit a sentiment score?****
Not currently. Re-opening or splitting a ticket re-evaluates sentiment automatically.

****Is sentiment available in Flows or Segments?****
Yes, the sentiment value will be present on the “Ticket Created” and “Ticket Closed” metrics.

****Does sentiment affect marketing deliverability?****
No. Sentiment is isolated to Helpdesk and does not influence campaign sending logic.