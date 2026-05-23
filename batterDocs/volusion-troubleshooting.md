<h1>Volusion Troubleshooting</h1>

## Volusion Placed Order Data isn’t Reporting in Klaviyo

This may be an issue with your Volusion API settings that allow data to be exported. To fix this, navigate to the **Inventory** tab of your Volusion admin panel. Select **Import/Export**from the dropdown menu.

![647863](https://klaviyo.zendesk.com/hc/article_attachments/28716301437851)

Click on **Volusion API** to access the main API page. In the **Generic** section, you will find the option to RUN the export of your store’s Generic/Orders. Once the export is ran, the page will refresh.

![647864](https://klaviyo.zendesk.com/hc/article_attachments/28716301441691)
![647865](https://klaviyo.zendesk.com/hc/article_attachments/28716328819611)

After clicking "RUN" to export your Generic Orders, an API URL is generated at the top of the page. the URL for example, would appear as so: https://storename.com/net/WebService.aspx?Login=user@storename.com&EncryptedPassword=****ABC123...****&EDI\_Name=GenericOrders

The value that appears between "EncryptedPassword=" and "&EDI\_Name=GenericOrders" (bolded above) would serve as your API Key. Use this to re-establish your integration settings from the Integrations tab of your Klaviyo dashboard.

Upon completion, test by clicking onto the **Metrics** tab of your Klaviyo account. View recent activity for the Volusion Placed Order metric to see if any new data has synced in Klaviyo.

If you see new data for the Placed Order metric, [contact our Success Team](https://help.klaviyo.com/hc/en-us/requests/new) to run a gap fill for missing orders in Klaviyo or for any further assistance.

For additional information on exporting data using the Volusion API, please refer to [Volusion support](https://support.volusion.com/hc/en-us/articles/208837888-Exports-Orders-Export-Developer-).

## People See an "Invalid Input" Error When Clicking my Email Links

The "email to web tracking" feature in Klaviyo uses click tracking to tie activity to a user who arrives to your website through a Klaviyo email before we would originally be able to identify him/her (such as when they make a purchase or subscribe to your newsletter).

|  |
| --- |
| Volusion does not support the URL format that our click tracking uses and produces an error when a user tries to visit your store through one of these links, so this feature will have to be disabled in Klaviyo to make sure links in your email follow through to your Volusion store correctly. |

If you don't disable this tracking, you customers will likely see the following error when clicking any links within emails that point to your website:

![647866](https://klaviyo.zendesk.com/hc/article_attachments/28716301452059)

You can disable this tracking in your account settings (<https://www.klaviyo.com/account>) under **Email Settings******>******Email to Website Tracking**.

![647867](https://klaviyo.zendesk.com/hc/article_attachments/28716301454491)

The only functionality lost with disabling this feature is the ability to track a new profile on your website through an email they clicked. As long as you have the Klaviyo web tracking analytics on your website, however, we will still be able to track users as soon as we get their email address through either a purchase in your store or after they sign up for a newsletter.
