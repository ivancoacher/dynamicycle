---
id: "17759932376475"
title: "Understand data warehouse syncing in Klaviyo"
source_url: "https://help.klaviyo.com/hc/en-us/articles/17759932376475-Understand-data-warehouse-syncing-in-Klaviyo"
section: "Syncing"
category: "Advanced KDP & Marketing Analytics"
category_slug: "advanced-kdp-marketing-analytics"
klaviyo_updated: "2026-04-21T13:54:30Z"
language: "en"
---
## You will learn

Learn how to sync data from Klaviyo to your data warehouse, and import warehouse data to Klaviyo via SFTP. You can sync your customer profile and event data, allowing you to store and analyze key information about your customers outside of Klaviyo.

[Advanced KDP](https://help.klaviyo.com/hc/en-us/articles/17655007276059) is not included in Klaviyo’s standard marketing application, and a subscription is required to access the associated functionality. Head to our [billing guide](https://help.klaviyo.com/hc/en-us/articles/115000976672) to learn about how to purchase this plan.

![](https://fast.wistia.com/embed/medias/1luu8fozn2/swatch)

## Before you begin

You will need to ensure that the data warehouse you are connecting with is configured as a destination. To make sure you have set this up correctly:

- Make sure the user that is provided to Klaviyo has the right permissions.
- Make sure to set tables with the appropriate names, shown below, based on your warehouse.

  Additionally, make sure to allowlist Klaviyo's outbound data warehouse traffic IP addresses. This will ensure that Klaviyo's requests are not blocked by your security layer. These addresses are represented by the following CIDR ranges:
- `184.72.183.187/32`
- `52.206.71.52/32`
- `3.227.146.32/32`
- `44.198.39.11/32`
- `35.172.58.121/32`
- `3.228.37.244/32`
- `54.88.219.8/32`
- `3.214.211.176/32`

## Connect to a data warehouse

To add a data warehouse connection to Klaviyo, navigate to ****Advanced KDP >********Data management > Syncing****.

To add a data warehouse, select a supported data warehouse on the **Select a connector modal**.

You can only have 1 data warehouse destination per account.

Alternatively, you can select your data warehouse from Klaviyo’s app marketplace by going to ****Integrations > Explore apps**** and searching for your platform.

When connecting a warehouse, you can either import data from your data warehouse to Klaviyo, or set a warehouse as an outbound sync destination.

![import_export.jpg](https://klaviyo.zendesk.com/hc/article_attachments/29207563157019)

## Import data via SFTP

If you’d like to import data from your data warehouse into Klaviyo, you can do this via [SFTP](https://developers.klaviyo.com/en/docs/use_klaviyos_sftp_import_tool).

To import your data into Klaviyo, select ****Import data**** when first connecting a warehouse destination, or click the ****Import**** button on the **Data syncing** page if you already have a connection established.

The process to import warehouse data into Klaviyo is as follows:

1. Export your desired data from your data warehouse.
2. Generate SSH keys on your local machine.
3. Configure SFTP client and import.

This is demonstrated with Snowflake, but the import process is similar regardless of your warehouse integration.

### Export your database

First, you’ll need to export your data from your warehouse. Log into your warehouse and export the data you’d like to import to Klaviyo into a CSV file.

Format your exported data based on the [CSV format and size limitations](https://developers.klaviyo.com/en/docs/use_klaviyos_sftp_import_tool#general-csv-formatting-and-size-limitations).

### Generate SSH keys on your local machine

Once you have your desired data exported from your warehouse, generate a new SSH key on your local machine and add it to Klaviyo by selecting the ****Add SSH key**** button.

When adding your key, make sure it starts with 1 of the following:

- Ssh-ras
- Ecdsa-sha2
- Ssh-ed
- Sk-ecdsa
- sk-ssh

### Configure SFTP client and import

Once your SSH key has been successfully added to Klaviyo, you’ll need to configure your SFTP client and import the data.

1. Open your SFTP client and configure a new connection with the credentials presented in Klaviyo You’ll see the credentials presented after successfully adding your SSH key
2. Once authenticated, make sure your database follows the recommended guidelines before importing
3. Upload your database file via your SFTP client and review

![configure.jpg](https://klaviyo.zendesk.com/hc/article_attachments/29207563159451)

You’ll also see a list view of your recent imports with the following information:

- ****Status****
  Completed or incomplete.
- ****Rows processed****
  Percentage of total rows processed so far.
- ****Import date****
  Date of import.
- ****Imported by****
  User that imported data.

![Panel.jpg](https://klaviyo.zendesk.com/hc/article_attachments/29207608998811)

## Export data to your warehouse

To configure your data warehouse as destination, you’ll need the following set of information and credentials for each data warehouse.

****Amazon Redshift****

To configure Amazon Redshift as a destination, run the following script to create the **klaviyo\_event** and **klaviyo\_profile** tables.

[“Example](https://www.napkin.io/api/embed/2907a5ae195545d4)

Once configured as a destination, connect your warehouse with Klaviyo using the following set of credentials:

- ****Name:**** The name of your database in Redshift (it’s recommend to use the same same name as your database in Redshift)
- ****Host URL:**** The endpoint of the Amazon Redshift server (called the connection URL in Redshift)
- ****Database:****  The name to identify your data source
- ****Port:**** The port number used by Redshift
- ****Schema:**** Your database schema
- ****Username:**** The username used for logging into Redshift
- ****Database password:**** The password used for logging into Redshift

![Redshift credentials to connect](https://klaviyo.zendesk.com/hc/article_attachments/28705665436571)

****Amazon S3****

To configure Amazon S3 as a destination, set the table names to **klaviyo\_profile** and **klaviyo\_event**.

Once configured as a destination, connect your warehouse with Klaviyo using the following set of credentials:

- ****Name****: The machine readable name for Amazon S3 database.
- ****Bucket****: Your bucket name.
- ****Bucket location****: The region name that was chosen when the storage bucket was created.
- ****Access key ID:**** Your AWS access key ID.
- ****Secret access key****: Your AWS secret access key.

![Amazon S3 credentials to connect](https://klaviyo.zendesk.com/hc/article_attachments/28705665430939)

****Google BigQuery****

To configure Google BigQuery as a destination, run the following script to set the **klaviyo\_profile** and **klaviyo\_event** tables. Your Google BigQuery account must have a payment profile for the connection process to be successful.

Note that in this script you must replace the placeholder "SERVICE ACCOUNT EMAIL" with your BigQuery service account email.

[“Example](https://www.napkin.io/api/embed/5a9fffbe699c45b6)

Once configured as a destination, connect your warehouse with Klaviyo using the following set of credentials:

- ****Name:**** A name to help your identify this destination
- ****Project ID:**** This is known as the Project ID and can be found in your API console.
- ****Dataset:**** Also known as schema. This is the same name you used in the script you should have run for setup.
- ****Service account key:**** Paste the entire contents of the JSON file you downloaded when creating your service account in BigQuery.

![BigQuery credentials to connect](https://klaviyo.zendesk.com/hc/article_attachments/28705638604827)

****Microsoft Azure Synapse Analytics****

To configure Microsoft Azure as a destination, run the following script to create the **klaviyo\_profile** and **klaviyo\_event** tables.

[“Example](https://www.napkin.io/api/embed/9814f97b94764202)

- ****Name:**** It is recommended to use the same name as your database in Azure.
- ****Workspace:**** The Azure Synapse workspace name.
- ****Database name:**** This identifies your Dedicated SQL Pool database.
- ****Username:**** Your login username for your Dedicated SQL Pool database.
- ****Database password:****Your login password for your Dedicated SQL Pool database.
- ****Account name:**** Your Windows Azure storage account, or DNS prefix you created.
- ****Access signature:**** Your shared access signature (SAS) string that proves access to the Blob Storage container.
- ****Container name:**** The Azure Blob container name for temporary staging area for data transfer.

![Azure credentials](https://klaviyo.zendesk.com/hc/article_attachments/28705665467547)

****Snowflake****

To configure Snowflake as a destination, take the following steps:

1. Generate a private key by running the following command in your terminal:

```
openssl genrsa 2048 | openssl pkcs8 -topk8 -inform PEM -out rsa_key.p8 -nocrypt
```

2. Generate a public key that references the private key by running the following command in your terminal:

```
openssl rsa -in rsa_key.p8 -pubout -out rsa_key.pub
```

3. Run the following script to set the **KLAVIYO\_PROFILE**, **KLAVIYO\_EVENT**, and **KLAVIYO\_METRIC** tables. You must have securityadmin and sysadminprivileges in order to complete the setup below. To review what role(s) you have, run SHOW GRANTS TO USER <your\_username> and ensure that you have both roles listed. Reach out to a system administrator if you need to have your role adjusted.

[“Example](https://www.napkin.io/api/embed/06339b3a07a5475f)

Once configured as a destination, connect your warehouse with Klaviyo using the following set of credentials:

- ****Name:**** It’s recommended to use the same name as your database in Snowflake.
- ****Username:**** Username to connect to your database. This should be the same as **user\_name** in the setup script.
- ****Private key:**** The Snowflake private key generated.
- ****Warehouse:**** Your warehouse in Snowflake.
- ****Account:**** Your account in Snowflake.
- ****Database:**** Your database name. This should be the same as **database\_name** in the setup script.
- ****Schema:**** Your database schema. This should be the same as **schema\_name** in the setup script.

![](https://klaviyo.zendesk.com/hc/article_attachments/36251501527707)

After entering your credentials for the data warehouse you are syncing with, choose the data you want to sync from Klaviyo.

### Data objects

In the **Data objects** section you can choose to sync all profile data, just specific event data, or both types of data by checking the applicable box(es) next to each option.

Klaviyo uses a nested JSON structure when sending data to your data warehouse. Profiles and events are each sent as a single table, allowing you to query against 1 table instead of a large number of potential table names in your data warehouse.

![Profile and events data objects](https://klaviyo.zendesk.com/hc/article_attachments/28705638636059)

Syncing all data from Klaviyo may cause you to incur additional charges from your data warehouse.

### Integrations to exclude

In the **Integrations to exclude** field, you can select the specific integration(s) that you want to exclude in the data warehouse sync. This is helpful if you want to remove a specific integration’s data that you may have already connected to Klaviyo from syncing as well.

Excluding specific integration data is only for events data, and does not exclude profile data.

![Integrations to exclude field](https://klaviyo.zendesk.com/hc/article_attachments/28705665480347)

### Selective sync

In the **Selective sync** field, you select the specific events that you want to sync to your data warehouse from Klaviyo. By default, all events are included. When you set specific events to sync with this field, only the selected events will sync.

This field will only appear if you select the **Events** data object.

![Selective sync field](https://klaviyo.zendesk.com/hc/article_attachments/28705665484699)

### Select how often your data will sync

The value set for the **Periodic sync cadence** field in the section called **Select how often your data will sync** defines how frequently a sync will occur from Klaviyo to your data warehouse.

Periodic sync cadence is set to be hourly by default and cannot be changed.

![Periodic sync cadence field](https://klaviyo.zendesk.com/hc/article_attachments/28705665488283)

### Select how much historical data you want to sync

In the **Select how much historical data you want to sync** section, you can define how much historical data you'd like to sync from Klaviyo to your data warehouse during the initial connection. You can pick:

- 30 days
- 90 days
- 1 year
- All time

![Select how much data to sync to your data warehouse](https://klaviyo.zendesk.com/hc/article_attachments/28705665476763)

You may incur additional costs from your data warehouse if syncing a large amount of data at once.

### Sync review

Once you have connected your integration, if the setup was successful, you will see a final screen noting that the connection is **Enabled**, along with:

- Details of the sync you setup
- What data is being shared (profiles, events, or both)
- Any excluded integrations
  ![Connection successful modal](https://klaviyo.zendesk.com/hc/article_attachments/28705665449115)

  If your sync was not successfully connected, you will instead see an **Unable to connect** status, along with options to either retry your connection or to edit the information in your credentials.

  Once you have successfully connected your data warehouse, you will be brought back to the main **Data syncing** list page. Here you will see your:
- Warehouse **Destination**
- The **Enabled** status
- Any potential errors that may have occurred with your sync in the past 24 hours
- The last sync that occurred along with a timestamp of this event

![Card.jpg](https://klaviyo.zendesk.com/hc/article_attachments/29207563162267)

Since you will only ever be able to connect 1 destination, you will only see 1 destination reflected in this list view.

## Data syncing dashboard

Once you have a successful connection, click on your integration from the **Data syncing** list page. From here you will be brought to the data syncing dashboard providing historic and current information on the data syncs that have run.

![Sync interface after connecting warehouse](https://klaviyo.zendesk.com/hc/article_attachments/28705638606491)

Here you’ll see the syncing information split into 2 tabs:

- Historical
- Periodic

### Historical

The **Historical** tab has logs that show the status of your historical data syncs. Historical syncs refer to the syncing of your existing data from Klaviyo to your data warehouse when you establish a connection.

You’ll see the following information for each sync:

- ****Name****
  The data is being included in the sync.
- ****Status****
  Status and potential progress of the sync with an estimated percentage or potential errors noted. These statuses could include:

  - ****Completed****
    Your data finished syncing for this one-off sync. It will not resync again automatically.
  - ****Scheduled****
    When the next sync is scheduled to automatically run.
  - ****In progress****
    Data is actively syncing to your data warehouse with an estimated percentage of completion.
  - ****Errored****
    An error occurred but Klaviyo will keep trying to re-establish a connection. Depending on the integration, this timing may slightly differ.
  - ****Failed****
    The sync completely failed even after trying to re-establish a connection. This means that you will need to review your configuration settings or even data warehouse setup.
  - ****Paused****
    You have paused the sync manually.
  - ****Disabled****
    The sync was disabled because the integration itself was disabled or removed.
- ****Started on****
  Start time of the sync.
- ****Ended on****
  End time of the sync.

### Periodic

The **Periodic** tab has logs that show the status of your periodic syncs. As customers continue to interact with your brand and new data is created, it will be routinely sent to your data warehouse. When setting up a data warehouse connection, periodic syncs will occur every hour.

You’ll see the following information for each sync:

- ****Name****
  The data is being included in the sync.
- ****Status****
  Status and potential progress of the sync with an estimated percentage or potential errors noted. These statuses could include:

  - ****Completed****
    Your data finished syncing for this one-off sync. It will not resync again automatically.
  - ****Scheduled****
    When the next sync is scheduled to automatically run.
  - ****In progress****
    Data is actively syncing to your data warehouse with an estimated percentage of completion.
  - ****Errored****
    An error occurred but Klaviyo will keep trying to re-establish a connection. Depending on the integration, this timing may slightly differ.
  - ****Failed****
    The sync completely failed even after trying to re-establish a connection. This means that you will need to review your configuration settings or even data warehouse setup.
  - ****Paused****
    You have paused the sync manually.
  - ****Disabled****
    The sync was disabled because the integration itself was disabled or removed.
- ****Data freshness****
  Data freshness refers to how up-to-date your data is. For example, if a sync has a freshness of 2 minutes, this means that any new data created in Klaviyo in the past 2 minutes is not yet in your data warehouse.
- Buttons to **Pause**, **Resume**, and re-enable individual syncs.

## Removing data warehouse connections

To delete a data warehouse connection from your Klaviyo account, select the ****Integrations**** tab.

Open the menu next to your data warehouse integration and select ****Remove integration**** to remove the connection.

![integrations_page.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28705638617627)

## View error logs

If you are experiencing issues with data syncing between Klaviyo and your data warehouse, viewing the associated error logs can provide additional information around the cause of the issue.

To view errors, click into your warehouse destination on the **Syncing** page. On both the **Historical** and **Periodic** sync tabs you’ll see a list of the exports and their status, along with an indicator showing whether there are any active errors.

![List of exports to warehouse with information about health and count of errors](https://klaviyo.zendesk.com/hc/article_attachments/28705638663707)

To view more details about a particular error, click into the export experiencing the failure.

Here, you’ll see a timeline of the outbound syncs, along with an error or success message based on the status of the sync.

![Timeline of outbound syncs with health status](https://klaviyo.zendesk.com/hc/article_attachments/28705638666395)

Clicking into a specific error will open a drawer with the following information:

- ****Summary****
  A brief description of the error returned by the data warehouse
- ****Code****
  The error code for the error
- ****External message****
  The actual error message returned by the data warehouse
- ****Date****
  The date and time of the error

![Drawer with information about syncing error](https://klaviyo.zendesk.com/hc/article_attachments/28705638658459)