---
id: 19097191216283
title: "How to use Wix contact labels to segment customers"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/19097191216283-How-to-use-Wix-contact-labels-to-segment-customers"
section: "Wix"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:56:45Z"
language: en
---

## You will learn

Learn how to use Wix contact labels to segment customers in Klaviyo. Wix contact labels are assigned as a list type [custom property](https://help.klaviyo.com/hc/en-us/articles/115005074627-Add-Custom-Properties-to-a-Contact-Profile#how-to-use-custom-properties) on each customer’s Klaviyo profile. These profiles sync into Klaviyo through your Wix integration.

## Before you begin

If you have not already, read our article on [Getting started with Wix](https://help.klaviyo.com/hc/en-us/articles/6202669053723) for step-by-step instructions on integrating, before continuing with this article.

## Segment people associated with a single Wix contact label

To create a segment of customers associated with a particular Wix contact label:

1. In Klaviyo, click the ****Audience**** dropdown and select ****Lists & segments****.
2. Click ****Create List/Segment,**** then select ****Segment****.
3. Name your segment.
4. Under **Definition**, choose ****Properties about someone > Wix Labels****.
5. The **Type** field will then automatically set to **List**.
6. Type the name of the label you'd like to use in the box after “**contains**.”
7. Click ****Create Segment****.
   ![Segment builder with segment Wix Label Subscribers](https://klaviyo.zendesk.com/hc/article_attachments/28717994667291)

## Segment people associated with multiple Wix contact labels

To create a segment of customers associated with multiple Wix contact labels:

1. In Klaviyo, click the ****Audience**** dropdown and select ****Lists & segments****.
2. Click ****Create List/Segment****, then select ****Segment****.
3. Name your segment.
4. Under **Definition**, choose ******Properties about someone > Wix Labels********.**
5. The **Type** field will then automatically set to **List**.
6. Type the name of the first tag you'd like to use in the box after “**contains**.”
7. Click ****And****.
8. Add another condition for each tag you would like to use, just like you did the first one.
9. Click ****Create Segment****.
   ![Segment builder with segment Wix Label Contacts and Subscribers](https://klaviyo.zendesk.com/hc/article_attachments/28718022424091)

## Segment people without a Wix contact label

You may want to create a segment of people who are not associated with a Wix contact label. To create this segment:

1. In Klaviyo, click the ****Audience**** dropdown and select ****Lists & segments.****
2. Click ****Create List/Segment**** and select ****Segment.****
3. Name your segment.
4. Under **Definition**, choose ****Properties about someone > Wix Labels******.**
5. Choose ****is empty**** as the option.
6. Click ****Create Segment.
   ![Segment builder with segment no wix label](https://klaviyo.zendesk.com/hc/article_attachments/28718022429723)****

## Use Wix contact labels in a flow filter

You can also use Wix contact labels within a flow filter, just like you did when building a segment. When editing the flow filter:

1. Select ******Properties about someone > Wix Labels > contains******.
2. Select the label you wish to use as your filter under “**Dimension value**”.
3. Make sure **Type** is set to ****Text****.
   ![Trigger setup in flow builder with dimension value dropdown open showing options such as contact, contacted me, subscribers, etc](https://klaviyo.zendesk.com/hc/article_attachments/28718022419739)

## Additional resources

- [Profile properties reference](https://help.klaviyo.com/hc/en-us/articles/115005074627-Add-Custom-Properties-to-a-Contact-Profile#how-to-use-custom-properties)
- [Getting started with flows](https://help.klaviyo.com/hc/en-us/articles/115002774932-Getting-Started-with-Flows)