<h1>Troubleshooting list imports</h1>

## You will learn

Learn how to troubleshoot errors that occur when uploading a CSV of contacts to a [new](https://help.klaviyo.com/hc/en-us/articles/115005078967-How-to-Create-and-Add-Contacts-to-a-New-List) or [existing](https://help.klaviyo.com/hc/en-us/articles/115005251128-How-to-Add-Subscribers-to-an-Existing-List) list in Klaviyo. Uploading reviews? Head to our article on [how to import reviews](https://klaviyo.zendesk.com/hc/en-us/articles/16318811222555).

## Before you begin

Want to make sure your file will import? Check the list of requirements below before importing your list.

- CSV file (not any other format)
- File size is 50 MB or less
- First row is headers
- Every row has either an email address or phone number associated with it
- There are no duplicate email addresses or phone numbers

Our Support Team is not able to import CSVs into Klaviyo on your behalf. If you need help with an import, please check out the troubleshooting section below for tips on how to successfully troubleshoot list import issues.

Having trouble uploading a list of profiles with SMS consent? [Check out Klaviyo’s Guide to uploading a list of SMS contacts](https://help.klaviyo.com/hc/en-us/articles/360035428731-Guide-to-Uploading-a-List-of-SMS-Contacts).

## Table of contents

- [Import delay](#h_01GDX6VNGXEC6Q29276AAZ95NK)
- [Import troubleshooting](#h_01GDX6VV934GDAPXKT5JVR6GJP)
- [All columns imported as a single field](#h_01GDX6W19CFB7EZNBJJ3KQ9KJB)
- [Invalid format error messages](#h_01GDX6WA4G3JEK59T8XP3FJET7)
- [Incorrect date or timestamp formatting](#h_01GDX6WGB9M5X22TZVQZPA9NNZ)
- [Duplicate or missing unique identifier error messages](#h_01GDX6YR7EJ5RPWX0PATF4PNZA)
- [Missing value in a required field](#h_01GDX6YY8A2BSR940SPF5XK3EK)
- [Phone number formatting issues](#h_01GDX70JJVTSZ58NRVRHB63HSC)

## Import delay

If you import a large file with a significant amount of data, the import process may take several hours to complete. Unfortunately, there is no way to speed up this process once it has begun. However, one way to preemptively expedite the import process is to remove all duplicate emails from your CSV before importing. We highly recommend planning to import a new list at least one day in advance of when you intend to email the contacts on the list.

After an import begins, you will initially see a status bar. If you click away, you’ll still be able to track the import’s progress by watching the list count increase over time. We will send you an email as soon as a list import completes.

## Import troubleshooting

If your list fails to upload, look for the following common errors in your CSV file that may be causing this roadblock:

### All columns imported as a single field

If you are using a version of Excel that does not use English as the default language, your software may use semicolons and not commas as the separator in your file. If this is the case, your file may look like this upon import:

![Semicolon delimiter.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28717386063131)

To remedy this, head to your computer's ****Number format**** or ****List (or Number) Separator**** setting. This setting is likely within the ****Language & Region**** settings, and may be located within the ****Advanced Settings**** section. Replace the semicolon with a comma and save. Now when you export files as a CSV, they will use the comma format. Note that the exact location of this setting may differ across operating systems.

![2017-05-22_14-59-31.png](https://klaviyo.zendesk.com/hc/article_attachments/28717386060699)

Also, check to make sure that your CSV aligns with Klaviyo’s formatting requirements. If you have not already, head to our documentation on [formatting your data](https://help.klaviyo.com/hc/en-us/articles/115005078967). For example, one of the required fields is for email addresses.

### Troubleshooting invalid format error messages

When you import a list into Klaviyo, the field mapping page enables you to match any properties to their corresponding data type in Klaviyo. For example, **Email** always has a **Text** data type; whereas, if you upload a custom property for **Birthday**, you will want to set the data type to **Date**.

Review the data types, acceptable formats, and examples below.

- ****Text****
  Any text, or combination of text and numbers. If you are unsure what format your data is in, choose this option.
  - Examples:
    email@example.com
    Hello, world
    $5.00
- ****Numeric****
  All numbers. Do not include currency symbols in numeric fields.
  - Examples:
    2
    5.0031
    130.0
- ****Boolean****
  True or false values.
  - Examples:
    true
    false
- ****Date****
  Reference our guide to [acceptable date and timestamp formats for profile and event properties](https://help.klaviyo.com/hc/en-us/articles/115005253428) to learn about accepted date formats.
  - Example:
    2014-09-01 13:34:08
- ****List****
  Data must be formatted as a JSON array.
  - Examples:
    ["apples","bananas","oranges"]
    ["apples"]
- ****Consent****
  Consent is formatted as the channel (email, SMS, etc.) and the type of consent (if there are multiple types available in Klaviyo). The only option for email is **Email Marketing Consent**; for SMS, it would be either **SMS Marketing Consent** or **SMS Transactional Consent**; etc. The value of this field must be "Subscribe," "Never Subscribed," or "Unsubscribed."

For more information about what the different data types entail and which to select when importing your list, head to our guide on [understanding data types](https://help.klaviyo.com/hc/en-us/articles/115005237648).

To learn more about “Invalid [data type] format” error messages (e.g., “Invalid list format”), head to our [troubleshooting guide for invalid format error messages](https://help.klaviyo.com/hc/en-us/articles/8557592023451).

### Incorrect date or timestamp formatting

You may be using the wrong format for dates or timestamps. If you have included either and are unsure of Klaviyo’s accepted formats, head to our guide on [acceptable date and timestamp formats for profile and event properties](https://help.klaviyo.com/hc/en-us/articles/115005253428).

### Troubleshooting duplicate or missing unique identifier error messages

#### Duplicate identifiers

Records skipped due to "Duplicate Unique ID" mean that an email address or phone number was repeated in your file. In these cases, Klaviyo will process the data from the first row containing the repeated identifier and will provide all non-processed records in a downloadable file.

Click ****Download Skipped Records**** to see the contacts skipped due to duplicate identifiers and re-upload these skipped records if needed.

#### Missing unique identifiers

Records skipped due to “Missing Unique ID” mean the skipped rows did not contain an email address, phone number, or other accepted unique identifier.

Click ****Download Skipped Records**** to see the contacts skipped due to missing identifiers, add an email address or phone number for each one, and re-upload your new file.

### Missing value in a required field

Check that all required fields have values associated with them. For example, if one of your contacts listed is missing an email address under the email column, you will see an error when uploading. Check to make sure that each contact you wish to upload has a value for all required fields. If they are empty, fill them in prior to your next attempt to upload.

Invalid email address or unrecognized characters

If you receive this error message, check the email addresses in your file for invalid characters. Invalid characters include `( ) , : ; [ / ]`, as well as spaces.

To maintain the security of your data, Klaviyo's support team is not able to open your CSV files. For further assistance troubleshooting a list import, [contact the support team](https://help.klaviyo.com/hc/en-us/articles/115001002272-How-to-Contact-Support) with a detailed description of the problem and screenshots of the error you encounter.

### Transferring profiles across accounts

When transferring profiles from one account to another, there are some [properties](https://help.klaviyo.com/hc/en-us/articles/115005074627) that cannot be uploaded to another account.

For example, **Profile created on** cannot be transferred because it is set to the date when a profile is created in the account. Another set of examples are **First Active** and **Last Active**, as these are automatically set based on profile activity on the account.

## Phone number formatting issues

Phone numbers must include a country code or a separate column indicating their country, and must follow an accepted phone number format. Learn how to [properly format and upload phone numbers](https://help.klaviyo.com/hc/en-us/articles/360035428731).

## Additional resources

- [Add subscribers to an existing list](https://help.klaviyo.com/hc/en-us/articles/115005251128)
- [Create and add contacts to a new list](https://help.klaviyo.com/hc/en-us/articles/115005078967)
- [Acceptable date and timestamp formats](https://help.klaviyo.com/hc/en-us/articles/115005253428)
