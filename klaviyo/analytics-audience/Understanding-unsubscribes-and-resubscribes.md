---
id: 115005078267
title: "Understanding unsubscribes and resubscribes"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005078267-Understanding-unsubscribes-and-resubscribes"
section: "Build and use lists"
category: "Audience"
category_slug: "analytics-audience"
klaviyo_updated: "2026-05-11T11:07:34Z"
language: en
---

## You will learn

Learn about unsubscribes in Klaviyo, and how to manually unsubscribe contacts yourself.

When a contact is unsubscribed, their consent status is set to **Unsubscribed** and they become unreachable in Klaviyo. An unsubscribe is different from [suppressing profiles](https://help.klaviyo.com/hc/en-us/articles/115005246108-Suppressed-Profiles-in-Klaviyo).

## Add an unsubscribe link to an email

To add a basic unsubscribe link, use the following Klaviyo tag: **{% unsubscribe %}**

You can place this unsubscribe tag directly in your template. By default, the **{% unsubscribe %}** tag populates as an unsubscribe link in your email with the text "Unsubscribe." If you want to customize the text in the link, this tag takes an optional parameter that allows you to customize the text.

If you need even more control, there is also a tag that provides only the URL for the unsubscribe link. All three options are shown here:

|  |  |
| --- | --- |
| ****How the tag looks within Klaviyo**** | ****How the tag appears to recipients**** |
| {% unsubscribe %} | Unsubscribe |
| If you'd no longer like to receive emails, {% unsubscribe 'click here' %} | If you'd no longer like to receive emails, click here. |
| This is a fancy <a href="{% unsubscribe\_link %}">unsubscribe</a> link.  NOTE: You will need to paste this into the source within the text block, rather than just pasting it into a text block. | This is a fancy unsubscribe link. |

When someone clicks an unsubscribe link that follows any of these formats, that click does not count toward your email's click rate unless you use a custom-coded (i.e., [hosted](https://help.klaviyo.com/hc/en-us/articles/360057676272)) unsubscribe page.

## Add one-click unsubscribe to meet Yahoo and Google sender requirements

There is no action you need to take to meet Google and Yahoo’s one-click unsubscribe requirement for bulk senders. Klaviyo automatically adds code to the header of every email you send to enable one-click unsubscribes for supported inboxes. Learn more about [Yahoo and Google’s email sender requirements](https://academy.klaviyo.com/2024-new-sender-requirements-checklist/1817230).

## List-specific vs. global unsubscribes

When an email recipient unsubscribes from an email you send, they will be suppressed for all future emails, regardless of which list(s) the message is sent to.

This setting only impacts email subscription status, not SMS or push notification consent.

If you have a paid Klaviyo plan, you can adjust this behavior on the account level or for specific lists. When the global unsubscribe setting is disabled, those who unsubscribe from a list-based email send will only be removed from the list (or lists) that email was sent to, and may still receive emails sent to other lists they have subscribed to.

If a campaign is sent to multiple lists, unsubscribes will always be treated as a global unsubscribe.

To maintain strong deliverability and avoid recipients marking your emails as spam, Klaviyo highly recommends that you leave global unsubscribes enabled.

To disable global unsubscribes for a single list (paid plans only):

1. Select your list from the ****Lists & Segments**** tab.
2. Open that list’s settings.
3. Uncheck the option **When someone unsubscribes from [LIST NAME], unsubscribe that person from all future emails.**
4. Click ****Update List Settings****.

****![Checkbox to disable global unsubscribe for specific list](https://klaviyo.zendesk.com/hc/article_attachments/28717379586331)****

To disable this setting for all lists:

1. Navigate to ****Settings > Other****.
2. Scroll down to the **Consent** section.
3. Uncheck the option **When someone unsubscribes from a list, unsubscribe that person from all lists.**
4. Click ****Update Email Consent Settings.****
5. ![Checkbox to disable global unsubscribe option at global level](https://klaviyo.zendesk.com/hc/article_attachments/28717385813275)

## Manually unsubscribe an email from Klaviyo

### Unsubscribe one or more emails globally

To manually unsubscribe someone from all emails sent by Klaviyo:

1. Navigate to the **Profiles** tab.
2. Select ****View s********uppressed profiles**** in the upper right-hand corner of the screen.
   ![Profile page header with profile count and view suppressed profiles button](https://klaviyo.zendesk.com/hc/article_attachments/28717379610523)
3. Choose whether you want to suppress a single profile or bulk suppress many profiles.

- To suppress a single profile, click the ****Add Email Address**** button.
- To bulk suppress contacts, use the ****Upload File**** button.

You can also suppress and unsubscribe a profile on the **Details** tab of a profile. To do this, click on menu next to the consent indicator on their profile:

![Options to suppress or unsubcribe currently subscribed profile](https://klaviyo.zendesk.com/hc/article_attachments/28717379625499)

Note that manually suppressing a profile will make them unreachable, but will not change their consent status and they can be unsuppressed later. Unsubscribing a user will set their consent status to **Unsubscribed** and they will have to resubscribe to receive emails again.

![Manually suppressed profile with that is still subscribed](https://klaviyo.zendesk.com/hc/article_attachments/28717379613083)

### Unsubscribe an email for a specific list

1. Navigate to the list you want to unsubscribe profiles from.
2. Click the ****Manage List**** dropdown.
3. Select ****List Suppressions****. ****![List suppressions option in manage lists menu](https://klaviyo.zendesk.com/hc/article_attachments/28717379590043)****
4. Click ****Add Email Address**** in the upper right.
5. Add the email address of the person you wish to suppress.
6. Select ****Add Email Address**** again in order to finish manually suppressing the profile.
   ![Modal to manually add a profile to the suppression list](https://klaviyo.zendesk.com/hc/article_attachments/28717385807515)

### Share a global unsubscribe link with someone

1. Navigate to ****Settings > Other****.
2. Scroll down to the section labeled **Consent**.
3. Copy the global unsubscribe link, which can be used to globally suppress contacts.
4. Share this link with someone or include it in an email.

When someone then clicks the link, they can globally unsubscribe themselves from all of your future emails.

## View how a profile was suppressed

From the **List Suppressions** page you can filter profiles based on whether they unsubscribed on their own (**Unsubscribed)** or were added manually (**Manually Added**).

Reasons why you'll see contacts on your suppression list include the following:

- The person unsubscribed
- The person marked an email of yours as spam
- Emails to this person hard bounced or soft bounced
- You or someone else on your account manually added them to the suppression list

![Filters by reason for suppressed profile](https://klaviyo.zendesk.com/hc/article_attachments/28717385801627)

You can also see the reason for a suppression on the **Details** tab of a profile. By expanding the channel you are interested in, you can see information about when and how someone became subscribed and the reason the profile is suppressed.

![Expanded channel showing suppression reason](https://klaviyo.zendesk.com/hc/article_attachments/28717379613083)

Unsubscribed and spam complaints are not displayed as a suppression reason in thissection. If these suppressions exist, the profile will always have an unsubscribed consent status.

![Unsubscribed status for email](https://klaviyo.zendesk.com/hc/article_attachments/28717385830299)

## Unsubscribe vs. update email preferences

In all of your emails, we recommend also including a direct link to update email preferences in addition to an unsubscribe link. This is a separate link — generated by the manage preferences tag, {% manage\_preferences %} — that will take the recipient to a page where preferences can be updated.

When someone attempts to unsubscribe, it's possible that they may actually just want to receive fewer emails from you. By allowing your subscribers to choose how often they'd like to hear from you, you can lower unsubscribe rates.

While it isn't possible to turn an unsubscribe page into a preferences form, you can add an update preferences link to your unsubscribe page — we support the same manage preferences tag syntax in the text box on this page. This way, you may stop some would-be-unsubscribers from unsubscribing completely.

## When someone unsubscribes and re-subscribes

Whenever someone unsubscribes from your emails or is suppressed for deliverability reasons (i.e., an email hard bounced or is invalid), they become [globally suppressed](https://help.klaviyo.com/hc/en-us/articles/115005246108) and unable to receive marketing emails in Klaviyo. This is because when contacts choose to unsubscribe from one of your emails, they typically expect to unsubscribe from all of them.

A contact can resubscribe by:

- Filling out a Klaviyo signup form or subscribe page
- Filling out a form built using Klaviyo’s [subscribe endpoint](https://developers.klaviyo.com/en/reference/subscribe_profiles) (either a third-party form, or a form built by your developers)
- Uploading a CSV file with email consent

If a contact who was suppressed for deliverability reasons (i.e., hard bounces or invalid emails) resubscribes, the deliverability suppressions will remain. However, if they just unsubscribed, resubscribing will update their subscription status and allow them to receive emails again.

Note the following:

- If someone is globally suppressed and then resubscribes to the same list they previously unsubscribed from, they will be re-added to that list.
- If someone is globally suppressed after unsubscribing from List A and then subscribes to List B, they will not be re-added to List A.
- If someone unsubscribes from an [event-based flow](https://help.klaviyo.com/hc/en-us/articles/115002774932-Getting-Started-with-Flows#types-of-flow-triggers2), then subscribes to List A, they will be added to List A and begin receiving future emails.

Note that Klaviyo does not store information from a previous email service provider (such as Mailchimp) around when a profile unsubscribed from emails sent via the previous platform. We will only track when someone unsubscribes from a Klaviyo email.

### Manually resubscribe a profile

If a former subscriber contacts you directly and asks to be resubscribed to your mailing list, you can manually unsuppress them. To do so:

1. Navigate to their profile in Klaviyo.
2. On the **Details** tab, click on the menu next to their consent indicator to see the **Resubscribe** option.

![Resubscribe option for an unsubscribed profile](https://klaviyo.zendesk.com/hc/article_attachments/28717379615003)

Note that if you resubscribe a profile, you are indicating that you have [explicit](https://help.klaviyo.com/hc/en-us/articles/4404203889947) consent to send email marketing to that recipient.

After manually resubscribing a profile, wait about 10 minutes before sending an email to them.

## SMS unsubscribes

### Manually unsubscribe an SMS number

1. Navigate to the profile you would like to unsubscribe.
2. On the **Details**tab locate the SMS channel **IMAGE**
3. Click the menu next to the consent indicator for SMS.
4. Click ****Unsubscribe****.

### Unsubscribe SMS numbers in bulk

1. Create a new CSV file for the SMS contacts you want to unsubscribe.
2. Make the CSV’s first column Phone Numbers, and fill in the phone numbers you’d like to unsubscribe using one of Klaviyo’s [accepted phone number formats](https://help.klaviyo.com/hc/en-us/articles/360046055671).
3. Include the country for each phone number using one of the following options:

- Include a second column labeled **Country** and add in the country name/abbreviation.
- Include a country code (e.g., 1 for U.S.) at the beginning of every phone number.
  ![Phone number and country headers in example file](https://klaviyo.zendesk.com/hc/article_attachments/28717385804443)
- In Klaviyo, open the dropdown under your account name.
- Click ****Settings > Other > Profile maintenance****.
- Scroll to the **Import SMS Unsubscribes** section.
- Click ****Browse Files**** and upload your CSV file of SMS contacts to unsubscribe.
  ![Browse files option to select a file for upload](https://klaviyo.zendesk.com/hc/article_attachments/28717379604507)
- Click ****Unsubscribe Phone Numbers****.
- Confirm your selection in the modal that appears.

### Manually resubscribing SMS numbers

SMS profiles that have unsubscribed can resubscribe through a signup form, by texting an opt-in keyword (e.g., UNSTOP), or through a Klaviyo user uploading a list of phone numbers and applying SMS consent.

In most cases, when someone opts out, they can resubscribe via a form, texting an opt-in keyword, etc. However, if someone used STOP to opt out, they must text UNSTOP in order to receive messages again. If you attempt to resubscribe one of these profiles through another method, consent will appear in Klaviyo, but mobile carriers will continue to block messages until the recipient texts in a resubscribe keyword.

## Additional resources

- [Understanding consent in profiles](https://help.klaviyo.com/hc/en-us/articles/360037101072)
- [Using the subscribed to list metric](https://help.klaviyo.com/hc/en-us/articles/360039666832)
- [How to upload and segment with consent](https://help.klaviyo.com/hc/en-us/articles/360043841811)
- [Guide to suppressed email profiles in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115005246108)