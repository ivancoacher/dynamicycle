---
id: "360043506852"
title: "How to use anchor links in your messages and forms"
source_url: "https://help.klaviyo.com/hc/en-us/articles/360043506852-How-to-use-anchor-links-in-your-messages-and-forms"
section: "Design best practices"
category: "Content"
category_slug: "content"
klaviyo_updated: "2026-04-21T13:54:47Z"
language: "en"
---
## You will learn

Learn how to use anchor links to target your sign-up forms, or in email and SMS messages to direct visitors to a particular section of a webpage.

Anchor links are an easy way to create a personalized on-site experience for your customers coming from different emails, advertisements, or even in-person events. You can use anchor links in sign-up forms to target different lists and segments with relevant content. While anchor links are similar to UTM parameters, you will not be able to track customers as well as you can with UTM parameters. For more information on using UTM parameters, head to our article on [UTM Tracking in Klaviyo](https://klaviyo.zendesk.com/hc/en-us/articles/115005247808).

## How to create an anchor link

To create an anchor link, add in a # symbol followed by a few descriptive words. For instance, if you want a popup to trigger when someone clicks on a link in your email, indicating they are interested in hearing about a new product you are releasing, you can make an anchor link that looks like the following.

`https://www.example.com/#newproduct`

From there, you can add this URL to your messages and forms.

When someone navigates to the anchor link you created, they will land on the page without the anchor link (i.e., <https://example.com/> in the example above). ****Optional:**** You can add the HTML tag `<a id="newproduct"></a>` to your webpage's code (replace **newproduct** with your anchor name) if you'd like people who click the anchor link to be directed to a specific location within the page.

## How to add anchor links in messages

To use your anchor links in messages, add a URL like the one created above to your emails and SMS messages.

### Email

To add an anchor link in an email:

1. Add a text, images, or button block to your template
2. In the block's settings, add in the URL with the anchor link
3. Click ****Save****
   ![Button with anchor link](https://klaviyo.zendesk.com/hc/article_attachments/28716055426971)

If you want to track where a person clicks within your email to use later in segmentation, follow our article on [using buttons to collect information about your recipients](https://klaviyo.zendesk.com/hc/en-us/articles/115005255248).

### SMS

To add an anchor link in an SMS message, paste in a URL with your anchor link in the SMS editor. Note that if you choose to shorten your link, the anchor link will still work.

![SMS with anchor link](https://klaviyo.zendesk.com/hc/article_attachments/28716065955995)

## Using anchor links with sign-up forms

After you’ve created a way for your customers to reach your anchor link, you can use sign-up forms to customize the on-site content for each browser so that your brand seems more human.

Continuing with the example above, if someone clicks through the button in the email or the link in the SMS, the goal is to direct them to a full-page popup to sign up to receive information about a product release. In the sign-up form behavior, you can specify that you only want to display this form to people who click with this particular URL. To do so:

1. From the sign-up form builder, click ****Behaviors & Targeting****
2. Scroll down to the **Targeting** section
3. Check ****Only show on certain URLs****
4. Set the form to only appear on URLs ****Containing > [your anchor]**** (e.g., ****Containing > #newproduct****)
   ![Targeting form for anchor link](https://klaviyo.zendesk.com/hc/article_attachments/28716065958683)

Test your form before setting it live and come back to it to make sure it’s performing well.

## Additional resources

- [Guide to using QR codes to gather subscribers](https://academy.klaviyo.com/using-qr-codes-to-gather-subscribers)
- [Guide to optimizing your sign-up form experience](https://academy.klaviyo.com/creating-an-effective-acquisition-strategy-using-signup-forms)
- [Add to calendar event for a button, link, or image](https://klaviyo.zendesk.com/hc/en-us/articles/360043932991)