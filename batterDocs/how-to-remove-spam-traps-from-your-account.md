<h1>How to remove spam traps from your account</h1>

## You will learn

Learn how to remove spam traps from your account, and why this is important.

[Spam traps](https://klaviyo.zendesk.com/hc/en-us/articles/360003019251) are fake email addresses that live on the web for the purpose of finding people who may be illegitimately acquiring contacts. By definition, a spam trap address should never engage, nor sign up for anything. They are just inboxes that are set up for Mailbox Providers (MBP) to flag your domain if you send to them. Spam traps can end up in your database if you import an extremely old list (2 years old or greater). As the age of the addresses increases the risk of importing spam traps increase.

Eliminating your risk of sending to spam traps will increase your likelihood of reaching the inbox, leading to more opens, clicks, and ultimately, more money. Klaviyo leverages this fact to identify any spam traps on your list or any other profiles in your account that have never engaged with your brand.

## Why you should remove spam traps

Sending to spam traps will cause [deliverability](https://klaviyo.zendesk.com/hc/en-us/articles/115005247008) issues. The first and foremost issue is that emailing spam traps is what triggers blocklistings. If you are blocklisted by one of the major providers then you will have your mail outright rejected (and this can also affect other Klaviyo customers).

The second issue comes by repeatedly emailing unengaged recipients. Doing so will cause MBPs (e.g., Hotmail, Gmail, Outlook, etc.) to re-evaluate where mail from your domain is placed (the inbox, or Junk/Spam folder). If you send many messages to the same addresses and they never engage with that mail from your brand, MBPs will take that as a sign that they do not want to receive your emails and will likely route them to the Junk/Spam folder. In the most extreme cases, they may start to block messages from your domain outright with a bounce reason mentioning that your brand sends "unsolicited mail".

Moreover, filtering companies use spam traps to identify which emails they should place in the spam/junk folder. In their eyes, it’s a sign that you are not obtaining emails legitimately or following email best practices. Even worse, sending to spam traps can lead to Klaviyo IPs being blocklisted, which leads to deliverability issues on our infrastructure, ultimately impacting Klaviyo’s other customers who are making an effort to implement best practices.

## Identify spam traps

It's impossible to identify the specific email addresses that are spam traps because this information is not publicized. MBPs know that if they publish the locations of their traps then bad actors will take steps to avoid them by filtering spam traps out, making them useless. Therefore, you must gather a segment of the profiles that have never shown any signs of engagement. This segment will contain any potential spam traps in your list. To do so, [create a segment of anyone who has never engaged with your brand](https://help.klaviyo.com/hc/en-us/articles/360044054732#h_01JEREANGCF07WNS6CSNF2MRSS).

![Button to create a never engaged segment on the action center](https://klaviyo.zendesk.com/hc/article_attachments/32674026136091)

Since we know that spam traps aren't real people, there are some things they simply cannot do. A spam trap will never open or click an email, start a checkout, or place an order, fill out lead ads, open support tickets, leave product reviews, or forget their password because these events require human action. Use the segment above as a foundation, and add any data pertinent to your business that require human interaction.

If you are new to Klaviyo, there may not be as much available data. However, if you sent emails on an ESP that Klaviyo integrates with prior to joining us, you can leverage this data when creating an unengaged segment. For instance, the segment conditions below show a Klaviyo account that is integrated with their prior Email Service Provider, Mailchimp:

![Spam trap segment with Mailchimp conditions](https://klaviyo.zendesk.com/hc/article_attachments/29720581141275)

Notice that, in the segment above, someone has to have received at least 10 Mailchimp emails but only 1 Klaviyo email. This would be a good way to find inactive profiles if you are a new sender on Klaviyo, but have existing open/click data from your former ESP.

Most likely, you will primarily utilize Klaviyo data, integration data, and any data from other custom properties you have uploaded into your account. For instance, there may be some individual profile data that you’ve uploaded into Klaviyo that could reference an action someone has done. If you have this available, you can also use this information to weed out profiles that couldn't perform a human action. An example may look like the segment below.

## How to remove spam traps

Once you identify the problematic segment of contacts, the next step in removing spam traps from your account is to suppress them. To suppress these contacts, following the steps below:

1. Go to [Lists & Segments](https://www.klaviyo.com/lists) in Klaviyo
2. Click the three dots next to the segment you wish to suppress
3. Click ****Suppress current members****

## Additional resources

- [What is a spam trap](https://klaviyo.zendesk.com/hc/en-us/articles/360003019251)
- [Guide to list cleaning](https://klaviyo.zendesk.com/hc/en-us/articles/115005078347)
- [Introduction to email deliverability](https://klaviyo.zendesk.com/hc/en-us/articles/115005247008)
