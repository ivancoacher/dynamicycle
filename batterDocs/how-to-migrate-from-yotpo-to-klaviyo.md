<h1>How to migrate from Yotpo to Klaviyo</h1>

Learn how to migrate from Yotpo email and SMS to Klaviyo via Klaviyo’s Yotpo Email & SMS Migration integration. This integration syncs profiles from Yotpo along with email and SMS subscriptions. Additionally, learn best practices and next steps when migrating.

![](https://fast.wistia.com/embed/medias/akui1d7vqk/swatch)

## Before you begin

1. You must be an account administrator in Yotpo in order to integrate.
2. You must be an administrator or owner in Klaviyo in order to integrate.
3. If you plan to migrate your SMS contacts from Yotpo, you must first:

- [Set up SMS in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/4404274419355). To sync SMS consent, you must configure sending numbers in each region where you want to collect and sync consent.
- [Notify subscribers](https://help.klaviyo.com/hc/en-us/articles/4403980438555) before you start sending from the new number.

### Recreate forms, email templates, and flows

First, recreate your most important customer collection methods (referred to as “forms” in Klaviyo), email templates, and flows in Klaviyo. Once you have these ready, you don’t have to worry about maintaining 2 different subscriber lists or having a gap in customer communications.

For information about these product areas, check out these getting started guides:

- [Forms](https://help.klaviyo.com/hc/en-us/articles/360026474752)
- [Email templates](https://help.klaviyo.com/hc/en-us/articles/115000102752#h_01HNG9WJTANZBQ3QZRJ4EHD43F)
- [Flows](https://help.klaviyo.com/hc/en-us/articles/115002774932)

  Since the integration is a 1-time sync, having your messages and forms ready means that you can immediately start using Klaviyo.

  Particularly for SMS, you should not be maintaining consent in 2 separate platforms. If you are still sending from Yotpo after you install the integration, anyone who subscribes or unsubscribes is not automatically transferred. This may mean you fall out of compliance or lose out on messaging those who subscribed.

  This is also a good time to review what’s working well:
- Is one form outperforming the rest?
- Which flows are generating the most revenue?
- Which email template creates the highest clicks?

This not only tells you what to prioritize when moving to Klaviyo, but it also indicates where you should spend time experimenting and optimizing.

## Integrate Yotpo with Klaviyo

To integrate Yotpo with Klaviyo, you'll need to obtain your App Key and Secret Key from Yotpo, then set up the integration in Klaviyo:

1. In your Yotpo SMS and Email admin, click your account icon and select ****Account Settings****.
2. Scroll to the **API Credentials** section, then copy your **App Key**.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/39742508136859)
3. In a new tab, log in to Klaviyo and select the ****Integrations**** tab.
4. Click ****Explore apps****.
5. Search for **Yotpo** on the Klaviyo app marketplace and select the card.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/39742508140059)
6. Click ****Install****.
7. Paste your Yotpo App Key you copied in the corresponding box.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/39749638021275)
8. Switch back to your Yotpo tab.
9. Under **API Credentials**, click ****Get secret key****.
10. Copy the code sent to your email and paste it in the box, then click ****Submit****.
11. Your Secret Key will appear in a pop-up. Click ****Copy to clipboard****.
    ![](https://klaviyo.zendesk.com/hc/article_attachments/39749664634523)
12. Switch back to your Klaviyo tab.
13. Paste your Secret Key in the corresponding box, then click ****Connect****.
    ![](https://klaviyo.zendesk.com/hc/article_attachments/39749664635803)
14. Review the permissions and click ****Allow****.
    ![](https://klaviyo.zendesk.com/hc/article_attachments/39742508146459)
15. Check **Sync your Yotpo Email & SMS Migration email subscribers to Klaviyo**. If you don’t check the box, Klaviyo will not sync email consent from Yotpo.
    1. Select a list from the dropdown to add email subscribers to.
       ![](https://klaviyo.zendesk.com/hc/article_attachments/39742499603355)
16. Check **Sync your Yotpo Email & SMS Migration SMS subscribers to Klaviyo**. If you don’t check the box, Klaviyo will not sync SMS consent from Yotpo.
    1. Select a list from the dropdown to add SMS subscribers to.
17. Click ****Complete setup****.
18. You’ll receive a success message confirming that your Yotpo integration has been connected.

![](https://klaviyo.zendesk.com/hc/article_attachments/39742508149403)

## Data synced from Yotpo to Klaviyo

Once you integrate Yotpo with Klaviyo, Klaviyo will perform a one-time sync of all profiles from Yotpo. This integration is intended for use in migration and does not have an ongoing sync. Data is only synced from Yotpo to Klaviyo.

The following data is synced from Yotpo to Klaviyo:

- Profiles
- Email subscriptions (if you checked the settings box and selected a Klaviyo list)
- SMS subscriptions (if you checked the settings box and selected a Klaviyo list)

  Email and SMS subscriptions sync based on subscription status in Yotpo; if a profile is subscribed to email or SMS in Yotpo, they will be subscribed in Klaviyo, and if they were unsubscribed in Yotpo they will be unsubscribed in Klaviyo. Subscribed profiles will be added to the list defined in your integration settings if they aren’t already subscribed in Klaviyo.

  If you choose not to sync subscriptions, all profiles will sync with a status of **Never Subscribed**.

  The following profile properties sync from Yotpo to Klaviyo:
- Email
- Phone number
- First name
- Last name
- Address1
- Address2
- City
- Region
- ZIP
- Country
- Yotpo Gender
- Yotpo Default Language
- Yotpo Default Currency
- Yotpo Tags
- Yotpo Email Last Opened
- Yotpo Email Last Delivered
- Yotpo Email Last Engaged
- Yotpo SMS Last Sent
- Yotpo SMS Last Engaged

## After migrating your data

### Turn off all subscriber collection methods in Yotpo

Once you import, you should immediately stop collecting new subscribers in Yotpo. Maintaining lists of subscribers in 2 different platforms is not only difficult, it’s a risky compliance move (particularly for SMS).

1. In Yotpo, navigate to ****Audience****.
2. On the **Subscriber Collection Tools** page, scroll down to **My tools**.
3. Click the 3 horizontal dots next to a live tool.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/39742499609499)
4. From the menu, click ****Edit**** to view this tool.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/39742499611035)
5. At the top, open the **Status** dropdown.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/39663829287451)
6. Select ****Draft****.
7. Now click, ****Save as Draft****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/39742499612699)
8. Repeat for any other live subscriber collection tools.

In addition, edit or remove any place where you’ve linked to these opt-in pages, such as on your social media pages, QR codes, etc.

### Take note of key settings in your Yotpo account

When you migrate to a new service provider, there’s no guarantee that they use the same settings. This can lead to significant differences in your data once you change platforms, so a key part of migration is noting down your current settings.

In particular, pay attention to the following:

- Conversion windows, and [how attribution works in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/1260804504250)
- UTM tracking
- Smart Sending

To find these settings in Yotpo:

1. In the left sidebar, open the ****Settings**** dropdown, then click ****General Settings****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/39742499614107)
2. Navigate to:
   1. ****Attribution**** for your conversion and UTM settings.
   2. ****Compliance**** for Smart Sending.

### SMS-specific considerations

If you are also moving your SMS plan to Klaviyo, please:

- Configure sending numbers in each region where you want to collect and sync consent.
- Write down your subscribe keywords.
- Check quiet hours.

## Next steps

Once you finish with the steps above, congratulations! You’ll have all of your key information now in Klaviyo.

As a next step, we recommend:

1. [Canceling your email plan in Yotpo](https://support.yotpo.com/docs/configuring-billing-and-payments).
2. [Adding your users in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/360053547071).
3. Recreating your [segments](https://help.klaviyo.com/hc/en-us/articles/360035312491).
