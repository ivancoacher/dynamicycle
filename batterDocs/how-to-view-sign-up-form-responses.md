<h1>How to view sign-up form responses</h1>

## You will learn

Learn how sign-up form responses are stored in Klaviyo, where to access a person’s form responses, and how to export a CSV of these responses from a group of profiles.

Using sign-up forms on your website helps you learn more about your audience, and you can use the information you collect to send highly targeted, personalized marketing.

## Before you begin

In order to see form responses, you must have a Klaviyo form that at least one person has submitted. All input fields in your form must be properly formatted, including both:

1. The profile property name, which represents the question
2. The property value, which is the person’s responses

For open-input fields (e.g., **Text input** or **Phone number**), the property value is whatever the site visitor types into the field.

For **Multi checkbox**, **Radio button**, and **Dropdown fields**, each option has a **Label** and **Value**. The labels are the options a visitor sees in the form, and the values are the responses saved on the back end after someone completes the form.

![Multi checkbox block settings](https://klaviyo.zendesk.com/hc/article_attachments/34360140061979)

If you want to include multiple input fields on your form, consider [using a multi-step form](https://help.klaviyo.com/hc/en-us/articles/4404213604251) to collect the information in smaller steps.

Where form responses are stored

When someone fills out your Klaviyo sign-up form, their responses are stored within the [custom properties section](https://help.klaviyo.com/hc/en-us/articles/115005074627) of their profile page. Every form that you create must include an email field, a phone number field, or both, in order for the responses to be attached to a profile and stored within their profile page.

If your form doesn’t contain 1 of these fields, the form responses will not be saved, although you may see a number of submissions counted in the form’s **Overview** page.

![The custom properties section highlighted on an individual profile page.](https://klaviyo.zendesk.com/hc/article_attachments/28715970929819)

If someone fills out the same form more than once, only their most recent response will be saved. Additionally, if you use the same property name in multiple forms (or if the property name is a special Klaviyo property), the property’s data will be overwritten each time Klaviyo receives new information about a person. Because of this, it’s important to use unique property names, and avoid using Klaviyo properties (e.g., $consent\_method, City, or Region) for most form fields.

There are a few exceptions. Use Klaviyo properties for the following fields:

- Email
- First Name
- Last Name
- Phone Number
- Organization
- Title
- Consent (e.g., if your form contains GDPR consent fields)

## View an individual's form response

To see a single person’s form responses:

1. Type their name or email into the search bar in the top navigation to locate their Klaviyo profile.
2. Select their profile to open the unique profile page
3. Locate the **Custom Properties** area of their profile.

Responses to any form questions will be stored here.

## View a group of form responses

To view the responses from a group without having to navigate to each individual profile, create a segment containing all people who submitted your form, then export a CSV of their answers.

### Create a segment of people who filled out the form

1. Open your sign-up form in the editor and copy the form ID.
   ![The Form ID circled in the URL.](https://klaviyo.zendesk.com/hc/article_attachments/28715964316059)

   The form ID is the six-digit identifier found in the form’s URL.
2. Exit out of the form editor and navigate to ****Audience > List & segments > Create List / Segment****.
3. Select ****Segment****.
4. Name your segment and add the following definition:
   ****Properties about someone > $consent\_form\_id > equals > Form\_ID****

   Replace Form\_ID with the form ID that you just copied.

   - Note that each time someone fills out a form, their $consent\_form\_id property is replaced with the ID of the form they filled out most recently, so profiles will only appear in this segment if they have not filled out any other forms since completing the one in question. To avoid this, [add a hidden field to your form](https://help.klaviyo.com/hc/en-us/articles/115005074627#ask-customers-for-properties6)before setting it live, then use the hidden field property as your segment definition.
5. Select ****Create Segment****.

Note that it may take a few minutes or more for the segment to populate, depending on its size.

### Export a CSV containing all form responses

1. Navigate to ****Audience > Lists & segments****.
2. Open the segment you just created of people who filled out your form.
3. Click ****Manage Segment > Export Segment to CSV****.
   ![The manage segment dropdown opened with the option to export segment to CSV being selected.](https://klaviyo.zendesk.com/hc/article_attachments/28715964320027)
4. On the **Export Review** page, check all the properties from your form. You can search for property names if needed.
5. Select ****Start Export**** to export a CSV containing the form responses.

The resulting CSV contains the corresponding data found in each individual’s profile. If someone filled out the form multiple times, the export will only include their most recent response. Additionally, if someone filled out the form anonymously (i.e., without an email address or phone number), their results will not be stored in Klaviyo or included in any exports, as Klaviyo cannot store anonymous data.

## Next steps

Now that you can segment based on form responses, you can use data in your emails and SMS. Head to our [guide on advanced segmentation](https://help.klaviyo.com/hc/en-us/articles/360035312491) to learn more.

## Additional resources

- [Understanding data types](https://help.klaviyo.com/hc/en-us/articles/115005237648-About-Data-Types)
- [Getting started with segments](https://help.klaviyo.com/hc/en-us/articles/115005237908-Guide-to-Creating-Segments)
- [How to segment for form results](https://help.klaviyo.com/hc/en-us/articles/360040841811-How-to-Segment-for-Form-Results)
