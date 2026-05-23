<h1>How to add historical Shopify SMS subscribers to your list</h1>

## You will learn

Learn how to add historical Shopify SMS subscribers to your Klaviyo SMS list. While historical email subscribers automatically sync through Klaviyo’s Shopify integration, historical SMS subscribers do not. Instead, they must be added manually via the process below.

## Before you begin

If you've yet to integrate your Shopify store with Klaviyo, head to [Getting started with Shopify](https://help.klaviyo.com/hc/en-us/articles/115005080407) before continuing with this article.

## How to add historical SMS subscribers

Adding historical SMS subscribers to your email list requires 4 steps:

1. Download your subscriber list from Shopify.
2. Edit your list to only contain SMS subscribers.
3. Upload the edited list to Klaviyo.
4. Combine the uploaded list with your preferred list in Klaviyo.

### Download your customer list from Shopify

1. In your Shopify admin, head to ****Customers****.
2. Click ****Export**** in the upper right.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28717881991579)
3. Select ****All customers****.
4. Select tags and/or metafields, if you'd like to include them.
5. Select ****CSV for Excel, Numbers, or other spreadsheet programs****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28717881994651)
6. When you are ready, click ****Export customers****.
7. If successful, Shopify will email you a CSV file of your subscribers.
8. Head to your inbox and download the file sent from Shopify.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28717881996699)

### Edit your list to contain only SMS subscribers

1. Open your CSV file downloaded from Shopify in your preferred spreadsheet program.
2. Find the **Accepts SMS Marketing** column.
3. Rename this column to **SMS marketing** consent.
4. In this column, change the following:
   - "Yes" to "Subscribe."
   - "No" to "Never Subscribed."
5. Save your CSV file.

### Upload your list to Klaviyo

1. Navigate to ****Audience > Lists & segments****.
2. Create a new list by selecting ****Create New > List****.
3. Name your list, then click ****Create new****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/32805244586779)
4. On the next page, select ****Import contacts****.
5. Click ****Upload****, then select your CSV file for upload.
6. Map only the following columns (other necessary properties sync through our integration):
   - Email > Email
   - Phone > Phone Number
     ![](https://klaviyo.zendesk.com/hc/article_attachments/28717888051611)
7. If you have the **SMS marketing consent column**, consent will be applied automatically to anyone marked as "Subscribe."
8. Click ****Import****.

The import may take some time to process. It will be marked **Completed** when it is finished. Once the import is completed, move on to the next step.
![](https://klaviyo.zendesk.com/hc/article_attachments/28717882006427)

### Combine the uploaded list with your list in Klaviyo

1. Navigate to ****Audience > Lists & segments****.
2. Click on the list you uploaded from Shopify.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/32805259414683)
3. Open the ****Manage list**** dropdown.
4. Select ****Merge lists****.
   ![Merge lists button.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28717882013211)
5. You'll want to choose whatever list you are using for SMS subscribers. You'll want to use the same lists you selected in your [Shopify integration settings](https://help.klaviyo.com/hc/en-us/articles/115005080407#h_01HSERAG9Y1DNHNSCHTKV3G04D).
   ![](https://klaviyo.zendesk.com/hc/article_attachments/32805259416091)
6. Choose whether to keep or delete your uploaded list from Shopify.
7. Click ****Merge****.

The merging process may take several minutes. For more information on merging lists, consult our [listing merging FAQ](https://help.klaviyo.com/hc/en-us/articles/115005078887#h_01H8YXX41PKBPHHVFJ751BD6CR).

## Outcome

You've now added historical Shopify SMS subscribers to your Klaviyo list.

## Additional resources

- [Getting started with Shopify](https://help.klaviyo.com/hc/en-us/articles/115005080407)
- [How to sync Shopify email subscribers to a Klaviyo list](https://help.klaviyo.com/hc/en-us/articles/115005080667)
