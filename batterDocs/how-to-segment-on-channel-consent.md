<h1>How to segment on channel consent</h1>

## You will learn

Learn how to build segments based on whether someone is subscribed to or able to receive marketing via a particular channel (i.e., email, SMS, or push notifications).

## About marketing channel consent in Klaviyo

Consent for each marketing channel in Klaviyo is stored separately. This means someone can be subscribed to one channel, like SMS, while being unsubscribed from another channel, like email.

Additionally, consent works slightly differently for each Klaviyo channel.

- ****Email****offers 3 consent statuses (i.e., subscribed, unsubscribed, and never subscribed).
  - ****Subscribed****
    Someone who is actively opted in to receive emails.
  - ****Unsubscribed****
    Someone who indicated that they do not want to receive emails. (Includes both [global and list-specific suppressions](https://klaviyo.zendesk.com/hc/en-us/articles/115005246108).)
  - ****Never subscribed****
    Someone that can still technically receive emails, but never provided explicit consent. **Never subscribed** contacts are often added through general engagement with your site, like abandoning their cart.
- ****SMS**** offers 3 consent statuses (i.e., subscribed, unsubscribed, and never subscribed).
  - ****Subscribed****
    Someone who actively opted in to receive SMS.
  - ****Unsubscribed****
    Someone who indicated that they do not want to receive SMS.
  - ****Never subscribed****
    Someone that cannot receive SMS, but has neither subscribed nor unsubscribed. These profiles were added through [general engagement](https://help.klaviyo.com/hc/en-us/articles/115005246968) or when they consented to another marketing channel, which does not indicate consent for SMS marketing.
- ****Push notifications****
  - ****Subscribed****
    Someone who has enabled push notifications on at least one device (i.e., the profile has at least one push token that is authorized to receive push notifications).
  - ****Unsubscribed****
    Someone who has not enabled push notifications on at least one device (i.e., the profile has at least one push token that is not authorized to receive push notifications).

## Segment on channel consent

To create a segment referencing channel consent:

1. Navigate to the ****Lists & segments**** tab in Klaviyo.
2. Click the **Create New** dropdown.
3. Click ****Create segment****.
4. Add the condition ****If someone can or cannot receive marketing****
5. Choose ****can receive**** or ****cannot receive**** and select a channel.
   ![Can receive marketing segment](https://klaviyo.zendesk.com/hc/article_attachments/28716118449819)
6. Add additional filters as desired.
7. Save the segment.

In most cases, it is best to add your consent condition using an AND connector, rather than OR.

### Email marketing consent

When ****can receive > email marketing**** is selected as a condition, all profiles without an associated email address are excluded and list-only suppressions are included as active profiles. When ****cannot receive > email marketing**** is selected, all profiles without an email address are included and list-only suppressions are excluded.

### Additional filters for email consent status

To narrow a segment down to only email subscribers, follow the steps above. Then, click ****Add filter**** and select ****Because person subscribed****.

![Subscribed to email segment](https://klaviyo.zendesk.com/hc/article_attachments/28716118456475)

From here, you can click ****Add filter**** again to add additional criteria, like subscription method, subscription date, double opt-in status, and more.

![Double opt in to email](https://klaviyo.zendesk.com/hc/article_attachments/28716057653275)

Because **Never subscribed** contacts don’t have an active subscription reason or other details, you cannot add additional filters to a condition on contacts who can receive email because of general engagement.

Alternatively, choose ****cannot receive > email****, then click ****Add filter**** to add a suppression reason (e.g., unsubscribed, manually suppressed, marked as spam) and an unsubscribe method or date, if relevant.

### Additional filters for SMS consent

Click ****Add filter**** after adding an SMS consent condition to narrow your segment down based on subscribe/unsubscribe method and subscribe/unsubscribe date.

![Subscribed to SMS in the last month](https://klaviyo.zendesk.com/hc/article_attachments/28716057636635)

### Additional filters for push consent

Click ****Add filter**** after adding a push consent condition to identify push subscribers who opted in during a certain date range. This filter is only available when you select ****can receive > mobile push marketing****.

![Subscribed to push in the last 30 days](https://klaviyo.zendesk.com/hc/article_attachments/28716118447259)

## Sample segments with consent

Use these sample segments as guides and inspiration for your own.

### Engaged segment of email subscribers

****If someone can or cannot receive marketing > can receive > email marketing > Because person > subscribed****

****AND****

****What someone has done (or not done) > Opened email > at least once > in the last 30 days****

****OR****

****What someone has done (or not done) > Clicked email > at least once > in the last 30 days****

****![engaged email subscribers](https://klaviyo.zendesk.com/hc/article_attachments/28716118454427)****

### Engaged segment of everyone who can receive emails

****If someone can or cannot receive marketing > can receive > email marketing****

****AND****

****What someone has done (or not done) > Opened email > at least once > in the last 30 days****

****OR****

****What someone has done (or not done) > Clicked email > at least once > in the last 30 days****

****![engaged and can receive email](https://klaviyo.zendesk.com/hc/article_attachments/28716057642011)****

### Subscribed to both email and SMS

****If someone can or cannot receive marketing > can receive > email marketing > Because person > subscribed****

****AND****

****If someone can or cannot receive marketing > can receive > SMS marketing****

****![email plus sms subscriber](https://klaviyo.zendesk.com/hc/article_attachments/28716057675547)****

### Subscribed to email but not SMS

****If someone can or cannot receive marketing > can receive > email marketing > Because person > subscribed****

****AND****

****If someone can or cannot receive marketing > cannot receive > SMS marketing****

****![subscribed to email not sms](https://klaviyo.zendesk.com/hc/article_attachments/28716118444315)****

### Recent SMS unsubscribers

****If someone can or cannot receive marketing > cannot receive > SMS marketing > because person > unsubscribed****

![Unsubscribed from SMS](https://klaviyo.zendesk.com/hc/article_attachments/28716057646491)

## Additional resources

- [Segment conditions reference](https://klaviyo.zendesk.com/hc/en-us/articles/115005062847)
- [Segmenting with dates reference](https://help.klaviyo.com/hc/en-us/articles/4403222359451)
