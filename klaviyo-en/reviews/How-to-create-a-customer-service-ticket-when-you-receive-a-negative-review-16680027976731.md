---
id: "16680027976731"
title: "How to create a customer service ticket when you receive a negative review"
source_url: "https://help.klaviyo.com/hc/en-us/articles/16680027976731-How-to-create-a-customer-service-ticket-when-you-receive-a-negative-review"
section: "Build and use reviews"
category: "Reviews"
category_slug: "reviews"
klaviyo_updated: "2026-04-20T16:48:53Z"
language: "en"
---
## You will learn

Learn how to create a flow in Klaviyo to create a customer service ticket whenever someone submits a negative review. Notifying your customer service team allows them to proactively reach out and amend any negative experiences your customers may have.

## Create a negative review flow

First, create a flow:

1. Click ****Flows**** in the left-side navigation in Klaviyo.
2. Click ****Create flow****.
3. Click ****Create From Scratch****.
   ![Create a flow from scratch](https://klaviyo.zendesk.com/hc/article_attachments/28715972707483)
4. Name your flow something descriptive and click ****Create Flow****.
5. Under **What will trigger this flow?**, choose ****Metric****.
6. From the **What action will trigger this flow?** menu, choose ****Submitted review****.
7. Click ****Trigger Filters > Add a Trigger Filter****.
8. Set the following trigger filter:
   ****review\_rating > is at most > 3****

   This will identify customers who submitted a 1-, 2-, or 3-star review. If desired, you can use a different number.

![Review rating trigger filter](https://klaviyo.zendesk.com/hc/article_attachments/28715966169499)

## Add an email notification action

Next, add an action to notify your customer service team about the negative review.

1. Add a ****Notification**** action to the flow directly under the trigger.
   ![A Notification action](https://klaviyo.zendesk.com/hc/article_attachments/28715972713627)
2. In the notification’s **Send to** field, add your customer support email address.
3. Set a subject like “{{ event.review\_author|default:'Someone' }} submitted a {{ event.review\_rating }}-star review”.
   ![Notification action subject line](https://klaviyo.zendesk.com/hc/article_attachments/28715972705051)
4. Add a body message that includes review details, like:
   Rating: {{ event.review\_rating }}
   Review body: {{ event.review\_content }}
   Customer name: {{ event.review\_author }}
   Customer email: {{ event.review\_email }}
5. Click ****Save****.

## Set the flow live

Once you’ve customized the notification action, click ****Review and set live**** to set the flow live. Any future negative reviews will be automatically sent to your customer service team, who can then proactively contact the customer.

If your customer service team is able to resolve a complaint, they can direct the reviewer to return to the original review request email within 30 days of submission and edit their review, if desired.