<h1>Understanding how segments update</h1>

## You will learn

Learn how segments (i.e., dynamic groups of profiles in Klaviyo) update. Most segments update in close to real time, and profiles move in and out of segments based on whether or not their interactions with your brand match the conditions you set. Once you create a segment, it pulls members from [all people in your account](https://help.klaviyo.com/hc/en-us/articles/115005246968) based on the definition you establish.

While building your segment, you only have to set the conditions once. After that, the segment will continually add and remove profiles based on the criteria you’ve set.

## Real-time segmentation updates

Segmentation requests are processed as close to real-time as possible. This means your segment updates shortly after a customer takes an action that qualifies them based on the definition you created (e.g., placing an order or opening an email). In some cases, a high volume of segmentation requests across our customer base can cause delays.

- If you manually update a segment, it can take up to 15 minutes to process
- If you are monitoring a segment, updates can take up to an hour

If you update segments and see delays that go beyond these time windows, [check Klaviyo’s status page](https://status.klaviyo.com/) or get support.

## Segments with relative time conditions

There is one notable exception to the above real-time processing; segments that rely on relative time conditions. For instance, “in the last 30 days” is relative since the timeframe constantly changes, whereas “before January 1, 2025” is not.

If a profile takes an action that causes them to qualify for, or no longer qualify for, a segment with relative time conditions, they are added or removed immediately. Profiles that qualify for a segment by taking an action at a specific time in the past, or those who no longer qualify for a segment based on relative time conditions, are added or removed once every 24 hours.

For example, if you have a segment containing profiles that have made at least one purchase in the last 30 days, anyone who makes a purchase will be added right away. If a profile doesn’t purchase again within 30 days, they will be removed from the segment on day 31. Because there's no event triggered by not purchasing, profiles that no longer qualify for the segment will be removed once per day.

![Segment of profiles that have purchased in the last 30 days](https://klaviyo.zendesk.com/hc/article_attachments/40167936832923)

In addition, a segment of people who purchased at least once between 30 and 60 days ago can't always be computed from a purchase event in real-time. This segment will add new profiles and remove old ones once every 24 hours.

![Segment of profiles that have purchased between 30 and 60 days ago](https://klaviyo.zendesk.com/hc/article_attachments/40167946243611)

## How to manually update a segment

To manually update a segment, select the segment and click ****Edit definition > Update segment****.

Note that manually updated segments don’t allow users to enter segment-triggered flows. For more information, head to our article on [creating a segment-triggered flow](https://help.klaviyo.com/hc/en-us/articles/360003040052#how-a-segment-triggered-flow-works2).

![Button to manually update a segment](https://klaviyo.zendesk.com/hc/article_attachments/40167936840475)

## Additional resources

- [Getting started with segments](https://help.klaviyo.com/hc/en-us/articles/115005237908)
- [AND vs. OR guide](https://help.klaviyo.com/hc/en-us/articles/360036534631)
- [How to create an engaged segment](https://help.klaviyo.com/hc/en-us/articles/115000200072)
- [Segmenting with dates reference](https://help.klaviyo.com/hc/en-us/articles/4403222359451)
