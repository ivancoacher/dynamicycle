---
id: 360022594552
title: "How to add a Klaviyo embed form to your BigCommerce site"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360022594552-How-to-add-a-Klaviyo-embed-form-to-your-BigCommerce-site"
section: "BigCommerce best practices"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:43Z"
language: en
---

## You will learn

Learn how to add a Klaviyo embed form to your BigCommerce site, which requires creating the form in Klaviyo, and then pasting it's embed code to your site’s files where you want it to appear (e.g., the footer).

This guide shows how to replace the BigCommerce default sign-up form with a Klaviyo embed form.

## Before you begin

Before creating an embed form in Klaviyo, you must first integrate with BigCommerce, and then enable sign-up form functionality (also called "onsite tracking"). If you checked the setting **Automatically add Klaviyo onsite JavaScript** when [integrating with BigCommerce](https://help.klaviyo.com/hc/en-us/articles/115005082547-Integrate-with-BigCommerce-Stencil-Themes#step-3---install-klaviyo-js-and-viewed-product-tracking5), you’re all set.

If not:

1. In Klaviyo, select the ****Integrations**** tab.
   ![An example account name selected in Klaviyo showing the Integrations tab being selected from the navigation menu.](https://klaviyo.zendesk.com/hc/article_attachments/32015108658459)
2. Click ****BigCommerce****.
3. Check the setting ****Automatically add Klaviyo onsite javascript****.
4. Click ****Save****.

The example in this article uses BigCommerce’s default Cornerstone theme. Keep in mind that your theme may differ, along with the names of some files or locations of code snippets.

## Adding the form's embed code to your site

First, [create and publish an embed form in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/360006897412). This section will go over the next steps of pasting your form's embed code on your BigCommerce site so it displays and syncs data properly.

1. If you have not already, copy the embed code for your embed form. You can access the form’s embed code by opening the form in the editor and clicking into the ****Targeting & behavior**** section.
   ![An example form's embed code highlighted to copy from the Display menu of the Targeting and behaviors tab within the form editor.](https://klaviyo.zendesk.com/hc/article_attachments/32015108670619)
2. Navigate to your website and locate the default BigCommerce sign-up form. If you’re using a Cornerstone theme, it’s in the footer of the site.
   ![A BigCommerce storefront showing sample products and an email subscription form in the site footer](https://klaviyo.zendesk.com/hc/article_attachments/28723630357531)
   - If you do not see a default form on your website:
     - Open your BigCommerce dashboard.
     - Navigate to ****Marketing > Email Marketing****
     - Check the box labeled **Allow newsletter subscriptions**. This enables you to collect email consent from visitors on your website, and also adds a default email sign-up box on your BigCommerce site. If this box is already checked and you still don’t see a default form, then your theme may not include one.
3. Open your BigCommerce dashboard, then navigate to ****Storefront > Themes****.
4. From the **Current Theme** section, click the ****Advanced**** dropdown then choose ****Edit Theme Files****.
   ![BigCommerce dashboard showing Current Theme with Advanced Settings dropdown open and Edit Theme Files highlighted in blue.](https://klaviyo.zendesk.com/hc/article_attachments/28723625055131)
   - If you’re using a default theme, you will not be able to select this option. Instead:
     - Click ****Make a Copy****, name it, then select ****Save a Copy****.
     - Once it’s added to the **Themes** section, select the 3 dots, then choose ****Edit Theme Files****. Note that any edits you make will only apply to the theme you're editing, and you'll need to apply the theme to your website to see the changes reflected.
5. In the left sidebar, open the file corresponding to where the default form appeared on your site. If the default form was located in the footer, like in the example, navigate to ****templates > components > common****, and click the ****footer.html**** file.
6. Use the find shortcut (Command+F on Mac or Control+F on Windows) to search the word “newsletter” within the footer file.
   ![The find shortcut command searching the term ](https://klaviyo.zendesk.com/hc/article_attachments/32015094392091)
7. Within the code beneath it, find the reference to the form. In the example, the form is referenced in a different file path: {{> components/common/subscription-form}}.
   ![The file path for the newsletter form referenced within an example site's footer file.](https://klaviyo.zendesk.com/hc/article_attachments/32015094399003)
8. In the left sidebar, follow the file path referenced in the code (in this example, select ****components > common > subscription-form****). You’ll see the actual components of the default form from here.
   - Because the default form's header and language matches the rest of our site's styles, we're only going to replace the actual form input. In the source code, you can see that the default form’s input is contained in the <form> element.
9. Highlight everything between the opening and closing <form> tags, then paste the embed code that you copied from Klaviyo to replace the highlighted text.
   ![The subscription-form file for an example website showing the default form input highlighted within the form tags.](https://klaviyo.zendesk.com/hc/article_attachments/32015108693787)
10. Click ****Save and apply file**** to apply these changes to your website.
    - If the button only says ****Save file****, then the file you just edited is not your **Current Theme** yet. You’ll need to click ****Save file****, then scroll up and select ****Edit Theme Files > Save > Use as Active Theme**** in the top right corner to apply the theme to your website.

Once you’ve pasted the embed code, saved, and applied the changes in BigCommerce, navigate back to your website and refresh the page. Your Klaviyo embed form will display on your site and begin adding new subscribers to the Klaviyo list linked to the form.

If you don’t see your form, see [troubleshooting embed forms](https://help.klaviyo.com/hc/en-us/articles/360006897412#h_01JFAQY2NHMG3PPV523K4ESXEV).

## Next steps

Next, create a [welcome series flow](https://help.klaviyo.com/hc/en-us/articles/115002775172) to make an immediate impact on your new subscribers.

## Additional resources

- [How to create an email welcome series](https://help.klaviyo.com/hc/en-us/articles/115002775172-How-to-Create-an-Email-Welcome-Series)
- [How to disable notification emails sent by BigCommerce](https://help.klaviyo.com/hc/en-us/articles/4403594764315-How-to-Disable-Notification-Emails-Sent-by-BigCommerce)