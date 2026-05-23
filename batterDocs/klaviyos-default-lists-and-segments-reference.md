<h1>Klaviyo&#039;s default lists and segments reference</h1>

## You will learn

Learn about the default lists and segments provided for all new Klaviyo accounts. Once you complete the Klaviyo [setup wizard](https://klaviyo.zendesk.com/hc/en-us/articles/115000255731), you will have several default lists and segments populated in your account. These lists and segments identify key groups of people within your account and are designed to help you get off on the right foot with your sending strategy. The pre-populated lists and segments are as follows:

- Preview List
- New Subscribers
- Engaged (30, 60, and 90 days)
- Email list

When you add an integration to your Klaviyo account, additional default segments are also populated in your account.

New to Klaviyo and need inspiration for segmentation? Check out our [Guide to creating segments](https://help.klaviyo.com/hc/en-us/articles/115005237908).

## Preview list

Your preview list is a static list of people that receive your test campaigns. This list should include yourself, as well as any other members of your organization who wish to receive previews of campaigns. Sending to this list will allow you to test the layout of your content in the inbox in a live send rather than a [preview email sent from within the email editor](https://help.klaviyo.com/hc/en-us/articles/115005081907#previewing-in-klaviyo-vs--sending-a-preview-email1). This can be particularly helpful if you want to check that your email is mobile-optimized, clips in Gmail, and more.

## New subscribers

New subscribers are contacts who subscribed to your email list in the last 2 weeks. If you've recently integrated your ecommerce platform or uploaded a CSV file of contacts to your email list in the past 2 weeks, these people will be included in this segment. Once someone has been on your email list for longer than 2 weeks, they will filter out of this segment. There is also a condition in this segment that excludes anyone who is suppressed. While it's not possible to email [suppressed](https://help.klaviyo.com/hc/en-us/articles/115005246108) contacts in Klaviyo, excluding them from a segment gives you a more accurate calculation of how many people within that segment you can email.

![new subscriber segment](https://klaviyo.zendesk.com/hc/article_attachments/28716065250459)

There are several reasons you may want to use this segment. First, if you [integrate your Klaviyo account with Facebook](https://help.klaviyo.com/hc/en-us/articles/115005082127), you can sync this segment to Custom Audiences to target new subscribers.

Second, if you have a [welcome series flow](https://help.klaviyo.com/hc/en-us/articles/115002775172), you may want to exclude new subscribers from your campaign sends until they finish going through the flow to ensure that you're not sending mixed messages.

Last, this is a good group to keep an eye on from a business intelligence standpoint. You may want to monitor how this number of people changes over time to ensure that your number of recent signups is growing.

## Engaged

Your engaged segment is the primary group of people that you should send to. This segment includes people who have opened or clicked an email at least once recently. New Klaviyo accounts have access to 30-, 60-, and 90-day engaged segments. These segments will be empty until you send your first email with Klaviyo.

![A segment of subscribers who have engaged in the last 60 days](https://klaviyo.zendesk.com/hc/article_attachments/28716065246491)

With the release of iOS15, macOS Monterey, iPadOS15, and WatchOS 8, Apple Mail Privacy Protection (MPP) changed the way that we receive open rate data on your emails by prefetching our tracking pixel. With this change, it’s important to understand that open rates will be inflated.

If your campaign analytics show a large number of iOS openers, we suggest identifying these affected opens in your individual [subscriber segments](https://help.klaviyo.com/hc/en-us/articles/4416791883163).

For complete information on MPP opens, visit our [iOS 15: How to Prepare for Apple’s Changes](https://www.klaviyo.com/blog/apple-ios15-klaviyo) guide.

## Email list

This is the default ["main email list"](https://klaviyo.zendesk.com/hc/en-us/articles/360043947571) that Klaviyo creates in your account. This should be the list that all new email subscribers are added to, whether they sign up via a signup form, by opting in at checkout, or subscribe via any other acquisition method that you use. Email this list whenever you're trying to reach a broad audience, but ensure that you exclude your 1-year and 3-month [unengaged segments](https://klaviyo.zendesk.com/hc/en-us/articles/360044054732) to ensure that your open rates are above 10%.

## SMS list

Use this list for all your SMS subscribers. Message this list when you want to reach all SMS contacts, or segment to send targeted messages.

## Integration segments

Once you add a Klaviyo-native ecommerce or hospitality integration to Klaviyo, the following segments are also added to your account. Note that segments will be added for every integration (for example, if you have both Zenoti and Magento, you’ll get two sets of segments).

|  |  |
| --- | --- |
| ****Segment Name**** | ****Integration(s)**** |
| Churn Risks | **Ecommerce******:**** Shopify, BigCommerce, Square, WooCommerce, Magento 1, Magento 2    **Restaurants******:**** Chownow    **Health and wellness******:**** Zenoti, Boulevard    **Hotels and travel******:**** Guesty, Mews |
| Potential Purchasers |
| VIP Customers |
| Winback Opportunities |
| Repeat Buyers |

### Churn risks

A churn risk segment includes anyone who has purchased from your store at least once but has since lapsed in engagement. This gives you insight into who may soon turn toward another brand completely. You will want to re-engage these profiles with campaigns that include targeted content and a discount or other incentive.

You may have a high churn risk if you have a large number of one-time purchasers, in which case you will want to focus your marketing efforts on retaining customers after their first purchase. Consider creating [upsell and cross-sell flows](https://klaviyo.zendesk.com/hc/en-us/articles/115002775212) to send after someone makes a purchase, guiding them in the direction of other products they may be interested in.

![Churn risks](https://klaviyo.zendesk.com/hc/article_attachments/28716054737947)

### Potential purchasers

A potential purchaser segment includes anyone who engaged with your brand in the past month but has yet to make a purchase. This is a good segment to target with campaigns, ads, and forms as they are interested in your brand and may benefit from a gentle reminder to purchase.

![potential purchasers](https://klaviyo.zendesk.com/hc/article_attachments/28716054747163)

### VIP customers

A VIP customer is one who has purchased from your site recently, does so frequently, and has spent a lot of money on your brand. You can redefine this segment to match your business preferences and customers’ buying cycles, but the default options are shown below.

![VIP customers](https://klaviyo.zendesk.com/hc/article_attachments/28716065258139)

### Winback opportunities

Your winback opportunities segment includes former customers who are not suppressed but who have not placed an order in an extended period of time. A best practice is to generate a [winback flow](https://klaviyo.zendesk.com/hc/en-us/articles/115002775192) to re-engage these individuals and remind them of the value of your brand.

![winback opportunities](https://klaviyo.zendesk.com/hc/article_attachments/28716054751643)

### Repeat buyers

A repeat buyer is someone who has purchased from your store multiple times and will likely do so again. They are a good audience to target with branded content as they are already interested and may need a nudge in the direction of another purchase.

![Repeat Buyers](https://klaviyo.zendesk.com/hc/article_attachments/28716065272859)
