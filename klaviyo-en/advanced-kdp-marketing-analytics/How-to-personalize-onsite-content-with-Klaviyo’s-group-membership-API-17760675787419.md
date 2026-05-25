---
id: "17760675787419"
title: "How to personalize onsite content with Klaviyo’s group membership API"
source_url: "https://help.klaviyo.com/hc/en-us/articles/17760675787419-How-to-personalize-onsite-content-with-Klaviyo-s-group-membership-API"
section: "Group membership API (Advanced KDP)"
category: "Advanced KDP & Marketing Analytics"
category_slug: "advanced-kdp-marketing-analytics"
klaviyo_updated: "2026-04-21T13:56:44Z"
language: "en"
---
## You will learn

Learn how to use the **klaviyo** JavaScript object’s getGroupMembership method, which can be used to implement onsite personalization on your website. This requires loading the **klaviyo** object and passing an array of lists or segments to check, which will return an output that you can leverage for onsite personalization.

[Advanced KDP](https://help.klaviyo.com/hc/en-us/articles/17655007276059) is not included in Klaviyo’s standard marketing application, and a subscription is required to access the associated functionality. Head to our [billing guide](https://help.klaviyo.com/hc/en-us/articles/115000976672) to learn how to purchase this plan.

## Before you begin

This feature is only available for Advanced KDP customers, and is only available through the **klaviyo** object. To learn more about the **klaviyo** JavaScript object and what it can do, read the [introduction to the Klaviyo object.](https://developers.klaviyo.com/en/docs/introduction_to_the_klaviyo_object)

When you add Klaviyo's onsite tracking to your site, only the browsing activity of "known browsers" is tracked (i.e. browsers that have visited, engaged, and been identified or "cookied"). Klaviyo’s onsite tracking does not track anonymous browsers. There are 3 key ways Klaviyo will identify a site visitor for onsite tracking:

- If someone has clicked through a Klaviyo email to your website
- If someone has subscribed through a Klaviyo form
- If someone has logged into your site and you have tracking installed

See our Klaviyo's [video](https://www.youtube.com/watch?v=0MYFjCsm9nw) on using the group membership API.

## Install Klaviyo.js and load the Klaviyo object

You’ll first need to install Klaviyo.js, if you have not done so already. Klaviyo.js, also known as [Klaviyo’s Active on Site JavaScript](https://developers.klaviyo.com/en/docs/guide_to_integrating_a_platform_without_a_pre_built_klaviyo_integration#active-on-site-tracking-snippet), automatically supports the **klaviyo** object. If you have enabled an integration with your Klaviyo account or installed Klaviyo.js manually, you will be able to initiate the **klaviyo** object to listen for relevant calls.

To use the **klaviyo** object immediately on page load, we recommend manually installing the snippet below on your site (in addition to installing Klaviyo.js as mentioned above). The **klaviyo** object only needs to be loaded once per page.

To load the **klaviyo** object:

```
!(function () {
  if (!window.klaviyo) {
    window._klOnsite = window._klOnsite || [];
    try {
      window.klaviyo = new Proxy(
        {},
        {
          get: function (n, i) {
            return "push" === i
              ? function () {
                  var n;
                  (n = window._klOnsite).push.apply(n, arguments);
                }
              : function () {
                  for (
                    var n = arguments.length, o = new Array(n), w = 0;
                    w < n;
                    w++
                  )
                    o[w] = arguments[w];
                  var t =
                      "function" == typeof o[o.length - 1] ? o.pop() : void 0,
                    e = new Promise(function (n) {
                      window._klOnsite.push(
                        [i].concat(o, [
                          function (i) {
                            t && t(i), n(i);
                          },
                        ]),
                      );
                    });
                  return e;
                };
          },
        },
      );
    } catch (n) {
      (window.klaviyo = window.klaviyo || []),
        (window.klaviyo.push = function () {
          var n;
          (n = window._klOnsite).push.apply(n, arguments);
        });
    }
  }
})();
```

To use the **klaviyo** JavaScript object’s getGroupMembership method for onsite personalization:

1. Within your code, select the list or segment IDs you want to check membership for. The limit is 50 lists or segments.
2. Identify users on your site via a Klaviyo form or other means.
3. Make a call in the following format, with an array of the list or segment IDs you want to check membership for:

```
klaviyo.getGroupMembership(['listID1', 'listID2', 'listID3'])
```

The output provided will be an array of the list/segment IDs that the identified user belongs to, given that those IDs were in the input array. If an empty array is returned, it means that you passed in too many IDs, or that the user does not belong to any of the lists or segments you provided.

You can use the returned segment and list membership data to customize your site with relevant products, content, and more based on customer segments from Klaviyo.

### Code example

Here is an example showing how to call the getGroupMembership API with multiple segment IDs.

```
const customerSegments = await klaviyo.getGroupMembership([
  VIPSegmentID,
  UnEngagedSegmentID,
  DogLoversSegmentID
]);
```

## Impact on site performance

The group membership API has minimal impact on your site's performance. The Javascript file (i.e., web\_personalization.js) Klaviyo loads on your site is only about 1.2KB and the bundle request for this file is not main thread blocking, so it does not impact the usability of any pages.

The data that is loaded to customize a site based on the customer profile is cached in the browser after it is first requested, so additional requests do not require backend API calls.

## Outcome

You can now use the **klaviyo** JavaScript object with web personalization tools and to personalize onsite content based on segment or list membership.