<h1>How to enable back in stock for PrestaShop</h1>

## You will learn

Learn how to send back in stock messaging with Klaviyo for your PrestaShop store. There are 3 steps in this process:

1. Check a setting in Klaviyo to sync PrestaShop variants (also known as combinations)
2. Toggle on the back in stock setting in PrestaShop
3. Create a back in stock flow in Klaviyo

## Before you begin

- You must be using version 1.9.0 or later of our PrestaShop module to access our Back in Stock feature. Learn how to [update your module](https://help.klaviyo.com/hc/en-us/articles/360054551492#h_01HD6YRW7VWJQKBXTN7TGA7N88).
- Make sure you’ve [integrated Klaviyo and PrestaShop](https://help.klaviyo.com/hc/en-us/articles/360054551492) before getting started with this article.

## Check the variant sync setting

First, you’ll need to check a setting in Klaviyo to sync variants from PrestaShop:

1. Select the ****Data**** tab of your PrestaShop integration.
2. In the section labeled **Sync catalog data**, click ****Re-sync****. Your catalog will begin re-syncing.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/33061467587611)

1. In Klaviyo, select the ****Integrations**** tab.
2. Select ****PrestaShop**** from the list.
3. On the settings page that appears, check the **Sync variants** setting.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/33061452698651)
4. **Sync inventory** will be checked by default if you checked **Sync variants**. This setting will periodically sync the inventory amount for each variant to make sure back in stock flows function correctly. If you check **Sync variants** but uncheck **Sync inventory**, you will not be able to use back in stock flows. You will, however, have access to variant-level data for use in email messaging.
5. Click ****Save****.
6. After updating the variant and/or inventory settings, we recommend re-syncing your catalog to ensure the changes take effect for all products. If you choose not to re-sync at all, your catalog items will re-sync individually over time, and only when variant records have been updated. Merchants with larger catalogs and limited server resources may wish to re-sync during a period of low site traffic, so as not to risk impact to site performance. To re-sync your catalog:

## Toggle on the setting in PrestaShop

Next, you’ll need to toggle on a setting in PrestaShop. Before toggling the setting, make sure you have the mail alerts module installed in PrestaShop and have turned on product availability:

1. In your PrestaShop admin, navigate to ****Modules > Module Manager****.
2. Search for **mail alerts**.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/33132025202331)
3. Find the module and click ****Install****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/33130254539291)
4. After the module installs, click ****Configure****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/33130200155931)
5. Make sure that ****Product availability**** is toggled on.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/33130254552219)
6. Click ****Save****.
7. Navigate to ****Configure > Klaviyo****.
8. Enable the **Email notification** toggle to enable back in stock email sending in Klaviyo. Note that enabling the toggle will also turn off back in stock email sending from PrestaShop.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/33130254554139)
9. Select ****Save**** to apply your changes.

## Create a Back in Stock flow

Next, you’ll set up a flow in Klaviyo to begin sending back in stock notifications:

1. First, configure your [back in stock flow settings](https://help.klaviyo.com/hc/en-us/articles/115003872251#h_01HBBYXYTAXRW86A1XXE4FRV2T) in Klaviyo, which include rules around minimum inventory and customer notifications.
2. Then, navigate to the ****Flows**** tab in Klaviyo.
3. Click ****Create flow****.
4. Filter by **PrestaShop** and search for **back in stock**.
5. Select the [pre-built back in stock flow for PrestaShop](https://www.klaviyo.com/library/flows?object_id=SEDaDq).
   ![](https://klaviyo.zendesk.com/hc/article_attachments/33061478937883)
6. In the flow builder, make any changes you’d like and customize the email.
7. Then, learn how to [set your flow live](https://help.klaviyo.com/hc/en-us/articles/115002774932#h_01H9JGTZ8RVQANQHGVRJ6V4W63).

## Outcome

You’ve now enabled back in stock messaging for your PrestaShop store.
