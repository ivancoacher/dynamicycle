<h1>Getting started with Shopify</h1>

## You will learn

Learn how to integrate Klaviyo with Shopify in order to bring your customer profile and order data into Klaviyo and reach customers with targeted messaging. Additionally, enable Klaviyo onsite tracking and sign-up forms, and sync data from Klaviyo to Shopify.

## Before you begin

If you are migrating from another ESP that is currently integrated with your Shopify store, make sure to disconnect your prior ESP from Shopify before integrating Shopify with Klaviyo. Failure to disconnect your old integration could result in double opt-in emails sending to your existing subscriber list.

## Video help

Learn how to integrate with Shopify using our step-by-step video!

![](https://fast.wistia.com/embed/medias/hcc8jhfi2w/swatch)

## How to integrate

1. In Klaviyo, select the ****Integrations**** tab.
2. Click ****Explore apps****.
3. Search for **Shopify** and click the card, then click ****Install****.
4. Paste the URL of your Shopify store in the box. Make sure that it is in the format **mystore.myshopify.com**.
5. Click ****Connect to Shopify****. This will take you to your Shopify account. You may be prompted to log in to Shopify.
6. After being brought into Shopify, review the permissions and click ****Install app**** to be redirected to Klaviyo.
7. Confirm the integration by clicking ****Integrate****, which will bring you back to the integration settings page.
8. You will be prompted to configure onsite tracking after connecting to Shopify, so this section will not yet be available.
9. Check the **Sync your Shopify email subscribers to Klaviyo** box to automatically add customers who accept email marketing at checkout, or sign up to any Shopify sign-up form, to the list you select from the dropdown.

   - As a [best practice for collecting consent](https://help.klaviyo.com/hc/en-us/articles/360003536031#01H8KRZQN97W49R600942Z4F4R), you should customize the **Accepts marketing** checkbox label in Shopify within your checkout settings.
10. If you selected the prior setting: Select a list to add email subscribers to from the dropdown. We recommend selecting your main email list that triggers your welcome series.
    ![](https://klaviyo.zendesk.com/hc/article_attachments/45236419416987)
11. Check the **Sync your Shopify SMS subscribers** to Klaviyo box to automatically add all future customers who accept SMS marketing in Shopify (including at checkout and in Shopify sign-up forms) to the list you select from the dropdown. You can always set up SMS and edit this setting later. Note that consent will only sync to Klaviyo if the person is subscribing to SMS in Shopify for the first time. To add historical SMS subscribers, follow the steps in [How to add historical Shopify SMS subscribers to your list](https://help.klaviyo.com/hc/en-us/articles/25184840445467).
12. If you selected the prior setting: Select a list to add SMS subscribers to from the dropdown. We recommend using separate lists for email and SMS subscribers.
13. Check the **Sync Shopify Markets to Klaviyo** button to automatically sync existing and future international markets catalogs.
14. Check the setting **Sync profiles and profile data from Klaviyo to Shopify** if you want to sync any data. We recommend syncing all profiles and all types of data to Shopify. If you checked this setting, do the following:
    1. Choose whether to sync updates for either all Klaviyo profiles, or only for profiles that already exist in Shopify.

       If you choose all profiles, Klaviyo will create new customers in Shopify for all profiles (existing and new) created in Klaviyo. This includes profiles synced from other Klaviyo integrations, or added through list imports, even if they have not interacted with your Shopify store.
    2. Choose which profile data you’d like to sync: Name, email address, phone number, Email subscription status, SMS subscription status (if you have SMS enabled), email events, SMS events, and custom profile properties. If you don’t yet have any custom properties in your Klaviyo account, you will see an option to sync all properties. If you have existing custom profile properties in your Klaviyo account, you can configure which properties you want synced.
       ![](https://klaviyo.zendesk.com/hc/article_attachments/28720891731099)
15. After configuring your settings, click ****Complete setup****.
16. A green success callout will indicate that your data is syncing with Klaviyo.

    It is not recommended to update custom profile properties in Klaviyo that were synced via Shopify (such as Shopify tags), since these will be overwritten the next time your integration syncs.

    Next, you’ll enable Klaviyo onsite tracking, which consists of multiple events. Using these tracking events can help you engage identifiable browsers of your store. Additionally, enabling tracking will allow you to use Klaviyo sign-up forms. Please note that enabling the sync of Shopify data to Klaviyo, and Klaviyo data to Shopify (steps 8 through 12 above) will help you see more onsite tracking events in your account due to more profiles syncing.

    Based on your Customer Privacy settings in Shopify, Klaviyo may not track onsite events for visitors to your Shopify store in the EU, EEA, UK and Switzerland, unless they have provided consent.
17. In the **Onsite tracking** section, check ****Track behavioral events**** to enable tracking for **Viewed Collection**, **Submitted Search**, and **Added to Cart**. Two other events, **Viewed Product** and **Active on Site**, are enabled by default and they will start tracking once you enable the app embed.
18. You’ll see a message calling out that your Klaviyo app embed is turned off. Click ****Turn on**** to be brought to Shopify.
    ![](https://klaviyo.zendesk.com/hc/article_attachments/28707509153563)
19. If prompted, sign in to Shopify using the account you integrated with Klaviyo.
20. You’ll be brought to your theme setting’s App embeds tab. Make sure the Klaviyo app embed is toggled on.
    ![](https://klaviyo.zendesk.com/hc/article_attachments/28707538327323)
21. Click ****Save**** in your theme editor.
22. Navigate back to your Shopify integration settings page in Klaviyo, and refresh the page if needed. You should see a green banner indicating that your app embed is now enabled.

![](https://klaviyo.zendesk.com/hc/article_attachments/28707882015771)

You’ve now integrated Klaviyo with Shopify and set up onsite tracking.

If you need to update these settings, you can return to the integration settings page by clicking ****Integrations****, and selecting Shopify. Then, make your changes and click ****Update Settings****.

Note that your product catalog in Klaviyo will autopopulate with the **myshopify.com** URL. [Contact Klaviyo support](https://help.klaviyo.com/hc/en-us/articles/115001002272-How-to-Contact-Support)to request an update to this setting.

The URL can be updated from this:

`https://[INSTANCE].myshopify.com/products/[PRODUCT_HANDLE]`

To this:

`https://[STOREFRONT_URL]/products/[PRODUCT_HANDLE]`

## Troubleshooting

Having trouble resolving errors with your Shopify integration? Check out our article [Troubleshooting your Shopify integration](https://help.klaviyo.com/hc/en-us/articles/4403927899291-Troubleshooting-Your-Shopify-Integration).

Are you trying to understand more about the behavior of Klaviyo’s Shopify integration?

- [Learn about onsite tracking and how to test it](https://help.klaviyo.com/hc/en-us/articles/4425956184731)
- [Learn about the email subscriber sync](https://help.klaviyo.com/hc/en-us/articles/115005080667)
- [Learn about data synced from Shopify to Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115005080447)
- [Learn about data synced from Klaviyo to Shopify](https://help.klaviyo.com/hc/en-us/articles/360030919351)
- [Learn about Shopify Markets in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/45224022467739)

## Outcome

You've now integrated Shopify with Klaviyo, and enabled Klaviyo onsite tracking and sign-up forms for your Shopify store.
