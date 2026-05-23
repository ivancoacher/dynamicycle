<h1>Understanding SMS and MMS quiet hours in flows</h1>

Learn about Klaviyo quiet hours for SMS and MMS flows.

By default, Klaviyo applies quiet hours using the recipient’s phone number area code for US and Canadian numbers. This prevents mobile messages from sending during restricted periods (such as 9 p.m.–8 a.m.) based on area code. When phone number area code is enabled, Klaviyo can also enforce state-level rules in the US.

For recipients outside the US and Canada, quiet hours are based on the eastern time zone in their country (for example, Australian Eastern Time in Australia, Greenwich Mean Time in the UK and Ireland).

Important: Even when the **Phone number area code** setting is selected, all international recipients are evaluated using their country’s eastern time zone—not their specific region or local time zone.

Quiet hours allow you to avoid sending your text messages during non-preferred hours of the day to your subscribers. This way, you can send SMS or MMS messages during reasonable hours of the day (not when they are sleeping or at other inconvenient times).

This also allows you to more easily comply with telemarketing laws and regulations.

## Understanding the importance of SMS and MMS quiet hours

Since text messages are typically viewed as more intrusive, it’s important to send them at legally compliant times.

Some countries (such as the US and UK) limit the hours when you can send text messages

In general, send in your recipient’s local time and avoid sending:

- Before 8 a.m.
- After 9 p.m.

Some states have stricter rules that may prohibit sending before 9 a.m. or after 8 p.m. Klaviyo’s state-level quiet hours setting helps you automatically comply with these requirements.

|  |  |
| --- | --- |
| ****Country**** | ****Quiet hours**** |
| \*United States  Canada  United Kingdom  Ireland  Germany  Netherlands  Australia  New Zealand | Before 8 a.m.  After 9 p.m. |
| \*\*France | Before 8 a.m.  After 10 p.m.  All Sundays  Public holidays |

\* For the US, most of the country is covered by the TCPA, which allows sending from 8 a.m. to 9 p.m. However, several states (such as Florida) have enacted mini-TCPAs for their state and limit sending to between 8 a.m. and 8 p.m.

\*\* Quiet hours in France are enforced by wireless carriers. This means that you may legally be allowed to send Sundays, but your messages won’t be delivered. The carriers may also decide to filter your other messages if you continue to send outside of the quiet hours.

When you’re planning to send an SMS message, consider the experience of the recipient. For example, sending a confirmation message immediately after a customer makes a purchase, or replying instantly to a text inquiry provides a great customer experience.

****Examples of messages to avoid sending during quiet hours****

You should not send any non-transactional flow messages during these “non-business” or quiet hours. Examples of these types of non-transactional messages include:

- Back in stock notifications.
- \*Welcome series messages.
  - \*An exception is the first message, which is considered a subscription confirmation unless it contains marketing content.
- Messages that include marketing content, like an order confirmation with pictures of promotions or links to other products.

We recommend that quiet hours also be used on all non-essential flows, including non-essential transactional flows (like order and shipping updates), which customers wouldn’t expect to get at odd hours.

## Quiet hours in Klaviyo

Klaviyo won't deliver messages during quiet hours for French recipients, including campaign messages. The only exception is the first message of an SMS welcome series and Shopify post-purchase flows.

Depending on your location, there are 2 options for quiet hours in Klaviyo:

- ****Use Phone number area code (****default****)****
  This bases quiet hours on the recipient’s phone number area code for US and Canadian numbers. You can also enable state-level quiet hours (US only) to automatically follow state-specific rules. For recipients outside the US and Canada, Klaviyo instead uses the eastern time zone in their country.
- ****Use eastern timezone****
  This bases quiet hours for a country on its eastern time zone (for example, Eastern Time in the US and Canada, Australian Eastern Time in Australia, Greenwich Mean Time in the UK and Ireland). Brands often use this option with extended hours (like 8 p.m.–11 a.m.) for the most conservative compliance approach.

Note: If you use the Eastern Time Zone setting, Klaviyo adjusts for Texas’s rules by limiting SMS flow messages to 11 a.m.–8 p.m. EST Monday–Saturday and 2 p.m.–8 p.m. EST on Sundays. This corresponds to the legal quiet hours of 9 a.m.–9 p.m. (Mon–Sat) and 12 p.m.–9 p.m. (Sun) in Texas, with a conservative buffer applied for compliance.

![Screenshot 2025-10-03 at 3.13.47 PM.png](https://klaviyo.zendesk.com/hc/article_attachments/41894166573851)

If you send to recipients in Alaska or Hawaii, either use quiet hours by area code or adjust the hours so that you aren’t sending between 8 p.m. and 2 p.m. ET.

Learn [how to change your quiet hour settings](https://help.klaviyo.com/hc/en-us/articles/22711363273627).

****Should I use phone number area code or eastern time zone?****

- ****Phone number area code****
  Best for most brands. It aligns with industry best practice, gives you the widest available sending hours, and allows you to enable state-level quiet hours in the US for added compliance.
- ****Eastern time zone.****
  The most conservative option. It uses the eastern time zone in each country (e.g., Eastern Time in the US and Canada). This minimizes risk if subscribers are traveling or if their area code doesn’t reflect their current location, but reduces available sending hours (often 8 p.m.–11 a.m.). The 8 p.m.–11 a.m. ET quiet hours window lines up as 5 p.m.-8 a.m. PT, thus providing the broadest coverage to comply with US laws.

****What happens if I use area codes and have subscribers outside the US and Canada?****

If you’re using quiet hours based on area codes, it will only be used for recipients in the US and Canada.

For subscribers in other countries, quiet hours will be according to set time zones.

### Transactional messages

By default, messages marked as transactional do not have quiet hours enabled. If you want to use quiet hours, you can enable this setting for any transactional message.

For France, quiet hours do not apply to transactional messages or the first message in an [SMS welcome flow](https://help.klaviyo.com/hc/en-us/articles/360036122291); however, this only applies if your flow uses the **Subscribed to SMS Marketing** metric as a trigger.

### Keyword auto-replies

Quiet hours do not apply to messages that involve Klaviyo default keyword auto-replies (e.g., the message that is sent automatically when someone texts Yes, Stop, Help, etc.).

For any [custom subscribe keyword](https://help.klaviyo.com/hc/en-us/articles/360050384091), quiet hours do apply.

### Smart Sending

Quiet hours differ from [Smart Sending](https://help.klaviyo.com/hc/en-us/articles/115002779311), but your quiet hours settings might affect Smart Sending.

Both quiet hours and Smart Sending are checked at send time, not the time you scheduled the message. However, quiet hours are checked before Smart Sending.

For example, say someone just received a text message. Then, they get triggered for another SMS during quiet hours. In this case, Klaviyo:

1. Checks that the message falls during quiet hours.
2. Delays the message until quiet hours are over.
3. Once quiet hours are over, checks the Smart Sending window.

- If enough time has passed (i.e., the message falls outside the Smart Sending window), Klaviyo sends the message.
- If not enough time has passed, Klaviyo skips the message.

### Daylight savings hours changes

Daylight savings time (DST) applies for each respective region and country as it occurs.

For example, if you are sending to recipients in the US, starting the second Sunday in March at 2 a.m., Klaviyo automatically switches to EDT, and starting the first Sunday of November will switch to using EST. Thus, Klaviyo will match the correct local time in accordance with daylight savings time.

You can see these changes in your SMS settings as they update.

## Enable or disable quiet hours for a flow message

To turn off quiet hours for a particular SMS or MMS:

1. Click on the SMS message in the flow.
2. In the details panel, scroll down to the **Settings** section.
3. Click the checkbox next to **Enable SMS quiet hours**.
   ![MMS1.jpg](https://klaviyo.zendesk.com/hc/article_attachments/38062456845211)
4. Click ****Save**** at the bottom of the details panel.

- You can always change your global SMS quiet hours settings by clicking ****SMS settings****.

Quiet hours are checked at message send time. For example, say you have quiet hours enabled so messages can only send between 11 a.m. and 8 p.m. If at 7:05 p.m., you change the quiet hours to start at 7 p.m., any messages that were about to go out will now wait until 11 a.m. the next morning.

### What happens when a recipient cannot be sent to yet

When quiet hours is enabled and the flow is live, any message scheduled to go out during quiet hours will wait to send.

Recipients go into the **Waiting** queue and their message will wait to send until the next available sending time. While in this queue, recipients pause their journey in the flow (i.e., they don’t move past the SMS to any following splits, time delays, emails, etc.).

Once quiet hours are over, the flow sends the SMS or MMS to the recipient, removes them from the **Waiting** queue, and allows them to continue in the flow.

The quiet hours setting is checked at message send time. If flow filters are being used, those will be checked and applied once the SMS message has been sent. More information on flow behaviors can be found our [guide on understanding how contacts move through a flow](https://help.klaviyo.com/hc/en-us/articles/360017706091).

## View recipients waiting due to quiet hours

In the left-hand sidebar for a flow message, you will see an **Analytics (Last 30 Days)** section. The line for **Waiting** activity will display how many recipients are waiting to receive this message.

If you click on this line, it will take you to the message’s ****Recipient Activity**** tab with the Waiting section automatically open. This section will show the number of people waiting to receive the message during their preferable hours that do not fall during quiet hours.

If you try to force a recipient through the **Waiting** queue by clicking ****Send Now**** or back-populating, quiet hours will still apply.
