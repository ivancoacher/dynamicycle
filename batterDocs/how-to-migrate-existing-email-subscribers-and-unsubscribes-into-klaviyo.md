<h1>How to migrate existing email subscribers (and unsubscribes) into Klaviyo</h1>

## You will learn

Learn how to use Klaviyo's list import tools to add contacts from a former ESP into your Klaviyo account, as well as other best practices for getting started with Klaviyo.

## Before jumping in

To start, we recommend that you [maintain one main email list](https://klaviyo.zendesk.com/hc/en-us/articles/360043947571) in your account, sometimes called an email list. As you import contacts and connect signup forms to Klaviyo, maintaining one primary list will make it easy to manage and communicate with your contacts efficiently.

Our [segment builder](https://help.klaviyo.com/hc/en-us/articles/115005237908) allows you to create dynamic subsets of your lists that don’t require maintenance. For example, instead of having different signup forms link to multiple lists, have all of your forms point to one list. Then, pass a sign-up source property ([**$source**](https://help.klaviyo.com/hc/en-us/articles/115005074627-Guide-to-Properties#ask-customers-for-them5)) that is unique for each form. This way, you maintain one subscriber list and create [segments based on this property](https://klaviyo.zendesk.com/hc/en-us/articles/360040841811).

## Sync contacts from another email service provider (ESP)

If you are migrating from Mailchimp, Campaign Monitor, Constant Contact, or Salesforce Marketing Cloud (formerly ExactTarget), you'll use a built-in integration with Klaviyo to import existing subscriber lists, as well as unsubscribes. To do this, install the relevant integration:

1. Navigate to ****Integrations**** ****> E********xplore apps****.
2. Click ****All categories**** in the top right.
3. Select ****Email Service Provider**** on the left, then select your provider.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/39460582424347)
4. Click ****Install****, then follow the steps to install the integration.
5. Once your integration is installed, your lists will automatically sync and appear in your account's **Lists & segments** tab within a few minutes.

All unsubscribed contacts will also sync and go straight to the [suppression](https://klaviyo.zendesk.com/hc/en-us/articles/115005246108) list in your account.

- For MailChimp, Campaign Monitor, and Salesforce Marketing Cloud (formerly ExactTarget) we automatically create an exclusion list for those that are unsubscribed. In MailChimp, if someone is suppressed in any list, they will be globally suppressed in Klaviyo. In Salesforce Marketing Cloud, if a profile has an inactive status, that profile will be globally suppressed within Klaviyo. Inactive statuses include Bounced, Held, Unsubscribed, and Deleted.
- For Constant Contact, we only sync a suppression list if they belong to a Constant Contact List ID of **do-not-mail**.

If you are not currently using an ESP we integrate with, you will need to take a more manual approach (outlined in the [next section](#section2)).

## Import contacts from a CSV file

If you are migrating from an ESP that we do not currently integrate with or have a subscriber list already saved as a CSV or Excel file, you can easily import your subscribers into Klaviyo. If you have your list saved as an Excel file, make sure to save it as a CSV file first.

Your CSV should have the first row formatted as the headings for the columns you intend to upload. You must have a column labeled "Email" or "Email Address." Other columns you may want to include are "First Name" and "Last Name," along with any other [custom properties](https://help.klaviyo.com/hc/en-us/articles/115005074627-Add-Custom-Properties-to-a-Contact-Profile) you wish to upload.

When importing a list from another ESP, most platforms have a link to export lists to a CSV or Excel file. If you're having trouble, we recommend reaching out to your current platform for help.

Once you have your list exported:

1. Navigate to the ****Lists & Segments**** tab in Klaviyo.
2. Choose a list (e.g., **Newsletter** or **Email list**).
3. Click ****Manage List > Import Contacts****.
   ![Klaviyo's list import tool](https://klaviyo.zendesk.com/hc/article_attachments/28716301211547)
4. Click ****Upload**** and select your CSV file of subscribers.
5. Map each column from your CSV to an appropriate property in Klaviyo, then click ****Next****.
6. If everyone in your CSV file has explicitly consented to receive email marketing from you, select the option **Yes, update subscription status for all imported contacts to subscribed**. If your CSV file contains both emails and phone numbers, select which channel(s) they’ve subscribed to.
7. Click ****Import****.

## Use the Klaviyo API

The Profiles API is used to create and manage lists in Klaviyo. If you're tech-savvy or have a developer on your team, you can use [Klaviyo's bulk subscribe API endpoint](https://developers.klaviyo.com/en/reference/bulk_subscribe_profiles).

## Load historic unsubscribes into Klaviyo

If you did not sync subscribers through one of our built-in ESP integrations, manually import your historic list of bounces and unsubscribes into Klaviyo.

This step is important for several reasons:

- To ensure you follow spam laws
- To keep your [email deliverability](https://klaviyo.zendesk.com/hc/en-us/articles/115005247008) high by sending to clean lists from the start
- To keep your subscribers happy and make sure you don't email anyone who has opted out

To import your historic unsubscribes into Klaviyo:

1. Prepare a CSV file of bounces and unsubscribes, with a single column containing one email per row.
2. Navigate to ****Audience > Profiles**** in Klaviyo.
3. Click ****View suppressed profiles**** in the upper right.
4. Select****Upload File**** and upload your file of unsubscribes.
   ![Upload_suppression_list.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28716328580635)

## Additional resources

- [Understanding the benefits of having a main list for each marketing channel](https://klaviyo.zendesk.com/hc/en-us/articles/360043947571)
- [Acceptable date and timestamp formats for profile and event properties](https://klaviyo.zendesk.com/hc/en-us/articles/115005253428)
- [Getting started with segments](https://klaviyo.zendesk.com/hc/en-us/articles/115005237908)
- [How to create customer engagement tiers](https://klaviyo.zendesk.com/hc/en-us/articles/360000407272)
