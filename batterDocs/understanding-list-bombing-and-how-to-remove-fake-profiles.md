<h1>Understanding list bombing and how to remove fake profiles</h1>

## You will learn

Learn about list bombing attacks and how you can remove fake email addresses to protect your lists. List bombing attacks fill your account with fake profiles, and can harm your sender reputation, data, and more.

## What is list bombing?

List bombing is a malicious attack where the attacker exploits a signup form or checkout page by making a large number of fake submissions, filling the associated list with emails and phone numbers that have not consented or are invalid. While an increase in email subscribers may initially seem like a good thing for your brand, this is only true if all the new leads are legitimate.

If you send to fake profiles created through a list bombing attack, it can negatively impact your deliverability in the following ways:

- Higher hard bounce rates
- Higher spam complaints
- Lower open rates
- Negative impact to sender reputation
- Potential spam trap hits
- Potential blocklisting resulting in blocked email traffic

  Not all profiles submitted as part of a list bombing attack are fake email addresses. Bots can fill out forms with real email addresses, and profiles of people who have no knowledge of this are being added to marketing lists. When a company sends emails to mass amounts of profiles submitted by bots, many of them mark the email as spam.

  These are a few of the most commonly targeted forms that bots target. Keep in mind this is not an all inclusive list; bots can submit profiles anywhere there is an unprotected form:
- ****Ecommerce checkouts****
  Bots have been observed, especially for customers using an ecommerce platform (such as Shopify). The bots can start a checkout and abandon it using a real person’s email, and the event will sync to Klaviyo.
- ****Home page footer form****
  Footer forms on a home page that collects email addresses and no other information has been a specific target of bots to sign up emails.
- ****Coupon codes (“$$OFF”, or “%OFF”) on the home page****
  Bots target these forms specifically to get coupon codes which they later put on coupon / promo code websites to drive website visits to those pages.
- ****Forms without captcha****
  Forms without captchas are susceptible to bots filling them out.
- ****API****
  Bots submitted by 3rd party forms and synced to Klaviyo through our public API.

## How to identify a list bombing attack

The first indicator of list bombing is if you've experienced a sudden spike in new subscribers. This is particularly true if you haven't planned any list growth campaigns, so there is nothing to tie this spike to. If this happens, examine the recent email subscribers, looking out for the following trends:

- The emails all came in through a single point of entry (e.g., same signup form)
- There was a specific timeframe in which the influx of emails was captured
- All the emails are from the same domain (e.g., all are from @phish.com)
- The contacts have unconventional first and last names
- All submissions are from the same IP source

## How do you protect against list bombing?

### CAPTCHA in forms

CAPTCHA is a tool that requires form submitters to complete a short task to verify that they are a real person and not a bot. When Klaviyo detects suspicious behavior or historical bot activity from a user’s IP address, they will be prompted to solve a CAPTCHA.

![Example reCAPTCHA](https://klaviyo.zendesk.com/hc/article_attachments/28720900531227)

This functionality is automatically enabled for forms that collect email or SMS leads, or utilize a coupon code. Additionally, only users that have had suspicious activity will be prompted to complete the CAPTCHA.

The user must successfully complete the CAPTCHA in order to see their coupon code and submit the form.

### Double opt-in

[Double opt-in](https://help.klaviyo.com/hc/en-us/articles/115005251108) is a process through which a new subscriber must confirm their subscription before being subscribed to a given list. It is the same for both email and SMS subscribers, and is on by default in Klaviyo.

When double opt-in is enabled, new subscribers will receive a confirmation message immediately after signing up. This message will prompt them to confirm their subscription. Only subscribers who confirm their subscription will be successfully added to the list, making it harder for malicious actors to list bomb.

### List bombing IP management

Klaviyo has a system in place to prevent list bombing called the List Bombing IP Management. The purpose of this system is to flag or block specific IP addresses that are making a large number of form submissions or [subscribe API](https://developers.klaviyo.com/en/reference/subscribe_profiles) calls within a short period of time. If you are being list bombed, this system would block IP addresses with a large number of initial subscribe requests to protect your account from further profile subscriptions.

Note that the IP blocking only occurs after the attack has already started to protect your account from further harm. This method of list bombing mitigation cannot prevent an attack entirely.

### Honeypot form field

This method requires a developer and access to the form’s HTML. If your forms are built through Klaviyo’s form editor, consider creating a custom form.

Adding a “honeypot” field to a website’s form is a method you can implement to easily identify if you are being list bombed. If you are using a custom, non-Klaviyo form, you can place a hidden field that is invisible on the front-end. If the form is submitted with a value set for the honeypot field, you can attribute the submission to a bot rather than a human user.

Make sure that your honeypot [adds a custom property](https://help.klaviyo.com/hc/en-us/articles/115005080127) to Klaviyo that you do not plan on using anywhere else. This allows you to use the honeypot field’s custom property to identify profiles submitted by a bot with segmentation in Klaviyo:

![Example honeypot segment](https://klaviyo.zendesk.com/hc/article_attachments/28720895209243)

For instructions on how to create a honeypot field, we recommend reading the following resource:

- [How to create a simple Honeypot protect your Forms against Spammers](https://dev.to/felipperegazio/how-to-create-a-simple-honeypot-to-protect-your-web-forms-from-spammers--25n8)

## What to do if you experience list bombing

If you experience list bombing, the next thing you should do is clean out the profiles that were created. Based on the trends that you notice with the new subscriptions, take the data points and create a segment to help pull in all the emails that were submitted during the attack.

A segment you can use to identify profiles that are likely submitted as part of a list bombing attempt is:

- If someone can or cannot receive marketing > Person **can receive email marketing**
  AND
- What someone has done > Person has **Received Email** is at least 3 in the last 180 days
  AND
- What someone has done > Person has **Opened Email** 0 times over all time
  AND
- What someone has done > Person has **Clicked Email** 0 times over all time
  AND
- What someone has done > Person has **Placed Order** 0 times over all time

Once the segment is created, [suppress the profiles](https://help.klaviyo.com/hc/en-us/articles/115005073867) so they cannot receive any sends from you.

If you have questions on building a segment that captures profiles created through a list bombing attack, reach out to our [Support Team](https://help.klaviyo.com/hc/en-us/articles/115001002272-How-to-Contact-Support).

It is also best practice to re-enable double opt-in on your lists if you have fallen victim to a list bombing attack. Once a brand has been targeted, it is more likely that they'll be targeted again in the future. By securing your forms through double opt-in, you can prevent future attacks.
