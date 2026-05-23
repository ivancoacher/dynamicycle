<h1>How to migrate from Mailchimp</h1>

## You will learn

Learn how to use Klaviyo’s Mailchimp integration to migrate your Mailchimp data to Klaviyo.

After you’re completely transitioned to Klaviyo, we recommend you remove your Mailchimp integration.

Klaviyo syncs the following data from Mailchimp:

- Subscriber information (including unsubscribes and cleaned contacts)
- Mailchimp audiences (synced to Klaviyo lists)
- Email receives, clicks, and opens
- Mailchimp ratings

## Before you begin

If your Mailchimp account is currently integrated with your Shopify store, and you've already [integrated Shopify with Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115005080407), make sure to disconnect Mailchimp from Shopify before integrating Mailchimp with Klaviyo. Failure to disconnect your old integration could result in double opt-in emails sending to your existing subscriber list.

## Checklist

Migrating from Mailchimp to Klaviyo requires four key steps:

1. Integrate your ecommerce platform with Klaviyo
2. Integrate Mailchimp with Klaviyo
3. Migrate your email templates from Mailchimp to Klaviyo
4. Sunset your Mailchimp account

## How to integrate with Mailchimp

Integrating your Mailchimp account with Klaviyo pulls over all of your contact data, including when contacts received, opened, and clicked emails.

1. First, you'll need to obtain a Mailchimp API key. We recommend creating a new key specifically for the Klaviyo integration, but you can use an existing key if you would like.
2. You can get your Mailchimp API key by logging in to Mailchimp, clicking your profile icon, then navigating to ****Account & billing > Extras > API keys****.
3. Click ****Create a Key****.
4. Name your key, then click ****Generate Key****.
5. Click ****Copy Key to Clipboard****. Then, save it securely.
6. Once you've obtained your API key from Mailchimp, log in to Klaviyo.
7. Select the ****Integrations**** tab.
8. Click ****Explore apps**** and search for Mailchimp. Click on the Mailchimp card, then click ****Install****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/31880103276059)
9. On the setup page, paste in the Mailchimp API key in the specified field.
10. Click ****Connect to Mailchimp****.
11. Once you've pasted in your API key, click to review the **Advanced o**ptions:
    - **Collect open and click data for Mailchimp campaigns** - check this option to sync Mailchimp engagement.
    - **Create Klaviyo lists from Mailchimp audiences** - check this option to sync all your existing Mailchimp audiences.
    - **Only sync contacts from specific audiences** - check this option to only sync specific Mailchimp audiences. You'll be prompted to choose which audiences to sync. You must check the previous option to c**reate Klaviyo lists from Mailchimp audiences** for this option to work.
      ![Klaviyo’s Mailchimp integration setup page with options for syncing audiences](https://klaviyo.zendesk.com/hc/article_attachments/28723506902811)
12. If you select **Only sync contacts from specific audiences** in **Advanced**, you'll need to designate all the Audience IDs to which campaigns were previously sent. Even if a different synced audience contains the same contact, if a campaign was not originally sent to that audience, you won't see complete engagement data for that campaign.
13. Klaviyo will only sync campaign data for campaigns with the "Sent" status. Data from campaigns with the "Sending" status won't be synced. Note that Klaviyo won't sync entire campaigns; we sync open and click data, and if you wish to re-create Mailchimp campaigns in Klaviyo, you can learn how to export your Mailchimp email templates below.
14. After you click ****Connect to Mailchimp****, data will start syncing over within a few minutes.

## Sync frequency

When you first integrate Klaviyo and Mailchimp, we will sync all your contacts and the last 90 days of campaign data. This is called a historical sync, and only occurs once.

After the historical sync, Mailchimp data syncs to Klaviyo as follows:

- Existing audiences sync every 30 minutes.
- New audiences and/or campaigns sync every 6 hours.
- Existing campaign activity syncs after campaigns are sent to capture recipient data.

## Review your Mailchimp data

Klaviyo automatically syncs all contacts, along with subscription info, from Mailchimp (unless you select **Only sync contacts from specific audiences**). You’ll see whether contacts are subscribed or unsubscribed, and contacts that have been marked as “cleaned” or have bounced will be added to your suppression list in Klaviyo.

We subscribe contacts based on whether they were subscribed in Mailchimp, unless the profile already exists in Klaviyo. If the profile already exists, we use the more recent consent status based on its timestamp.

If you delete a contact in Mailchimp after integrating with Klaviyo, they won't be deleted in Klaviyo.

If a profile already exists in Klaviyo as an active profile before you add the Mailchimp integration, and it has been cleaned/bounced in Mailchimp, it won’t be suppressed in Klaviyo. To suppress these contacts, you can export them from Mailchimp as a CSV and upload them to your suppression list in Klaviyo.

Additionally, our Mailchimp integration:

- Syncs open and click data for Mailchimp campaigns, if you checked the **Collect open and click data for Mailchimp campaigns** setting.
- Creates Klaviyo lists from Mailchimp audiences, if you checked the **Create Klaviyo lists from Mailchimp audiences** setting.
- Syncs Mailchimp ratings if you checked the **Create Klaviyo lists from MailChimp audiences** setting. If you only sync contacts from specific audiences, your Mailchimp ratings (even for those synced contacts) won't sync to Klaviyo.
- Syncs the following metrics for campaigns that have finished sending, and have sent in the last 90 days (excluding campaigns that were part of an A/B test):
  - Clicked Email
  - Opened Email
  - Received Email

It’s important to note that only names, email addresses, Mailchimp ratings, and locations of contacts will sync; to migrate over custom properties (tags) that may be attached to contact profiles in Mailchimp, see the section below.

## Import Mailchimp tags into Klaviyo

If you use Mailchimp tags to label and organize your contacts, you can manually export and import these tags into Klaviyo. Klaviyo's built-in Mailchimp integration does not sync any of your tags.

1. Start by navigating to ****Manage contacts > Tags**** in Mailchimp to view specific tags you want to sync.
2. Clicking the dropdown next to **View** will give you the option to "Export as CSV" to export your segment from Mailchimp. Use Mailchimp's guide for more information on exporting contacts with specific tags.
   ![In Mailchimp’s Tags settings, View menu is selected on right-hand side of page for VIP tag, and mouse is hovering near Export as CSV option](https://klaviyo.zendesk.com/hc/article_attachments/28723506886043)
3. Once you've exported your data from Mailchimp you can [import it into Klaviyo as custom properties](https://klaviyo.zendesk.com/hc/en-us/articles/1260806293150). Custom properties get attached to your Klaviyo profiles, and you can create segments based off of specific properties, or use them to add filters to your flow or dynamically display data inside of your emails.

## Migrate your email templates from Mailchimp to Klaviyo

Klaviyo has an intuitive drag-and-drop template builder that you can use to recreate your Mailchimp templates. We recommend using this method to build your templates because it will ensure that they are mobile-optimized, responsive, and easy to edit and iterate on going forward.

However, if you don’t have time to dedicate to recreating your Mailchimp templates using Klaviyo’s template builder, it is possible to export your email templates from Mailchimp and import them into Klaviyo.

This process involves editing and updating the raw HTML of the email template. If you would instead like to use Klaviyo’s drag-and-drop editor to recreate your templates, [check out our guide](https://klaviyo.zendesk.com/hc/en-us/articles/4407911841435) to learn the ropes of using Klaviyo’s template editor.

### Export your template from Mailchimp

1. In your Mailchimp account, navigate to the template that you would like to migrate to Klaviyo. In the dropdown beside the name of the template, select ****Export as HTML****.
   ![In Mailchimp’s Templates, Edit menu is selected on right-hand side of page for desired template, with mouse hovering over Export as HTML optio](https://klaviyo.zendesk.com/hc/article_attachments/28723518563611)
2. You will be prompted to confirm your export and an HTML file will save to your computer.

### Swap out template tags

Klaviyo and Mailchimp use different template tags to insert dynamic content in your emails. For example, the “first name” tag is different in Mailchimp than it is in Klaviyo, so it’s important that you swap out any Mailchimp-specific tags with the corresponding Klaviyo tags.

The tag that is most important to swap out is the unsubscribe tag.

1. Before you import your template into Klaviyo, you will have to add an {% unsubscribe %} tag because Klaviyo does not allow you to upload HTML templates that don't have unsubscribe tags unless they're for transactional emails.
2. To edit the tags in your template, open the HTML file in a text editor, like Sublime Text. Below is a table of other common Mailchimp tags and their corresponding Klaviyo tags.

|  |  |
| --- | --- |
| ****Mailchimp Tag**** | ****Klaviyo Tag**** |
| `*|UNSUB|*` | `{% unsubscribe %}` |
| `*|FNAME|*` | `{{ first_name }}` |
| `*|LNAME|*` | `{{ last_name }}` |
| `*|LIST:COMPANY|*` | `{{ organization.name }}` |
| `*|EMAIL|*` | `{{ email }}` |
| `*|UPDATE_PROFILE|*` | `{% manage_preferences %}` |
| `*|MC:SUBJECT|*` | This is the subject line of the email, which is set on a per-email basis in the Klaviyo template editor. |
| `*|MC_PREVIEW_TEXT|*` | This is the preview text of the email, which is set on a per-email basis in the Klaviyo template editor. |

See the **Additional resources** below to learn more about Klaviyo's template tags.

Once you've swapped out the tags for Klaviyo tags, you can save your HTML file.

### Import your template into Klaviyo

1. In your Klaviyo account, click the ****Content**** dropdown and select the ****Templates**** tab, then select ****Import Template****.
2. In the ****Import template**** modal, select the HTML file from your computer to upload the file you just saved.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/33047503255835)
3. You can see a preview of what your email template will look like in the ****Preview**** tab.
4. Please note that going forward, you will have to directly edit the HTML in order to change the template.

## Sunset your Mailchimp account

If you begin cleaning contacts in Mailchimp before removing the integration, these contacts will be suppressed in Klaviyo. Once your Mailchimp account is safely sunsetted, be sure to remove the integration before cleaning contacts in Mailchimp that you don't want suppressed in Klaviyo. Audiences and profiles synced from Mailchimp to Klaviyo won't be removed in Klaviyo if you disable or remove the Mailchimp integration.

After you've moved all your data over to Klaviyo, there are three key steps you can take to ensure that you no longer need your Mailchimp account:

1. Ensure that your sign-up forms and list growth tools point to Klaviyo, not Mailchimp
2. Recreate your automations as flows in Klaviyo
3. Remove the Mailchimp integration

### Sign-up forms and list growth tools

If you have any sign-up forms or sign-up form campaigns in your Mailchimp account, you will want to ensure that these are recreated in Klaviyo so that your list continues to grow in Klaviyo rather than Mailchimp. You won't be able to redirect forms created in Mailchimp to Klaviyo. Instead, you can:

1. Use the Klaviyo sign-up form builder to re-create your forms from scratch
2. Use a third-party list growth tool that integrates with Klaviyo
3. Integrate your custom form through your ecommerce platform

If you are using a third-party list growth tool instead of Mailchimp's built-in form builder, make sure that this syncs to Klaviyo. Klaviyo integrates with a number of third-party list growth tools. [Scan our list of integrations](https://help.klaviyo.com/hc/en-us/categories/115000874028-Other-Data-Integrations) to find the tool that you're using. If you don't see it listed, consider using Klaviyo's [sign-up form builder](https://help.klaviyo.com/hc/en-us/articles/360026474752-Getting-started-with-signup-forms) to create your forms, or switching to a different third-party tool.

Please note that all Klaviyo lists are double opt-in by default. To change a list to single opt-in, head to our [guide to the double opt-in process](https://klaviyo.zendesk.com/hc/en-us/articles/115005251108).

If you’re using a custom-coded form, you can ensure that these contacts sync to Klaviyo. To do this, make sure that your custom form syncs new subscribers directly to your ecommerce platform and that your ecommerce store is integrated with your Klaviyo account.

After switching all your sign-up forms to point to Klaviyo, wait a few days and watch your audiences in Mailchimp. If you notice subscribers are still being added to these audiences, there's probably at least one form that still needs to be swapped out.

Next, you'll want to turn off your Mailchimp sign-up forms. To do that, head to the code of the page where you installed the form and remove the code that begins with

`<!-- Begin Mailchimp Sign-up Form -->`

and ends with

`<!--End mc_embed_sign-up-->`

### Email automations

Klaviyo refers to email automations as flows and allows for much more advanced and targeted sequences. It is important to recreate these in Klaviyo so that you don't need to continue to use Mailchimp to send triggered emails. To learn more, check out our guide to [getting started with flows](https://help.klaviyo.com/hc/en-us/articles/115002774932).

Once your Klaviyo flows are live, turn off all of your automations in Mailchimp to ensure that you're not double-emailing people.

1. To do this, click ****Pause and Edit**** next to the specific campaign.
2. Then, click ****Pause**** in the pop-up.
   ![Email campaign in Mailchimp with Pause and Edit selected in dark gray](https://klaviyo.zendesk.com/hc/article_attachments/28723518566555)

### Remove the Mailchimp integration

Once you’ve pointed all of your list growth tools to your Klaviyo account, paused your Mailchimp automations, and turned your Klaviyo flows live, you can remove the Mailchimp integration. Before you remove your Mailchimp integration, make sure to double-check that everything is working as expected. Enter a test email into your sign-up form and other list growth tools, abandon a cart, and sign up for your newsletter to trigger a welcome series.

1. Click the ****Audience**** dropdown and select the ****Profiles**** tab in your Klaviyo account to make sure that the information in the profile reflects all of the correct communication.
2. If the list you sign up to is double opt-in, be sure to confirm your email first.
3. Once you've taken these steps and are fully migrated to Klaviyo, you can go ahead and remove your Mailchimp integration. Select the ****Integrations**** tab.
4. Click the action button to the right of the Mailchimp integration.
5. Select ****Remove integration**** to remove the integration.
   ![Integrations tab with Remove integration selected for the Mailchimp integration](https://klaviyo.zendesk.com/hc/article_attachments/28723506904347)

## Outcome

You've now migrated from Mailchimp to Klaviyo and learned about best practices for switching your email sending.

## Additional resources

### Klaviyo resources

- [How to migrate from another email service provider to Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115005082767)
- [Template tags and variable syntax reference](https://klaviyo.zendesk.com/hc/en-us/articles/4408802648731)

### Mailchimp resources

- [About contact ratings](https://mailchimp.com/help/about-contact-ratings/)
- [View or export your contacts](https://mailchimp.com/help/view-export-contacts/#View_or_Export_Tagged_Contacts)
