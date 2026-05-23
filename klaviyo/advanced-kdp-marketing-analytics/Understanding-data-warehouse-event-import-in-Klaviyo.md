---
id: 45442043369499
title: "Understanding data warehouse event import in Klaviyo"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/45442043369499-Understanding-data-warehouse-event-import-in-Klaviyo"
section: "Syncing"
category: "Advanced KDP & Marketing Analytics"
category_slug: "advanced-kdp-marketing-analytics"
klaviyo_updated: "2026-04-21T13:55:02Z"
language: en
---

****Note:**** Data warehouse import is part of [Advanced KDP](https://help.klaviyo.com/hc/en-us/articles/17655007276059) and is not included in Klaviyo’s standard marketing application. A subscription is required to access this functionality.

# Understanding data warehouse event import in Klaviyo

## You will learn

Learn how to use ****data warehouse event import**** to sync event data from your warehouse into Klaviyo, so you can power segments, flows, and reporting with behavior that originates outside of Klaviyo’s native integrations (e.g., POS systems, support platforms, or custom applications).

---

## What is data warehouse event import?

****Data warehouse event import**** lets Klaviyo connect directly to your data warehouse and configure ****import syncs**** from warehouse tables or views that contain event data.

Each row in your source table is treated as a single event in Klaviyo:

- The row’s timestamps, metric name, and identifiers define ****what happened****, ****when****, and ****for whom****.
- Additional columns become ****event properties**** that you can use in segmentation, flows, and analytics.

Event import is built on the same data warehouse import infrastructure as profile import, but targets Klaviyo’s event ingestion pipeline instead of profiles.

---

## How does data warehouse event import work?

After you connect Klaviyo to your warehouse and configure an event sync:

1. ****Klaviyo queries your warehouse**** for the configured table or view.
2. On each run, Klaviyo reads only rows whose ****change detection timestamp**** is newer than the last successful sync. This allows incremental imports without reprocessing the entire table.
3. Each row is then processed as follows:

   - Klaviyo determines the ****metric name**** (event type) based on options selected during sync setup: either a single chosen metric or dynamically based on the value of a designated metric name column in the source table.
   - ****Event timestamp****, ****profile identifiers****, and optional ****unique ID****, ****value****, and ****value currency**** are set based on field mappings configured during sync setup.
   - All remaining columns are ingested as ****event properties****, using the column names as property names. Column names with three underscores (e.g., `parent___child1`, `parent___child2`) can be used to create an event property (`parent`) with child properties.
4. Klaviyo loads the resulting events into your account, where they behave like other ****custom API metrics**** in segmentation, flows, and analytics.

Imports run on a ****recurring cadence**** (e.g., hourly), so new or updated rows in your warehouse are regularly translated into events in Klaviyo.

---

## Before you begin

Make sure the following requirements are met before creating an event import sync:

- Your account has access to ****Advanced KDP**** and ****data warehouse import****.
- You have created and validated a ****data warehouse connection**** in Klaviyo. See the support center articles for your data warehouse for details on the required service account and schemas.
- Your source table or view contains the required columns below.
- You have sufficient privileges in your warehouse to expose the necessary tables/views to Klaviyo’s service user.

---

## Source table structure for events

To ensure that your event data can be imported correctly, your source table or view must satisfy Klaviyo’s ****required fields**** and structure.

### Required fields

The following columns are required in V1 of data warehouse event import:

| Column | Required? | Type | Description |
| --- | --- | --- | --- |
| ****Event timestamp**** | Required | Timestamp / datetime | When the event occurred. |
| ****Metric name**** | Required if a single metric is not selected during sync configuration setup. | String / text | The event or metric name (e.g., `Placed Order`, `Support Ticket Opened`). |
| ****Profile identifier**** | Required (at least 1) | String / text | One of: email, phone number, external ID, or Klaviyo ID. You can include multiple in the row but must map at least one. |
| ****Change detection timestamp**** | Required | Timestamp | Stable timestamp used to detect new or updated rows since the last run. Must be ****different**** from the event timestamp so you can safely import historical events. This should reflect when the row was added to the dataset and must be stable for syncing to work correctly. |

### Optional fields

These fields are ****recommended**** when applicable but not strictly required:

| Column | Required? | Type | Description |
| --- | --- | --- | --- |
| ****Unique ID**** | Recommended | String / Number | Unique identifier of the event (used for deduplication). |
| ****Value**** | Recommended | Number | Numeric value for the event (e.g., order total, points used). Maps to the `value` top-level field in Klaviyo’s event model. |
| ****Value currency**** | Recommended | String / text | Currency code associated with `value` (e.g., `USD`). Maps to the `value_currency` top-level field. |

### Event properties

All other columns in your table are treated as ****event properties****:

- Columns are imported as ****flattened properties****, with the column name used directly as the property name in Klaviyo.
- You don’t need to explicitly map every property; unmapped columns will be included as event properties.
- Nested JSON can be stored inside an individual property value if needed (for example, a JSON object of line items), but the ****property name itself**** comes from a top-level column.

Klaviyo performs ****best-effort type parsing**** for event properties and does not provide per-field transformation logic as part of the event import setup.

---

## Common use cases

Customers typically use data warehouse event import for:

### 1) Importing offline or POS events

Bring in ****in-store or offline events**** (e.g., POS purchases, returns, or appointments) from your warehouse so that they behave like other Klaviyo events and metrics.

****Examples:****

- `In-Store Purchase` events with order totals, store location, and tender type
- `Appointment Completed` events with staff member, service type, and duration

### 2) Service and support interactions

Sync ****support and service events**** like ticket creation, resolution, or returns to enrich your customer timelines and power messaging based on service history.

****Examples:****

- `Support Ticket Created` and `Support Ticket Resolved`
- `Order Returned` with reason codes and refund amounts

### 3) Modeled or derived events

Convert ****warehouse-modeled behaviors**** into events that are easier to use in Klaviyo.

****Examples:****

- `High Churn Risk` events generated from a model in your warehouse
- `Lifecycle Milestone Reached` events when a customer moves stages in a custom lifecycle model

---

## Set up a data warehouse event import sync

### 1) Connect your data warehouse

If you haven’t yet connected your warehouse:

1. In Klaviyo, go to ****Advanced KDP > Data management > Syncing****.
2. Click ****Add data warehouse**** and select your warehouse connector.
3. Complete the connection steps for your platform following the applicable connection guide linked from the data warehouse import overview article.

Klaviyo supports one active data warehouse connection per account.

### 2) Create a new event import sync

Once your warehouse is connected:

1. From ****Advanced KDP > Data management > Syncing****, select your warehouse connection.
2. Choose ****Import data**** (if you are configuring imports for the first time) or click ****Create sync**** / ****Add sync**** for an existing connection.
3. When prompted for the ****data type****, select ****Events**** (instead of Profiles).
4. Choose the ****table or view**** in your warehouse that contains the events you want to import.

### 3) Map required fields

Next, you’ll map columns from your warehouse table to Klaviyo’s required event fields.

The event import configuration requires you to provide mappings for:

- ****Event timestamp****
- ****Metric name**** (either a constant you select in the configuration or a column that contains the metric name per row)
- ****Profile identifier**** (at least one)
- ****Change detection timestamp****

  You can also map recommended fields:
- ****Unique ID****
- ****Value****
- ****Value currency****

Any remaining columns that you don’t explicitly map to these core fields automatically become ****event properties****.

The configuration UI prevents you from mapping multiple columns to the same top-level field and validates that all required fields are present before allowing you to save.

### 4) Choose sync cadence and historical scope

When you save your event import:

- Klaviyo schedules ****recurring syncs**** to run at a regular cadence (typically hourly).
- On each run, only rows whose ****change detection timestamp**** is newer than the last successful run are processed, ensuring that imports are incremental.

  For historical backfill, you can either:
- Point your event import at a table or view that already includes all relevant historical events, or
- Start with a dedicated historical table and later switch to a change-data-capture-backed view for ongoing updates.

---

## How imported events behave in Klaviyo

Once imported:

- Each row appears as an event of a ****custom API metric**** in Klaviyo.
- The metric name you mapped (or configured as a constant) determines the event type name you see in the product (for example, `Placed Order`).
- All profile identifiers are resolved to existing profiles where possible; otherwise, Klaviyo creates new profiles using the identifier fields provided, similar to other event ingestion paths.

  You can use these events to:
- Build segments based on ****what someone has done**** and filter on event properties.
- Trigger and filter flows.
- Analyze behavior in metrics and reporting alongside events from other sources.

---

## Limitations and best practices

Keep the following in mind when using data warehouse event import:

- V1 of event import focuses on ****event data only****. Profile property updates derived from events may be added in a later iteration; for now, profile properties should be updated via profile import or other supported paths.
- The ****change detection timestamp must be different from the event timestamp****. Using the same column for both can prevent you from safely importing historical events after your first sync.
- For optimal speed, set the change detection field to the timestamp of when the new table is created. Records are batched in sync cycles using this value, so the time to import historical records can be reduced if all historical records have a change detection timestamps in a narrow range (e.g. the timestamp of a job that creates the new table).
- Use a stable ****unique ID**** per event where possible to improve deduplication and make downstream debugging easier.
- If your table contains multiple event types (metrics) with different sets of columns, it’s generally fine to keep them together: columns that are NULL for particular rows are simply ignored for those events in Klaviyo.
- For complex nested objects (e.g., line item arrays), we recommend flattening into multiple columns where feasible, especially for properties you expect to use in segmentation or flows.

```