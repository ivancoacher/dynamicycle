<h1>Getting started with global holdout groups</h1>

## You will learn

Learn how to use global holdout groups to understand the impact and efficacy of your marketing. Global holdout groups provide a way to exclude a number of profiles from your messaging to determine the incremental success of your marketing program. These holdout groups allow you to compare and then analyze the base value of your marketing programs, as well as ways to continually optimize these strategies.

## Before you begin

You must have at least 400,000 profiles (note that this is total profile count) to qualify for holdout groups. This ensures that Klaviyo has enough profile data to compare the holdout group to your other profiles receiving marketing. We additionally recommend that you run holdout groups for 3 months to gather enough data.

Learn more about [when to or when not to use holdout groups](#01H8CZ7FWK8QTQC2W2MHR4C8YR).

## Using holdout groups appropriately

### How to use holdout groups

Holdout groups should be used when you want to test the efficacy of your marketing programs, and potentially any changes that you may make to these strategies. Holdout groups are helpful in that they provide a clear comparison to show the impact that your marketing strategies are making as they are not receiving any communications from you.

For example, you want to consider using holdout groups if you want to establish:

- The clear value and impact of your overall marketing program against costs.
- When making changes to your marketing program (e.g., adding in a new channel), the value that is associated with these incremental changes.
- If certain marketing activities are actually detrimental and producing negative results and need to be adjusted (e.g., too many flows at the wrong times to customers).

  ****Additional factors to consider with holdout groups****

  It’s important to consider the timing and application of when you may use holdout groups.

  Since those in a holdout group are withheld from receiving any emails, SMS, push notifications, sent via campaigns or flows you will want to consider the following factors:
- You can only have one active holdout group at a time to use for comparison with your marketing programs.
- A holdout group applies to all channels used in a campaign or flow; it cannot be turned on for one specific channel vs. another.
- A holdout group does not interfere with other important seasonal ecommerce events or times of year (e.g., Black Friday Cyber Monday).
- What messages that those, even in holdout groups, should always receive. Learn more about [overriding messages](#01H8DEG9AAKVP8AXQHXTZV0SQJ).

****Holdout groups vs. A/B testing****

Holdout groups are different in nature than A/B testing and the two functions should not be confused. Holdout groups allow you to understand the impact of your marketing communication by not sending anything to a group of people. In contrast, A/B testing allows you to compare 2 or more versions of your marketing communication. For example, you can compare 2 versions of an email campaign.

## Creating a holdout group

1. To create a holdout group, head to ****Analytics > Experiments**** and click on the ****Global Experiments**** tab.

Note if you are unable to access this page, you do not have the required 400K+ profiles needed to qualify. Additionally, only Owners, Admins, and Managers can create holdout groups.

2. Click on ****Create test****.

![create test.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28704486763675)

You will then be brought through a series of steps to set up and customize your holdout group.

3. Use the field on the left to add a number representing the percentage of marketable profiles that you want to put in your holdout group. As you update your percentage in the field, the numeric value will update the total count on the right. Use only numbers (out to 2 decimal points) in this field.

It is recommended to use about 5% of your total marketable profiles to create a holdout group. Once you have chosen your holdout group percentage, it cannot be modified once you complete this setup process and it is active. However, it’s important to note that your holdout group will grow as your company and subscriber lists grow, to remain consistent with the percentage you originally set up.

4. Once you are satisfied with your percentage, click ****Continue****.

![holdout_size.png](https://klaviyo.zendesk.com/hc/article_attachments/41316029264283)

5. By default, your holdout group will start on today’s date, but you will be able to choose your end date. Click into the ****Select Date**** field to bring up the calendar widget. From here, click on a ****date from the calendar**** to select your end date.

It is recommended to have a holdout group running for 3 months in order to gather enough data.

![start and end date.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28704486766491)

You can also ensure that certain flows deemed necessary are still received by profiles in your holdout group. To do this, you will override the holdout group rules for certain flow(s). For example, many welcome flows may be important enough that they should still be received by your holdout customers and therefore overridden.

This next step is optional and it is not required to override certain flows. However, it is advised that you consider which messages are important to your audiences’ experiences with your brand and consider using overriding where appropriate. Note that transactional messages (e.g., order confirmations) will always be respected and overridden so that your holdout group receives them.
You can also skip certain campaigns or even choose to skip flows at a later day through additional steps outside of this setup wizard. Complete the next steps below to finish setup and then review the sections of this guide on [overriding campaigns](#01H8DEG9AAKVP8AXQHXTZV0SQJ) or [flows](#01H8DDBC4848J8YHZRT4BAE6NH) for more information.
Additionally, by overriding certain messages so that your holdout groups receive them, this will affect the [holdout group analytics](#01H8DG51ASZMG00MHT61S880XB). You may see a decrease in overall marketing uplift as the holdout group is still receiving some messaging.

6. To make sure your profiles still receive certain flow(s), search by the flow name in the ****Search flows**** field to the left. You can also narrow your search for a particular flow by opening the ****Select tags**** dropdown and selecting certain tag(s) from the dropdown.

![field and tags flow lookup.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28704478662299)

You can additionally narrow your search for a certain flow by opening the ****All dropdown**** and either choosing ******Welcome Series****** or ******Browse Abandonment******. By choosing one of these options, you will only see these types of flows listed below.

![welcomes series dropdown.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28704478665627)

Finally, you can choose to look for flows based on status (**Live**, **Manual**, **Draft**). Open the ****All statuses**** menu and choose one of the options; this will then narrow your list below.

![status dropdown.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28704486780443)

7. Once you have found the flow(s) you want to override (i.e., your profiles will receive these flows), select the ****checkbox**** next to each applicable one and click ****Review****.

![selected flow override.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28704486781851)

If you do not wish to select any to override, click ****Skip****.

8. In the **Details** tab, review the settings including start and end dates and percentage of marketable profiles in the holdout group.

![review test, details tab.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28704486783131)

9. Click on the ****Overridden flows**** tab to review any flows that will still send to your holdout group profiles, as shown in the example below.

![overriden flows.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28704486784795)

10. If you have any changes to make click ****Back****. Otherwise click ****Start test**** if you are ready for your holdout group to be active.

## Editing or ending your holdout groups

If you have set up a holdout group and want to edit certain settings (i.e., name or end date) or end the group test early, head to ****Analytics > Experiments > Global Experiments****.

Here you will find the global holdout card (it will be the card with data above the history card).

![Holdout group_experiment_klaviyo.png](https://klaviyo.zendesk.com/hc/article_attachments/41317824834587)

### Editing an active holdout group

1. If you want to edit the name of your holdout group or the end date, click on the ****3 dot menu**** in the upper right corner of the card.

![three dot menu.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28704486787867)

2. Choose ****Edit details**** from the menu.

3. From here, you can edit your holdout group’s name in the **Edit test name** field. You can also adjust the end date by clicking on the ****Change test end date**** field and choosing a new date from the calendar widget.

![edit account holdout details.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28704478680731)

4. Once you are done with your edits, click ****Save****.

### Ending an active holdout group test

If you find that you wish to end your test early, you may do so via this card as well.

Note that ending a test early may result in insufficient or skewed data.

1. Click on the ****3 dot menu**** in the upper right corner of the card.

![three dot menu.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28704486787867)

2. Choose ****End test**** from the menu.

3. A modal will then appear asking you to confirm if you want to end the test and have your holdout group start receiving all marketing messages again. To confirm, click ****End test****. Otherwise, click ****Cancel**** to avoid completing this action.

![end test modal.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28704486789019)

### Reviewing overridden flows

1. If you want to review what flow(s) you may have overridden for your holdout group, click on the ****3 dot menu**** in the upper right corner of this card.

![three dot menu.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28704486787867)

2. Choose ****Active overrides**** from the menu.

3. Review the flow override(s) that you have chosen for this particular holdout group, if applicable.

If you wish to add additional overridden flows, you will need to [manually add these](#01H8DDBC4848J8YHZRT4BAE6NH).

![holdout group exaple settings.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28704478683419)

## Overriding additional flows

After you have gone through the initial holdout group setup, you may find that you want to add more overridden flows. In other words, you may have other flows that you want your holdout group to receive.

Overriding is set at the main flow level and profiles will receive all elements of this flow as normal. If you are running a flow with A/B tests, all variations will now reach the appropriate profiles in your holdout groups.

1. To add more overridden flows, navigate to ****Flows****. Find and click on an existing flow from the list or click on ****Create Flow**** to override holdout groups.
2. Once inside the flow, either create or click on the trigger in your flow.

Depending on what trigger you chose (e.g., list), this is where you will see the **Trigger Setup** panel on the left with the option to override an existing global holdout group. In the example below, the option to override a global holdout group is shown on a list trigger.

3. In the **Trigger Setup** panel, click on the ****Override global holdout**** group link.

![trigger setup.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28704486791707)

4. If you wish to send messages from this particular flow to those in your global holdout group, choose ****Yes****. Otherwise, choose ****No**** and exit the override process.

![trigger setup confirm.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28704478685211)

5. Click ****Save**** at the bottom of the **Trigger Setup** panel to save your changes. Click ****Cancel**** if you do not wish to save your updates.

## Overriding individual campaigns (email, SMS, or push)

It may be necessary to allow certain campaigns to reach your holdout groups. For example, you may want your global holdout groups to receive an individual welcome email from your brand. In this case, you will need to override the specific campaign to ensure that your global holdout groups receive this particular message or campaign.

1. Navigate to ****Campaigns****.
2. Search in the field or find the appropriate draft campaign from the list below. If you are creating a new campaign you can also add the override directly during setup at the same time.

You will not be able to edit sent campaigns.

3. Within the first campaign setup step, click on the ****Configure option**** in the **Recipients** section.

![campaign toggle option.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28704486794011)

4. If you wish to send this particular campaign to those in your global holdout group, choose ****Yes****. Otherwise, choose ****No**** and exit the override process.

![campaign confirmation message.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28704486793499)

5. Click ****Save**** to confirm your changes. Click ****Cancel**** if you do not wish to save your updates.

6. Continue setting up the rest of your campaign. When you are done, click ****Save & Continue********to Content****.

The **Ready to send?** screen will then confirm and show that your active global account group will not receive this campaign.

### Adding new marketing channels at a later date

If you add a new channel to an existing campaign (e.g., SMS), your settings will be respected from your initial campaign setup, including if you have chosen to override global holdout groups.

![add sms remix.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28704478689179)

If you wish to adjust this, follow the [setup directions above](#01H8DEG9AAKVP8AXQHXTZV0SQJ) and instead toggle the override option off.

## Reviewing if a profile is or was part of a holdout group

You can review if a particular profile(s) is currently or was part of a global holdout group at one point.

### Within a singular profile

1. Navigate to ****Audiences > Profiles****.
2. Search in the field above or choose a profile from the list below. A banner, as shown in the example below, will let you know if a profile is part of global holdout group.

![participant banner profile.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28704478691483)

You can also see if a profile was previously part of a holdout group and when this occurred. Removal from a holdout group means that the test was ended and the profile was removed from it.

![profile events log.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28704486800923)

If a profile was merged, future sends will respect the holdgroup status of the merged profile.

### Within flows

1. Navigate to ****Flows****.
2. Use the search field above or find the flow from the list below.
3. Click on a message in the flow that has been skipped.
4. View the left-hand panel for a given flow message to see the **Analytics (Last 30 Days)** section. Here, you will see a line for skipped activity.

![skipped reason in flow.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28704486802587)

5. Click ****Skipped**** to be directed to the email's **Recipient Activity** tab and the **Skipped** section automatically. This section shows why individuals have been skipped at send time for a given flow message, including if they were in a global holdout group.

![global holdouts suppresed view.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28704486804379)

### Within campaigns

1. Navigate to ****Campaigns****.
2. Search in the field or find the appropriate sent campaign from the list below.
3. Click on the ****Skipped Activity**** tab. This section will show why individuals have been skipped at send time for this particular flow message, including if they were in a global holdout group.

![global holdouts suppresed view.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28704486804379)

## Reviewing analytics on holdout groups

### Global active holdout group card

The global holdout card at the top of the analytics section will detail all information and data on any currently active holdout group. This card is especially helpful as it provides a clear way to review the success of your marketing strategies and the revenue, conversions, and uplift associated with them.

![Holdout group_experiment_klaviyo_coimpleted.png](https://klaviyo.zendesk.com/hc/article_attachments/41317824844315)

The top of your card will note the overall marketing lift percentage, as shown below. This represents the lift of your marketing program compared to those in the holdout group who didn’t receive any messages. This metric is critical to understanding the overall impact of your marketing program.

![marketing lift.png](https://klaviyo.zendesk.com/hc/article_attachments/41317824850203)

Below the marketing lift, will include data on:

- ****Holdout percentage****
  The percentage of total marketable profiles who didn't receive any marketing messages. This is derived from your initial holdout group setup.
- ****Win probability****
  Probability that your marketing program provides a meaningful improvement over the holdout group.

  Note that if you have 10 or fewer samples from both your treatment and holdout combined, you will not see a win probability reflected yet.
- ****Treatment group****
  The main group receiving all of your marketing.
- ****Holdout group****
  The group that is held from receiving emails, SMS and push notifications sent through campaigns and flows.
- ****Marketable profiles****
  Any profile that can be emailed through Klaviyo is considered a marketable email profile. There are 2 main categories of active profiles:
  - ****Subscribers****
    Subscribers have filled out a signup form or otherwise explicitly consented to receive email marketing.
  - ****Profiles added by general engagement****
    It is possible for someone to share their email with you without explicitly consenting to ongoing email marketing. For example, someone who placed an order or abandoned a checkout on your site may have added their email address during the checkout process, but never explicitly opted in.

The last two columns represent the conversion metric your account is using, reflected by total raw number and then percentage this represents out of the total. Note that is total conversions made by your profiles and not attributable conversions.

### History card

The history summary card provides the data for all your holdout groups. This card is especially helpful for seeing any incremental changes that you may have made to your marketing programs and how these affected the conversions and uplift. Here, you can trace back these changes or points in time and track what was successful in your programs.

![history card-updated.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28704486806683)

Columns will represent the following:

- ****Name****
  Name of the global holdout group you set up.
- ****Start date****
  When the global holdout group was set up and first active.
- ****End date****
  When the global holdout group ended and profiles were removed from it.
- ****Holdout size****
  The percentage of profiles out of your total marketable profiles that are represented in the holdout group. This is derived from your initial holdout group setup.
- ****Marketing lift****
  The percentage lift of your marketing program compared to those in the holdout group using your account’s selected conversion metric. This shows the overall success of your marketing strategies compared to those not receiving all or most of your marketing.
- ****Win probability****
  Probability that your marketing program provides a meaningful improvement over the holdout group.

You can also click the arrows next to any of these columns to sort by names, dates, holdout sizes, marketing lift, and win probability by ascending or descending order.

By clicking on any of the global holdout names, you will be brought to an individual analytics card with data on this particular group compared to your marketing programs.
