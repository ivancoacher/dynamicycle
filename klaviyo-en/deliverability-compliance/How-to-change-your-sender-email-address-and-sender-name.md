---
id: 360024994912
title: "How to change your sender email address and sender name"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360024994912-How-to-change-your-sender-email-address-and-sender-name"
section: "Warm and ramp your domain"
category: "Deliverability & compliance"
category_slug: "deliverability-compliance"
klaviyo_updated: "2026-05-11T10:57:07Z"
language: en
---

## You will learn

Learn how to change the sender email address and sender name in your Klaviyo account.

If you’re finding that your emails end up in the spam folder when you're first getting started with Klaviyo, it may be the case that your sender email address is a Gmail, Yahoo, or another free email address. Sending mass email from a personal address can cause inbox providers like Gmail, Outlook, etc. to flag your messages as spam, as this is considered to be suspicious activity.

Before you start sending to your customers, make sure that you have an email address that includes your domain name. For example, you’ll want your sender email address to look like **yourname@yourbusiness.com**. This indicates to inbox providers that you are a legitimate sender with a legitimate business.

If you have a dedicated sending domain, your sender email address's root domain must match the root domain of your dedicated sending domain.

## Changing your sender information

To edit the default sender email and name settings for your business:

1. Navigate to the account menu in the bottom left corner of Klaviyo.
2. Select ****Settings****.
3. Click ****Organization****.

   ![Organization tab in account settings, where you can update the default sender name and email address](https://klaviyo.zendesk.com/hc/article_attachments/28713329926299)
4. Edit the default sender email address or sender name.
5. Click ****Update Information**** to save your changes.

After changing your default sender email address or name, any email you create after will reflect this. However, pre-existing flows and campaigns do not automatically update; rather, you will need to manually update each email. Prioritize high-engagement flows such as your welcome series, browse abandonment, and abandoned cart flows so you can set them live quickly. See the section [below](#h_01EJ90A7Y3TG8PBYKWCVMTRYCA) for more details.

Note that Klaviyo does not support the use of Unicode characters (e.g., ä ) in the email From or Reply-To fields.

## Changing your sender information for a single email

For a campaign or flow email, click into the email and navigate to the message overview page. Here, you can edit the sender email address or name directly.

Click ****Save Changes**** to save your updates.

![sendername2.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28713335603227)

## Bulk update your sender email address

You can also apply your account's default sender email address to all existing campaign and flow email messages. For campaigns, you can only update the entire email address. For flows, you can choose to update the entire sender email address, or just the domain.

To apply your default sender email to all campaigns and flows:

1. Navigate to the account menu in the bottom left corner of Klaviyo.
2. Select ****Settings****.
3. Click ****Organization****.

Next to your default sender email, you'll see the **Apply sender email to all messages**button, that you can use to apply the sender email address to all your emails in Klaviyo.

![Apply sender email to existing campaign and flow messages](https://klaviyo.zendesk.com/hc/article_attachments/28713335617691)

Once you select an option to update existing email addresses, select ****Confirm choices****for the changes to apply to your flow and campaign emails.

As part of [Gmail and Yahoo's sender requirements](https://www.klaviyo.com/marketing-resources/2024-google-yahoo-sender-requirements), bulk senders (i.e., those that send more than 5000 emails to Gmail recipients per day) must align their sending domain and their sender email address domain for all emails.

## Changing your reply-to email without changing your main sender email

If you change your sender email for a single email in a flow or campaign, it will be used as the reply-to address by default. To update the sender email without it being set as the reply-to address, uncheck the box that reads **Use this as your reply-to address**for a campaign or flow email.

**![Checkbox that allows you to set different reply-to address for campaign or flow email](https://klaviyo.zendesk.com/hc/article_attachments/28713335605275)**

## Additional resources

- [Guide to rebranding in Klaviyo](https://klaviyo.zendesk.com/hc/en-us/articles/360047183572)
- [Understanding email deliverability](https://help.klaviyo.com/hc/en-us/articles/115005247008)
- [Deliverability glossary](https://help.klaviyo.com/hc/en-us/articles/360039295051)