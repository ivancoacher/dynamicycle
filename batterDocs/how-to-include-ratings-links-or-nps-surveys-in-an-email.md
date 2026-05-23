<h1>How to include ratings links or NPS surveys in an email</h1>

## You will learn

Learn how to send a simple survey via email to collect information from users and then send that information back to Klaviyo as a custom property. A common use case for this is including rating links in an email or an NPS Survey.

## Configure your email template to collect user ratings

When using the code snippets provided below, make sure to use straight quotes (') rather than curly quotes (‘) to ensure the code renders correctly. This can be achieved by copying the code below and pasting it directly into your template using the "Paste as Plain Text" function (Ctrl+Shift+V or Cmd+Shift+V).

1. Within your email template, drag in a **Header** block.
2. In the **Desktop layout** and **Mobile layout** menus, select ****Links and buttons only****.
3. In the **Content** section of the block settings, click ****Add Link**** until you have 10 link fields (or, as many as desired).
4. For **Link 1**, add the number 1 in the **Text** field. Repeat with the number 2 in **Link 2**, and so on.
5. Add the following tag in the **Link address** field for each link:
   `{% update_property_link 'profile_property' 'property_value' 'redirect_link' %}`
6. Replace the generic placeholders in the tag above with the following information:
   - ****profile\_property****The custom property name that should be recorded on someone's profile (e.g., 'NPS Rating').
   - ****property\_value****The actual value that is recorded for the custom property, like the numbers 1-10 in this example.
   - ****redirect\_link****This is the URL that someone will be taken to after they select a value (e.g., your website homepage).

In the example below, the full tag for button ****1**** is:

```
{% update_property_link 'NPS Rating' '1' 'https://botanic-organics.com/' %}
```

The full tag for button ****2****is:

```
{% update_property_link 'NPS Rating' '2' 'https://botanic-organics.com/' %}
```

![NPS configuration in email template.png](https://klaviyo.zendesk.com/hc/article_attachments/34368159432475)

Once a recipient clicks on a button, they will be brought to the URL that you specify as a redirect URL and the value will automatically be added to their profile as a custom property. Please note that if someone responds to multiple NPS survey emails that use the same ****profile\_property****, the new value they input will overwrite their previous response.

## Preview your template

When you preview your template and click any of your ratings links, you’ll be directed to a placeholder page, rather than the link provided in the Update Property tag.

![Placeholder displayed when an Update Property link is clicked from a preview email](https://klaviyo.zendesk.com/hc/article_attachments/28723517937819)

If you’d like to test the full functionality of the link or button, send yourself a live email following our guide: [How to send a personal email in Klaviyo](https://klaviyo.zendesk.com/hc/en-us/articles/115005246328).

## Additional resources

- [How to show or hide template blocks and sections based on dynamic variables](https://klaviyo.zendesk.com/hc/en-us/articles/7655965301531)
- [Guide to creating a post-purchase flow](https://klaviyo.zendesk.com/hc/en-us/articles/360028872611)
