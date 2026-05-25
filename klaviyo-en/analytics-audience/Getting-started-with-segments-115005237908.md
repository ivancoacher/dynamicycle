---
id: "115005237908"
title: "Getting started with segments"
source_url: "https://help.klaviyo.com/hc/en-us/articles/115005237908-Getting-started-with-segments"
section: "Build and use segments"
category: "Audience"
category_slug: "analytics-audience"
klaviyo_updated: "2026-04-21T13:54:22Z"
language: "en"
---
## You will learn

Learn how to create and use segments in Klaviyo, which are a powerful tool for understanding your audience and sending targeted messages.

Ready to build more custom segments? Head to [Understanding segment conditions](https://klaviyo.zendesk.com/hc/en-us/articles/115005062847) to learn how.

## About segments

Unlike traditional subscriber lists, segments are groupings of contacts defined by a set of conditions. Lists are static, meaning they grow as people subscribe or are manually added.

Segments, on the other hand, are dynamic, meaning they grow as people meet the segments' conditions and shrink as people no longer meet them. Moreover, segments update in close to real time. Learn more about [how segments update](https://help.klaviyo.com/hc/en-us/articles/115005233488).

Highly segmented campaigns return more than 3 times the revenue per recipient as unsegmented campaigns. Some examples of how you can use segments to identify different audiences include:

- Customers who purchase a new product, so you can watch the segment grow after launch
- Inactive subscribers who have been on your list for at least 6 months but have never opened or clicked an email
- VIP customers, which includes everyone who has purchased at least X number of times before or have spent over a certain amount of money
- Customers with a high predicted customer lifetime value (CLV) who are likely going to be future VIPs

When you build a segment with a certain set of conditions, it will pull from all of the contacts in your account. This means that segments don't necessarily have opt-in criteria in order for people to be added, which is important to keep in mind when you're planning on emailing a particular segment.

## How to create a segment

1. Navigate to ****Audience >**** ****Lists & segments**** in your account.
2. Click ****Create New**** in the upper right corner.
3. Select****Create segment****.
4. Use the segment builder to add conditions and specify who should be included in your segment.
5. Once you are satisfied with the definition you create, click ****Create segment****.

We dive deeper into segment conditions in the next section.

Depending on the size of your segment, it may take a while to populate. If you're planning on sending a campaign to a segment, please allow time for your segment to populate before scheduling the email.

![](https://fast.wistia.com/embed/medias/zrerckigzi/swatch)

## How to generate a segment definition using text

If you know what kind of segment you’d like to create, but aren’t sure how to build it, try the **Define with AI** tool. You can input a phrase or a few sentences describing the segment you’d like to create, and we’ll use AI to generate a starting point for you.

1. Navigate to ****Audience > Lists & segments****.
2. Click ****Create New****.
3. Select ****Create segment****.
4. Click ****Define with AI****.

   This option only appears for new segments. If you edit an existing segment, you will not see the ****Define with AI**** button.
5. Add a segment name.
6. Type out a sentence or phrase describing the segment you’d like to create.
7. If you’re happy with the sample segment, click ****Create segment****. Otherwise, revise your input and try again. Alternatively, click ****Open in builder**** to open the segment in the segment builder and add or modify conditions.

Generating a segment with the Define with AI tool will overwrite any existing definition in the segment builder. AI-defined segments are automatically tagged "klaviyo-ai."

Learn more about [how to use the define with AI tool](https://help.klaviyo.com/hc/en-us/articles/18986425586715).

## Segment snapshots

Segments dynamically grow and shrink as profiles meet the required criteria. However, there may be occasions where you'd like to capture all the profiles currently in a segment. You can use a segment snapshot to create a new list with all the profiles currently in your desired segment.

To take a snapshot of your desired segment, select ****Snapshot segment**** Under the **Manage segment** menu.

![Snapshot segment option in manage segment menu](https://klaviyo.zendesk.com/hc/article_attachments/31334668712475)

This will create a separate list that contains all the profiles in the segment at the moment of the snapshot.

The original segment will continue to grow dynamically, but the list created from the snapshot will be static.

## Segment conditions

Every segment consists of one or more conditions. You can select conditions based on who you'd like in the segment. For example, to create a segment of people who have taken a certain action, you'd use the condition **What someone has done (or not done)**, then select the action (e.g., Placed order)

Learn more about the [segment conditions available in your account](https://klaviyo.zendesk.com/hc/en-us/articles/115005062847).

## Filtering a segment condition

When building a new segment around what someone has done (or not done), you have the opportunity to filter this action to refine your segment. To use a filter to add specificity to a segment:

- Only top-level properties are available for segmentation, so nested data (i.e., second- and third-level data) will not appear in the dropdown menu.
  1. Choose an action (e.g., **What someone has done (or not done)** > [Action or event]).
  2. Select the filter icon next to your condition.
     ![Filter button in segments](https://klaviyo.zendesk.com/hc/article_attachments/28717810853147)
  3. Choose a property from the dropdown menu that appears.
  4. Next to **equals** or **contains**, choose the specific value you'd like to filter on.

  Values in segments are case sensitive. For example, a segment of profiles with @Gmail.com email addresses would have different results than a segment of profiles with an @gmail.com email address.

  Note that a value will only pre-populate if it has synced to Klaviyo along with a tracked event (e.g., Klaviyo will only pre-populate values for products that have already been purchased).

  If you want to build a segment around a property value that does not yet exist in Klaviyo (for example, a new product that nobody has purchased yet), copy and paste the value into the empty value box and click ****Use [your\_value]****. If the property value you paste is identical to the value that will eventually sync to Klaviyo, the segment will work as expected

  While Klaviyo may sync many details about a given metric, not all synced properties are available for segmentation. For data management purposes, only the primary details of an event are synced as "top-level" properties, and only these top-level properties are segmentable.

  If you [view the raw data](https://help.klaviyo.com/hc/en-us/articles/115005076747) Klaviyo syncs for an event, you see key data points for the event. For a **Placed Order** event, for example, you can see the following top-level properties:

- Value
- Collections / Categories
- Item Count
- Items
- Source Name

You will see an array labeled **Extra** or **Details**. While the data in this array is available to insert within an email template, properties nested within this array are not be segmentable.

## Using AND vs. OR to join conditions

The AND/OR selector can be used to combine multiple conditions in a segment. To create another condition, select the ****Add condition**** button.

By default, the operator is set to **OR** but this can be toggled to **AND** at any time.

The **AND** connector between conditions will make a segment more exclusive and more strict. Each condition is checked separately and individually, and every condition must be true in order for someone to be included. Someone must meet all of the segment's conditions in order to be added.

![AND vs OR toggle in segment builder](https://klaviyo.zendesk.com/hc/article_attachments/28717850464411)

In the following example, only those who have placed an order AND subscribed to email marketing are included in the segment. If someone is subscribed but hasn't placed an order, they are not included.

![Example of AND being used in segment](https://klaviyo.zendesk.com/hc/article_attachments/28717810841499)

Meanwhile, the OR connector between a sequence of segment conditions makes the segment more inclusive and less strict. Each condition in the sequence is checked individually, meaning someone only has to meet 1 of the conditions in order to be added.

In the following example, anyone who is subscribed OR who has placed an order at least once will be included. So, this segment captures everyone who is subscribed to email as well as anyone who has ever placed an order, even if there is no overlap between them. Someone could place an order and not be subscribed, and vice versa, and still be included in the segment.

![Example of OR being used in a segment](https://klaviyo.zendesk.com/hc/article_attachments/28717850472603)

### Using AND vs. OR with negative conditions

When using OR connectors, it's especially important to keep an eye on segments with negative conditions, e.g., **someone has done X zero times over all time**. Let's say, for example, that we'd like to create a segment of people who don't live in the US or Canada.

If we use an OR connector, contacts only have to meet 1of the conditions in order to be added, not both. Someone who is in Canada, or Mexico, or Italy, and so on, is not in the US. So, people from Canada fulfill the first condition, and are therefore added to the segment (even though they don’t meet the second condition). Likewise, for the second condition, someone in the US is not in Canada, since no one can be in 2 places at once. So, people from the US, Canada, and every other country in the world are also added to this segment.

Learn more [about AND vs. OR conditions](https://help.klaviyo.com/hc/en-us/articles/360036534631).

## Clone conditions

When building segments, you can clone conditions so that you can create multiple conditions more quickly.

To clone a condition, select the clone icon next to it:

![Clone condition option in segment builder](https://klaviyo.zendesk.com/hc/article_attachments/28717850475547)

This duplicates the condition. Once cloned, you can modify either condition to fit your needs.

## How to segment your audience

### When to use a segment vs. a flow

Segments are great tools to identify cross-sections of your audience to send one-time campaigns to. While it is possible to build a flow that is triggered by being added to a segment, the same filtering and targeting options that you have in the segment builder are also available within the flow builder.

For example, if you would like to trigger an email when someone buys a specific product, you can accomplish this by creating a flow that is triggered by the **Placed Order** metric, and then add a trigger filter to the flow to only include people who purchased the specific item.

Any segment that leverages the metrics from the **What someone has/has not done** dropdown can also be built using a metric-triggered flow. Likewise, **Properties about someone** targeting options are available as flow filters.

## Additional resources

Not sure which segments to start with?

- Use [engagement tiers](https://help.klaviyo.com/hc/en-us/articles/360000407272-Create-Customer-Engagement-Tiers) to identify different levels of interest within your audience, and then market to these segments accordingly.
- Check out our [guide to list cleaning](https://help.klaviyo.com/hc/en-us/articles/115005078347-List-Cleaning) to suppress any unengaged subscribers and ensure that your deliverability remains strong and your emails make it to the inbox.
- Create [email frequency segments](https://help.klaviyo.com/hc/en-us/articles/115000769631-Create-Email-Frequency-Segments) to market to people based on how often they'd like to hear from you. This helps you keep contacts engaged by letting them choose how many emails they get.
- [Segment based on someone's predicted customer lifetime value (CLV)](https://help.klaviyo.com/hc/en-us/articles/360013201072-Segment-by-Customer-Lifetime-Value-CLV-) to identify your future VIPs.
- Learn just how powerful segments can be with our [Segmentation for ecommerce benchmark report](https://www.klaviyo.com/marketing-resources/segmentation-benchmark-report).