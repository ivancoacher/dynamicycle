<h1>How to ask for SMS consent within an email</h1>

## You will learn

Learn how to send a message to your existing email subscribers encouraging them to opt in to SMS marketing. By following this process, your email subscribers will be able to sign up for SMS marketing with just a few clicks.

You can collect SMS consent via email in targeted campaigns or within flows. For instance, post-purchase flows are an effective place to advertise your SMS program and gather sign-ups.

## Before you begin

Before you start, make sure you’ve:

- [Configured SMS in your Klaviyo account](https://help.klaviyo.com/hc/en-us/articles/4404274419355)
- Set up your [mobile terms of service](https://help.klaviyo.com/hc/en-us/articles/360049177511-) and [privacy policy](https://help.klaviyo.com/hc/en-us/articles/4404199571867)

## Send an email to request SMS consent

To collect SMS consent from your existing subscribers, we recommend taking three steps:

1. [Create an embedded SMS sign-up form.](#h_01GARPD00Q4T6YX1BNTSNCDMMZ)
2. [Embed your sign-up form in a landing page on your website.](#h_01GARPDFDAZSQ73SZG7QW4TM1W)
3. [Send a campaign encouraging email subscribers to sign up for SMS.](#h_01GARPDTY04QFPZ64DB8W70BDF)

### Create an embedded sign-up form

Start by creating a sign-up form and designing it to match your brand.

1. In Klaviyo, navigate to ****Content > Signup Forms**** > ****Create Sign-up Form > Build From Scratch****.
2. Choose a descriptive form name, like **SMS Sign-ups from Email**.
3. From the **Choose a list...** dropdown, select your SMS list (e.g., “SMS Subscribers” or “SMS List”).
4. From the **Choose a form type** menu, select ****Embed****.
   ![The modal to create a new signup form](https://klaviyo.zendesk.com/hc/article_attachments/28704477770523)
5. Click ****Save and Continue to Design****.
6. Delete the **Email** block in the default form.
7. Click ****Add Blocks**** from the menu on the left.
8. Drag a ****Phone Number**** block into your form.
9. If needed, edit the highlighted portions of the SMS marketing disclaimer.
10. Click ****Done****.
11. Click ****Targeting & Behaviors**** in the menu on the left.
12. Set the form to show to all visitors on both desktop and mobile devices.
13. Copy the code in the **Embed Code** section, which you’ll need for the landing page you create in the next step.
    ![An embedded form's embed code](https://klaviyo.zendesk.com/hc/article_attachments/28704477772059)
14. Once you’ve designed and customized the form, click ****Publish****.

![A user click's Publish on a signup form](https://klaviyo.zendesk.com/hc/article_attachments/28704477774491)

### Embed your signup form on a landing page

1. Open your website’s admin and create a new landing page, custom page, or blog post.
2. Paste the code snippet from the prior section into your new page’s code (often indicated by a `</>` or **Source** button).
3. Save your new page and copy its URL, which you’ll need in the following section.

### Send a campaign encouraging email subscribers to sign up for SMS

#### Create an SMS sign-up button in your email

First, [create an email template](https://help.klaviyo.com/hc/en-us/articles/115000102752-How-to-create-edit-delete-and-manage-templates). Once you've designed your template:

1. Drag a ****Button**** block into the template.
2. In the **Button Text** field, add descriptive button text like ****Sign up for SMS****.
3. In the **Link URL** field, add the URL for the landing page you created in the last section.

![The button settings for a button block in an email](https://klaviyo.zendesk.com/hc/article_attachments/28704477775387)

#### Create a segment of potential SMS subscribers

When your email is ready to send:

1. Navigate to ****Lists & Segments > Create List / Segment > Segment****.
2. Name your segment something descriptive, like **Subscribed to email but not SMS**.
3. Create a segment with the definition ****If someone can or cannot receive marketing > can receive > email marketing > because person subscribed AND If someone can or cannot receive > cannot receive > SMS marketing > because person never subscribed****.
4. Click ****Create Segment**** to save the segment.

#### Send your campaign

1. Navigate to ****Campaigns > C********reate Campaign****.
2. Select ****Email > Create Campaign****.
3. Choose the segment you created above (e.g., the **Subscribed to email but not SMS** list) as your **Send to** list.
4. Click ****Continue to Content****.
5. Add a subject line, then click ****Drag and Drop****.
6. Click ****My Templates****.
7. Select the template you created previously.
8. Proceed through the steps to [review and send your campaign](https://help.klaviyo.com/hc/en-us/articles/115005054847-How-to-create-and-send-an-email-campaign).

In addition to sending this message to your existing email subscribers, consider adding it to your email welcome series as well. Just make sure to add the following as an **Additional Filter** to the message: ****If someone is or is not consented to receive SMS > is not****.

## Alternative method: add a click-to-text banner to a campaign

Note that this approach is designed to automatically open a text message, but it will not work with Gmail or in Microsoft Outlook; however, everyone can see the banner and manually text your number to subscribe, regardless of their inbox provider.

A click-to-text banner in an email generates a text message with an opt-in keyword when a recipient clicks it. To use this functionality, you’ll create 2 versions of your call-to-action: one for desktop users and another for mobile users.

1. Add a **Text** block to your email template.
2. Add the following text to your text block:

   - Text subscribe\_keyword to sending\_number.
3. Replace **subscribe\_keyword** with a subscribe keyword from your account (e.g., JOIN).
4. Replace **sending\_number** with your sending number.
   ![A click-to-text banner followed by disclosure language](https://klaviyo.zendesk.com/hc/article_attachments/28704477779099)
5. Within ****Display Options > Visibility****, click ****Desktop**** to set the block to only show on desktop.
   ![A block set to mobile only in Klaviyo's template editor](https://klaviyo.zendesk.com/hc/article_attachments/28704477781915)
6. Click ****Save**** to save the block.
7. Use the clone icon to clone the block.
8. Within ****Display Options > Visibility****, click ****Mobile**** to set the new block to show only on mobile devices.
9. In the mobile-only block, click the source code button to access the block’s HTML.
   ![The source code button in Klaviyo's email template editor](https://klaviyo.zendesk.com/hc/article_attachments/28704485928219)
10. Replace all the existing code with the code below:

    - `<a href="sms:+sending_number?&body=Send%20this%20text%20to%20subscribe%20to%20SMS%20Updates!%20%28ref:JOIN%29">
      Text JOIN to sending_number
      </a>`
11. Replace both instances of sending\_number (in bold) above with your SMS sending number.

    - The first instance of your sending number should include the country code (e.g., 1 for the US) followed by the 10 digits of your SMS sending number, with no dashes, spaces, or parentheses: **16171110000**
    - The second instance of your sending number may include formatting characters: **(617) 111-0000**![The code for a click to text banner in an email](https://klaviyo.zendesk.com/hc/article_attachments/28704477786523)
12. Click ****Save**** to save the block.
13. Add disclosure language to the banner or within the email.
    ![A click-to-text banner followed by disclosure language](https://klaviyo.zendesk.com/hc/article_attachments/28704485925403)
14. Create a segment of your email-only subscribers with the following condition:
    ****If someone can or cannot receive marketing > can receive > email marketing > because person subscribed AND If someone can or cannot receive > cannot receive > SMS marketing > because person never subscribed****

[Send your email](https://help.klaviyo.com/hc/en-us/articles/115005054847-How-to-create-and-send-an-email-campaign) to your email-only subscribers using a campaign, or add the message to your email welcome flow.

## Review your results

To keep track of your new SMS subscribers, navigate to ****Analytics > Metrics > Consented to Receive SMS****. Here, you can review your subscriber trends and understand who is opting in to SMS. Learn more about [understanding your subscribers in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/360047399472-Getting-Started-with-Reporting).
