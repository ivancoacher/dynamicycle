<h1>How to set up extended ID cookie tracking</h1>

## You will learn

Learn how to set up extended ID to compliantly capture and track subscriber interactions with your brand for longer. Extended ID is a first-party identity graph feature that allows you to track and hold cookies for up to 1 year. Thus allowing you to identify these interactions and behaviors longer to target, segment, and automate marketing messages.

## Before you begin

Please note the following items related to the extended ID:

- Extended ID is available on all Klaviyo paid plans.
- Extended ID does not provide integrations with conversion APIs (CAPIs) and support for probabilistic identifiers (i.e., identifiers like IP address, device data, click ID, location, or user agent).
- Re-identification tracking across a company, devices, and browsers are not supported
- Extended ID does not use fingerprinting technology.

If you choose to turn on extended ID, it is strongly suggested that you re-issue your cookie notices to your customers and inform them that Klaviyo will use a first-party cookie to re-issue the Klaviyo cookie. This will allow Klaviyo and your business to re-identify users after their browser cookie expires. Furthermore, it is recommended that you update your privacy notice to ensure that your customers are notified of this re-identification process.

## How does extended ID work?

Extended ID works by leveraging common deterministic identifiers (i.e., exact unique identifiers). For other platforms or solutions, you will need to set up custom identifiers.

Extended ID cannot automatically create new profiles based on shopper info from other sites. A shopper needs to already have a Klaviyo profile for extended ID to re-identify them and update their Klaviyo identity cookie.

## Turning on extended ID

1. Click on the account menu in the lower left of your account.
2. Choose ****Settings**** from the menu.
   ![Settings page in account menu](https://klaviyo.zendesk.com/hc/article_attachments/32053902569883)
3. Navigate to the ****Data**** tab.
4. In the **Extended ID** section, click ****Enable****. Once you click ****Enable****, your account will start extending the tracking of cookies.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/45139567095707)

   Once enabled, Klaviyo will begin to re-identify users using other first party identifiers from your brand's site. By default we attempt to use the following common identifiers

   |  |  |  |
   | --- | --- | --- |
   | ****Type**** | ****Platform**** | ****Identifier**** |
   | E-commerce platform (if applicable) | Shopify | \_shopify\_y |
   | E-commerce platform (if applicable) | Salesforce | \_\_cq\_uuid |
   | Analytics tools | Google Analytics | \_ga |
   | Ad network | Microsoft Clarity | \_clck |
   | Ad network | Microsoft Bing | \_uetvid |
   | Ad network | Snapchat | \_scid |
   | Ad network | Tiktok | \_ttp |
   | Ad network | Reddit | \_rdt\_uuid |
5. Optional: on the **Add custom identifiers**, fill in the name of your custom identifier in the **Enter Custom Identifier** field. Add your cookie value in the **Key** field. Keep in mind that this information is commonly stored as key-value pairs. For example, in the cookie user\_id=12345, the “user\_id” is your key and “12345” is the value. Then, open the **Location/source** dropdown to find and select your tool.
6. Optional: click the ****+ Add**** button to add more custom identifiers as needed.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/45139588163867)
7. Optional: in the upper right, click ****Save****. Once you have saved your custom identifier, you will be brought to the initial setup screen showing it’s status as **Verifying**. Note that it could take up to 2 weeks for the identifier to be verified.

Once your custom identifier has been verified, the status on the setup page will change to **Active**. This now means that any tracking going forward has been extended for that solution. However, if your status is **Failed**, the Extended ID system found that the identifier you provided is not universally unique enough to use for Extended ID. To avoid overlapping data across profiles in Klaviyo, the identifier has been blocked and will not be used for Extended ID identification.

## Disabling extended ID or specific identifiers

If you have a solution or tool connected that you no longer wish to have extended tracking for, you can disable them. Additionally, if you wish to turn off extended ID completely across all of your tools, you can do that as well.

By disabling one or all extended ID identifiers, you will immediately revert back to Klaviyo [default tracking settings](https://help.klaviyo.com/hc/en-us/articles/360034666712).

1. Click on the account menu in the lower left of your account.
2. Choose ****Settings**** from the menu.
   ![Setings page in account menu](https://klaviyo.zendesk.com/hc/article_attachments/32053902569883)
3. Navigate to the ****Data**** tab.
4. Optional: in the **Extended ID** section, click on the 3 dot menu in the upper left. Choose ****Disable Extended ID**** and click ****Disable**** to confirm.

## Measuring the impact of extended ID

To view the impact of extended ID on your brand's ability to identify visitors, you can leverage the **Active on Site** event.

1. Navigate to ****Analytics**** > ****Metrics**** > ****Active on Site****.
2. Add the filter ****By > extended\_id****.

This demonstrates the number of additional active on site events that were captured due to extended ID compared to Klaviyo's standard client-side cookies. Extended ID events have a value of **1.0** (i.e., true) while events captured with Klaviyo's standard cookie tracking have a value of **0.0** (i.e., false).

![](https://klaviyo.zendesk.com/hc/article_attachments/36116155646619)
