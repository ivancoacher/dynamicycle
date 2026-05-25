---
id: "115000769631"
title: "How to create email frequency segments"
source_url: "https://help.klaviyo.com/hc/en-us/articles/115000769631-How-to-create-email-frequency-segments"
section: "Segment examples and types"
category: "Audience"
category_slug: "analytics-audience"
klaviyo_updated: "2026-04-21T13:56:36Z"
language: "en"
---
## You will learn

Learn how to provide different email frequency preferences to your subscribers so you can pre-emptively set expectations and provide more relevant content. Allowing your subscribers to choose how often they hear from you is a great way to maintain engagement and reduce unsubscribes. If you come on too strong and email your subscribers very frequently, you risk having new signups unsubscribe right off the bat.

## Let your subscribers set email frequency preferences

The first step in segmenting your email list based on frequency preferences is to allow your subscribers to choose how often they hear from you. Learn how to add a frequency preference field to your Manage Preferences page:

1. Click on your account name in the bottom left corner.
2. Select ****Settings****.
3. Choose ****Other****.
4. Under **Preference Page**, click ****Edit Page****.
   ![Consent pages](https://klaviyo.zendesk.com/hc/article_attachments/28711672627611)

   If you've previously created list-specific consent pages, navigate to your main list's preference page editor.
5. Click ****Add blocks****.
   ![Add blocks to preference page](https://klaviyo.zendesk.com/hc/article_attachments/28711660470811)
6. Add a **Radio button** block to your preference page.
7. In the **Label Text** field, input "How often would you like to receive emails from us?" (or similar).
   ![A preference page's radio button settings show a Label Text field](https://klaviyo.zendesk.com/hc/article_attachments/28711660455835)
8. In the **Profile Property** field, type in "Email frequency," then click ****Create ["Email frequency"]****.

   If you'd prefer to use a different property name, choose it from the menu or type it into the search field to create it.

   ![A preference page's radio button settings show a Profile Property field](https://klaviyo.zendesk.com/hc/article_attachments/28711660459419)
9. In the **Label** column, add a series of email frequency options (e.g., Daily, Weekly, Monthly). These labels will appear on your preference page.
10. In the **Value** column, add corresponding property values. These values will appear in customer profiles in Klaviyo.
    ![A preference page's radio button settings show several value fields](https://klaviyo.zendesk.com/hc/article_attachments/28711672625947)
11. Click ****Publish**** to publish your preference page.

When someone signs up or chooses to edit their preferences, a [custom property](https://help.klaviyo.com/hc/en-us/articles/115005074627-Add-Custom-Properties-to-a-Contact-Profile) will be added to or changed on their contact profile.

## Ask subscribers for their preferences

Once your preference page includes a question about email frequency preferences, send a campaign to ask subscribers to complete it.

To include a link to your preference page in an email, use the template tag `{%
manage_preferences %}`. Alternatively, to customize the text that appears in your manage preferences link, use the tag `{% manage_preferences 'click
here' %}` and replace the text "click here" with your preferred text.

In addition to sending a campaign specifically to request subscriber preferences, consider including a manage preferences link in your email footers.

## Build email frequency segments

Once you collect this information from your subscribers, build segments to [include or exclude](https://help.klaviyo.com/hc/en-us/articles/115005227808-Send-a-Campaign-to-Multiple-Lists) in your campaign sends. If you make frequency preferences optional, you will need to have a default sending cadence in case a subscriber does not choose any of the options provided. It is usually best to make this a middle ground rather than sending to your subscribers daily emails right off the bat.

### Daily

![Daily preference segment](https://klaviyo.zendesk.com/hc/article_attachments/28711660472475)

### Weekly

![Weekly preference segment](https://klaviyo.zendesk.com/hc/article_attachments/28711660478747)

### Monthly

![Monthly preference segment](https://klaviyo.zendesk.com/hc/article_attachments/28711660487963)

## Subscribers whose email frequency preference is not set

If you make email frequency preferences optional, you will have some people in your email list whose frequency is not set****.**** It is important that you do not forget to message these subscribers. To get a count of how many people this is, build a segment using the following conditions:

![No frequency set segment](https://klaviyo.zendesk.com/hc/article_attachments/28711672652059)

Send these subscribers an email campaign and exclude your daily, weekly, and monthly segments.

![A campaign for those without a frequency preference](https://klaviyo.zendesk.com/hc/article_attachments/28711660453531)

Then, you can build campaigns for your daily, weekly, and monthly segments and send to them as you normally would.

The content that you send to each of these segments should vary. For example, weekly newsletters can be a digest of any new product releases, etc. that have happened over the course of the week, while daily updates can highlight any sales or promotions you're running. Monthly newsletters should be longer and carefully curated since you don't communicate with these subscribers very often.

## Additional resources

- Course: [Develop a content calendar](https://academy.klaviyo.com/developing-a-content-calendar)
- [How to create a sending schedule based on email engagement](https://help.klaviyo.com/hc/en-us/articles/360037527052-Create-a-Sending-Schedule-Based-on-Email-Engagement)
- [How to create customer engagement tiers](https://klaviyo.zendesk.com/hc/en-us/articles/360000407272)