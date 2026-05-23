---
id: 34603509978907
title: "Understanding in-app forms"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/34603509978907-Understanding-in-app-forms"
section: "Push notification campaigns"
category: "Campaigns"
category_slug: "campaigns"
klaviyo_updated: "2026-05-05T20:44:44Z"
language: en
---

## You will learn

Learn about in-app forms and how you can use them to share important messaging with your mobile app users.

This guide provides an overview of in-app forms, including how they work and customization options in the form editor. To learn how to create a new in-app form, please refer to our guide on [How to create an in-app form](https://help.klaviyo.com/hc/en-us/articles/34567685177883).

## What are in-app forms?

Mobile in-app forms are messages that appear to users inside your mobile app, similar to how a sign-up form would appear on a website. They are designed to capture the attention of users at opportune moments when they open the app.

In-app forms created in Klaviyo will be visible to all users who open your app (depend on the form's display settings), making them an effective tool for engaging users while they're actively using your app and more likely to take action.

Any account with a mobile app can use in-app forms; however, they’re only supported to display on iOS and Android devices. Your mobile app must be using at least version 4.2.0 of the iOS SDK, version 3.2.0 of the Android SDK, or version 1.2.0 of the React Native SDK to display in-app forms. Please note that some features of in-app forms, like time delays and event triggers, are only available with the latest SDK versions.

****In-app forms vs. mobile push notifications****

Both in-app forms and mobile push notifications serve to communicate with your app users, but they function quite differently. Understanding these differences is crucial for building these communication strategies.

|  |  |  |  |
| --- | --- | --- | --- |
| ****Feature**** | ****Display location**** | ****Purpose**** | ****User details**** |
| In-app forms | Within the mobile app, on an app screen | Update users on news and/or prompt specific actions within the app | Users do not need to enable notification settings to see in-app forms |
| Mobile push notifications | On lock screens or within the notification center | Drive users into the mobile app | Users must have enabled app notifications to receive push notifications |

In short, mobile push notifications and in-app forms are different but complementary: push notifications drive app opens, where in-app forms provide visual content integrated into the app experience.

## How are in-app forms used?

In-app forms allow you to communicate with all users via the mobile app, including those who have disabled push notifications, ensuring broad reach for your messaging.

Unlike web forms, in-app forms cannot be used to gather consent or profile data and, therefore, do not need to be connected to a list.

In-app forms are ideal for:

- Informing users about important updates such as promotions, product launches, or live events.
- Encouraging users to take specific actions that can increase engagement and conversion rates.

## Building an in-app form

The form editor allows you to create popup, full page, and flyout forms for your mobile app. You can modify the appearance, content, and behavior with the various customization options in Klaviyo's form editor. Pre-built templates for in-app forms will be available in the form library soon.

![The form editor in Klaviyo showing a sample in-app form in the preview and the menu of options for customizing the form.](https://klaviyo.zendesk.com/hc/article_attachments/34609859892507)

As you build, use the undo and redo buttons (rounded arrows) in the menu bar as needed. The editor automatically saves your work as you make changes, even if you leave and return later. Note that you must publish changes to see them live on your in-app form.

### Add content to in-app forms

You can customize the content in your in-app forms to fit your needs. In-app forms are single step only as they’re focused on effective message delivery, making them ideal for announcement style messages. They do not include a success step or support consent collection for email or phone number input fields.

From the **Add blocks** tab, you can drag and drop the following content blocks into your form preview:

- ****Text****
  - Add custom text to provide instructions, context, or other relevant information to guide the user's experience with the form.
- ****Button****
  - Include interactive buttons to direct users to other pages within your app or prompt specific actions.
  - If you add a button, you can configure it to deep link to a specific page in your app (like a featured collection). Note that this functionality requires that deep-linking be set up for your app. For more information on deep links, talk to your developer, or refer to our article on [Using deep links in push notifications](https://help.klaviyo.com/hc/en-us/articles/14750403974043).
- ****Image****
  - Incorporate visual elements to enhance the form's appearance and engage users.

![The Blocks tab in the Klaviyo form editor showing the 3 block options: text, button, and image. ](https://klaviyo.zendesk.com/hc/article_attachments/34609859895067)

Once added to the form preview, click on any block to access its styling and customization options (e.g., font style, size, and color, etc.).

### Style an in-app form

Use the **Styles** tab in the form editor to modify your form's design, including:

- ****Form type****
  - Popup
    Appear in the middle of the mobile app screen. Popups are eye-catching and high-converting, but potentially disruptive to a user's experience.
  - Full page
    Display over the entire mobile app screen, capturing your users' complete attention. Full page forms are high-converting since users cannot easily overlook them; however, they are also more intrusive since users must interact with them to close them.
  - Flyout
    Slide in from the top or bottom of the mobile app screen. Flyouts strike a balance between visibility and subtlety, being noticeable enough to drive engagement while allowing users to continue interacting with the rest of the screen.
- ****Height****
  - Adjust the form's size and how much space it occupies on the screen.
- ****Background color****
  - Choose the background color of the form.
- ****Background image**** (optional)
  - Include a background image and adjust its settings.
- ****Overlay color****
  - Select a color to display behind your form. A semi-transparent overlay will highlight the form and dim the app’s content.

![Screenshot 2025-08-29 at 2.29.44 PM.png](https://klaviyo.zendesk.com/hc/article_attachments/40535404479771)

These settings are some of the key design elements, but there are additional styling options available, which you can learn more about in our guide on [How to style a sign-up form](https://help.klaviyo.com/hc/en-us/articles/4413537049883).

### Configure your form’s behavior

The **Targeting & display behavior** tab of the form editor contains the **Audience, Timing, Trigger,** and **Display frequency** settings. Use these settings to select who sees the in-app form, in which cases, when, and how frequently. Read more about setting targeting & behavior for your in-app forms in the [How to create an in-app form](https://help.klaviyo.com/hc/en-us/articles/34567685177883) guide.

We also recommend enabling the **Don’t show again if a go to app screen button is clicked** setting to prevent the form from reappearing after a user has engaged with it.

Note that in-app forms can be scheduled to go live or to be reverted to draft status. Learn more in the [How to schedule a sign-up form](https://help.klaviyo.com/hc/en-us/articles/10391017061019) guide.

![Screenshot 2025-08-29 at 2.36.27 PM.png](https://klaviyo.zendesk.com/hc/article_attachments/40535427165211)

![](https://klaviyo.zendesk.com/hc/article_attachments/42159973994523)

## Analytics for in-app forms

After you create an in-app form draft, you can find it in the forms list view within your Klaviyo account, under the ****Sign-up forms**** tab. In-app forms are marked with an "In-app" badge to differentiate them from your website forms.

![The Sign-up forms tab in Klaviyo showing an example account's existing forms in a list view.](https://klaviyo.zendesk.com/hc/article_attachments/34609859901723)

Once published, you can view the analytics for an in-app form by clicking the additional actions menu (3 dots), then ****Analytics****. The analytics page shows metrics for:

- Views
- Submits
- Submit rate

![The Overview analytics report for a sample in-app form showing the form's submit rate, and number of submits and views.](https://klaviyo.zendesk.com/hc/article_attachments/34609859903771)

When a user interacts with your form and clicks a “Go to app screen” button, Klaviyo will track both a view and submit for the form, and you can analyze these aggregate counts for the form in the **Form Overview** report.

Refer to our guide on [Understanding form analytics](https://help.klaviyo.com/hc/en-us/articles/360015960712) for more information on these metrics and how to evaluate your in-app form's performance.