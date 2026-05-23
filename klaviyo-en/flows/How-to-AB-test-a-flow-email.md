---
id: 6960371049115
title: "How to A/B test a flow email"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/6960371049115-How-to-A-B-test-a-flow-email"
section: "Test and optimize flows"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-04-21T13:55:04Z"
language: en
---

## You will learn

Learn how to use Klaviyo’s A/B testing experience to test individual emails in a flow, including things like subject line, discounts, and email content, etc. You can even use A/B tests to determine if plain-text emails perform better than image-heavy HTML emails.

## About flows and A/B testing

Flow email A/B testing includes the processes of:

1. Creating a single flow email and scheduling this email to send after a certain number of hours or days, just as you normally would.
2. Configuring two or more email variations for this single flow email — adjusting the subject line or core email content for each variation.
3. Selecting the weight of each variation to establish the percentage of recipients that will receive each email.
4. Having a winning variation chosen automatically after statistical significance is reached, or manually choosing a winner based on the highest open rate or highest click rate amongst variations.

## Perform a flow email A/B test

Creating an A/B test can be easily done through the flow builder. Note that after a test has completed for an email, you can create another test for the same email in the future if needed.

### Create a new test

1. To set up A/B testing for an individual email in any flow, click on the email within the flow builder.
2. Configure the content of the email if you have not already done so.
3. Click ****Create A/B test**** in the **Email details** panel.

![Create A/B test button in the Email details panel](https://klaviyo.zendesk.com/hc/article_attachments/28713339726619)

When you create an A/B test for an existing flow email, two new copies of the email are created. If the flow email is live and has already been sending, when the A/B test is published the analytics for each of these copies are tracked separately. We do not continue tracking analytics for the original email once you have added a variation.

### Edit variations

After creating a new test, you will be taken directly to the **A/B Test** tab of the **Manage****Content** window. Every test will automatically include 2 variations. When you click on a variation, you can edit the variation name, subject line, preview text, sender name, and sender email address.

1. To edit the content of the email, click the ****Edit Email**** button above the email preview on the right.

![When viewing the configuration options for a specific variation, there is an 'Edit Email' button in the top right.](https://klaviyo.zendesk.com/hc/article_attachments/28713384317211)

### Add a new variation

If you’d like to add another variation, you must clone 1 of the existing 2 variations.

1. Click the clone icon to the right of the variation you want to base your new variation on.
   ![The clone button is found to the right of the variation name.](https://klaviyo.zendesk.com/hc/article_attachments/28713384313499)
2. This will create a new variation which you can modify to be distinct from the original 2 variations.

![The cloned variation will appear below the original variations.](https://klaviyo.zendesk.com/hc/article_attachments/28713339674779)

### Delete a variation

An A/B test must have at least 2 variations, so a variation can only be deleted when there are 3 or more. Additionally, variations can only be deleted while a test is in **Draft** status. Deleting variations is disabled for live A/B tests.

1. To delete a variation, click on the trashcan icon to the right of the variation you want to delete.

![The delete button is is depicted with a trashcan icon and is found to the right of the clone button.](https://klaviyo.zendesk.com/hc/article_attachments/28713339678875)

### Choose the weight of each variation

At the bottom of the **A/B Test** tab, you will see the **Test Settings** section where you can edit the weight of each variation – this will establish the percentage of recipients that will receive each variation.

It's generally recommended to weigh each variation equally, but you can change the percentages to any amount you’d like.

You can also select the option to automatically choose distribution. This will set the distribution to be equal for each variation at first. Over time, if one of the variations performs better than the others, Klaviyo will automatically adjust the distribution to direct more recipients to the better performing variation while the test is still running.

![In the test setting section, you can configure distribution, winner selection, and notes for the A/B test.](https://klaviyo.zendesk.com/hc/article_attachments/28713339694107)

### Configure winner selection

Tests will default to automatically choose a winner based on click rate, but this can be changed.

1. In the **Test Settings** section at the bottom of the **A/B Test** tab, you can also configure winner selection by clicking on the ****Configure**** link under **Winner Selection**.


   ![Under the Winner Selection label, there is a link to open the Winner Selection modal.](https://klaviyo.zendesk.com/hc/article_attachments/28713339724443)
2. A modal will appear in which you can change the **Winning Metric** to ****Open Rate**** instead.
   ![The winner selection modal has options for selecting the winning metric (Click Rate/Open Rate) as well as turning on/off automatic winner selection.](https://klaviyo.zendesk.com/hc/article_attachments/28713384349083)

   For flow emails, only Open Rate and Click Rate are available as winning metrics.
   Using Click Rate is recommended since many factors such as Apple Mail Privacy Protection (MPP) can cause inflated open rates. For complete information on MPP opens, visit our [iOS 15: How to Prepare for Apple’s Changes guide](https://www.klaviyo.com/blog/apple-ios15-klaviyo).
3. In the **Automatic Winner Selection** section, there are 2 options:
   1. ****End test if the winning metric is determined to win with high statistical certainty (statistical significance)****: this option is checked by default. Uncheck the box next to this option if you’d like to manually end the test instead or choose the option to end the test after a specific date.
   2. ****Set a date limit:**** this option allows you to select a specific date to end the test automatically.
4. If you select both options, the test will end if statistical significance is reached or if the specified date is reached depending on which occurs first.
5. Click the ****Save Settings**** button to confirm your configuration.

### Publish a test

1. Once you have your variations configured, you are ready to publish your test. From the **A/B Test** tab, click the ****Publish Test**** button in the upper right.


   ![The Publish Test button is in the upper right of the A/B Test tab.](https://klaviyo.zendesk.com/hc/article_attachments/28713339702939)
2. A modal will appear asking you to confirm the publication. Click the ****Publish Test**** button to confirm.

![A modal will appear asking you to confirm that you want to publish the test.](https://klaviyo.zendesk.com/hc/article_attachments/28713384355483)

### Delete a test

1. If you wish to delete a test, from the **A/B Test** tab, click the arrow next to the ****Publish Test**** button and select ****Delete****.

![Clicking the arrow next to the Publish Test button will reveal the Delete option.](https://klaviyo.zendesk.com/hc/article_attachments/28713339709723)

## View A/B test results

1. You can view the results of a test while it is running or after completion by clicking the email within the flow builder and clicking the ****View test**** button.

![The View A/B Test button is in the left sidebar of the flow builder and will appear when a test has been created for a flow message.](https://klaviyo.zendesk.com/hc/article_attachments/28713384398107)

This will take you to the A/B Test Results page where you can view the following metrics:

- ****Recipients****
  How many people received the email
- ****Opens****
  What percentage/number of people opened the email
- ****Clicks****
  What percentage/number of people clicked through the email
- ****Conversion Metric****
  Total recipients who triggered the conversion metric the selected conversion metric for the email such as **Placed Order**.

![The A/B test results page has a chart for measuring performance as well as statistics related to open rate, click rate, and conversion metrics. ](https://klaviyo.zendesk.com/hc/article_attachments/28713384363675)

For more detailed information on the A/B test results page, please see our article on [how to review email A/B test results for flows](https://klaviyo.zendesk.com/hc/en-us/articles/9360405808027).

### Manually choose a winner

In most cases you will want to wait for your A/B test to automatically choose a winner, but there may be a situation in which you want to end an A/B test early. In that case, follow the steps below.

1. From the **A/B Test Results** page you can manually choose a winning variation for the test by clicking the ****Choose Winner**** button in the top right corner of the page.


   ![The Choose Winner button is in the top right of the A/B test results page.](https://klaviyo.zendesk.com/hc/article_attachments/28713384368795)
2. A modal will appear asking you to choose a winner from each of your existing variations. Select the variation you’d like to win from the dropdown then click the ****Choose Winner**** button.

![A modal appears with a dropdown with each message variation to choose as a winner.](https://klaviyo.zendesk.com/hc/article_attachments/28713384386075)

Changing a message’s status from live to draft status will end the test and automatically choose a winner based on the winning metric – the first variation will be chosen if there is a tie.

Learn more about A/B testing in flows: