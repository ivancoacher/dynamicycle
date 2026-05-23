<h1>How to use deep links in push notifications</h1>

## You will learn

Learn how to use deep linking in Klaviyo push notifications so that you can direct customers to a specific in-app screen. Deep links make it easy for your profiles to access the content they want with a simple tap.

You can [deep link from email and text messages](https://help.klaviyo.com/hc/en-us/articles/41701832186523) by linking your click tracking domains to your app.

****What is a deep link?****

A deep link is a custom URI that opens your mobile app to a certain page. It’s a common feature for push notifications, allowing marketers to link to, for example, a specific product page rather than the app’s home page. This way, recipients don’t need to search your app or navigate through menus to find the page they are interested in.

****What’s a URI?****

URI stands for uniform resource identifier. URIs are similar to URLs: while a URL is the address for a website, a URI is the address (or “identifier”) for an app (or other resource).

## Before you begin

To use deep links in your push notifications, you must have connected Klaviyo to your [iOS](https://help.klaviyo.com/hc/en-us/articles/360023213971) or [Android](https://help.klaviyo.com/hc/en-us/articles/14750928993307) mobile app.

You must also have deep linking set up for your app. If you aren’t sure if your app has deep linking, please talk with your developer.

Once deep linking is set up, you can use these links in other channels besides push notifications, including email and SMS.

Note that deep links can offer a potential way for unauthorized users to gain access to your app. You should always validate your URIs and their parameters, making sure to test and get rid of any that are formatted improperly. Also, add limits to any actions so that other apps can’t affect a user’s data (e.g., deleting content).

Want to request a feature for Klaviyo push notifications? Fill out this [Google form](https://forms.gle/7iPm6JQ4eKB6H2C4A) to tell us about it!

## About deep linking

Deep links are custom URIs that go to a specific part of your app.

There are 3 parts to a deep link:

1. Identifying your app
2. Tell the app what action to take
3. Include any additional data about the action

These parts make up how your URI should look.

Note that deep links can offer a potential way for unauthorized users to gain access to your app. You should always validate your URIs and their parameters, making sure to test and get rid of any that are formatted improperly. Also, add limits to any actions so that other apps can’t affect a user’s data (e.g., deleting content).

### Deep linking example

A URI scheme looks like this: scheme:[//authority]path[?query][#fragment]

Let’s break it down using an example:

myapp://product/123abc

- myapp://
  This is the scheme, which points to your mobile app. While this scheme can be anything (letters, numbers, symbols), we recommend using your domain name. For instance, if this was Klaviyo’s app, it would look like: **klaviyo://**
- product/
  This is the path in the URL, telling the app which page to open a product page (i.e., the action).
- 123abc
  This provides the app with additional information; in this case, to open the page for product 123abc.

****Can I include UTM parameters in deep links?****

Yes, you can use UTM parameters in both campaign and flow push notifications. This way, you can monitor the performance of push notifications in Google Analytics or other software.

For now, you will need to add the UTM parameters manually.

****Can I include dynamic variables and personalization tags in deep links?****

Yes, you can include both dynamic variables and [personalization tags](https://help.klaviyo.com/hc/en-us/articles/4408802648731) in deep links. You can thus personalize the links so that you can direct someone to their profile, cart, or favorites.

## Add a deep link to a push notification

You can add a deep link when creating the message text for your push notification.

Note that you’ll see different options depending on if you set up push for iOS, Android, or both. If you only have iOS set up in Klaviyo, you won’t have the option to add an Android deep link (and vice versa).

1. In Klaviyo, navigate to the campaign or flow message where you want the deep link.
2. Go into the message editor.
3. Enter in your push notification content.
4. On the left-hand menu, click the ****Behaviors**** tab.
5. Click the dropdown under **Open Action**.
6. Select ****Deep link****.
   Note that for the example below, the account only has enabled iOS push notifications.
   ![Option to send a deep link in a push notification.](https://klaviyo.zendesk.com/hc/article_attachments/34417696684955)
7. Add in your deep link(s).
   Note: If the link is the same for both Android and iOS, you must add it to both fields.
8. Click ****Next**** to save the message with the deep link and proceed with sending your message.

## Outcome

After including a deep link in your push notification, anyone who clicks on the message will automatically be directed to the page you specified.

This makes it easy for you to promote new products, encourage recipients to fill out their profiles, and more.

If you’re experiencing issues with your deep link (e.g., if it doesn’t open the right page), we encourage you to talk to your developer, as Klaviyo cannot help you troubleshoot these issues.
