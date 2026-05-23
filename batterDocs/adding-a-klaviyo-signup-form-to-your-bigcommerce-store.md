<h1>Adding a Klaviyo Signup Form to your BigCommerce Store</h1>

## Overview

This guide walks through syncing your BigCommerce signup form to a Klaviyo List.

If you don't have an existing sign up form in your store, or are otherwise interested in how to fully migrate existing subscriber lists and sign up forms to Klaviyo, explore the following two guides:

- [Redirect Existing Sign Up Forms to Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115005080167-Redirect-Existing-Sign-Up-Forms-to-Klaviyo)
- [Migrate Existing Subscribers (and Unsubscribes) into Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115005078487-Migrate-Existing-Subscribers-and-Unsubscribes-into-Klaviyo)


## Syncing a BigCommerce Form to a Klaviyo List

First choose a list to sync, then replace your BigCommerce signup form with a Klaviyo form by editing your BigCommerce theme source files.

1. From your BigCommerce dashboard, navigate to ****Storefront > My Themes****.
2. Now from your BigCommerce dashboard, navigate to ****Storefront Design > My Themes****.
3. From the **Current Theme box**, click the ****Advanced Settings dropdown**** and click ****Edit Theme Files****. This opens the web editor.
   ![bc_editTheme.png](https://klaviyo.zendesk.com/hc/article_attachments/28720845992987)

   #### Note

   If you're working with a default theme the option to **Edit Theme Files** will not appear. First make a copy of the theme, then make your edits to the copy. This is most likely the case if your new to BigCommerce or if you have never edited your default theme before.
4. Navigate to t**emplates > components > common > subscription-form.html**. Clicking ****subscription-form-html**** opens the file in the web editor.
   ![signupFormSubscriptionTemplate.png](https://klaviyo.zendesk.com/hc/article_attachments/28720891042587)
5. The next step is to replace the existing source code with a default Klaviyo form code. From your Klaviyo account, navigate to the list you want to sync to, and click the ****Sign Up Forms**** link.
6. Select the style of signup form you want to use, and copy the source code.
7. Switching back to your BigCommerce web editor, paste the Klaviyo signup form source code into the **subscription-form.html** file. You should paste over all of the existing source code.
   ![signupFormKlaviyoCode.png](https://klaviyo.zendesk.com/hc/article_attachments/28720845986843)
8. Click ****Save & Apply file****.

You can now check your storefront to verify that your new signup form has been added. Enter a test email address and confirm the subscription to verify that the signup from is working correctly.

From here you can edit the form's styles either in the Klaviyo UI or by editing the source code directly. Updating any styles in the UI updates the source code within the UI. You have to copy this source code and paste it into your **subscription-form.html** file to push these changes to your storefront.

## Troubleshooting

If you run into any issues with the form, remember that you're editing a copy of your original theme. All the original, unedited files can be accessed by applying your original theme, accessing the editor, and copying the source needed.
