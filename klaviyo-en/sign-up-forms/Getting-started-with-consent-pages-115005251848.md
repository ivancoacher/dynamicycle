---
id: "115005251848"
title: "Getting started with consent pages"
source_url: "https://help.klaviyo.com/hc/en-us/articles/115005251848-Getting-started-with-consent-pages"
section: "Getting started with consent pages"
category: "Sign-up forms"
category_slug: "sign-up-forms"
klaviyo_updated: "2026-04-21T13:54:23Z"
language: "en"
---
## You will learn

Learn about the different consent pages related to Klaviyo lists, including the preferences, subscribe, and unsubscribe pages, and how to customize them.

In your Klaviyo account, there is 1 set of account consent pages that all lists will use by default. These account-level consent pages include your default preference page, subscribe page, email confirmation page, and email unsubscribe page.

You can edit the style and design to standardize the look of your account’s default consent pages for a consistent experience. However, if you would like 1 particular list to have its own consent pages (i.e., give your VIP list its own subscribe page) you can disconnect a list from the default pages and customize a unique set of consent pages for the specific list.

This article will cover how to use and manage consent pages within Klaviyo; however, if you would prefer to design your own custom coded consent pages, you can explore [Klaviyo’s hosted pages feature](https://help.klaviyo.com/hc/en-us/articles/115005077067-How-to-custom-code-an-unsubscribe-or-manage-preferences-page). Navigate to ****Settings > Other > Hosted pages**** to enable this feature. Only accounts with a paid plan who have passed [account verification](https://help.klaviyo.com/hc/en-us/articles/115000628331-About-Account-Verification) have access to this setting.

## About consent pages in emails

Your account's default consent pages are used by default in:

- Emails sent to segments
- Emails sent to multiple lists and/or segments
- Segment triggered flows
- Flows triggered by an event
- Date triggered flows
- Price drop flows

This means that when you insert an unsubscribe tag, {% unsubscribe %}, or a manage preference tag, {% manage\_preferences %}, into a campaign that is sent to a segment, the account default consent pages will be used. The same is true when you insert these tags into flow emails where the flow is triggered by an event.

If you're adding the manage preferences tag as linked text in a message, use {% manage\_preferences %}. However, if you're adding the manage preferences tag to a button or image block in a message, you must use {% manage\_preferences\_link %}.

When you send an email to a list that uses a customized set of consent pages, the default consent pages are not used. Instead, the customized consent pages that you created for that particular list will be used. To edit these pages further, navigate to the list you want to edit the pages for, then select ****Subscribe and preference pages****.

While your account’s default consent pages are helpful for centralizing a consistent experience for your subscribers, choosing to customize a unique set of consent pages for a list is often helpful. For example, if a specific list is being used for a [special contest or subscriber offer](https://help.klaviyo.com/hc/en-us/articles/115000798472), you may want the consent pages for this list to look a certain way and display a unique set of subscriber preferences.

## Find your account's default consent pages

To navigate to your default consent pages:

1. In Klaviyo, navigate to ****Audience > Growth tools****.
2. Select ****Customize subscribe and preferences pages.****
3. Select ****Account default pages****.

The pages available to edit include:

![All of the consent pages that are available to edit, including preferences page, subscribe page, email confirmation page, and email unsubscribe page.](https://klaviyo.zendesk.com/hc/article_attachments/28705636071835)

****Preference pages****

- ****Preferences page****
  The page where existing subscribers can update their preferences. Here, you can provide your subscribers with the opportunity to share more information about themselves like age, gender, or birthday, but also more detailed information like their preferred email frequency or product interests.
  - The information collected on preferences pages will show on the site visitor's individual profile. [Learn more about viewing form responses and creating segments based on this information](https://help.klaviyo.com/hc/en-us/articles/360040841811#h_01HSXZRBZ32393XVEDZJFWEVRZ).
- ****Preferences success page****
  The page subscribers will see after updating their preferences.

****Subscribe pages****

- ****Subscribe page****
  The page where interested shoppers can sign up to hear more from your brand. If your list uses single opt-in, subscribers are directed straight to the subscribe success page after submitting the form. For double opt-in lists, subscribers will first see a confirmation page, then need to confirm their subscription in the confirmation email, and finally, they'll be directed to the subscribe success page.
- ****Confirmation page****
  If your list is double opt-in, this is the page that new subscribers will see after they submit the subscribe page, instructing them to check their email to confirm their subscription. Note that only paid accounts have the ability to add and edit links and source code on this page.

****Email confirmation pages****

- ****Confirmation email****
  For double opt-in lists, this is the email sent to subscribers after they subscribe via subscribe page or sign-up form. It includes a button that, when clicked, takes them to the subscribe success page. Note that only paid accounts have the ability to add and edit links and source code on this page.
- ****Subscribe success page****
  The page that subscribers will see after signing up via subscribe page. By default, this page includes a button linking to the preferences page, allowing new subscribers to manage their preferences. Note that if someone fills out the subscribe page again, the button to the manage preferences pages won't appear because a new profile isn't created.

****Email unsubscribe pages****

- ****Email unsubscribe page****
  The page someone will see when they click the unsubscribe link in an email.

  The default email unsubscribe page includes a link to your preference pages at the bottom. Using unsubscribe and manage preferences pages together allows you to encourage recipients to change their email preferences, rather than unsubscribe completely.
- ****Email unsubscribe success page****
  The page someone will see after they unsubscribe from receiving emails.

  On your account unsubscribe success page, the button settings will show a **Primary action** and a **Secondary action**. The **Secondary action** comes into play when a list uses this page. For example, if a list uses the default consent pages instead of customized ones, then subscribers of this list will see the secondary action (i.e., Resubscribe) when they click the button.

  ![The button selected in the preview and the button menu displayed along the left, with the primary action set to Go to URL, and the secondary action set to Resubscribe. ](https://klaviyo.zendesk.com/hc/article_attachments/28705662808603)

These consent pages listed above come into play when you build sign-up forms that add new subscribers to your list. By reviewing and updating these pages, you can control the experience and messaging that your subscribers see when they first opt in, when they update their preferences, as well as when they unsubscribe.

When you choose to create a new list, each list will default to using your account’s default consent pages.

## Customize consent pages for a specific list

You can choose to disconnect your list from the default consent pages and instead customize a unique set of consent pages for a particular list.

List‑specific consent pages are only used when an email targets exactly one list (a single static list). This includes:

- Campaigns sent to one list
- Flows triggered by a list (e.g., “added to list” flows)

If a list doesn’t have its own customized pages, Klaviyo falls back to the account default consent pages.

To customize consent pages for a list, follow the steps below:

1. Navigate ****Audience > Growth tools****.
2. Select ****Customize subscribe and preferences pages****.
3. Choose ****For a specific list****.
4. Select ****Unlink and customize**** to override the default pages****.****
5. Here you will see a new set of consent pages available to edit. Find the consent page(s) you’d like to edit (e.g., the preference page), click ****Edit Page.****
6. Once you finish customizing the page in the editor, click ****Publish.****

Note that you can revert to your account’s default consent pages if you no longer want your list to use these customized pages. However, all prior customizations will be lost and cannot be recovered if you reset back to the defaults. Click ****Reset All Pages To Default**** at the bottom of the page to re-link your list to the default consent pages.

## Edit the design of your consent pages

Whether it is your default consent pages or a particular list’s unique set of consent pages, you can customize the style and design of each page to give your site visitors a consistent, on-brand experience.

If you would prefer to custom code your own preference, subscribe, or unsubscribe pages, click the dropdown arrow and select ****Use Hosted Page****. Head to our [guide on using hosted consent pages](https://help.klaviyo.com/hc/en-us/articles/115005077067-How-to-custom-code-an-unsubscribe-or-manage-preferences-page) for more detail.

1. Find the consent page you’d like to edit (e.g., the preference page), click ****Edit Page****
2. Selecting a consent page will bring you to its respective editor, where you can customize the style and design to fit your brand. Choose what you would like to edit, these include:
   - ****Styles****
     Use this section to edit design settings such as **Form Background**, **Page Background**, **Form Styles**, etc.
   - ****Add Blocks****
     Use this section to add elements to your consent page, such as a text or image block. You can also edit any text in the preview by clicking on it and replacing the default text with your own.
     ![The editor for an example Preferences page showing the options to Add blocks or edit Styles.](https://klaviyo.zendesk.com/hc/article_attachments/28705662819611)

     When adding blocks to your preference page and subscribe page, you also have the option to [add input fields](https://help.klaviyo.com/hc/en-us/articles/4413550187035-Understanding-form-blocks-and-fields#input-fields6), such as a date field or a checkbox.
   - ****Button****
     Click on the button in your preview (e.g. the **Unsubscribe** button or **Update your preferences** button) for options to edit the **Button Text**, **Button Styles**, and **Block styles.**
     **![The Button menu that appears along the left when you select a button in the preview form, and where you can edit various button function and style settings.](https://klaviyo.zendesk.com/hc/article_attachments/28705662821787)**
3. When you're ready to share your consent page, click ****Publish****.

Be sure to edit each step of the consent page that you want to customize. You can also click ****Success page**** in the top menu bar of the editor to adjust the design of the success message that appears when a recipient completes the form.

### Add profile properties

If you add an input field (e.g., a date field) to your consent page, use the ****Profile property**** dropdown to select a corresponding property (e.g., birthday). This enables Klaviyo to track the information on the visitor's dedicated profile when they submit the form. Klaviyo supports many profile properties that you can choose from to add personal information to someone’s profile.

Note that you cannot use the same profile property in multiple input fields on a form as it can cause issues with tracking. For example, if you have two text input fields in your form to collect first and last name, each of these must have their own dedicated profile property, such as First Name and Last Name.

![The Profile property dropdown that comes with any input fields added to a consent page showing the option to select or create a new property.](https://klaviyo.zendesk.com/hc/article_attachments/28705662823579)

If you don’t see the property that you would like to use in the list, you can also [collect custom properties](https://help.klaviyo.com/hc/en-us/articles/115005074627-Guide-to-Properties#custom-vs--klaviyo-properties2) by typing the property you want to use in the **Filter** box, and clicking ****Create Property****.

### Translate consent pages to different languages

If your customer base comprises different native speakers, it’s important that you create content that they will understand. The language on consent pages defaults to American English. However, to edit the language, follow the steps below.

1. Navigate to the builder of any consent page you would like to translate.
2. Click on any text in the preview to edit it.
3. In the menu that appears on the left, delete the default text, then type the text that you would like to appear in the language of your choice. Note you can click on any text in the preview form to customize it into a different language, including error messages and required text alerts for input fields.


   ![Selecting default text in the preference page preview, then deleting it in the text menu that appears and typing in new text.](https://fast.wistia.com/embed/medias/ne451y53to/swatch)

   Be sure to follow this process for each step and each consent page you would like to translate (e.g., preferences pages, subscribe pages, email confirmation pages, and email unsubscribe pages).
4. When you're ready to share your consent page, click ****Publish****. A green dot indicates a page is live, while a green circle indicates a page is live, but has unpublished edits.

## Find your subscribe page URL

Klaviyo automatically creates a subscribe page for every list in your account, which you can use to enable potential subscribers to sign up for your email or SMS marketing. Once you’re finished editing the design, you can copy the subscribe page URL to share in an email or elsewhere to grow your audience.

To find a list’s subscribe page URL:

1. Navigate to ****Lists and Segments.****
2. Choose your list.
3. From the menu bar, select ****Sign-up forms.****
   ![The Sign-up forms tab underlined and selected from the menu bar within a specific list's page.](https://klaviyo.zendesk.com/hc/article_attachments/28705636091035)
4. Here you will see all of your sign-up forms that are connected to this list. Scroll past these to find the list’s subscribe page.
   ****![Copy Subscribe Page URL being selected from the botton of the sign-up forms tab within a specific list's page.](https://klaviyo.zendesk.com/hc/article_attachments/28705662825115)****

You can also retrieve the URL by clicking ****Edit Page****, and copying the subscribe page URL from the overview menu.

Your subscribe page URL is now copied to your clipboard and ready to use in marketing campaigns or social channels. Check out [this guide on using a subscribe page as a landing page](https://help.klaviyo.com/hc/en-us/articles/115005251988-How-to-embed-a-full-subscribe-page-on-your-website) on your website to learn more.

## Redirect opted-in recipients to a different website page

When a visitor on your website confirms their subscription via double opt-in and lands on a confirmation page, you have the option to redirect them to a different URL, such as a specific page on your website. This is a great way to maximize on site traffic from highly interested subscribers.

To use a redirect URL in a confirmation page:

1. Navigate to your consent pages (this can be your account’s consent pages or a specific list’s consent pages).

   To reach your default consent pages, navigate to ****Settings > Other****. To navigate to a specific list’s consent pages, navigate to ****Audience > Lists & Segments****, choose a list, and then click ****Subscribe and Preference Pages.****
2. Under **Subscribe Page**, click ****Edit Page.****
   ****![Selecting Edit page on the account default subscribe page.](https://klaviyo.zendesk.com/hc/article_attachments/28705636086427)****
3. In the menu bar at the top, select ****Success page.****
4. Click ****Custom Redirect.****
   ****![The Custom Redirect option selected on a subcribe page's success step within the editor.](https://klaviyo.zendesk.com/hc/article_attachments/28705636088347)****
5. Check the box to **Skip page and redirect.**
6. Paste the URL that you would like subscribers redirected to.
   ![The Custom Redirect menu with the box checked to skip page and redirect and an example URL pasted in the Redirect URL box.](https://klaviyo.zendesk.com/hc/article_attachments/28705636097563)
7. When you are finished with all other design edits, click ****Publish.****

## Additional resources

- [How to custom code consent pages](https://klaviyo.zendesk.com/hc/en-us/articles/115005077067)
- [How to use a subscribe page on your website](https://help.klaviyo.com/hc/en-us/articles/115005251988-How-to-embed-a-full-subscribe-page-on-your-website)
- [How to customize a list’s unsubscribe page](https://help.klaviyo.com/hc/en-us/articles/115005079627-Customize-a-List-s-Unsubscribe-Page)