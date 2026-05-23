<h1>AND vs. OR reference</h1>

Learn more about AND and OR connectors and how they are critical to setting up segments and flows in Klaviyo. These connectors define who will be grouped within your segments as well as when someone will receive flow messages. In this guide, we will go over what differentiates the 2 conditions and when to use each to target the right audience.

[Understand AND vs. OR Video](https://fast.wistia.net/embed/iframe/gmtnipvb1k?seo=true&videoFoam=true)

## AND connector

Using the AND connector between conditions will make a segment or flow filter more exclusive. Klaviyo checks each condition separated by AND individually; therefore, each condition must be true in order for someone to be included. So, if a customer meets one condition but does not meet the other, they will be excluded from your flow or segment.

### Flow example

In the example flow below, someone must be part of your Newsletter list AND have opened an email in the last 30 days to be included. If someone is only part of your Newsletter list, or has only opened an email in the last 30 days, they will not go through this flow when they place an order.

They must have done both to qualify.

![Example flow where someone must have subscribed to your newsletter and placed an order at least once in the last 30 days](https://klaviyo.zendesk.com/hc/article_attachments/32044321298459)

### Segment example

In the example segment below, the customer must have subscribed to your Newsletter list AND placed an order at least once over all time. If someone has done only one of these actions, they will not be included in your segment.

Only those who have done both actions appear within this segment.
![Example segment where someone must have subscribed to your newsletter and placed an order at least once ever](https://klaviyo.zendesk.com/hc/article_attachments/32044360155675)

### Flow example with negative conditions

In the example flow below, we set a winback flow to include anyone who has not placed an order since starting this flow AND has not been active on your site in the last 20 days. This way, anyone who has been active on your site recently, or who has placed an order while going through the flow, will not receive the message. If someone fails either filter, they will be excluded from the flow.

Because the conditions are negative (i.e., they must **not** have placed an order, they must have been active on site **zero** times), use the AND connector so only those who meet both conditions are included.

![Example flow where someone must not have placed an order since entering the flow and has not been active on your site in the last 20 days](https://klaviyo.zendesk.com/hc/article_attachments/32044321305883)

## OR connector

Using the OR connector between a sequence of segment or flow conditions will make them more inclusive. Because of the OR connector’s inclusivity, someone only has to meet 1 of the joined conditions in order to be added. So, if a customer meets one condition but does not meet the other, they are included in your flow or segment.

### Segment example

In the example below, the customer must have subscribed to your email list OR ordered a product at least once over all time.

If someone has done neither of these actions, they will not be included in your segment. However, as long as they do at least one of the actions, they will appear in this segment.

![Example segment where customer must have subscribed to your Newsletter list OR ordered a product at least once ever](https://klaviyo.zendesk.com/hc/article_attachments/32044360159131)

## AND vs OR visual aid

![Graphic showing add is exclusive requires a profile to meet every condition and Or is inclusive and requires profile to meet just on](https://klaviyo.zendesk.com/hc/article_attachments/28723520063387)

## Complex examples

### Negative conditions

When it comes to negative statements, remember that AND requires every condition to evaluate as true, whereas with OR, only 1 must be true.

For instance, if you want to create a flow filter that excludes those who live in the USA and Canada, you may think you would use **Properties about someone** and say **Country doesn’t equal USA** OR **Country doesn’t equal Canada**.

However, the OR connector means that someone can live in Canada (and not the United States) and still go through this flow, since only 1 of these conditions must be true. To exclude people in both countries, use the AND joiner.

|  |  |
| --- | --- |
| ****Incorrect**** | ****Correct**** |
| ![Incorrect setup of a flow trigger where Country doesn't equal US or Canada, using the OR connector](https://klaviyo.zendesk.com/hc/article_attachments/32044321312027) | ![Correct setup of a flow trigger where Country doesn't equal US or Canada, using the AND connector](https://klaviyo.zendesk.com/hc/article_attachments/32044360166427) |

### Applying both connectors

In some cases, you will need to apply both AND and OR conditions when generating a segment or flow. The rules around the conditions do not change, so when two conditions are joined by AND they both must be true for subscribers to be included; whereas when conditions are separated by OR, either one can be true for subscribers to be included.

For example, in a Nearly There segment, your goal is to find subscribers who are engaged but have not yet purchased from your store. Engagement is defined with both AND and OR conditions as shown below.

![And vs or example.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28723541999259)

In this case, the OR connector acts as if it’s contained within parentheses. It is sandwiched between 2 AND connectors, but since the opened and clicked email conditions are separated by OR, they do not both need to be true for someone to appear within the segment.

## Additional resources

- [Understanding flow triggers and filters](https://klaviyo.zendesk.com/hc/en-us/articles/115002779051)
- [Advanced segmentation reference](https://klaviyo.zendesk.com/hc/en-us/articles/360035312491)
- Course: [Apply programming logic concepts to build more personalized messages](https://academy.klaviyo.com/apply-programming-logic-concepts-to-build-more-personalized-messages/1857035)
