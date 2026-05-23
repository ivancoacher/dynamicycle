<h1>Guide to email and SMS consent collection in the Customer Hub</h1>

## You will learn

Learn how Klaviyo collects email and SMS consent from profiles through your Customer Hub onsite experience.

Customer Hub for Shopify currently supports standard storefronts and Shopify Headless. For WooCommerce, navigate to https://help.klaviyo.com/hc/en-us/articles/47792369863451

For feedback about Customer Hub functionality, email customerhub@klaviyo.com.

## Before you begin

To collect email or SMS consent in the Customer Hub interface, first make sure you've completed the following steps in your Klaviyo account:

- [Enable Customer Hub in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/33660324811675)
- If you plan to collect SMS consent
  - [Turn on SMS in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/4404274419355)
  - Set up your disclosure language, including:
    - Create a [mobile terms of service](https://help.klaviyo.com/hc/en-us/articles/360049177511)
    - Update your [privacy policy](https://help.klaviyo.com/hc/en-us/articles/360049177511)

Note that SMS consent collection in Customer Hub is only available for those on an Klaviyo SMS plan. If you use a different SMS provider, [disable the SMS consent collection setting](https://help.klaviyo.com/hc/en-us/articles/35094079400219#h_01JWAE1A2R3S6SXFA7XAC0KK83). Additionally, SMS consent collection is currently unavailable for [Klaviyo brands that require age-gating](https://help.klaviyo.com/hc/en-us/articles/17252552814875#h_01H9NZT3W40TBKBXGFQHKCEYRZ).

## How Customer Hub connects to Shopify Accounts

To understand how Klaviyo collects consent through the Customer Hub, it’s helpful to first understand how it integrates with Shopify Accounts. When the Customer Hub feature is enabled on your site:

- The Customer Hub drawer experience replaces the default Shopify account login pages. Once it's live, clicking the account icon or visiting any /account page on your site automatically opens the Customer Hub interface with a prompt to log in.
- Customer data syncs from Shopify Accounts to Klaviyo, allowing profiles to sign in with their existing Shopify credentials. If a profile doesn't have a Klaviyo profile, one is created upon login.
  - Klaviyo uses this data to identify which profiles have already subscribed to SMS marketing and to accurately display their personal information on the **Profile** tab of the Customer Hub drawer.

## Collecting consent in Customer Hub

Within Klaviyo you can control whether profiles are asked for email and SMS marketing consent in the Customer Hub interface.

For SMS consent collection:

- ****If you have an active SMS plan in Klaviyo****: SMS consent collection in the Customer Hub interface is enabled by default.
- ****If you do not have a Klaviyo SMS plan****: SMS consent collection is automatically disabled, so no site visitors are asked to subscribe to SMS in the Customer Hub.

### Where consent is requested

There are 2 places where profiles may be asked for consent:

1. ****Customer Hub sign in****: After signing in with their email, visitors who are not current email or SMS subscribers yet are prompted to provide their email and / or phone number and consent to email and / or SMS marketing (left image in the table below).
2. ****Edit profile information page in the Customer Hub drawer****: Signed-in profiles can manage their channel consent directly in the "edit profile" page in the profile tab of Customer Hub.

|  |  |
| --- | --- |
| Customer Hub login consent request interstitial | Edit profile page - marketing consent management |
| ![](https://klaviyo.zendesk.com/hc/article_attachments/44083736752667) | ![](https://klaviyo.zendesk.com/hc/article_attachments/44083755248667) |

Your account's disclosure language is included by default. Note that smart opt-in and tap-to-text are not supported in the Customer Hub interface, and the text and button labels on these pages also cannot be customized.

Klaviyo only asks for phone numbers from visitors who haven't subscribed to SMS marketing yet. If a site visitor skips the SMS consent prompt during login, they will not see another prompt at login for 30 days.

### Double opt-in for SMS consent in the Customer Hub

Klaviyo uses a double opt-in process for all SMS sign-ups through the Customer Hub interface. This 2-step verification process ensures customers explicitly agree to receive SMS marketing messages.

This process goes as follows:

1. The visitor provides their phone number, checks the **Sign me up for SMS marketing** checkbox, and clicks ****Continue****.
2. A loading screen in the Customer Hub interface tells them to check their messages.
   ![Loading screen in a Customer Hub interface instructing someone to go reply yes to confirm SMS consent subscription.](https://klaviyo.zendesk.com/hc/article_attachments/37621292472731)
3. They recieve an automated text message asking them to confirm their subscription (e.g., reply YES).
4. Once they confirm, their Klaviyo profile updates to a **Subscribed** SMS status, and a **Subscribed to SMS marketing** metric is recorded in their activity.

If a site visitor enters their phone number but does not confirm their subscription via the text message, they are not marked as subscribed, and they also will not be prompted again in the future for SMS consent at Customer Hub sign in. However, they can still subscribe to SMS marketing on the **Edit profile** page.

Similarly, if a visitor unsubscribes from SMS marketing after previously subscribing, they will not see the SMS consent request again at sign in, but they do have the option to go resubscribe from the **Edit profile** page within the Customer Hub interface.

## Configure consent collection in the Customer Hub

To choose which channels to request consent for in the Customer Hub interface:

1. In Klaviyo's main navigation, select ****Service - Customer Hub****.
2. Click ****Settings****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/40773879688091)
3. Scroll to the **Marketing consent** section, then uncheck the boxes to disable
   ![](https://klaviyo.zendesk.com/hc/article_attachments/44083736758939)
4. Click ****Save****.

## FAQs

#### I can already email my customers without getting explicit email consent. What's the value in collecting their email consent?

Email consent is a nuanced topic. While SMS consent is explicitly required before sending any marketing messages, email consent is not always required. To understand what's right for your brand, refer to:

- [Understanding explicit vs. implicit consent](https://klaviyo.zendesk.com/hc/en-us/articles/4404203889947)
- [Understanding consent in profiles](https://klaviyo.zendesk.com/hc/en-us/articles/360037101072)
- [Email deliverability best practices reference](https://klaviyo.zendesk.com/hc/en-us/articles/25620771311643)

## Additional resources

- [Getting started with Customer Hub](https://klaviyo.zendesk.com/hc/en-us/articles/33660324811675)
- [SMS opt-in methods reference](https://klaviyo.zendesk.com/hc/en-us/articles/27902671291419)
- [Understanding the Customer Hub dashboard](https://klaviyo.zendesk.com/hc/en-us/articles/33660382797595)
