---
id: "42766438882075"
title: "How to create segments directly from funnels"
source_url: "https://help.klaviyo.com/hc/en-us/articles/42766438882075-How-to-create-segments-directly-from-funnels"
section: "Customer insights"
category: "Advanced KDP & Marketing Analytics"
category_slug: "advanced-kdp-marketing-analytics"
klaviyo_updated: "2026-04-21T13:54:56Z"
language: "en"
---
Available to customers with the Marketing Analytics or Advanced Klaviyo Data Platform (AKDP) products.

### ****Overview****

With the ****actionability**** added in the ****Funnel analysis**** page, you can now build a segment of profiles who completed—or dropped off—at a specific point in a funnel. This lets you quickly act on insights by building segments from your funnel data without leaving the Marketing Analytics experience.

For example, you can quickly build a segment of:

- Customers who added items to their cart but didn’t place an order
- Profiles who opened a campaign but didn’t click through
- Visitors who started checkout but didn’t complete it within your funnel’s time window

These segments use the same ****sequential event logic**** available in [event funnels for segmentation](https://help.klaviyo.com/hc/en-us/articles/42691974773147), helping you turn funnel insights into actionable audiences for campaigns and flows.

### ****How to create a segment from a funnel****

1. Navigate to ****Marketing Analytics**** > ****Customer Insights**** > ****Funnel analysis****.
2. Hover over a ****funnel step**** (blue bar) or ****drop-off**** (lighter diagonal connector) to see a tooltip.

   ![hover on funnel to see actionable tooltip](https://klaviyo.zendesk.com/hc/article_attachments/42766454485787)
3. Click the tooltip and select ****Create segment****.

   ![click on tooltip to create segment](https://klaviyo.zendesk.com/hc/article_attachments/42766454486171)
4. The ****Create segment**** drawer appears on the right-hand side of the page.

   - The segment definition is ****pre-filled**** based on the funnel event or drop-off you selected.
   - Any ****segment filter**** applied to the funnel is automatically included in the segment definition.
   - The segment name and a ****“Funnel Analysis” tag**** are also added automatically.![segment creation drawer with segment definition](https://klaviyo.zendesk.com/hc/article_attachments/42766454486299)
5. Review the segment definition and membership preview.
6. Choose one of the following:

- ****Create segment**** — immediately creates the segment and shows a success toast confirmation.
- ****Edit in builder**** — opens the segment builder, where you can further customize the definition.

Once created, you’ll find the new segment on your ****Segments**** page, tagged as **Funnel Analysis**.

![funnel segment on segments list page](https://klaviyo.zendesk.com/hc/article_attachments/42766454486683)

### ****How the segment is built****

The segment is built using the ****event funnel segmentation condition**** (**Steps someone has taken in a specific order**).

It uses your selected funnel step(s) and applies these settings automatically:

|  |  |
| --- | --- |
| ****Funnel Setting**** | ****How it’s applied in segment definition**** |
| ****Segment filter**** | Included, if applied on the funnel |
| ****Event filters**** | Not supported currently (filters applied on individual steps in the funnel are not carried over to the segment) |
| ****Date range**** | Matches the funnel analysis date range, up to a maximum of 1 year (365 days) |
| ****Completion window**** | Snaps to the closest supported window in segmentation: 1 hour, 1 day, 3 days, 5 days, 1 week, 1 month, 3 months, 6 months, or 1 year. If none is set, defaults to **all time**. |

****Note:**** You can edit these defaults anytime in the segment builder after creation.

### ****Best practices and limitations****

- Use this feature to ****quickly turn insights into action****—for example, re-engage drop-offs or nurture converters.
- For more complex sequential logic, open the segment in the ****segment builder**** and modify further.
- Filters on ****individual funnel events**** are not yet supported in automatic segment creation.
- The ****maximum date range**** for created segments is ****1 year****, even if your funnel is set to a longer range.

### ****Example use cases****

- ****Re-engagement:**** Create a segment of customers who **viewed a product** but **didn’t add to cart** within 3 days.
- ****Abandonment recovery:**** Build a segment for users who **started checkout** but **didn’t purchase** in the last 7 days.
- ****Campaign targeting:**** Create a segment of profiles who **opened** a specific campaign but **did not click**.

### ****Additional resources****

- [Getting started with the funnel analysis report](https://help.klaviyo.com/hc/en-us/articles/17798009376155)
- [How to use event funnels in segmentation](https://help.klaviyo.com/hc/en-us/articles/42691974773147)