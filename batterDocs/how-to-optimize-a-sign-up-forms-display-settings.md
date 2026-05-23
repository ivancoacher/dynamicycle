<h1>How to optimize a sign-up form&#039;s display settings</h1>

## You will learn

Learn how to run an optimization test on a Klaviyo sign-up form to determine the best time for the form to display to website shoppers. In an optimization test, Klaviyo runs a series of AI-generated experiments to determine the most effective display timing settings that increase a form’s submission rate.

An optimization test is similar to an A/B test in that its purpose is to identify areas that work well or need improvement. However, an optimization test uses AI, and is completely automated to save you time and deliver more accurate results.

![](https://fast.wistia.com/embed/medias/fque2tcpwb/swatch)

## Before you begin

You must have at least 400,000 profiles (note that this is total profile count) to qualify for optimization tests.

## Create an optimization test

Create and run an optimization test with your desired test settings to determine the optimal display timing settings for your sign-up form. Once you complete an AI optimization test, your sign-up form will automatically update with the new display timing settings and that version will be live on your site.

Note that you can only run 1 optimization test at a time.

To create an optimization test:

1. Select ****Sign-up forms**** from the left-hand navigation.
2. Create a new sign-up form, or open the form editor for an existing form by selecting the 3 dots, then ****Edit form****.

   You cannot make any edits to the sign-up form (e.g. styles, content, behavior, etc.) while an optimization test is running. If you do need to make a change while an optimization test is running, you’ll have the option to end the test, make your desired changes, and then begin a new test.
3. In the top left corner, select ****Create A/B test****.
   ![The Create A/B Test button highlighted and being selected from the top menu bar in the sign-up form editor.](https://klaviyo.zendesk.com/hc/article_attachments/28720762175899)
4. Select ****Optimization test****. You cannot begin an optimization test if an A/B test is currently in progress.
   ![The Create Test popup that appears when you click Create A/B test on a sign-up form, and Optimization test selected from the test options on the menu.](https://klaviyo.zendesk.com/hc/article_attachments/28720762194843)
5. Under **Test name** you can change the default name of your test. Beneath this, verify the control group’s timing settings next to **Settings**. The control is your current form.
6. Select ****Continue to test settings****.
7. On the **Test settings** modal that appears, choose the percentage of traffic for each group:

   - **Control group**
     This is the group that will always see the current version of the form**.**
   - **Test group**
     This is the group that’s tested throughout the phases of the optimization test.![](https://klaviyo.zendesk.com/hc/article_attachments/34320465316763)
8. Optional: Select the ****Advanced settings**** tab if you'd like to further specify the types of variations that AI will generate and test against your current form. From here you can remove any timing settings that you don't want to include in the tests, or specify values for a time delay or scroll percentage.

   ![The Create Test modal showing the Advanced settings options where you can select the display rules that Klaviyo AI will use to create variations in an optimization test.](https://klaviyo.zendesk.com/hc/article_attachments/28720790665371)

   Optimization tests do not currently allow page view variations, so the timing option to display **After visitor sees a certain number of pages** will not be considered in the test. If you have a sign-up form set to display based on a page view rule, you will not see the option to create an optimization test.
9. When you’ve chosen your test settings, select ****Start optimization.****

- If your sign-up form does not have enough traffic, a callout will appear stating that Klaviyo does not recommend running an optimization test on this form. We suggest running optimization tests on sign-up forms with higher traffic to see the most accurate results. If you choose to run the test on a low traffic form, the test will run for a maximum of 90 days.

The optimization test will run through various phases, using AI to test and measure your current form against variations with different display timing settings based on your test set up. After phase 1, Klaviyo will choose a variation that it wants more data on for continued testing in phase 2 and 3. The experimentation process will continue running until AI recommends a form variation 3 times, or until 90 days have elapsed since the start of the test. At either point, the test will end, and the optimal display timing settings identified by AI will be automatically updated in your sign-up form.

## Monitor an ongoing optimization test

To monitor an optimization test while it’s running:

1. Select ****Sign-up forms**** from the main navigation.
2. Click on the form that has an optimization test in progress. It will feature a small “Running an optimization” banner in the **Status** column.
3. In the menu bar, click on the ****A/B Test results**** tab.
4. Make sure that the dropdown at the top is set to **Optimization test**, along with the name of the test you’d like to view.

![The A/B test results tab a form with the ongoing optimization test showing the two dropdown menus at the top set to Optimization test and the correct name of your test, respectively.](https://klaviyo.zendesk.com/hc/article_attachments/28720790627867)

From here, you’ll see an overview of the ongoing optimization test. This includes a visual of the sign-up form being tested, and a breakdown of the following results for the phase in progress:

- ******Submit rate lift******
  The percentage difference between the control group’s submit rate and the highest performing variation’s submit rate.
- ****Win probability****
  The percentage likelihood that the variation will perform better than the control group.
- ****Traffic distribution****
  The traffic percentages that you selected when initially creating the test. They reflect how much traffic goes to the control group and the test variations (AI generated variations of the form), respectively.
  ![The top half of the Optimization test results page where you can view an overview of the test's planned phases, and cards depicting submit rate lift, win probability card, and traffic distribution.](https://klaviyo.zendesk.com/hc/article_attachments/28720762187035)

  On the bottom half of the **A/B Test results** tab, a results table displays each completed phase in the optimization test. Each phase is broken down by:
- ****Start date****
  The date that this phase began.
- ****Eligible unique views****
  The number of unique users eligible to view a sign-up form in this testing phase. Because you’re testing display timing, views will be counted by the number of unique users who could have seen a form in order to accurately compare form variations.
- ****Eligible submit rate****
  The number of unique submitted form events divided by the number of unique users eligible to see the form variation (**Eligible unique views**). For example, if 2 unique users view a form variation, and 1 of them submits the form, the submit rate will reflect 50%.
- ****Win probability****
  The win probability for the variant being tested against the control group.
- ****Submit rate lift****
  The percentage increase of submission rates in comparison to the control group.

Click the dropdown arrow on any phase to see the key details and data for the control group, as well as a breakdown of the raw data (i.e., **Submit rate, Win probability,** and **Submit rate lift**) for each variant tested during the phase.

![The table at the bottom on the Optimization test results page where you can see a breakdown of data across for completed phase and variation in the test thus far.](https://klaviyo.zendesk.com/hc/article_attachments/28720762217755)

A phase will end when at least 2 days have passed, and both the control and the variation being tested have received a minimum of 600 views. For Phase 1, when multiple variations are tested against the control, the variations must average 600 views. Alternatively, a phase will also end if the control group has statistically significantly better performance after 1 day.

The optimization test will continue running phases until 1 form variation is identified as having the optimal display timing settings in multiple, consecutive phases. You can view the raw data from each phase at the conclusion of the optimization test.

### Edit an optimization test name

To edit the name of optimization test while it’s in progress:

1. On the **Sign-up forms** page, select the form with the optimization test running.
2. Click on the ****A/B Test results**** tab.
3. In the top right corner, select the 3 dots, then ****Edit details****.
   ![The option to Edit details being selected from the 3 dots dropdown menu in the top right corner of the Optimization test results page.](https://klaviyo.zendesk.com/hc/article_attachments/28720790636699)
4. Under **Test name**, replace the current name with your desired change.
5. Click ****Save****.

![The Rename optimization test popup where you can change the test name that you previously set.](https://klaviyo.zendesk.com/hc/article_attachments/28720790642459)

You cannot make edits to the sign-up form itself while an optimization test is in progress. If you enter the editor for a sign-up form with an ongoing test, a modal will ask if you want to end the test in order to make edits to the form, and how you’d like to end it. You can either:

- ****Keep control variation****
  Selecting this option means choosing the control sign-up form, which was tested against the different variations during the test, as the the highest performing variation. Note that no changes would be made because this is the sign-up form that you initially began the test with.
- ****Replace control with highest performing variation****
  Selecting this option means choosing the highest performing variation from the most recent test phase as the highest performing variation. Klaviyo will replace the sign-up form that you began the test with with the the highest performing form variation.

![The Editing your form will end the optimization test modal that appears if you attempt to enter the sign-up form editor for a form with an optimization test in progress.](https://klaviyo.zendesk.com/hc/article_attachments/28720790645147)

If you choose to end an ongoing test to make modifications to the sign-up form, you’ll need to create a new optimization test to start again.

## Manually end an optimization test

if you need to make adjustments to the test settings (i.e., site traffic distribution or variation selection settings), you have the option to manually end an optimization test, rather than wait for the results to identify a winner, To do so:

1. On the **Sign-up forms** page, select the form with the optimization test running.
2. Click on the ****A/B Test results**** tab.
3. In the top right corner, select the 3 dots, then ****End test****.
   ![The option to End test being selected from the 3 dots dropdown menu in the top right corner of the Optimization test results page.](https://klaviyo.zendesk.com/hc/article_attachments/28720762209947)
4. On the confirmation modal, choose a winning variation. You can choose either the control group, or the winner of the current phase of the test.
   ![The End test popup where you can opt to manually end an optimization test and choose to either Keep control variation, or to Replace control with the highest performing variation thus far.](https://klaviyo.zendesk.com/hc/article_attachments/28720790652443)

   If you choose the **Current winner** as the winning variation, your original sign-up form will automatically update with the corresponding display settings.
5. Select ****Choose winner and end test****.

## How a winning variation is chosen

When an optimization test is complete, the sign-up form will automatically update to the winning display timing settings, or remains the same if the control won, and the test status changes from **Live** to **Completed** on the **A/B Test results** page.

At this point, an overview of the test and finalized results will display for your analysis, and 1 of 3 results will show:

1. **Successfully optimized**: A winning variation was identified

   - The AI test identified a variation that performed better than the control group. A description of the winner will display under **Winning variation**.
2. **Successfully optimized**: The control is the winner

   - The control outperformed all variations tested against it. **Submit rate lift** will show 0%, and a description of the control's display timing settings will display under **Winning variation**.
3. **Inconclusive results**:

- The AI test did not have sufficient data during the 90 days to reach conclusive results, despite running multiple phases. Because of this, the control will display as the winning variation, and the **Submit rate lift** will reflect 0%.

## Next steps

See [how to view sign-up form responses](https://help.klaviyo.com/hc/en-us/articles/4406228129051) to dive deeper into the information collected from your new subscribers in your sign-up forms.

If you have multiple sign-up forms live on your website, consider [enabling collision prevention display settings](https://klaviyo.zendesk.com/hc/en-us/articles/19788320859419) to keep multiple sign-up forms from appearing at once.
