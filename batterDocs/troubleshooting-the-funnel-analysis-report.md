<h1>Troubleshooting the funnel analysis report</h1>

## You will learn

Learn how to troubleshoot potential issues with your funnel analysis cards that may be producing errors or inaccurate numbers. This guide will walk through the main issues that arise when placing certain events together and in certain orders.

[Advanced KDP](https://help.klaviyo.com/hc/en-us/articles/17655007276059) and [Marketing Analytics](https://help.klaviyo.com/hc/en-us/articles/33789259613595) are not included in Klaviyo’s standard marketing application, and a subscription is required to access the associated functionality.Head to our [billing guide](https://help.klaviyo.com/hc/en-us/articles/115000976672) to learn about how to purchase these plans.

## Placing an onsite event before an event from another source

For example, you add **Viewed product** as the first step in a checkout funnel, but the counts of **Checkout started** and **Placed orders** seem to have dropped significantly.

Klaviyo’s funnel analysis report allows you to combine events from different sources in order to visualize various customer journeys. However, when combining events from Klaviyo’s onsite JS tracking with events from an integration partner, it’s important to keep in mind how your shoppers are tracked across these different sources.

Examples of common events from an ecommerce platform include:

- Checkout started
- Checkout completed
- Placed order
- Refunded order
- Canceled order
- Fulfilled order

Examples of common events driven by Klaviyo.js include:

- Active on site
- Viewed product
- Custom events sent via `klaviyo.track` from the browser.

### Klaviyo onsite tracking considerations

Klaviyo’s onsite tracking (klaviyo.js) only fires for “identified” site visitors that [Klaviyo has been able to cookie](https://help.klaviyo.com/hc/en-us/articles/115005076767#who-klaviyo-tracks5).

There are 3 key ways Klaviyo will identify a site visitor for onsite tracking:

1. If someone has, at some point, clicked through a Klaviyo email to your website.
2. If someone has, at some point, subscribed/opted-in through a Klaviyo form.
3. If someone has, at some point, logged into your site and you have tracking installed.

For example, if you support a “guest checkout” experience on your website then you may have a significant list of customers whom Klaviyo has not yet cookied, which means you could be recording events like **Checkout started**, **Placed order**, **Refunded order** etc., but are not recording events like **Active on site** or **Viewed product**.

![faqs troubleshooting events.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28717418130459)

Consequently, when using the funnel analysis report, you may notice that the counts of events from your ecommerce integration drop when you add a Klaviyo onsite event in a preceding funnel step. This is because you are now limiting subsequent steps in your funnel only to “Klaviyo identified” shoppers.

Additionally, even fully identified shoppers may use different devices and browsers, use ad blockers that prevent onsite tracking from firing, or reside in a country/locale that prevents or blocks cookies. These behaviors can also contribute to a gap between onsite tracking coverage and the server-side tracking supported by integration partners.

Advanced KDP customers now have the option to enable post-identification backfill for anonymous profiles. This feature will store a shopper’s information in a browser’s local storage for a period of time (different browsers impose different time limits on data storage). When this feature is enabled, Klaviyo will populate new customer profiles with any data that has been saved in their browser once the customer becomes identified. This will provide greater coverage for Klaviyo’s onsite events and reduce, but not eliminate, the gap between onsite events and integration partners.

## Using **Viewed product** and **Active on site** events together

For example, you see a drop in **Viewed product** counts when you add **Active on site** in a preceding funnel step.

It is not recommended to combine **Active on site** and **Viewed product** events within the same funnel chart because these events are fired asynchronously. This means that when a user visits your website, we may record a **Viewed product** event before an **Active on site** event, or vice versa. Since this behavior is inconsistent, it can provide a misleading view of shopper behavior when visualized in a funnel diagram, which relies on a logical sequence of events.

For example, you see a large drop in **Active on site** counts when you add **Viewed product** in a preceding funnel step.

As noted above, it is not recommended to combine these events within the same funnel chart. You may notice a larger drop in **Active on site** counts when **Viewed product** precedes it in a funnel.

In addition to the asynchronous relationship between these events, it’s also important to note that **Active on site** fires once per session (which can last up to an hour), while **Viewed product** events can fire multiple times per session. This means that if a **Viewed product** event happens to fire after the initial **Active on site** event, a user will need to return after their session expires in order to record an **Active on site** event after the **Viewed product** event. Hence, you may notice a big drop in **Active on site** events when you order your funnel this way.

## Additional resources

[Getting started with the funnel analysis report](https://help.klaviyo.com/hc/en-us/articles/17798009376155)

[Getting started with Klaviyo onsite tracking](https://help.klaviyo.com/hc/en-us/articles/115005076767)

[Understanding cookies in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/360034666712)
