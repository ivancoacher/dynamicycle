<h1>How to create a base template</h1>

Learn how to create a base email template in Klaviyo. Once you create a base template, you can use it across your campaigns and flows to speed up your building process and ensure your branding is consistent across messages.

[Create visually stunning emails in Klaviyo Video](https://fast.wistia.net/embed/iframe/8sgk45i709?seo=true&videoFoam=true)

## Before you begin

A base template includes key sections like a header, body content, and a footer. Navigate to ****Content > Templates**** and click ****Create**** to get started. Then, follow the steps below to add reusable content to your template.

## 1. Set base styles

Before styling any individual blocks, set your base styles. These styles, like font, colors, padding, and more, apply to all blocks across your template.

Adding base styles makes it easier to apply your branding, and it also reduces your code weight, making it easier to avoid [clipping in Gmail](https://help.klaviyo.com/hc/en-us/articles/115000591251).

To add base styles:

1. Click ****Styles**** (next to **Content**).
   ![Main styles tab](https://klaviyo.zendesk.com/hc/article_attachments/28723629342491)

   If you see **Display Options** next to the **Styles** tab instead of **Content**, click ****Done**** to navigate out of the block/section’s styles settings, which only apply to that block or section.
2. Set a background color for your template and content, along with margin and padding. We recommend leaving the [Width setting as 600px](https://help.klaviyo.com/hc/en-us/articles/115001435352) for optimal compatibility with inbox providers.
   ![Email style settings](https://klaviyo.zendesk.com/hc/article_attachments/39576806498075)
3. Add text styles, including fonts, font sizes, colors, and spacing. Make sure to set styles for ****Normal**** text, as well as ****H1****, ****H2****, ****H3****, and ****H4****. You can use these heading styles for prominent text throughout your email. Learn how to [use a custom font in your emails](https://help.klaviyo.com/hc/en-us/articles/4412748537627).
   ![Text and Headings](https://klaviyo.zendesk.com/hc/article_attachments/39576797317659)
4. Add a link color and style.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/39576806505499)
5. Select your store’s currency in the **Currency** menu. The selected currency symbol is used wherever the [{% currency\_format … %} tag](https://help.klaviyo.com/hc/en-us/articles/115005061007) is present in a template.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/39576797322907)
6. If **Mobile optimization** is turned on, add mobile settings. These will appear when someone opens your email on a mobile device. Learn more about [mobile optimization](https://help.klaviyo.com/hc/en-us/articles/115005254428).
   ![Mobile settings](https://klaviyo.zendesk.com/hc/article_attachments/39576797325979)

## 2. Build a header section

After you set up your email styles, add your header section. Generally, header sections include a logo, key links, and sometimes a banner featuring information about your latest sale or the recipient’s VIP status.

1. If your template already has a header bar, update it with your own logo. Alternatively, drag in a **Header** block and add your logo. Learn best practices for [image sizing and quality](https://klaviyo.zendesk.com/hc/en-us/articles/115005253688).
   ![Replace header logo](https://klaviyo.zendesk.com/hc/article_attachments/39576806515611)
2. Select a layout in the **Desktop layout** and **Mobile layout** menus (e.g., ****Logo inline**** for desktop and ****Stack all**** for mobile). Remember that mobile devices use much smaller screens than desktop, so stacking content can make it easier to read and navigate.
3. In the **Content** section, add key site navigation links. Click the trash icon to remove links, or ****Add links**** to add them. Common links to include in your header are: shop now, new arrivals, about, sale, FAQs, or a selection of product categories.
   ![Header bar links](https://klaviyo.zendesk.com/hc/article_attachments/39576797331483)
4. Adjust block styles in the sections below your link content. Remember, if you want to apply a style setting to your whole email, use the main **Styles** tab as outlined in the section above.
5. Click ****Done**** to return to the main template editing options.

### Add an optional feature banner

You can add a feature banner above or below your header bar.

1. Drag a text block into the same section as your link bar.
   ![Add text banner above](https://klaviyo.zendesk.com/hc/article_attachments/39576797335195)
2. Set the background to an accent color and add a featured message, like “Use code WELCOME for 15% off your first order!”
3. Check that your feature banner and link bar are in the same section by hovering over the space to the left or right of the blocks. A grey **Section** border should surround both blocks on hover, and it turns blue when the section is clicked.
   ![Section border](https://klaviyo.zendesk.com/hc/article_attachments/39576806528923)
4. Optional: Click the star icon to save the section as universal content. Universal blocks and sections can be used across multiple templates, and you can edit all instances of the block/section at one time. Learn more about [universal content](https://help.klaviyo.com/hc/en-us/articles/115005413888).

## 3. Add body content

[Create high-converting emails Video](https://fast.wistia.net/embed/iframe/ktggbub1ds?seo=true&videoFoam=true)

1. Drag a ****Section**** block from the **Layout** section of the **Content** sidebar and place it beneath your header.
   ![Add a section](https://klaviyo.zendesk.com/hc/article_attachments/28723629384731)
2. Add placeholder blocks for your email body content. This might include text blocks with descriptions of your brand or promo messaging, common layouts you intend to use, placeholder product imagery, and more. Learn how to [place content side-by-side](https://help.klaviyo.com/hc/en-us/articles/115000807711) using columns, split blocks, and tables.
   ![Body content section](https://klaviyo.zendesk.com/hc/article_attachments/28723624075547)

Learn how to [add a background image to a section](https://help.klaviyo.com/hc/en-us/articles/4408802285083) and overlay buttons, text, and other elements on top of it.

## 4. Build a footer section

Klaviyo requires you to include an unsubscribe link in your emails, and this is most commonly placed in the footer. In addition, these footer elements are recommended:

- Your business address
- A link to your privacy policy
- Links to your social profiles (e.g., Facebook, Instagram, Twitter, Tiktok)
- A link to your website
- An email preferences link

To add a footer to your base template:

1. Drag a new section beneath your body section, or edit the default footer.
2. Add a text block.
3. Click ****Personalization****.
4. In the **Search personalization** field, search for “unsubscribe.”
5. Select ****Unsubscribe**** to add an unsubscribe link tag to your text block.
6. Use this same menu to add an organization address, manage preferences link, web view link, and more.
   ![Organization personalization options](https://klaviyo.zendesk.com/hc/article_attachments/28723624097307)
7. When you send the email, these tags will be replaced with the appropriate text or links.
   ![Footer rendered](https://klaviyo.zendesk.com/hc/article_attachments/28723624092699)
8. Next, drag a ****Social links**** block into your template, directly above the text block from the previous steps.
9. Select your social channels from the dropdown to add them to the block.
   ![Select social channels](https://klaviyo.zendesk.com/hc/article_attachments/39576797344923)
10. In the **Link address** field for each social channel, add a link to your profile.
11. Choose an icon style.
    ![Social icon styles](https://klaviyo.zendesk.com/hc/article_attachments/39576806533787)
12. Click ****Done**** to return to the main template editing options.
13. Optionally, save the entire footer section as [universal content](https://help.klaviyo.com/hc/en-us/articles/115005413888).

## 5. Preview

Once you’ve added a header, body content, and a footer section, preview the email.

1. Click ****Preview & test**** in the top right corner of the email editor.
2. Toggle between desktop and mobile to make sure the template appears as desired in both formats.
3. Click ****Send test**** to send a test email to your own inbox.
4. Click ****Done**** to close the preview modal.
5. Click ****Save**** to save your template.

Once you’ve saved the base template, you can use it as the basis for all future [campaign](https://help.klaviyo.com/hc/en-us/articles/115005054847) and [flow](https://help.klaviyo.com/hc/en-us/articles/115002774932) emails.

## Next steps

- Course: [Best practices to improve your email content](https://academy.klaviyo.com/en-us/courses/best-practices-to-improve-your-email-content/1881092)
- [How to create, edit, delete, and manage templates](https://help.klaviyo.com/hc/en-us/articles/115000102752)
- [How to add a first name to an email or SMS](https://help.klaviyo.com/hc/en-us/articles/11613154130843)
- [How to show or hide template blocks and sections based on dynamic variables](https://help.klaviyo.com/hc/en-us/articles/7655965301531)
