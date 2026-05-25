---
id: "115000931551"
title: "How to run a re-engagement email campaign"
source_url: "https://help.klaviyo.com/hc/en-us/articles/115000931551-How-to-run-a-re-engagement-email-campaign"
section: "Build and send email campaigns"
category: "Campaigns"
category_slug: "campaigns"
klaviyo_updated: "2026-04-20T16:45:20Z"
language: "en"
---
## You will learn

Learn how to create and send a re-engagement email campaign.

Note that a re-engagement campaign differs from a [winback flow](https://help.klaviyo.com/hc/en-us/articles/115002775192) because it is a one-off email rather than a sequence of emails.

- A ****winback flow**** is triggered by the **Placed Order** event and sends when a certain amount of time has passed without an additional purchase.
- A ****re-engagement campaign**** is a single email that is sent infrequently to those who may not receive a winback flow. Once a year is a good rule of thumb.

You can run a similar re-engagement campaign for SMS subscribers. Simply swap the email-based segment criteria for SMS-based criteria, like "can receive SMS marketing" and "clicked SMS."

## Run a re-engagement campaign

To run a re-engagement campaign, take the following steps:

1. [Create these 2 segments](#h_01GG55VEJ04D6FEHTEZKD1XN68): one for unengaged purchasers and another for unengaged non-purchasers.
2. [Send a personalized email campaign](#h_01GG55VQ3V7PE3QY1HC8RDFMHK) to these subscribers featuring your latest releases and an easy way to update their preferences or unsubscribe.
3. [Suppress profiles that don't engage with your re-engagement campaign](#h_01GG55VZ7ERCSS9T946VT0K61D) to preserve strong deliverability.

### Split your unengaged subscribers into 2 segments

First, split your unengaged subscribers into segments: those who have made a purchase and those who have not made a purchase. This allows you to easily determine which group is more valuable once you send your campaign.

#### Unengaged subscribers - purchased

This segment should contain people who:

- Are subscribers and subscribed more than 60 days ago
- Haven't opened an email in the past 120 days
- Have had an email bounce less than 5 times over all time
- Have placed an order at least once over all time

![emailai2.jpg](https://klaviyo.zendesk.com/hc/article_attachments/37120567244571)

#### Unengaged subscribers - never purchased

Your second segment should have exactly the same conditions as the first, except they should have never placed an order:

- Are subscribers and subscribed more than 60 days ago
- Haven't opened an email in the past 120 days
- Have had an email bounce less than 5 times over all time
- Have placed an order 0 times over all time

![emailai4.jpg](https://klaviyo.zendesk.com/hc/article_attachments/37120567244699)

### Send the campaign

[Send a campaign](https://klaviyo.zendesk.com/hc/en-us/articles/115005054847) to these unengaged subscribers. Consider the following best practices for re-engagement campaigns:

- Make the email personal. Try using a [text-only email](https://klaviyo.zendesk.com/hc/en-us/articles/12415384810651) for a personal feel.
- Use the `{{ first_name }}` tag to customize the email for each recipient.
- Try a "friendly from" address like "Marissa from Klaviyo."
- Include a prominent unsubscribe and [manage preferences link](https://help.klaviyo.com/hc/en-us/articles/115005251848), in case subscribers want to update their settings rather than unsubscribe completely.
  ![Campaign content reengagement](https://klaviyo.zendesk.com/hc/article_attachments/28711672849435)
- Include content about any new products that have been released since they've become inactive.
- Consider offering a discount to entice them to buy.

Include prominent unsubscribe and [manage preferences](https://klaviyo.zendesk.com/hc/en-us/articles/115005251848) links, in case subscribers want to update their settings rather than unsubscribe completely. You may also want to consider [segmenting your newsletter by sending frequency](https://help.klaviyo.com/hc/en-us/articles/115000769631-Create-Email-Frequency-Segments) to avoid bombarding subscribers with emails and causing them to become inactive in the first place.

#### Use batch sending

When you're ready to send out your campaign(s), you may want to use the batch sending option. This distributes deliveries over a longer span of time, which can be a safer option if you're sending to a large group of unengaged people.

![Schedule reengagement campaign](https://klaviyo.zendesk.com/hc/article_attachments/28711672840091)

After you've sent the campaigns, monitor the results closely to see if this is something you would like to repeat annually. If you see an open rate above 10%, you can consider the campaign successful. It's possible that one segment will have a higher open rate than the other, in which case you may only want to email one segment for future re-engagement campaigns.

You may also want to [suppress](https://help.klaviyo.com/hc/en-us/articles/115005073867-Bulk-Delete-or-Suppress-Contacts-in-Klaviyo) anyone who does not respond to these emails. You can do this by creating and exporting a segment of those who received either email but did not open them (see below). Once you've exported the segment, navigate to ****Audience > Profiles > View suppressed profiles > Import**** to suppress these profiles from receiving future emails.

In the segment below, replace **Campaign Name 1** and **Campaign Name 2** with the names of your re-engagement campaigns.

![Reengagement segment for suppression](https://klaviyo.zendesk.com/hc/article_attachments/28711660687003)

## Additional resources

Check out flows for re-engaging and sunsetting subscribers:

- [Guide to creating a winback flow](https://help.klaviyo.com/hc/en-us/articles/115002775192)
- [Guide to creating a sunset flow](https://help.klaviyo.com/hc/en-us/articles/360017518492)