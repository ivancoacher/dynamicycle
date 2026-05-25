---
id: "360035312491"
title: "Advanced segmentation reference"
source_url: "https://help.klaviyo.com/hc/en-us/articles/360035312491-Advanced-segmentation-reference"
section: "Build and use segments"
category: "Audience"
category_slug: "analytics-audience"
klaviyo_updated: "2026-05-11T10:58:26Z"
language: "en"
---
## You will learn

Learn effective advanced segmentation strategies that provide insights into your customer base and create highly personalized experiences for your subscribers.

Segmentation allows you to gain detailed insights about customers so that you can produce a powerful, data-driven marketing strategy. While you may already be familiar with the basics of segmentation, the Segment Builder is such a powerful tool that there are likely still areas where you can level up.

In this guide, you will learn how to group customers in a more thoughtful, strategic way based on their own behavior. By the end, you will be able to advance beyond the basics of segmentation to improve your email and SMS performance, sign-up forms, social media, and analytics capabilities.

[How to create key segments in Klaviyo Video](https://fast.wistia.net/embed/iframe/ey9s3upm9v?seo=true&videoFoam=true)

## Before you begin

This guide will walk you through some of the more advanced use cases and best practices for segmentation. Before jumping in, if you need a refresher on segmentation basics (e.g., examples of engaged, unengaged, and VIP segments) be sure to check out [Getting started with segments](https://klaviyo.zendesk.com/hc/en-us/articles/115005237908).

We will touch upon using segments with forms, so you’ll want to have sign-up forms enabled on your site. Sign-up forms are enabled by a code snippet called Klaviyo.js. This snippet is automatically installed through the Klaviyo integration for most ecommerce platforms.

To use segments to analyze business performance metrics, you’ll want to already have data in your account. In your ****Analytics**** tab, you should see a list of events from your integrations. If you do not and need a refresher on how to get started, head to [Getting started with metrics](https://klaviyo.zendesk.com/hc/en-us/articles/115005076787).

Another prerequisite for segments that utilize our predictive analytics feature is that you must have at least 180 days of order history, orders within the last 30 days, and at least 500 customers who have placed an order over all time (all three of these refer to the **Placed Order** metric). This is what enables Klaviyo to make accurate predictions.

Finally, we will discuss how to improve your online advertising with segmentation. Because of this, you will need to have a Facebook / Instagram Business account integrated with Klaviyo.

Once all of these prerequisites are met, you're ready to get started.

## Advanced segmentation

Segmentation allows you to group your audience based on behaviors, interests, and personal characteristics. Segments are defined by a set of conditions and are typically used to:

1. Send [targeted campaigns](https://klaviyo.zendesk.com/hc/en-us/articles/115005054847)
2. Trigger [email flows](https://klaviyo.zendesk.com/hc/en-us/articles/360003040052)
3. [Analyze your performance](https://klaviyo.zendesk.com/hc/en-us/articles/360034785292)
4. Enhance [sign-up forms](https://klaviyo.zendesk.com/hc/en-us/articles/4413544555547)
5. Target with [ads on social media](https://klaviyo.zendesk.com/hc/en-us/articles/360039769672)

### For email and SMS

[Send a campaign to a target segment Video](https://fast.wistia.net/embed/iframe/d70o52p0vq?seo=true&videoFoam=true)

Here are 7 key segments you can use to boost email and SMS performance:

1. [Cross sell segment](#h_70f0c55d-02f3-40c1-abf0-e6ca9d3497c4)
2. [Location-based segment](#h_9ef12b55-89c0-4f8b-a3c3-4902e9d75bd2)
3. [Item and brand-specific segment](#h_1e65af5a-9b91-440e-9fde-3a7e717e4085)
4. [Engagement tier segment](#h_a7cac5fd-a357-4953-bc32-5081d68d273e)
5. [Churn risk segment](#h_6eaf0425-d77d-4a33-a89d-7aadd5dd5871)
6. [Average order value (AOV) segment](#h_2e887e62-054e-4e11-a8c5-dd50dbedc210)
7. [Holiday shoppers segment](#h_6155b242-d7b0-4d58-b1cf-79aa2dfc10d0)

#### Cross sell segment

A cross sell segment groups individuals that have all purchased a particular item but have not purchased one or more related items that they may be interested in. For example, if you want to create a campaign around summer tank tops, a good segment to advertise to is anyone who ordered summer shorts. Generate this cross sell segment with the following conditions:

![cross sell.jpg](https://klaviyo.zendesk.com/hc/article_attachments/31302007890587)

#### Location-based segment

You can also use location-based segments to send your location-specific content to those who may be interested. For example, if you own a business that sells winter jackets throughout North America, you can target cold weather shoppers within that region. Due to your products’ specificity, this segment will likely include customers in New England and Canada.

To create this segment, select ****Properties about someone**** and add the states, regions, and countries that you wish to include. This fine-tunes your audience to target individuals in colder climates of North America, so you can send more meaningful campaigns as winter approaches.

![location.jpg](https://klaviyo.zendesk.com/hc/article_attachments/31301989734299)

Notice in this example we use OR between our conditions. That is because OR is inclusive, so all of the states and the country of Canada are included in this grouping. However, if you want to do the inverse and find people that are not in certain locations, then you need to use AND to separate conditions. When building segments, it's vital to remember that OR is inclusive and AND is exclusive.

A visual example that highlights the importance of AND and OR for location-based segments is shown below. In this case, AND is correct because we wish to find people who are **not** in the US or Canada, rather than those who are.

![An infographic indicating that the correct connector for this location-based segment is AND (exclusive), not OR (inclusive)](https://klaviyo.zendesk.com/hc/article_attachments/28713330428059)

Learn more about [when it's best to use AND versus OR](https://klaviyo.zendesk.com/hc/en-us/articles/360036534631).

Location-based segments are also useful to target people within a certain location radius, especially when promoting an event, or for targeting people based on local laws and regulations, such as those in the EU affected by [GDPR](https://klaviyo.zendesk.com/hc/en-us/articles/360003536031).

#### Item and brand-specific segments

Your item or brand-specific segments are classifications of customers who come to your site for a specific product or type of product. This narrows down your audience by interest so that you can generate content that will appeal to them specifically.

Continuing with the New England theme, let’s say you sell football-themed merchandise. You can create a segment of individuals who come to your site to buy women's New England Patriots apparel.

Klaviyo’s gender prediction algorithm uses a customer’s first name and census data to make a gender prediction of either likely male, likely female, or uncertain. Predicted gender is an approximation, so when using targeted communication, you will likely want to include some information for both genders.

![item_specific.jpg](https://klaviyo.zendesk.com/hc/article_attachments/31302007906971)

There are many other customer characteristics to use to hone your segments as well, so feel free to experiment with different conditions that interest you or will be more applicable to your store.

You can also add your own [custom properties](https://klaviyo.zendesk.com/hc/en-us/articles/115005074627) to profiles to make segments even more detailed beyond what Klaviyo has as default options. An example of a custom property that is not a default in the Klaviyo platform is **Favorite Color**. To acquire this data from customers, consider asking for it within sign-up forms.

#### Engagement tiers

You can also create [engagement tiers](https://klaviyo.zendesk.com/hc/en-us/articles/360000407272) to reach the next level of targeted sending. This goes beyond making one engaged and one unengaged segment. Instead, you add multiple levels in between rather than a single, standard grouping. For example, you can focus on recent customers who purchased within the last four months or nearly lapsed customers who purchased 4-13 months ago. You can take into account purchase frequency and target those who purchase three or more times, or segment based on the value of their purchases as a whole.

With the release of iOS 15, macOS Monterey, iPadOS 15, and watchOS 8, Apple Mail Privacy Protection (MPP) changed the way that we receive open rate data on your emails by prefetching our tracking pixel. With this change, it’s important to understand that open rates will be inflated.
If your campaign analytics show a large number of iOS openers, we suggest identifying these affected opens in your individual [subscriber segments](https://klaviyo.zendesk.com/hc/en-us/articles/4416791883163).

For complete information on MPP opens, visit our [iOS 15: How to Prepare for Apple’s Changes](https://www.klaviyo.com/blog/apple-ios15-klaviyo) guide.

A **Nearly There** segment is just one way you can utilize the various conditions in this manner. The conditions for this are as follows:

![Segment of nearly there profiles have who have engaged but not purchased](https://klaviyo.zendesk.com/hc/article_attachments/31301989740955)

A nearly there customer is one that actively engages with your content but has yet to make a purchase. Your goal in making this segment is to nudge them in the direction of purchasing by giving them a good reason to buy. Once you group those who fit into this category, send them targeted content or incentives to purchase from your website.

#### Churn risk segment

Another vital segment to have in your account is a churn risk segment. This segment tests the likelihood that a group of customers will stop purchasing entirely from your site and switch to a competitor. You can target these individuals with winback campaigns (or via forms and social media) to revive their loyalty toward your brand. Likewise, [creating a winback flow](https://klaviyo.zendesk.com/hc/en-us/articles/115002775192) is a best practice to automate this process.

For this churn risk segment, the conditions are:

![Churn risk segment](https://klaviyo.zendesk.com/hc/article_attachments/31302007917211)

Profiles gathered in this segment will provide you key insight as to who needs a nudge to re-engage and remind them of the value of your products. You may have a high number of churn risk customers if you have many one-time purchasers, in which case, focus your marketing efforts on retaining customers after their first purchase.

You can also use Klaviyo's predicted CLV metric to identify people who are not likely to purchase again as outlined in our article on [segmenting by CLV](https://klaviyo.zendesk.com/hc/en-us/articles/360013201072).

#### Average order value (AOV) segment

Another best practice to level up your segmentation capabilities is to group customers by average order value. By doing so, you can visualize which customers tend to spend more money on purchases and which spend less. This behavioral data enables you to send them content to fit their budget and the kind of products they search for on your site.

Here is an example that focuses on customers with a high AOV:

![Average order value segment](https://klaviyo.zendesk.com/hc/article_attachments/31301989750939)

You can do the same for a low-AOV as well by selecting an AOV that is lower than a monetary number of your choice. With high- and low-AOV segments, target customers based on spending habits with customized campaigns that acknowledge their shopping behaviors.

#### Holiday shoppers segment

A holiday shoppers segment is important because it paves the way for you to reach high revenue and increased customer engagement. Some examples of key holidays include Black Friday, Cyber Monday, Mother’s Day, Father’s Day, Memorial Day, and Valentine's Day.

Below is a segment of customers who specifically shopped during your Black Friday sale last year. Make sure to use last year's BFCM dates in your own segment.

![Holiday shoppers segment](https://klaviyo.zendesk.com/hc/article_attachments/31302007926811)

Once you access these shoppers, send them content that invites them to this year’s offers, provides insight on new products, and reminds them of what about your brand drove them to purchase a year ago. Moreover, think about how you can build off of this and generate a customer base that will return year-round as well. Think about your email (or SMS) cadence around the BFCM weekend, the weekends between the holidays, and beyond.

Segments for holidays are incredibly important for implementing a sending strategy leading up to and following an event. It's a great time to use your data productively and send customers highly personalized, targeted communication to boost sales. Check out our [holiday marketing](https://academy.klaviyo.com/page/holiday-marketing-strategies) resources for more information on how to maximize your performance during this time.

### For forms

Forms, though primarily used for subscribing to a website, can be used in a variety of ways beyond opting in for marketing. Moreover, using segmentation to target forms opens doors to new strategies that promote growth and increase revenue.

Here are 3 segmentation strategies for forms:

1. [Expected date of next order segment](#h_083ea948-2101-40e6-8741-deb8c5c866a0)
2. [Customer lifetime value segment](#h_808aa393-a297-4850-a6d3-f13ac9a130ae)
3. [Location-proximity segment](#h_40878f43-1cf2-4efc-869c-690d1fbe3a85)

#### Expected date of next order segment

You can use an expected date of next order segment to target customers when they will be ready for their next purchase from your brand. In this example, we identify people whose expected date of next order is within the next two weeks, however, you can customize this as you choose.

![Expected date of next order segment](https://klaviyo.zendesk.com/hc/article_attachments/31301989758875)

Once this segment is generated, create a form that will appear for this customer around the time of their expected order date to guide them in the direction of purchasing.

When editing the form contents, head to the ****Targeting & Behaviors**** section. Select ****Target visitors in a list or segment**** and choose the specific segment you want the form to appear to. In this case, choose your expected date of next order segment.

#### Customer lifetime value (CLV) segment

Alternatively, you can edit the settings on your form to target visitors based on their customer lifetime values. Create segments for low-CLV customers by adding the following conditions:

![Customer lifetime value segment](https://klaviyo.zendesk.com/hc/article_attachments/31302007935003)

In this example, we input a predicted CLV that is at most 5. This means that the customers in this segment are predicted to spend $5 in the next year. To determine what these numbers should be for your brand, check out our guide on [How to segment by customer lifetime value (CLV)](https://help.klaviyo.com/hc/en-us/articles/360013201072).

Once these CLV segments are established, extend your targeted marketing toward your website with forms that are specific to this value. Edit the settings on your sign-up form to target visitors differently based on their CLV.

#### Location-proximity segment

Another way to apply segments to forms is to segment based on a profile's proximity to a location and promote a nearby event that they can sign up for directly on your site.

The difference between stating an exact location and stating proximity is that the exact location must be precise for those individuals to be added to the segment whereas proximity is less constrained. When you use proximity, anyone within the radius that you set will be included. This is best for event promotion because people within driving distance may sign up even if they are not within the specific city or state where the event takes place. An example segment of customers within 30 miles of Boston is shown below.

![Proximity to location segment](https://klaviyo.zendesk.com/hc/article_attachments/31301989769627)

After generating this segment, create a sign-up form targeting the location-proximity segment, urging them to sign up for an event nearby.

This form strategy ensures that you target the appropriate audience and increases your likelihood of gaining attendees. You can also use this to advertise links to an e-book or other promotional offers based on age, gender, or general interest.

### For analytics

Segmentation is also crucial for gaining business intelligence and maintaining a healthy Klaviyo account. Since segments automatically update in real-time, they provide an easy way to get a pulse check on your audience at any given moment.

Learn more about [segments with relative time conditions](https://help.klaviyo.com/hc/en-us/articles/4403222359451), which update every 24 hours.

3 ways to use segments to analyze customer data in your account include:

1. [CLV segment](#h_39ac79c5-2b88-4388-b7ec-bc3500198cf7)
2. [Test segment](#h_11430530-0f9d-4576-afb7-35213d125f76)
3. [Chronic soft bounced segment](#h_9a9b7b77-41f0-4918-adf7-e6e0cdbf1e20)

#### Customer lifetime value (CLV) segment

A CLV segment helps you estimate yearly revenue from current customers. If you segment your customer lifetime values and add up their predicted values for the year, you can gain a 12 month projected revenue. This is a key piece of information as it allows you to assess how well your business will do and strategize to increase company growth in the next year.

To create this segment, the only necessary condition is that they have placed at least one order over all time, as shown below.

![CLV segment to export CLV data](https://klaviyo.zendesk.com/hc/article_attachments/31301989774363)

Once you’ve created this segment, export it by going to ****Manage Segment**** and clicking ****Export segment to CSV****.

Select all of the following CLV related data to appear in your download: Historic Customer Lifetime Value, Predicted Customer Lifetime Value, Total Customer Lifetime Value, Predicted Number of Orders, Churn Risk Prediction, Average Days Between Orders, and UTM Medium.

Then, click ****Start Export****.

![Select CLV metrics](https://klaviyo.zendesk.com/hc/article_attachments/28713336171291)

In this CSV file, sum every cell in the **Predicted Customer Lifetime Value** column to see your predicted revenue for the next 12 months.

This projected revenue does not include potential customers who will likely emerge within the year. However, it gives you a good idea of how much revenue your current customer base will generate in that timeframe. With this information, you can adjust your business strategy accordingly and plan for the year ahead. You can use it to determine how much revenue you'll need from new customers to meet financial goals, or to create a spending budget.

#### Test segment

Another best practice is to create a sample of a larger list or segment that you wish to send a campaign or flow to. This allows you to analyze different customer groups to validate the impact of your emails or text messages compared to a control group.

To create a sample of a segment, open ****Manage segment**** menu, then click ****Sample segment members****.

![Sample segment members](https://klaviyo.zendesk.com/hc/article_attachments/28713336151579)

Send your campaign to that small sample and continue checking its performance once you do. The results will help you visualize whether or not the content is successful before sending it out to a larger customer base. Depending on the success of this segment with regard to open, click, and conversion rates, you may want to tweak the email or re-define your audience. On the other hand, you may do very well with your test segment, in which case you can send the campaign to a larger audience with confidence.

#### Chronic soft bounced segment

A chronic soft bounced email segment will analyze and monitor your email deliverability. A soft bounced email address is one that could not receive an email due to a temporary reason, such as a full inbox or the recipient’s email server being momentarily down. However, If emails frequently bounce or go unopened, email clients eventually start sending your emails to the spam folder. As a result, Klaviyo suppresses profiles that soft bounce more than seven times.

Creating this segment prevents deliverability issues because you can use it to [clean your list](https://klaviyo.zendesk.com/hc/en-us/articles/115005078347) of profiles that continually soft bounce. The suggested conditions for this segment are shown below.

![Chronic soft bounce segment](https://klaviyo.zendesk.com/hc/article_attachments/31302007947931)

When the segment generates a group of individuals who qualify for these conditions, you will be ahead of the game from a deliverability standpoint and can adjust to whom you are sending. For more information on how the segment builder is helpful when monitoring deliverability, check out [How to monitor deliverability performance](https://klaviyo.zendesk.com/hc/en-us/articles/115000201131).

### For advertising

[What are Google audiences? Video](https://fast.wistia.net/embed/iframe/oybqd7ibla?seo=true&videoFoam=true)

Segments can also level up your online advertising game, namely on Facebook, Instagram, and Google Ads. Use segments for advanced targeting for online ad campaigns and analyzing your leads.

The following are 3 types of segments to use with social media:

1. [Cross-channel segment](#h_341e8ea2-e183-4a3f-89b1-516a8140a842)
2. [Recent subscribers segment](#h_76baa83f-6117-4212-9ee6-c6cc857b5147)
3. [Former VIP segment](#h_4d375c41-c522-4da1-a356-dd4585ca7575)

#### Cross-channel segment

The first segment that you can use with social media, and in particular, a Facebook Business Account, is a cross-channel segment. A cross-channel segment works exactly as it sounds; you segment based on another mode of contact, like an email campaign or a specific form for a targeted group of people. You then use this segment to target the same individuals on social media as well, reinforcing the message that they are already seeing, now on two channels instead of one.

Here is an example of a cross-channel segment:

![Cross channel segment to identify profiles to target with social media](https://klaviyo.zendesk.com/hc/article_attachments/31302007956635)

The target audience is that of a specific email campaign. On Facebook, you can create an ad that will jog a customer’s memory of the email they already engaged with but did not purchase from.

This is best practice over re-sending an email to avoid seeming overbearing on one channel and inundating customers with too much of the same content. When audiences are surrounded by the same message in multiple channels, they become familiar with your brand and are reminded of the product you're trying to push; meanwhile, you won't rely too much on any one channel. This will boost the likelihood that these customers purchase.

#### Recent subscribers segment

A second segment that is particularly useful to sync with your social media accounts is a recent subscribers segment. These are individuals that recently opted-in to your marketing, but have not placed an order. They are a good audience to target since they have shown interest already in your brand and are in the window of time where they are most likely to make a purchase.

This screenshot shows what this new subscriber segment may look like:

![Recent subscribers segment](https://klaviyo.zendesk.com/hc/article_attachments/31302007960091)

Facebook or Instagram can provide the perfect medium to communicate a message about your brand and remind them of why they opted-in in the first place.

#### Former VIP segment

Another segment for your social media toolkit is a segment of former VIPs. If there is a lapse in how a group of former brand enthusiasts engages with your emails (or SMS), then it is time to retarget them in a different channel to regain their attention and remind them of what they're missing with user-specific content. The end goal is to re-engage this potentially lapsed segment.

To create this segment, you can use the following set of conditions, adjusting the numbers to best suit your brand:

![Former VIP segment](https://klaviyo.zendesk.com/hc/article_attachments/31301989799195)

Target this segment with ads and a unique UTM tag set to bring them back to your site. The content of this message could be anything from a discount incentive to a simple reminder message. You may also consider creating a sign-up form to target them based on that same UTM URL.

Then, create a flow that is triggered when someone enters their email into that form. This brings together email, SMS, social media (like Facebook), and forms to immerse your customers in your messaging once more.

#### Further examples

Segmenting for social media will broaden your horizons beyond just campaigns and flows. Segmentation narrows your target audience, allowing you to reach out to customers with more specific content that will resonate with them.

Even though we only went over three examples of best practices with social media segmentation, it should be noted that many of the segments you use in email or SMS can also be used on Facebook or Instagram. For example, you can use segments for cart abandonment, winback, location, re-engagement, cross sell, VIP, and more.

## Additional resources

- [How to segment for form results](https://klaviyo.zendesk.com/hc/en-us/articles/360040841811)
- [Create a VIP loyalty program](https://academy.klaviyo.com/en-us/courses/create-a-vip-loyalty-program)
- [Guide to advanced targeting on Facebook and Instagram](https://klaviyo.zendesk.com/hc/en-us/articles/360039769672)
- [Guide to AND vs. OR](https://klaviyo.zendesk.com/hc/en-us/articles/360036534631)