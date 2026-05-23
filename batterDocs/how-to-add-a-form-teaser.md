<h1>How to add a form teaser</h1>

## You will learn

Learn how to add a teaser to your popup or flyout sign-up form, which is a small widget that a visitor can click on to close and reopen open a form as they please.

![](https://fast.wistia.com/embed/medias/lmqiwf1eek/swatch)

Teasers can be used for popup, flyout forms and full page forms. Teasers are not available for embedded forms.

## Add a teaser to a popup or flyout, or full page sign-up form

To add a teaser to a form, navigate to the ****Sign-up forms**** tab and open an existing form or [create a new one](https://help.klaviyo.com/hc/en-us/articles/360026474752-Guide-to-Creating-a-Signup-Form). Click ****(+) Teaser**** in the form editor.

![The + Teaser button being selected from the menu bar within the form editor.](https://klaviyo.zendesk.com/hc/article_attachments/28723633426331)

### Choose a teaser style

Under **Styles**, choose one of 3 teaser shapes:

- ****Rectangle****
  Use the rectangle shape for a tab-style teaser
- ****Circle****
  Use the circle shape for a bubble-style teaser
- ****Corner****
  Use the corner shape for a teaser tucked into a corner of your site

Position your teaser on any of the sides or corners of your site. The teaser’s size is optimized for a variety of devices. Be sure to view the desktop and mobile previews to ensure the teaser’s placement doesn’t conflict with other popup or teaser-style elements on your site.

![The Styles section for the form editor for an example sign-up form showing the teaser set to Rectangle in the bottom right corner and size Medium.](https://klaviyo.zendesk.com/hc/article_attachments/28723633433115)

Here you can also choose a **Size** for your form teaser (i.e., Small, Medium, Large, Custom) using the dropdown.

Note that if you choose a rectangle style, it will not change size on mobile. Rectangle form teasers are automatically optimized on mobile to display centered and wider, making them easier to tap on.

### Edit the teaser's content

Under **Content**, add or edit text and text styles in your teaser. At a minimum, your teaser should hint at your form’s offer. Keep the teaser short for maximum impact. Use these examples of teaser text for inspiration:

- 15% off
- Redeem gift
- 🎁
- Enter giveaway
- Free shipping ➡️

If your teaser text mentions a specific offer, make sure to deliver that offer to subscribers either in your form’s success message or using a [welcome series](https://help.klaviyo.com/hc/en-us/articles/115002775172-How-to-Create-an-Email-Welcome-Series).

Here you can also edit your teasers design (i.e., **Background Color**, **Color Radius**, **Drop Shadow**, **Background Image,** and **Block Styles**).

![The Content, Background, and Block Styles section for an example form teaser in the form editor.](https://klaviyo.zendesk.com/hc/article_attachments/28723661569051)

### Set teaser behaviors

Choose 1 of the following options to determine when your teaser will appear:

- ****After form is closed****
  A teaser set to show after a form is closed will allow a visitor to reopen the form if they dismiss it, but will not appear before the form pops up. The teaser will continue to display on all pages until the visitor completes the form’s primary conversion action.
- ****Before displaying form****
  A teaser set to show before displaying a form will appear 2 seconds after the page loads. It will display until a visitor clicks it, or until the form's display conditions are met (e.g., time delay or scroll percentage).

  Note that if your form is set to display immediately on page load, or after less than a 2 second wait, the teaser will be skipped.
- ****Before displaying form and after form is closed****
  A teaser with this setting will appear 2 seconds after the page loads, and will continue displaying unless the form is currently open or the visitor has completed its primary conversion action.

If you have [collision prevention settings](https://klaviyo.zendesk.com/hc/en-us/articles/19788320859419) enabled in your Klaviyo account, form teasers will not appear on your site, since it is considered showing another form in the same session. You can adjust the time delay on the collision settings to make the teaser appear. For example, if your collision prevention settings are set to show the next form after 5 minutes, then the teaser will appear after 5 minutes.

In addition to the rules above, a teaser will only show to visitors who [meet the form’s targeting settings](https://help.klaviyo.com/hc/en-us/articles/4413544555547-How-to-Choose-Form-Targeting-and-Behavior-Settings) found in the ****Behaviors & Targeting**** section of your form. For example, a teaser set to show before displaying a form will only appear to visitors who meet the form’s targeting settings (i.e., list/segment membership, location, and URL). Once that form’s remaining triggers are satisfied (e.g., exit intent, scroll length, or time delay), the teaser will close and the form will appear.

![The Behavior section of the Teaser menu with the Show teaser setting set to after the form is closed, and the Show Close Button toggle on.](https://klaviyo.zendesk.com/hc/article_attachments/28723633436315)

#### Add a close button to your teaser

You can add a close button to your form teaser (the X button) to allow your shoppers to close the teaser if they are not interested in the form's content.

By default, your teaser will not include a close icon. Under Behavior, toggle the ****Show close button**** switch on to add one.

Note that if a shopper clicks on the X to close the teaser, it will follow the same rules for display frequency as the sign-up form that it is connected to. For example, if a shopper closes both a form and its teaser, and that form is set to show again 5 days after someone closes it, then both the form its teaser will follow the behavior setting and show again in 5 days.

## Form teasers and primary conversion actions

If a teaser is added to a multi-step form and is set to display after the form is closed, it will appear until the visitor completes the form’s primary conversion action.

- For forms with email or SMS subscription actions, submitting an email or phone number counts as a primary conversion action.
- For forms containing both email and SMS fields across multiple steps, submitting whichever appears first in the form counts as a primary conversion action.

  Note that if the primary conversion step (i.e., the email step in a multi-step form) is submitted, the teaser will not go away automatically when declining the second step (i.e., the SMS step). Rather, you will need to refresh the page or navigate to a new page to no longer see the form teaser.
- For forms without an email or SMS subscription action (e.g., a flash sale popup with a “Go to URL” action), clicking the “Go to URL” button counts as a primary conversion action.

If a multi-step form’s primary conversion action has not been completed, clicking the form’s teaser within the same browsing session will reopen the form on the last incomplete step.

## Delete a teaser

To delete a form’s teaser, click the 3 dots on the Teaser button, then click ****Delete****. This will remove all teaser settings. If you later re-add a teaser to the same form, it will be reset to the teaser defaults.

![The 3dots selected next to the Teaser button in the menu bar of the form editor showing the option to Delete.](https://klaviyo.zendesk.com/hc/article_attachments/28723633440795)

## Additional resources

- [How to A/B test a sign-up form](https://klaviyo.zendesk.com/hc/en-us/articles/360045462071)
- [Understanding sign-up form analytics](https://klaviyo.zendesk.com/hc/en-us/articles/360015960712)
- [How to optimize popup and flyout forms for mobile](https://klaviyo.zendesk.com/hc/en-us/articles/4406161800987)
