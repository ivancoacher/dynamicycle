<h1>How to use go-to-inbox buttons in forms</h1>

## You will learn

Learn how to streamline the email sign-up process for your subscribers. With the **Go to inbox** button action, you can direct site visitors from your form’s success step to their inbox so they can easily confirm their subscription.

## About go-to-inbox buttons

When creating a Klaviyo sign-up form or subscribe page that collects email consent, you must link it to a list so those who complete the form are added to that list. If you choose a list with [double opt-in settings](https://help.klaviyo.com/hc/en-us/articles/115005251108), then the site visitor who fills out the form must confirm their subscription via a confirmation email in their inbox before they are actually added to the list.

While you can add messaging on the form's success step reminding visitors to confirm their subscription in their email, some people may forget or get distracted and never confirm. By adding a button on the success step of your form with the **Go to inbox** action, you can make it easier for shoppers to locate the opt-in confirmation email in their inbox so they can easily complete the double opt-in journey and join your marketing list.

To include a go-to-inbox button, your form must collect email consent. Alternatively, you can use a multi-step form that collects email first and then uses a traditional SMS opt-in method. This feature is not compatible with single-step forms that collect both email and SMS consent.

![inbox1.jpg](https://klaviyo.zendesk.com/hc/article_attachments/34598575491227)

### How do they work?

When a new site visitor fills out the form on your site and lands on the success step, clicking the go-to-inbox button directs them to their email inbox. Klaviyo automatically searches and filters their inbox for the email from your sender address and with the corresponding subject line. This helps the subscriber easily locate the opt-in email to confirm their subscription, and minimizes distractions from other email messages they may have.

### When the button doesn’t appear

The go-to-inbox button only appears for email addresses from supported email service providers (ESPs). If a subscriber’s email address domain is not supported, Klaviyo automatically hides the button; however they will still receive the confirmation email. See supported providers below.

If, at any point, you [change the form’s submit list](https://help.klaviyo.com/hc/en-us/articles/360002049952#01H8PDB7M745EXVSGVWXR6Q5QA) to single opt-in, the button will also be hidden from subscribers; however, you may still see it on the form preview in the editor.

## Add a go-to-inbox button to a sign-up form

1. Select the ****Sign-up forms**** tab in Klaviyo’s left-hand navigation.
2. Open the editor for one of your existing email opt-in forms, or create a new one.

   Your form must collect email consent to include a go-to-inbox button.
3. Click ****Success**** in the top menu bar to edit the form’s success step. Note that you cannot configure go-to-inbox buttons on other form steps. Only the success step is supported.
   ![Sniper1.jpg](https://klaviyo.zendesk.com/hc/article_attachments/34598575496603)
4. Select ****Add blocks**** in the left sidebar.
5. Click and drag a new button block into your success step preview wherever you’d like it to appear.
   ![Sniper2.jpg](https://klaviyo.zendesk.com/hc/article_attachments/34598599004443)
6. In the left sidebar menu, verify that the **Action** is set to ****Go to inbox****.
   ![sniper3.jpg](https://klaviyo.zendesk.com/hc/article_attachments/34598575498779)
7. Adjust the button text and styling as needed; "Go to inbox" is the default button text. It is recommended to keep the default text or use something similar so that subscribers know what action will happen when they click on the button.
8. If you haven’t already, add text on the success step instructing subscribers to check their email and confirm their subscription (e.g., “Head to your inbox to confirm your email”). This gives additional context to the button, as well as accounts for visitors with unsupported email providers. The message should not directly reference the button, as it will not appear for everyone.
   ![sniper4.jpg](https://klaviyo.zendesk.com/hc/article_attachments/34598575500315)
9. When satisfied with your form’s appearance and functionality, click ****Publish****.

When clicked, the go-to-inbox button opens a new tab to the visitor's email platform and directs them to their inbox, which is automatically filtered to display the confirmation email.

## Add a go-to-inbox button to a subscribe page's confirmation step

You can also add go-to-inbox buttons to a subscribe page's confirmation step. To do so:

1. Navigate to the consent pages for the subscribe page you'd like to edit:
   1. To edit your account-level subscribe page, select ****Settings > Other > Consent pages****.
   2. To edit a subscribe page that's tied to a specific list, navigate to ****List & segments****, select the list, then click ****Subscribe & preference pages**** in the top menu bar.
2. On the **Email confirmation** page, click ****Edit page****.
   ![sniper9.jpg](https://klaviyo.zendesk.com/hc/article_attachments/36057747490843)
3. Select the ****Confirmation page**** step in the top menu bar.
4. Click ****Add blocks****.
5. Click and drag a **Go to inbox** button block into your confirmation page wherever you’d like it to appear.
   ![sniper10.jpg](https://klaviyo.zendesk.com/hc/article_attachments/36057758186139)
6. Adjust the button text and styling as needed; "Go to inbox" is the default button text. It is recommended to keep the default text or use something similar so that subscribers know what action will happen when they click on the button.
7. If you haven’t already, add text on the success step instructing subscribers to check their email and confirm their subscription (e.g., “Head to your inbox to confirm your email”). This gives additional context to the button, as well as accounts for visitors with unsupported email providers. The message should not directly reference the button, as it will not appear for everyone.
   ![Sniper11.jpg](https://klaviyo.zendesk.com/hc/article_attachments/36057747496091)
8. The go-to-inbox button opens a new tab to the visitor's email platform when clicked. The visitor is then directed to their inbox, which is automatically filtered to display the confirmation email.

When clicked, the go-to-inbox button directs the visitor to a new tab with their email platform open and automatically filtered to display the confirmation email.

## Supported mail providers for go-to-inbox buttons

The following email providers are supported with the **Go to inbox** button action, on both desktop and mobile devices.

- Gmail
- Yahoo Mail
- Microsoft Outlook
- Proton Mail
- iCloud Mail

If a site visitor enters an email address that doesn't contain one of the specified domains, the button will not appear on the form's success step.

Note that each ESP has different regulations that may affect Klaviyo's ability to search and filter a shopper's inbox, and they may change their rules at any time. For example, Gmail, Yahoo, and Proton allow Klaviyo to apply filters to search by subject line, sender address, and spam folder. However, Outlook Mail and iCloud do not permit filtered searches of the spam folder; therefore, Klaviyo won't be able to surface a double confirmation email if it was sent there.

To account for this, maintain a strong sender reputation so that your emails are delivered to the inbox. [Learn more about email deliverability](https://help.klaviyo.com/hc/en-us/articles/115005247008).
