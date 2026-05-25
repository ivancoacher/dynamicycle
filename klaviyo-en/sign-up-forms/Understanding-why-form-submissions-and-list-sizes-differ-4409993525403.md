---
id: "4409993525403"
title: "Understanding why form submissions and list sizes differ"
source_url: "https://help.klaviyo.com/hc/en-us/articles/4409993525403-Understanding-why-form-submissions-and-list-sizes-differ"
section: "Troubleshooting sign-up forms"
category: "Sign-up forms"
category_slug: "sign-up-forms"
klaviyo_updated: "2026-04-21T13:55:00Z"
language: "en"
---
## You will learn

Learn why the number of subscribers in your Klaviyo list doesn't match the number of submissions in your form, as well as how to find each of these numbers.

The number of form submissions will rarely match the number of subscribers on your list. This is because sign-up form analytics calculate the total number of submit events from your form, while your list size represents the number of unique profiles that are fully opted into your list. In this article, you'll learn how to find your list size and form submission count, and how to interpret these two different numbers.

## How to find form submission counts and list sizes

To find the number of submissions for a form, navigate to the ****Sign-up forms**** tab and review each form’s submission count in the **Submitted form** column. Note that this view shows the last 30 days of data.

![The Sign-up forms tab list view with the Submitted form column highlighted to show a few example forms' submit counts.](https://klaviyo.zendesk.com/hc/article_attachments/28705637596827)

To view data for a different time frame, navigate to the click on your form to see the **Analytics** page. From here you can adjust the date range as needed. The **Submits** count indicates the total number of form submissions.

![](https://klaviyo.zendesk.com/hc/article_attachments/34319309887003)

In either view, the number represents the total number of submissions for your form, so it may include duplicate submissions or submissions from non-legitimate site visitors (e.g., list bombers).

To see a list’s size, navigate to the ****Lists & Segments**** tab, then search for your list. The number of list members can be found in the **Members** column.

![The Lists & segments tab in Klaviyo showing the list view with the Members column highlighted for an example list.](https://klaviyo.zendesk.com/hc/article_attachments/28705664418203)

## Why form submissions differ from list size

Form submissions may differ from a list’s size for a variety of reasons. Before troubleshooting, first make sure that you are referencing the same list that your sign-up form is connected to by visiting the ****Sign-up forms**** tab and reviewing the list written beneath the **Form name**.

![The list view on the Sign-up forms tab with the Form name column highlighted showing 3 example forms and the list that each form is tied to.](https://klaviyo.zendesk.com/hc/article_attachments/28705637601947)

### Double opt-in

If your list is [set to double opt-in](https://help.klaviyo.com/hc/en-us/articles/115005251108), only those who complete the double opt-in step (by clicking a link in a confirmation email or responding to a welcome SMS with the confirmation keyword) will be added to the list.

Anyone who fills out the form but doesn’t complete the opt-in confirmation will be counted in your form’s submissions, but will not be included in the list.

### Duplicate submissions

If a site visitor fills out a sign-up form more than once with the same email address or phone number, each form submission will be counted in the form’s submission count. However, the person will only appear in the list once.

### Spam/list bombing

Klaviyo has [list bombing protections](https://help.klaviyo.com/hc/en-us/articles/360026474752#h_01J5TV397QJWT15VJ9DJDMK8KA) in place to prevent bad actors and spam profiles from appearing in your lists. These protections help maintain strong deliverability to ensure you can continue contacting legitimate subscribers who want to hear from you. If your sign-up form was the victim of a spam submission or list bombing attack, you may see inflated form submission numbers, but your list will not include these bad actors.

### Changes to form settings

If the list connected to your sign-up form is changed at any time, those subscribers who filled out the form before the change occurred will appear on the original list. Only those who fill out the form after a change to the form’s list will be added to the new list.

## Identifying non-subscribed form submissions

To identify profiles that filled out a form but are not members of the connected list, use a segment. Once you’ve created this segment, you can individually review the profiles to troubleshoot.

First, navigate to your sign-up form and copy the 6-digit form ID in the form’s URL.

![The form URL showing your 6-digit form ID.](https://klaviyo.zendesk.com/hc/article_attachments/28705664413979)

Next, open the ****Lists & Segments**** tab and click ****Create List / Segment > Segment****. Use the following segment definition:

****Properties about someone > $consent\_form\_id equals [6-digit form ID]****
****AND****
****If someone is in or not in list > is not > in [your list]****

This segment will contain profiles who filled out your form but are not in the attached list.