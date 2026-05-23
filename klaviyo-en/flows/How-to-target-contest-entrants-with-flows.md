---
id: 360036881312
title: "How to target contest entrants with flows"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360036881312-How-to-target-contest-entrants-with-flows"
section: "Lifecycle flows"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-04-21T13:54:46Z"
language: en
---

## You will learn

Learn about best practices for marketing to contest subscribers as well as tagging contest entrants in order to add them to a welcome series.

Contests, sweepstakes, and giveaways attract a lot of sign-ups and can be a quick way to grow your list. However, many of those who opt in expect to only receive information about these events, and might not be interested in being part of your general list. It’s important to keep these subscribers separated from your main list until they confirm their interest.

SMS marketing for sweepstakes is only permitted on US and Canadian short codes. Learn more about [compliance requirements around sweepstakes and contests](https://help.klaviyo.com/hc/en-us/articles/31921649483803).

## Tag contest entrants

The best option for targeting contest entrants in a welcome series is to tag these subscribers and then create a separate list and flow for them. This approach works well regardless of whether you are using Klaviyo or a third-party service or product to run your contest and grow your list.

While you could use tags to separate contest entrants in an existing welcome series, anyone who previously went through this flow wouldn’t go through it again (since people can only go through a list-triggered flow once). For instance, if someone signed up for your email list, and later signed up for a contest, they wouldn’t get the welcome emails for the contest as expected.

## Add contest entrants to a new list

To add entrants to a new list:

1. Click the ****List & Segments**** tab and then ****Create List / Segment > List.****
2. Name the list something descriptive (e.g., Contest Participants).
3. Set your sign-up form to send entrants to this list.

## Tag contest entrants using a sign-up form

The steps below apply to Klaviyo sign-up forms. If you are using a third-party sign-up form, follow their documentation to add identifying or hidden properties.

You can design a sign-up form from scratch or use a template from the Sign-up Form Library, but either way, you can customize the content to suit your brand and contest. When creating a sign-up form, consider how you want to contact entrants and include a text input for an email address and/or phone number.

![Example of a contest form in the form builder.](https://klaviyo.zendesk.com/hc/article_attachments/28717992339867)

In addition, you need a button to submit the form and tag the entrants.

1. From the form builder overview, click ****Add Blocks****.
2. Drag a button onto the form in the form builder.
3. Under **Button Click Action**, change the action to ****Submit Form******.**
4. Choose the list that triggers your welcome series flow.
5. To tag contest subscribers, add a new or select an existing profile property under **Submit Hidden Fields** and give it a value. In this case, the profile property is **Contest** and the value is **Contest Entrant**.

It is a best practice to always tag profiles with source information, as if someone unsubscribes from a list, you may lose context about how they got into Klaviyo.

![Example of a contest form with a subscribe button.](https://klaviyo.zendesk.com/hc/article_attachments/28717992341019)

In addition, add a note to say that submitting this form will opt in the contact to general marketing. Including this message means that you will be able to add engaged entrants to your main list.

## Create a flow for contest entrants only

Next, create a welcome series flow based on this list. You can create a flow from scratch, by using a template from the Flow Library, or by cloning another flow. The last of these is the easiest option if you have already set up a welcome series flow. Simply copy it from the Edit Flow dropdown menu by clicking ****Clone Flow****. Change the name to be more descriptive and set the trigger to be the list you created for your contest.

![Video showing the steps to clone a flow.](https://fast.wistia.com/embed/medias/wx2x4i0y30/swatch)

Create or change the content and timing of the messages by following the best practices mentioned at the top of this article.

## Best practices for crafting content for contest entrants

Keep in mind that these subscribers originally signed up for information about a specific contest, giveaway, or sweepstakes, so not everyone will be as invested as someone who signed up for your general list. To help prevent those who are less engaged from hurting your deliverability, there are a few best practices you can follow:

- Reduce the number of messages in your welcome series (to avoid overloading these subscribers)
- Send messages that offer high-quality content and avoid those that sell products/services
- Include a noticeable unsubscribe link in all emails
- Remind recipients why they are receiving these messages (e.g., because they signed up for a certain contest)

For the first message in this series, it is a good idea to say “thank you”, and to include details about the contest, giveaway, or sweepstakes. Doing so can not only serve as a reminder about why the recipient has received this message (so they know it's not spam) but also help manage their expectations about when they will receive more information.

In addition, remember that many contest entrants might have already gone through your regular welcome series. Adjust your content so that it is different enough to still provide value to those who received similar messages from your regular flow.

## Add engaged entrants to your list

After this series nurtures contest entrants, you can segment them and add engaged entrants to your main list. A best practice is to wait until the contest is over, before setting up the segment.

1. Navigate to the ****List & Segments**** tab.
2. Click ****Create List / Segment > Segment****.
3. Add the following conditions to include only highly engaged contest entrants, typically opened 50% of emails in the contest welcome flow. Here, there are 6 emails in the series, so the segment is set to **Opened Email is at least 3 over all time**.
   ![Example configuration for an engaged contest entrants segment.](https://klaviyo.zendesk.com/hc/article_attachments/28717986522011)
4. [Export the segment](https://help.klaviyo.com/hc/en-us/articles/115005078687) and then [import it into your main list](https://help.klaviyo.com/hc/en-us/articles/115005251128). By only including the most engaged users, you can more safely grow your subscriber list.
5. For those who are more unengaged, create a segment of those who have opened less than 3 emails in your contest Welcome series.

## Additional resources

- Read more about flows:
  - [A/B testing a flow emails](https://help.klaviyo.com/hc/en-us/articles/6960371049115)
  - [Manage emails within a flow](https://help.klaviyo.com/hc/en-us/articles/115002779271)
- Learn more about [tags in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/360025834271)