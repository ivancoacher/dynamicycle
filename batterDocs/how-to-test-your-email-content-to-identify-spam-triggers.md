<h1>How to test your email content to identify spam triggers</h1>

## You will learn

Learn how to find the content in your emails that is causing content to go to the spam folder or be blocked.

You should go through the content process only when you have ruled out all [other factors for emails going to spam](https://help.klaviyo.com/hc/en-us/articles/12034571748251), or it is only occurring on a specific message and no others.

## How to test content to identify spam triggers

To identify the content that is causing emails to go to spam, you can iteratively construct your email with a test send in between each piece of content to see what causes it to go to spam.

Testing content and its impact on delivery requires a test email account with the mailbox provider you are testing with.

Start by sending a blank email to check if something other than an email’s content is causing it to land in spam.

You can use the [email’s header](https://help.klaviyo.com/hc/en-us/articles/360002117891) to see information about the network path for the email and what may be causing it to go to spam. All emails have an email header and all email clients pull some key information from the header and display it in a user-friendly way. Here you can see whether email authentication issues may be causing it to go to spam, or if there are issues with the sender or recipient email itself.

![Example email header summary from Gmail](https://klaviyo.zendesk.com/hc/article_attachments/28722611917979)

If you are seeing emails go to spam when your email is blank, this is due to another reason rather than content.

If you don’t see any issues in your email header, take the following actions:

1. Remove all the words and links in your email template and perform a test send. This will test the HTML in the email to see if that may be causing placement issues.
2. If you don’t see any placement issues with the HTML in the email, you can start adding content paragraph by paragraph, with test sends in between. This allows you to iteratively check for words or phrases in your email that may be triggering inbox providers’ spam filters.
3. Once you have added all your desired text without any spam issues, add in your links one by one. This way you can see if any of the URLs are considered suspicious by the inbox provider and are causing the email to land in spam.
4. Finally, add in all of your images and ads one by one. This allows you to make sure any image repositories or 3rd party ads are not affecting your placement.
5. If you have identified a piece of content that is causing emails to go to spam, remove that section from future tests and continue testing. You want to make sure that you catch all potential causes.

## 3rd party tools

You can also use a 3rd party tool like [Litmus](https://www.litmus.com/spam-filter-tests) for content testing. Tools like Litmus allow you to preview your campaigns in different email clients, and run your email’s HTML code through a content scanner to identify any spam triggers and authentication failures.

See [how to export the HTML](https://help.klaviyo.com/hc/en-us/articles/115005085167) for an email template in Klaviyo.

## Additional content

[Troubleshooting why emails go to spam](https://help.klaviyo.com/hc/en-us/articles/12034571748251)

[Understanding why some preview emails go to spam](https://help.klaviyo.com/hc/en-us/articles/115005250468)
