---
id: 50588009523227
title: "General Account Security Tips and Tricks"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/50588009523227-General-Account-Security-Tips-and-Tricks"
section: "Security"
category: "Account & billing"
category_slug: "account-billing"
klaviyo_updated: "2026-05-19T19:33:50Z"
language: en
---

## For non Admins / Owners

1. Use Strong Passwords

- Create a unique, strong password for your Klaviyo account that includes numbers, letters, symbols, and at least 12 characters.
- Never share your password with others, including your teammates or colleagues, and never reuse it across different sites.

  2. Enable Multi-Factor Authentication (MFA)
- Turn on MFA if available for your account for additional protection, and add a backup method to prevent account lockout.
- Klaviyo suggests using an authenticator app-based MFA over SMS, but any form of MFA is better than none.

  3. Beware of Phishing

  ****Klaviyo employees will never ask you for your password, MFA code, or recovery codes. Never give these out****
- Check the sender address before opening any Klaviyo-related email. We will only send you emails directly from an @[klaviyo.com](http://klaviyo.com) email address, so please double check before opening.
- Never click on suspicious links or download unknown attachments.
- Don’t enter your Klaviyo login credentials on unfamiliar websites. Always navigate to [www.klaviyo.com](http://www.klaviyo.com) directly if you’re unsure.

  4. Access Klaviyo from Trusted Devices Only
- Avoid using public/shared computers or unsecured Wi-Fi when logging in to Klaviyo.
- Always log out after your session, especially on shared devices.

  5. Promptly Report Security Issues
- If you notice suspicious emails, unexpected password prompts, or odd behavior in your Klaviyo account, reach out to [reportphishing@klaviyo.com](mailto:reportphishing@klaviyo.com) right away, and notify your IT department, security team if applicable.
  - We also advise you to change your password immediately, to prevent anyone from gaining access to your account.
- Share as much information as you can safely gather - such as the email address you received content from, the email header, or any screenshots you think are relevant.

## For Admins / Owners

1. Require Strong Authentication

- Instruct all users to create strong, unique passwords for their Klaviyo accounts.
- Enforce MFA on your Organization’s Account (Note: if you’re in a paid account, we’ve already done this for you!)
- It is recommended to enable Single Sign-On (SSO) if your organization has an Identity Provider (IdP)
  - Note: this is only available for paid plans

    2. Regularly Audit User Access
- Periodically review all users and roles in your Klaviyo account.
- Remove users who no longer need access (such as former employees, partners, marketing agencies, or contractors).
- Follow the principle of least privilege. When you're setting up [permissions](https://help.klaviyo.com/hc/en-us/articles/115005231648), give your users the smallest scope of permissions required to do their job, and no more

  Ensure you’re ****never**** sharing login credentials between multiple people - you can have as many people as you want on your Klaviyo account for free. Shared user accounts make it impossible for you to tell who took an action in your account, and also makes it harder for Klaviyo to detect if someone is accessing your account who shouldn’t.

  3. Monitor Account Activity
- Validate the users and roles in the account, check to see if there are any new users that appear unfamiliar.

  4. Manage Integrations and API Keys Carefully
- Restrict who can create or manage API keys and integrations by assigning the appropriate user role.
- Migrate API Keys to OAuth when possible
- Rotate API keys in your account regularly. This means periodically generating new keys to replace your old ones, and deleting the old ones, enhancing security by limiting the potential damage if a key is compromised.
  - ****Tip:**** You can do this easily within Klaviyo by [cloning your existing API key](https://help.klaviyo.com/hc/en-us/articles/115005062267#h_01HWR57G5STR2SW10YW0VBNEFQ) for easy replacement. Limit each integration’s access to only the data it needs.

    5. Keep Contact and Recovery Information Up to Date
- Ensure your organization's admin contact info on file with Klaviyo is always current to support account recovery in emergencies.

  6. Stay Informed
- Monitor Klaviyo’s status [page](https://status.klaviyo.com/), [blog](https://www.klaviyo.com/blog), and [trust center](https://www.klaviyo.com/trust) for important updates or security advisories.
- Adapt your practices as new security features or threats emerge.