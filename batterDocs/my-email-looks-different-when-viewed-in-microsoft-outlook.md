<h1>My email looks different when viewed in Microsoft Outlook</h1>

## You will learn

Learn why some emails look different in Microsoft Outlook than other inboxes, as well as tips for improving consistency in how your messages render in Outlook.

## Outlook's rendering engines

While some versions of Outlook use Webkit (a modern browser engine that interprets and renders HTML in expected ways) to display emails, many others use Microsoft Word as a rendering engine.

Consider the last time you tried to make edits to a table or resize an image in Microsoft Word. The formatting challenges you face when using Word are similar to the challenges faced by emails in Outlook inboxes.

Because of this, an email may look slightly different in Outlook than when you initially design and preview in Klaviyo.

If you choose to optimize your emails for Outlook, use [Klaviyo's built-in inbox testing](https://klaviyo.zendesk.com/hc/en-us/articles/37463094051611) to preview your messages on various devices and inboxes.

## Optimize your emails for Outlook

You may see the following issues in Outlook:

- Background images in divs and table cells not supported or shown
- CSS float and position elements ignored
- Text shadow not supported or shown
- Unusual padding and margin, due to poor support for these elements
- CSS width and height not shown as intended, due to poor support for these elements
- Nested elements’ background colors shown incorrectly or ignored

Optimizing an email specifically for recent versions of Outlook can take a lot of time and extensive testing, as there are no established guidelines. Doing this also requires making significant changes to how images are positioned, and this can skew how emails render across other email clients and devices.

### Sizing images for Outlook

A common problem in Outlook inboxes is images that become stretched or oversized. To avoid this, set a width for every image in your template.

1. Select an image block.
2. Add a number to the **Image layout > W** field. For full width images, use 600 px (or whatever width your email is set to, found in the **Styles** section).
   ![](https://klaviyo.zendesk.com/hc/article_attachments/32083288343067)
3. Save your changes.

### GIFs in Outlook

Outlook does not support GIFs in emails. Rather than displaying a moving image, Outlook will select the first frame of your GIF and display it as a static image.

## Understand Outlook’s impact on your audience

To see what percentage of your audience is opening your emails using Outlook:

1. Navigate to the ****Campaigns**** tab in Klaviyo.
2. Click a recently-sent campaign.
3. Click the ****Deliverability**** tab of the campaign’s summary.
4. Review the **Performance By Email Domain** section to see the percentage of recipients who interacted with your message using Outlook.

## Additional resources

- [How to use images in emails](https://help.klaviyo.com/hc/en-us/articles/115005253688-How-to-use-images-in-emails)
- [How to optimize your emails for mobile](https://help.klaviyo.com/hc/en-us/articles/115005254428-Optimize-Your-Emails-for-Mobile)
- [Understanding CSS optimization](https://help.klaviyo.com/hc/en-us/articles/360049848692-Understanding-CSS-Optimization-)
