---
id: 6456860853275
title: "MMS throughput in the US, Canada, and Australia"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/6456860853275-MMS-throughput-in-the-US-Canada-and-Australia"
section: "SMS deliverability best practices"
category: "SMS"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-21T13:55:04Z"
language: en
---

## You will learn

Learn about throughput for MMS and strategies for getting the most out of this channel in the United States, Canada, and Australia.

## Before you begin

Please note that MMS is only available for a few countries and number types:

- United States: toll-free numbers and short codes
- Canada: toll-free numbers
- Australia: long codes

MMS is not available for any other number type or country.

## What is throughput?

Throughput is the sending speed for messages. Think of it as your speed driving down a road. The higher the speed, the faster you go, and the faster your messages are delivered.

When you’re driving, it’s not just about how fast your car can go. A few things can get in the way of moving at top speed. Continuing with the driving analogy, the two biggest factors that impact your throughput speed are:

- The road itself (i.e., the systems wireless carriers use to deliver messages)
- How many other people are using the road (i.e., how busy those systems are)

For instance, your speed will be very different on a one-lane road full of traffic versus an open highway.

### SMS vs. MMS throughput

Does throughput work the same for both SMS and MMS? The short answer is no.

Wireless networks have near-unlimited throughput for SMS, but this is not true for MMS. If SMS throughput is an interstate highway with 10 lanes each way, MMS throughput is a 2-lane residential road.

****Why is throughput different for MMS and SMS?****

The reason for this difference comes down to how wireless networks were originally built.

They started as a way for individuals to send simple, plain-text messages to their friends and family.

Years later, the networks adapted their systems to allow people to attach images and GIFs to their text messages. However, the networks didn’t build their infrastructure with large-scale communications in mind. Thus, the networks’ capacity for messages with images or GIFs, known as MMS messages, is much smaller than for messages without any media (i.e., SMS messages).

## How throughput for MMS works

Today, marketers are sending MMS to thousands of people. However, the networks simply can’t handle too many of these kinds of messages at once.

There’s already a small queue for MMS messages. When a lot of people want to send at the same time, it takes longer for the messages to be delivered.

## Canada’s hard limit on MMS

Canada allows very few MMS messages per minute on toll-free numbers, which applies to all carriers.

Due to this, we suggest limiting the number of MMS campaigns to 14,000 recipients or fewer when sending to Canada.

## Best practices for MMS

### Break large campaigns into smaller campaigns

Break up any MMS campaigns that are being sent to:

- 14,400 people in Canada
- 30,000 people in the United States (if using a toll-free number)
- 30,000 people in Australia

  An MMS campaign can time out after around 4 hours, and if someone didn’t get the message in that timeframe, they will be skipped.

  Note that all messages count toward these numbers, including flows, conversations, and other campaigns.

  Say you want to divide up an MMS campaign going to 10,000 recipients. Consider segmenting your group to not only break up the send, but also make it more personalized:
- Send your VIPs the MMS at 10 a.m. on day 1
- Send customers who bought from you in the last 20 days receive the MMS at 5 p.m. on day 1
- Send remaining subscribers the MMS at 10 a.m. on day 2

You may need to adjust the criteria based on how many people are in these groups, spacing out the sends depending on your segment size or creating additional groups, if needed.

### Don’t send MMS during busy times or holidays with a toll-free number

Except with US short codes, we don't recommend sending any MMS during holidays or busy shopping times.

During these times (e.g., Black Friday/Cyber Monday), many companies will want to send MMS to their customers. Businesses also tend to send messages to more recipients than they usually do.

These 2 things means that throughput is hard to come by. Carriers will often fail to deliver MMS messages during busy times. This is particularly true for toll-free numbers (US and Canada) and long codes (Australia).

As an example, during normal times, the limit for MMS campaigns to US recipients is ~30,000; however, during Black Friday/Cyber Monday, the limit will be closer to 25,000.

### Use MMS in flows

Rather than sending images and GIFs via campaigns, try using MMS in your flows.

Flows are triggered by a customer’s actions, so they send to individuals, one at a time. This is a huge plus for your MMS deliverability. Fewer messages trying to go out at once means that carriers can handle the sends more easily.

Overall, flows are better at delivering MMS than campaigns, although they may still experience issues during busy sending times in the year.

### Use MMS sparingly

SMS tends to perform as well or better than MMS.

We recommend testing how your audience responds to MMS to make sure it's worth the extra credits. For instance, you can test showing a new product in a text message or a GIF that shows items on sale.

Alternatively, you may want to reserve MMS for small, specific groups of people. If you have a large campaign, think about who you want to make the biggest impression on. For instance, you can use MMS for only your VIPs or to convert site visitors into new customers. Once you decide on the group you want to send an MMS to, send everyone else a similar SMS, leaving off the image or GIF.

### Use a short code (US only)

If MMS is important to your business model, consider purchasing a short code.

Carriers prioritize MMS from short codes. Thus, a business with a short code may have an easier time sending this type of message than someone with any other number type.

MMS is not available on short codes in Canada, so this option will only help you send to US subscribers.