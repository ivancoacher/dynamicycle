<h1>Sync a Shopify Signup Form to a List in Klaviyo</h1>

## Overview

This guide covers syncing your Shopify signup form to a list in your Klaviyo account. We use Shopify's 10 free themes as examples. If you plan to use this method to sync a form from a customized theme, keep in mind that if you edited your signup form, you may need to edit some of the items in the code snippet used below.

#### Learn more

We also have a guide for [adding a Klaviyo form to all of Shopify's free themes](https://help.klaviyo.com/hc/en-us/articles/115001618871-Add-a-Klaviyo-Form-to-a-Shopify-Free-Theme).


The snippet that you add to your Shopify `theme.liquid` file is slightly different depending on your theme. Choose your theme from the list below, and follow the respective instructions. You can also check out our section on [using a custom theme](https://help.klaviyo.com/hc/en-us/articles/115002451292#using-a-custom-theme) if you don't see your theme on the list below.

|  |  |
| --- | --- |
| [Themes with jQuery 3.2.1 or higher](https://help.klaviyo.com/hc/en-us/articles/115002451292#shopify-themes-that-include-jquery-3-2-1-or-higher) | [Themes with a jQuery version < 3.2.1](https://help.klaviyo.com/hc/en-us/articles/115002451292#shopify-themes-with-a-jquery-version-lower-than-3-2-1-or-no-jquery) |
| - Brooklyn - Supply - Jumpstart - Pop - Simple | - Minimal - Narrative - Debut - Venture - Boundless |

## Shopify Themes That Include jQuery 3.2.1 or Higher

Use the following snippet to sync your Shopify signup form to a list in your Klaviyo account. Remember to update the list id in the snippet. The basic process is as follows:

1. From your Shopify admin click ****Online Store****, and then from the **Actions** dropdown click ****Edit Code**** to open your web editor.
2. Open your `theme.liquid` file and paste in the code snippet below. Paste the snippet before the closing `</body>` tag.

   ```
   <script type="text/javascript">
       $("input[name='contact[email]']").on('blur', function(e) {
           e.preventDefault();
           var email = $(this).val();
           var settings = {
               "async": true,
               "crossDomain": true,
               "url": "https://manage.kmail-lists.com/subscriptions/external/subscribe",
               "method": "POST",
               "headers": {
                   "content-type": "application/x-www-form-urlencoded",
                   "cache-control": "no-cache"
               },
               "data": {
                   "g": "LIST_ID",
                   "$fields": "$source",
                   "email": email,
                   "$source": "Shopify form"
               }
           };
           $.ajax(settings).done(function (response) {
               console.log(response);
           });
       });
   </script>
   ```
3. From your Klaviyo account, select the list you want to sync and copy the [list id](https://help.klaviyo.com/hc/en-us/articles/115005078647-Find-a-List-ID).
   ![listID.png](https://klaviyo.zendesk.com/hc/article_attachments/28716062299547)
4. From your Shopify account, add the list id to the code snippet in your `theme.liquid` file. At this step, you can also [modify the $source of this form if you'd like](https://help.klaviyo.com/hc/en-us/articles/115002451292#modify-the--source-of-your-form).
   ![shopifyDefaultFormListid.png](https://klaviyo.zendesk.com/hc/article_attachments/28716062302107)
5. Save your updated `theme.liquid` file.

You can now test your signup form to ensure that it is working. First, enter your email address into the form. Next, check your inbox and confirm your subscription with the opt-in email. Last, search for your email address in your Klaviyo account to confirm that your profile has been added.

If you continue to experience any difficulties please [contact our support team](https://help.klaviyo.com/hc/en-us/articles/115001002272-How-to-Contact-Support).

## Shopify Themes With a jQuery Version Lower than 3.2.1 or no jQuery

Use the following snippet to sync your Shopify signup form to a list in your Klaviyo account. Remember to update the list id in the snippet. The basic process is as follows:

1. From your Shopify admin click ****Online Store****, and then from the **Actions** dropdown click ****Edit Code**** to open your web editor.
2. Open your `theme.liquid` file and paste in the code snippet below. Paste the snippet before the closing `</body>` tag.

   ```
   <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
   <script>var $KL = jQuery.noConflict(true);</script>
   <script type="text/javascript">
       $KL("input[name='contact[email]']").on('blur', function(e) {
           e.preventDefault();
           var email = $KL(this).val();
           var settings = {
               "async": true,
               "crossDomain": true,
               "url": "https://manage.kmail-lists.com/subscriptions/external/subscribe",
               "method": "POST",
               "headers": {
                   "content-type": "application/x-www-form-urlencoded",
                   "cache-control": "no-cache"
               },
               "data": {
                   "g": "LIST_ID",
                   "$fields": "$source",
                   "email": email,
                   "$source": "Shopify form"
               }
           };
           $KL.ajax(settings).done(function (response) {
               console.log(response);
           });
       });
   </script>
   ```
3. From your Klaviyo account, select the list you want to sync and copy the [list id](https://help.klaviyo.com/hc/en-us/articles/115005078647-Find-a-List-ID).
   ![listID.png](https://klaviyo.zendesk.com/hc/article_attachments/28716062299547)
4. From your Shopify account, add the list id to the code snippet in your `theme.liquid` file. At this step, you can also [modify the $source of this form if you'd like](https://help.klaviyo.com/hc/en-us/articles/115002451292#modify-the--source-of-your-form).
   ![shopifyDefaultFormListid.png](https://klaviyo.zendesk.com/hc/article_attachments/28716062302107)
5. Save your updated `theme.liquid` file.

You can now test your signup form to ensure that it is working. First, enter your email address into the form. Next, check your inbox and confirm your subscription with the opt-in email. Last, search for your email address in your Klaviyo account to confirm that your profile has been added.

If you continue to experience any difficulties please [contact our support team](https://help.klaviyo.com/hc/en-us/articles/115001002272-How-to-Contact-Support).

## Using a Custom Theme

If you're using a custom theme you first have to verify the version of jQuery that your theme uses, then select a code snippet accordingly. As well, if your theme has modified the standard Shopify signup signup form, you will need to modify the snippet so that it is targeting the email input element with the correct id.

1. Navigate to your site and open the console of your web browser (if you're using Chrome on a Mac you can press `⌥`-`⌘`-`J).`
2. The following command returns the current version of jQuery on your site: `$.fn`.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28716051920923)
3. If your jQuery version is 3.2.1 or higher, you can use the instructions in the section for [Shopify Themes That Include jQuery 3.2.1 or Higher](https://help.klaviyo.com/hc/en-us/articles/115002451292#shopify-themes-that-include-jquery-3-2-1-or-higher).
4. If your jQuery version is lower than 3.2.1, you can use the instructions in the section for [Shopify Themes With a jQuery Version Lower than 3.2.1](https://help.klaviyo.com/hc/en-us/articles/115002451292#shopify-themes-with-a-jquery-version-lower-than-3-2-1).

If you continue to experience any difficulties please [contact our support team](https://help.klaviyo.com/hc/en-us/articles/115001002272-How-to-Contact-Support).

## Modify the `$source` of Your Form

In the default snippets on this page, you can modify the line with `$source": "Shopify form"` if you'd like to change the `$source` property that appears on your customer's profiles within Klaviyo. Change only the value of this expression. For example, updating to `“$source”: “Homepage form”` will set a user's `$source` on their profile as follows:

![](https://klaviyo.zendesk.com/hc/article_attachments/28716051912347)

Take care when modifying elements of this form. If you find your form is not working correctly, contact customer support or try adding the form from scratch using the default code snippets in this article.
