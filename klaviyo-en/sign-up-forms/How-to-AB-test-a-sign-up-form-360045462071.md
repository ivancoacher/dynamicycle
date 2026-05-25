---
id: "360045462071"
title: "How to A/B test a sign-up form"
source_url: "https://help.klaviyo.com/hc/en-us/articles/360045462071-How-to-A-B-test-a-sign-up-form"
section: "Test forms"
category: "Sign-up forms"
category_slug: "sign-up-forms"
klaviyo_updated: "2026-04-21T13:54:48Z"
language: "en"
---
## You will learn

Learn how to use A/B testing to evaluate the performance of various elements of your sign-up forms. By effectively analyzing the results, you can ensure that your forms resonate with site visitors and contribute to list growth.

## Preparing for your A/B test

Before you start creating your A/B test, consider these general guidelines:

- Test 1 variable at a time (e.g., coupon offering)
  - Focus on changing a single variable (element) at a time, such as a coupon, to clearly assess its impact.
- Start small with test variations
  - When testing a variable (e.g., coupon offering), begin with 1 or two variations to measure effectiveness. You can increase complexity in later tests as you collect more data, but don't use more than 4.
- Avoid mid-test changes
  - Don't alter test settings while it's live. Note that you can't edit the form variations themselves once a test is live; you must end the test to make these types of changes, so confirm all configurations beforehand.
- Allow for substantial test duration
  - Wait for statistically significant results or until you have a sufficient sample size of viewers to end your test. Remember, more variations require more traffic for reliable results.
- Understand statistical significance
  - Familiarize yourself with [how statistical significance impacts the results of an A/B test](https://klaviyo.zendesk.com/hc/en-us/articles/25187312302747).

## What to A/B test

|  |  |  |
| --- | --- | --- |
| ****Use case**** | ****Goal**** | ****Setup**** |
| Test a popup with a teaser | Measure the effectiveness of a teaser in your popup form. | Create 2 identical variations of your form, 1 with a teaser and 1 without, and compare results. [Learn more about teasers.](https://klaviyo.zendesk.com/hc/en-us/articles/4411540984859) |
| Test display timing | Determine the optimal timing for displaying your form on your website. | Test variations with different **Timing** settings (e.g., 1 appears after a visitor has scrolled a certain amount and the other at exit intent). **Timing** is configured in the ****Targeting & behaviors**** tab of the form editor. [Learn more about display timing](https://help.klaviyo.com/hc/en-us/articles/4413544555547#h_01HJV573090CKH5QJMHPFPAXD9). |
| Test your form with a coupon offer | Assess if providing a promotional discount in a form boosts submissions. | Create 2 variations, 1 offering a coupon and 1 without. Once a winner is declared, further test types of coupon offers (e.g., 10% off vs. free shipping). [Learn more about coupons in forms](https://klaviyo.zendesk.com/hc/en-us/articles/6038674938523). |
| Test your form's content | Test to learn what form copy, imagery, or layout resonates with site visitors and increases submit rates. | Test 1 content element at a time across multiple variations, such as:   - Colors or branding - Copy (header, body, or call-to-action text) - Brand voice - Visuals (different images or no image) - Use of gamification elements ([counter block](https://help.klaviyo.com/hc/en-us/articles/4413550187035#h_01J4SQ3GYMYJX5P816JCQ09QQZ) or [countdown timer](https://klaviyo.zendesk.com/hc/en-us/articles/11206946148891)) - Layout adjustments   [Learn more about form content.](https://help.klaviyo.com/hc/en-us/articles/4413537049883) |

Learn more [use case examples and setup from Klaviyo customers that leverage A/B testing to actively increase form conversion rate](https://www.klaviyo.com/blog/email-sms-list-growth-strategies).

## Creating an A/B test

### Creating a test

There are 2 different ways to create an A/B test for your sign-up form:

- On the ****Sign-up forms**** tab, click the 3-dots dropdown menu next to the form you'd like to test and select ****Create A/B test****.
- Open the the form editor for a sign-up form you'd like to test and select ****Create A/B test**** in the top corner.

No matter where you enter from:

1. Select ****Create A/B Test**** to get started.
   ![chandi1.jpg](https://klaviyo.zendesk.com/hc/article_attachments/39871161563419)
2. Next, name your test something descriptive. If you’re testing colors of the buttons on your newsletter popup, you could name the test **Newsletter - Color of Submit Button**.
3. After you’ve named your A/B test, give your sign-up form variations different so you can distinguish between them.
   - By default, it will come with the name **Copy # of Name of Form**. With the different color submit button example from before, you might have your forms named **Newsletter - Blue** and **Newsletter - Gray**.
   - Here, you can also add more variations by selecting the copy button. You can add up to 7 variations to your A/B test. Keep in mind, the more variations you add, the longer you’ll need to run your test. An ideal A/B test would have [between two to four variations](https://klaviyo.zendesk.com/hc/en-us/articles/360045012632). In the example below, there are three variations: the original form and the 2 additional tests.
4. After you’ve configured your test, select ****Create Test****.
   ![chandi2.jpg](https://klaviyo.zendesk.com/hc/article_attachments/39871161564443)

### Configuring the variations

After you’ve created your test, you’ll be directed back to the sign-up form editor. You will be able to toggle between the different variations of your form by selecting the name of your form. From this menu, you can also choose to change the name of the variation, create an additional variation, or delete the variation.

See the What to A/B test section for inspiration.

![In the signup form editor, the drowdown arrow next to the form's name showing the variations and allow you to edit them or add more.](https://klaviyo.zendesk.com/hc/article_attachments/28720893119003)

Once you’re done configuring your form, select ****Continue to Test Settings****.

![chandi3.jpg](https://klaviyo.zendesk.com/hc/article_attachments/39871161564571)

### Configuring A/B test settings

On the test settings page, the customizable settings of your test will appear here. Consider customizing:

- - Variation names
  - Traffic selection (Weight)
  - Winner selection
  - Notes

![The A/B test settings page for an example A/B test showing the settings available to customize, including title, variation weight, and winner selection settings.](https://klaviyo.zendesk.com/hc/article_attachments/28720893123739)

Note that you can also reach the test settings page by selecting your form on the sign-up forms list view page, then navigate to ****A/B Test Results > Edit Test****.

#### Traffic selection

From this section, you can determine how much traffic goes to the variations of your form. By default, each form will appear to an equal amount of viewers. As your test runs, if one of your variations is outperforming the rest, Klaviyo will direct traffic to the better performing form while the test is still running.

If you toggle to select **Weight - Manual**, you can specify how much traffic you want to go to each variation of the form. The amounts need to add up to 100%.

![The A/B test settings page with the variation weight menu highlighted and showing both variations are set to automatic traffic selection.](https://klaviyo.zendesk.com/hc/article_attachments/28720848040987)

#### Winner selection

Similar to the traffic selection section, you have 2 options in determining how to choose the winner of the test. You can end the test automatically or manually.

- ****Automatically****If you end your test automatically, it will end when there is 1 variation that outperforms the other(s) at a statistically significant level or when it reaches a particular date. You can also select both boxes and the test will end when 1 of the conditions are met. For example, if you have both conditions selected and your form will only run for a month, if the form has statistically significant results after a week, the test will end.
  - If you end your test when the results are statistically significant alone, Klaviyo’s data science model will do the math for you and pick a winner.
  - If you choose to send the test on a particular date, the test will end at midnight coordinated universal time (UTC).
- ****Manually****If you choose to end your test manually (uncheck both boxes), you will choose both the winner and the date that the test ends.

![The A/B test settings page with the winner selection section highlighted and showing that the test is set to automatically end when statistical significance is achieved.](https://klaviyo.zendesk.com/hc/article_attachments/28720848034459)

Regardless of which automatic selection you pick, after the test has finished, the form that wins will be live on your site.

Select ****Publish A/B Test**** once you've finished editing your test settings. Before your test is underway, Klaviyo will check if there is an issue publishing forms to your site and if your form has all of the content it needs (e.g., consent language, CTA, submit fields, etc.).

## Review A/B test results

While the test is running or after you’ve completed your A/B test, you can monitor the data in your account. Navigate to ****Sign-up forms****, then select your form. On the **Overview** tab, you can see how your form is performing overall. Select the ****A/B test results**** tab to dive into the analytics of your A/B test specifically.

![The A/B Test results tab selected in the menu bar from an individual form's analytics pages.](https://klaviyo.zendesk.com/hc/article_attachments/28720848051611)

From here, you can also edit your A/B test's settings. To do so, select ****Edit A/B test**** in the top right corner of the A/B test results tab****.**** Here you will be able to edit the test settings (i.e., name, variation weight, winner selection settings).

You won’t be able to change the test forms' content while the test is in progress. To edit the content, click ****Edit content**** to end the test, clone a new test to edit, and start again.

### Test overview

Under **Overview**, you’ll get a snapshot of how your test is performing. You can use the dropdown in the top left corner to toggle the different variations in your A/B test. The metrics shown in the **Overview** include:

- **Win probability**
  The win probability displays in the top left card. This percentage denotes the likelihood that the current variation that is winning will be the statistically significant winner. As your test gains more viewers and is live for a longer period of time, you should see this number increase. You’ll know when the test results become statistically significant from the label below the win probability. If you’re viewing a completed test, there will also be a reason stating why the test ended (e.g., manually ended by choosing a winner).
- **Start date** and **End date**
  The start and end date for the test are listed in the top right right card. If you did not set an end date, this will be left blank. If the test is completed, you’ll see the date the winner was selected.

  To manually stop the test and choose a winner at any time, select ****Choose Winner.****If you select this button at any time, you’ll have the option to end the test and set your winning form variation to live or draft mode.

![The top half of the A/B Test results tab showing the data from an example form's recently completed A/B test.](https://klaviyo.zendesk.com/hc/article_attachments/28720893132571)

Beneath these cards, the raw data from each form variation in your test is displayed. Next to each variation, you can see a breakdown of the following metrics by variation:

- **Current weight**
  This metric reflects current weight of traffic directed to each form. If you have manually selected how much traffic goes to each form, these numbers will be consistent with the settings you selected when you started the test. If you’re using Klaviyo’s data science model, you will see the weight of traffic changing over time, giving more traffic to the form that is winning and letting you gain more subscribers as you run your test.
- **Orders**The number of placed orders attributed to this form.
- **Average order value** (**AOV**)
  The store revenue associated to this form divided by the number of orders associated with the form.
- **Revenue**The sum of placed orders ($) which occurred after a form submission within the lookback window.

  To learn more about how revenue is linked to sign-up forms, see [Understanding revenue metrics for forms](https://klaviyo.zendesk.com/hc/en-us/articles/27695838219675).
- **Unique views**
  The number of unique users who have viewed a sign-up form variation (e.g., if 1 site visitor views your form twice, it counts as 1 view).
- **Unique submits**
  The number of unique users who submit a sign-up form variation or click a "Go to URL" button (e.g., if 1 site visitor submits your form twice, it counts as 1 submit). If the form has both a submit button and a “Go to URL” button, it will only count the event when someone submits the form.
- **Submit rate**
  The **Unique submitted** form value divided by the number of **Unique views**. Because this rate uses unique metrics, it will differ from the **Submit rate** on the **Overview** tab, which uses totals.

Note that if you are testing different display times in your A/B test (e.g., **Show immediately on page load** and **Show 30 seconds after page load**), you will see **Eligible unique views** and **Eligible submit rate** instead. Eligible views are based on the number of site visitors who could have seen this form, in order to accurately compare form variations. Scroll down to the FAQs to learn more.

### Form submit rate graph

Beneath the raw data is a plot of your variations, showing the **Form submit rate by variation** over the duration of the A/B test. If you’re interested in a particular date, hover over data points for more information.

![The Form submit rate by variation plot graph for an example A/B test.](https://klaviyo.zendesk.com/hc/article_attachments/28720893128091)

### Engagement rates

If you're running an A/B test on a multi-step form, there is a breakdown of the engagement rates for step in the form per variation, so you can understand where site visitors may be abandoning the form. Here you can analyze:

- **Step 1 engagement rate**This metric reflects the percentage of users who engaged with the first step of the sign-up form variant.
- **Users who completed all steps**This metric reflects the percentage of users who engaged with every step of the sign-up form variant.

Beneath this data, there is a chart of **Step completion rate by variation** chart, so you can visualize the engagement rates per step, and compare rates between form variations in the A/B test.

![The Engagement rates section of the A/B test results page for an example form, where you can measure engagement rates across the steps of multi-step forms.](https://klaviyo.zendesk.com/hc/article_attachments/28720848046619)

## FAQs

#### I have a notification that my form that has a time delay A/B test is calculating form submit rate differently. Why is that?

If you’re testing a time delay on your form, your form submit rate will be calculated by looking at the conversions of unique users eligible to see your form (**Eligible unique views**), rather than the number of total views the form had.

Say, for instance, your A/B test is evenly weighted and has the message, “Need help browsing?” In the test, 1 form shows immediately upon someone visiting your site, and the other form loads after a minute. While the same number of people will be queued up to see both forms, more people will see the form that shows immediately. While there will not be as many people who see the form with the delay, it offers help to confused shoppers, and thus could still have a greater form submit rate. To test if the form delay leads to a higher or lower submission rate, the form submit rate will not be the amount of submits as a percentage of the number of views, but rather the amount of submits as a percentage of the number of people who could have seen the form.

#### I selected both boxes for the Winner Selection part of my A/B test. Will the test end when both or either one of the conditions are met?

These checkboxes function as an OR condition, meaning that either one of the conditions can be met and the test will stop. Both conditions do not need to be met for the test to stop.

#### Can I edit the test settings for my form A/B test after it's already running?

Yes, click into your A/B test from your form and select ****Edit A/B Test**** to change the settings. You will not be able to change the content of the forms without ending your current test and starting a new one, however.

#### If someone doesn’t engage with a form that is a part of an A/B test, when the form shows to them a second time, will they see a different version of the form?

No, they will be cookied upon viewing the form the first time and will only ever see that variation unless they clear their cookies or are browsing in an anonymous browser.

#### When I create an A/B test for my form, will my form go to draft mode?

The form will stay at whatever state your form was in before you created the test. If it was live mode and you create an A/B test, the current version will be live. If it was in draft, the form will be in draft mode.

#### I had a typo in my form A/B test, so I published a new one. How can I permanently delete the test with a typo?

Go to the results of the test you want to get rid of by selecting on the form and going to A/B Test Settings then choose ****Delete Test****.

#### I set my form A/B test live, then afterward I realized I had a typo. I don’t want to stop the test, re-build it, and set it back live. What should I do?

Head to the A/B Test Settings page while the test is running by clicking ****Edit A/B Test**** from the form analytics and click ****Edit Content****. This will create a new draft A/B test, and you can make edits to it as needed and then set it live by clicking ****Publish A/B Test****.

#### One of my form variations is performing very poorly and I want to update the amount of traffic going to the form. Can I do that?

Yes. Click on your form and go to the A/B test settings for your particular form. Select ****Edit A/B Test**** and either change the weighting or toggle to automatic weightings where the model will take performance into account.

#### I want to test to see if different offers are more likely to convert. How do I make sure to give a different welcome series correlated to each form?

You can [adjust the list that a person is submitting to](https://community.klaviyo.com/sign-up-forms-38/how-to-change-the-list-that-your-klaviyo-form-is-pointed-to-359) for each variation. To make each variation go to different lists, click on your CTA button in the form and change the ****List to Submit**** under the ****Button Click Action**** section. From there, [trigger your welcome series flow](https://help.klaviyo.com/hc/en-us/articles/115002775172) based on someone joining each variation’s list and follow up with the associated offer.

#### I want to track who sees each form variation of the A/B test. How can I do that?

There are 2 ways that you can do that. You can [adjust the list that a person is submitting to](https://community.klaviyo.com/sign-up-forms-38/how-to-change-the-list-that-your-klaviyo-form-is-pointed-to-359) or you can [add in a hidden field that is submitted when someone clicks through on your form](https://help.klaviyo.com/hc/en-us/articles/115005074627-Guide-to-Profile-Properties#ask-customers-for-them5). If you want the different variations to go to different lists, select the button and change the ****List to Submit**** setting under the****Button Click Action**** section. If you want to submit through a hidden field, you would add in a property under the ****Submit Hidden Fields**** section. Then, create a segment based around each property.

## Additional resources

- [Best practices for A/B testing reference](https://help.klaviyo.com/hc/en-us/articles/360045012632)
- Course: [Creating an effective acquisition strategy using sign-up forms](https://academy.klaviyo.com/creating-an-effective-acquisition-strategy-using-signup-forms)
- [Getting started with sign-up forms](https://klaviyo.zendesk.com/hc/en-us/articles/360026474752)
- Course: [Enhance your marketing with A/B testing](https://academy.klaviyo.com/en-us/courses/enhance-your-marketing-with-ab-testing)