<h1>How to manually import historical event data</h1>

## You will learn

Learn how to manually import historical event data to Klaviyo. While we recommend using Klaviyo-built integrations with platforms such as Shopify, Magento, and BigCommerce, and our API for custom integrations, it's also possible to add this data manually. A common example of this is adding historical purchase data from a previous ecommerce platform that Klaviyo doesn't have a prebuilt integration for.

Please note that there is a limit of 50 MB for CSV uploads.

## Format your data

The first step is to format your data correctly in a CSV file. Below is an example of Placed Order data, along with a description of the fields below. Each row in your CSV file should represent an action or activity someone performed, like "Purchased product" or "Signed up for webinar." If you have multiple actions to track, you should upload them as separate CSV files. Email address must come first when you're uploading your CSV.

Here are some [example event CSVs](https://klaviyo.zendesk.com/hc/article_attachments/8358345129371) you can reference when formatting your data.

### Required fields

The 2 required fields are a timestamp to identify when the event occurred, and a customer property (an email or a unique ID) to identify who performed the action.

- ****Timestamp****: A timestamp showing the day and time of the event. The format is YYYY-MM-DD HH:MM:SS. For example, 1:30pm on November 14th of 2012 would be: **2012-11-14 13:30:00.**

  If two or more events in your CSV file have the same timestamp, you must include a unique `$event_id`, or only one of the events will be imported and the rest will be skipped. See the section on `$event_id` below.
- ****Person//Email or Person//ID****: Most likely, you will use an email to identify your customers. Some customers will also use an unique ID. You can use both if you would like.

### Optional fields

There are 2 special fields to take note of.

- ****$event\_id****: This is a unique identifier for the event. In practice, you should send an `$event_id` if you have a unique identifier for each event (e.g., an order ID). You should also set the `$event_id` if you expect certain events to occur at the same point in time. This can happen when someone takes one action which you will split into multiple events. For example, if someone purchases multiple items, you may want to record 1 event for each item purchased.

  In the 2 sample data sets below there is 1 placed order event, along with 3 ordered product events (1 for each product in the placed order). All of these events have the same timestamp, but they will all be imported because they each have a unique $event\_id. If the $event\_ids were identical, or if they were absent, then only one of the events would be imported and the others would be skipped.
  ![mceclip0.png](https://klaviyo.zendesk.com/hc/article_attachments/28713333717403)![mceclip1.png](https://klaviyo.zendesk.com/hc/article_attachments/28713328091931)
- ****$value****: Use this field if the event you're importing includes a value. For example, if you're importing Placed Order event data, each order will have a value. You do not need to prefix your values with a $ or other currency symbol.

If you have additional data about the person who did something, it should go in a column whose label starts with ****Person//**** and then the type of data that column has. For instance, if you had the company or organization each person belongs to, you'd want to label that column ****Person//Organization****. The special prefix lets us know to associate the data in that column with each person rather than the activity. The following are special columns you can use to help you identify people:

- ****Person//First Name****: first name
- ****Person//Last Name****: last name
- ****Person//Phone****: phone number
- ****Person//Organization****: organization
- ****Person//Title****: job title

If you have additional data about each action, you can include it in extra columns with any labels you want. For instance, if someone purchases something and you want to include what item they bought, you could include that data in a column labeled ****Item Purchased****. Below are some examples.

- ****Item Purchased****
- ****Item Category****
- ****Product****
- ****Location****

If you don't have data for a particular column, leave it blank and we'll ignore it. For instance, if you don't know someone's organization, you can leave the column for ****Person//Organization****blank and we'll skip tracking that property for that row in your data.

Once you're done formatting your data, save it in a CSV file.

## Upload a CSV file of data

After your data is properly formatted, head to Klaviyo.

1. In Klaviyo, select the ****Integrations**** tab.
2. Select ****Manage data > Import via CSV****.
3. You'll be prompted to upload your CSV file, then click ****Next****.
4. You will have the opportunity to name the event. If you are attempting to map the imported data to an event metric that already exists in your account, make sure to type the event name exactly as it already appears.![](https://klaviyo.zendesk.com/hc/article_attachments/30151098171675)
5. Once you've named your event you can preview your data below.
6. When you're ready to import your data click ****Next****. Your file will start to process, and you can navigate away from the page.

## Note for ecommerce stores loading purchase data

If you're uploading purchase data, you'll want to upload two files: one for the overall order, and a second that includes item by item data.  For example, a customer might place an order for multiple products. In this case there would be 1 event for the Placed Order, and then separate events for each of the Ordered Products. Here's what the headers of those files should look like typically:

### Placed Order

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ****Person//Email**** | ****Person//First Name**** | ****Person//Last Name**** | ****Timestamp**** | ****$event\_id**** | ****$value**** | ****Quantity**** | ****Items**** |
| John@gmail.com | John | Smith | 2014-03-10 08:55:01 | 12425 | 49.00 | 2 | ["To Kill a Mockingbird", "Pictionary"] |

### Ordered Product

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ****Person//Email**** | ****Person//First Name**** | ****Person//Last Name**** | ****Timestamp**** | ****$event\_id**** | ****$value**** | ****Quantity**** | ****Item**** |
| John@gmail.com | John | Smith | 2014-03-10 08:55:01 | 12425\_TKM | 24.00 | 1 | To Kill a Mockingbird |
| John@gmail.com | John | Smith | 2014-03-10 08:55:01 | 12425\_P | 25.00 | 1 | Pictionary |

We do not use the `$` to prefix order values. Use just numbers to indicate the price or value of an order. Using the $value header will populate the data correctly in your Klaviyo account.

The reason to include two metrics is that it makes it easier to later trigger emails off of both an overall order and off of specific categories / items.

For Ordered Product events, `$event_id` needs to be a unique identifier for each combination of the order and the product ordered. One easy way to create a unique identifier is to combine the Order ID and Product ID like in the example above.

## Import troubleshooting

Below are some common issues and resolutions you may find when manually importing historical event data.

### My import is taking a long time

Imports can take between 5 minutes and 24 hours depending upon the size of your list. We highly recommending beginning the import of any list at least 24 hours in advance of needing it for a given campaign to ensure the import process does not hold up your send.

### My import keeps failing

If your import fails, it is likely due to one of the following reasons:

- ****Is your file a .csv file?****Your file must be in .csv format. If you attempt to upload an Excel file or a .txt file, the import will fail.
- ****Did you format your Timestamp column correctly?****You should format the date and time as YYYY-MM-DD HH:MM:SS. For example, 1:30pm on November 14th would be: **2012-11-14 13:30:00.** As a second check, open your CSV in a text editor to ensure that any trailing 0s in your timestamps are not being stripped out when you save or export your CSV files. If you're working with data in a spreadsheet, make sure the Timestamp cells are set to the correct timestamp format.
  ![](https://klaviyo.zendesk.com/hc/article_attachments/28713328081691)
- ****Do all required columns have data filled in for every row?****You must have a column labeled **Person//Email** or **Person//ID.**If either of these columns has an empty row, this can cause your import to fail.
- ****Does your **Person//Email** column have invalid email addresses in it?****If you have values within the **Person//Email** that don't have a valid email address format, this can cause your import to fail.
- ****Are all of your columns labeled correctly? Are there any spaces?****Make sure that all of your column headers match what is outlined in this guide. You will also want to make sure there are no spaces in your column names.

## Additional resources

- [Acceptable date and timestamp formats for profile and event properties reference](https://klaviyo.zendesk.com/hc/en-us/articles/115005253428)
- [Formatting dates for CSV files reference](https://klaviyo.zendesk.com/hc/en-us/articles/360039859932)
- [Migrate to Klaviyo](https://help.klaviyo.com/hc/en-us/sections/360011611931)
