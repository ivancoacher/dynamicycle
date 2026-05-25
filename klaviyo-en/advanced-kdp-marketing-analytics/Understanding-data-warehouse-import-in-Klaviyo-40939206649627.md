---
id: "40939206649627"
title: "Understanding data warehouse import in Klaviyo"
source_url: "https://help.klaviyo.com/hc/en-us/articles/40939206649627-Understanding-data-warehouse-import-in-Klaviyo"
section: "Syncing"
category: "Advanced KDP & Marketing Analytics"
category_slug: "advanced-kdp-marketing-analytics"
klaviyo_updated: "2026-04-21T13:54:55Z"
language: "en"
---
![Snowflake-updated.gif](https://klaviyo.zendesk.com/hc/article_attachments/41426468027419)

[Advanced KDP](https://help.klaviyo.com/hc/en-us/articles/17655007276059) is not included in Klaviyo’s standard marketing application, and a subscription is required to access the associated functionality. Head to our [billing guide](https://help.klaviyo.com/hc/en-us/articles/115000976672) to learn about how to purchase this plan.

## Introduction .

Data warehouse import allows Klaviyo to connect directly to your Snowflake or BigQuery data warehouse and configure import syncs for tables (or views) of profile data.

Events and custom object import syncs are coming soon, as is support for additional data warehouses.

## How does data warehouse import in Klaviyo work?

After establishing a connection to your warehouse, you can select a dataset (e.g. a table or a view) to sync.

The dataset must contain a profile identifier and a modified\_at timestamp. Data columns can be mapped to specific profile properties, including custom properties.

At the desired interval (e.g. hourly, daily), Klaviyo will extract any records that were created or modified since the last run and then import them, creating or updating profiles accordingly.

If you do not have a fully-joined dataset with all the fields you want to sync, you can create multiple syncs with different field mappings (e.g. contact info, loyalty balances, and custom segments).

E-mail and text messaging consent work the same way file or SFTP uploads do in terms of valid values and formats.

## Common use cases

### Profile management

- Create new profiles in Klaviyo that originate in systems not directly integrated with Klaviyo (e.g. POS, reservation, or order management systems)
- Update profile info in Klaviyo from offline sources that are available in-warehouse.

### Profile enrichment

- Sync loyalty program balances to a custom Loyalty\_Balance property.
- Sync scores or categories from custom models running in the warehouse (e.g. intent scores for bespoke lifecycle events, affinity categories, churn risk, or LTV metrics.)
- Sync third party demographic or behavioral enrichment data to custom profile properties
- Sync support or service touch points into custom profile fields to represent whether the customer has open service requests, days since last service visit, or the most recent category of support interaction.

### Custom segmentation

- Perform complex segmentation in-warehouse and sync the segment names to custom profile properties to use as criteria in segments or flows.
- Perform segmentation in-warehouse based on sensitive, confidential, or regulated data and sync segment group assignments or profile flags with sanitized names (e.g. Group A, Group B) as a custom profile property

## Setup Guide

### Establishing a connection

These articles provide step-by-step instructions for setting up data warehouse import.

[****Connecting Klaviyo and Snowflake****](https://klaviyo.zendesk.com/hc/en-us/articles/41373252392731)

[****Connecting Klaviyo and BigQuery****](https://klaviyo.zendesk.com/hc/en-us/articles/41406928654107)

[****Connecting Klaviyo and Redshift****](https://klaviyo.zendesk.com/hc/en-us/articles/42790298131611)

[****Connecting Klaviyo and Databricks****](https://klaviyo.zendesk.com/hc/en-us/articles/42790208080283)

### Importing Event Data

[Understanding Data Warehouse Event Import](https://klaviyo.zendesk.com/hc/en-us/articles/45442043369499)

### Debugging New Syncs

If you've set up a new sync and are not seeing profiles updated as you might expect, we recommend utilizing the error reporting in the web-based list upload tool to validate your data, especially in the case of consent fields and timestamps.

****To identify any potential errors in your source data:****

1. Export your source table/view to a CSV file.
2. Go to [Audience | Lists & Segments](https://www.klaviyo.com/lists) in your dashboard.
3. Select an existing list or create a new list for testing purposes
4. Select **Import contacts** in the **Manage List** menu in the top right.
5. Upload your csv file from step #1.
6. If there are any issues with the data that would prevent a successful sync from completing, they will be made available in a downloadable error file.