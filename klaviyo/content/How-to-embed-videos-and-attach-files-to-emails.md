---
id: 115005256968
title: "How to embed videos and attach files to emails"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005256968-How-to-embed-videos-and-attach-files-to-emails"
section: "Getting started with templates"
category: "Content"
category_slug: "content"
klaviyo_updated: "2026-04-21T13:54:25Z"
language: en
---

## You will learn

Learn about the types of content that can be embedded in an email, and how to avoid deliverability issues caused by embedding unsupported content.

## About embedded content and attachments

Most major email clients (such as Gmail) view embedded content such as surveys, forms, videos, and other widgets as a security threat. These email clients will often strip out this embedded code completely and your recipients will not see your content rendered when they open your email.

Klaviyo is committed to setting our customers up for success. Because our testing shows that these features do not reliably render across all major email clients, we don't support embedded surveys, forms, videos, or widgets inside of Klaviyo emails.

That said, there are a few ways you can ensure good deliverability and still provide your email subscribers access to exclusive content.

- Learn how to [deliver video content via email](https://help.klaviyo.com/hc/en-us/articles/115005256968#h_01J4MDQQ0XMJC9HQXDRCCBNKY5)
- Learn how to [deliver attachments and files via email](#h_01HE3NARPVQ7PVM7SA1TJJ2AFM)
- Learn how to [initiate surveys via email](#h_01HE3NARPWVVV8CE6YS2H1Z3X0)

## Deliver video via email using a block

Using a static image with a play button is the most common (and recommended) way to feature a video in an email. That image should link to a hosted version of your video (e.g., a video hosted on Youtube or Vimeo). Klaviyo offers a video block to make this process simple.

1. Copy a video’s URL (e.g., from Youtube, TikTok, Vimeo, or another video hosting platform).
2. Open an email template in Klaviyo.
3. Drag a ****Video**** block into the email.
   ![The video block icon](https://klaviyo.zendesk.com/hc/article_attachments/28723629942427)
4. Paste the video URL into the **Video URL** field.
5. For the video’s thumbnail:
   1. If you use Youtube to host your video, Klaviyo automatically detects the video thumbnail. Note that automatic thumbnail detection is not supported for Youtube Shorts, only standard Youtube videos.
   2. If your video is hosted anywhere else, click ****Select image**** to upload a thumbnail.
      ![The option to upload a thumbnail image](https://klaviyo.zendesk.com/hc/article_attachments/28723624611995)
6. Adjust the block’s appearance, including toggling the play button on or off and changing block padding in the block’s ****Styles**** tab.

When someone opens your email, they’ll see an image that looks like a video player. When they click it, they’ll be redirected to a webpage where the video will play automatically.

### Add a GIF

If the video clip you’d like to share is short and doesn’t have sound, try a GIF instead. Animated GIFs work in emails as long as they are less than 5 MB in size. You can upload a GIF just as you would upload a JPEG or PNG, by dragging it into your email template.

![A gif in Klaviyo's email editor](https://klaviyo.zendesk.com/hc/article_attachments/28723624605467)

## Include attachments in an email

To include an attachment like a PDF, Word document, or Google document in an email, you’ll first need to host your file online, like on your website, in Google Drive, or in Dropbox. After uploading the file to your content management system, copy a link to the document.

To access a sharing link to a document in Google Drive:

1. Click the **More options** icon (three dots) in the top-right corner of the item’s card, or on the far right if using list view.
2. Open the ****Share**** menu.
3. Click ****Copy link****.
   ![A Google Drive file with the menu open to copy the public link](https://klaviyo.zendesk.com/hc/article_attachments/28723624608283)
4. To ensure your file is visible to recipients, reopen the menu, then click ****Share > Share**** and set the permissions to ****Anyone with the link**** and ****Viewer****.

Then, insert the link in your email. You can add the link to almost any element in an email, including:

- A CTA button
- An image
- Text in a text block

Learn more about [using the email editor](https://help.klaviyo.com/hc/en-us/articles/4407911841435).

## Initiate a survey with an email

Most survey platforms offer a way to pre-populate the first question in a survey based on a button clicked by the recipient. Learn how to [use links to preselect an answer in a Typeform survey](https://www.typeform.com/help/a/preselect-answers-through-typeform-links-for-advanced-users-4410202791060/).

Once you’ve generated these links through your survey platform, add a corresponding button to your email for each answer option. For example, if your email asks “Are you satisfied with your purchase?”, you can add buttons to your email that say “Very satisfied,” “Somewhat satisfied,” and “Unsatisfied.” Then add the corresponding link to each button. When a recipient clicks a button, they will see a survey with their answer automatically selected.