<h1>Understanding bounced emails in Klaviyo</h1>

## You will learn

Learn about the reasons that emails can bounce, as well as how to view and suppress bounces in Klaviyo.

A "bounce" occurs when an email is either not successfully delivered or is rejected by the recipient's inbox provider. If your account has a high number of bounces, this can have a negative impact on your deliverability rate.

There are two types of bounces:

- A ****hard bounce**** occurs when an email cannot be delivered due to a permanent reason. This could be caused by a variety of reasons, including a misspelled email. Klaviyo automatically suppresses any email address that hard bounces.

The **Dropped email** event will also be considered a bounce suppression.

- A ****soft bounce**** is always caused by a temporary reason, such as when a recipient's inbox is full or when their email server is momentarily down. If an email soft bounces more than 7 consecutive times, Klaviyo will suppress this address. Only soft bounces within the past 2 years are considered for this count.

Once a profile is suppressed due to a hard bounce or 7 consecutive soft bounces, they will automatically be removed from any lists they are on.

## Why emails bounce

There are several possible reasons why an email address may hard or soft bounce, including:

- ****Content****
  Occurs when mailbox providers detect content in emails that are consistent with other messages that were classified as spam or malicious.
- ****Message length****
  Indicates that the per-message length limit has been exceeded to deliver.
- ****Message size****
  Indicates that the message is larger than the per-message size limit to deliver.
- ****Frequency or volume too high****
  Indicates the mailbox provider is unable or unwilling to process the number of messages you’re trying to send because of the large volume.
- ****Invalid address****
  Indicates that you attempted to send a message to an address that does not exist. The contact could have provided a false address or made a typo in the address. If you are unsure, you can try correcting the email address and sending a one-off email. If the email still bounces, this address should remain suppressed.
- ****Invalid sender address****
  Occurs when your sender email address is misspelled or does not exist.
- ****Reputation****
  Occurs when the mailbox provider determines you have a poor sender reputation.
- ****Mailbox unavailable****
  A broad classification indicating that there was a problem delivering the message to the inbox. This could be because of reasons including the recipient’s mailbox being full, a temporary auto-reply setup, or an error with the recipient’s mail server.
- ****Technical****
  Can occur for a variety of reasons such as missing DNS records or authentication problems.
- ****Unclassified****
  The mailbox provider returned an ambiguous rejection message.

## Viewing hard bounce and soft bounce metrics

### Deliverability hub

The [deliverability hub](https://help.klaviyo.com/hc/en-us/articles/18378819907995) in Klaviyo is a centralized space that allows you to analyze and diagnose your email deliverability health at the account level. To access the page, navigate to the **Deliverability** tab under **Analytics**.

The **Bounce details** page on the deliverability hub provides information around why your sends are bouncing. If you are seeing issues with bounces, you can analyze this data to take corrective action and improve your overall email deliverability.

The **Bounce details** page has two main sections:

### Top bounce categories

The Top bounce categories card provides information about the types of bounces you are experiencing.

The card features a heatmap that shows:

- All 10 bounce categories.
- The 5 inbox providers with the most send volume.

![bounce_heatmap.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28723506557467)

Each box on the heat map will show the count of bounces for the corresponding category and inbox provider. The color of the box is based on the percentage of total messages sent in the chosen time period.

In the top right corner is a toggle between the heatmap view and the line graph view. The line graph shows the following information:

- Date range
- Bounce count

### Bounce report

The **Bounce report** card shows a further breakdown of the bounces on your account.

The report shows the:

- ****Count****
  The number of bounces for the respective category and the percentage of the total number of bounces.
- ****Type****
  Hard or soft bounce.
- ****Inbox provider/email domain****
  The inbox provider experiencing the bounces.
- ****Category****
  The bounce category.
- ****Definition****
  A definition explaining the reason for the bounce.

![bounce_report.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28723506559259)

### Segments

You can use segments to identify profiles that have hard or soft bounced as well:

![Klaviyo segment showing conditions to identify all profiles that hard bounced](https://klaviyo.zendesk.com/hc/article_attachments/28723506550043)

### Profiles

If you want to see what type of bounce a customer experienced, click into the customer profile and search for the bounced email event. You can click on the timestamp for the event on the right-hand side and see whether the bounce recorded is hard or soft.

### Campaigns and flows

You can also see bounce information on the **Recipient activity** tab for sent campaigns. On the **Bounced**section within the **Recipient activity** tab for a sent campaign, for each bounce you'll see the:

- Bounce category (the classification for the bounce reason)
- Bounce reason (the specific reason the email bounced)
- Bounce type (i.e., hard or soft)

To see overall bounces across all campaigns, view the [campaign trends report](https://www.klaviyo.com/campaigns/trends).

## Resolving bounce issues

Based on the bounce reasons you are seeing, you can take the following action:

****Content****

- Check message for link shorteners
- Make sure all links are branded
- Ensure you do not have too many images. Emails should contain a combination of images and text.

For more content best practices, see our guide on [understanding deliverability](https://help.klaviyo.com/hc/en-us/articles/115005075107).

****Message length****

- Limit the amount of scrolling a customer must do to read your message.

****Message size****

- Limit the size and number of media files within your message. We recommend an email size below 110KB.

****Frequency or volume too high****

- Make sure you have properly [ramped and warmed your sending infrastructure](https://help.klaviyo.com/hc/en-us/articles/360025945671).
- Determine which mailbox provider is returning these rejections.

- Once you have identified the affected mailbox provider, you should reduce the number of messages you are sending to that mailbox provider. This could mean trimming some unengaged recipients from your mailing list or eliminating a few of your daily sends to that mailbox provider.

- Use [batch sending](https://help.klaviyo.com/hc/en-us/articles/360050216012) to spread your messages out over a longer duration

****Invalid address****

- Validate emails with [double opt-in](https://help.klaviyo.com/hc/en-us/articles/115005251108).
- Implement a [sunset flow](https://help.klaviyo.com/hc/en-us/articles/360017518492) that will help reduce invalid address rejections by removing unengaged recipients before mailboxes become invalid
- Ensure that all [sending lists are compliant.](https://help.klaviyo.com/hc/en-us/articles/360002057172)
- [Remove or suppress unengaged profiles](https://help.klaviyo.com/hc/en-us/articles/115005078347) from your list to minimize future issues of invalid addresses bouncing at high rates.

****Invalid sender address****

- Ensure that your default sender email address in your organization account settings is properly spelled and is an existing email.

****Reputation****

- Take action to [repair your sender reputation](https://help.klaviyo.com/hc/en-us/articles/8983758025883)
- Monitor key [deliverability metrics](https://help.klaviyo.com/hc/en-us/articles/115000201131)
- Tighten [sunsetting](https://help.klaviyo.com/hc/en-us/articles/360017518492) windows
- Ensure your [domain is warmed](https://help.klaviyo.com/hc/en-us/articles/360025945671) if applicable
- Consider reducing your sending frequency

****Mailbox unavailable****

- Tighten [sunsetting](https://help.klaviyo.com/hc/en-us/articles/360017518492) windows
- Temporarily [suppress these profiles](https://help.klaviyo.com/hc/en-us/articles/115005073867)

****Technical****

- Ensure you have all the necessary DNS records in place
- Ensure you are passing [SPF, DKIM, and DMARC](https://help.klaviyo.com/hc/en-us/articles/4402601857307).
- Identify which mailbox provider is generating the bulk of these failures
  - If the problem is isolated with a mailbox provider, the problem is most likely with the mailbox provider, and no action is necessary.

****Unclassified****

When an email bounces with the reason **Unclassified**, the mailbox provider returns an ambiguous rejection message that is not associated with a specific issue. If this was a soft bounce, consider temporarily [suppressing these profiles.](https://help.klaviyo.com/hc/en-us/articles/115005073867)

## Removing bounced emails

Klaviyo will automatically suppress emails that hard bounce, and then exclude them from future emails. You can see these email addresses by clicking the ****Profiles**** tab and selecting ****View**** ****s********uppressed profiles**** in the upper right-hand corner of your account.

![View suppressed profiles button on Profiles page](https://klaviyo.zendesk.com/hc/article_attachments/28723518180251)

Then, choose ****all email**** and ****email bounce**** from the dropdowns.

![Klaviyo suppression list with filter for suppressions due to bounces](https://klaviyo.zendesk.com/hc/article_attachments/28723518177179)

If an email soft bounces more than 7 consecutive times, Klaviyo will suppress this address.

You can choose to manually suppress profiles that chronically soft bounce before they do so 7 times as well, using a [chronic soft bounce segment](https://help.klaviyo.com/hc/en-us/articles/360035312491).

## Suspicious emails in Klaviyo

When an email hard bounces at least once across the Klaviyo infrastructure, it is marked as suspicious. This means that even if they have never hard bounced in your account, they have previously hard bounced in another Klaviyo user's account.

 Suspicious emails are automatically skipped from receiving emails. This is done in an effort to preserve your sending reputation, as well as the sending reputation of other Klaviyo customers since sending to invalid addresses can negatively impact both IP and domain reputation.

 If you believe that a profile or profiles have been marked suspicious in error, please reach out to our [Support Team](https://help.klaviyo.com/hc/en-us/articles/115001002272-How-to-Contact-Support), and provide us with evidence of the email address still being valid. Typically a screenshot of an email from the said profile would be sufficient.

 Please make sure that this screenshot clearly shows the following:

- The email address that has been marked suspicious.
- The timestamp of the email address being delivered on a date after the profile was marked suspicious.

## Additional resources

- [List cleaning](https://klaviyo.zendesk.com/hc/en-us/articles/115005078347)
- [Understanding email deliverability](https://klaviyo.zendesk.com/hc/en-us/articles/115005247008)
- [KPI decrease troubleshooting](https://klaviyo.zendesk.com/hc/en-us/articles/360043802871)
