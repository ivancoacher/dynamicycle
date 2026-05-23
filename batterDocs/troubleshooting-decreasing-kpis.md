<h1>Troubleshooting decreasing KPIs</h1>

## You will learn

Learn how to adjust your strategy to improve important KPIs within Klaviyo.Key performance indicators (KPI) are metrics that identify how successful your business is in achieving its goals and maintaining good deliverability practices. Some KPIs that measure your success are open rate, click rate, owned revenue, conversion rate, and more.

## Owned revenue

Owned revenue includes any revenue attributed to the owned channels (e.g., email, SMS, push, and forms) sent through Klaviyo. For example, if a customer engages with your email and then makes a purchase within a set [attribution window,](https://help.klaviyo.com/hc/en-us/articles/115005248128) that purchase is a part of your owned revenue.

If you see your owned revenue diminish over time, it may have to do with one or multiple of the following bullet points. Each is elaborated on in more depth in the next few sections.

1. [Successful deliveries are down, or you are sending fewer emails](#h_4bae3153-27bc-4ee2-91ff-cd0f65b7f548)
2. [Unique opens are down, and thus fewer people are seeing your messaging](#h_cfd9974a-1c79-4c71-bd94-6158d4b7b8fb)
3. [Unique clicks are down, and fewer people navigate to your website](#h_9a94b215-a279-499a-b0ac-5da92b44af02)
4. [Conversion rate is down, and thus fewer people are purchasing](#h_f77ac56f-76f0-4526-9c51-5d6069654146)
5. [Form submission rate is down, and thus list growth rate is down](#h_ef04f07c-abea-4332-94db-4542a9ec97bc)
6. [Average order value (AOV) is down, and thus the monetary value of your customers’ carts and your total revenue are lower than usual](#h_8fe3ac3d-f8cd-4a6c-803b-8ffac05551a2)

## 1. Successful deliveries

The successful deliveries metric is the total count and percentage of your emails that are delivered to your subscribers. Thus, these do not include emails that bounce, regardless of whether it’s a hard bounce (due to a permanent error such as a false email) or soft bounce (due to a temporary error such as a full inbox).

If you notice that your successful delivery rate drops below 99%, and your bounce rate is increasing above 0.15%, this suggests it is time to [clean your lists](https://help.klaviyo.com/hc/en-us/articles/115005078347). In addition, consider creating a segment of contacts who have experienced soft bounces four times.

![soft_bounces.png](https://klaviyo.zendesk.com/hc/article_attachments/28715970304923)

Emails to these subscribers are likely to keep soft bouncing and, though Klaviyo suppresses profiles after seven soft bounces, you can be proactive in cleaning out these unengaged profiles before you get to that point.

Something else to consider if you see a low number of successful deliveries is the quantity and frequency of your campaigns, as well as how many recipients you are sending to. Keep a regular email cadence with your subscribers, especially those who are most engaged. Don’t stop when you have momentum, as your goal should be to build a relationship and community around your brand that grows from your messaging. However, if you send too many campaigns over a short amount of time to the same recipients, it can overwhelm your subscribers and increase the likelihood of them unsubscribing or marking your emails as spam. This will shrink your list and affect the count of deliveries in subsequent sends. If you struggle with this cadence, consider creating a content calendar to keep track of your sending schedule.

Moreover, if you have [smart sending](https://help.klaviyo.com/hc/en-us/articles/115005078227) enabled in your account, and you send multiple emails to the same individuals in a short window of time, Klaviyo may automatically refrain from sending some content to avoid overloading those recipients. If you think this may be the case, check your settings to see what timeframe you have smart send time set to.

For flows, if you see the deliveries decline, review all of your live flows and identify where the decline is stemming from. Check to ensure the flow is still triggering as expected and ensure that the data is syncing properly to Klaviyo. For example, if you recently updated your ecommerce store, but forgot to include viewed product tracking, your browse abandonment flow may have stopped sending, causing a decrease in successful deliveries.

Read [Klaviyo's anti-abuse and campaign performance monitoring](https://help.klaviyo.com/hc/en-us/articles/115000308972) for more information around this metric for email. For information around your SMS successful deliveries, head to our [FAQ on what may be causing SMS sends to fail](https://help.klaviyo.com/hc/en-us/articles/360035804352).

## 2. Open rate

Open rate is the rate at which your customers open your emails, and is thus a prominent measure of engagement. When you send a campaign that results in a critically low open rate (less than 10%), Klaviyo will send you a low open rate alert, prompting you to refine your sending in order to avoid damage to your sender reputation.

If your open rate is critically low, and few subscribers are seeing your email content as a result, then you will need to do the following:

- Adjust your subject lines
- Create an engaged segment
- Target your engaged segment with applicable content
- Monitor deliverability going forward

Learn [how to improve low open rates](https://help.klaviyo.com/hc/en-us/articles/360042454031).

Some other things to consider when you see low open rates is how often you send, who you send to, and what content you are creating at the time when your opens dipped. For example, perhaps a sudden change in list membership played a role in an open rate decrease. If you recently launched a giveaway campaign and gained unengaged profiles, then this may affect your typical metrics.

Consider if there either was a shift in the following to cause this, or if you need to adjust these action items in general:

- ****Your sending strategy****
  Have you been sending more or less frequently? For example, perhaps your subscribers are facing email fatigue if you send too often to the same profiles. Alternatively, do not send too infrequently for subscribers to forget about your brand. Consider trying out [A/B testing for campaigns](https://help.klaviyo.com/hc/en-us/articles/115005228148) and [flows](https://help.klaviyo.com/hc/en-us/articles/6960371049115), adjusting your [smart sending](https://help.klaviyo.com/hc/en-us/articles/115005078227)settings, or changing the time of day you send emails. By monitoring your results, you can see what resonates best with your audience.
- ****Subject line content****
  Are you offering fewer promotions, new arrivals, or back in stocks recently? Your subject lines should grab a reader's attention and encourage them to click to read your email content. This is directly in your control, so really personalize your subject lines to connect with your audience.
- ****Your audience****
  Check the age of the profiles you are sending to—have they been in your account for a long time and are now unengaged subscribers? Refine your audience and create segments to make sure you are sending to people who are engaged and want to open your emails. Try to create more [advanced segments](https://help.klaviyo.com/hc/en-us/articles/360035312491) to optimize your targeting. For example, include purchase history and on-site activity to gauge engagement. Alternatively, if you have men’s and women’s product lines, use [predicted gender](https://help.klaviyo.com/hc/en-us/articles/360020919731) or product preferences in segmentation to personalize messaging.
- ****Successful deliveries****
  Has there been a decrease in successful deliveries or an increase in spam or [clipped](https://help.klaviyo.com/hc/en-us/articles/115000591251) emails? These will all have an effect on your open rate.

## 3. Click rate

Click rate is the percentage of people who clicked a link in your email out of the people who received your email. There are a variety of reasons why click rate may decline at different times as you send out campaigns and flows. Here is a list of potential reasons to look out for:

- ****Fewer incentives in your content****
  If you have recently increased the price of your products or offered fewer discounts, a drop in incentives may translate to a decrease in clicks. Alternatively, if customers are getting too much of the same content, they may be less likely to click into your emails. Avoid sending the same product offerings or message content to the same profiles. Instead, keep them engaged with new collections and creative content.
- ****Rendering change****
  Always make sure to account for mobile versus desktop layouts for your emails. For example, if there is a rendering issue on one of the layouts, then customers using that device are less likely to click in your emails.
- ****Broken or fewer links****
  Broken links can confuse or frustrate your customers, leading them to not open your emails in the future or mark them as spam which will harm your deliverability. Always make sure that your links are valid before sending or scheduling your emails. Moreover, include links where needed though always make sure to have one main CTA. Link to recommended products, more categories or collections to explore, or a navigation bar for your site.
- ****Slower email load times and clipping****
  If your customers experience slower email load times or [clipping](https://help.klaviyo.com/hc/en-us/articles/115000591251), then click rate is likely to diminish for those email sends. Moreover, did you recently introduce new designs to your email templates?

## 4. Conversion rate

Conversion rate measures how often your subscribers become customers. When you use your owned channels to the fullest, you will be able to nurture customers through the acquisition funnel, from when they first hear about your brand to when they become loyal brand enthusiasts. This relationship begins in earnest at conversion.

If you notice a dip in conversion rate, consider why your subscribers may not be making that first purchase. Perhaps you need to focus on acquiring new subscribers who have never purchased before. Maybe your email content is not effectively encouraging customers to purchase. Moreover, check if there are changes in the following areas:

- ****Links leading to non-ecommerce pages of your site****
  Consider the different page types that you link out to in your emails, and cut down on links that don’t lead to your goods or services page. In general, you want a link from your messaging to prompt a conversion. If you are linking to your home, blog, news article, or collections page instead of your ecommerce-related page, perhaps this is why. Remember to use links wisely, and make changes where changes are due. That does not mean that you should remove all non-ecommerce links that are assisting your business (such as your contact or unsubscribe pages), but rather to cut down on ones that do not help your business grow. Otherwise, feature items in a more subtle way in copy and creative work to make it easy for someone to follow up and purchase.
- ****Changes in the checkout experience****
  If you have recently changed the checkout experience in any way (e.g., popup triggered on checkout page, etc.), then this could also lead to a decrease in conversions. Likewise, if the price of your products or your shipping costs recently increased, this will have an effect. If your prices have risen, you may want to re-think who you target in order to accommodate for slightly higher price points. For example, send new higher-priced promotion emails to a segment of [high-CLV customers](https://help.klaviyo.com/hc/en-us/articles/360018536172). In addition, make sure to have an abandoned cart flow set up to drive conversions. Across the board, abandoned cart flows are the most lucrative emails and, according to our [ecommerce industry benchmark report for abandon carts](https://www.klaviyo.com/marketing-resources/abandoned-cart-benchmarks#section2), abandoned cart emails that included coupon codes resulted in an above-average open rate (44.37%) and click-through rate (10.85%).
- ****Decline in open and click rate****
  If there is a decline in your open and click rates, particularly when there is also an increase in successful deliveries, then your conversion rate will likewise diminish. Head to the designated sections on [open rate](#h_cfd9974a-1c79-4c71-bd94-6158d4b7b8fb) and [click rate](#h_9a94b215-a279-499a-b0ac-5da92b44af02) for troubleshooting tips.

## 5. Form submission rate

The median form submit rate for popups and flyouts is 2.3%. If your form submission rate is lower than usual, or too low in general, then this will have a negative effect on your list growth rate, since you will not have as many new subscribers entering into your account. Think about how you can make these forms better at catching someone’s attention and providing a clear and enticing CTA. Each form will differ depending on its purpose, and so will the metrics associated. For more information on signup form analytics, [review your signup form analytics.](https://help.klaviyo.com/hc/en-us/articles/360015960712)

With regard to list growth, check if you recently changed your lead-generation efforts. This can affect your rate of growth as well. Head to our article on [getting started with signup forms and subscribe pages](https://help.klaviyo.com/hc/en-us/articles/115005080327) to learn how to grow your list strategically and enhance your form submit rate.

## 6. Revenue

Revenue is a measure of your company’s profit, including your owned revenue in Klaviyo as well as revenue gained via channels not directly in your control. There are three key situations to monitor that may cause revenue to fall:

- ****Traffic is the same, AOV is down, conversion rate is the same, total orders are the same:****
  A lower-than-usual AOV means that customers' carts are lower in price than normal, perhaps because of a sale or recent promotion. This may have to do with a decrease in average item price, a higher discount is applied to your products, or a lower amount of items in your customers’ carts. If the reason for a lower AOV is intentional, then you have no need to worry. Otherwise, consider targeting your engaged customers with higher-value goods, or creating an [upsell or cross-sell flow](https://help.klaviyo.com/hc/en-us/articles/115002775212) to encourage a second, potentially high-value, purchase. For [VIP customers](https://help.klaviyo.com/hc/en-us/articles/360039239972), introduce a loyalty program and create a VIP welcome flow to recognize their loyalty and drive repeat purchases.
- ****Traffic is the same, AOV is the same, conversion rate is down, total orders are down:****
  Total orders are down as a result of a lower than usual conversion rate; if people convert at a lower rate, fewer orders are being placed and thus a loss in revenue is incurred. This may be because the average add to cart rate is low, average bounce rate is high, or your cart abandoned rate is high.
- ****Traffic is down, AOV is the same, conversion rate is the same, total orders are down:****
  In this case, total orders drop as a result of decreased traffic to your website, and thus, fewer orders are placed. Look to improve all of the channels that take customers on your site:
  - Direct
  - Organic
  - Email
  - Social
  - Referral
  - Other

You can amplify awareness of your brand and continue leveraging your owned channels with exciting sales or promotions to re-engage subscribers. Also, create flows, such as [winback](https://help.klaviyo.com/hc/en-us/articles/115002775192) and [sunset](https://help.klaviyo.com/hc/en-us/articles/360017518492), to prioritize who you can and cannot re-engage at this time. Moreover, use forms in creative ways to acquire subscribers and build relationships with returning customers over time.

Leverage your brand community to amplify your social media presence with unique hashtags and shareable content. Launch a VIP program to gain insight into how to improve upon your current ecommerce brand, and ask your VIPs to refer friends for an added incentive. Finally, if you have a brick-and-mortar location, use QR codes to direct traffic to your site as well.

Make sure to closely [monitor your email deliverability performance](https://help.klaviyo.com/hc/en-us/articles/115000201131), especially with regard to opens, clicks, successful deliveries, and [UTM tracking.](https://help.klaviyo.com/hc/en-us/articles/115005247808) Alternatively, if you use Google Analytics (GA) and experience tracking issues, check if the following scenarios are impacting your results:

- Default GA tracking is OFF
- Default GA tracking is OFF, but they’re appending custom UTMs that aren’t working
- Default GA tracking is ON, but they’re appending custom UTMs that aren’t working with Klaviyo’s default
- Default GA tracking is ON, but there’s an issue post-click in which UTMs are stripped on the landing page or redirecting on-site.

For SMS tracking, UTM tracking needs to be added to the links within SMS messages.

## Additional resources

- [How to monitor email deliverability performance](https://help.klaviyo.com/hc/en-us/articles/115000201131)
- [Understanding Klaviyo's anti-abuse and campaign performance monitoring](https://help.klaviyo.com/hc/en-us/articles/115000308972)
- [Understanding UTM tracking in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115005247808)
- [Troubleshooting decreasing campaign open rates](https://help.klaviyo.com/hc/en-us/articles/360042454031)
