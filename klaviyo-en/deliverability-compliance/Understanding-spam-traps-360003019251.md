---
id: "360003019251"
title: "Understanding spam traps"
source_url: "https://help.klaviyo.com/hc/en-us/articles/360003019251-Understanding-spam-traps"
section: "Monitor deliverability and metrics"
category: "Deliverability & compliance"
category_slug: "deliverability-compliance"
klaviyo_updated: "2026-04-21T13:54:42Z"
language: "en"
---
## You will learn

Learn about spam traps and how to prevent sending to them, so you can protect your deliverability.

## What is a spam trap?

A spam trap is an email address used to identify senders who are not following best practices or sending unsolicited email. Spam traps are commonly used to place senders in the spam folder or worse, block all traffic to a particular inbox provider, which is why in recent years, they have become more popular and are monitored by major inbox providers.

### Pristine spam trap (PST)

Pristine spam traps are created with the intention of finding people who are sending spam or not following best practices. These emails are never used in real-world instances and are brand new addresses, so hitting a PST is likely to cause your IP to be blocklisted or your emails to go to spam. In the eyes of Inbox providers, this means that you either purchased a list or do not follow best practices since these addresses are not legitimate and do not open emails.

### Recycled spam trap (RST)

Recycled spam traps, unlike pristine spam traps, are addresses that were used as real addresses at some point in the past. It’s common to see RSTs as domains provided by free services, such as @yahoo or @gmail. However, in some cases, you may see domains of closed businesses being repurchased with the intention of making them RSTs.

An out-of-date email doesn’t always become an RST immediately after it falls out of use. Some inbox providers may delete the address after no activity — i.e. if the address stops receiving emails. Once the address is deleted, if you send to the address, the email will hard bounce. Klaviyo automatically suppresses hard bounces.

Typically, an inbox provider will leave the account deleted for 6-12 months before recycling it as a spam trap. The purpose of an RST is to identify people who are not following best practices when it comes to list cleaning, not necessarily to identify spammers.

Here is a chart that covers when an inbox provider may delete an account for inactivity:

|  |  |
| --- | --- |
| ****Domain**** | ****Time of Inactivity before Deletion**** |
| Yahoo | 12 months |
| AOL | 3 months |
| Gmail | 9 months |
| Outlook/Live/Hotmail | 12 months |

### Role accounts

Role accounts are email addresses that you want to avoid sending marketing emails to because they are not monitored by one person. Usually, these are group addresses, or aliases, that wouldn’t opt-in to receive marketing emails.

|  |  |  |  |
| --- | --- | --- | --- |
| Abuse@ | support@ | staff@ | unsubscribe@ |
| postmaster@ | admin@ | subscribe@ | info@ |
| jobs@ | noc@ | sales@ | webmaster@ |
| mailer-daemon@ | help@ | www@ | orders@ |
| No-Reply@ (or noreply@) | hostmaster@ | billing@ | marketing@ |

More details on this are outlined in [RFC 2142](https://tools.wordtothewise.com/rfc/2142).

## How to prevent sending to spam traps

Spam traps can be easily avoided by using some of the following tactics:

- Suppress profiles that have Never shown any signs of engagement. [How to create a never engaged segment](https://help.klaviyo.com/hc/en-us/articles/115005078347)
- Check out our guide on [how to remove spam traps from your account](https://help.klaviyo.com/hc/en-us/articles/360015537111-How-to-Remove-Spam-Traps-from-Your-Account)
- Use [double opt-in](https://help.klaviyo.com/hc/en-us/articles/115005251108)
- Never purchase a list of emails

## Additional resources

- [How to create a never engaged segment](https://help.klaviyo.com/hc/en-us/articles/115005078347)
- [Guide to list cleaning](https://help.klaviyo.com/hc/en-us/articles/115005078347-List-Cleaning)
- [Understanding bounced emails in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115005250408-Bounced-Emails-in-Klaviyo)
- [How to remove spam traps from your account](https://help.klaviyo.com/hc/en-us/articles/360015537111-How-to-Remove-Spam-Traps-from-Your-Account)