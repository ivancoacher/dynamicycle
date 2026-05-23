<h1>How to use a subscribe page on your website</h1>

## You will learn

Learn how to create and customize a subscribe page so that your customers can easily sign up to hear more from your brand.

This guide will go over how to find and customize your subscribe pages, such as with questions to gauge personal preferences, and how to use a subscribe page to grow your lists, such as by sharing the unique URL on social media or embedding it on your site.


![Explaining how you can add questions to a form and tie them to profile properties in order to learn and capture information from your new subscribers.](https://fast.wistia.com/embed/medias/pfkr3txgaf/swatch)



## Find your subscribe page

By default, any time you create a new list it will automatically use your account's default consent pages (manage preferences page, subscribe page, and unsubscribe page). The account's default consent pages standardize a consistent experience for subscribers; however, you can also choose to create a new set of consent pages specifically for 1 list.

To find your default subscribe page:

1. Click on your organization name in the bottom left corner of the main menu.
2. Click ****Settings.****
3. Select ****Other**** from the top.
4. Under **Subscribe page**, click ****Edit Page**** to enter the editor.
   ![The account default consent pages, which are found under the Other tab in the Account Settings.](https://klaviyo.zendesk.com/hc/article_attachments/28717991640987)

If you customized a set of consent pages for a specific list, or you would like to, navigate to that list's unique subscribe page:

1. Select ****Audience >**** ****Lists & Segments****.
2. Choose your list.
3. Select ****Subscribe & Preference Pages**** from the top.
   ![A specific list's page with the subscribe and preferences pages tab selected from the menu bar.](https://klaviyo.zendesk.com/hc/article_attachments/28717985755291)
4. Click ****Customize for this List**** (if you haven't yet customized any of this list's consent pages).
5. Below Subscribe Page, click ****Edit Page**** to enter the editor.

## Style and add fields to a subscribe page

In the editor you have various options for customizing your subscribe page's style and content. You can edit the page's style settings, change any default text to match your tone or preferred language, and also add blocks or input fields to collect more information from your customers. If your list is set to double opt-in, then you can also customize the email confirmation page. Head to our [guide on how to edit consent pages](https://help.klaviyo.com/hc/en-us/articles/115005251848#edit-the-design-of-your-consent-pages4) for more detail on the editor.

Note that it's Klaviyo best practice to only collect 1 of the 2, email or SMS consent, on a subscribe page. This guide will cover collecting email, but head to [how to create an SMS subscribe link](https://help.klaviyo.com/hc/en-us/articles/14104388043931) if you want to grow your SMS audience with a subscribe page.

If you add an input field to your subscribe page (e.g., a date field), you can also add a [profile property](https://help.klaviyo.com/hc/en-us/articles/115005074627-Guide-to-Properties) from the dropdown menu that will add personal information to someone's Klaviyo profile. Choose a property from the dropdown menu.

![the profile property dropdown menu options from a date field added to the form](https://klaviyo.zendesk.com/hc/article_attachments/28717985752987)

If you do not see the property you would like to use, type your own [custom property](https://help.klaviyo.com/hc/en-us/articles/115005074627-Guide-to-Properties#custom-vs--klaviyo-properties2) into the **Filter** box and click ****Create Property.****

## Share your subscribe page URL

Once you're satisfied with the design, you can copy the URL for a list's subscribe page to share in your various marketing campaigns. To find the subscribe page URL:

1. Navigate to ****Lists and Segments.****
2. Choose your list.
3. From the top menu bar, select ****Sign-up forms.****
4. Scroll down to the bottom of the page.
   - If you customized new consent pages for this list, you'll find a **Subscribe page** card at the bottom of the page. Click the 3 dots menu, then select ****Copy URL****.
     ![The subscribe page tile for a specific list's subscribe page with the dropdown option to Copy the URL selected.](https://klaviyo.zendesk.com/hc/article_attachments/28717991638683)
   - If your list uses the default consent pages,  you'll see a menu reminder that you can customize consent pages for this specific list. Beneath this reminder, click ****Copy Subscribe Page URL****.
     ****![The Copy Subscribe Page URL link found in the sign-up forms tab of a list's page.](https://klaviyo.zendesk.com/hc/article_attachments/28717991645211)****

You can share this link in your social channels, such as in an [Instagram story](https://help.klaviyo.com/hc/en-us/articles/360059544911#add-your-link-to-an-instagram-story4). Recipients who click on this link will be brought to a subscribe page serving as a landing page where they can sign up to hear more from you brand.

## Embed the subscribe page

Using the subscribe page URL, you can also embed form to appear as a landing page that is part of your website. Embedded forms are helpful for customers who come to your site with the intention of subscribing.

To embed this page on your website:

1. Copy the snippet of code below.
2. Replace ****SUBSCRIBE\_URL**** with the URL for the page you want to embed it on.
3. Open your website in the backend.
4. On the page where you want the subscribe page to appear, paste the code.

```
<iframe id="klaviyo_subscribe_page" src="SUBSCRIBE_URL&embed=1" seamless="seamless" width="100%" scrolling="no" ></iframe>
<script type="text/javascript" src="//a.klaviyo.com/media/js/lib/iframeresizer.js"></script>
<script type="text/javascript">iFrameResize({}, '#klaviyo_subscribe_page');</script>
```

Because pasting code requires access to your site's HTML and platform, our support team is unable to offer hands on assistance. If you're not comfortable with code or do not have a developer on your team, consider reaching out to a [Klaviyo partner](https://klaviyo.partnerpage.io/).

## Additional resources

- [Getting started with consent pages](https://help.klaviyo.com/hc/en-us/articles/115005251848-Getting-started-with-opt-in-related-pages-for-a-list)
- [Understanding list growth tools in Klaviyo](https://klaviyo.zendesk.com/hc/en-us/articles/115005080327)
- [How to find the subscribe link for a list](https://klaviyo.zendesk.com/hc/en-us/articles/115005078547)
