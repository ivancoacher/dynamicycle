<h1>How to update Klaviyo after switching ecommerce platforms</h1>

## You will learn

Learn about the areas of Klaviyo that need to be updated when you switch from one ecommerce platform to another. It is completely possible to switch ecommerce platforms while keeping the same Klaviyo account, but there are some important steps to keep in mind to ensure that your sign-up forms, flows, and other Klaviyo features continue to perform as expected.

## 1. Migrate historical data

### Between ecommerce platforms

Before integrating a new ecommerce platform with Klaviyo, make sure you've fully migrated all the historic purchase data from your old ecommerce platform to your new ecommerce platform. This will ensure that your reporting in Klaviyo is consistent, and you won't have to reference metrics from both ecommerce platforms in Klaviyo segments and flows.

### From your ecommerce platform to Klaviyo

If you need to add historical purchase data directly to Klaviyo from a previous ecommerce platform that Klaviyo doesn't have a prebuilt integration for, [you can follow these steps to manually add event data to Klaviyo.](https://help.klaviyo.com/hc/en-us/articles/115005081247-How-to-Manually-Import-Historical-Event-Data)

## 2. Integrate with your new platform

For each of our built-in ecommerce integrations, we have corresponding documentation. After finding the appropriate instructions for your new platform, you can integrate and new metrics will begin to populate in your account.

- [Shift4Shop (formerly 3dcart)](https://help.klaviyo.com/hc/en-us/articles/115005083107-Integrate-with-3dcart)
- [BigCommerce](https://help.klaviyo.com/hc/en-us/sections/115001509808-BigCommerce)
- [Magento 1](https://help.klaviyo.com/hc/en-us/articles/115005082187-Integrate-with-Magento-1-x-CE-and-EE-)
- [Magento 2](https://help.klaviyo.com/hc/en-us/articles/115005254348-Integrate-with-Magento-2-x-CE-and-EE-)
- [Mi9](https://help.klaviyo.com/hc/en-us/articles/360020156011-How-to-Integrate-with-Mi9)
- [OpenCart](https://help.klaviyo.com/hc/en-us/articles/115005255408-Integrate-with-OpenCart)
- [PrestaShop](https://help.klaviyo.com/hc/en-us/articles/360054551492-How-to-Integrate-with-PrestaShop)
- [Salesforce Commerce Cloud](https://help.klaviyo.com/hc/en-us/articles/360033744951-How-to-Integrate-with-Salesforce-Commerce-Cloud)
- [Shopify](https://help.klaviyo.com/hc/en-us/articles/115005080407-Integrate-with-Shopify)
- [Spree](https://help.klaviyo.com/hc/en-us/articles/115005255448-Integrate-with-Spree)
- [Volusion](https://help.klaviyo.com/hc/en-us/articles/115005083427-Integrate-with-Volusion)
- [Wix](https://klaviyo.zendesk.com/hc/en-us/articles/6202669053723)
- [WooCommerce](https://help.klaviyo.com/hc/en-us/articles/115005255808-Integrate-with-WooCommerce)

If you don't see your new ecommerce integration above, you'll need to [use a custom integration instead](https://developers.klaviyo.com/en/docs/guide_to_integrating_a_platform_without_a_pre_built_klaviyo_integration).

## 3. Confirm new data is syncing to Klaviyo

After you integrate your new platform, you will be able to view your metrics from two different stores by clicking the ****Analytics**** dropdown and selecting ****Metrics****. This includes metrics like **Placed Order** and **Checkout Started**.

You may wish to [delete the legacy metrics](https://help.klaviyo.com/hc/en-us/articles/115005076787-Managing-Metrics#how-to-delete-a-metric) from your old platform, but deleting the metrics will also delete all historical data associated with that metric from your account. Only do this if you do not want to leverage this historical data (i.e. previous **Placed Order events**), or if you've already migrated data from your old ecommerce platform to your new platform.

## 4. Set up onsite tracking

Be sure to follow all the integration instructions listed in the respective documents, including enabling [Active on Site and Viewed Product tracking](https://help.klaviyo.com/hc/en-us/articles/115005076767) (known together as "onsite tracking") on your new site.

## 5. Update sign-up forms

Update your ecommerce platform's sign-up forms to make sure they are syncing to a Klaviyo list. With many ecommerce integrations, this is done through a setting when you enable the integration. You can also replace your platform's sign-up forms with [Klaviyo sign-up forms](https://help.klaviyo.com/hc/en-us/articles/360026474752-Guide-to-Creating-a-Signup-Form).

## 6. Clone and update flows

You will likely have [metric triggered flows](https://help.klaviyo.com/hc/en-us/articles/360003057151-Create-a-Metric-Triggered-Flow) in your account that need to be connected to the new metrics. While you cannot change a flow trigger directly, you can [clone the flow](https://help.klaviyo.com/hc/en-us/articles/115002775032-Clone-a-Flow) and select a new trigger for the correct metric.

If any of the flows have filters, be sure to double-check that these are correctly mapped.

If you don't clone your metric triggered flows, no new contacts who take the trigger action will be queued up, since no more data will be flowing into Klaviyo from your legacy platform.

Any ecommerce metric triggered flow templates must also be updated if they include dynamic data. For example, the template tags used in your abandoned cart flow for Platform A will be different from the template tags used for Platform B. These flows include:

- Abandoned cart
- Post-purchase
  - New customer thank you
  - Repeat customer thank you
  - Product review / cross sell

The quickest way to update your cloned flow with the correct dynamic data is to:

1. Navigate to ****Browse Ideas**** within the ****Flows**** tab.
   ![Flows tab in Klaviyo showing Abandoned Cart flow in list with yellow status](https://klaviyo.zendesk.com/hc/article_attachments/28717380554907)
2. Select the flow that you would like to rebuild. If you are migrating to Platform B, you will want to choose the flow with the Platform B logo next to it.
3. Find the dynamic code block or section and save it.
4. Next, navigate to your new, cloned template and swap out the existing dynamic content with the saved content. This saves you the time of redesigning your existing flow templates from scratch.
5. Make sure to [set your cloned flows to **Draft** or **Manual**](https://help.klaviyo.com/hc/en-us/articles/115002774932#h_01H9JGTZ8RVQANQHGVRJ6V4W63) so that messages do not start sending automatically during migration. You can turn your flows live once you have completed the migration process.

## 7. Confirm welcome series setup

Klaviyo's ecommerce integrations are not set up to exclude purchasers who subscribe at checkout from entering a welcome flow. If you want to exclude these profiles from triggering your Welcome Series, add a filter "Placed Order zero times over all time" to your flow.

## 8. Clone segments

Additionally, any segments that have metric-based conditions will need to be recreated to incorporate the new metric. [Clone all segments](https://help.klaviyo.com/hc/en-us/articles/24898429283739) with metric-based conditions and edit them to pull in information from the new, correct metric.

## 9. Disable your old integration

Once you have completely stopped using your legacy platform, you can disable the integration selecting the ****Integrations**** tab, then looking for the integration on the list. Once you select the integration, click ****Manage integration > Disable integration****.

## Outcome

You've now updated Klaviyo after switching ecommerce platforms.

## Additional resources

- [Getting started with Klaviyo (Academy course)](https://academy.klaviyo.com/getting-started-with-klaviyo)
- Need more help integrating with Klaviyo? Check out [Klaviyo's Agency Partners](https://klaviyo.partnerpage.io/?utm_source=helpcenter&utm_medium=integrations)
