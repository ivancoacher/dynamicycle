<h1>How to test and preview flow messages</h1>

## You will learn

Learn how to test your flow after you have configured the trigger, filters, and messages. You may want to test the first few messages to make sure they look exactly right, especially if the email or SMS contains dynamic variables. There are two types of tests you can run:

- Preview individual flow emails or SMS messages to verify that the content is correct using built-in tools that allow you to preview with real data from your account.
- Test your flow and flow filter logic to ensure messages are only sent to the people you want to receive them. You can accomplish this using the [flow preview tool](https://help.klaviyo.com/hc/en-us/articles/360028374111) to ensure that people are being correctly evaluated and move through the flow as expected.

## Test and preview email content

Testing and previewing email content can be quickly and easily done while you're editing each email.

1. While editing a flow message, click ****Preview & test**** in the upper right.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/33627696238619)
2. Select the event and person you want to use to see a preview directly in Klaviyo, or click ****Send test**** to send a preview to your own inbox.
3. Optionally, select ****Inbox testing**** to preview your email in various inboxes. Learn more about inbox testing.

## Test and preview SMS messages

Like emails, testing and previewing SMS messages can be done quickly as you’re editing your message.

1. In a flow, click on the SMS message you want to test.
2. Click ****Edit**** on the right-hand side.

In the SMS editor, there are three important areas:

- Left: A space to configure your SMS content
- Center: A preview of how this message will look upon delivery
- Upper-right: A ****Preview & test**** button allowing you to choose data to preview with

![](https://klaviyo.zendesk.com/hc/article_attachments/33627732960027)

### Content configuration

The message count is based on the number of characters in a message. However, multiple messages will appear as a single message unless the recipient's phone or carrier does not support concatenated messages. This is because the underlying technology will send it as multiple messages, but your carrier and phone will reformat the SMS so that it appears as only one.

Use the icons above the message content field to attach an image or GIF (making the message an [MMS](https://help.klaviyo.com/hc/en-us/articles/360041075091)), add emoji, or select personalization tags. Use the star icon to have AI draft content for you.

![](https://klaviyo.zendesk.com/hc/article_attachments/33627732965659)

The ****Compliance**** tab offers message add-on options, including opt-out language, which is [required by some countries](https://help.klaviyo.com/hc/en-us/sections/360000775792) and carriers. For US recipients, you can also add an organization prefix to the beginning of the message. As for Canadian recipients, you can add an info link with your contact information, which is required under Canadian law.

![](https://klaviyo.zendesk.com/hc/article_attachments/33627696250395)

### The mobile preview

When creating and configuring your message, you can see what it will look like once it’s sent to a mobile device.

The organization prefix comes at the beginning of the message, while opt-out language and the info link are added to the end of the message.

![](https://klaviyo.zendesk.com/hc/article_attachments/33627732974491)

### The previewing tab

In the upper right-hand corner, click ****Preview & test**** to see the 10 most recent, qualified profiles or events that you can navigate between. For metric-triggered flows, this card will show the events for the flow’s trigger (i.e., for an abandoned cart flow, the 10 most recent **Started Checkout** events will show here). For date property flows, this screen will default to profiles with that date property set. If no one meets the qualifications for a flow, the tab will show a message that indicates there are no available profiles.

As for list- and segment-triggered flows, the tab will show those added to the specified list or segment, but you can search for any profile in your account. You can search for someone by name, phone number, or email address. You can preview the message with any profile, meaning you can preview the message as someone even if that person is not in the list or segment that triggers the flow.

For metric-triggered flows, open the ****All properties**** menu for information related to the event that triggered the flow, including the event variables. Hover over any line of data and click to copy the variables to your clipboard.

![](https://klaviyo.zendesk.com/hc/article_attachments/33627732985115)

With list-, segment-, or date property-triggered flows, this menu will show details about the profile, including their first and last name, email, location/timezone, and any profile or custom properties. Open the ****All properties**** menu to view them. All of the profile properties will appear, even if they are empty on a certain profile, while the custom properties section only displays the custom properties that are applied to that profile. To use any variable for these properties in your text message, simply click to copy the property.

![](https://klaviyo.zendesk.com/hc/article_attachments/33627696262683)

### Send test

Additionally, you can send a test SMS to yourself to ensure your message looks as expected. The test message will show any images/GIFs, personalization tags, as well as how the link looks when shortened.

1. From the editor, select ****Preview & test**** at the very top of the screen.
2. Select a country code and type in a phone number.
3. Optionally, select the option **Save phone number as your default test recipient** if you plan to use that number for testing in the future.
4. Click ****Send test****. You will not be charged to send SMS messages. However, the links don't appear shortened for test SMS messages.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/33627696267035)

If the option to **Send** is grayed out, make sure you have a verified toll-free number. A preview send uses your account's associated number, and thus still requires verification. See our article on [understanding toll-free number verification](https://help.klaviyo.com/hc/en-us/articles/4415873897499) for more information. Otherwise, check that you set up SMS properly. Head to the course on [getting started with SMS](https://academy.klaviyo.com/getting-started-with-sms/1411601) to make sure.

## Test your flow logic

If your flow has complex filters, you may want to review the first few messages before all enabling your flows to start sending automatically. To test your flow logic, use the [trigger preview setup tool](https://help.klaviyo.com/hc/en-us/articles/360028374111-Preview-a-Flow-Trigger-Setup). This will help you understand how contacts are entering the flow and how the filters are being evaluated.

If you would like to test a specific message, you can use another method. First, change the message you'd like to test to ****Manual****mode. Flow messages in manual mode will be scheduled in real-time as if the message were live. However, instead of being sent automatically, the message will be marked for you to manually review.

After you've set your message's status to ****Manual****, you can watch your flow for a set period of time to observe who is queued up in the ****Needs Review**** tab**.** When someone first enters a flow, they will be placed in ****Waiting**** until the scheduled send time. At send time, contacts will move from ****Waiting**** to ****Needs Review**** if they pass your flow's filters.

When messages accumulate in ****Needs Review****, you will have an option to manually send individual messages, manually send all messages, or cancel one or all messages.

![](https://klaviyo.zendesk.com/hc/article_attachments/33627732998427)

## Best practices for testing flow logic

There are a couple best practices recommended to ensure your flow behaves as expected:

- If the flow you've created is based on a built-in Klaviyo idea or it's very simple and doesn't need flow filters, for example, a welcome series when someone subscribes to your newsletter, you can set all messages in the flow to live and skip testing the flow logic.
- If you set a flow to ****Manual****and notice that nobody is entering your flow, it likely means your filters are too restrictive or the logic is keeping everyone out. Try creating a segment that mirrors your flow's setup and see if any contacts populate.

## Additional resources

Find more articles on testing flows and their messages:

- [How to manually send to flow recipients](https://help.klaviyo.com/hc/en-us/articles/115002779331)
- [How to preview a flow trigger setup](https://help.klaviyo.com/hc/en-us/articles/360028374111)
- [How to use the preview panel for message personalization](https://klaviyo.zendesk.com/hc/en-us/articles/27843522951707)
