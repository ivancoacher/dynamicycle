<h1>How to create a tap-to-text sticker on Instagram</h1>

## You will learn

Learn how to create a tap-to-text (also called click-to-text) sticker for Instagram stories so that your followers can subscribe to SMS updates with just a few clicks.

Only those with a paid Klaviyo account and who have passed account verification can create a tap-to-text sticker.

****How the sticker will work****

When clicked, the sticker will:

1. Open up the individual’s messaging app
2. Automatically populate a message from Klaviyo that includes some type of subscribe keyword

All the person then needs to do is send this message, and they will opt in to your SMS marketing efforts. This makes it simple for you to gather SMS subscribers and grow your list.

## Before you begin

Before you get started, note that:

- You need to have [enabled hosted pages in your account](https://help.klaviyo.com/hc/en-us/articles/360057679192)
- Stickers are only available for Instagram stories, not posts

## Create a tap-to-text sticker for SMS

1. In Klaviyo, navigate to ****Hosted Pages**** in your account.

   - Note that this tab will only appear if you have already [enabled hosted pages](https://help.klaviyo.com/hc/en-us/articles/360057679192) for your account.
2. Under **Pages**, click the plus symbol ****(+)**** to add a new page.
3. Name this page (e.g., clicktotext.tmpl).
   ![Modal to name the new hosted page](https://klaviyo.zendesk.com/hc/article_attachments/28717994187803)
4. Click ****Add Page****.
   1. Add the following code snippet to the page:

      ```
      <html lang="en">
           <body>
              <script>
              var phone_number = 'Your SMS sending number'
              var message = "Text JOIN to sign up for texts"
              var sms_string = 'sms://'+phone_number+'?&body='+encodeURIComponent(message);
              location.replace(sms_string);
              </script>
         </body>
      </html>
      ```
5. Check that you’ve replaced “Your SMS Sending Number” with your Klaviyo sending number.

   - To find your Klaviyo sending number, go to ****Account > Settings > SMS****.![Example of a code snippet where the SMS sending number has been replaced](https://klaviyo.zendesk.com/hc/article_attachments/28717994198811)
6. Optional: replace JOIN with a [custom subscribe keyword](https://help.klaviyo.com/hc/en-us/articles/360050384091).
7. Click ****Preview****.
8. Copy the URL for the preview page.
9. Click ****Save****.
10. Log in to your Instagram account.
11. Swipe left to access the Instagram Story builder.
12. Take a new photo or click on the image selector icon in the bottom left to access your latest pics.

    - The image size should be 1080 x 1920 px, as a best practice.
    - The image should include [SMS disclosure language](https://help.klaviyo.com/hc/en-us/articles/4412878737051).
13. Click the ****sticker**** button on the top menu, which looks like a smiling face in a rounded square
    ![Example of image encouraging SMS signups along with disclosure language for Instagram story](https://klaviyo.zendesk.com/hc/article_attachments/28717988407323)
14. Select the ****Link**** sticker option
    ![Stickers options for an Instagram story](https://klaviyo.zendesk.com/hc/article_attachments/28717988409371)
15. Paste in the link you copied from the preview
16. Once added, click ****Done**** in the upper right
17. Optional: tap and drag to reposition the sticker
    ![Example of an Instagram story with a click-to-text sticker for SMS signups](https://klaviyo.zendesk.com/hc/article_attachments/28717994196507)
18. Click ****Your Story**** to post it to your story

## Outcome

Once the post is live, anyone who clicks the sticker will be able to easily text you and consent to SMS marketing. This makes it easier for you to grow your list of SMS subscribers, allowing you to directly reach more people.
