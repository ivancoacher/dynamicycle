---
id: 360039881992
title: "Troubleshooting your Instagram web feed in emails"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360039881992-Troubleshooting-your-Instagram-web-feed-in-emails"
section: "Meta Ads"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-17T00:34:28Z"
language: en
---

## You will learn

Learn how to troubleshoot your Instagram web feed if it is not working in your emails, which is likely due to Klaviyo having an issue retrieving your feed content. To determine the cause, we recommend first trying to test your feed.

## Test your feed

If you would like to test or preview an existing Instagram feed, navigate to the Data Feeds section of your Klaviyo account by doing the following

1. Click your account name in the lower left corner.
2. Navigate to ****Settings > Other > Web feeds****.
3. Click on the feed that references Instagram.
4. In the upper right-hand corner, click ****Preview.****

If you are able to preview your feed content, this means your feed is currently set up correctly and working as expected. Make sure your feed is referenced properly in your email.

If you see an error message, this likely means your feed URL was either not set up correctly or the required access permissions have expired. Reference the section below if you are seeing errors and believe your feed may be relying on Instagram's Legacy API.

## Does your feed rely on the Instagram legacy API?

As of June 29, 2020, Instagram will deprecated their Legacy API. This API was commonly used by Instagram users & third-party applications to pull Instagram content and generate a feed of recent posts.

If your Instagram web feed relied on this Legacy API, or relied on a third-party app that was built using Instagram's Legacy API, these feeds will no longer work. Unfortunately, as this API is managed by Instagram and this is something that Klaviyo has no control over.

First, head to your Instagram web feed from the [Data Feeds section](https://www.klaviyo.com/feeds). Here, you will find any Web Feed that may be setup to pull in content from your Instagram account.

## What to do if your feed relies on the Instagram legacy API

#### ****If your feed directly references api.instagram.com****

You will need to explore using Instagram's new [Basic Display API](https://developers.facebook.com/docs/instagram-basic-display-api) (which requires you to regularly refresh your [Access Token](https://developers.facebook.com/docs/instagram-basic-display-api/overview#instagram-user-access-tokens)) or an [RSS Feed Generator](https://rss.app/) to pull content directly from your Instagram account. [Review our step-by-step instructions on adding Instagram content to your emails.](https://help.klaviyo.com/hc/en-us/articles/360004384031-Using-Instagram-Content-in-Campaign-Emails)

You can alternatively seek out a third-party application that supports generating an Instagram Feed for you such as [Klaviyo technology partner Foursixty](http://foursixty.com/?utm_source=partners&utm_medium=blog&utm_campaign=Klaviyo).

#### ****If you are using a third-party app to generate your feed****

Reach out to the service you are using and follow their instructions to ensure your feed can remain active if possible.

## Alternatives to using an Instagram web feed

If a live updating Instagram feed is not essential for you to have, while not the most evergreen option, you can add static images of your Instagram to your messages. This is recommended if you are having trouble generating a feed on content directly from your Instagram account. For more information, check out our article on [using images in templates](https://help.klaviyo.com/hc/en-us/articles/115000108632).

## Additional resources

- [How to use Instagram content in campaign emails](https://help.klaviyo.com/hc/en-us/articles/360004384031-Using-Instagram-Content-in-Campaign-Emails)
- [Getting started with Meta Ads](https://klaviyo.zendesk.com/hc/en-us/articles/115005082127)