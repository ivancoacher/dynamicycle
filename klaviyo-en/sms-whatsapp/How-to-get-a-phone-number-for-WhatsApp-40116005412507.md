---
id: "40116005412507"
title: "How to get a phone number for WhatsApp"
source_url: "https://help.klaviyo.com/hc/en-us/articles/40116005412507-How-to-get-a-phone-number-for-WhatsApp"
section: "Getting started with WhatsApp"
category: "WhatsApp"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-20T16:50:23Z"
language: "en"
---
Find out where and how to get a phone number to use for WhatsApp. There are a few options for how you can do this:

- Using an existing phone number (like your customer support number).
- Receiving a number from Meta.
- Purchasing a number from a provider like Twilio or Infobip.

****Can I get a phone number from Klaviyo?****

Unfortunately, Klaviyo cannot provide you with a number for WhatsApp. You also cannot use your SMS sending number from Klaviyo, since WhatsApp requires that the phone number be able to receive calls.

## WhatsApp phone number requirements

Before we go into how to pick your number, let’s cover WhatsApp’s phone number requirements. The phone number must be:

- Owned by you or your business.
- Able to receive phone calls or text messages.
- Ready to receive verification code when you’re setting up your account.
  - This includes being able to receive international calls or texts during the registration process.
- Not connected to any other WhatsApp service:
  - Example: the number cannot be connected to a personal WhatsApp account or the WhatsApp Business Platform.
- Not a short code.

## Which option should I pick?

There’s 3 options to choose from, and what’s best depends on your business needs. You can:

- Use an existing phone number.
- Request a phone number from Meta.
- Purchase a phone number from a third party.

### Use an existing phone number

This approach is the quickest and uses a phone number you’re already paying for, so there’s no extra cost. The only caveat is a WhatsApp number can only be active with one WhatsApp provider at a time. However, you can migrate that number from one provider to another using the set up workflow in Klaviyo.

To use an existing phone number, you can follow the [instructions for connecting Klaviyo to WhatsApp](https://help.klaviyo.com/hc/en-us/articles/40111819732635). Simply make sure you select the option to ****Add a new or existing phone number**** and then verify the number.

![image (3).png](https://klaviyo.zendesk.com/hc/article_attachments/40650266161435)

### Request a phone number from Meta

The phone number is free, but it takes up to 5 business days while Meta verifies your business.

If you request a Meta phone number, note that it cannot be:

- Migrated to another WhatsApp Business Account.
- Used outside of the WhatsApp Business platform
- Used for Click-to-WhatsApp ads or buttons.

To request a phone number from Meta, simply select this option when [connecting your Klaviyo account to WhatsApp](https://help.klaviyo.com/hc/en-us/articles/40111819732635).

### Purchase a phone number from another provider

You can buy a phone number from a provider, such as Infobip or Twilio.

Please note that the time it takes to acquire a phone number can vary. Some countries require that you register phone numbers, a process that may take several business days. If this happens with your number, you may need to submit certain information or to complete the registration process before you can set up WhatsApp with the number.

### Infobip

To [buy a number from Infobip](https://www.infobip.com/docs/numbers/getting-started):

1. Log in to your Infobip account.
2. Navigate to ****Channel and Numbers > Numbers****.
4. Select ****Buy Number****.
5. Pick the country for your phone number (typically, this is the country where your business is headquartered).
6. Click ****Next****.
7. For the number capabilities, choose at least ****SMS**** and ****Voice****.
8. Click ****Next****.
9. Choose the type of number you want (e.g., virtual long code).

   - Depending on which number and country you picked, you may need to provide additional information. For instance, you must register a 10-digit long code (10 DLC) in the United States.
10. Click ****Next****.
11. Review the offered phone numbers and select the one you want.
13. Continue the steps to submit additional information (if required) and to purchase the number.

    Once your number is ready in Infobip, you can get the verification code:
14. During the WhatsApp phone number confirmation step in Klaviyo, choose to get the verification code by text message.
15. Log in to Infobip.
16. Check the ****analyze logs**** for the code.

- Note that it may take a few minutes for the code to appear.

### Twilio

#### Buy a number

To [buy a number from Twilio](https://help.twilio.com/articles/223135247-How-to-Search-for-and-Buy-a-Twilio-Phone-Number-from-Console),

1. Log in to your Twilio console.
2. Navigate to ****Develop > Phone Numbers > Manage > Buy a Number****.
3. Select the country for your phone number (typically, this is the country where your business is headquartered).
4. Under **Capabilities**, select at least both ****Voice**** and ****SMS****.
6. If desired, add other criteria, such as area code.
7. Click ****Search****.
8. Find the number you want, and then click ****Buy****.

#### Configure your phone number

Next, you must configure the phone number so that WhatsApp can verify it. To do so:

1. Navigate to the **Active Numbers** page in Twilio.
2. Select the number you want to use for WhatsApp.
3. Scroll down to the **Voice & Fax** section.
4. Open up the ****Configure with**** dropdown menu.
5. From the dropdown, click ****Webhook, TwiML Bin, Function, Studio Flow, Proxy Service****.
6. Edit the **Webhook URL** and use the ****Voicemail Trimlet**** to send voicemails to your email address:
7. <https://twimlets.com/voicemail?Email=>[YOUR EMAIL ADDRESS]
8. Select ****Save****.

## Next steps

[Connect your WhatsApp Business account to Klaviyo](https://help.klaviyo.com/hc/en-us/articles/40111819732635)

[Verify your WhatsApp Business account](https://help.klaviyo.com/hc/en-us/articles/40116148219163)

[Import WhatsApp consent into Klaviyo](https://help.klaviyo.com/hc/en-us/articles/40116243735579)