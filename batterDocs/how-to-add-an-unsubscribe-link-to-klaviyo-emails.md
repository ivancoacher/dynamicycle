<h1>How to add an unsubscribe link to Klaviyo emails</h1>

## You will learn

Find out how to include an unsubscribe link in your Klaviyo email campaigns and flows.

## The importance of including an unsubscribe link

Klaviyo requires an unsubscribe link to be present in all emails. Why?

For one, it's the law. The [CAN-SPAM Act](https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business) requires that all commercial emails "must include a clear and conspicuous explanation of how the recipient can opt out of getting email from you in the future." You also must honor a recipient’s opt-out request within 10 business days.

Including an unsubscribe link is critical to maintaining a strong sender reputation. If you don't allow recipients to opt out and decide if/when they want to stop receiving your emails, they are more likely to mark your email as spam through their inbox service. Spam complaints are serious and can significantly damage your email deliverability. If your abuse rate hits even 0.1%, mailbox providers (like Gmail, Hotmail, and Yahoo) will start to consider you a "bad sender" and take matters into their own hands, filtering your emails as spam for all recipients.

### What if I forget?

If Klaviyo doesn't detect an unsubscribe tag in one of your emails, it will automatically add an unsubscribe link at the bottom of your email that includes a basic unsubscribe tag.

![The default unsubscribe footer](https://klaviyo.zendesk.com/hc/article_attachments/28720656374299)

## Add an unsubscribe link

By default, the basic tag will generate a link with the text "Unsubscribe."

1. Navigate to your email template.
2. Select an existing text block or add a new one into your email.
3. Double-click into the block to open the text editing menu.
4. Click the personalization icon in the text editing menu.
5. From the ****All types**** menu, select ****Links and preview****.
6. Select ****Unsubscribe****.

![The Unsubscribe menu option](https://klaviyo.zendesk.com/hc/article_attachments/28720668168859)

When a recipient clicks a Klaviyo unsubscribe link, they will be taken to a confirmation page to confirm the unsubscribe request.

## Style the unsubscribe link

You can style the text for an unsubscribe however you'd like inside of the text editor. Note that the tags below are supported for all emails sent through Klaviyo (i.e., those built with the drag-and-drop editor, text-only emails, and custom HTML emails).

To customize the text for the generated link:

1. Insert the tag: `{% unsubscribe %}`
2. Add two single quotation marks after **unsubscribe** with the text you want: `{% unsubscribe 'YOUR UNSUBSCRIBE TEXT' %}`

### Troubleshooting a broken unsubscribe link

If you use the default `{% unsubscribe %}` tag in a button or as the **URL** for a text link, it will break. This is because the default unsubscribe tag generates a full HTML link, not just a URL.

![A broken unsubscribe link](https://klaviyo.zendesk.com/hc/article_attachments/30007938335387)

If this happens, use the following tag instead: `{% unsubscribe_link %}`

This tag provides more control than the default tag, as it generates just the unsubscribe URL. To use it:

- Add it to the **URL** field when hyperlinking text.
  ![The URL field](https://klaviyo.zendesk.com/hc/article_attachments/30007938339611)
- Add it to a button block's **Link address** field.
  ![A button block's Link address field](https://klaviyo.zendesk.com/hc/article_attachments/30007938342939)
- Using custom HTML, place the unsubscribe tag within <a href></a> tags:`<a href ="{% unsubscribe_link %}" style="color: red;">Unsubscribe here.</a>`

## Add one-click unsubscribe to meet Yahoo and Google sender requirements

There is no action you need to take to meet Google and Yahoo’s one-click unsubscribe requirement for bulk senders. Klaviyo automatically adds code to the header of every email you send to enable one-click unsubscribes for supported inboxes. Learn more about [Yahoo and Google’s email sender requirements](https://academy.klaviyo.com/2024-new-sender-requirements-checklist/1817230).

## Unsubscribe link best practices

It’s best practice to make your unsubscribe link visible and easily accessible. Making it easy to unsubscribe can reduce customer frustration, and is a requirement for many inbox providers.

Follow these best practices to ensure your unsubscribe link is easy to find:

- Use colors that [meet accessibility standards](https://help.klaviyo.com/hc/en-us/articles/360034711931). Ensure there is high contrast between the text and background color.
  ![Examples of email footers with good and bad accessibility in terms of color choice](https://klaviyo.zendesk.com/hc/article_attachments/28720668162459)
- Don’t use a font size that is substantially smaller than the surrounding text.
- Don’t bury your unsubscribe link in a long sentence, or change the hyperlinked word to something hard to scan.
  ![Examples of email footers with easy and hard to find unsubscribe buttons](https://klaviyo.zendesk.com/hc/article_attachments/28720656365083)
- Use a link color that stands out from the rest of your text. Don’t manually change the link color so it blends in and is hard to read.

![Examples of email footers with easy to spot and camoflaged unsubscribe buttons](https://klaviyo.zendesk.com/hc/article_attachments/28720656366875)
