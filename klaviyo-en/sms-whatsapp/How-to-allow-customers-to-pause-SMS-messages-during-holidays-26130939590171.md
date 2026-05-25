---
id: "26130939590171"
title: "How to allow customers to pause SMS messages during holidays"
source_url: "https://help.klaviyo.com/hc/en-us/articles/26130939590171-How-to-allow-customers-to-pause-SMS-messages-during-holidays"
section: "Sending best practices"
category: "SMS"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-21T13:56:47Z"
language: "en"
---
## You will learn

Learn how to allow customers to pause receiving text campaigns without unsubscribing completely from SMS.

Use this strategy before you launch large, multi-message campaigns or around holidays that may be sensitive.

****Why give people the option to pause SMS?****

By giving the people the option to pause messages, you:

- Keep a subscriber who otherwise may have opted out.
- Give your customers a more positive experience by letting them choose if they want certain messages.
- Engage with a smaller, more interested audience, saving on SMS credits and achieving higher click and conversion rates on follow-up messages.

****What times of year should I do this?****

Give the option to pause before your biggest sending times of the year and any sensitive holidays, including:

- Black Friday/Cyber Monday
- Mother’s and Father’s Day
- Valentine’s Day and White Day
- Christmas
- Back to school
- Easter
- Australia Day

## Before you begin

The process for allowing customers to pause is:

1. [Decide on the property that will indicate a pause.](#h_01HZ29GD9ANSNG394C6MY5AA8S)
2. Ask subscribers to either:
   - [Text in a certain word](#h_01HZ29GD9A98Q4VT61RKXMWQDB).
     \*Note that this does not work for branded sender IDs.
   - [Click a button on a sign-up form](#h_01HZ29GD9BD6A61MKVVB2SD41Z).
3. [Create a segment of people with the property](#h_01HZ29GD9B9VCJZN0RE10BB3FS).
4. [Exclude the segment from any campaigns related to that holiday](#h_01HZ29GD9BBBVAEGKM9G1DYSMP).

## Decide on the property that will indicate a pause

The property will be used in your flow, form, segment, etc., so it’s important to think through what you want to use before you start setting these up.

You can use the same property every time or change it for each major promotion or holiday. Each approach has its own pros and cons, as explained in the table below.

|  |  |  |
| --- | --- | --- |
|  | ****Pro**** | ****Con**** |
| ****Re-use the same property**** | Single setup you can re-use every time with minimal changes | No insight into who has paused SMS for a certain holiday or event in the past |
| ****Use a unique property each time**** | Allows you to analyze who has opted out of past campaigns | Requires you to update the flows and segments for each new campaign |

Once you decide on your property, add it to at least 1 profile in your account.

Next, we discuss how to collect this property from your subscribers, starting with asking customers to text in a certain word. If you only have a branded sender ID, jump ahead to [learn how to collect a property using a button in a sign-up form](#h_01HZ29GD9BD6A61MKVVB2SD41Z).

## Ask customers to text in a word

If you have a number that can receive text messages (i.e., not a branded sender ID), you can:

1. [Choose the word for subscribers to text in](#h_01HZ29GD9AYN28NKSPV61NMAS5).
2. [Prepare your campaign to ask people to text you a certain word](#h_01HZ29GD9A3KYN103MYDCVT6BW).
3. [Use a flow to add a profile property for anyone who texts the keyword in](#h_01HZ29GD9AXXV5H05CGK2V798K).

### Choose the word for subscribers to text in

The word you choose to use should be:

- Unique enough that subscribers won’t text it accidentally (e.g., don’t use “heart” during Valentine’s Day).
- Not part of another common word someone might text in (e.g., don’t use “no” since it’s part of many other words, like “not,” “afternoon,” etc.)
- Easy enough for subscribers to spell and text to you.

### Prepare a campaign to ask if subscribers want to pause

We say “prepare” because while you need information from the campaign, you don’t want to actually send it until you finish setting up the flow.

1. Navigate to the ****Campaigns**** tab.
2. Click ****Create campaign****.
3. Name the campaign and choose ****SMS****.
4. Select ****Continue****.
5. Choose your recipients (i.e., anyone you plan to market to during the holiday).
6. Select ****Next****.
7. Design your message.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/33627695129883)
8. Return to the ****Campaigns****tab.
9. Find and hover over the campaign you just created.
10. In the modal that pops up, click ****Copy message ID****.
    Note: for campaigns, using either the ID in the URL or the campaign ID (typically ~26 digits) does not work. You must copy the message ID, as shown below.
    ![Copy message ID.jpg](https://klaviyo.zendesk.com/hc/article_attachments/32593201251867)
11. Do not send this campaign until you set up the flow (discussed in the next section).

### Create a flow that triggers when a subscriber texts your word

We’ll say that “pause” is the word subscribers will text in. Now, we need a flow to respond and add a profile property when a subscriber texts in this word.

We provide the basic steps here; however, see this article on [creating a flow to respond to inbound SMS messages](https://help.klaviyo.com/hc/en-us/articles/360049930372) for tips and more details.

1. Navigate to ****Flows > Create flow > Build your own****.
2. Name the flow, then click ****Create flow****.
3. Select ****All triggers > Metric****.
4. Choose ****Sent SMS**** as the action that triggers the flow.
5. In the **Trigger filters** section, click ****Add****.
6. Click ****Add trigger filter****.
7. Use the following filters:
   1. **Message > equals** [add the copied message ID]AND
   2. **Message body > contains** Pause
      OR
   3. **Message body > contains** pause
      OR
   4. Note: include alternate spellings,  typos, or capitalizations by adding ****OR**** between the filters.
      ![](https://klaviyo.zendesk.com/hc/article_attachments/34235862491675)
8. Click ****Save > Confirm and save****.
9. Add an SMS message directly below the trigger.
10. In the right sidebar, click ****Edit**** in the **Content** section.
11. Customize the content for that SMS.
    ![](https://klaviyo.zendesk.com/hc/article_attachments/33627695134107)
12. Select ****Save & continue****.
13. Under the SMS, add a **Profile property update** action.
14. Click ****+ Add step****.
15. Set the action to ****Create a new property**** and name the new property (e.g., **Paused?** for a generic property or **Paused-BFCM2024** if you want to change it for each promotion).
    Note that the property must exist on at least 1 profile before you can use it for a **Profile property update** action.
16. Set the property type to ****Boolean**** and value to ****True****, then click ****Save****.
    ![Adding a profile property for someone wanting to pause in the flow](https://klaviyo.zendesk.com/hc/article_attachments/28717888255003)
17. Click ****Review and turn on****.
18. Set the flow to ****Live**** and then save.
19. Go back and send the campaign to ask subscribers if they want to pause SMS.

If you also are using a branded sender ID, continue reading. Otherwise, skip ahead to [learn how to create a segment of people who asked to pause](#h_01HZ29GD9B9VCJZN0RE10BB3FS).

## Collect a property using a button on a form

For branded sender IDs, you need a method that doesn’t rely on people texting you back.

There are 2 steps to this:

1. [Create a form that asks if subscribers want to pause](#h_01HZ29GD9BJ6YH0VWYH221VVEB).
2. [Send a campaign that links to your form.](#h_01HZ29GD9B9CTZEQR9YBD7GPVB)

### Create a form that asks if subscribers want to pause

You can create a form and collect a hidden profile property whenever someone clicks a button.

To do this:

1. Create a full-page form in Klaviyo.
2. Design the form as you see fit, but make sure you include at least 1 button.
   ![Form with a single button asking customers if they want to pause](https://klaviyo.zendesk.com/hc/article_attachments/28717888260635)
3. Click on the button (e.g., “Pause” in the example above).
4. Under **Button Click Action**, set the following:
   1. **Action** to ****Submit Form****.
   2. **After Submit** to ****Show next step****.
      ![Form button settings to bring those who click the button to the next step](https://klaviyo.zendesk.com/hc/article_attachments/28717888262683)
5. Under **Submit Hidden Fields**, click ****+ Add a property****.
6. Set the property that you want (e.g., **Paused?** for a generic property or **Paused-BFCM2024** if you want to change it for each promotion).
   Note that at least 1 profile in your account must have this property before you can use it in your form.
   ![Adding a hidden profile property to the button](https://klaviyo.zendesk.com/hc/article_attachments/28717888267931)
7. Above the preview of your form, select ****Success**** to design the page that shows after a user clicks the button.
   ![Highlighting the Success step button at the top of the form](https://klaviyo.zendesk.com/hc/article_attachments/28717882219803)
8. On the **Success** page, confirm that the user will no longer get texts for that holiday.
   ![Example of a success page to confirm users paused after they click the button](https://klaviyo.zendesk.com/hc/article_attachments/28717888277403)
9. Select ****Targeting & behavior****.
10. In the ****Display**** tab, set the following:
    1. **Timing** to ****Immediately****.
    2. **Frequency** to ****0 days****.

       If you plan to re-use this form for any holiday in the future, uncheck the box for ****Don’t show again if form was submitted or if go to URL button was clicked****. This will allow the form to show every time someone navigates to the link.
    3. **Devices** to ****Both desktop and mobile****.

       ![Settings to display the form immediately and to all users](https://klaviyo.zendesk.com/hc/article_attachments/28717882242715)
11. Scroll to the top of the sidebar and click into the ****Targeting**** tab.
12. Change the targeting settings so that:
    1. **Visitors** to ****Show to any existing profile****.
    2. **URLs** to ****Only show on certain URLs**** ****>**** ****Containing > #pause****
       Note that here, “#pause” is an anchor link we’ll use for our campaign. The hashtag is required, but you can replace “pause” with another word.
       ![Form targeting settings to show the form on an anchor link](https://klaviyo.zendesk.com/hc/article_attachments/28717882230683)
13. Click ****Publish**** to set the form live.

### Create your campaign with a link to your form

1. Navigate to the ****Campaigns**** tab.
2. Click ****Create campaign****.
3. Name the campaign and choose ****SMS****.
4. Select ****Continue****.
5. Choose your recipients and tags.
6. Select ****Next****.
7. Design your message.
8. For the link, add your website, then add the anchor link (e.g., #pause) at the end.
   Example: [www.mywebsite.com#pause
   ![](https://klaviyo.zendesk.com/hc/article_attachments/33627695136539)](http://www.mywebsite.com#pause)
9. Click ****Next****.
10. Schedule or send the campaign.

## Create a segment of people who paused

The next step is to create a segment of everyone who texted with the profile property you added in your flow.

1. Navigate to ****Lists & segments > Create New > Create segment****.
2. Name your segment (e.g., Pause segment).
3. Add the profile property as the segment’s condition (e.g., **Paused?** or **Paused-BFCM2024**):
   **Properties about someone** > **Paused? equals true**![Segment conditions for anyone who pauses](https://klaviyo.zendesk.com/hc/article_attachments/28717882232091)
4. Click ****Create segment****.

## Exclude the segment from your campaigns

Once you create this segment, simply exclude it from any campaign, flow, or form that has to do with that holiday or time of year.

The example below shows how this looks for a Klaviyo campaign.

![Excluding a paused segment from a campaign](https://klaviyo.zendesk.com/hc/article_attachments/28717882236315)

## Additional resources

- [How to create flows to respond to sent SMS messages](https://help.klaviyo.com/hc/en-us/articles/360049930372)
- [How to use SMS in replenishment flows](https://help.klaviyo.com/hc/en-us/articles/16318679373595)
- [How to send order updates via SMS](https://help.klaviyo.com/hc/en-us/articles/18389135527323)