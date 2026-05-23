<h1>How to resend a campaign that exceeded account sending limits</h1>

## You will learn

Learn how to resend a campaign to recipients skipped due to exceeding your sending limits. This error appears as: "Your campaign CAMPAIGN\_NAME was automatically canceled for exceeding account sending limits."

## Why a campaign was canceled

Klaviyo automatically cancels campaigns when the testing pool exceeds an account's monthly sending limits. If a campaign is canceled for this reason, it does not automatically continue sending if you later upgrade your plan.

To view your account's current monthly sending limit:

1. Click your company name in the bottom-left corner of Klaviyo.
2. Click ****Billing****.
3. Locate the **Profiles + email** card to view your current email limits and monthly usage, or the **SMS** card to view your SMS limits and usage.
   ![Billing overview page, with your plan limits](https://klaviyo.zendesk.com/hc/article_attachments/28720900586523)

### How to avoid exceeding sending limits

To avoid messages being canceled when you reach your monthly sending limit, turn on the auto-upgrade billing option. With this option turned on, Klaviyo will move you up automatically to the next plan level if you exceed your current plan’s limits. Learn [how to turn on auto-upgrade billing](https://help.klaviyo.com/hc/en-us/articles/4405883690651).

## Resend your campaign

Once you have turned on auto-upgrade billing, continue sending the campaign.

First, locate the campaign ID of the original campaign:

1. Navigate to the ****Campaigns**** tab.
2. From the list view, click the 3-dot menu next to a campaign.
3. Click ****Copy campaign ID****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/34609738033947)
   ![Copy campaign ID mini.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28720895276059)

Then, resend the campaign.

- Navigate to the ****Lists & segments**** tab.
- Create a segment with the following definition:
  - **What someone has done > Received [email or SMS] > at least once over all time > where > Campaign ID equals [your campaign's ID]**
- Navigate to your ****Campaigns**** tab and find the canceled campaign.
- Click the 3-dot icon on the far right of the campaign, then click ****Clone****.
- Exclude the segment you created in step 2 from the cloned campaign.
- Send the campaign.

By following the steps above, no one who received your message before you ran out of funds will receive the second, re-sent campaign.

## Additional resources

- [Understand how Klaviyo billing works](https://help.klaviyo.com/hc/en-us/articles/115000976672-Understand-how-Klaviyo-billing-works-)
- [Best practices for A/B testing](https://help.klaviyo.com/hc/en-us/articles/360045012632-Best-Practices-for-A-B-Testing)
