<h1>How to collect SMS consent at checkout on Magento 2</h1>

## You will learn

Learn how to collect SMS consent at checkout for Magento 2.

Consent will be synced to Klaviyo once someone provides their phone number, opts in to SMS marketing, and then places an order.

## Before you begin

Note the following about collecting SMS consent at checkout:

- You must have
  - [Set up SMS in Klaviyo](https://klaviyo.zendesk.com/hc/en-us/articles/4404274419355)
  - [Created a mobile terms of service](https://klaviyo.zendesk.com/hc/en-us/articles/360049177511)
  - Followed [best practices for your privacy policy](https://klaviyo.zendesk.com/hc/en-us/articles/4404199571867)
- You must be on [version 2.1.0 or higher of the Magento 2 plugin](https://help.klaviyo.com/hc/en-us/articles/115005254348) to use this feature
  - It is not available for Magento 1 stores
- You can only collect SMS consent in countries [where Klaviyo SMS is available](https://help.klaviyo.com/hc/en-us/articles/4402914866843)

Also, if you’re syncing customers to a list with double opt-in, customers will get a text confirming their subscription before they are added to that list.

## Set up SMS consent at checkout

1. Navigate to your Magento 2 store.
2. From the left-hand sidebar, navigate to ****Stores > Configuration****. ****![Configuration highlighted in Magento's navigation](https://klaviyo.zendesk.com/hc/article_attachments/28720772122651)****
3. Once you’re on the **Configuration** page, navigate to ****Klaviyo > Consent at Checkout****. **![Consent at Checkout option highlighted in the Configuration page](https://klaviyo.zendesk.com/hc/article_attachments/28720772117147)**
4. Expand the **SMS** section.
   - This is a separate section than the one for collecting email consent.
5. Under **SMS**, select ****Yes**** for **Subscribe contacts to SMS marketing at checkout**.
6. Choose the list you want your SMS contacts to sync to (e.g., SMS Subscribers).
   - If you also gather email subscribers, choose a different list for SMS than the one you use for email.
7. Optional: Edit the text for the SMS opt-in checkbox.
   - The default text is as follows:
     **Subscribe to SMS**
8. Optional: Edit the SMS consent text.
   - The default text is as follows:
     **By checking this box and entering your phone number above, you consent to receive marketing text messages (such as [promotion codes] and [cart reminders]) from [company name] at the number provided, including messages sent by autodialer. Consent is not a condition of any purchase. Message and data rates may apply. Message frequency varies. You can unsubscribe at any time by replying STOP or clicking the unsubscribe link (where available) in one of our messages. View our Privacy Policy [link] and Terms of Service [link].**
9. In this disclosure language, replace the **[link]** placeholders to include direct links to your privacy policy and terms of service pages.
   - Example:
     **View our Privacy Policy (<https://www.klaviyo.com/legal/privacy-policy>) and Terms of Service (<https://www.klaviyo.com/legal/terms-of-service>)
     ![Configuration for adding SMS consent at checkout to a Magento store](https://klaviyo.zendesk.com/hc/article_attachments/28720772127515)**
10. Optional: Edit the sort order to change the placement of the email and SMS consent boxes.
    - By default, these boxes appear under the first email input and shipping phone number field, respectively.
    - If you haven’t rearranged the checkout page, you do not need to change the sort order. If you have changed the layout, adjust the sort order accordingly.
      ![Example of a Magento checkout page when SMS consent at checkout is active](https://klaviyo.zendesk.com/hc/article_attachments/28720760346907)
11. When you're done, click ****Save Config**** in the upper right.

## Outcome

Now, when someone adds their phone number, clicks the SMS opt-in checkbox, and places their order, their consent will sync to Klaviyo. This allows you to more quickly and easily grow your SMS list and reach more customers via this channel.

Note that consent will not sync until they finish placing the order and, if applicable, confirm their subscription due to double opt-in.

## Additional resources

- Learn how to [write impactful SMS copy](https://academy.klaviyo.com/en-us/courses/write-impactful-sms-copy/1823767)
- Learn the [basics of using SMS and email together](https://help.klaviyo.com/hc/en-us/articles/360056849631)
