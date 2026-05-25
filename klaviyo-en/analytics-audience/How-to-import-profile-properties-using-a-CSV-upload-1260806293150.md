---
id: "1260806293150"
title: "How to import profile properties using a CSV upload"
source_url: "https://help.klaviyo.com/hc/en-us/articles/1260806293150-How-to-import-profile-properties-using-a-CSV-upload"
section: "Profile management"
category: "Audience"
category_slug: "analytics-audience"
klaviyo_updated: "2026-05-11T11:04:56Z"
language: "en"
---
## You will learn

Learn about profile properties and how to import them by uploading a CSV file.

This method of adding profile properties to Klaviyo requires that you upload contacts to a list. If your file includes contacts that have not explicitly opted in to email or SMS marketing, exercise caution to ensure you don’t send those contacts unwanted messages, as this can hurt your deliverability. [Learn more about deliverability.](https://help.klaviyo.com/hc/en-us/articles/115005247008)

## Table of contents

To import profile properties using a CSV upload:

1. [Create a properly formatted CSV file](#h_01G3VR2ERGP5SK3JRQDE6686XV).
2. [Upload your CSV file](#h_01G3VR2MDFF51K1TMDXR954279).
3. [Review the import](#h_01G3VR2VQMPA6SZRHPEX3B1BQP).
4. [Ensure compliance](#h_01G3VR33BN9G1TPV69DGT4NSNA).

## Create a CSV file

The first step in uploading profile properties to Klaviyo is creating a correctly formatted CSV file containing those properties. Use any spreadsheet tool to create your file, like Excel or Google Sheets.

1. In your CSV, label the first row of the first column **Email.**
2. In the first cell of the following columns, add the name of the profile properties you'd like to upload (e.g., First Name, Last Name).
3. In the following rows, add in the email address and profile properties you'd like to upload.

![A sample CSV file ready for upload](https://klaviyo.zendesk.com/hc/article_attachments/28717383030171)

Make sure that all the data in your spreadsheet is in a format that can be read by Klaviyo. [Learn more about data types in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115005237648-About-Data-Types), including how to format them.

## Upload profile properties

![Video demonstrating how to import profile properties to Klaviyo](https://fast.wistia.com/embed/medias/v2e7efjdrp/swatch)

Once your CSV file is ready to upload:

1. Navigate to ****Audience > Lists & Segments**** in Klaviyo.
2. In the top right corner select the ****Create New**** button and set the list name and any tags.
3. Choose ****Create List****.
   - If you’re using an existing list rather than a new list, click into the list and open the ****Manage List**** dropdown in the top-right corner, then ****Import Contacts****.
4. Click ****Upload Contacts****.
5. Click ****Upload**** and select the CSV file you just created in the upload modal.
6. Map each column from your CSV to an appropriate property in Klaviyo.
7. If the property doesn’t yet exist in Klaviyo, click the ****Select**** ****or create new**** dropdown and select ****Create new field****.
   ![map.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28717383034011)
8. Click ****Next****.
9. Select **No, import without updating subscription status**.
10. Click****Import****.

Do not update consent status to subscribe these profiles. If you do, all profiles in the list will be marked as subscribers in Klaviyo, even if they've previously unsubscribed. By selecting **No, import without updating subscription status**, anyone with a current subscription will remain subscribed, and unsubscribers will remain suppressed.

Your import may take anywhere from a few seconds to a few hours, depending on the size of your list. You can navigate away from the page and the upload will continue.

Having trouble with your upload? Head to Klaviyo’s guide to [troubleshooting list imports](https://help.klaviyo.com/hc/en-us/articles/115005078807-How-To-Troubleshoot-List-Imports).

## Review your import

Once the import is complete, open up your list and click on any profile. Navigate to the **Information** section of their profile. Here, you’ll find the properties you just uploaded. Many will appear under **Custom Properties**, but note that some default Klaviyo properties, like phone number or first and last name, will appear in the **Contact** section.

Note that if there are any new contacts being added to your list as part of this upload, they will enter any list-triggered flows associated with the list. Temporarily turn off your flow if you are adding new contacts to a list and don't want them to trigger the flow.

## Ensure compliance

In order to maintain strong deliverability and comply with data privacy and marketing laws, make sure you only market to people who have explicitly opted in to email or SMS marketing. If the list you uploaded contains profiles who haven’t opted in, we recommend taking precautions to ensure you don’t reach out to them accidentally. For example, you could:

- Review your segment definitions to confirm only opted-in subscribers are included.
- Delete the list once the upload is complete. To delete the list, but keep the profiles, navigate to the ****Lists & Segments**** tab. Locate the list you just created and click the more options icon (three vertical dots). Click ****Delete****.

To maintain the security of your data, Klaviyo's support team is not able to open your CSV files. For further assistance troubleshooting a list import, [contact the support team](https://help.klaviyo.com/hc/en-us/articles/115001002272-How-to-Contact-Support) with a detailed description of the problem and screenshots of the error you encounter.

## Additional resources

- [About the information section of a profile](https://help.klaviyo.com/hc/en-us/articles/115005247028-About-The-Information-Section-of-a-Profile)
- [Guide to properties](https://help.klaviyo.com/hc/en-us/articles/115005074627-Guide-to-Properties)
- [About data types](https://help.klaviyo.com/hc/en-us/articles/115005237648-About-Data-Types)
- [How to insert personalization into text blocks](https://help.klaviyo.com/hc/en-us/articles/115000096232)