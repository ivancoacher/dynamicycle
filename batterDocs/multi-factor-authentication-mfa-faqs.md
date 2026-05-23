<h1>Multi-factor authentication (MFA) FAQs</h1>

Get answers to frequently asked questions about multi-factor authentication (MFA).

## Where do I get my MFA code?

It depends on whether you set up MFA via SMS or an authenticator app:

- SMS: your code is texted to your phone number.
  - If you change your phone number, you must disable and set up MFA again.
- Authenticator app: your code in the app, whether that’s on your desktop (for a web- or browser-based app) or in an app (for a mobile app).

If both SMS and an authenticator app are set up, the code is sent to the authenticator app, as this method is considered more secure.

Once you receive the code either via text or in your app, you can enter the code into Klaviyo.

## What is the difference between a trusted device code and MFA?

In both cases, the goal of these codes is to check that you are who you say you are.

The trusted device code sends the first time you log in on a new device, whereas MFA requires a new code each time you log in.

The other key difference is where you get this code. When checking if a device should be trusted, Klaviyo sends the code via email. For MFA, the code is sent via text message or appears in your authenticator app, depending on which method you’re using.

****More about the trusted device code****

The first time you sign in on a new device, Klaviyo sends you an email with a code. This code, called the trusted device code, helps ensure that you are who you say you are, preventing anyone with your login credentials from accessing the account.

The trusted device code happens 1 time per device. Once you’ve verified your device by entering the code from your email, we won’t ask this again unless you use incognito mode or a VPN. Learn more [about trusted devices](https://help.klaviyo.com/hc/en-us/articles/360027783611) at Klaviyo.

## How can I reset my MFA?

Depending on which method you’re using, you may need to reset MFA when you change phone numbers or if you lose access to your app.

If you are currently logged in to Klaviyo, you can reset MFA yourself. Please note that if you are in a paid account, you must have 1 MFA method at all times, so you’ll need to set up another method before disabling and resetting your current one. For step-by-step instructions, see our dedicated [article on setting up MFA](https://help.klaviyo.com/hc/en-us/articles/360026617692).

If you are fully locked out of Klaviyo, see the next section.

## What do I do if I have lost my phone or backup codes?

If you are fully locked out of your Klaviyo Account due to an issue with your MFA, you can have an Admin or Owner on your account [reset your MFA for you](https://help.klaviyo.com/hc/en-us/articles/20599699660571).

If you are the sole owner or admin on the account, or the Owner and Admin are unavailable, you can also reach out to Klaviyo Support. This will require you to verify your identity and may take several days.

## What are backup codes and how do I use them?

If you downloaded backup codes when setting up MFA via an authenticator app, these codes will let you log in to Klaviyo . Please note that these codes:

- Can only be used 1 time.
- Cannot be used as a backup method for SMS MFA.

If your backup codes are not working, please make sure you:

- Are using the correct backup codes (not a set intended for a different application).
- Haven’t already used these codes before.

## Why is my account asking me to log in with MFA if I never set it up?

A few things may be at play here:

- You may have set up MFA at one point and forgotten, so check:
  - Your mobile device to see if you got a text with the code.
  - Any authenticator apps you may have on your device to see if “Klaviyo” shows up on any of them.
  - If you can’t find the code anywhere, please see the section on [resetting your MFA](#h_01JP8J20AEZ198X0A4961D0QZC).
- You’re sharing login credentials and someone else set up MFA without you knowing.
  - If this is the case, we recommend talking with your account Owner or Admin to make sure each person using Klaviyo has their own login. See how to [add users in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/360053547071).

****Why shouldn’t I share credentials?****

Sometimes it can be tempting to share a login with a teammate to get them access quicker, but this puts you and your data at more risk.

This also means that whoever set up MFA on that account now is the only person who has access to the one-time-code needed to login.

## It keeps saying my code is incorrect

A common reason for this error is that there’s a mismatch between the time used for your authenticator app and the actual UTC time.

Authenticator apps create a time-based one-time password (TOTP), which relies on UTC time to create the codes. When you’re out of town or the time on your device doesn’t align with your app, it can lead to an error saying the code is incorrect.

Try resetting your device’s timezone or test out SMS MFA as an alternative MFA option.

## Why is my SMS MFA code not sending?

Please check that:

1. You’re using the same phone number you set up SMS MFA with.
   - If you changed numbers recently or are using your work phone instead of your personal phone, it might be sending to your other device.
2. Your device has service. If your provider cannot receive text messages, then it cannot receive the SMS MFA code needed to verify your identity.
   - Double check there isn’t an outage in your area as well.
3. If you are using a VOIP or a landline, your texts likely will not arrive. Please try using a standard mobile device, or use an authenticator app as your MFA method.
   - We do not support landlines or third-party VOIP services that allow you to send and receive calls and texts over the internet.

## Additional resources

- [Ask Owner or Admin to reset MFA](https://help.klaviyo.com/hc/en-us/articles/20599699660571)
- [Set up or change your MFA method](https://help.klaviyo.com/hc/en-us/articles/360026617692)
- [Request a password reset](https://help.klaviyo.com/hc/en-us/articles/7872914223899)
