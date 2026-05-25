---
id: "360036238671"
title: "How to A/B test flow SMS messages"
source_url: "https://help.klaviyo.com/hc/en-us/articles/360036238671-How-to-A-B-test-flow-SMS-messages"
section: "Test and optimize flows"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-04-21T13:56:51Z"
language: "en"
---
You must have [SMS set up in your account](https://help.klaviyo.com/hc/en-us/articles/4404274419355) to use SMS features.

Learn how to A/B test your SMS messages in flows and find inspiration on what to test.

## How to test your SMS messages

The best approach for testing your SMS flow message depends on what you want to test.

Click on what you want to test for details on how to do it.

- [Test message content](#h_01GM6F1HM4KJ3J8EMXC3SRV0EC)
  - MMS versus SMS
  - Emojis
  - Discounts
  - CTAs
  - Personalization
- [Timing or number of messages](#h_01GM6F1SXKAH0QXXMX00FFKS7D)
- [Message channel](#h_01GM6F200ZDGTEHK09TNTM6H9X)
  - Email versus SMS
  - SMS versus push

****Best practices for A/B testing SMS****

As with email, there are several best practices for A/B testing SMS:

- Test 1 aspect at a time
- Include a link and use the Klaviyo link shortener
- Keep any images or GIFs under 600 KB
- Test different types of SMS campaigns
- Optimize your CTA and message text

You should also test different types of SMS flow messages; e.g., abandoned cart and welcome. What performs well for one type of message may not perform well for another. Further, a flow might yield different results than a campaign message, so do not apply the results of an A/B test to every message you send.

## Test message content

1. Navigate to the flow where you want to A/B test an SMS.
2. If you haven’t already, drag an SMS into the flow.
3. In the left sidebar, click either ****Configure Content**** or ****Edit****.
4. Write new content or edit existing copy (you will need to have something typed in the message box before A/B testing is available).
5. Click ****Create A/B test****.
   ![Message creation screen, showing the A/B test option](https://klaviyo.zendesk.com/hc/article_attachments/28720657265563)
6. In the box for message B, click ****Edit Message****.
   ![A/B test settings screen, where you can edit a variation](https://klaviyo.zendesk.com/hc/article_attachments/28720657269531)
7. Change the content in the message editor box.
   As a best practice, only test 1 element of a message at a time. For instance, you should either make the CTA different, add an image, or include an emoji; don’t do all 3 in a single message.
8. Optional: To add more variations, click the ****Clone**** button next to one of the existing variations. Then, click into the new variation and edit it.
   Note that you can have up to 25 variations.
9. Click ****Save and Exit****.
10. Optional: adjust the settings for the A/B test, such as:

    - Changing the sending distribution (e.g., the percent of people who will receive variation A versus variation B)
    - Configuring the winner selection settings
    - Adding notes for the A/B test (e.g., explain what you’re testing)![A/B test sending options in the settings page](https://klaviyo.zendesk.com/hc/article_attachments/28720669001755)

    For winner selection settings, only Click Rate is available as a winning metric for flow SMS messages.
11. Click ****Publish Test****.

****Note on editing an A/B test****

To edit the test (e.g., add more variations or update the message for a variation), you will need to decide to either:

- Continue with the existing test
  or
- End the current test and start a new one

We recommend the first if you plan to change something small about 1 of the variations, and you don’t think it should affect the results. For instance, continue with the test if you are simply fixing a typo or removing a few characters.

If the change is significant, we recommend ending the current test and starting a new one. For instance, you should do this if you are changing a CTA or making an SMS into an MMS (or vice versa).

Note that you’ll have to decide on this before you actually start editing.

****When I’m creating or editing my variations, will this affect my live messages?****

No. You can create or edit your variations for as long as you want, and it won’t affect what messages your subscribers receive until you publish the test.

Only after you publish your test will subscribers begin receiving the messages you created in your A/B test.

If you want to check what message is currently live, go to the ****SMS Content**** tab.

Further, note that editing the message in this tab will not affect the variations for the A/B test.

## Test the timing or number of messages

To test either the timing or number of messages in a flow, follow these steps:

1. Navigate into the flow.
2. Drag a conditional split and place it where you want to test.
3. In the left sidebar, click the **Select the condition** dropdown menu.
4. Choose ****Random sample****.
5. Select your percentage.
   Note that the percentage represents how many should go down the YES path. If you choose 10%, only 10% will go down the YES path, while 90% of people will go down the NO path.
   ![Example of A/b testing the timing of messages](https://klaviyo.zendesk.com/hc/article_attachments/28720657272859)
6. Drag in your messages and time delays onto each path.
7. Rejoin the split.

When testing the timing of messages, make sure the content is exactly the same on each path.

If you’re testing the number of messages, keep the timing and content of the messages as similar as possible. This is to limit the number of variables that can affect the results.

## Test message channel

Test the message channel (e.g., email or SMS) by following these steps:

1. Navigate into the flow.
2. Drag a conditional split and place it where you want to test.
3. In the left sidebar, click the **Select the condition** dropdown menu.
4. To compare an SMS against an email, choose **can receive SMS marketing**.
5. Leave the condition as **Person can receive SMS marketing**.
6. Click ****Save****.
7. Add an email to the NO path.
8. Place a conditional split on the YES path.
9. In the left sidebar, click the **Select the condition** dropdown menu.
10. Choose ****Random sample****.
11. Select your percentage.
    Note that the percentage represents how many should go down the YES path. If you choose 10%, only 10% will go down the YES path, while 90% of people will go down the NO path.
    ![Example of A/B testing the message channel](https://klaviyo.zendesk.com/hc/article_attachments/28720657275291)
12. Place an SMS on the YES path and configure the message.
13. Copy the email on the first NO path and drag it to the NO path below the random sample.
14. Rejoin the split paths.

## Determine a winner when using splits

When determining a winner using conditional splits, you will have to manually check the performance of each path. Depending on how many subscribers you have, it may take some time for you to get [statistically significant results](https://help.klaviyo.com/hc/en-us/articles/11233978755611).

If you’re trying to determine the significance when testing the number of messages, add up the numbers for every message on each path, rather than comparing, say, just the first messages in that path.