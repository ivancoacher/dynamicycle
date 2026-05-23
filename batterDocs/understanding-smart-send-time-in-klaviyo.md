<h1>Understanding Smart Send Time in Klaviyo</h1>

## You will learn

Learn how Smart Send Time uses your business' data to find the optimal time for you to email your customers, maximizing open and click rates as well as helping you to better understand your customers.

In order to conduct the exploratory and focused tests outlined below, you must be able to send campaigns to an audience of 12,000 people or greater. These tests cannot be conducted for a campaign with a recipient list smaller than 12,000. You must also be on an email billing plan that supports sending to this many profiles.

![](https://fast.wistia.com/embed/medias/5vhljv3dvg/swatch)

## How Klaviyo's send time optimization model is different

While there are a lot of companies that have send time optimization capabilities, Klaviyo's model is different. Instead of determining your business' send time through hidden formulas, Klaviyo uses a robust testing framework to gather data about your customers to figure out when they are most likely to open your emails. For transparency, your results will always be available to you.

## When you should use Smart Send Time

While knowing the best time to send is important, it's crucial that you use this feature strategically. Because we send in a recipient's local time, avoid sending time-sensitive content such as a flash sale or an announcement about an impending deadline. Accordingly, you shouldn't do Smart Send Time testing around major holidays or dates that are important to your brand.

## How to utilize Smart Send Time

You can create a Smart Send Time test from either the campaign wizard or the Smart Send Time reporting page. You may create multiple Smart Send Time tests as well; however, Smart Send Time is only available for email. For details on how to run a test, check out [how to perform and analyze Smart Send Time tests](https://help.klaviyo.com/hc/en-us/articles/360049073691).

Klaviyo's Smart Send Time tests send based on recipient's time zones. If Klaviyo is not sure of a recipient’s time zone, the message will send based on the time zone you select at the account level.

### Exploratory send

During this phase, Klaviyo will send out an email over a 24-hour period. Customers will be randomly assigned to a time during that period. All emails will be sent in the recipient local time. For instance, if you are in Eastern Standard Time and a subscriber in Central Standard Time is assigned to receive a 10 a.m. email, they will receive it at 10 a.m. CST.

![exploratory send.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28715969706779)

If you schedule an exploratory send today, it will begin sending at the beginning of the next hour (e.g., if you schedule it for today at 2:45 p.m., the first batch will send starting at 3:00 p.m.) If you schedule an exploratory send for a future date, the first batch will send at 12:00 a.m. in your account's local timezone.

The email that you send out should be a wide-reaching, not time-sensitive email (e.g., a weekly newsletter). Additionally, consider turning off Smart Sending to ensure that the same people on your list all have an opportunity to open your emails. If you're sending out other campaigns in a similar window, consider sending the non-Smart Send Time email campaign with smart sending or on a different day.

In order to narrow down the window of time that works best, the model will need a good amount of data. Depending on how large your usual recipient count is, you may have to do this portion of Smart Send Time multiple times.

|  |  |
| --- | --- |
| ****Number of recipients**** | ****Number of exploratory****   ****sends required**** |
| <12,000 | Not eligible |
| 12,000 - 17,999 | 4-5 |
| 18,000 - 23,999 | 3-4 |
| 24,000 - 47,999 | 2-3 |
| 48,000 - 71,999 | 1-2 |
| >72,000 | 1 |

If you run an exploratory send but the results are skewed (perhaps due to a holiday or simple bad timing), you can request that your historical Smart Send Time data be deleted.

### Focused send

After the exploratory send phase, Klaviyo determines a focused send time (i.e., the time with the highest engagement).

During the second phase, Klaviyo continues to validate the time determined from the results of the exploratory send and refines based on any changes to customer behavior.

![focused send.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28715963121307)

With a focused send, 1 email sends at the optimal send time and 2 emails send in a 2-hour window from the optimal send time; all emails also send in the recipient's local time.

For instance, if the model thinks that 7 a.m. is your optimal send time, your recipients are split into 3 groups. Group A receives an email at 5 a.m., group B at 7 a.m., and group C at 9 a.m. in the recipient's local time.

### Optimal send

Once the optimal send time is discovered, you can begin using this to send campaigns. Optimal send time can be used for audiences of any size.

With this option selected, Klaviyo sends your campaign at the specific time in the recipient's local time zone.

Thus, the campaign will send over the course of up to 24 hours. Note that the resulting performance does not affect your optimal send time, as the emails only send at 1 specific time in each time zone. Since recipients all get the message at, for example, 10:00 p.m., there are no other times for Klaviyo to compare the campaign's performance with. Therefore, Klaviyo doesn't learn anything to update the Smart Send Time model or the optimal send time.

![optimal time.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28715969712155)

## Smart Send Time reporting

Smart Send Time reporting allows you to view an experiment’s details, such as what phase it is in and the last time a campaign was sent. You can also see an overview of the results. The graph shows the open rate per hour for all campaigns associated with an experiment.

![A Smart Send Time report's opens per hour chart](https://klaviyo.zendesk.com/hc/article_attachments/28715969702939)

You can also view an individual’s campaign performance and see how it performs over the course of the test.

For more information, read the guide on [understanding Smart Send Time results](https://help.klaviyo.com/hc/en-us/articles/360041411132).

## Smart Send Time FAQs

#### Why don't I see the option to use Smart Send Time?

Smart Send Time exploratory and focused sends are only available for campaigns with 12,000+ recipients.

#### I've been sending to 12,000 recipients and have done the exploratory send 5 times, but still do not see the option for the focused send. Why is that?

For each campaign sent, Klaviyo automatically tracks conversions or a recipient opening an email and then taking another action (such as placing an order) within the conversion period. The send time model waits until after your conversion period before recording the results that will impact your ideal send time. By default, the conversion period is 5 days, but you can change this window in your account settings. For more information, check out our article on [conversion tracking](https://help.klaviyo.com/hc/en-us/articles/115005248128).

#### Do I have to use the same list every time I do an exploratory send?

No, you can use different lists. If you're trying to find an optimal send time for a particular group (i.e. just your US customers), you wouldn't want to add in other groups of people, as they would skew the results. However, if you're trying to understand the optimal send time for your entire customer base, you can include all of your lists and segments.

#### Can I send more than one email using Smart Send Time out at a time?

Yes, you can send out as many as you want. You should still send in accordance with your normal sending cadence. For example, if you normally send emails once a week, you won't want to increase your sending cadence just to have the model work faster. This will skew your results.

#### Can I A/B test emails while using Smart Send Time?

You should only test one variable at a time. Accordingly, you cannot A/B test Smart Send Time emails.

#### How many focused sends do I have to send out before I know my true optimal send time?

After the model has enough data to allow you to send out focused emails, it is certain that the time suggested is your optimal send time. The focused send is used to continue to validate and refine the time should your customer behavior change.

#### How is Smart Send Time different than Smart Sending?

Smart Send Time is a series of tests that allow you to know the optimal time to send to your customers. Smart Sending keeps you from bombarding your customers with too many emails over a short period of time.

#### Why was a campaign unable to be used to update send time?

As part of the analysis process, Klaviyo checks that each campaign sent with Smart Send Time has valid data. For instance, if a focused send is sent to a segment containing only two recipients at time of send, only two variations will be sent instead of three, and the campaign will be removed from the analysis. This ensures outliers are excluded from skewing Smart Send Time. No action is required and Klaviyo will automatically include subsequent valid campaigns in the analysis so you can continue sending with Smart Send Time.

Common reasons campaigns maybe excluded include: uneven recipient counts due to smart sending, analytics delays, very small recipient segments at time of sending.
