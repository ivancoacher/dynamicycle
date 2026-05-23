<h1>Getting started with the subscriber growth report</h1>

## You will learn

Learn how to use the subscriber growth report to better understand how you are acquiring and losing subscribers over time per marketing channel. Additionally, understand which of your specific forms were the most effective in gathering subscribers as well as why profiles are being suppressed.

## Before you begin

Note that:

- Mobile push is not supported on this report.
- Suppressions are email-only, but there are reasons that a profile may be excluded from receiving SMS marketing.
- If you are newer to Klaviyo and have not started collecting consent on any channel yet, your report will be empty. Once you start collecting consent and engaging with your subscribers, you can revisit building this report.
- The subscriber growth report may have slightly different numbers than the [email deliverability dashboard](https://help.klaviyo.com/hc/en-us/articles/18378819907995). This is because the subscriber growth report only reports on someone's status if they give or remove explicit consent for receiving e-mail marketing (i.e., not if a profile was created because of a purchase or for some other reason and the profile was never opted-in for messaging). For example, customer A browses a site, makes a purchase, never explicitly agrees to receive marketing emails, but a profile is still created. Meanwhile, customer B does the same actions but explicitly consents to receive emails. This means that a subscribe event will count for customer B but not customer A, and the same thing is also true should they unsubscribe. In other words, all subscribe or unsubscribe events in the subscriber growth report are only counted for those that who have explicitly consented.

## Accessing the report

You have 2 options for accessing the subscriber growth report, either through the **Profiles** section or through the **Subscriber Growth** card on an overview dashboard. You can find both directions below.

### Via the **Profiles** tab

1. Navigate to ****Audience >********Profiles****.
2. At the top of the page, click ****View Subscriber Growth****.

![](https://klaviyo.zendesk.com/hc/article_attachments/39648348762267)

### Via the **Overview dashboard** tab

1. Navigate to ****Analytics >********Dashboards****.
2. Open an existing overview dashboard from the list, or create a new one by selecting ****Create Dashboard****.
3. Look for the S**ubscriber Growth** card. If this is not already on your dashboard, click ****Add card**** to find and add it from the library.
4. On the card, click ****View full report****.

![](https://klaviyo.zendesk.com/hc/article_attachments/28720903515547)

## Customizing your report

At the top of your subscriber growth report, you have the option to customize how your data displays as well as the time range of the data it pulls from.

### Date range

By default, the **Date range** is 7 days.

To change this:

1. Open the dropdown.
2. Choose one of the following options:
   1. **Week-to-date**
   2. **Month-to-date**
   3. **Last 7 Days**
   4. **Last 30 Days**
   5. **Custom** (note that you can pull data from 12/13/23 on)

### Data viewing or aggregation

By default, the **View by** aggregation shows data by daily increments. To make adjustments:

1. Open the dropdown.
2. Choose one of the following options:
   1. **Daily**
   2. **Weekly**
   3. **Monthly** (note that this is not viewable when your time range is set to 7 days)

### Refreshing the data

At the top, the report notes the timestamp of when it was last updated.

The report needs to be refreshed manually. By refreshing the report, you will refresh it for all applicable users in your account.

To refresh the report with the latest data:
1. Click on the ****circular arrows icon**** in the upper right.

![refresh icon.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28720903519515)

## Reviewing your total subscribers size by channel

On the **Overview** page, you will see the total subscribers per channel within your report's time range. If you are multi-channel, you will see all your channels (with the exception of mobile push). If you are only using a single-channel, you will just see the one reflected.

![](https://klaviyo.zendesk.com/hc/article_attachments/39648318277659)

## Reviewing the channel subscribers cards

Th**e Email subscribers** and **Text messaging subscribers** cards provides a snapshot view of your subscriber performance over your chosen time range, including:

The text messaging channel can be further broken down into marketing and transactional subscribers using the **Consent type** dropdown on the **Text messaging** tab.

- Overall subscriber growth
- Total number of new subscribers
- Total number of excluded subscribers and reasons for exclusion
- Sources of opt-ins, along with the total number of subscribers per source
- Top opt-in and exclusion sources

If your account is only a single marketing channel (i.e., email), you will only see that channel reflected.

![email subscribers- main card, redo.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28720903522843)

In addition, at the top of this card, there will be 3 tabs (**Growth**, **Opt-in sources**, and **Exclusion reasons**) breaking out this data into more detailed views.

A suppressed profile cannot receive marketing messages, even if they have provided consent and indicated they want to receive emails. Learn more about suppressed profiles in Klaviyo.

### **Growth** tab

The left line chart on the **Growth** tab visualizes your subscriber growth across your selected time range, aggregated view, and channel. Here, you can see at each point in time how many subscribers you have.

![email susbcribers growth left, redo.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28720903526427)

You can also review the total number of subscribers per channel in this time period along with the percentage change (i.e., **Over the last period**), as shown below.

![email susbcribers total number only.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28720898223771)

By hovering over any points in the line chart, you can also see the total number of subscribers for that point in time.

![](https://klaviyo.zendesk.com/hc/article_attachments/28720898227483)

The right bar chart on the **Growth** tab visualizes the number of subscribed (green bar) and excluded members (red bar) across your selected time range, aggregated view, and channel. Here, you can see at each point in time how many subscribers you are adding or losing.

![](https://klaviyo.zendesk.com/hc/article_attachments/28720898230811)

By hovering over any points in the line chart, you can also see the total number of added and excluded subscribers for that point in time.

![](https://klaviyo.zendesk.com/hc/article_attachments/28720898235547)

### **Opt-in sources** tab

The **Opt-in sources** tab provides information on where and how subscribers are joining your lists. You can also see details around which of these sources are currently performing the best in order to optimize the subscriber sign-up journey.

![](https://klaviyo.zendesk.com/hc/article_attachments/28720903544987)

#### Opt-in sources details

You may note the following opt-in reasons in each of the charts, including:

Email-specific reasons

- ******Klaviyo form******
  A profile subscribed via a Klaviyo-specific form.
- ******Custom hosted page******
  A profile subscribed via a [custom hosted page](https://help.klaviyo.com/hc/en-us/articles/360057676272) in Klaviyo.
- ******Subscribe page******
  A profile subscribed via a [standard subscribe page](https://help.klaviyo.com/hc/en-us/articles/115005251988) in Klaviyo.
- ******Shopify integration******
  When a profile’s consent is passed from Shopify to Klaviyo.
- ******Magento 2 integration******
  When a profile’s consent is passed from Magento 2 to Klaviyo.
- ******BigCommerce integration******
  When a profile’s consent is passed from BigCommerce to Klaviyo.
- ******Facebook integration******
  When a profile consent is passed from Facebook to Klaviyo.
- ******WooCommerce integration******
  When a profile’s consent is passed from Woo Commerce to Klaviyo.
- ******NetSuite integration******
  When a profile’s consent is passed from Netsuite to Klaviyo.
- ******Wix integration******
  When a profile’s consent is passed from Wix to Klaviyo.
- ******Square integration******
  When a profile’s consent is passed from Square to Klaviyo.
- ******Back in stock email******
  When a profile signs up to receive notifications for when a product is back in stock, a "Subscribed to Back in Stock" event will be tracked on their Klaviyo profile.
- ******Profile manual subscribe******
  Consent was manually added to a profile record in Klaviyo.
- ******Bulk manual subscribe******
  When profile consent has been bulk added within Klaviyo via a list upload or import.
- ******API subscribe******
  When a list of profiles' consent is passed via API.
- ******Klaviyo account creation******
  When you create a new Klaviyo account, you are subscribed to Klaviyo's own marketing by default.

  Note that you may see a discrepancy between the count the count of new subscribers in the **Growth** tab and the count of profiles in the **Opt-in sources** tab. This is because if someone unsubscribes in the same day after subscribing, they will not be considered in the new subscribers count.

  Text messaging-specific reasons

  SMS consent is stored on a per phone number basis. This means that if a new profile is created with an already consented number, the consent information of the original profile will apply to the new profile. Learn more about [SMS consent collection](https://help.klaviyo.com/hc/en-us/articles/360035056972).
- ******SMS checkout******
  When a profile provides consent to SMS at checkout.
- ******SMS form******
  When a profile provides consent to SMS via a Klaviyo form.
- ******SMS inbound message******
  When a profile subscribes to SMS via an opt-in keyword such as "Join."
- ******SMS list upload******
  When a list of profiles' SMS consent is updated via a manual list upload.
- ******SMS message******
  When consent is provided by a profile via a SMS message.
- ******SMS API******
  When a list of profiles' SMS consent is passed via API.
- ******Preference page******
  A profile subscribed via a preference page.
- ******Manual subscription******
  When consent is manually added to a profile in Klaviyo.
- ******Shopify integration******
  When a profile’s consent is passed from Shopify to Klaviyo.
- ******Facebook integration******
  When a profile’s consent is passed from Facebook to Klaviyo.
- ******SFTP******
  When a list of profiles and their consent has been passed via a SFTP file import into Klaviyo.

The descending list on the left provides the total number of subscribers joining via each specific form (either Klaviyo or custom form), and if these subscription rates are trending up (green arrow) or down (red arrow). Here, you can spot which forms are leading to the most sign-ups and which may need to be adjusted or even removed because of poor performance.

Klaviyo forms will have a link and send you to the relevant forms page.

![](https://klaviyo.zendesk.com/hc/article_attachments/28720898242075)

The bar chart on the right displays the top 5 sources of subscriber sign-ups during the selected time period. You can use this chart to review which sources have been recently successful in driving subscription rates.

![](https://klaviyo.zendesk.com/hc/article_attachments/28720898246171)

Additionally, by hovering over any of these bars, you can review the total number of subscribers that signed up via that specific source.

![](https://klaviyo.zendesk.com/hc/article_attachments/28720898248859)

### Exclusion reasons tab

The **Exclusion reasons** tab provides details about why your subscribers are getting excluded from receiving marketing. This tab is helpful in identifying if there are deliverability or list cleanliness issues, or even potential issues related to the types and frequency of the messages you send.

A completely suppressed profile cannot receive marketing messages, even if they have provided consent and indicated they want to receive emails. Learn more about [suppressed profiles](https://help.klaviyo.com/hc/en-us/articles/115005246108) in Klaviyo.

![](https://klaviyo.zendesk.com/hc/article_attachments/28720898252059)

#### Exclusion reasons details

You may note the following exclusion reasons in each of the charts, including:

Email-specific reasons

- ******Bounce******
  Occurs when an email cannot be delivered due to a permanent reason. This can be caused by a variety of reasons, including a misspelled email address or a deliberate block by the email server.
- ******Spam complaint******
  After a profile marks one or more of your emails as spam, they will be unreachable. When there's a spam complaint, the profile shows an "unsubscribed" consent status, rather than being suppressed.
- ******Invalid email address******
  Email address is not valid and cannot be emailed.
- ******Mailbox provider******
  When a profile directly unsubscribes via a mailbox provider.
- ******Email link******
  When a profile unsubscribes via the direct link in the footer of the email.
- ******Manual suppression******
  When a profile is manually suppressed via the profile record in Klaviyo.
- ******Suppressions removed******
  Suppressions have been removed across profiles within Klaviyo. Note that lifting a suppression on it’s own doesn’t mean a profile can receive email marketing. The profile has to have been subscribed prior to getting suppressed.
- ******Unsubscribe******
  A profile is no longer interested in receiving your email marketing and has explicitly revoked their consent. Once unsubscribed, the profile can no longer receive emails.
- ******Unsubscribe page******
  When a profile opts out of marketing via a Klaviyo unsubscribe page.
- ******Klaviyo custom hosted page******
  When a profile opts out of marketing via a custom hosted page in Klaviyo.
- ******Other******
  Consent status is missing and it cannot be determined how a profile subscribed or unsubscribed.
- ******Square integration******
  When a profile’s consent is passed from Square to Klaviyo.
- ******Campaign monitor integration******
  When a profile’s consent is passed from Campaign Monitor to Klaviyo.
- ******Exact Target integration******
  When a profile’s consent is passed from Exact Target to Klaviyo.
- ******Constant Contact integration******
  When a profile’s consent is passed from Constant Contact to Klaviyo.
- ******Mad Mimi integration******
  When a profile’s consent is passed from Mad Mimi to Klaviyo.
- ******API unsubscribe******
  When a profile’s consent is passed via API.

  Text messaging-specific reasons
- ******Invalid number******
  When a phone number is currently not a valid or cannot accept text messages (such as a landline).
- ******Landline detected******
  If anyone adds a landline number to a sign-up form or you try to import a landline number, Klaviyo will automatically remove consent.
- ******Message blocked******
  This usually only applies to toll-free numbers and generally occurs after a profile opted out using "STOP," and then opted in without texting "START" or "UNSTOP." They are then blocked by wireless carriers and unsubscribed in Klaviyo. In this case, Klaviyo receives this error from the carriers, and will remove SMS consent from that profile.
- ******Carrier deactivation******
  Consent has been removed on a profile because a wireless carrier informed Klaviyo that the profile changed numbers or switched providers. Note that as of September 2021, once a day, Klaviyo will automatically remove consent for any profile who was either removed from their original carrier’s list or has a new number.
- ******Age-related data missing******
  Age or date of birth data information is missing, so the profile cannot receive [SHAFT content](https://help.klaviyo.com/hc/en-us/articles/4408311712667#h_01HA4R92DZQCAHT4VMMDY19SGM) and thus SMS consent is revoked.
- ******Profile underage******
  Consent is revoked on a profile because their age is below minimum for receiving [SHAFT content](https://help.klaviyo.com/hc/en-us/articles/4408311712667#h_01HA4R92DZQCAHT4VMMDY19SGM).
- ******Known litigator******
  Profile was a known litigator and SMS consent was removed.
- ******SMS bulk manual removal******
  After a list of profiles has their consent removed via manual bulk suppression in Klaviyo.
- ******Bulk manual suppression******
  After a list of profiles has their consent removed via manual bulk suppression in Klaviyo. Note that this instigated via a request to Klaviyo to complete this action.

The descending list on the left provides the total number of suppressions per reason, and if these suppression rates are trending up (green arrow) or down (red arrow). Here, you can spot which things are leading to the most suppressed profiles and consider how to potentially resolve these.

![](https://klaviyo.zendesk.com/hc/article_attachments/28720903560347)

The bar chart on the right displays the top 5 sources of suppressions during the selected time period. You can use this chart to review which sources have been recently driving suppression rates.

![](https://klaviyo.zendesk.com/hc/article_attachments/28720898260251)

Additionally, by hovering over any of these bars, you can review the total number of subscribers that were suppressed via that specific source.

![](https://klaviyo.zendesk.com/hc/article_attachments/28720898262939)

## Exporting the report

After you are done customizing and reviewing your report, you also have the option to download the raw data as a CSV file. Note that any downloads will not include any of the chart or list visualizations.

To download your report:

1. Click ****Export to CSV****.
2. Choose either option:
   a. **Export growth over time** (this download includes all the subscriber totals per channel as well as additions and suppressions per specific channel).
   b. **Export sources & suppressions** (this download only includes the raw reasons for suppressions per channel).
3. Review your downloads folder or location and find the applicable file.

## Troubleshooting report and card issues

### Report loading issues

If your report is continuing to build, you will see the message “Working on your report,” shown below. Note that depending on your connection, the report should load completely within a few seconds or under. Refresh or retry loading your report if you are continuing to have issues.

![](https://klaviyo.zendesk.com/hc/article_attachments/28720903565979)

If your report cannot be built, you will see a message noting “There is no data yet.” This may be because you are a newer Klaviyo account and have not started collecting consent on any channel yet. Once you start collecting consent and engaging with your subscribers, you can revisit building this report.

![](https://klaviyo.zendesk.com/hc/article_attachments/28720903570075)

Additionally, you may see this message If there is no channel-specific subscription activity during the time period you selected. Consider adjusting your timeframe to see if the report has data and can load.

If there is a larger issue with your report or Klaviyo’s infrastructure is momentarily unreachable, you may see an error message noting “Something went wrong.” It is suggested to retry or refresh the page and attempt to reload the report.

![](https://klaviyo.zendesk.com/hc/article_attachments/28720903572251)

### Card-loading issues

If one of your channels does not have sufficient activity during the time period you selected, you may see an error like below. Consider adjusting your timeframe to see if the report has data and can load. Additionally, there may have been an issue with fetching that specific channel’s data at that point in time, so it’s advised to refresh and retry to load the report.

![](https://klaviyo.zendesk.com/hc/article_attachments/28720903575835)

If there is a larger issue with a particular channel’s data or Klaviyo’s infrastructure is momentarily unreachable, you may see an error message noting “Something went wrong.” It is suggested to retry or refresh the page and attempt to reload the report.

![](https://klaviyo.zendesk.com/hc/article_attachments/28720903578651)
