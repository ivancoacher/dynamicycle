---
id: "115005255868"
title: "How to set up GoFundMe Pro campaigns and flows"
source_url: "https://help.klaviyo.com/hc/en-us/articles/115005255868-How-to-set-up-GoFundMe-Pro-campaigns-and-flows"
section: "Classy"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:25Z"
language: "en"
---
## You will learn

Learn how to set up GoFundMe Pro campaigns and flows in order to personalize and target emails based on each supporter's contribution, fundraising, and web activity.

## Before you begin

Before reading this article, make sure you've [integrated with GoFundMe Pro](https://help.klaviyo.com/hc/en-us/articles/115005083387--NEEDS-VIDEO-Integrate-with-Classy). If you have any other platforms you’d like to integrate with Klaviyo (e.g. Salesforce, Eventbrite, etc.), you can find them on our [app marketplace](https://marketplace.klaviyo.com/en-us/).

## Set up segments

Dynamic segments are one of the most powerful features of the Klaviyo platform, and they provide an easy way for your organization to start saving time and raising more money.

Klaviyo's segment builder can be used to quickly slice and dice your contacts based on activity and behavior. For example, you can easily build a segment of everyone who has donated, or get more targeted and capture those who gave only during a specific timeframe or part of a specific campaign. You can also build segments of those who have opened/clicked a specific email, everyone who has created a fundraising page, everyone that has hit a specific fundraising milestone, etc. To learn more about segments, check out our guide to [getting started with segments](https://help.klaviyo.com/hc/en-us/articles/115005237908).

## Add a sign-up form

Klaviyo's sign-up forms are easy to use, highly customizable forms that can be added directly to your website to help you grow your lists.

For each list in Klaviyo, there is a dedicated sign-up form builder that allows you to customize the styling for various types of sign-up forms.

As a starting point, check out our [guide to building your audience with sign-up forms](https://help.klaviyo.com/hc/en-us/articles/115005080327-Build-your-Audience-with-Sign-Up-Forms).

## Start sending campaigns

Now that you’ve setup your Klaviyo account, it’s time to start sending - you can turn automated email flows live, and also start scheduling and sending regular campaigns.

A campaign is a one-time send to a pre-established target group of contacts - think regular newsletters about your organization's work, news about an upcoming fundraiser, or special announcements.

Getting started with campaigns could not be easier - learn about [how to create and send an email campaign](https://help.klaviyo.com/hc/en-us/articles/115005054847-Introduction-to-Campaigns).

## Set up automated flows

You may be familiar with the terms Drip Campaign, Autoresponder, or in general, Marketing Automation. In Klaviyo, we call these types of emails "flows". A flow is an automated series of emails triggered by an event.

For GoFundMe Pro customers, Klaviyo provides a number of pre-built email flows that can help you quickly get started with automated sending, such as the Fundraising Milestone flow and the Donor Re-engagement flow. Read on to learn more about these two flows.

### Create a fundraising milestone flow

Peer-to-peer fundraising has become a staple for nonprofits. One of the challenges with peer-to-peer fundraising, however, is helping your supporters engage their networks effectively. Because your supporters are likely not professional fundraisers, providing them with structure and guidance to help them reach their goals can lead to a greater rate of success. As time goes on in a supporter's journey, a Fundraising Milestone flow can help encourage fundraisers to stay active and motivated.

Once a supporter has created a Fundraising Page and has started to raise funds towards his/her goal, you can reach out to both congratulate the supporter and provide additional advice. You could also consider offering a prize for reaching a certain fundraising milestone.

Once you integrate your GoFundMe Pro account with Klaviyo, a number of pre-built flows will automatically populate into your account, including the Fundraising Milestone Flow. You can check out all of your flows [i](https://www.klaviyo.com/flows)n the [Flows tab](https://www.klaviyo.com/flows).

For the Fundraising Milestone Flow, the trigger for the flow is **Raised Contribution.** The flow filter, however, is designed to establish a certain milestone threshold for the flow.

Let’s use $100, $500, and $1000 as milestone examples:

|  |  |  |
| --- | --- | --- |
| Milestone | Trigger Filter | Flow Filters |
| Milestone 1 - $100 | Raised Contribution | - Has Raised Contribution Value is at least $100 since campaign start date - Has Raised Contribution is less than $500 since campaign start date |
| Milestone 2 - $500 | Raised Contribution | - Has Raised Contribution Value is at least $500 since campaign start date - Has Raised Contribution Value is less than $1000 since campaign start date |
| Milestone 3 - $1000 | Raised Contribution | - Has Raised Contribution Value is at least $1000 since campaign start date |

As you can see, two filters are needed to create a given milestone threshold - an "at least" filter and a "is less than" filter.

Klaviyo's default Fundraising Milestone flow will come with the following filters:

- Has **Raised Contribution Value**is at least 100 over all time
- Has **Raised Contribution Value**is less than 500 over all time
- Has not been in this flow over all time

The last filter is there to ensure that each fundraiser only gets these emails once for a specific milestone. You will want to adjust the two filters regarding the milestone thresholds so that instead of **over all time**, you specify the start date of your campaign.

Our pre-built flow consists of two emails, but you can add or delete as many emails to the series as you want. For the first email, we recommend congratulating your supporter on hitting a milestone, while subsequent emails can provide tips and words of encouragement to help him/her reach the next milestone. To get you started, Klaviyo has setup two example emails for you:

- Email #1 is scheduled to go out 1 hour after someone has reached a milestone. This email will both congratulate the fundraiser on reaching a goal and provide information on what the organization can accomplish with those funds. If you give rewards for milestones, this email is where you would give that reward.
- Email #2 Is scheduled to go out 3 days later and will provide best practice tips to help your fundraiser reach the next milestone. If you give rewards for milestone successes, you can motivate your fundraiser by including a picture or description of the next reward.

To build out your series even further, you can clone Email #2 and swap in new content to provide tips every few days or weeks - this can help keep your fundraisers engaged and motivated!

Klaviyo's pre-built templates are designed to include the following:

- Dynamic Content: Content that’s specific to the person receiving the email. For example, First Name, campaign name, and a link back to the supporter's Fundraising Page.
- Fundraising Tips: We have some suggestions of fundraising tips, but recommend customizing the content to reflect your organization and the tips you believe will be most helpful and relevant for your audience. Consider using inspiring pictures and GIFs!

After you’ve created the content for each email in your series, the final step is setting the status of each email to **Live**. For each email in your flow, you'll see a colored icon with a paper airplane inside of it. This icon signals the flow email's status.

Once **Live**, each fundraiser will automatically get scheduled for all emails in the flow when they meet the flow criteria for the first time. Emails will then send automatically based on the scheduled timing you've established.

### Create a donor re-engagement flow

To learn about this flow, read our article about [how to create a donor re-engagement flow](https://klaviyo.zendesk.com/hc/en-us/articles/115002775292).

## Outcome

You've now learned how to set up a sign-up form, and how to use your GoFundMe Pro data in Klaviyo segments, campaigns, and flows.

## Additional resources

- [Getting started with Classy](https://klaviyo.zendesk.com/hc/en-us/articles/115005083387)
- [Getting started with flows](https://klaviyo.zendesk.com/hc/en-us/articles/115002774932)