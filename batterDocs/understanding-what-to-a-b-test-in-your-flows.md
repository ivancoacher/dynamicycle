<h1>Understanding what to A/B test in your flows</h1>

Learn about what you can test in your flows using Klaviyo's A/B testing feature.

Flows send automatically to customers, making them an instrumental part of your communication strategy. You can simply set up a flow, turn it live, and then leave it to send; however, because flows represent your brand at key touchpoints in the customer journey, it's important to test and optimize flows.

Note that you should only test one variable at a time. If you test more than one, the results may be skewed.

Apple Mail Privacy Protection (MPP), which was released with iOS15 and updates to other Apple devices, may lead to inflated open rates due to changes in how we receive open rate data.

If you are triggering flows off of opens themselves, we suggest creating a [custom report](https://help.klaviyo.com/hc/en-us/articles/4416803987739) that includes an MPP property to review these affected opens. You can also identify these opens in your individual [subscriber segments](https://help.klaviyo.com/hc/en-us/articles/4416791883163).

## Timing

To determine when your flow should send out messages, you can use a conditional split to find the optimal timing for a flow message.

1. Drag a conditional split before the time delay you want to test.
2. Configure your split to be based on a 50% random sample. This will allow you to run an A/B test on the timing of one of your messages.

   Bear in mind that if you change the weighting of the random sample to something other than 50%, that will be the percentage of people who flow down the YES path.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/40172960360475)
3. Drag a time delay to the NO branch of the flow. Set this to be the other timeframe that you would like to test.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/40172960372251)
4. Clone all of the components on the YES branch and drag the clones over to the NO branch, so that everything is identical except the timing of the message. This allows you to isolate timing as the variable that you're testing.

After you set the cloned messages live, monitor the conversion rate of the messages to determine which time delay is performing best. Then, you can test another time delay or delete the split and only keep the winning time delay.

You can repeat this process with as many messages in a flow as you would like, but remember to A/B test them one at a time so that you can isolate this as the only variable you're testing.

## Number of messages

You may want to test how the number of messages in your flow affects your conversion rate. For example, maybe you want to test adding another message to the flow. When analyzing this message, pay special attention not only to its conversion rate but also the open and click rates. If the additional message has poor open and click performance, it could be doing more harm than good for your deliverability, even if it’s producing revenue.

To test the number of messages in your flow:

1. Drag in a conditional split below the trigger.
2. Base the split on a random sample and select the weighting you would like to assign to the control branch. The test branch will be the NO branch or the remainder of people who enter the flow.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/40172960376731)

## Subject lines (email only)

Subject lines are directly tied to your open rates. To test a subject line:

1. Click on the email that you would like to test.
2. Click ****Create A/B Test**** in the details sidebar.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/40172916684827)
3. You will see sections for 2 different variations of the email. You can change the ****Subject line**** field for each variation.

## Content

Click rates, unlike subject lines, are primarily affected by the content and, for emails, the layout. You can A/B test your message content by changing the body of the email or text, but nothing else (e.g., subject lines). You can measure your results in the same way you would measure them for a subject line A/B test, but instead of looking at open rate, pay special attention to the message's click rate.

## Images and GIFs

For emails, changing the images or GIFs is part of testing the overall content, but that's not the case for your text messages. The question of whether or not to add an image or GIF is much bigger for text message marketing. A/B testing can help you decide if you should use an SMS or MMS message and for MMS messages, if it should be an image or GIF.

## Additional resources

Learn more about A/B testing:

- [A/B testing best practices](https://help.klaviyo.com/hc/en-us/articles/360045012632)
- [A/B testing flow branches](https://help.klaviyo.com/hc/en-us/articles/360049849432)
- [A/B testing an individual flow email](https://help.klaviyo.com/hc/en-us/articles/6960371049115)
