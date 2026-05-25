---
id: "11118357030555"
title: "How to change your attribution model"
source_url: "https://help.klaviyo.com/hc/en-us/articles/11118357030555-How-to-change-your-attribution-model"
section: "Attribution"
category: "Analytics"
category_slug: "analytics-audience"
klaviyo_updated: "2026-04-21T13:54:10Z"
language: "en"
---
## You will learn

Learn how to adjust your attribution lookback window settings, remove bot clicks and Apple Privacy opens from attribution, and preview attribution model changes.

## Default message attribution settings

By default, Klaviyo uses a last touch attribution model with the following lookback window for all new accounts

- 5 days for email clicks
- 5 days for email opens
- 5 days for text message clicks
- 1 day for text message opens
- 12 hours for text message deliveries
- 24 hours for push opens
- 5 days for Whatsapp clicks
- 12 hours for Whatsapp opens
- 1 day for Active on Site (Advanced KDP and Marketing Analytics customers only)

However, you may find that you want to adjust these settings to better align with your customer behaviors or marketing strategies. The guide below provides a step-by-step walkthrough on adjusting your attribution settings for each channel.

## Updating your attribution model

1. Click on the account menu in the lower left of your account.
2. Choose ****Settings**** from the menu.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/41070100712859)
3. Navigate to ****Attribution****.
4. In the **Attribution windows** section, select the checkboxes next to the interactions you want to track. You can see the available touchpoints for a channel by expanding it.
   ![Attribution windows for different channels](https://klaviyo.zendesk.com/hc/article_attachments/31608853239579)

   If you do not select a channel checkbox, Klaviyo will exclude this particular interaction from counting towards attribution.
5. Optional: if you do not need to make changes to the **Time frame** selections, select ****Save****.
6. Optional: if you want to adjust the **Time frame** values, use the picker to add or subtract.

   For any channels that have more than one option (i.e., SMS or email), it is advised to choose options that do not potentially skew your attribution data and marketing strategies. For example, selecting a longer email open window instead of clicks may introduce a bias towards opens, which may not be conclusive indicators of conversions.
7. Optional: if you want to further adjust the **Time frame** measurement, open the **Days** dropdown and adjust to **Hours** where needed. Note that the max option for days is 90 and 720 for hours.
8. Optional: select the ****Compare model**** button to preview your changes and how they may adjust your attributed performance tracking. Learn more in the [section below about using the](#h_01J6WHBMRHXEAXD7A4B8439P74) [**Model comparison**](#h_01J6WHBMRHXEAXD7A4B8439P74) [tool](#h_01J6WHBMRHXEAXD7A4B8439P74).
9. Once you are done with your changes, select ****Save****.

It can take up to 36 hours for your settings to be applied.

## Other attribution model settings

Klaviyo’s attribution model also supports the ability to exclude certain types of message interactions from attribution which includes:

- Interactions with transactional messages
- Email bot clicks: Removes[email bot clicks](https://help.klaviyo.com/hc/en-us/articles/22981852783899) from your reporting and attribution. These include clicks made by third-party security software, certain inbox providers, etc.
- Text message bot clicks: Removes [text message bot clicks](https://help.klaviyo.com/hc/en-us/articles/22981852783899)from your reporting and attribution. These include clicks made by third-party security software, certain mobile carriers, etc
- Apple Mail Privacy Protection (MPP) opens: Removes[Apple Privacy Protection (MPP) opens](https://help.klaviyo.com/hc/en-us/articles/4416791883163#h_01HSXXZR43X6RVYX9A3BBK4YDT) from your attribution. Note that this does not include removal from reporting.

By default for all new accounts email and text message bot clicks are excluded from attribution and reporting.

Once updated and saved, Klaviyo will update your attribution data historically to reflect these changes.

## Using the **Model comparison** tool

The **Model comparison** tool provides options for previewing potential changes to your attribution and bot click settings and how these will affect your performance reporting. This tool helps ensure any changes you make to your settings align with your brand’s measurement needs.

The **Model comparison** tool provides a snapshot of your performance tracking data based on a message's sent date. However, given this preview is reflective of that point in time, these may not match what your actual reporting shows.

![](https://klaviyo.zendesk.com/hc/article_attachments/41070116528539)

The **Model comparison** tool will use the [set or custom mapped metric for revenue](https://help.klaviyo.com/hc/en-us/articles/25829057055899).

1. As noted in the sections above, once you have completed any changes to your attribution or bot clicks settings, select ****Compare model****.
   ![compare model button.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28886060833435)
2. In the **Attribution settings** panel on the right, you will see your current attribution window and bot clicks settings by default. To experiment with adjustments to any of these settings, click on the ****Preview**** tab.
3. Adjust any of your attribution or bot click settings as necessary. Once you adjust anything, you will see the following sections of the tool update and show you a preview:
   1. ******Preview settings****** ****section****
      Review how your Klaviyo attributed and other non-attributed revenue adjusts across each marketing channel. Compare this section to the **Current settings** section on the left to see how your performance changes when you adjust your settings.
      ![](https://klaviyo.zendesk.com/hc/article_attachments/36496806931867)
   2. ******Change**********section****
      In the **Overview** tab, review how your attributed, unattributed, and specific channel revenue performance changes depending on your chosen **Current vs.****Preview** settings. In the last column, you will see a percentage change indicating how these settings adjusted your performance tracking overall.

      In the **Top performing** tab, click on the ****Campaigns**** dropdown to toggle between your top performing sent campaigns (email, SMS, or push) or flows and how performance changes depending on your settings. In the last column, you will see a percentage change indicating how these settings adjusted your tracking per campaign or flow.
      ![](https://klaviyo.zendesk.com/hc/article_attachments/36496806932891)
4. Optional: click on the timeframe dropdown to adjust the preview's timeframe.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28858656252059)

   7 days is the default timeframe. Additionally, the max window for a custom number of days is 31.
5. Optional: select the****Count**** option to review data by total counts instead of revenue.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28859661622427)
6. Once you finish adjusting your attribution or bot click settings, select ****Apply settings****.

By choosing **Apply settings**, your attribution and bot clicks settings will update to match what you selected in your **Preview settings** section. Click this button only when you are satisfied with your settings. Additionally, note that any changes to attribution will apply to both historical and future conversions.

## Additional resources

[Understanding Klaviyo attribution](https://help.klaviyo.com/hc/en-us/articles/1260804504250)

[Understanding conversion tracking](https://help.klaviyo.com/hc/en-us/articles/115005248128)