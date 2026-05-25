---
id: "360050242551"
title: "How to opt in and out of an internal alert action"
source_url: "https://help.klaviyo.com/hc/en-us/articles/360050242551-How-to-opt-in-and-out-of-an-internal-alert-action"
section: "Add steps or actions to flows"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-04-21T13:54:50Z"
language: "en"
---
## You will learn

Learn how to opt in and out of the internal alert action in a Klaviyo flow. Someone does not need to have a profile in your Klaviyo account, or exist as an account user, in order to receive emails from an internal alert action. However, all recipients will need to opt in to receive internal alerts from your account before they start receiving any messages. They can also opt out at any time. In this article, we explain the recipient opt-in and opt-out process for the internal alert action as well as the different statuses.

Opting in or out of internal account alerts does not impact a contact’s subscriber or suppression status in Klaviyo if they also have a profile in your account.

## Recipient statuses

To review recipient statuses:

1. In the flow builder, click on the internal alert.
2. In the sidebar, click on the **Sent to** dropdown.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/34335763835035)

There are three possible statuses for a internal alert recipient:

- ****Confirmed****Represented by a green checkmark next to their email. The recipient has been successfully added to the recipient list for at least one internal alert action, and has clicked through a confirmation email opting in to receive internal alerts from your account. Confirmed recipients will receive internal alerts.
- ****Unconfirmed****Represented by a dotted circle next to their email. The recipient has been successfully added to the recipient list for at least one internal alert action, but has not yet clicked through their confirmation email and opted in to receive internal alerts from your account. Unconfirmed recipients will not get internal alert messages until they confirm their opt-in.
- ****Disabled****Represented by a red X next to their email. The recipient at one point was confirmed and received internal alerts but has since opted out by clicking an unsubscribe link within an internal alert message. Disabled recipients will not get internal alert messages unless you remove them, re-add them, and they reconfirm opt-in.

## The opt-in process

When you first add someone’s email address to an internal alert action, and click to save your changes, Klaviyo will send this person an email asking them to confirm that they would like to receive internal alerts from your account, as shown below. Until a recipient confirms, their status in your **Send to** list will show as **Unconfirmed** and they will not receive any internal alerts.

![Example of an internal alert confirmation email with a 'Confirm Email Address' button.](https://klaviyo.zendesk.com/hc/article_attachments/28720771732123)

A new recipient, once confirmed, can be added to any internal alert action across any flow without needing to re-confirm. To retrigger an opt-in confirmation email to an unconfirmed or disabled recipient, simply remove them from the action, click save, and then re-add them. This will trigger a new confirmation email to be sent.

## The opt-out process

Every internal alert message will also contain an autopopulated unsubscribe link that is specifically used to track opt-outs for account internal alerts.

If someone decides they no longer want to receive internal alerts from your account, they can opt out by clicking the unsubscribe link in any internal alert email. After they opt out, they will show as **Disabled** in your **Send to** list and will be grayed out. Opted-out recipients will no longer receive internal alerts.

If a recipient unsubscribes, they will become disabled and no longer receive any internal alerts from your account moving forward.

## Troubleshooting

To test if internal alerts are sending properly, enter your own email address as a recipient and check your inbox for the opt-in confirmation.

If you haven't received the opt-in email, check the following:

- Check your spam folder to see if the email was filtered.
- Make sure the **From / reply-to email** is a valid address. Similar to the sending address you use for customers, this must be a business email with a domain associated with your website and not a personal email address.

## Additional resources

- Learn more about the internal alert action:
  - [Add an internal alert action to a flow](https://help.klaviyo.com/hc/en-us/articles/360050242251)
  - [Internal alert action use cases](https://help.klaviyo.com/hc/en-us/articles/360049857552)
- Find out [how contacts move through a flow](https://help.klaviyo.com/hc/en-us/articles/360017706091)