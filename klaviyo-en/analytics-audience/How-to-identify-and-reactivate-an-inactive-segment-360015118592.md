---
id: "360015118592"
title: "How to identify and reactivate an inactive segment"
source_url: "https://help.klaviyo.com/hc/en-us/articles/360015118592-How-to-identify-and-reactivate-an-inactive-segment"
section: "Build and use segments"
category: "Audience"
category_slug: "analytics-audience"
klaviyo_updated: "2026-04-21T13:54:43Z"
language: "en"
---
## You will learn

Learn the criteria for an inactive segment, how to manually deactivate segments, as well as how to reactivate one.

Inactive segments are any segments that you have not used in the last 45 days (for regular segments) or 365 days (for starred segments). These segments are automatically moved to the Inactive Segments section of your Lists & segments page. Once a segment has been marked as inactive, you will no longer see it available for campaigns, flow triggers and filters, exporting, or sign-up forms. Inactive segments can be reactivated at any time.

You can also manually deactivate segments. You may wish to do this when you need to reduce the number of active segments in your account, or simply want to clean them up to make your account easier to navigate. Segment deactivation is an alternative to permanent segment deletion, if you think you might want to use or refer to that segment again in future.

## Criteria for an inactive segment

Any unused segment will automatically be moved to your Inactive Segments tab. A segment will be marked as inactive based as long as it meets all of the criteria below for 45 consecutive days:

- Is not connected to any flows, signup forms, or outbound ad syncs (e.g., Facebook, Google Ads)
- Has not been used in any campaigns
- Has not been starred in your dashboard
- Name or definition has not been updated
- Public API endpoints haven’t been used
- Segment memberships haven’t been exported
- Segment performance report and growth report have not been viewed
- Segment has not been opened/viewed (note: this means clicking the segment link; simply expanding the definition in the Lists and segments page doesn’t count)

If the segment is starred, the above criteria holds, except the inactivity window is 365 consecutive days (instead of the standard 45 days).

General segment activity (i.e., profiles moving in and out of segments based on its definition) does ****not**** prevent a segment from becoming inactive.

Additionally, if a Klaviyo account is not on a paid plan and is inactive for 12 months, all segments in the account will be deactivated (including starred segments).

At this time, only Klaviyo can deactivate a segment. You cannot deactivate a segment manually.

## How to prevent segment deactivation

To prevent a segment from becoming deactivated, you can take any of the following qualifying actions:

1. Use in a campaign (by selecting the segment in the recipient list or exclusion list)
2. Use in a segment-triggered flow. As long as the flow is active, the segment will also remain active.
3. Use in a form. As long as the form is active, the segment will also remain active.
4. Use in an ad sync operation. As long as the ad sync is active, the segment will also remain active.
5. Use the public API endpoints for segment/list membership
6. Export segment memberships
7. View the segment performance or segment growth reports
8. Update the segment name or definition
9. Click open and view the segment in the UI (note: you have to click the segment link; simply expanding the definition in the Lists and segments page doesn’t count)
10. Star the segment in the UI. This will allow the segment to remain active, even without any qualifying action, for 365 days. Learn more about [starred segments](#h_01K8Y0AQGJEQKPT6GR5R15DX2Z).

##

## How to manually deactivate a segment

1. Find the segment you wish to deactivate.
2. Click on the segment menu (three dots to the right of the screen).
3. Select ****Deactivate Segment**** from the dropdown menu. You'll be prompted to confirm whether you want to deactivate the segment.

   ![](https://klaviyo.zendesk.com/hc/article_attachments/46630692439451)
4. Confirming will move that segment to the Inactive Segments section on your lists/segments page.

## Reactivate an inactive segment

To reactivate an inactive segment:

1. Navigate to ****Audience >**** ****Lists & segments****.
2. Select ****Inactive Segments****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/46630728552987)
3. Find the segment you want to reactivate.
4. Click ****Reactivate****.
   ****![reactivate button](https://klaviyo.zendesk.com/hc/article_attachments/28711676853659)****
5. Click ****Update segment****.
   ****![Update segment button](https://klaviyo.zendesk.com/hc/article_attachments/28711676855067)****

The segment then appears among your active lists and segments.

## What are starred segments and how do I use them?

Starring a segments allows that segment to avoid the 45-day inactivity limit, and extends that inactivity window up to 365 days. That means that a starred segment can go for up to 365 days without taking any [qualifying action](#h_01HCWV4J0HDZ8KPC5XVD6GCENR).

After 365 days have passed with no qualifying action, the starred segment will be made inactive. It can be reactivated using [the same steps above](#h_01HCWV4J0HHK0JBS4HKFNE7M1B).

Note: this ****does not apply**** to Klaviyo accounts who are subscribed to our [Advanced KDP/Marketing Analytics product](https://help.klaviyo.com/hc/en-us/articles/17655007276059). For MA/AKDP customers, starred segments will never go inactive.

To star a segment, click on the star icon next to the segment name.

![How to star a segment](https://klaviyo.zendesk.com/hc/article_attachments/28711676849947)

Starred segments are also used in the Klaviyo app in the following ways:

(1) As a tag/filter on the lists and segments page

(2) To specify which segments appear on the [Audience performance dashboard](https://help.klaviyo.com/hc/en-us/articles/17798068936219) in accounts that have access to our Advanced KDP/Marketing Analytics product.

## Additional resources

- [Getting started with segments](https://help.klaviyo.com/hc/en-us/articles/115005237908)
- [About the lists and segments dashboard](https://klaviyo.zendesk.com/hc/en-us/articles/360046335551)
- [Advanced segmentation reference](https://klaviyo.zendesk.com/hc/en-us/articles/360035312491)