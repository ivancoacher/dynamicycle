<h1>Getting started with BigCommerce</h1>

## You will learn

Learn how to enable the BigCommerce integration in Klaviyo, add **Viewed Product** tracking, and confirm that all onsite tracking is working properly for your store.

When you integrate with BigCommerce, your historic ecommerce, customer, and catalog data is synced into your Klaviyo account. The integration automatically adds Klaviyo's onsite tracking snippet to your BigCommerce store, which allows you to add Klaviyo sign-up forms to your site and track when your customers are active on your site. The BigCommerce integration also sets up a real-time sync to capture future data.

## Before you begin

Before integrating, we recommend logging out of both BigCommerce and Klaviyo.

## How to integrate video

![](https://fast.wistia.com/embed/medias/cklrl4qtcm/swatch)

## Enable the BigCommerce integration

To integrate Klaviyo with BigCommerce:

1. Log in to your Klaviyo account.
2. Select ****Integrations****in the left-hand navigation.
3. Click ****Explore apps**** and search for BigCommerce, then click the card. Then, click ****Install****.
4. Click ****Connect to BigCommerce****, log in to BigCommerce when prompted, then click ****Install****.
5. Review the permissions and click ****Confirm**** to be brought back into Klaviyo.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28716053446555)
6. Under **Store URL**, enter your store’s permanent address. Your store's permanent address is not the same as your store's URL where customers visit your store. The permanent address is a special URL BigCommerce uses to manage your store.
   1. To find this address, go into your BigCommerce admin and navigate to ****Account Settings > Store Details****. Scroll down to find the ****Permanent Address**** for your store.
      ![BigCommerce store details page showing permanent address field with blurred address](https://klaviyo.zendesk.com/hc/article_attachments/28716063842075)
7. Check the box to automatically add Klaviyo onsite javascript, which will allow onsite tracking and forms.
8. Next, if you’d like to collect email subscribers at checkout, check ****Sync your BigCommerce email subscribers to Klaviyo****. This will subscribe contacts who opt in during a checkout or through BigCommerce footer form. Choose which Klaviyo list from the dropdown you would like to add subscribers to. If you prefer, you can [create a new list](https://help.klaviyo.com/hc/en-us/articles/115005078967-How-to-Create-and-Add-Contacts-to-a-New-List#create-a-new-list2) instead.
9. To collect SMS subscribers who opt in via BigCommerce, check the setting to ****Sync your BigCommerce SMS subscribers to Klaviyo****. Before you can enable this setting, you must first [set up SMS for your Klaviyo account](https://help.klaviyo.com/hc/en-us/articles/360035285472-How-to-Set-Up-SMS).
10. If you decide to collect SMS subscribers at checkout, choose the list you want them to be added to from the dropdown. You will also be prompted to include links to your Terms of Service and Privacy Policy, and copy a code snippet to your BigCommerce checkout file. For instructions on how to do this, follow our guide to [collecting SMS consent at checkout with BigCommerce](https://help.klaviyo.com/hc/en-us/articles/360058194032). You must also add disclosure language for TCPA compliance.
11. When you're done, click ****Complete setup****.

You've successfully enabled the BigCommerce integration.

## Confirm Onsite Tracking installation

When you integrated with BigCommerce, a Klaviyo.js file which enables onsite tracking was automatically installed in your BigCommerce store if you checked the relevant setting. Klaviyo.js does two things:

- It enables you to add Klaviyo sign-up forms to your site directly from your Klaviyo account.
- It adds **Active on Site** tracking, which allows you to track when your customers access your site.

No further action is required on your part, but you can verify that Klaviyo.js is working correctly.

1. In your Klaviyo account, click ****Integrations****.
2. In the upper right corner, click ****Manage data > Set up web tracking****. You already completed the first step when integrating, and the second step will be covered in the next section on **Viewed Product** tracking.
3. Go to the third step and enter your store URL in the box, then click ****Next****.
4. Click on the link that’s generated to be redirected to your store.
   ![Setup web tracking page in Klaviyo showing three steps, third step has a text box filled with a BigCommerce store URL and Next with a blue background](https://klaviyo.zendesk.com/hc/article_attachments/28716063844251)
5. Back in Klaviyo, check for the success button that data has been received. This means that web tracking is working successfully.
   ![Klaviyo setup web tracking page step 3 shows a box with a generated link, and Data received continue with arrow and green background](https://klaviyo.zendesk.com/hc/article_attachments/28716053427739)
6. Click the green success button to be brought back to your Klaviyo dashboard.

## Add Viewed Product tracking

**Viewed Product** tracking allows you to track when customers view your products. To enable **Viewed Product** tracking, you will need to  add a **Viewed Product** code snippet to your BigCommerce Theme file.

**Viewed Product** tracking is necessary for building flows such as a browse abandonment flow, which you can learn more about in [Creating a Browse Abandonment Flow](https://help.klaviyo.com/hc/en-us/articles/115002775252-Creating-a-Browse-Abandonment-Flow?utm_source=How%20to%20Integrate%20with%20Big%20Commerce%20Stencil%20Themes%20Viewed%20Product&utm_medium=Help%20Center%20article&utm_campaign=BC%20Viewed%20Product#build-your-own-browse-abandonment-flow9).

1. In your Klaviyo account, click ****Integrations****.
2. In the upper right corner, click ****Manage data >**** ****Set up web tracking****. You already completed the first step when integrating.
3. Copy the **Viewed Product** snippet from the second step.
   ![Klaviyo setup web tracking page step 2 showing viewed product code snippet in box](https://klaviyo.zendesk.com/hc/article_attachments/28716053433243)
4. Next, you'll paste the **Viewed Product** code snippet into your BigCommerce theme file. In a new tab, log in to your BigCommerce dashboard and navigate to ****Storefront**** > ****My Themes****.
5. From the **Current Theme**, click the ****Advanced Settings**** dropdown and click ****Edit Theme Files****. If you're working with a default theme, the option to edit theme files will not appear. First, make a copy of the theme, and then make your edits to the copy. Any edits you make will only apply to the theme you are editing. Note that if you change your theme in the future, you will need to install Viewed Product tracking to your new theme.
   ![BigCommerce My Themes page with Advanced dropdown open for current theme and Edit Theme Files highlighted in light blue](https://klaviyo.zendesk.com/hc/article_attachments/28716053430427)
6. In the editor, navigate to ****Templates > Pages****, scroll down, and click to open the ****product.html**** page.
7. At the bottom of this page, paste the Viewed Product code snippet. Then click ****Save all files.
   ![BigCommerce file editor showing product.html file with Klaviyo Viewed Product snippet added to bottom](https://klaviyo.zendesk.com/hc/article_attachments/28716053438363)****

You have now enabled Viewed Product tracking on all of your product pages.

## Data synced to Klaviyo

The BigCommerce integration syncs with Klaviyo in real-time.

After you've enabled your BigCommerce integration, it will sync the following information about your customers:

- Sales and order data, including which products were purchased, product images, price, and quantity.
- Customer information, including first name, last name, and how they found your store.

  Location information is only synced to Klaviyo if the customer has placed an order.
- Fulfillment, refund, and canceled order data.
- When people visit your website and what products and collections they view.

To view BigCommerce event data in your Klaviyo account:

1. Click the ****Analytics**** dropdown and select ****Metrics****.
2. Select ****BigCommerce**** from the filter drop-down on the upper right-hand side to display all BigCommerce events. BigCommerce events are associated with the BigCommerce icon.
   ![Klaviyo metrics tab filtered by BigCommerce with 6 BigCommerce metrics showing in list including Cancelled Order and Fulfilled Order](https://klaviyo.zendesk.com/hc/article_attachments/28716063859227)
3. Read more about [your BigCommerce Data](https://help.klaviyo.com/hc/en-us/articles/115005082587-Review-and-Understand-Your-BigCommerce-Data) for a full reference of all the types of data and specific events that sync to Klaviyo.

Klaviyo limits the number of unique metrics you can create to 200. When you approach this threshold, you will be alerted via a warning in your account, along with an email to the account owner.

## Outcome

You've successfully enabled the BigCommerce integration, confirmed that onsite tracking is working, and added **Viewed Product** tracking to your store.

## Next steps

Congratulations on getting set up! Now that you've got your integration running, it's time to start adding Klaviyo's core features so you can start making money and growing your business.

After you complete the items in this category, you'll be all set to get the most out of Klaviyo's features.

- [Set up your welcome series flow](https://help.klaviyo.com/hc/en-us/articles/115002775172-Create-a-Welcome-Series-Flow).
- [Set up your abandoned cart flow](https://help.klaviyo.com/hc/en-us/articles/115002779411-Create-an-Abandoned-Cart-Flow).
- [Add a Klaviyo sign-up form to your site](https://help.klaviyo.com/hc/en-us/articles/360002035871-Install-Klaviyo-Signup-Forms). We also have go-to options for using your existing forms or third-party form providers, but we recommend Klaviyo forms because they are free and you can target key Klaviyo segments.
- Create your core segments ([Engaged](https://help.klaviyo.com/hc/en-us/articles/115000200072-Create-an-Engaged-Master-List), [Unengaged](https://help.klaviyo.com/hc/en-us/articles/115005078347-List-Cleaning), [VIP](https://help.klaviyo.com/hc/en-us/articles/115005065707-Create-a-Segment-of-VIP-Customers-)).
- [Send your first campaign](https://help.klaviyo.com/hc/en-us/articles/115005054847-Create-and-Send-a-Campaign).

## Additional resources

- [BigCommerce data reference](https://klaviyo.zendesk.com/hc/en-us/articles/115005082587)
- [How to create a custom added to cart event for BigCommerce](https://help.klaviyo.com/hc/en-us/articles/360024310292-Create-a-Custom-Added-to-Cart-Event-for-BigCommerce)
- Need more help getting started? Check out [Klaviyo's Agency Partners](https://klaviyo.partnerpage.io/?utm_source=helpcenter&utm_medium=integrations)
