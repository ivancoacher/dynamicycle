---
id: 115005258768
title: "How to add a custom web feed in an email"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005258768-How-to-add-a-custom-web-feed-in-an-email"
section: "Build and use products "
category: "Content"
category_slug: "content"
klaviyo_updated: "2026-04-21T13:54:25Z"
language: en
---

## You will learn

Learn how to add and use a custom web feed within an email. A custom web feed allows you to dynamically populate a feed of data from an external URL within a Klaviyo email. Before sending an email, Klaviyo makes an HTTP request to the URL and fetches the data. The content of the web feed is then available for use in your email.

The power of web feeds is that they allow you to use a single template and pull in content dynamically, where you only need to keep the feed up-to-date and Klaviyo will ensure fresh content from your feed gets populated into every send.

This article will go over adding and using a custom web feed in campaigns and flows.

## Before you begin

The first step to adding dynamic external content to any email in Klaviyo is creating your web feed source. Your feed must:

- Be hosted at an accessible URL in either JSON or XML format
- Be 3.3 MB or smaller
- Not use a redirecting URL

Klaviyo will make an HTTP request to your specified URL and fetch your feed data. Due to how flow emails send continuously, Klaviyo will keep your feed content up-to-date by periodically querying your feed URL to pull in refreshed content on one of the following schedules:

- ****15-minute refresh****
  Klaviyo will attempt to refresh your feed every 15 minutes. In order to accomplish this, your feed must load within five seconds and return with a successful response.

While Klaviyo refreshes web feeds every 15 minutes, it can take longer for the refresh to complete. For your web feed products to be updated campaigns, the feed should be updated at least 30 minutes prior to a campaign send.

- ****Nightly refresh****
  If your feed takes longer than five seconds to return, after three hours of trying, we will start trying to update your feed nightly instead. For ongoing nightly refreshes, your feed must load in under 30 seconds.

If we cannot load your feed within 30 seconds for three nights in a row, you will not be able to use this feed in your emails. Flow emails relying on this feed will stop sending, and campaign and flow emails will not send until the feed is removed or the outstanding issue with your feed is resolved.

When we query your feed, if we get an error response, we will be unable to access your feed content. We will follow the same pattern as above and retry for up to three days. In the meantime, emails will not send.

If we are having trouble accessing your web feed, you will receive in-app and email notifications letting you know. An easy troubleshooting step is to double check the feed requirements and make sure they fit the parameters outlined above.

Should you make changes to a feed — for example, reduce the size to speed upload time or fix an issue causing an error response — and would like Klaviyo to attempt a new refresh, navigate to the feed in the Data Feeds tab and click ****Update Data Feed****. We will test and re-validate your feed. If your feed is valid and returns a timely response, we will resume trying to keep your content up-to-date. This is a good troubleshooting step to try if you are having trouble accessing your web feed, even if you have not made changes.

## Django filters

We support the use of Django filters for the variables you insert. Below are a few commonly used filters, and you can learn more in our [guide on Using Filters to Customize Variables](https://help.klaviyo.com/hc/en-us/articles/360058907911) and the [Glossary of Variable Filters](https://help.klaviyo.com/hc/en-us/articles/360058466052).

### Limit post summary to X number of words

If you want to include a brief summary of a blog post under the post title (and your feed provides this summary text), you can use [the Truncate Filter](https://docs.djangoproject.com/en/4.2/ref/templates/builtins/#truncatechars).

![An example of the truncatechars Django filter](https://klaviyo.zendesk.com/hc/article_attachments/28723518838683)

To limit the summary of an article to 250 characters, for example, you may use:

`{{ item.summary|truncatechars:250 }}`

## Add a custom web feed

### Set up your feed

1. Click on your company name in the bottom-left corner of Klaviyo.
2. Click ****Settings****.
3. Click ****Other****.
4. Click ****Web feeds****.
5. Click ****Add Web Feed****.
6. Fill in the web feed fields as follows:
   - ****Feed name****
     You’ll later use this identifier in your template to access the feed’s content. Give your feed a short descriptive name. We recommend naming feeds either in camel case (e.g., "MyDataFeed") or all uppercase with spaces replaced by underscores (e.g., "MY\_DATA\_FEED"). Spaces are not permitted in feed names.
   - ****Feed URL****
     The endpoint Klaviyo uses to fetch the feed contents (i.e., the URL of the JSON or XML feed configured previously). If your feed contains private information, we strongly recommend using an HTTPS URL and including a nonce query parameter to secure your feed.
   - ****Request method****
     Specify the HTTP method that will be used to request your feed. If you’re not sure which to choose, select ****GET****.
   - ****Content type****
     The format of the feed (either JSON or XML). We recommend using JSON if possible. For XML feeds, the feed will be converted to JSON.
7. Once you've filled out all the fields, click ****Add web feed****. We will attempt to query the Feed URL and validate your feed is working properly. If we encounter an error, you will see an error message and will be unable to save this new feed until the issue is addressed.
   - Want to try this out but don't have your own web feed URL? Use ours. Copy the following URL for the Klaviyo Help Center into the **Feed URL** box and try it out in your own Klaviyo account:

     ```
     https://help.klaviyo.com/api/v2/help_center/en-us/articles.json
     ```
8. Klaviyo validates your feed and shows any potential errors. Once validated, you will see your feed in Klaviyo and it's ready to be used in emails.
   ![A validated feed](https://klaviyo.zendesk.com/hc/article_attachments/28723507172507)

### Preview your feed

It's useful to preview a web feed before adding it to an email. To preview a feed:

1. On the **Web feeds** page, find your feed.
2. Click the three dots, then select ****Edit****.
   ![The Edit option](https://klaviyo.zendesk.com/hc/article_attachments/28723518845467)
3. From the feed detail page, click ****Preview****.

When previewing your feed, you will either see the feed content or an error message if we cannot load the feed.

If your feed is a JSON array, we'll automatically parse and show each row individually. If it's anything else, most likely a JSON dictionary, we'll show the entire dictionary.

If you are actively developing your feed, use the ****Refresh**** button to pull the latest version of your feed. The preview page for a feed shows the entire feed. If your feed is large, it may take several seconds to display the contents. Keep in mind if your feed takes over 30 seconds to query, this will impact the performance of any emails relying on this feed.

Now that you've added a web feed and previewed its contents, you can use it in an email.

## Use a web feed in an email

For campaigns, Klaviyo will fetch each feed once per send, and store the returned content. Even if you're sending to thousands of recipients, Klaviyo won't make thousands of requests to your servers.

### Populate feed content in a template

In our example web feed from the previous section, we have an array of articles where each entry includes a name, URL, article ID, and more. After a feed is added to an email, it's available through the feeds variable:

`{{ feeds }}`

For example, for the JSON feed above, we can now reference or output the contents of the articles feed by including this syntax in our template:

`{{ feeds.Klaviyo_Help_Center }}`

Let's run through an example where we iterate over all entries in the array, displaying certain variables. We'll use the Klaviyo Blog feed as an example here, and iterate over Images.

1. Drag a new text block into your email and place it where you want the web feed to populate.
2. Turn on the Repeat Block/Content Repeat Feature: click into the text block’s ****Display Options**** tab, then click ****Create Repeat Rules****.
3. For the **Repeat For** field, insert **feeds.YOUR\_FEED\_NAME**, followed by the name of the variable(s) that contain the array you want to iterate through.
   - In our example, because we are iterating over the "articles" value as well, we will repeat for: **feeds.Klaviyo\_Help\_Center.articles**.
4. Your data may be nested within a series of variables. For example, your feed might be structured like this:

   ```
   rss: {
            .....
            channel: {
                    .....
                        item: {
                                .....}}}
   ```

   In this case, you’d use `feeds.YOUR_FEED_NAME.rss.channel.item` as your **Repeat for**.
5. If you only want this block to iterate over a certain number of entries, use the "slice" filter. To use this filter, adjust the **Repeat For** value by adding the filter to the end:  `feeds.Klaviyo_Help_Center.articles|slice:':3'`
   In this example, `|slice:':3'` will cause only the first three entries to display.
6. For the **Item Alias** field, insert: `item`
7. Once you have configured the **Repeat Block/Content Repeat** feature, you can insert variables using the "item" alias.
8. To identify and add variables, open your web feed’s preview and reference the way your data is structured. Any data nested within the array used in the **Repeat for** field can be used as a variable.
   In this example, all of the data shown within the articles array is available for use in an email:
   ![Data nested within the articles array](https://klaviyo.zendesk.com/hc/article_attachments/28723507180827)
9. For first-level data, simply add **item** before the variable name shown in your data. For example, use `{{ item.title }}` to display an article’s title, or `{{ item.url }}` to display an article’s URL.
10. To access data nested within the first-level variables, use dot notation (e.g., `{{ item.images.thumbnail_url }}`). To learn more about dot notations and template variables, head to our [guide to template tags and variable syntax](https://klaviyo.zendesk.com/hc/en-us/articles/4408802648731).
11. When you preview your template, you will notice that the **Repeat Block/Content Repeat** feature will allow this simple text block to automatically iterate over all entries in your feed. Only the variables you specify in the text block will show for each entry.
12. If you are inserting an image, please note that you will need to edit the **Source code** field of the text block and contain the image in an `<img src>` tag.
    ![custom web feed image](https://klaviyo.zendesk.com/hc/article_attachments/28723507183259)

You've added a custom web feed to your email and can now dynamically populate a feed of data from your external URL.

## Test or validate your feed

If you receive an email or in-app notification that we are having trouble accessing your web feed:

1. Navigate to your feed and click the ****Update feed**** button.
2. Once validation completes, there are two types of error messages that you might see:
   - ****Invalid Response****
     If we receive an error response when attempting to query your feed content, we will tell you the status code of the error. You will need to address the issue causing this error response before the feed can be successfully used within any email.
   - ****Performance Issue****
     If we do not get a response from your feed within 30 seconds, this will lead to sending delays. While you may have been able to save your feed historically, to mitigate the risk of sending delays, you will need to address the performance issue with your feed before re-validating and successfully saving it.

In both cases, if you use a problematic feed within a send, this will lead to sending delays or your email may be cancelled altogether. For flows, it is also likely emails are not sending.

We recommend removing a problematic feed from all emails while you address any outstanding issues to prevent sending disruption.

## Additional resources

- [Troubleshoot your Instagram web feed in emails](https://help.klaviyo.com/hc/en-us/articles/360039881992)
- [How to use product feeds and recommendations](https://help.klaviyo.com/hc/en-us/articles/115005082787)