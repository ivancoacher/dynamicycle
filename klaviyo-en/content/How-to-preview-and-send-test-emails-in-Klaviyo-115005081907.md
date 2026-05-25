---
id: "115005081907"
title: "How to preview and send test emails in Klaviyo"
source_url: "https://help.klaviyo.com/hc/en-us/articles/115005081907-How-to-preview-and-send-test-emails-in-Klaviyo"
section: "Getting started with templates"
category: "Content"
category_slug: "content"
klaviyo_updated: "2026-04-21T13:54:19Z"
language: "en"
---
Learn how to preview and test drag-and-drop emails in Klaviyo so you can be confident in how your email will appear in each recipient’s inbox.

After you design a new email, there are several ways to preview and test how your email will look when it's sent:

- Preview in Klaviyo
- Send a preview email
- Send a live campaign to a preview list
- Test your email with a third-party tool

Keep in mind that the options available when previewing will depend on whether your email was created as an email template, a flow email, or a campaign.

![](https://fast.wistia.com/embed/medias/quctt6z3i0/swatch)

This article covers previewing drag-and-drop emails in Klaviyo. If you are previewing an HTML email:

1. Navigate to the HTML editor.
2. Click ****Preview********Email****.
3. Under **Choose a different person:**, type an email and select the profile you'd like to preview as.
4. Click ****Preview Now****.

## How to preview an email in Klaviyo

To preview a campaign or a list-, segment-, or date-triggered flow email:

1. Navigate to the email template editor for a template; a campaign; or a list-, segment-, or date-triggered flow email.
2. Click ****Preview & test**** from the template editor.
   ![preview and test button](https://klaviyo.zendesk.com/hc/article_attachments/28716328666267)
3. In the **Search profiles** field, enter the email of a profile that includes the variables in your message.
4. Preview the message in Klaviyo’s previewer or click ****Send Test**** to send a test to your inbox.
5. Click ****Done**** to return to the editor.

   To preview an event-triggered flow email:
6. Navigate to the email template editor for an event-triggered flow email.
7. Click ****Preview & test**** from the template editor.
   ![preview and test button](https://klaviyo.zendesk.com/hc/article_attachments/28716328666267)
8. If needed, use the arrows next to **Select a profile for the preview** to preview different instances of the event.
9. Preview the message in Klaviyo’s previewer or click ****Send Test**** to send a test to your inbox.
10. Click ****Done**** to return to the editor.

While previewing the email in Klaviyo’s preview modal, you have a few previewing options:

- ****Desktop/Mobile****
  Toggle between desktop and mobile views of your message.
- ****Previewing as****
  Search or toggle between profiles to see how your email will appear to different recipients.
- ****Send test****
  Use this button to send an email to your own inbox or other previewers.
- ****Profile/Event****
  When previewing a template found in ****Content > Templates****, you have the option to choose event data to preview with. Note that event data is only supported in flows triggered by that event.

Sending a preview email will allow you to test how an email will render when viewed in your own inbox. Keep in mind, however, that message variables (such as manage preferences and unsubscribe links) and dynamic coupons will not render in previews, rather than functional links or coupons. Klaviyo will also not apply Google Analytics tracking variables or click tracking to links in a preview email.

You can send previews to multiple email addresses by separating the addresses with a comma.

## How to share an email preview link

This feature is only available for paid Klaviyo accounts.

1. Navigate to the template editor for any email.
2. Click ****Preview & test****.
3. Select ****Inbox testing****.
4. [Run an inbox test](https://help.klaviyo.com/hc/en-us/articles/37463094051611).
5. Once the inbox test is complete, toggle on the **Share a preview link** setting.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/39934405550875)
6. Click the copy icon to copy the share URL to your clipboard.
7. Share this link with anyone you’d like to review the email.

The sharing link will expire after 6 days, or immediately if you disable preview link sharing. Previewers will be able to see all the versions of the message you selected when you ran the inbox test.

## Preview email limits

When previewing an email, you can add up to 30 recipients at one time. In addition to this per-preview limit, accounts have a monthly email limit.

Monthly email preview limits are applied per account relative to your email billing plan. Preview limits vary based on the total number of profiles covered by your plan.

|  |  |
| --- | --- |
| ****Plan size**** | ****Preview email limit (per billing cycle)**** |
| 0-250 contacts (free plan) | 100 preview emails |
| 251-500 contacts | 500 preview emails |
| 501+ contacts | 1/10th of your plan's sending capacity |

To see your current billing plan:

1. Click your account name in the bottom-left corner of Klaviyo.
2. Select ****Billing****.
3. Scroll down to the **Profiles + email** section and note your plan size.

For any plans over 500 contacts, your preview limit is based on your plan size. For example, if your plan accounts for 5,001-5,500 contacts, then your total permitted number of emails is 55,000. This means your email preview limit is 5,500 emails.

## Sending a live campaign to a preview list

When you send a preview email using the template editor's preview tool, message variables (such as manage preferences and unsubscribe links) and dynamic coupons will render previews, rather than live links or coupons. Klaviyo will also not apply Google Analytics tracking variables or click tracking to links in a preview email. If you are interested in testing how these will appear and function in your email, we recommend sending a live test email.

1. Create a new list titled "Preview" (or similar).
2. Use the ****Quick Add**** button to add yourself or members of your team.
3. Ensure your new email is saved as a template if you did not design your email from ****Content > Templates****.
4. Create a new campaign.
5. Choose your preview list as the recipient list.
6. Configure your message details, including a subject line and from address.
7. Choose your template.
8. Send the campaign.

The email you receive will contain live links, and will provide an accurate preview of what your contacts will see when they receive the same message.

Messages sent as campaigns will not contain the dynamic event content available within metric-triggered flows. To send a live metric-triggered flow email that populates all event details, you must trigger the flow yourself by taking the trigger action.

## Testing across inboxes

If you are concerned about how your email design will render across different email clients and devices, use Klaviyo's built-in inbox testing, in partnership with Mailgun. [Learn how to use inbox testing with Klaviyo](https://klaviyo.zendesk.com/hc/en-us/articles/37463094051611).

While it isn't always possible to optimize an email design for all email clients and devices, understanding the differences in how emails render can be useful as you test different variations.

Mobile optimization relies on media queries, which are fully supported by Apple Mail for Android and iOS and Samsung Email for Android, and partially supported by Gmail for iOS and Android and other mobile email apps. Learn more about [support for media queries](https://www.caniemail.com/features/css-at-media/).