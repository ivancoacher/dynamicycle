---
id: "360017518492"
title: "How to create a sunset flow"
source_url: "https://help.klaviyo.com/hc/en-us/articles/360017518492-How-to-create-a-sunset-flow"
section: "Lifecycle flows"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-05-14T16:05:13Z"
language: "en"
---
## You will learn

Learn how to set up a sunset flow that is designed to phase out customers who are no longer engaging with your brand. You can use this flow as a last-ditch effort to win back their business, and then delete or suppress anyone who is not responsive. You will also see how this recommended ****sunset segment**** definition connects to the prebuilt ****Sunset (Email)**** segment in the Segment Library. This will help you maintain a clean list and avoid having inactive customers contribute towards your Klaviyo billing plan.

## When to sunset subscribers

Since sunset flows act as a final effort to engage profiles, you should sunset lists and segments that you plan to suppress. Once you suppress a profile, they will be unable to receive marketing emails and promotions from your brand. By sunsetting these profiles, you have an opportunity to exclude profiles that engage with the flow from suppression, as they still are valuable to keep as active and send to.

You should also sunset profiles as they become inactive, or churn as customers. It no longer makes sense to keep them as active in your account and have them contribute towards your Klaviyo billing plan. These are profiles that have demonstrated a long, sustained period of inactivity (i.e., no website visits, purchases, or marketing engagement). Due to this sustained period of inactivity, it is highly unlikely that these profiles will engage with your brand again.

Once a profile is no longer generating any revenue for your business in Klaviyo and you do not see any opportunity to win them back, you can take action to suppress them so they do not count towards your Klaviyo billing plan.

## Set up a sunset segment

A sunset flow is triggered when a profile is added to a particular segment. While the recommended segment below enables you to identify and sunset profiles that have demonstrated a long period of inactivity, you can run any segment or list you plan to suppress through a sunset flow.

To identify profiles that have demonstrated sustained periods of inactivity, you can build the following segment and run it through a sunset flow:

- If someone can or cannot receive marketing > Person ****can receive**** ****email marketing****
  AND
- Properties about someone > ****Created**** is at least ****180**** days ago
  AND
- What someone has done (or not done) > has ****Received Email at least 5**** in the last ****72**** weeks
  AND
- What someone has done (or not done) > has ****Opened Email 0 times**** ****over all time****
  AND
- What someone has done (or not done) > has ****Clicked Email 0 times over all time****
  AND
- What someone has done (or not done) > has ****Active on Site 0 times**** ****over all time****
  AND
- What someone has done (or not done) > has ****Viewed Product 0 times over all time****
  AND
- What someone has done (or not done) > has ****Checkout Started 0 times over all time****
  AND
- What someone has done (or not done) > has ****Placed Order 0 times over all time****

This definition also appears as the prebuilt Sunset (Email) segment in the Segment Library, and it is the same logic Klaviyo uses for [suppression recommendations](https://help.klaviyo.com/hc/en-us/articles/24312135764251) on the Suppressed profiles page.

First navigate to the Segment Library, and you'll see the "Sunset (Email)" option.

![](https://klaviyo.zendesk.com/hc/article_attachments/47698582815515)

When you select it, you will see the following definition of the Sunset (Email) Segment and be able to name it and add tags.

![](https://klaviyo.zendesk.com/hc/article_attachments/47698545407771)

## Deliverability benefit

One of the major benefits of building this segment is to suppress it and stop delivering to profiles that are unmonitored because sending to unmonitored inboxes will hurt your deliverability over time. Klaviyo uses this same sunset definition when [recommending low engagement profiles](https://help.klaviyo.com/hc/en-us/articles/24312135764251) to suppress from the ****Suppressed profiles**** page. Continuing to send to profiles in this cohort will lower your open rate, which is the most important signal used by mailbox providers to determine where future emails go (the inbox or the spam folder)

As inactive profiles enter this segment, they will trigger the sunset flow and automatically receive some final emails from your brand before they can ultimately be suppressed.

If you attempt to send emails to these inactive profiles then it has the opposite effect. Rather than improving your sending reputation, doing this will put your reputation at risk. Please do so with extreme caution.

## Set up a sunset flow

After setting up your sunset segment, you will need to build a flow that is triggered by being added to your sunset segment. We recommend using a pre-built sunset flow from the flows library.

1. Navigate to the ****Flows**** tab.
2. Click ****Create Flow**** to view the flows library.
3. In the searchbar, search for "sunset" to see Klaviyo's pre-built sunset flow.
4. Click on the pre-built "sunset unengaged subscribers" flow.
5. In the trigger dropdown, select your sunset segment.
6. Click ****Create Flow**** at the bottom on the modal.
7. Customize the message content to match your brand.
8. Add past profiles to your flow if you created it for an existing list or segment.

****Create a sunset flow from scratch****

If you'd prefer to create a flow from scratch:

1. Navigate to the ****Flows**** tab.
2. Click ****Create Flow****.
3. Click ****Create From Scratch**** in the top right.
4. Name your flow and click ****Create Flow****.
5. In the **Trigger Setup**sidebar, click ****Segment****.
6. In the dropdown, select your sunset segment.
7. Add flow filters to exclude anyone who opens or clicks an email since starting the flow. Anyone who engages your sunset email (or any other email you send them while they're in the flow) will automatically be removed from the flow and will not be tagged for suppression. See the screenshot below for reference.
   ![Sunset flow with trigger filters to check that a profile has not opened an email and has not clicked an email since starting the flow](https://klaviyo.zendesk.com/hc/article_attachments/28704485061403)
8. Add one to three emails that prompt customers to unsubscribe if they are no longer interested in receiving emails from you. It is best to limit this flow to be no more than three emails because you don’t want to repeatedly contact people who are unengaged, since this can hurt your deliverability. Anyone who unsubscribes will be suppressed automatically, with no further action needed on your (or their) part.
9. After the last email, drag in a short time delay to give recipients a grace period to open or click the email. Here, the grace period is three days, assuming a daily sending frequency. If you send less regularly, push the grace period to be a longer time period, such as 7–10 days.
   ![Example of a time delay set for 1 day after the flow trigger](https://klaviyo.zendesk.com/hc/article_attachments/28704485062811)
10. Drag in an update profile property flow action. This will tag those who do not engage with the email and thus are passively indicating that they would like to unsubscribe.
11. Configure the tag to specify that these contacts should be suppressed. You can do this by creating a new boolean profile property where the value "Unengaged" is "True."
    ![Example of an update profile property action at the end of the flow which sets Unengaged property to True](https://klaviyo.zendesk.com/hc/article_attachments/28704476922651)

Thanks to the flow filters, anyone who opens or clicks an email will exit the flow before this action, and the tag will not be added to their profile.

Once unengaged subscribers are tagged as **Unengaged = True**, they will exit the flow.

### Suppress unengaged profiles

Anyone who has gone through the entire sunset flow will be tagged as unengaged and can now be suppressed. To suppress these profiles:

1. Navigate to the ****Lists & Segments**** tab of your account.
2. Select ****Create New**** > ****Create Segment****.
3. Name your segment something that makes it clear it's meant for suppression.
4. Add the following segment definition:
   1. ****Properties about someone**** > ****Unengaged****> ****is true****.
      ![](https://klaviyo.zendesk.com/hc/article_attachments/33901479807131)
5. Click ****Create segment****.
6. Back on the ****Lists & Segments**** tab, click the action button to the right of your new segment.
7. Choose ****Suppress current members****. ![Bulk suppress option for list in Klaviyo](https://klaviyo.zendesk.com/hc/article_attachments/33901479809563)This action applies to all the profiles within the list or segment at the time of suppression, and does not impact profiles that join after. If a profile in the group is already suppressed, their status will not be impacted.

Please note that you will have to do this each time before sending a campaign to effectively phase inactive profiles out of future sends. It is not currently possible to suppress profiles as a Flow Action.

There is a workaround for this but you would need to utilize Klaviyo's API to do this. This will require a developer. If you are a developer, please see the process documented in the article, "[Solution Recipe 9: Use Klaviyo Flow Webhooks to Automate Suppressions Using Segments and Klaviyo’s APIs .](https://www.klaviyo.com/blog/solution-recipe-9-use-klaviyo-flow-webhooks-to-automate-suppressions-using-segments-and-klaviyos-apis)

When you suppress other lists or segments that may include recently active customers, Klaviyo may show a suppression modal summarizing how many profiles will be suppressed versus kept active based on recent verified email engagement or purchases.

For the strict “sunset” segment defined above (no opens, clicks, site activity, or orders), you generally won’t see this modal, because those profiles are already classified as long‑term inactive and ready to be suppressed. Learn more about [how to manage email suppressions and delete profiles in bulk.](https://klaviyo.zendesk.com/hc/en-us/articles/24312135764251)

### Flow content best practices

We recommend using plain text and being as personal as you can in the email by using the `{{ first_name }}` tag and a from address like "Marissa from Klaviyo." Include content about any new products that have been released since they've become unengaged and consider offering a discount to entice them to buy.

You will want to include prominent unsubscribe and manage preferences links, in case subscribers want to update their settings rather than unsubscribe completely.

![Message content editor with a message containing language appropriate for a sunset email](https://klaviyo.zendesk.com/hc/article_attachments/28704476913691)

In the email(s), give recipients the option to browse your site or otherwise interact with you if they do want to remain subscribed. Below is an example from [Princess Awesome](https://princess-awesome.com/).

![Example sunset email with links for customers to set their email preferences](https://klaviyo.zendesk.com/hc/article_attachments/28704485056795)

In addition, indicate in the email subject line that you will say goodbye to these subscribers if they continue to not engage (e.g., “Is it time to say goodbye?” or “We miss you already”). For instance, the email below from Framebridge has the subject line: “Goodbyes are hard…”

![Example sunset email with a link that a customer can click to keep them on the subscribe list](https://klaviyo.zendesk.com/hc/article_attachments/28704485058715)

## Add past profiles

When you create a sunset segment, it will be filled with profiles that previously fit the criteria in the segment definition. However, the flow will only trigger for profiles that organically enter the segment, i.e., those that fulfill the segment's criteria after it was created.

If you'd like to add past profiles to your flow:

1. Make sure the flow's messages are set to either manual or live status before adding past profiles.
2. Click on the ****Add past profiles**** icon on the trigger card
   ![](https://klaviyo.zendesk.com/hc/article_attachments/46896183205659)

Learn more about the effects of [adding past profiles to a flow](https://klaviyo.zendesk.com/hc/en-us/articles/360049924272).

## Additional resources

Read about similar flows in the Klaviyo Help Center:

- [How to create a winback flow](https://help.klaviyo.com/hc/en-us/articles/115002775192-Create-a-Winback-Flow)
- [How to create a segment-triggered flow](https://help.klaviyo.com/hc/en-us/articles/360003040052-Create-a-Segment-Triggered-Flow)
- [How to update profile property action](https://help.klaviyo.com/hc/en-us/articles/360001768432-Update-Profile-Property-Action)