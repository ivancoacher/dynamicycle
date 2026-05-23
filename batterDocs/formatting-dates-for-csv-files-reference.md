<h1>Formatting dates for CSV files reference</h1>

## You will learn

Learn how to edit dates in Excel and Google files to match the required date format in Klaviyo. This will make the process of uploading a CSV with customer data seamless and help you avoid upload errors.

When you run an ecommerce business that sells to customers around the world, many of these customers will format dates differently. Likewise, when you import dates from an Excel or Google File, these systems may reformat dates according to their default date settings. For example, Excel may reformat “March 1, 2020” to “1-Mar”.

When you import dates with timestamps, map this field to the date data type in Klaviyo. However, if you import a date without a timestamp, a default time of midnight UTC is applied if mapped to the date data type. This may cause date based flows to send a day early or late depending on the account’s timezone. For that reason, if you only upload dates (no timestamps), map them to the text data type instead.

## Acceptable date and timestamp formats

See the example below for information around formatting your date and timestamps in a CSV file. Note that, you must format dates as either YYYY-MM-DD or MM/DD/YYYY. If there's no time of day associated with your date, you can set it to midnight by using the HH:MM:SS value 00:00:00.

If you do not include seconds on your timestamps they will default to 0. For example, a timestamp of `2014-09-30 13:34` would be submitted to Klaviyo as `2014-09-30 13:34:00`

For example, the date September 30, 2014, at 1:34:08 pm should be formatted using one of the following supported formats:

- `2014-09-30 13:34:08`
- `2014-09-30 13:34:08+00:00`
- `09/30/2014 13:34:08`
- `09/30/14 13:34:08`
- `09/30/2014 13:34`
- `09/30/14 13:34`
- `2014-09-30T13:34:08`
- `2014-09-30 13:34:08.000001`
- `2014-09-30T13:34:08.000001`
- `2014-09-30 13:34:08.000001-04:00`
- `1412098448` (Unix)

## Microsoft Excel

### Edit for consistency

To edit dates and timestamps within an Excel file, first select the cells that you want to reformat. Press ****Command+1**** or ****Control+1**** (if you are using a macOS) or ****CTRL+1**** (if you are using Windows).

![Sample Excel data with dates](https://klaviyo.zendesk.com/hc/article_attachments/28716330281755)

A **Format Cells** popup will appear. Select ****Number**** from the main tab (if it is not already selected), and under **Category**, select ****Date****.

![Excel's date format options menu](https://klaviyo.zendesk.com/hc/article_attachments/28716353282203)

Under **Type**, choose your desired date format. Make sure that you [choose a date and timestamp format that is supported within Klaviyo](https://klaviyo.zendesk.com/hc/en-us/articles/115005253428).

For example, if you select ****2012-03-14**** (which is supported in Klaviyo) it will reformat each selected cell to reflect this formatting, as shown below.

![Sample data in Excel with consistent date formatting](https://klaviyo.zendesk.com/hc/article_attachments/28716330289307)

### Edit for location

You can also change date formatting by location, or locale, under **Language** **(location)** in the **Format Cells** popup.

In the above example, **English (United States)** is selected; thus, the dates will reflect US formatting (MM/DD). However, if you based in the UK, for example, and want dates to reflect the UK formatting (DD/MM), select ****English (United Kingdom)**** from the dropdown.

![The Excel language setting](https://klaviyo.zendesk.com/hc/article_attachments/28716330296603)

Once your Excel file reflects the correct date/timestamp formatting, click ****File**** > ****Save As****. Save your file as a CSV.

Then, head back to your Klaviyo account and [upload your CSV file to a list](https://help.klaviyo.com/hc/en-us/articles/115005078967).

If these customers already exist in your account, when you upload your CSV to your list, new profiles will not be added. Instead, their profile will be updated to reflect the changes you make when you map fields. This will avoid duplicating customer information and cluttering your account.

## Google Sheets

### Edit for location

You can change dates in Google Sheets to reflect your native date format, or locale, as well. For example, if you are in the UK, you may want to change the US date formatting (MM/DD) to UK formatting (DD/MM).

To do so, head to ****File**** > ****Spreadsheet Settings****. The following popup will appear.

![Google Sheets' setting modal](https://klaviyo.zendesk.com/hc/article_attachments/28716330299931)

Edit the **Locale** to reflect your location by selecting your country in the dropdown. You can also edit the **Display language** and **Time zone** as well. Then, click ****Save settings****.

If you're in the UK, set your **Locale** as ****United Kingdom**** and save this change. After saving, your dates will reformat to reflect this change.

Ideally, edit **Locale** prior to reformatting for consistency. However, if you edit **Locale** second and then do not immediately see a change to your cells, simply select them again and click ****Format**** > ****Number**** > ****Date****. Google Sheets will then update to reflect location changes.

### Edit for consistency

To edit dates and timestamps for consistency within a Google spreadsheet, select the cells that you want to reformat.

![A set of data in Google Sheets with dates](https://klaviyo.zendesk.com/hc/article_attachments/28716330305563)

Select ****Format**** > ****Number**** > ****Date**** (or ****Date time**** if you want to edit both the date and time in your file).

![The date formatting option in a dropdown menu in Google Sheets](https://klaviyo.zendesk.com/hc/article_attachments/28716330310555)

This will update your dates to reflect the default Google Sheets formatting, as shown in the image below.

![A set of data in Google Sheets with consistently formatted dates](https://klaviyo.zendesk.com/hc/article_attachments/28716330313883)

Alternatively, you can find date information by selecting the ****123**** dropdown.

![The Date option from the 123 menu in Google Sheets](https://klaviyo.zendesk.com/hc/article_attachments/28716353308315)

Now that you have one consistent format across your spreadsheet, make sure that it aligns with [Klaviyo’s guidelines for formatting dates and timestamps](https://klaviyo.zendesk.com/hc/en-us/articles/115005253428).

In the example above, the date does not include 0s in the Month and Day listed which are needed when you upload dates in Klaviyo. If this is the case and you need to update the default format, select ****More Formats****.

Then click ****More date and time formats****. Alternatively, you can create your own custom format.

![The option to further customize dates in Google Sheets](https://klaviyo.zendesk.com/hc/article_attachments/28716353310235)

After selecting ****More data and time formats****, a popup will appear showing your current date format. You can then choose from a variety of options. Select your desired format. Then, click ****Apply****.

For example, you may choose ****08/05/1930**** which is an acceptable format in Klaviyo.

![A custom date and time format](https://klaviyo.zendesk.com/hc/article_attachments/28716353313307)

This will update all of your dates to appear in your desired format which can then be uploaded into Klaviyo.

![A date column in Google Sheets with consistently formatted dates](https://klaviyo.zendesk.com/hc/article_attachments/28716353322139)

From there, navigate to ****File**** > ****Download****, and download your Google Sheet as a CSV file. Next, you will be able to [upload your CSV file to a Klaviyo list](https://help.klaviyo.com/hc/en-us/articles/115005078967).

If these customers already exist in your account, when you upload your CSV to your list, new profiles will not be added. Instead, their profile will be updated to reflect the changes you make when you map fields. This will avoid duplicating customer information and cluttering your account.

To maintain the security of your data, Klaviyo's support team is not able to open your CSV files. If you need assistance troubleshooting a list import, [contact the support team](https://help.klaviyo.com/hc/en-us/articles/115001002272) with a detailed description of the problem and screenshots of the error you encounter.

## CSV upload example

Below is an example of what this CSV file may look like as you upload it with the correct date/time formats.

![Example of a CSV with dates and times](https://klaviyo.zendesk.com/hc/article_attachments/30318677964699)

## Additional resources

- [Acceptable date and timestamp formats for profile and event properties](https://klaviyo.zendesk.com/hc/en-us/articles/115005253428)
- [Profile properties reference](https://klaviyo.zendesk.com/hc/en-us/articles/115005074627)
