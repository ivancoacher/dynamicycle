<h1>How to send a campaign to people skipped by a list-triggered flow</h1>

## You will learn

Learn how to build a segment of people who should have received a list-triggered flow and send them a campaign. The main reason you would want to send a campaign to a group of people who were skipped by a [list-triggered flow](https://help.klaviyo.com/hc/en-us/articles/360003031652-Create-a-List-Triggered-Flow) (for example, a welcome series) is if you have an existing flow, but a number of people were skipped by a flow email for some reason. Perhaps you initially had the wrong filters on the flow, or Smart Sending was on by mistake.

This approach works best when you have to resend to a large group of people or if you need to resend an SMS message; if you instead only need to send to a few people, [check out our guide on resending emails in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/360033684431).

If you would like to email people who qualified for the flow's conditions **before** you created the flow, you should instead [add past profiles to the flow](https://help.klaviyo.com/hc/en-us/articles/115002779231).

## Build a segment of contacts skipped by a flow

1. Click ****Audience**** in the Klaviyo sidebar.
2. Choose ****Lists & segments****.
3. Click ****Create New > Create segment****.
4. Build a segment with conditions that exactly match the trigger and event filters of the flow. For example, if your flow is triggered by the list **Newsletter** and has no flow filters, use the segment definition ****If someone is in or not in a list > is in > Newsletter****.
5. Add an AND condition with these criteria:
   ****What someone has done > Received Email > zero times over all time > where Message equals [your flow message name]****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/34359431841819)
6. Click ****Create segment****.

## Save the flow message as a template (email only)

1. Click ****Flows**** in the Klaviyo sidebar.
2. Locate the list-triggered flow you'd like to resend and click to open it.
3. Locate the email you'd like to resend and click it.
4. In the right-hand panel, next to **Template**, select the three dots.
5. Click ****Save as template****.
6. Name and save your template.

## Create a campaign

1. Navigate to your ****Campaigns**** tab in Klaviyo.
2. Click ****Create campaign****.
3. Choose the type of campaign and click ****Continue****.
4. In the **Send to** field, choose the segment you created in the first section of this article.
5. Toggle off the ****Smart Sending**** setting.
6. Click ****Next****.
7. Set a subject line and preview text.
8. Select your saved email template, then click ****Next****.
9. Schedule the message to send immediately or at a later time.

## Additional resources

- [How to resend emails in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/360046797191)
- [How to bulk update flow statuses](https://help.klaviyo.com/hc/en-us/articles/360048376172)
