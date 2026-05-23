<h1>How to turn off SMS consent at checkout for BigCommerce</h1>

## You will learn

Learn how to stop collecting SMS consent at checkout for BigCommerce.

To do so, you need to:

1. Remove the code snippet from your theme file in BigCommerce.
2. Uncheck the **Collect SMS Subscribers** box in Klaviyo.

## In BigCommerce

1. Go to your BigCommerce store.
2. Click ****Settings > Advanced > Data Solutions****.
3. Look for **Site Verification Tags**and click the three dots to open a dropdown menu.
4. From the dropdown, click ****Disconnect****. ![Data solutions page in BigCommerce](https://klaviyo.zendesk.com/hc/article_attachments/28713332696603)
5. In the modal that pops up, click ****Disconnect**** to continue.
   ![Modal to disconnect site verification tags](https://klaviyo.zendesk.com/hc/article_attachments/28713338341787)

Note that the script will still appear under **Site Verification Tags**; however, it will no longer be active on your site. As soon as you hit ****Disconnect****, this stops SMS consent collection. (If you want to remove the script entirely, you must input some other text (e.g., a space or another script.)

## In Klaviyo

1. In Klaviyo, select the ****Integrations**** tab, then click on ****BigCommerce****.
2. Uncheck the ****Sync your BigCommerce SMS subscribers to Klaviyo**** box**.**
3. In the modal, click ****Stop collecting SMS consent****.
4. To save the changes, click ****Save****.

## Additional resources

- Find out [how to add an embedded form to your site](https://help.klaviyo.com/hc/en-us/articles/360022594552)
- Learn how to [re-enable SMS consent at checkout](https://help.klaviyo.com/hc/en-us/articles/360058194032)
