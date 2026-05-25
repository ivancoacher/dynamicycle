---
id: "38938328988827"
title: "How to automatically forward support emails to Klaviyo Helpdesk"
source_url: "https://help.klaviyo.com/hc/en-us/articles/38938328988827-How-to-automatically-forward-support-emails-to-Klaviyo-Helpdesk"
section: "Foundation & Setup"
category: "Helpdesk"
category_slug: "helpdesk"
klaviyo_updated: "2026-04-29T15:54:05Z"
language: "en"
---
Learn how to forward customer emails to Klaviyo Helpdesk to manage support in one central place. You can set up automatic email forwarding to direct any emails sent to your customer support address to Helpdesk, allowing you to handle email support through Klaviyo.

## Before you begin

- Ensure you have admin access to your email provider and domain settings. [Invite your admin](https://help.klaviyo.com/hc/en-us/articles/360053547071) to Klaviyo if you need help configuring forwarding.

## How email forwarding works

Adding email support to Klaviyo Helpdesk allows you to manage customer emails alongside other support channels. After you set up email forwarding, any message sent to your support address (for example, support@yourcompany.com) is delivered directly to your Klaviyo Helpdesk.

Each inbound email appears as a new ticket in Klaviyo Helpdesk. You and your team can view, assign, and reply to tickets from within Klaviyo. All replies are sent to your customer’s email, supporting two-way communication.

## Set up automatic email forwarding

You can forward multiple email addresses into Klaviyo Helpdesk. Repeat these steps for each address you want to add.

1. In Klaviyo, go to your account icon in the bottom left corner and click ****Settings > Email > Inbound settings**** or click [here](https://www.klaviyo.com/settings/email/inbound-email-settings).
2. Under **Email support**, toggle the setting ****On****. You’ll see an auto-generated **Workspace email address**. Emails forwarded here will create tickets in your Helpdesk.

   ![Inboxemail2.jpg](https://klaviyo.zendesk.com/hc/article_attachments/38939453598619)
3. Click ****Add email address****.
4. Enter your support email address (e.g., support@yourcompany.com) and click ****Next****.
5. In the **Forward your emails** step, copy your workspace email address. This is the same address shown earlier.

   ![inboxemail3.jpg](https://klaviyo.zendesk.com/hc/article_attachments/38939453601691)
6. Set up forwarding from your support email to the workspace email address in your email provider’s settings. Note that this setup will vary depending on your provider. See your provider’s documentation for exact steps:

   - [Gmail](https://support.google.com/mail/answer/10957?hl=en)
   - [Google Workspace](https://support.google.com/a/answer/10486484?sjid=4903480503918793160-NA)

     Setting up Gmail differs significantly from setting up Google Workspace. If you're unsure which one you have, check if you have an administrator; if so, it's Google Workspace.
   - [Outlook](https://support.microsoft.com/en-us/office/turn-on-automatic-forwarding-in-outlook-7f2670a1-7fff-4475-8a3c-5822d63b0c8e)

     If you are using Outlook you need to ensure that the 'Enable external forwarding' switch is enabled. If you are unsure whether it's enabled or disabled, connect with your IT team to enable it.
   - [Yahoo](https://help.yahoo.com/kb/SLN36684.html)
   - [Apple iCloud Mail](https://support.apple.com/guide/icloud/automatically-forward-email-mm6b1a3960/icloud)

   Your provider may ask you to verify the forwarding address. Look for a verification email in your Klaviyo Helpdesk, usually under the **Unassigned** tab.
7. After completing the verification, go back to Klaviyo and click ****Mark done**** on the **Add email address** menu.
8. Click ****Send test****. This prompts Klaviyo to send a test email to confirm your setup. When forwarding is active, you’ll see a success message. This may take a minute to load.

   ![inboxemail4.jpg](https://klaviyo.zendesk.com/hc/article_attachments/38939453603995)
9. Click ****Finish setup****. Once confirmed, the email you just added will display in the **Email forwarding** section.

![inboxemail5.jpg](https://klaviyo.zendesk.com/hc/article_attachments/38939576088987)

### Test your forwarding address

Now that your email forwarding connection is set up, send a test email to your support address and confirm it appears in your Klaviyo Helpdesk.

- If the test email does not appear, ensure your address is marked as Verified in the forwarding table and that setup is complete.
- If you still don’t receive forwarded emails, double-check your forwarding settings in your email provider and review your email provider’s documentation.

## Managing email support tickets in Klaviyo’s Helpdesk

After you set up email forwarding, all emails sent to your support address will appear as tickets in the Klaviyo Helpdesk.

Your support team can:

- Click any ticket to see the full email conversation and any attachments from the customer.
  - If the sender’s email matches an existing profile in Klaviyo, their profile details and communication history are visible in the sidebar.
  - If there is no match, a new profile is automatically created.
- Reply directly from Klaviyo Helpdesk; your response is sent to the customer’s email address.
- Manage all follow-up messages in the same ticket thread until the ticket is closed, either by a team member or automatically.

Support emails sent via Helpdesk do not affect marketing email deliverability and are not included in your marketing email billing. Learn more about Klaviyo Helpdesk.

## Troubleshooting

****Symptom****: My forwarded support email was marked as failed even though I followed the documentation

****Likely Cause****: Enterprise emails providers often disable forwarding to external recipients by default for security purposes.

****Fix****: You’ll need to reach out to your IT admin to enable forwarding to external recipients.

---

****Symptom:**** My forwarded support emails are not appearing in Helpdesk, or my test emails fail.

****Likely cause:**** The emails are being ****manually forwarded**** (i.e., a team member clicks "Forward" in their inbox). Manually forwarded emails lack the original headers that Klaviyo Helpdesk requires to identify the customer. These emails will be dropped and will not create a ticket.

****Fix:**** You must set up automatic, server-side forwarding from your support inbox to your Klaviyo workspace email. Instruct your team ****not**** to manually forward messages into the helpdesk; instead, have them manage all tickets from within the Klaviyo Helpdesk UI.

---

****Symptom:**** Tickets are being created, but the "customer" is one of my own company's email addresses (e.g., `info@mybrand.com`) instead of the actual customer.

****Likely cause:**** You are using ****chained or nested forwarding****. For example, customers email `info@mybrand.com`, which then forwards to `help@mybrand.com`, which **then** forwards to your Klaviyo workspace address. In this case, Helpdesk may incorrectly identify the intermediate address (`info@mybrand.com`) as the original sender.

****Fix:**** Configure your email provider to forward messages **directly** from the **first** inbox your customers contact (e.g., `info@mybrand.com`) to your Klaviyo Helpdesk workspace email. Remove any intermediate forwarding steps.