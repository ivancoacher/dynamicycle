---
id: 18229698831003
title: "How to add a Klaviyo embed form to your Square Online site"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/18229698831003-How-to-add-a-Klaviyo-embed-form-to-your-Square-Online-site"
section: "Square"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:31Z"
language: en
---

## You will learn

Learn how to add a Klaviyo embed form to your Square Online site, which requires creating a form in Klaviyo, and then pasting its embed code into your site’s files where you want it to appear (e.g., the footer).

## Before you begin

Before creating an embed form in Klaviyo, make sure you've integrated Klaviyo with Square and set up onsite tracking to enable sign-up form functionality. If you checked the setting **Automatically add Klaviyo onsite JavaScript** when [integrating with Square](https://help.klaviyo.com/hc/en-us/articles/11117215837211), you’re all set.

If not:

1. In Klaviyo, select the ****Integrations**** tab.
2. Click on ****Square****.
3. Check the setting **Automatically add Klaviyo onsite javascript**.
4. Click ****Save****.

## Add the form's embed code to your site

First, create and publish your embed form in Klaviyo. This section will go over the next steps of pasting your form's embed code on your Square Online site so it displays and syncs data properly.

1. Navigate to your Square Online dashboard.
2. Click ****Website > Edit Site****.
3. Open to the page where you’d like to embed the form.
4. Select ****Add Section > Embed code****, then click ****Add****.
5. Copy the following script and paste it into the **Code** box:

   ```
   <script type="text/javascript" src="https://static.klaviyo.com/onsite/js/PUBLIC_API_KEY/klaviyo.js"></script>
   ```
6. In the code you just pasted, replace PUBLIC\_API\_KEY with your [Klaviyo public API key.](https://help.klaviyo.com/hc/en-us/articles/115005062267#find-your-api-keys2)
   - To find your public API key, navigate to ****Settings > API keys**** in Klaviyo. This is a 6-character code, also referred to as your "account ID."
7. Navigate back to Klaviyo and copy your form's embed code from the **Targeting & behaviors** tab within the form editor.
   ![An example form's embed code highlighted to copy from the Targeting and behaviors tab of the form editor.](https://klaviyo.zendesk.com/hc/article_attachments/32015281228443)
8. In Square, paste the embed code in the **Code** box beneath where you pasted the other script in step 5.
9. Select ****Done****.
10. Select ****Publish**** to save your changes.

Once you've pasted the embed code and saved your changes in Square, nagivate back to your website and refresh the page. Your embed form will display on your site and add new subscribers directly to the Klaviyo list linked to the form.

If you don't see your form, see [troubleshooting embed forms](https://help.klaviyo.com/hc/en-us/articles/360006897412#h_01JFAQY2NHMG3PPV523K4ESXEV).

If you decide to disconnect your Square integration, you will need to manually remove this embed code from the Square Online site editor to remove your form.

## Next steps

Next, [create a welcome series](https://help.klaviyo.com/hc/en-us/articles/115002775172) to make an immediate impact on your new subscribers.

## Additional resources

- [Getting started with Square](https://help.klaviyo.com/hc/en-us/articles/11117215837211)
- [How to embed a sign-up form](https://klaviyo.zendesk.com/hc/en-us/articles/360006897412)
- [How to verify that sign-up forms are enabled](https://klaviyo.zendesk.com/hc/en-us/articles/360002035871)