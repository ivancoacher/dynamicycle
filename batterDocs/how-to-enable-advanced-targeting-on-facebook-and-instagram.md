<h1>How to enable advanced targeting on Facebook and Instagram</h1>

## You will learn

Learn how to enable advanced targeting on Facebook and Instagram. Advanced targeting strategies can engage your customers creatively, targeting them on multiple channels.

- Learn how to re-engaged lapsed VIPs on Facebook and Instagram
- Use A/B testing to identify your best-performing sign-up forms
- Retarget customers who have not responded to your abandoned cart or welcome emails
- Launch a cross-sell campaign on Facebook and Instagram
- Target lapsed subscribers with a Facebook winback campaign

## Before you begin

The advanced targeting strategies in this guide leverage your Meta Ads integration. If you have not already integrated Meta Ads with your Klaviyo account, follow these [instructions to enable your integration](https://klaviyo.zendesk.com/hc/en-us/articles/115005082127).

## Re-engaging VIPs who have lapsed

If customers who were once on your VIP list haven’t engaged with your brand recently, you can target them on a different platform to bring them back to your brand. There is a chance your emails might be [going to their spam folder](https://help.klaviyo.com/hc/en-us/articles/115005247008), so you should target them on Facebook or Instagram to increase the chances your message is heard.

### Create an unengaged VIP segment

1. First, you’ll need to define your audience. Create a segment of customers who have spent a significant amount of money at your store. One way to identify a big-spender is to use **Historic Customer Lifetime Value** to measure your customers’ predicted spending.
2. If your account is not yet large enough to pull meaningful predictive analytic data consider using another available metric such as **Revenue**.
   ![Unengaged VIP segment in Klaviyo segment builder based on predictive analytics historic CLV at least 500 and has opened email zero times in the last 120 days](https://klaviyo.zendesk.com/hc/article_attachments/28717382066331)
3. Further define your unengaged VIPs by identifying users who have not opened an email in the last several months. Change the values within this segment based on your business model, price of goods, and how often you send out emails.

Next, you’ll create a Meta custom audience with the customers in this segment.

### Create a Meta campaign

1. After you’ve created the segment of your lapsed VIPs, [sync this segment with a Meta audience](https://help.klaviyo.com/hc/en-us/articles/115005082127).
2. Create a Meta campaign to target your unengaged VIPs.
3. Ads should direct a profile to your site with a unique UTM tag. You’ll use this UTM tag for targeting in the next step.
4. Customize your messaging with some eye-catching content based on your segment’s interests. Remind them about what an awesome brand you are and/or offer them an incentive, such as a discount for their next purchase.
   ![Facebook Ad for 10% off at Pet Supply Co with image of large brown dog](https://klaviyo.zendesk.com/hc/article_attachments/28717388357403)

### Create a UTM-targeted sign-up form

1. Next, create a sign-up form tailored to your unengaged VIPs who respond to the Meta campaign. Surface the sign-up form only to customers who land on the URL with the unique UTM, as described in the previous section.
2. In the sign-up form builder, navigate to ****Behaviors****. In ****Targeting > By URL****, select ****Only show on certain URLs******,** and specify the unique UTM you created in the previous step.
3. In the example below, the form shows to existing Klaviyo customers on URLs containing **utm\_vip**.
   ![Welcome Back signup form with puppy in Klaviyo form builder](https://klaviyo.zendesk.com/hc/article_attachments/28717388364955)
4. You’ll want to drive these customers to sign up for an email-only discount message. This is one way of driving customers to re-engage with you by email.

### Create a re-engagement flow

1. Customers who sign up via UTM-targeted sign-up form can be added to a new list.
2. You can then create a re-engagement flow that is triggered by an addition to a re-engaged VIP list. Send an email-exclusive offer to these customers.
   ![Flow chart showing sync form, create list, and send email steps](https://klaviyo.zendesk.com/hc/article_attachments/28717388372507)
3. This will pull your unengaged VIP profiles into your engaged main list and hopefully lead to conversions and additional revenue.
4. You can also use an email-only discount method for subscribers who are purchasing customers but are not yet email subscribers.

## A/B testing a form

Although you’re not able to create an A/B test with the Klaviyo sign-up forms, you can use Meta’s A/B testing feature to test two different UTM-targeted Klaviyo forms.

1. You’ll start by creating two unique UTM links that will direct your customers from your Meta ads.
2. Then, create a Meta ad, and split your Meta audience into two. Each audience will be identical except they’ll be directed to 2 different URL destinations. Customers will click through to the same site, but the UTMs will be different. This will allow you to target each unique URL with a different UTM-targeted sign-up form.
3. For example, when people are directed from Facebook to URL A, you’ll surface UTM-targeted Sign-up Form A. When people are directed from Facebook to URL B, you’ll surface UTM-targeted Sign-up Form B.
4. You can then analyze the performance of each UTM-targeted form to determine which performs better.

### Create unique links for the CTA

1. First, create two unique links to be featured in your Meta ads.
2. Each URL should link to the same site but be tagged with different UTMs. For example, below are two links that direct to Klaviyo.com but are tagged with two UTM variations:
   [www.Klaviyo.com?/utm\_variation=A](http://www.klaviyo.com?/utm_variatio)
   [www.Klaviyo.com?/utm\_variation=B](http://www.klaviyo.com?/utm_variatio)

### Create a Meta target audience

1. Next, create a Meta audience.
2. Within Meta, you can find the audience builder in ****Business Tools > Audience > Create a Saved Audience****.
   ![Facebook Audience builder with audience based on custom audience Dog Lovers 25+ with targeting settings selected](https://klaviyo.zendesk.com/hc/article_attachments/28717388374427)

### A/B test a Meta ad

1. When you are creating a Meta ad campaign, use the A/B test feature to create two random, non-overlapping ads.
2. In Meta, test variants can be created after your campaign is published by selecting a variable and creating new versions to compare against the original.
3. When you are creating the campaign, select "Get Started" under A/B Test to set that campaign as the control.
   ![A/B Test information in Facebook including note about how A/B test creation has changed](https://klaviyo.zendesk.com/hc/article_attachments/28717388377755)
4. When you create the test variant, make the ad identical to the original with only the URL destination varying.

### Create two UTM-targeted sign-up forms

1. Next, head over to Klaviyo to create two different Klaviyo sign-up forms.
2. The forms should be identical except for the section you’re A/B testing.
3. Here are some examples of variables you might test:
   - Discount vs. non-discount
   - Two different discount values
   - Two different calls to action
   - Two different welcome messages
4. Next, in the Klaviyo sign-up form editor, navigate to the ****Behaviors****, and in the **By URL** section, select **Only show on certain URLs**. Insert one of the two URLs here. For example, Form A will target [www.Klaviyo.com?/utm\_variation=A](http://www.klaviyo.com?/utm_variatio) and Form B will target [www.Klaviyo.com?/utm\_variation=B](http://www.klaviyo.com?/utm_variatio).
5. When you’ve set your forms live, turn on your Meta campaign. We recommend running the campaign for about two weeks to collect enough data to analyze.

### Monitor sign-up form performance

1. Use Klaviyo analytics to review each form’s performance.
2. Based on your results, refine and iterate your forms to increase ad conversions.
3. Learn more in our article on [sign-up form analytics](https://klaviyo.zendesk.com/hc/en-us/articles/360015960712).

## Third-party retargeting

Use Meta Ads to complement the customer journey. Meta Ads can be used on both Facebook and Instagram, so consider targeting customers on both of these platforms. Create a segment of customers for each of the following scenarios (Abandoned Cart and Welcome Series) and target them on Facebook and/or Instagram. Remember that you can retarget customers who are suppressed with Meta ads without it impacting your email deliverability.

### Abandoned cart

Abandoned cart emails can be highly effective, but sometimes a person needs an extra nudge to convert. Retarget customers who have received an abandoned cart email but have not yet purchased. For example, create a segment of customers who received an abandoned cart email in the last three days and have placed an order zero times.

### Welcome series

The first 14 days after a customer subscribes is a critical time to get your customers to convert. Encourage your newest subscribers to purchase by retargeting them on Facebook or Instagram. A Facebook Ad campaign can run in conjunction with a welcome flow (via email).

1. Below is a segment of customers who have been added to the newsletter list in the last 14 days but have never placed an order:
   ![Segment in Klaviyo segment builder of customers who have been added to the newsletter list in the last 14 days but have never placed an order](https://klaviyo.zendesk.com/hc/article_attachments/28717382085019)
2. [Sync this segment of customers to a Meta audience](https://help.klaviyo.com/hc/en-us/articles/115005082127-Integrate-Facebook-Advertising-with-Klaviyo#sync-a-list-or-segment-to-a-custom-audience2) for advanced targeting.
3. Consider creating a complimentary lookalike Audience as well.

### Cross-sell

Targeting customers with Facebook and Instagram ads is a great way to encourage customers to buy a complementary product that they may also be interested in.

1. Create a segment of customers who bought from X category but not Y category. See example below:
   ![Segment in Klaviyo segment builder of customers who have placed a whole bean order but not a ground blend order](https://klaviyo.zendesk.com/hc/article_attachments/28717388383515)
2. [Sync this segment of customers to a Meta audience](https://help.klaviyo.com/hc/en-us/articles/115005082127-Integrate-Facebook-Advertising-with-Klaviyo) for advanced targeting. Consider creating a complimentary lookalike audience as well.

### Winback

Another key social media strategy is to remind your unengaged customers of your brand on Facebook and Instagram. This strategy is similar in concept to retargeting lapsed VIPs, but instead, we’re targeting any former customer that is no longer engaging with your brand. It is especially helpful to target lapsed customers via Facebook Ad because retargeting on Facebook will not affect your email deliverability, and you may still target contacts who are suppressed from receiving Klaviyo emails on Facebook.

1. Create a segment of customers that have purchased before but not in the last six months.
   ![Segment in Klaviyo segment builder of customers that have purchased before but not in the last six months](https://klaviyo.zendesk.com/hc/article_attachments/28717388386715)
2. [Sync this segment of customers to a Meta audience](https://help.klaviyo.com/hc/en-us/articles/115005082127-Integrate-Facebook-Advertising-with-Klaviyo) for advanced targeting. Consider creating a complimentary lookalike audience as well.

## Outcome

You've learned how to enable advanced targeting strategies on Facebook and Instagram.

## Additional resources

- [Getting started with Meta Ads](https://klaviyo.zendesk.com/hc/en-us/articles/115005082127)
- [Grow your business with Klaviyo's Meta Ads integration (Klaviyo Academy course)](https://academy.klaviyo.com/grow-your-business-with-klaviyos-facebook-advertising-integration)
- Need more help getting started with Klaviyo? Check out [Klaviyo's Agency Partners](https://klaviyo.partnerpage.io/?utm_source=helpcenter&utm_medium=advertising)
