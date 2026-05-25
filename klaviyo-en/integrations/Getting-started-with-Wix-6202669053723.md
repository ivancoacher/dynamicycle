---
id: "6202669053723"
title: "Getting started with Wix"
source_url: "https://help.klaviyo.com/hc/en-us/articles/6202669053723-Getting-started-with-Wix"
section: "Wix"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:55:04Z"
language: "en"
---
## You will learn

Learn how to easily integrate Klaviyo with your Wix site in order to sync customer profile, order, and catalog information to Klaviyo. With this data, you’ll be able to reach customers with targeted messaging through segmentation, automated flows, and campaigns.

Integrating with Wix will:

- Create a historic sync of all data (customer, order, catalog) to your Klaviyo account.
- Create a real-time sync of data to your Klaviyo account going forward.
- Enable the use of Klaviyo sign-up forms and **Active on Site** visitor tracking through the automatic addition of Klaviyo’s onsite JavaScript to your site. With Klaviyo sign-up forms, you can collect both email and SMS subscribers. Please note that Klaviyo embedded forms do not work for Wix.
- Enable the addition of Wix email subscribers (collected through a Wix footer form or at checkout) to a Klaviyo list (also known as an audience).

## Before you begin

In order to use Klaviyo’s integration with Wix, your Wix site must:

- Have a premium plan
- Have a connected domain
- Be published

When you integrate Wix with Klaviyo, you should only connect one Wix store per Klaviyo account. If you try to add a second Wix store, it will replace the first, but there will still be data from the first store in your account. If you have multiple Wix stores, you should connect them to separate Klaviyo accounts.

## Integration video

Check out our step-by-step video on integrating with Wix.

![](https://fast.wistia.com/embed/medias/hqgxzcxeu9/swatch)

## How to integrate with Wix

1. If you need to create a new list in Klaviyo, navigate to the ****Lists & Segments**** tab in the ****Audience**** dropdown.
2. Click ****Create List/Segment****.
3. Name the list and assign any tags.
4. Click ****Create List****.

1. In your Klaviyo account, click ****Integrations**** in the left-hand navigation.
2. Select ****Explore apps****, search for **Wix**, and click the card. Then, click ****Install****.
3. Click ****Connect to Wix****.
   ![Page in Klaviyo Let's get Wix integrated with Klaviyo with Connect to Wix with black background](https://klaviyo.zendesk.com/hc/article_attachments/28717988326811)
4. You’ll be brought to your Wix account and prompted to login (if you are not currently logged in).
5. Once you’ve logged in, review the permissions and click ****Add to Site**** to be brought back into Klaviyo.
   ![Wix Klaviyo integration permissions page with permissions listed, with Add to Site with blue background, and Cancel with white background](https://klaviyo.zendesk.com/hc/article_attachments/28717994095131)
6. Review your store URL setting to make sure that you’ve chosen the correct Wix account to integrate with Klaviyo.
   ![Wix integration settings page in Klaviyo reading You're almost done with store URL, onsite JavaScript, and email subscriber settings](https://klaviyo.zendesk.com/hc/article_attachments/28717988320539)
7. The setting **Automatically add Klaviyo onsite JavaScript** is checked by default; leave it checked if you would like to enable Klaviyo’s **Active on Site** tracking and signup forms.
8. Check the setting **Add Wix email subscribers to a Klaviyo list** if you would like to do so; customers who opt-in to email via Wix, such as during checkout or with a Wix footer form, will be automatically added to the Klaviyo list you select.
9. Select a Klaviyo list from the dropdown, such as your Newsletter list, that you wish to add subscribers to.
10. Click ****Complete Setup.****
11. After a loading screen, you should see a success message reading **Your Wix account is now connected to Klaviyo!**

    You’ve finished integrating and your Wix data will now start syncing to Klaviyo.

    If you ever need to edit your Wix settings:
12. In your Klaviyo account, select the ****Integrations**** tab.
13. Select ****Wix**** on the list of **Enabled Integrations**.
14. You’ll be brought to the integration settings page, where you can make changes.
15. Click ****Save Settings****.

## Data synced from Wix to Klaviyo

To check on the data sync from Wix to Klaviyo:

1. In your Klaviyo account, select the ****Integrations**** tab.
2. Select ****Wix**** on the list.
3. Select the ****Data**** tab at the top.

Here, you’ll see recent data synced from Wix to Klaviyo, and a sync progress bar for your historical data sync.

If you are experiencing issues with your sync, select ****Restart Import**** here to restart the historical data sync.

The data synced from Wix to Klaviyo includes:

- [Known site visitors](https://help.klaviyo.com/hc/en-us/articles/115005076767-Guide-to-Klaviyo-Onsite-Tracking#who-klaviyo-tracks5) tracked as **Active on Site** events (if you left the onsite JavaScript setting checked)
- Email subscribers (if you chose to add them to a Klaviyo list)
- Profile information associated with order events
- Your Wix catalog
- The following order events:
  - Abandoned Checkout (note that there is no historical sync of **Abandoned Checkout** events, only a sync going forward from the time you integrate)
  - Placed Order
  - Modified Placed Order
  - Ordered Product
  - Refunded Order
  - Canceled Order
  - Fulfilled Order
  - Fulfilled Partial Order

For more information on the properties associated with each event synced from Wix, check out our article [Wix data reference](https://help.klaviyo.com/hc/en-us/articles/6202715127579).

## Create automated messaging with Wix

There are a number of pre-built flows for Wix in Klaviyo’s flow library, which you can use to personalize customer messaging.

These flows can be accessed by:

1. Selecting the ****Flows**** tab in Klaviyo.
2. Clicking ****Browse Ideas**** in the upper right.
3. Selecting ****Wix**** from the filter dropdown next to the search bar.

These pre-built flows include abandoned cart reminder, customer winback, cross sell, and repeat purchase nurture flows.

## Troubleshooting

### Why aren't my Wix subscribers being added to my Klaviyo list?

If you're using a Wix sign-up form to collect subscribers on your website, but the subscribers that submit your form are not being added to your Klaviyo list, this is most likely due to the fact that these contacts are not being tagged as 'subscribed' in Wix.

There are many different kinds of Wix sign-up forms, but not all of them add a 'subscribed' tag to the contact in Wix. This 'subscribed' tag is required for Klaviyo to properly add the profile to the list you specified on the integration settings page.

If your form adds a 'subscribed' tag when a contact submits the form, the tag will appear on the contact like this:

![A contact in Wix with email address and subscribed tag](https://klaviyo.zendesk.com/hc/article_attachments/28717988324635)

If this tag is missing, you need to update your Wix form to ensure that it adds the 'subscribed' tag. You can either [create a subscribe form](https://support.wix.com/en/article/wix-forms-adding-and-setting-up-a-subscribe-form#adding-a-subscribe-form-to-your-site) or [add a subscriber field to a standalone form](https://support.wix.com/en/article/wix-forms-adding-and-setting-up-a-subscribe-form#add-a-subscriber-field-to-a-standalone-form) to make sure the tag is added.

Now, your subscribers should sync properly from Wix to your Klaviyo list.

## Outcome

You’ve integrated Wix with Klaviyo and verified your synced data. Now, you can create automated flow messages, personalize campaigns, segment your lists, and more based on data synced from Wix.