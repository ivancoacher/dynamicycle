<h1>How to preview segments</h1>

## You will learn

Learn how to preview a segment’s membership before you create it. Previewing segments can help speed up the creation process by providing insights into who is included, and allowing you to troubleshoot without waiting for a segment to generate. These features are supported for segments with 100 or fewer criteria.

## Preview segment counts

1. Navigate to ****Audience > Lists & segments****.
2. Click ****Create New****.
3. Select ****Create segment****.
4. Add segment criteria (e.g., Person can or cannot receive marketing > can receive email marketing > because person subscribed AND What someone has done > Received email > at least once in the last 30 days).
5. Note the criteria count immediately below each criterion and the **Segment profiles** count at the top of the page.

![Segment profile counts highlighted](https://klaviyo.zendesk.com/hc/article_attachments/28720762560539)

## Preview segment profiles

To preview a selection of profiles who meet the criteria for a segment while you build it:

1. Navigate to ****Audience > Lists & segments****.
2. Click ****Create New > Create segment**** or select an existing segment and click ****Edit definition****.
3. Add segment criteria (e.g., Person can or cannot receive marketing > can receive email marketing > because person subscribed AND What someone has done > Received email > at least once in the last 30 days).
4. Click ****Preview details****.
   ![Preview details button](https://klaviyo.zendesk.com/hc/article_attachments/28720790991899)
5. In the sidebar that opens, you’ll see a summary of the segment’s estimated size as a proportion of all your profiles, plus a selection of sample profiles who meet your current criteria.
   ![Segment preview details](https://klaviyo.zendesk.com/hc/article_attachments/28720791001755)
6. Click any listed sample profile to explore their profile and understand why they qualify for the segment.

Segment counts at this stage in the creation process are estimates. There may be slight differences between the segment count shown here and your final segment size.

### Understanding segment counts

To understand how these numbers interact, think of your segment criteria like a Venn diagram. The number below each criterion indicates the number of people in that circle within the Venn diagram. The **Segment profiles** count reflects the number of profiles that are in the area where the Venn diagram circles overlap.

Your **Segment profiles** count cannot be larger than the smallest criterion count. It is also possible for your **Segment profiles** count to be 0, even if each criterion count is a large number.

Consider these examples:

- ****Person can or cannot receive marketing > can receive email marketing AND Person can or cannot receive marketing > cannot receive email marketing****
  In this example, the criteria are mutually exclusive. There are many profiles that can receive email marketing, and many profiles that cannot receive email marketing (indicated by the criteria counts for each row), but there is no one who meets both criteria, so the **Segment profiles** count is 0.
- ****Person can or cannot receive marketing > can receive email marketing AND What someone has done (or not done) > Placed order > at least once > in the last 30 days > where Collections contains Shoes****
  In this example, the criteria count for the first criterion is high, because there are many emailable profiles in the account. However, only a few people have placed an order in the last 30 days for items in the **Shoes** collection. The **Segment profiles** count is slightly smaller than the criteria count for the second criterion, because some shoe purchasers are unable to receive email (e.g., they are unsubscribed or suppressed).
