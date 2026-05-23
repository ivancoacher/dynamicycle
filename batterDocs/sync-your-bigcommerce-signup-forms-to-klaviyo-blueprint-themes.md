<h1>Sync Your BigCommerce Signup Forms to Klaviyo - Blueprint Themes</h1>

## Overview

This guide walks through syncing your BigCommerce signup form to a Klaviyo List.

## Syncing a BigCommerce Form to a Klaviyo List

First choose a list to sync, then replace your BigCommerce signup form with a Klaviyo form by editing your BigCommerce theme source files.

1. From your BigCommerce dashboard, navigate to ****Storefront > My Themes****.
2. From the Current Theme, click the ****Edit HTML/CSS**** link. This opens the web editor.
   ![bc_editBPtheme.png](https://klaviyo.zendesk.com/hc/article_attachments/28722594733467)
3. Navigate to the ****Other Template Files > Panels**** and click on the ****SideNewsletterBox********.html**** file. This loads the SideNewsletterBox.html file into the web editor.
   ![bc_BPsideNewsletterBox.png](https://klaviyo.zendesk.com/hc/article_attachments/28722556305947)
4. The next step is to replace the existing source code with a default Klaviyo form code. From your Klaviyo account, navigate to the list you want to sync to, and click the ****Sign Up Forms**** link.
5. Select the style of signup form you want to use, and copy the source code.
6. Switching back to your BigCommerce web editor, paste the Klaviyo signup form source code into the **SideNewsletterBox.html** file. You should paste over all of the existing code.
   ![blueprintSignupFormKlaviyoCode.png](https://klaviyo.zendesk.com/hc/article_attachments/28722594738331)
7. Click ****Save****.

You can now check your storefront to verify that your new signup form has been added. Enter a test email address and confirm the subscription to verify that the signup from is working correctly.

From here you can edit the form's styles either in the Klaviyo UI or by editing the source code directly. Updating any styles in the UI updates the source code within the UI. You have to copy this source code and paste it into your **subscription-form.html** file to push these changes to your storefront.

## Troubleshooting

If you run into any issues with the form you can revert to the original form of your BigCommerce theme files by clicking ****Revert to Original.****

![647770](https://klaviyo.zendesk.com/hc/article_attachments/28722594729755)
