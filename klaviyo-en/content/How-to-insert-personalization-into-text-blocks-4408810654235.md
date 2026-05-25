---
id: "4408810654235"
title: "How to insert personalization into text blocks"
source_url: "https://help.klaviyo.com/hc/en-us/articles/4408810654235-How-to-insert-personalization-into-text-blocks"
section: "Use variable syntax and tags"
category: "Content"
category_slug: "content"
klaviyo_updated: "2026-04-21T13:55:00Z"
language: "en"
---
Learn how to add personalization to email templates by including things like a recipient’s first name, custom properties, an unsubscribe link, and more.

You can add these tags to your templates by typing them directly into a text field by copying them from the email preview modal, or by using the personalization menu in a text block.

## Before you begin

Before you get started, it’s helpful to understand how personalization works within Klaviyo. The tags available in your account are different from the tags in anyone else’s Klaviyo account, and are dependent on the data you store in Klaviyo.

You can store and use a small handful of default Klaviyo properties (like first and last name), along with an unlimited number of custom profile properties and dynamic event data. To see all of the tags available in your own account, follow the steps for adding them through the personalization menu or the preview modal below.

## Add tags using the personalization menu

To add personalization without copying, pasting, or typing anything, use the personalization menu:

1. Select a text block that you would like to add personalization to.
2. Click the edit icon.
3. In the upper left, click the personalization icon. A searchable dropdown menu will appear with a list of profile and custom properties, along with select event properties in certain event-triggered flow messages.
4. Scroll through the tags or search to find the one you’d like to add, then click it to add it to your template.

![](https://klaviyo.zendesk.com/hc/article_attachments/32002307618075)

## Add personalization from the preview modal

You can add profile property and event data by copying them from the preview modal and pasting them into your message. Learn more about [using the preview panel for message personalization](https://klaviyo.zendesk.com/hc/en-us/articles/27843522951707).

### Adding profile properties

To add profile personalization from the preview modal:

1. Click ****Preview & test**** from the template editor.
2. For event-triggered flow emails, use the arrows to navigate between the 10 most recent events. For other messages, search for a profile that includes the tag you’d like to add. Note that you’ll only copy the tag name from the sample user’s profile, and each recipient of the email will see information from their own profile.
3. Open the ****All properties**** dropdown and scroll until you find the tag you’d like to use.
4. Hover over the tag's name until you see the message **Copy {{ person.variable\_name }} variable**, then click to copy it.
5. Click ****Done****.
6. Paste the variable into a block in your template.

### Adding event variables

To add an event variable from the preview modal:

1. Click ****Preview & test**** from the template editor.
2. If available, under **Preview data source**, click ****Event**** and select an event from the dropdown. Note that this option is only available under ****Content > Templates****; the correct even is automatically selected for event-triggered flow emails.
3. Open the ****All properties**** menu and scroll through the **Event properties** until you find the variable you’d like to use. If you don’t see the variable you need, use the arrows to select a different instance of the event.
4. Hover over the variable’s name until you see the message **Copy {{ event.variable\_name }} variable**, then click to copy it.
5. Click ****Done****.
6. Paste the variable into a block in your template.

You can also paste in variables from other areas (e.g., other templates or a Klaviyo Help Center article). If you paste a variable from elsewhere, make sure to paste it as plain text using ****Command+Shift+V**** or ****Control+Shift+V****. This will ensure no formatting is pasted along with your text, which can introduce code errors and increase the size of your message.

## Manually adding personalization

If you know a variable’s name, you can add it by typing it into a text field directly. Klaviyo variables use the following structures:

|  |  |
| --- | --- |
| ****Variable type**** | ****Sample Format**** |
| Profile properties (no spaces or special characters) | {{ person.variable\_name }} |
| Profile properties (any) | {{ person|lookup:'variable name' }} |
| Event properties (no spaces or special characters) | {{ event.variable\_name }} |
| Event properties (any) | {{ event|lookup:'variable name' }} |

## Setting a default value

You may not always have complete information for every email recipient you contact. For example, you might have some subscribers’ first names, but not others. To avoid blank spaces in your emails for those recipients with incomplete data, use the default filter to set a backup.

To add the default filter:

1. Add the following after your variable name: |default:''
2. Add your default variable between the single quotes. In an email, this might look like:

|  |
| --- |
| Hey {{ first\_name|default:'friend' }}! |

When the message is sent, any recipients whose names are not stored in your database will see this message:

|  |
| --- |
| Hey friend! |

## Additional resources

- [Using filters to customize your variables](https://developers.klaviyo.com/en/docs/glossary_of_variable_filters)
- [Message personalization reference](https://klaviyo.zendesk.com/hc/en-us/articles/4408802648731)
- [Guide to the email template editor](https://help.klaviyo.com/hc/en-us/articles/4407911841435)