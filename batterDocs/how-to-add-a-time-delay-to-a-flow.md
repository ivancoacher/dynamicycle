<h1>How to add a time delay to a flow</h1>

## You will learn

You will learn how to add a time delay component within the flow builder which is used to create delays (or wait periods) between messages or other components in your flow series.

If components are back-to-back, without any time delays, they will all occur simultaneously. For this reason, you will likely always want to ensure you have a time delay component between consecutive emails or SMS.

A time delay must be followed by a flow action that is set to live or manual status. If a time delay is added to the end of a flow without an action following or if all following actions are set to draft status, profiles in the flow will skip the time delay and immediately exit the flow.

If you want to add a time delay before someone exits a flow, but you do not want to send out a message afterwards, you can use a non-message flow action such as an [update profile property action](https://klaviyo.zendesk.com/hc/en-us/articles/360001768432) at the end of the flow.

## Add a time delay

To add a new time delay into a flow:

1. Drag the time delay component from the sidebar and drop it where you would like to create this waiting period.
2. After you drop the time delay into your flow, configure the details in the left-hand sidebar.

![The time delay component is found in the left sidebar and can be dragged into the flow where you'd like it to be placed.](https://fast.wistia.com/embed/medias/cr10dmb46w/swatch)

Configuration options for a time delay include:

- Wait \_\_ Minutes
- Wait \_\_ Hours
- Wait \_\_ Days
- Wait \_\_ Days and delay until a specific time of day

When you choose to create a waiting period of X days, each day will be calculated as a 24-hour period. If you choose to wait X days but specify a certain time of day, however, each day will be calculated as a calendar day to avoid prolonged wait periods depending on when a recipient enters your flow. To explain this further, consider the following scenario.

Let's say you want to have a time delay set to "Wait 1 Day, until 3PM" and then send an email:

- **Person A** enters your series at 2 PM. Waiting 1 day (24 hours) would land your recipient at 2PM the next day and the email would send 1 hour later at 3 PM. The total amount of time between when they trigger the flow and when they receive the first email is 25 hours.
- **Person B** enters your series at 4 PM. Waiting 1 day (24 hours) would land your recipient at 4PM the next day. In order to send at your specified time of 3 PM, we'd need to wait another 23 hours. This means **Person B** would receive your email almost a full day later than **Person A**. What happens instead is that **Person B**will receive the email at 3 PM the following day, 23 hours after they triggered the flow.

To avoid the above problem, we'll only wait X "calendar days" instead of X "24-hour days" when your time delay includes a specific time of day. With this behavior, using the above example, **Person A** and **Person B** will both get the email at the same time.

## Delay until a specific time

You may want to control what time of day recipients receive a specific flow email or SMS in your series. This can be useful when you want to normalize the time of day people receive your messages, for instance, if you know your audience typically opens emails at a certain time.

Within the settings for a time delay component, you can choose, **Delay until a specific time of day**. If you have an SMS following this time delay, this will establish the send time for that SMS.

After choosing a time of day, you can then select a timezone. You can choose ****Recipient's Local Timezone**** in order to ensure each recipient receives your message at your preferred time, regardless of where they are located.

![When configuring a time delay, there will be an option to set the amount of time for the delay as well as the option to delay until a specific time of day.](https://klaviyo.zendesk.com/hc/article_attachments/28715962257307)

One benefit to choosing the "Wait \_\_ Days" option, without selecting a set time, is that each recipient will then receive the SMS or email at the same time they took the flow's trigger action — the time someone took the trigger action is one data point that tells you the recipient was online engaging with your business at that time, and thus it might be a time they're typically active online.

## Delay until a specific day of the week

If you only want a flow email or SMS to send on specific days of the week, you can add a time delay component before it in your series and use the **Delay until a specific day(s) of the week** option.

All days will be selected automatically. You can remove days by clicking the X next to the day name or add days by clicking on the dropdown and clicking the checkbox next to the day.

Selected days shown in the dropdown are the days of the week when the message **does**send. Unselected days are the days of the week when the message **does not** send.

For example, let's say John enters your flow on a Tuesday:

- You have a delay after the trigger to "Wait 2 Days," but delay until a Monday, Wednesday, or Friday.
- John enters the flow on a Tuesday, we wait two days, and now it's Thursday. Because you only want emails to send on Monday, Wednesday, or Friday, however, we'll delay one more day until it's Friday.
  ![Below the option to delay until a specific time of day, there is also the option to delay until a specific day of the week with buttons for each day so that multiple days can be selected.](https://klaviyo.zendesk.com/hc/article_attachments/28715968827163)

Messages are scheduled based on the timezone associated with the recipient's profile. If the profile's timezone cannot be accurately determined, your account's timezone will be used which can be found in your [account settings](https://help.klaviyo.com/hc/en-us/articles/115005232388).

When you delay until a specific day of the week, note that you will no longer see the expected number of days in any subsequent components (e.g., emails or SMS messages). For instance, if you have a time delay component that's set to wait 10 days and delay until Monday or Friday, it's not possible to determine when exactly a recipient will receive the following message; each person that is added to the flow is going to have a different number of days before they are sent the next message.

## Additional resources

Read more about [flow branching](https://help.klaviyo.com/hc/en-us/articles/115003883992-Introduction-to-Flow-Branching).

Learn more about time delays in Klaviyo:

- [About using time delays near splits](https://help.klaviyo.com/hc/en-us/articles/360050334651)
- [Understanding the timing of a flow](https://help.klaviyo.com/hc/en-us/articles/360046164352)

Find out more about [understanding how contacts move through a flow](https://help.klaviyo.com/hc/en-us/articles/360017706091-How-Contacts-Move-Through-a-Flow).
