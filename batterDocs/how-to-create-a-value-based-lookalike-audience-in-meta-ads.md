<h1>How to create a value-based lookalike audience in Meta Ads</h1>

## You will learn

Learn how to create a value-based lookalike audience in Meta Ads using CLV (customer lifetime value) data from Klaviyo. Essentially, when you export a list or segment from Klaviyo, you can upload it as a Facebook custom audience and use it as a source to create a similar, lookalike audience. In this case, because you're using CLV data, your lookalike audience will be value-based, giving you a better idea of how much to spend on advertising to this group of customers.

## Before you begin

Please note that CLV data will only be available to export when you meet the following requirements:

- At least 500 customers have placed an order. This does not refer to active profiles, but the number of people who have actually made a purchase with your business. If the CLV section is on a profile but is blank, this means we don't have enough data on that individual to make a prediction.
- You have an ecommerce integration (e.g., Shopify, BigCommerce, Magento, etc) or use our API to send placed orders.
- You have at least 180 days of order history with the current integration and have orders within the last 30 days.
- You have at least some customers who have placed three or more orders.

You can read more about [predictive analytics in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115005247088-Contact-Profiles-in-Klaviyo#predictive-analytics4) as well as our guide to [segmenting by CLV](https://help.klaviyo.com/hc/en-us/articles/360013201072).

## Export your CLV segment

1. Select a segment you want to export depending on your business and advertising goals; for example, a VIP segment.
2. Follow the steps outlined in our article, [How to export a list or segment to a CSV file](https://klaviyo.zendesk.com/hc/en-us/articles/115005078687).
3. On the **Export Review** screen, include the **Email** and **Total Customer Lifetime Value** properties. You can include more properties as well if you'd like. Check the details in [Meta's documentation](https://www.facebook.com/business/help/185705781836755).
   ![Export review page with properties list and Total Customer Lifetime Value checked](https://klaviyo.zendesk.com/hc/article_attachments/28716054141723)
4. Your segment will save to your computer as a CSV file. Use this CSV in the next section when creating a source custom audience in Meta.

## Create a source custom audience

1. Log in to your Meta ad account and create a new custom audience.
2. Select ****Customer File > Use a file that includes customer lifetime value (LTV)**** in the workflow.
   ![Create a custom audience page in Facebook with Use a file that includes customer lifetime value highlighted in white](https://klaviyo.zendesk.com/hc/article_attachments/28716054138651)
3. If you haven't already, you'll be prompted to accept the terms of service for working with value-based audiences. To do so, click ****I Accept****.
   ![Requirements for using value-based custom audiences agreement in Facebook with I Accept at the bottom with dark blue background](https://klaviyo.zendesk.com/hc/article_attachments/28716064596635)
4. Next, add your CSV file for upload by selecting the **Original Data Source** and **Name Your Audience** from the dropdown menus.
5. On the next screen, choose your customer value column. From the dropdown, select ****Total Customer Lifetime Value****to map your Klaviyo Total CLV to Facebook's LTV.
   ![Create a customer list custom audience with LTV page in Facebook](https://klaviyo.zendesk.com/hc/article_attachments/28716064597659)
6. Next, preview and map your data; then, finish creating your audience. You'll now have the option to create a lookalike audience, which we'll cover in the next section.

## Create a value-based lookalike audience

1. After creating your CLV custom audience, pick up where you left off and click ****Create a lookalike audience.
   ![Next steps create a lookalike audience highlighted in white on create a customer list custom audience page in Facebook](https://klaviyo.zendesk.com/hc/article_attachments/28716064599707)****
2. Next, for **Select Your Lookalike Source**, choose the custom CLV audience you created in the previous section.
3. Enter your audience location and size, and click ****Create Audience****.
   ![Create a lookalike audience page in Facebook](https://klaviyo.zendesk.com/hc/article_attachments/28716054151835)
4. Your value-based lookalike audience is now available for you in Meta for ad targeting. Read more about [creating a value-based lookalike audience](https://www.facebook.com/business/help/185705781836755) in Meta's documentation.

## Connecting a source custom audience through Klaviyo

When you integrate a Klaviyo list or segment to a source custom audience, new profiles added to the list or segment are synced to the Meta custom audience. You can sync a Klaviyo list or segment to a source custom audience.

If you connect a list or segment to a custom audience through Klaviyo, CLV information is not automatically passed over to Meta. New customers added to your list or segment in Klaviyo will be synced over to Meta, but because we do not natively support passing over CLV data, these customers will be added to your source customer audience with a default CLV value. This could potentially skew the customers added to any value-based lookalike audiences connected to your source audience.

## Outcome

You've now learned how to create a value-based lookalike audience in Meta Ads using Klaviyo CLV.

## Additional resources

- [Grow your business with Klaviyo's Meta Ads integration (Klaviyo Academy course)](https://academy.klaviyo.com/grow-your-business-with-klaviyos-facebook-advertising-integration)
- [How to enable advanced targeting on Facebook and Instagram](https://help.klaviyo.com/hc/en-us/articles/360039769672-Guide-to-Advanced-Targeting-on-Facebook-and-Instagram)
