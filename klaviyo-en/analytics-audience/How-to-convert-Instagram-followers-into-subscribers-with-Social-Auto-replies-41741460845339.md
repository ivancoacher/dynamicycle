---
id: "41741460845339"
title: "How to convert Instagram followers into subscribers with Social Auto-replies"
source_url: "https://help.klaviyo.com/hc/en-us/articles/41741460845339-How-to-convert-Instagram-followers-into-subscribers-with-Social-Auto-replies"
section: "Use growth tools"
category: "Audience"
category_slug: "analytics-audience"
klaviyo_updated: "2026-05-20T17:20:22Z"
language: "en"
---
Discover how to turn social interactions into subscriber growth with Social Auto-replies. You can now set up Instagram campaigns that grow, email, text and WhatsApp lists directly from Instagram messages.

Popular campaigns with this strategy include [Instagram giveaways, early access offers, and evergreen campaigns](https://www.klaviyo.com/wp-content/uploads/2025/04/Klaviyo-04_2025-GatsbyListGrowthGuide-PDF.pdf).

- You'll need Admin access to your Instagram Business Account to set up this feature.
- For now, you can only connect one Instagram account to your Klaviyo account. If you’re on the paid version of Social Marketing, you can connect your same Instagram account to multiple regional Klaviyo accounts that you manage.

Watch the setup video, or scroll down for step-by-step instructions.

[Embed](https://www.youtube.com/embed/1sl_yPQ5hD4)

## Step 1: Connect Instagram

Connect your Instagram with Klaviyo in order to set up Social Auto-replies that grow your subscriber list. For a detailed step-by-step on connecting Instagram, see the guide “[Connect Instagram to Klaviyo](https://help.klaviyo.com/hc/en-us/articles/50223235019675)”

## Step 2: Create your Auto-reply trigger keyword

Set an Instagram keyword and series of Auto-replies that prompt your followers to join your email, text or WhatsApp list right from their Instagram direct messages (DMs).

1. Navigate back to ****Social**** in the left nav.
2. Select ****Auto-replies****.
3. By default, your first auto-reply uses the keyword ****“access,”**** which is ideal for publishing in your Instagram bio and general marketing.

   ****Keyword requirements and trigger behavior****

   - Keywords are ****not case sensitive****. Users could send Access, access, or ACCESS; all variations would work.
   - Klaviyo uses fuzzy matching, so small typos, emojis, or extra characters can still trigger an auto-reply. Matching is case-insensitive.
   - Keywords must be unique across Social Auto-replies and SMS.
   - You can listen for keywords in DMs, comments, or both. Comments always trigger a DM reply, not a comment reply.
   - ****Best practice:**** If you listen in comments, also enable DMs. Comment auto-replies can time out, and DMs let customers restart by re-sending the keyword.
4. Pick whether you want this auto-reply to request the customer’s email address or phone number for SMS and/or WhatsApp.

![KlaviyoAutoRepliesAccessKeyword.png](https://klaviyo.zendesk.com/hc/article_attachments/41874372800539)

****Note for collab / influencer posts:****

Your brand's Instagram account must create the post and invite the collaborator. If the collaborator creates the post instead, Klaviyo cannot auto-reply to comments on that post or to DMs the collaborator receives.

## Step 3: Collecting subscriber information

After setting the trigger, scroll down to review the message content.

1. Start by editing or leaving-as-is the default text and default Subscribe List for “****Collect email address”****
2. For ****Collect phone number****, select a ****channel****:
   1. ****Text message**** – opts the subscriber in to SMS only.
   2. ****WhatsApp**** – opts the subscriber in to WhatsApp only.
   3. ****Text message and WhatsApp**** – opts the subscriber in to both channels with a single phone number submission.
      1. Select the ****Subscribe List**** for phone number submissions. The list you pick controls the subscription rules that apply (single vs. double opt-in).
3. If you see placeholders like [Company Name] and [Privacy Policy], update the text.
4. On formatting:

   - Email: Klaviyo verifies the format (e.g., name@domain.com).
   - Phone:
     - Klaviyo checks that the phone number format matches the country you selected while setting up this auto-reply; phone numbers from other countries need a country code to receive auto-replies.
     - Users can input phone numbers with dashes, periods, no spaces - it's pretty flexible but Klaviyo doesn't understand the message it will prompt the user to try again.
5. Customize the confirmation message.

- The confirmation message is the last message they receive from this DM sequence, and it typically drives them to look at their emails, check their text messages, or visit a page on your website. This is a great place to include a link back to your website.

After submission, Klaviyo starts the opt-in process for that channel.

Want to collect more profile data? On the paid Klaviyo Social Marketing plan, you can add up to 5 Custom Questions. See [**Add Custom Questions to your auto-reply**](https://help.klaviyo.com/hc/en-us/articles/50223235904411).

## Step 4: Understand the opt-in flow

Klaviyo’s existing list subscription rules apply to all new subscribers:

- ****Text messages -**** If the list you chose uses double opt-in (DOI), the user must reply ****YES**** over text message to confirm subscription.

  ****SMS requirement:****

  You must have a [2-way SMS sending number](https://help.klaviyo.com/hc/en-us/articles/6637671573403) configured to support reply-based actions, including tap-to-text and double opt-in confirmation replies (e.g., replying “YES”).
- ****Email -**** If the list you chose uses double opt-in (DOI), the user must confirm via the link sent to their inbox.

## Step 5: View the subscriber profile in Klaviyo

Once submitted, the subscriber's profile will automatically be ****created or updated**** in Klaviyo:

![Screenshot 2025-10-07 at 2.34.07 PM.png](https://klaviyo.zendesk.com/hc/article_attachments/41874372802459)

The profile will contain the following:

- ****Subscription Method:**** SOCIAL\_INSTAGRAM\_MESSAGE
- ****New events, including:****
  - Started Automation
  - Submitted Email via Automation
  - Submitted Phone via Automation
  - Ended Automation
- ****New custom profile properties, including:****
  - Instagram Username
  - Follower count
  - Whether they follow your account
  - The keyword(s) they used to trigger the auto-reply

| Property name | Type | Description |
| --- | --- | --- |
| InstagramFollowerCount | int | The number of followers this user has on Instagram. |
| InstagramUsername | string | The user's Instagram username. |
| InstagramProfile Image | string | URL to the user's Instagram profile picture. |
| InstagramFollowsYou | bool | Indicates whether or not the user follows your brand on Instagram. |
| InstagramKeyword | Array[string] | List of all the auto-reply keywords that the user has sent to you through DMs. |

![Screenshot 2025-10-07 at 2.40.21 PM.png](https://klaviyo.zendesk.com/hc/article_attachments/41874372804379)

These new social properties will update automatically every time the consumer DMs your brand on Instagram. These new social data points allow you to build targeted segments and leverage Instagram data as part of your broader marketing strategy.

Once a customer has gone through an Auto-reply, you can also use Engagement events (Posted UGC, Social Comment, Social DM) to track their ongoing Instagram activity. Engagement events are included in the paid version of Social Marketing.

## Testing Auto-replies

Auto-reply behavior depends on your Instagram message control settings.

- ****Your settings gate the triggers.**** If your Message settings are set to "Followers only" or "No one" then this will limit your ability to send Auto-replies.
- ****Consumer settings can block delivery.**** Both public and private accounts can receive your DMs, but if the consumer's message settings are set to "No one," Klaviyo can't deliver the auto-reply.

To test:

- Send your account a DM with your keyword and follow the DM prompts
- Search for your new or updated subscriber profile in Klaviyo and confirm the new Instagram properties are there
- Monitor subscriber growth from Instagram in your **Subscriber Growth Report** and **Lists & Segments** dashboard.
  - You can easily create a segment of subscribers who engaged with your campaign. Select the option to "Create Segment" from the menu to the left of each Auto-reply.
    ![Screenshot 2025-12-22 at 10.20.44 AM.png](https://klaviyo.zendesk.com/hc/article_attachments/44693906469531)
- ****Review completion rate****, defined as the number of profiles who trigger the keyword and then provide at least one piece of contact information (email address or phone number). It may take up to 15 minutes for the completion rate to update after a submission.

## Troubleshooting

#### Auto-replies aren't firing

If your Instagram is connected in Klaviyo but auto-replies are not triggering on test DMs or comments, it usually means one of the required permissions has been toggled off. Check the following places:

****1. Facebook Page > Advanced Messaging****

These permissions are on by default but can be disabled at the Facebook Page level.

1. Open your Facebook Page.
2. Go to ****Settings**** > ****Page Setup**** > ****Advanced Messaging****.
3. Under ****Connected Apps****, find ****Klaviyo-IG**** and click ****Edit****.
4. In the ****Klaviyo-IG Settings**** modal, confirm that both ****Access standby channel**** and ****Take control of conversations**** are both turned on.
5. Click ****Save****.
   ![](https://cdn.sanity.io/images/6ct6b26e/help-center-prod/b3809ae9178fff1bc72ff3db9ffc54e12992057e-2978x1622.png)

   ****2. Instagram Business Account > Apps and Websites****

   The permissions you accepted when first connecting Klaviyo can also be edited from inside Instagram.
6. In the Instagram app or on instagram.com, open ****Settings****.
7. Go to ****Website Permissions**** > ****Apps and Websites****.
8. Find ****Klaviyo-IG**** in the list and tap ****View and edit****.
9. Confirm all permissions are turned on (basic business info, business message info, content, insights, comment info).

![](https://cdn.sanity.io/images/6ct6b26e/help-center-prod/c07e8b811ea0db74e76b9f568d5416951cb99301-2974x1616.png)

****3. Reconnect from Klaviyo****

If the permissions look correct in both places and auto-replies still are not firing, disconnect and reconnect Instagram from your Klaviyo settings.

When the auth modal appears, leave all permissions toggled on before clicking ****Allow****.

If the issue persists after these checks, contact [Klaviyo Support](https://www.klaviyo.com/support).