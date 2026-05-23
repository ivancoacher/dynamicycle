<h1>How to unset profile properties</h1>

## You will learn

Learn how to bulk remove profile properties from profiles in Klaviyo. If you have a profile property that you’d like to remove for a group of profiles, you can do this using a CSV upload.

## Unset profiles with a CSV upload

The Klaviyo property **$id** cannot be unset. If you need to remove this property, reach out to [Klaviyo’s support team](https://help.klaviyo.com/hc/en-us/articles/115001002272).

First, group all the profiles you want to remove a property for in a list or segment, and [export the group](https://help.klaviyo.com/hc/en-us/articles/115005078687). When you export the group, you only need to select the properties you’d like to remove.

Once you have the exported CSV file, you’ll need to update it to match the following structure:

1. The first column should have the header **Email**, with each row corresponding to the email address of a profile that will have the property removed.
2. The second column should have the header **$unset**, with each row containing the names of properties to be removed. This must be in a list format (e.g., (“Property A”, “Property B”, “Property C”)).

To unset a native Klaviyo property, add the prefix $. For example, to unset the [Klaviyo property](https://help.klaviyo.com/hc/en-us/articles/115005074627#h_01HA32RZBA24MZSHF2MQK71861) city, use $city in your CSV file.

![unsetCSV.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28716118917915)

When your file is correctly formatted and ready to upload, select a new or existing list to [upload the profiles](https://help.klaviyo.com/hc/en-us/articles/115005251128) to.

![The import contacts button](https://klaviyo.zendesk.com/hc/article_attachments/28716118928923)

On the **Import contacts page** you are brought to, map the column with your properties to the Klaviyo field **$unset**, and set the data type of that column to **List**.

When mapping your file, you’ll have to manually write this in using the “Create new field” option, as **$unset** will not populate by default.

![$unset.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28716118919707)

Once you are done mapping, select ****Next**** and the relevant properties will be removed from the profiles included in the file once successfully uploaded.

## Additional resources

[Profile properties reference](https://help.klaviyo.com/hc/en-us/articles/115005074627)

[How to export a list or segment](https://help.klaviyo.com/hc/en-us/articles/115005078687)
