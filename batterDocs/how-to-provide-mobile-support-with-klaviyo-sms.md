<h1>How to provide mobile support with Klaviyo SMS</h1>

## You will learn

Learn how to use SMS for customer support, allowing you to quickly answer subscribers’ questions and hear their feedback. With [Klaviyo two-way messaging](https://help.klaviyo.com/hc/en-us/articles/360059002271), you can leverage SMS to provide your current subscribers support and a better overall experience.

## Before you begin

Note that two-way messaging is only available when:

- The customer is subscribed to SMS
- The customer texts your number first
- You're using a number that can receive text messages (i.e., not a branded sender ID)

## Mobile support checklist

For this process, we highly recommend completing all of the steps below in order to provide the best experience for your subscribers:

- [Create a list for those signing up for support](#h_01GJQSCEVQA9ZCEXG1WAVXVSB4)
- [Add a subscribe keyword](#h_01GJQSCSVT5QDP9P0PZ7WTYGVP)
- [Set up subscribe method](#h_01GJQSCZ1R0QB58ZGSW39DME9J)
- [Add forms to product/website pages](#h_01GJQSD589MWCG0QBDDBZ5DJH9)
- [Build a flow to prompt customers to ask a question](#h_01GJQSDC8540H3SEBNQPQ7T68F)
- [Create a segment to exclude support-only subscribers](#h_01GJQSDKMMVWCNKZ4FPGC5GJBP)
- Respond to the customer

## Create a list for support questions

First, make a new list for those texting in with questions.

1. Navigate to ****Audience >**** ****Lists & Segments**** on the left sidebar.
2. Click ****Create List/Segment****.
3. Choose ****List****.
4. Pick a descriptive name for the list (e.g., “Support Qs- SMS”).

![Example of a list for people who want support](https://klaviyo.zendesk.com/hc/article_attachments/28717987335323)

You may want to [disable double opt-in for this list](https://help.klaviyo.com/hc/en-us/articles/115005251108). This can help streamline the process for those with questions. If you do so, it is especially important to create a segment of support-only subscribers, discussed farther down in this article, and exclude them from your campaigns.

## Add a unique subscribe keyword

For your forms, you’ll need to have a unique subscribe (also called a custom) keyword for when people want to ask you a question.

1. Navigate to your organization name in the bottom left.
2. Click ****Settings > SMS > Automations****.
3. Select ****Add Subscribe Keyword**** in the **Subscribe Keywords** section.
   ![Keywords section in the SMS automations page](https://klaviyo.zendesk.com/hc/article_attachments/28717993167003)
4. Name the keyword, making sure it’s not similar to another keyword (in particular, do not use a variation of “Info” or “Help”).
5. Set the new keyword to add subscribers to the list you just created before clicking ****Save****.
   ![Modal to create a new subscribe keyword](https://klaviyo.zendesk.com/hc/article_attachments/28717993137307)

After you save, you’ll see the new subscribe keyword along with the list it sends to and the $source profile property under **Subscribe Keywords**.

![Subscribe keywords section, showing the newly created keyword for support](https://klaviyo.zendesk.com/hc/article_attachments/28717993143323)

For more information about subscribe keywords, check out this [guide on adding, updating, and deleting custom keywords](https://help.klaviyo.com/hc/en-us/articles/360050384091).

## Set up your forms

For the best customer experience, you’ll need to make 2 signup forms. The first is a click-to-text form for mobile users, and the second is simply a message for desktop users that says customers should text your number and use a subscribe keyword.

Below, we discuss creating embedded forms, but another good option for desktop is a flyout form. If you use a flyout form instead, consider setting them to appear a few seconds after a page loads, so that you're offering help to those who are "stuck." It's not recommended for mobile: only desktop.

![Example of a flyout form for support](https://klaviyo.zendesk.com/hc/article_attachments/28717987354011)

### Desktop form

Let’s start with the desktop embed form.

1. Go to ****Sign-up forms**** on the left-hand sidebar.
2. Click ****Create Sign-up Form > Create from Scratch****.
3. Name the form, select the list you just created, and choose ****Embed****.
4. Delete any unnecessary fields, such as email and buttons, and add in the text you want to show on your site.
5. Drag in a text field.
6. In the field, add a message with your subscribe keyword and SMS number. For instance, “Want more information? Text QUESTION to XXX-XXX-XXXX.” (To find your SMS number, go to ****Settings > SMS**** .) If you have double opt-in enabled are sending to either the US or Canada, you may also want to call out that someone must then text “Yes” to get an answer.
7. Add in a phone number field.
8. Check the **Collect SMS consent** box.
9. Edit the disclosure language, making sure to link to your terms of service and privacy policy.
   ![Disclosure language for collecting SMS consent](https://klaviyo.zendesk.com/hc/article_attachments/28717987360283)
10. Go to the ****Targeting & Behaviors**** tab.
11. Change the form to ****Desktop Only****.
12. Add in any countries [where Klaviyo SMS is available](https://help.klaviyo.com/hc/en-us/articles/4402914866843), as you can only collect consent from people in those regions.
13. In the upper right, set the form to ****Live**** and copy the embed code.
14. Click ****Publish****.
    ![Example of embed code when a form is about to be published](https://klaviyo.zendesk.com/hc/article_attachments/28717993136027)

### Mobile form

For your mobile form

1. Clone the desktop form, name it, and use the same list as for desktop.
2. Drag in a button to make it easy for customers to get their questions answered.
3. Edit the text of your button to include a clear call-to-action, encouraging customers to click.
4. Click the button on the form and change the action from ****Submit Form**** to ****Subscribe via SMS****. This will automatically change the form to be mobile-only.
5. Change the subscribe keyword to the one you created for customer support and add in your subscribe message.
   ![Changing the subscribe keyword for the mobile form to the newly created keyword](https://klaviyo.zendesk.com/hc/article_attachments/28717993133723)
6. In the upper right, click ****Publish****. A modal will appear with the embed code and a warning to make sure you’ve linked to your terms of service and privacy policy.
7. Click ****Publish**** to set the form live.
   ![Example of the embed code showing when a form is going to be published](https://klaviyo.zendesk.com/hc/article_attachments/28717987372315)

## Embed the forms

There are several places where you might want to put these forms, including in the footer, product pages, and any contact or help pages on your website. How you embed the form depends on your integration, but generally, you’ll need to go into your theme, theme files, and then paste the embed where you want it to appear. This [article on pasting embed codes](https://help.klaviyo.com/hc/en-us/articles/360006897412) provides more information.

## Build a welcome flow for customer support

Your welcome flow for those texting in questions will not be your regular welcome flow.

1. Create a list-triggered flow using your SMS support list.
2. Drag in an ****Update Profile Property**** action directly after the trigger. (Note that someone must have the property on their profile before it can be used in a flow.) For example, you may apply a profile property titled "Support."
3. For the first message in this series, use something like, “Hey there! How can we help you? Please keep in mind that our office hours are 9 to 5 Mon–Fri, and we’ll respond as soon as we can.”
   - Acknowledge that they’re looking for help.
   - Don’t send a standard welcome series message where you thank them for subscribing, as this may make them worry that they joined your main subscription list when it’s highly possible that they only want answers to a specific question.
     ![Example of the mobile support flow](https://klaviyo.zendesk.com/hc/article_attachments/28717993153051)

### Optional: give recipients the choice to continue to hear from you

1. After the first message, add a time delay.
   Give enough time for you to have fully answered and followed up with the customer. We recommend between 3–7 days, depending on how much time you want to leave after your last response.
2. Add another message asking if they want to continue to hear from you.
   For example, you can say: “Want to continue hearing from us via text? Reply with TEXT ME to get special deals, early access, + more. If you say NO or don't respond, we'll only text you if you’ve reached out with a question.”
3. Follow the message with a time delay to allow a little time for someone to respond (e.g., 2 to 3 days).
4. Add a conditional split to separate who has sent an SMS in the last few days where the message body has the phrase you used in the previous message (e.g., TEXT ME).
5. Drag in an ****Update Profile Property**** action to remove the profile property for anyone who responded with this phrase.
6. For everyone else, keep the profile property in place, as we’ll use it to create a segment of those only interested in support.
   ![Adding a profile property to allow support subscribers to opt out](https://klaviyo.zendesk.com/hc/article_attachments/28717993157531)

## Create a segment to exclude support-only subscribers

This is perhaps one of the most important things to set up. It’s critical that you don’t treat someone who’s looking for answers the same as someone who wants to hear from you on a regular basis. Instead, you’ll foster a relationship with these subscribers via the flow above.

To exclude this group from your regular communications, you’ll need to create a new segment. The conditions for this segment should be that someone is consented to SMS and is either not in your main SMS subscriber list(s) or has the profile property you used in your welcome flow.

For instance, let’s say we have 2 lists with SMS subscribers named “Newsletter” and “SMS Subscribers” and our customer support welcome series adds Support equals true to profiles. In this case, the segment conditions would be as follows:

- If someone is or is not consented to receive SMS > Person is consented to receive SMS
  AND
- Properties about someone > Support is true
  Or
- If someone is in or not in a list > Person is not in Newsletter
  AND
- If someone is in or not in a list > Person is not in SMS subscribers

![Segment of SMS support subcribers](https://klaviyo.zendesk.com/hc/article_attachments/28717987368859)

Once created, exclude this segment from all SMS campaigns going forward. This will help you avoid texting those who aren’t interested in SMS marketing content.

## Additional resources

- Learn more about [SMS conversations in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/360059002271)
- Get advice for building your SMS program:
  - Blog post: [SMS marketing strategies for all levels [+12 Pro tips]](https://www.klaviyo.com/blog/sms-marketing-strategies)
  - Help Center: [your strategic guide to Klaviyo SMS success](https://help.klaviyo.com/hc/en-us/articles/25220861016091)
