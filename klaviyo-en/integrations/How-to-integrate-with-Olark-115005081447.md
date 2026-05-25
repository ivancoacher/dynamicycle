---
id: "115005081447"
title: "How to integrate with Olark"
source_url: "https://help.klaviyo.com/hc/en-us/articles/115005081447-How-to-integrate-with-Olark"
section: "Olark"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:19Z"
language: "en"
---
## You will learn

Learn how to integrate Olark, a live chat provider, with Klaviyo in order to automatically sync chat activity to your Klaviyo account after a chat conversation ends. Klaviyo receives data from Olark via a webhook configured from within your Olark account. To enable the integration, you'll first get a webhook endpoint URL from Klaviyo, which you will add to your Olark account to complete the integration.

## Get webhook endpoint from Klaviyo

1. In your Klaviyo account, select the ****Integrations**** tab.
2. Select ****Explore apps****, search for **Olark**, then click the card. Then, click ****Install****.
3. Click ****Connect to Olark****.
4. Copy the provided webhook endpoint URL, and keep it secure, for use in the next section of this guide.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28717810667547)
5. If you would prefer to sync specific chats to Klaviyo, check the option **Only sync chats with visitors in specific Olark groups**. Then, add the names of the groups you'd like to sync into Klaviyo separated by commas. You can take advantage of this feature when first getting started, or you can come back and adjust your integration settings later on.
6. When you are done, click ****Complete setup****.

## Set up webhook in Olark

1. Log in to Olark and navigate to the ****Integrations**** page.
2. Enter "Webhooks" into the search box at the top of the page and click on ****Webhooks**** when it appears.
   ![Integrations page in Olark with web in the searchbar and Webhooks in the search results](https://klaviyo.zendesk.com/hc/article_attachments/28717850261659)
3. In the box under **URL to post to**, paste the webhook endpoint URL you previously copied from Klaviyo.
   ![Connect a Webhook box in Olark with URL to post to box, other settings, and Save with blue background](https://klaviyo.zendesk.com/hc/article_attachments/28717810654875)
4. You can choose to add any of the options under the webhook URL box if needed.
5. Click ****Save****.
6. If the webhook connection was successful, you'll see a green box with the text **Settings saved successfully!** and the option to test your new connection.
   ![Connect a Webhook box in Olark with green Settings saved successfully banner and blue Connected banner with send text with white background](https://klaviyo.zendesk.com/hc/article_attachments/28717810646427)
7. If the webhook connection was not successful, check the Olark [Webhooks Integration Guide](https://www.olark.com/help/webhooks) for more assistance.
8. Click ****Send test**** Helvetica, Arial, sans-serif;"> to make sure your endpoint is configured correctly. If the test is successful, you will see a green box with the a smiley face and the text **Test sent**.
   ![Connect a Webhook box in Olark with green Sent test banner with smiley face](https://klaviyo.zendesk.com/hc/article_attachments/28717810650011)

## Olark data in Klaviyo

When an Olark chat finishes, Klaviyo will automatically record who the chat was with and any custom properties you set on that chat. If a chat was anonymous, Klaviyo will not store any of the chat's data.

There is one Olark metric tracked in Klaviyo: **Chatted on Website**. Navigate to the ****Metrics**** tab in Klaviyo (under the ****Analytics****) dropdown, you can view and filter al recorded events by filtering to the **Chatted on Website** events.

![Metrics tab in Klaviyo filtered by Olark with Chatted on Website in list](https://klaviyo.zendesk.com/hc/article_attachments/28717810659611)

As a part of the **Chatted on Website** metric, Klaviyo automatically receives the following information about a customer (if available):

- Email
- First Name
- Last Name
- Organization
- Phone Number
- City
- Region
- Country

You can expand an event to see the “From” field, as well as the chat message. If there’s no location information available, Klaviyo will automatically use IP geolocation to determine where a customer is located. Klaviyo also records any custom properties you may have set for a customer.

![Klaviyo activity feed for Chatted on Website event showing one timestamped event for Natalie](https://klaviyo.zendesk.com/hc/article_attachments/28717810662555)

## Outcome

You have integrated Olark with Klaviyo, and now new Olark chats will be tracked in Klaviyo in real-time.

## Additional resources

- [Understanding types of information exchanged between Klaviyo and apps](https://help.klaviyo.com/hc/en-us/articles/360030696012)
- [Understanding how information is exchanged between Klaviyo and apps](https://klaviyo.zendesk.com/hc/en-us/articles/360030265051)