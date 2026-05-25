---
id: "11286232753051"
title: "How to use dynamic blocks in forms"
source_url: "https://help.klaviyo.com/hc/en-us/articles/11286232753051-How-to-use-dynamic-blocks-in-forms"
section: "Form best practices"
category: "Sign-up forms"
category_slug: "sign-up-forms"
klaviyo_updated: "2026-04-21T13:54:10Z"
language: "en"
---
Learn about dynamic blocks, and how you can use them in sign-up forms to create distinct views and experiences for shoppers on desktop and mobile devices. Any block in your form can be made dynamic by adjusting its visibility settings.

## About dynamic blocks

Dynamic blocks allow you to control which blocks appear based on the device. You can configure blocks to appear differently in your form based on the device, or to appear on 1 device but not the other.

Use cases for dynamic blocks:

- Customize form displays for different device types (e.g., mobile and desktop) so shoppers see a design tailored to their screen.
- Create a single form with different SMS opt-in methods shown to either device type to optimize conversions (i.e., show a tap-to-text option on mobile devices and a phone number input field on desktop devices).

## Before you begin

Open your form in the editor and navigate to the ****Targeting and Behaviors**** section. Ensure your form is set to display on **Both desktop and mobile** so all shoppers can see it.

![visibility2.jpg](https://klaviyo.zendesk.com/hc/article_attachments/29797996251419)

This setting will allow you to configure separate displays for desktop and mobile.

## Use dynamic blocks to create distinct desktop and mobile views

Any blocks or input fields in a form, whether existing or newly added from the **Add Blocks** tab can be made dynamic. To adjust which devices display a certain block, follow these steps:

1. Click on the block in the form preview panel (e.g., a text block).
2. In the block's settings menu along the left, scroll down to **Visibility**.
3. Choose whether to show the block on ****desktop****, ****mobile****, or all ****devices****.
4. Repeat this process for any blocks that you want to be dynamic.

To preview how your form looks on each device, use the view selector in the top-right corner of the form editor. You can toggle back and forth between the desktop icon and the mobile device icon to see each view.

- The desktop view shows how your form will appear to shoppers browsing your site on a desktop. Only blocks configured to ****Desktop**** and ****All devices**** will be visible in this view.
- The mobile view previews what shoppers will see when browsing on a mobile device. It displays blocks configured for ****Mobile**** and ****All devices****.

### Example

Let's say you want your form's headline text to appear differently on desktop versus a mobile device. To configure this:

1. In the view selector in the top right corner, select the desktop icon.
2. Select the text you want to edit in the form preview and make your changes.
3. In the text block's settings menu, scroll to **Visibility** and set the text block to show on ****Desktop**** only.

   ![ Setting a text block to show on desktop only by clicking the desktop icon in the view selector, then selecting the text block and choosing desktop under devices.](https://fast.wistia.com/embed/medias/e32c6cdnz2/swatch)

   When you set a block to only show on desktop, you're choosing to hide the block from mobile users, so it will not be visible on the mobile preview.
4. To adjust the mobile view, switch to the mobile preview by selecting the mobile icon in the view selector.
5. Go to the ****Add blocks**** tab, and drag and drop a new text element into the mobile preview.
6. Customize the default headline text for mobile shoppers. This text should be different than what you used on the desktop version.
7. In the text block's settings menu, scroll down to **Visibility** and set this text block to show on ****Mobile****.

   ![Use the mobile/desktop toggle in the top right corner to switch to the mobile view, and then click on the block to edit, make your changes, and set it to show on mobile devices only.](https://fast.wistia.com/embed/medias/wvhcm7caxp/swatch)
8. Optional: Repeat this process for other elements or input fields that you want to display differently based on the device type (e.g., show an image to desktop shoppers but hide it on mobile).
   - If you want to make images in your form dynamic, you could:
     - Add a side image to both the mobile and desktop views, or just one of the two.
     - Use a side image in the desktop view and place an image above the headline text on mobile, or vice versa.

## Use dynamic blocks to optimize SMS consent collection

If you have a sign-up form that collects SMS consent, you can use dynamic blocks to optimize SMS opt-in method for each device (e.g., show mobile shoppers a tap-to-text button, while desktop shoppers see a phone number input field).

Keep in mind, the pre-built templates in the form library that collect both email and phone numbers already have dynamic blocks set up for optimized SMS opt-ins on each device. If you choose one of these templates, you won't need to configure the blocks; you will only need to customize the form's styling to match your brand.

If you're starting fresh or or want to create a new form to collect SMS subscribers, check out our guide on [how to collect SMS consent with Smart opt-in](https://help.klaviyo.com/hc/en-us/articles/24743883751451).

To set this up:

1. Open your existing form in the editor and navigate to the ****SMS Opt-in**** step in the menu bar.
   - If your form does not already have this step, click ****+Step > SMS Opt-in**** and select a list to add it.
     ![The add step option selected in the menu bar of the sign-up from editor.](https://klaviyo.zendesk.com/hc/article_attachments/28722559509659)
2. In the view selector at the top right, select the desktop icon to customize the desktop view of your form.
3. Select the phone number input field in the preview and under **Visibility,** set it to show on ****Desktop****. Do the same for the SMS disclosure language, and the submit button.

   ![Video setting the phone number input field, the disclosure language and the submit button to show on desktop devices only on the desktop view of the SMS Opt-in step.](https://fast.wistia.com/embed/medias/7v70pc9u9a/swatch)

   Note that when you set a block to show on desktop devices specifically, it will not be hidden in the mobile view.
4. Switch to the mobile view of your form by selecting the mobile icon in the top right corner.
5. Select the ****Add Blocks**** tab, then drag and drop a new button block into the mobile preview.
6. Change the button's **Action** to ****Subscribe via SMS****.

   ![Switch to the mobile device view with the toggle in the top right corner, drag a button block in and set the action to subscribe via SMS to set up a tap-to-text.](https://fast.wistia.com/embed/medias/a0lo7w8bp6/swatch)
7. Customize your **Subscribe Keyword and Subscribe Message** for your tap-to-text call to action.
8. Under **Sending Region**, choose the appropriate phone number for the region you’d like to target with the form.
9. Toggle back and forth between the desktop and mobile views to make sure the blocks appear as you intended on each device.

Now, your dynamic blocks are configured to collect SMS consent in the most optimized method for both desktop and mobile.

## Next steps

Before you publish your sign-up form, navigate to the ****Styles**** tab to change the layout, fonts, and colors to match your brand. Also, be sure to add and customize your SMS disclosure language.

## Additional Resources

[SMS opt-in methods reference](https://klaviyo.zendesk.com/hc/en-us/articles/27902671291419)

[Understanding form blocks and fields](https://klaviyo.zendesk.com/hc/en-us/articles/4413550187035)

[Understanding styles for a sign-up form](https://klaviyo.zendesk.com/hc/en-us/articles/4413537049883)

Course: [Klaviyo practitioner certificate](https://academy.klaviyo.com/en-us/certificates/klaviyo-practitioner-certificate)