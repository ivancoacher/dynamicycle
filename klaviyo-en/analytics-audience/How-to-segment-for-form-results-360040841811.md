---
id: "360040841811"
title: "How to segment for form results"
source_url: "https://help.klaviyo.com/hc/en-us/articles/360040841811-How-to-segment-for-form-results"
section: "Segment examples and types"
category: "Audience"
category_slug: "analytics-audience"
klaviyo_updated: "2026-04-21T13:54:48Z"
language: "en"
---
## You will learn

Learn how to create segments to see who submits your Klaviyo forms and how they responded. By creating and analyzing the right segments, you can glean information about who enters your account through Klaviyo forms. This information will show you which forms work best for your audience, and allow you to analyze customer behavior and properties over time.

## Segment for form identification with the $source hidden field

Hidden fields are [properties](https://klaviyo.zendesk.com/hc/en-us/articles/115005074627) that you add to a Klaviyo form that customers do not see. They are attached to the submit button and typically collect information on form content or their locations on your site. How you name your hidden field property is how you identify these characteristics, and by default, all forms have the $source hidden field (which is the name of the form itself).

The most important forms to enable on your site are ones that link to and fuel your general list of customers, such as a newsletter list. To see who is currently a subscriber and entered via a specific form:

1. Click ****Audience**** in the Klaviyo sidebar.
2. Choose ****Lists & Segments****.
3. Click ****Create List / Segment****.
4. Select ****Segment****.
5. Create a segment with the following definition:
   ****If someone can or cannot receive marketing > can receive > [channel] marketing
   Because person > subscribed
   And subscribe method is > Klaviyo form > [your form name]
   ![Subscribed via form](https://klaviyo.zendesk.com/hc/article_attachments/28711698878363)****

Here, the source form is **Multi-step email & SMS**. It takes on the name of your form to identify the avenue through which the profile entered into Klaviyo. If you have multiple forms leading to a single list (such as a popup and an embed) that you want to include in this segment, add both sources separated by an OR condition.

## Segment for form results with profile properties

You can likewise create segments to view form results that have several response options if, for example, you have a form that collects survey responses. To do this, segment using profile properties that are attributed to these results. [Profile properties](https://klaviyo.zendesk.com/hc/en-us/articles/115005074627) are bits of information about the profiles in your account, and are categorized in two ways:

- ****Klaviyo properties****
  Properties that are pre-constructed in Klaviyo (e.g., **Email**, **Address**, **First Name**, etc.)
- ****Custom properties****
  Properties that you customize yourself

For example, say you run a bakery and want to target customers with content that specifically appeals to them. You can set up a form asking customers if they like chocolate, vanilla, or both.

When someone fills out this form, these preferences will save as profile properties that you can then use to segment. If you want to target customers who prefer chocolate, then your segment would look something like this:

![Favorite flavor chocolate](https://klaviyo.zendesk.com/hc/article_attachments/28711677443483)

Use this segment to analyze your customer preferences, and then send them content that directly applies to them. This allows you to fully own your marketing and connect with your customers.

## Additional resources

- [Profile properties reference](https://klaviyo.zendesk.com/hc/en-us/articles/115005074627)
- [Advanced segmentation reference](https://klaviyo.zendesk.com/hc/en-us/articles/360035312491)
- [Getting started with signup forms](https://help.klaviyo.com/hc/en-us/articles/360026474752)