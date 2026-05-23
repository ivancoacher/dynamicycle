<h1>Add a Klaviyo Embedded Form to a Shopify Free Theme</h1>

## Overview

This article covers adding a Klaviyo signup form to a Shopify store. We use each of Shopify's free themes as an example. Each theme includes a video overview of the process. If you don't see your theme here, or you're using a custom theme, we've also got [a section at the end of this guide that covers the basic process for adding a Klaviyo signup form to your Shopify store](https://help.klaviyo.com/hc/en-us/articles/115001618871#custom-theme10). You can also watch the videos below to understand the general approach.

Find your theme from the list below:

- [Brooklyn](https://help.klaviyo.com/hc/en-us/articles/115001618871#brooklyn)
- [Narrative](https://help.klaviyo.com/hc/en-us/articles/115001618871#narrative)
- [Supply](https://help.klaviyo.com/hc/en-us/articles/115001618871#supply)
- [Jumpstart](https://help.klaviyo.com/hc/en-us/articles/115001618871#jumpstart)
- [Debut](https://help.klaviyo.com/hc/en-us/articles/115001618871#debut)
- [Boundless](https://help.klaviyo.com/hc/en-us/articles/115001618871#boundless)
- [Pop](https://help.klaviyo.com/hc/en-us/articles/115001618871#pop)
- [Simple](https://help.klaviyo.com/hc/en-us/articles/115001618871#simple)
- [Minimal](https://help.klaviyo.com/hc/en-us/articles/115001618871#minimal)
- [Custom theme](https://help.klaviyo.com/hc/en-us/articles/115001618871#custom-theme10)

## Brooklyn

Adding a Klaviyo signup form to Shopify's free [Brooklyn theme](https://themes.shopify.com/themes/brooklyn/styles/classic).


## Narrative

Adding a Klaviyo signup form to Shopify's free [Narrative theme](https://themes.shopify.com/themes/narrative/styles/warm).


## Supply

Adding a Klaviyo signup form to Shopify's free [Supply theme](https://themes.shopify.com/themes/supply/styles/blue).


## Jumpstart

Adding a Klaviyo signup form to Shopify's free [Jumpstart theme](https://themes.shopify.com/themes/jumpstart/styles/jumpstart).


## Debut

Adding a Klaviyo signup form to Shopify's free [Debut theme](https://themes.shopify.com/themes/debut/styles/default).


## Boundless

Adding a Klaviyo signup form to Shopify's free [Boundless theme](https://themes.shopify.com/themes/boundless/styles/black-white).


## Pop

Adding a Klaviyo signup form to Shopify's free [Pop theme](https://themes.shopify.com/themes/pop/styles/bone).


## Simple

Adding a Klaviyo signup form to Shopify's free [Simple theme](https://themes.shopify.com/themes/simple/styles/light).


## Minimal

Adding a Klaviyo signup form to Shopify's free [Minimal theme](https://themes.shopify.com/themes/minimal/styles/vintage).


## Custom Theme

To add a Klaviyo signup form to a Shopify store we follow the same basic approach covered in the videos on each of Shopify's free themes above. This section covers the steps of this approach for users with custom themes that may not match the examples above exactly. That said, the basic process is similar, so use the videos above as a reference as needed.

1. In your Klaviyo account, find the list that you want customers who sign up to be added to. Click into the list, and click the ****Sign Up Forms**** tab.
2. Select the **Standard Embed** tab. You can edit your style settings on this screen. After you have edited your form, scroll to the bottom of the screen. Click into the code block to copy the form code.
3. Switch over to your Shopify store admin. Click ****Online Store**** and select ****Edit Code****from the **Actions** drop-down. This opens the Shopify web editor.
4. Next, scroll to the **Snippets** folder and click ****Add a new snippet****. Name your new snippet something like "klaviyo-form". Paste your Klaviyo form code into the new snippet, and click ****Save****. Your Klaviyo form code is now saved as a theme file in your Shopify store.
5. Next, we will reference your new snippet file in the footer of your store. Search for the `footer.liquid` file and click to open it in the web editor.
6. Find the area in your `footer.liquid` file where you want to add your form and reference your form with the following line of code, where "klaviyo-form" matches the name of your new snippet.
   `{% include 'klaviyo-form' %}`
7. The last step is to clean up any existing signup forms. First, scan the file for any existing `<form>` elements. If you find any, highlight the opening and closing form elements, and any code in between, and press `⌘ /` to comment out the code.
8. Search for any statements that include a default newsletter snippet. These will appear similar to the following:
   `{% include 'newsletter-form' %}`

After this, your form should be visible on your storefront in the footer. You can test the form by submitting an email address, opening and accepting the confirmation email from your inbox, and checking your list in Klaviyo to ensure the email address has been added to the list.
