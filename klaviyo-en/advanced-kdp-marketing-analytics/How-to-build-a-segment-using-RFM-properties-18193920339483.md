---
id: "18193920339483"
title: "How to build a segment using RFM properties"
source_url: "https://help.klaviyo.com/hc/en-us/articles/18193920339483-How-to-build-a-segment-using-RFM-properties"
section: "Customer insights"
category: "Advanced KDP & Marketing Analytics"
category_slug: "advanced-kdp-marketing-analytics"
klaviyo_updated: "2026-04-21T13:54:31Z"
language: "en"
---
## You will learn

Learn how to use RFM values and customer groupings as properties in your segments. Using RFM properties in a segment is useful for creating segment-based recommendations in your marketing content. For example, you may want to provide discounts to some of your current **At Risk** or **Inactive** customers, or use cross-selling content with customers in your Recent group.

For information on how to use RFM segments in campaigns or flows, head to our [strategy guide](https://help.klaviyo.com/hc/en-us/articles/18194102384539).

[Advanced KDP](https://help.klaviyo.com/hc/en-us/articles/17655007276059) and [Marketing Analytics](https://help.klaviyo.com/hc/en-us/articles/33789259613595) are not included in Klaviyo’s standard marketing application, and a subscription is required to access the associated functionality.Head to our [billing guide](https://help.klaviyo.com/hc/en-us/articles/115000976672) to learn about how to purchase these plans.

## Recent report updates (as of 5/2/2024)

As of May 2, 2024, the RFM report is rolling out new‌ properties and settings. Please review the information below for [existing](#h_01HWWHY499J0M3QFMVG16Z3ZWY) and [new](#h_01HWWJ5KRZPD5X16RWRMN70BWQ) customers using Advanced KDP.

### Existing customers using Advanced KDP

#### Profile properties changes

The RFM report will have 3 new properties. The first 2 properties shown in the chart below can be used in segments.

Beginning on May 2nd, 2024 Klaviyo will introduce the new properties noted in the table below. Then on May 21st, Klaviyo will automatically update your segments to use these new properties and remove the old property values. It is recommended that before the 21st, you manually adjust any of your items using the old properties (e.g., in reports, flows, templates, forms, etc.).

| ****Old property**** | ****New property**** | ****What does it measure?**** | ****Additional considerations**** |
| --- | --- | --- | --- |
| **$current\_month\_rfm\_group** | **Current RFM group** | The RFM group the profile currently belongs to. |  |
| **$previous\_month\_rfm\_group** | **Previous RFM group** | The most recent **different** RFM group, the profile belonged to prior to their current RFM group. | Until a profile’s RFM group changes, their **Previous RFM group** will show as **Unknown******.**** |
| N/A | **RFM group last changed** | Timestamp of when the profile transitioned from **Previous RFM group** to **Current RFM group**. This will only appear when a profile changes its RFM group. |  |

#### When profile properties refresh

Additionally, RFM properties are refreshed every night instead of the 1st of the month. This means that Klaviyo will check for updates every 24 hours, and if these RFM properties have changed on a profile, you will see these changes reflected.

Keep in mind that the RFM dashboard updates immediately while the changes on a profile record update every 24 hours. Thus, you may see differences in numbers per RFM group in the dashboard that are not yet reflected in your profiles.

### New customers using Advanced KDP

New customers just getting onboarded to Advanced KDP on or after May 2, 2024 date do not need to worry about transitioning to the new profile properties, as these will already be standard.

Additionally, keep in mind that you may see the **Unknown** status for **Previous RFM group** when onboarding or when updating your RFM model while the model calculates **Current RFM group** and detects the prior state.

## Setting up a segment with RFM properties

From within **RFM Analysis**:

1. If you are an Advanced KDP customer, navigate to ****Advanced KDP > Intelligence > Customer insights > RFM analysis****. Alternatively, if you are a Marketing Analytics customer, navigate to ****Marketing Analytics > Customer insights > RFM analysis****.
2. Scroll to find the **RFM Segments** card and click on ****Create segment****.
   ![segment build button.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28705699287579)
3. Once inside the segment builder name your segment and add any applicable tags from the **Tags** dropdown.
4. In the **Definitions** dropdown, choose ******Properties about someone******.
5. Under the **Dimension** dropdown, find or use one of the two RFM options:
   ******Current RFM group******
   The RFM group the profile currently belongs to.
   ******Previous RFM group******
   The most recent **different** RFM group, the profile belonged to prior to their current RFM group.
6. Use the **Equals** dropdown to have RFM equal or not equal a certain group. For example, you may use **doesn’t equal Champion** to target all customer groups besides **Champions**.
   Learn more about [segment conditions and how to use them](https://help.klaviyo.com/hc/en-us/articles/115005062847#segment-conditions1).
7. Use the dimension value to find and choose the particular customer RFM group. By default, the data output **Type** will be **Text**. Leave this as **Text** so that the property works correctly.
   You can also choose to use [**And**](https://help.klaviyo.com/hc/en-us/articles/360036534631) [or](https://help.klaviyo.com/hc/en-us/articles/360036534631) [**Or**](https://help.klaviyo.com/hc/en-us/articles/360036534631) [connectors](https://help.klaviyo.com/hc/en-us/articles/360036534631) to tailor your segment further. For example, you may just want to target **Inactive** and **At Risk** groups.
8. Once your segment is complete, click ****Create Segment****.

![](https://klaviyo.zendesk.com/hc/article_attachments/28705699290011)