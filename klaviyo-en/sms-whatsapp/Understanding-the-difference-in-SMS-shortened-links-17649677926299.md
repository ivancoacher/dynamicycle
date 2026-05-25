---
id: "17649677926299"
title: "Understanding the difference in SMS shortened links"
source_url: "https://help.klaviyo.com/hc/en-us/articles/17649677926299-Understanding-the-difference-in-SMS-shortened-links"
section: "SMS deliverability best practices"
category: "SMS"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-21T13:54:30Z"
language: "en"
---
## You will learn

Learn about the differences between the various types of SMS shortened links: the default Klaviyo link, branded Klaviyo link, and branded custom link.

## Before you begin

There are 3 available types of SMS shortened links in Klaviyo:

- A Klaviyo link
- A branded Klaviyo link
- A branded custom link

Note that branded Klaviyo links only work for 90 days after being sent. If a recipient clicks on a link after 90 days, it will not work.

The table below shows an example of what these links might look like for a company called “James Black.”

|  |  |
| --- | --- |
| ****Link type**** | ****Example**** |
| Klaviyo link | klv3.io/382aNpW5 |
| Branded Klaviyo link | jblck.klv3.io/382aNpW5 |
| Branded custom link | sms.jamesblack.com/382aNpW5 |

Klaviyo cannot track shortened links from third parties. If you're not using a Klaviyo shortened link (i.e., disable the **Automatically shorten links** setting), then you cannot track or review clicks, conversions, or revenue that a text message generates.

To add a shortened link to a message, simply paste the link you want into the **Message content** box and do not uncheck the box labeled **Automatically shorten links**.

![Example of a Klaviyo shortened link](https://klaviyo.zendesk.com/hc/article_attachments/28711730648347)

## Branded Klaviyo link vs. branded custom link

The main advantage of using a branded subdomain or domain is is that the link shows that it's coming from your business.

****Branding****

A subdomain is like a branded prefix. It shows your brand name at the beginning, followed by what looks like a normal shortened link in Klaviyo. For example:

- Klaviyo link: [klv3.io/382aNpW5](http://klv3.io/382aNpW5)
- Branded Klaviyo link: [jblck.klv3.io/382aNpW5](http://jblck.klv3.io/382aNpW5)

Branded custom links mean links in your SMS messages look like any other link to your website. The only difference is that they are shorter than normal, not showing the specific page they are linking to.

- Normal website link: JamesBlack.com/catalog/signed-jerseys
- Branded domain: sms.jamesblack.com/xxxx

****Sender reputation****

With branded custom links, you have more control over your specific deliverability and sender reputation. These URLs have their own domain, and thus individual sender reputations.

Both regular and branded Klaviyo links use a shared domain. In general, this doesn’t have a large impact on SMS deliverability; however, if you have concerns over your deliverability or SMS sender reputation, it is recommended to request a branded custom link.

****Universal links and App Links****

[Universal links and App Links](https://klaviyo.zendesk.com/hc/en-us/articles/41701832186523-How-to-set-up-iOS-universal-links-and-Android-App-Links) are only available for text messages if you have a branded custom link.

These links direct your customers to content within your mobile app or, if the app isn't installed, to the same content on your website. Using these links in email and text messages allows you to use consistent URLs across all your marketing channels while creating a seamless experience for your customer, no matter their device.

****Character count****

Branded Klaviyo links are always longer than the default Klaviyo URL, since branded links include extra characters as well as the full Klaviyo URL.

When it comes to branded custom versus branded Klaviyo links, it depends on what you use.

Let’s look at this using the James Black example above.

- Example where the branded custom link is more characters
  - Custom: [sms.jamesblack.com](http://sms.jamesblack.com) (18 characters)
  - Klaviyo: [jblk.klv3.io](http://jblk.klv3.io) (12 characters)
- Example where the branded Klaviyo and custom links are equal
  - Custom: [sms.jamesblack.com](http://sms.jamesblack.com) (18 characters)
  - Klaviyo: [jamesblack.klv3.io](http://jblk.klv3.io) (18 characters)
- Example where the branded Klaviyo link is more characters
  - Custom: [sms.jamesblack.com](http://sms.jamesblack.com) (18 characters)
  - Klaviyo: [jamesblackSMS.klv3.io](http://jblk.klv3.io) (21 characters)

Note that the max subdomain length is 20 characters.

****Time to set up or edit****

The process of creating a branded Klaviyo link is simple and fast. They are also available as soon as you create them.

As for branded custom links, the process can take up to 14 days to complete. It is also recommended that you are familiar with the technical details of how your website is hosted (e.g., your DNS provider).

## Additional resources

- [How to create a branded shortened link for SMS](https://help.klaviyo.com/hc/en-us/articles/17649597637147)
- [Understanding and reviewing your SMS deliverability](https://help.klaviyo.com/hc/en-us/articles/1260806260849)