---
id: "360054551492"
title: "Getting started with PrestaShop"
source_url: "https://help.klaviyo.com/hc/en-us/articles/360054551492-Getting-started-with-PrestaShop"
section: "PrestaShop"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-05-15T08:50:33Z"
language: "en"
---
## You will learn

Learn how to integrate your PrestaShop store with Klaviyo. Klaviyo is PrestaShop’s preferred marketing automation partner. This process involves 2 steps: installing a free module (**PrestaShop Automation with Klaviyo**) in PrestaShop and enabling the integration within Klaviyo. This article also provides information about monitoring your data sync, setting up transactional emails, and updating your module so that you can grow with Klaviyo.

## Before you begin

In order to use the Klaviyo module, you’ll need to be on one of the following PrestaShop versions:

- PrestaShop 1.7.0 through 9.1.x (and using PHP 7.1 or higher)
  - Please note that if you want to use our SMS consent at checkout collection feature, you'll need to be on PrestaShop 1.7.6 or higher.

    If you are using a PrestaShop version prior to 1.7.0 and want to upgrade in order to use a Klaviyo module, check out PrestaShop's [guide to upgrading your store.](https://devdocs.prestashop.com/1.7/basics/keeping-up-to-date/upgrade/)

    Please review the following information before integrating:
- If you're using PrestaShop Edition, the [PrestaShop Automation with Klaviyo](https://addons.prestashop.com/en/promotions-marketing/91359-prestashop-automation-with-klaviyo.html) module comes pre-installed. If you're using another version of PrestaShop, you’ll need to install it (detailed in the next section).
- **PrestaShop Automation with Klaviyo** is designed to integrate with PrestaShop [back office functionality](https://docs.prestashop-project.org/1.7-documentation/user-guide/connecting-back-office) like PrestaShop Account. When installing **PrestaShop Automation**, you'll be prompted to install the PrestaShop Account, PrestaShop EventBus, and PrestaShop Marketplace modules in your back office in order to use the Klaviyo module.
- Don’t want to integrate with back office functionality on your open source PrestaShop store? You can use our [Klaviyo by PrestaShop Partners](https://addons.prestashop.com/en/newsletter-sms/49837-klaviyo.html) module instead, which contains the same set of features as **PrestaShop Automation with Klaviyo** and does not require PS\_MBO.
- It is highly recommended to add Klaviyo IPs to your firewall provider’s allow list to minimize authentication and configuration issues. For more details, please check out [How to allowlist Klaviyo integration traffic IP addresses](https://help.klaviyo.com/hc/en-us/articles/19143781289115).

Looking to update your current Klaviyo module? See the [end of this article](https://help.klaviyo.com/hc/en-us/articles/360054551492#h_01HD6YRW7VWJQKBXTN7TGA7N88) to learn more.

## How-to video

![](https://fast.wistia.com/embed/medias/bywqzlujfa/swatch)

## Install the module in PrestaShop

1. If you use PrestaShop Edition, the **PrestaShop Automation with Klaviyo** module comes pre-installed. You should:
   1. Log in to your PrestaShop shop.
   2. Under ****Configure**** in the left-hand menu, select ****Klaviyo****.
   3. Skip to [the next section](https://help.klaviyo.com/hc/en-us/articles/360054551492#h_01HD6YRW7VPWVC4900MNN5F0K8) of this article to configure the module.
2. If you do not use PrestaShop Edition, head to the [PrestaShop Automation with Klaviyo module page](https://addons.prestashop.com/en/newsletter-sms/91359-prestashop-automation-with-klaviyo.html) on the PrestaShop marketplace and proceed to the next step.

   ![](https://klaviyo.zendesk.com/hc/article_attachments/28715970454683)
3. On the module page, click ****Download****. Validate your details if necessary, then select the version of PrestaShop you're using and download the zip file. You do not need to extract the zip file.

   ![](https://klaviyo.zendesk.com/hc/article_attachments/28715963851931)
4. Log in to your PrestaShop shop and navigate to ****Modules > Module Manager****. Click ****Upload a module****, then drag and drop the zip file to the module manager.

   ![](https://klaviyo.zendesk.com/hc/article_attachments/35197766381595)
5. The module will display a successful installation message upon completion. Next, click ****Configure**** and continue to the next section.

## Configure the module in PrestaShop

1. You will need to retrieve your Klaviyo public API key (also known as your site ID), as well as generate a Klaviyo private API key for use in PrestaShop.

   - Log in to Klaviyo, then click your organization name in the lower left.
   - Select ****Settings > API keys****.
   - Copy your public API key from the page and paste it in the corresponding setting in PrestaShop.
   - Back in Klaviyo, click ****Create Private API Key****, name it, select ****Full Access Key****, and click ****Create****.
   - Securely copy your newly created private API key and paste it in the corresponding setting in PrestaShop.
2. Toggle on ****Send real-time order events to Klaviyo**** if you want transactional order events to sync in real time. These events can be used to send transactional messaging, and will appear as a second set of events labeled as transactional (e.g., you’ll see a metric in Klaviyo labeled **Placed Order Transactional**, which will sync in real time, in addition to a metric labeled **Placed Order,** which will sync every 30 minutes).

   ![](https://klaviyo.zendesk.com/hc/article_attachments/28715963854107)
3. Toggle on ****Turn off PrestaShop-generated transactional order emails**** if you wish to do so. We recommend leaving this setting disabled until you have transactional emails ready to go in Klaviyo. You can return to this page at any time and toggle on the setting to disable PrestaShop sending. Note that toggling on this setting blocks transactional emails associated with **Placed Order**, **Fulfilled Order**, **Canceled Order**, and **Refunded Order**, as well as payment reminder emails.
4. Enable **Sync PrestaShop email subscribers to Klaviyo** if you wish to sync email subscribers collected at checkout or via a sign-up form.
5. Enable **Sync PrestaShop SMS subscribers to Klaviyo** if you wish to enable users to opt-in to SMS marketing during checkout.
6. ![](https://klaviyo.zendesk.com/hc/article_attachments/28715963860379)

   You must [set up SMS in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/4404274419355) before you can sync SMS subscribers.
7. Click ****Save**** to proceed.
8. If you toggled on the email subscriber sync setting, you will be prompted to select a list from your Klaviyo account to add email subscribers to. All new subscribers will be added to the list you choose. We recommend using the **Email List.**
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28715970464923)
9. If you would like to subscribe profiles to a Klaviyo list using the [PrestaShop Newsletter Subscription module](https://addons.prestashop.com/en/newsletter-sms/22318-newsletter-subscription.html#overview), please make sure you have enabled the module, and that the module uses version 2.6.0 or higher.
10. If you toggled on the SMS subscriber sync setting:
    1. You will be prompted to select a list from your Klaviyo account to add SMS subscribers to. All new subscribers will be added to the list you choose. We recommend using a separate list for email and SMS subscribers.
    2. Choose **When do customers subscribe**? This can either be after they start checkout, or place an order
    3. Add a consent label for your marketing checkbox; use a clear label to inform users what they’re opting in to (e.g., “Subscribe to SMS marketing”).
    4. Add consent [disclosure text](https://help.klaviyo.com/hc/en-us/articles/4412878737051). You must include disclosure language for compliance. Make sure to include the terms of your SMS marketing program in your terms of service and privacy policy. Please note that you must use HTML in the disclosure box. Example disclosure language:
       **By checking this box and entering your phone number above, you consent to receive marketing text messages (e.g. promos, cart reminders) from [Company Name] at the number provided. Msg & data rates may apply. Msg frequency varies. Unsubscribe at any time by replying STOP or clicking the unsubscribe link (where available). <a href="link">Privacy Policy</a> & <a href="link">Terms</a>.**
    5. You can use the language toggle to the right of the disclosure box to add language-specific disclosure text for each language your store is displayed in.

       ![](https://klaviyo.zendesk.com/hc/article_attachments/28715963865755)
11. Click ****Save**** to proceed.
12. Next, complete the order status mapping form by either accepting the default values or selecting different values. Order statuses correspond to which order events are recorded in Klaviyo. You can select multiple values for each order event. Use Cmd or Ctrl+Click to select multiple. The same value cannot be selected in multiple order events. Selecting a duplicate value will result in an error message and cannot be saved. Both transactional and non-transactional events will adhere to the order mapping you select.
13. When you are done configuring order statuses, click ****Save****.
14. You’ll see a **Coupons** section where you can generate coupons. On the **Cart Rule Limit** field, select **One cart rule per prefix** or **One cart rule per order** to limit how customers can use coupons. By default, this is set to **One cart rule per prefix,** preventing a customer from adding more than one code with the same prefix at checkout.

    ![Cart rule limit field in Klaviyo module settings](https://klaviyo.zendesk.com/hc/article_attachments/28715970473371)
15. If you wish to generate coupon codes as well using the **Quantity to generate** field, you can return to this page later. Read about [how to create static coupons for PrestaShop](https://help.klaviyo.com/hc/en-us/articles/19655157461403) for more information.
16. Under **Back in Stock**, you'll see the **Email notification** toggle, which enables access to back in stock email sending in Klaviyo. In order to enable this toggle, you’ll need to have the mail alerts module installed in PrestaShop and have turned on product availability:
    1. In a new tab, navigate to ****Modules > Module Manager**** within your PrestaShop admin.
    2. Search for **mail alerts**.
    3. Find the module and click ****Install****.

       ![](https://klaviyo.zendesk.com/hc/article_attachments/33130255350043)
    4. After the module installs, click ****Configure****.

       ![](https://klaviyo.zendesk.com/hc/article_attachments/33130255356315)
    5. Make sure that ****Product availability**** is toggled on.

       ![](https://klaviyo.zendesk.com/hc/article_attachments/33130255362715)
    6. Click ****Save****.
17. Enable the **Email notification** toggle to enable back in stock email sending in Klaviyo. Note that enabling the toggle will also turn off back in stock email sending from PrestaShop. You’ll still need to set up a [back in stock flow](https://help.klaviyo.com/hc/en-us/articles/33059375555099#h_01JJ80E2W0K4N9THD0RPEBVJ3Y) in Klaviyo in order to begin sending.

    ![](https://klaviyo.zendesk.com/hc/article_attachments/33130201022107)
18. Next, select ****Advanced Parameters**** within the ****Configure**** section of the left-hand navigation. Select ****Webservice****. Copy the Klaviyo webservice key that has been generated for you and continue to the next section.

- This key will be used when enabling the integration in Klaviyo in the next step. We recommend validating that the webservice key has the correct Klaviyo permissions by selecting the pencil icon next to the Klaviyo webservice key. Scroll down the list of all permissions and locate Klaviyo. Ensure all permissions checkboxes are checked. Select ****Save**** to apply any changes.

## Enable the integration in Klaviyo

1. Next, enable the PrestaShop integration within your Klaviyo account. In Klaviyo, select ****Integrations**** from the left-hand navigation.
2. Click ****Explore apps****, search for **PrestaShop**, and select the card. Then, click ****Install****.
3. On the next page, click ****Connect to PrestaShop****.

   ![](https://klaviyo.zendesk.com/hc/article_attachments/35197766384411)
4. On the next page, enter your PrestaShop shop URL in the ****Shop URL**** field. You can find your shop URL in your PrestaShop account under ****Shop Parameters > Traffic & SEO > Shop URLs****. You can also click ****View my shop**** to quickly navigate to your PrestaShop site from any page within your account to retrieve your shop’s URL.

   ![Connection details for PrestaShop in Klaviyo including Shop URL and Webservice key](https://klaviyo.zendesk.com/hc/article_attachments/28715963832347)
5. Paste the Webservice key you copied from PrestaShop into the ****Webservice key**** field.
6. If you’d like to convert all currencies used by your shops to a single currency in Klaviyo, check ****Convert all currencies to one standard currency**** and select a global currency code from the dropdown list.

   - This will not change the currency of your Klaviyo account. To change the currency you use account-wide, please refer to our guide to [Changing the Currency for Your Account](https://help.klaviyo.com/hc/en-us/articles/115005061007-Change-the-Currency-for-Your-Account).
7. Pull a list of your available PrestaShop shops by selecting ****Retrieve list of shops****. Then, check the shops you wish to integrate. You must select at least 1 shop to proceed.
8. Check **Sync variants** if you would like to sync catalog variants (also known as combinations) from PrestaShop to Klaviyo. We recommend syncing variants to support back in stock, low inventory, and price drop flows.

   ![](https://klaviyo.zendesk.com/hc/article_attachments/33082359779355)
9. **Sync inventory** will be checked by default if you select **Sync variants**. This setting will periodically sync the inventory amount for each variant to make sure back in stock, low inventory, and price drop flows function correctly. If you check **Sync variants** but uncheck **Sync inventory**, you will not be able to use these flows. You will, however, have access to variant-level data for use in email messaging.
10. When you are done, select ****Complete setup****.
11. You’ll see a success message indicating your accounts have been connected.

![Your PrestaShop account is now connected to Klaviyo success message](https://klaviyo.zendesk.com/hc/article_attachments/28715963840795)

## PrestaShop data in Klaviyo

3 types of events sync from PrestaShop to Klaviyo:

- Order events synced every 30 minutes (e.g., **Placed Order**).
- Transactional order events synced in real time, if you choose to enable them (e.g., **Placed Order Transactional**).
- Klaviyo onsite events (e.g., **Active on Site**, **Viewed Produc**t, and **Added to Cart**).

Additionally, customer information syncs from PrestaShop to Klaviyo profiles, including email address, phone number, email consent, and SMS consent if applicable.

You can view all these events in Klaviyo by navigating to ****Analytics > Metrics****. Filter by **PrestaShop** to see order and transactional order events (they will have a PrestaShop icon) or filter by **API** to see Klaviyo onsite events (they will have a gear icon). For a full list of metrics synced from PrestaShop, check out our [PrestaShop data reference](https://help.klaviyo.com/hc/en-us/articles/360055123191).

When you first integrate with PrestaShop, Klaviyo will sync the last 90 days of your data so you can start engaging your most recent customers right away. After the sync of your most recent 90 days of data, Klaviyo will begin your complete historical data sync. Depending on how many orders, customers, and products your store has, it can take anywhere from a few minutes to several days to sync all of your data.

We recommend that you have a minimum of 1024 mb allotted PHP memory while your historical sync is in progress. This allows the sync to complete in a timely manner. The initial memory requirements can be reduced after the historical sync is completed, if desired.

When the sync is complete, the PrestaShop integration in the Integrations tab will be marked complete. To verify that all data from PrestaShop is successfully synced, you can cross-check the total orders for a few days or a week. Before you start validating, make sure your account's timezone matches the settings in PrestaShop. To check or update your account's timezone:

1. Click your organization name in the bottom left.
2. Select ****Settings****.
3. Select the ****Organization**** tab.

## Send transactional emails

Want to send transactional emails using real-time order data synced from PrestaShop? You’ll need to create flows from scratch in Klaviyo to do so. Read [How to use flows to send transactional emails](https://help.klaviyo.com/hc/en-us/articles/360003165732) to learn about how transactional emails work in Klaviyo. You’ll need to set up these flows and then contact Klaviyo’s support team to get them approved. Once they’re approved, you can toggle off transactional email sending in PrestaShop and set your transactional flows live in Klaviyo.

## Re-sync your catalog

If you’d like to re-sync your PrestaShop catalog data at any point, you can do so in your integration’s **Data** tab:

1. In Klaviyo, select ****Integrations**** from the left-hand navigation.
2. Select ****PrestaShop**** from the list.
3. Click the ****Data**** tab.
4. In the section labeled **Sync catalog data**, click ****Re-sync.**** Your catalog will begin re-syncing.

![](https://klaviyo.zendesk.com/hc/article_attachments/33082365067547)

## Update your module

Are you using a PrestaShop module version below 1.4.1? We recommend upgrading immediately to 1.4.1 or higher. Older versions of the module use Klaviyo’s v1 and v2 APIs which have been retired and no longer operate as expected.

Additionally, upgrading to version 1.4.1 or higher will let you take advantage of these features first released on 1.3.0:

1. Easily display the true price and inclusive value-added tax (VAT), for products promoted in your emails. Please note that upgrading from below version 1.2.10 to version 1.2.10 or above can cause email template inaccuracies due to this change; [read our article](https://help.klaviyo.com/hc/en-us/articles/14477037350299) to learn what to do.
2. Send transactional emails to your customers with a real-time event sync.
3. Quickly generate and import bulk coupons into Klaviyo.

   To update your module to the newest version:
4. Log in to your PrestaShop admin.
5. Navigate to ****Modules > Module Manager****.
6. Scroll to find the Klaviyo module and select ****Upgrade****.

![](https://klaviyo.zendesk.com/hc/article_attachments/28715963843099)

If you are upgrading from a version below 1.3.0: it’s important to note that, once you have completed the upgrade, cart rebuild links that were used in abandoned cart emails sent prior to the upgrade will no longer work. However, all abandoned cart emails sent after the upgrade will function properly.

To learn about changes made in each version, head to the [Klaviyo module on the Addons marketplace](https://addons.prestashop.com/en/newsletter-sms/49837-klaviyo.html), scroll down to **What’s New**, and click ****Show changelog history****.

## Outcome

You’ve now integrated PrestaShop with Klaviyo and can start using Klaviyo for your owned marketing needs.