---
id: "360004384031"
title: "How to use Instagram content in emails"
source_url: "https://help.klaviyo.com/hc/en-us/articles/360004384031-How-to-use-Instagram-content-in-emails"
section: "Build and use templates"
category: "Content"
category_slug: "content"
klaviyo_updated: "2026-04-21T13:54:42Z"
language: "en"
---
## You will learn

Learn how to set up a custom web feed with your Instagram account using an RSS feed generator, and how to display the feed in your emails. With a custom web feed, you can connect your Instagram content to your emails and dynamically display your latest Instagram photos, captions, and more.

This process requires setting up an XML feed and inserting custom code into your email template. If you aren’t comfortable editing your email’s code, reach out to a [Klaviyo Partner](https://connect.klaviyo.com/) for help.

## Set up an Instagram web feed

To set up an Instagram web feed without the help of a developer or Klaviyo Partner, use an RSS feed generator.

Note that this RSS feed generator app requires a paid plan in order to host an Instagram RSS feed. You can use any RSS feed generator, but if you use a different app, you may need to customize the sample code in the section below.

1. Create an account with an [RSS feed generator tool](https://rss.app/).
2. Navigate to [My Feeds](https://rss.app/myfeeds).
3. In the upper right, click ****New Feed****.
4. In the **Enter Webpage URL** field, add your Instagram URL, following the format https://www.instagram.com/YOUR\_USERNAME.
5. Click ****Generate****.
6. Click ****Save to My Feeds****.

Once the feed is saved, navigate to the feed page and locate the feed URL. It should follow this format: <https://rss.app/feeds/UNIQUE_FEED_ID.xml>.

![A feed URL](https://klaviyo.zendesk.com/hc/article_attachments/28720656477851)

As an alternative to this method, you can set up an Instagram web feed using their Basic Display API, or by using a third-party app. Certain [Klaviyo Partners](https://connect.klaviyo.com/) offer this as a service, like [FourSixty](https://connect.klaviyo.com/integrations/foursixty).

## Set up your feed in Klaviyo

Once you’ve set up your RSS feed:

1. Click your account name in the bottom left corner of Klaviyo.
2. Select ****Settings****.
3. Select ****Other****.
4. Open the ****Web feeds**** tab.
5. Click ****Add Web Feed****.
   ![Add a web feed](https://klaviyo.zendesk.com/hc/article_attachments/28720668265883)
6. Name your feed and enter the RSS feed URL you just generated as the **Feed URL** in the section above.
7. Set the **Request Method** to ****GET**** and the **Content Type** to ****XML****.
   ![The feed settings](https://klaviyo.zendesk.com/hc/article_attachments/28720668267931)
8. Click ****Add web feed****.

## Pull Instagram content into your emails

If you are using a third-party platform or Instagram’s Basic Display API to generate your feed, follow our [guide on adding a custom web feed to an email](https://help.klaviyo.com/hc/en-us/articles/115005258768-Guide-to-Adding-a-Custom-Web-Feed-in-an-Email). If you’ve used the RSS feed app recommended above, use the code below to display the 3 most recent items from your Instagram feed in an email.

1. Add a new HTML block to your template.
2. Copy the following code into the HTML block, and make sure to replace FEED\_NAME with your feed name (e.g., **Instagram\_Feed** in the example above).

```
<div>{% for item in feeds.FEED_NAME.rss.channel.item|slice:":3" %}
    <table style="display:inline-block; margin-left:auto; margin-right:auto">
	<tbody>
	    <tr>
		<td style="width:150px; text-align: center;"><a href="{{ item.link }}">
		  <img style="max-width: 150px; height: auto;" src="{% if item|lookup:'media:content'|lookup:'0'|lookup:'@url' %}{{ item|lookup:'media:content'|lookup:'0'|lookup:'@url' }}{% else %}{{ item|lookup:'media:content'|lookup:'@url' }}{% endif %}" style="margin: 1px; max-width: 150px; height: auto;" /></a>
		</td>
	    </tr>
	</tbody>
    </table>
{% endfor %}</div>
```

Your Instagram feed will not load when previewing the message in Klaviyo. Send a preview email to your own inbox to make sure it appears correctly.

If you’d like to show more than 3 recent posts, adjust the filter, **|slice:":3"**, to include the number of posts you’d like to display (e.g., |slice:":6" to show 6 posts).

If you’d like to add additional fields to your table (e.g., captions or the date an image was posted), follow our guides on [adding custom web feeds to emails](https://help.klaviyo.com/hc/en-us/articles/115005258768-Guide-to-Adding-a-Custom-Web-Feed-in-an-Email) to adjust the code above as needed.

We only recommend using custom HTML for technically savvy marketers, or for anyone who has access to a developer. While our product does support custom HTML, our support team is unable to help you build out your custom templates beyond offering the general guidance covered in this documentation. To maintain the security of your data, Klaviyo's support team is not able to open your HTML files.

If you need developer assistance to set this up, reach out to one of [Klaviyo’s Partners](https://klaviyo.partnerpage.io/).