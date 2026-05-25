---
id: "42790208080283"
title: "Connecting Klaviyo and Databricks"
source_url: "https://help.klaviyo.com/hc/en-us/articles/42790208080283-Connecting-Klaviyo-and-Databricks"
section: "Syncing"
category: "Advanced KDP & Marketing Analytics"
category_slug: "advanced-kdp-marketing-analytics"
klaviyo_updated: "2026-04-21T13:54:56Z"
language: "en"
---
[Advanced KDP](https://help.klaviyo.com/hc/en-us/articles/17655007276059) is not included in Klaviyo’s standard marketing application, and a subscription is required to access the associated functionality. Head to our [billing guide](https://help.klaviyo.com/hc/en-us/articles/115000976672) to learn about how to purchase this plan.

# Environment Setup and Connection

****Overview:**** Follow these steps to prepare Databricks for Klaviyo. You’ll create required **schemas** (in a catalog), set up a dedicated account and access token for Klaviyo, assign the minimum required privileges, verify the configuration, and connect Databricks to Klaviyo.

****Important:**** The Databricks connection currently supports ****importing data into Klaviyo**** only.

- ****Profiles**** and ****Events**** can be imported now.
- ****Exporting to Databricks**** is not yet available. Until then, exporting to S3 is recommended.
- ****Unity Catalog**** is required. To connect to a Databricks instance that uses Hive metastore (HMS), consider [Hive metastore federation](https://docs.databricks.com/aws/en/query-federation/hms-federation-concepts).

For details on how data warehouse imports work in Klaviyo—including schema structure, required tables, and field mappings—see [How Data Warehouse Imports Work in Klaviyo](https://klaviyo.zendesk.com/hc/en-us/articles/40939206649627) and [Understanding Data Warehouse Event Import.](https://klaviyo.zendesk.com/hc/en-us/articles/45442043369499)

---

## 1) Create Required Schemas

In Databricks, ****schemas**** (sometimes called databases) live ****inside a catalog****. You can use the default `main` catalog or another catalog if your workspace uses Unity Catalog.

```
USE CATALOG main;  -- or your organization’s designated catalog
CREATE SCHEMA IF NOT EXISTS KLAVIYO_IMPORT_FROM_DWH;
CREATE SCHEMA IF NOT EXISTS KLAVIYO_TMP;
```

- `KLAVIYO_IMPORT_FROM_DWH`: Tables and views created in this schema will be available for selection when configuring a new sync.
- `KLAVIYO_TMP`: temporary/staging data used during sync.

****Note:**** If your workspace does not use Unity Catalog, Databricks treats “schema” and “database” as equivalent. You can use `CREATE DATABASE` instead of `CREATE SCHEMA`.

---

## 2) Create the Klaviyo Service Account and Access Token

Klaviyo authenticates to Databricks using a dedicated account with a ****personal access token (PAT)****. Use a non-human (service) account when possible and store the PAT securely (e.g., a password manager or secret store). You will provide this token to Klaviyo during initial setup.

### 2.1 Create the account

Create a Databricks workspace user or a service principal that Klaviyo will use exclusively for this integration.

### 2.2 Generate the personal access token

- ****Workspace user account:**** Generate the token via the Databricks web UI (see Databricks docs): [Create personal access tokens for workspace users](https://docs.databricks.com/aws/en/dev-tools/auth/pat#create-personal-access-tokens-for-workspace-users)
- ****Service principal:**** Generate the token using the Databricks CLI (see Databricks docs): [Create personal access tokens via the Databricks CLI](https://docs.databricks.com/aws/en/dev-tools/auth/pat#create-personal-access-tokens-for-service-principals)

****Important:**** Treat the PAT as a secret. Anyone with the token can access Databricks with the associated account’s permissions.

---

## 3) Assign Required Permissions

Grant the Klaviyo account the following privileges on the schemas created in Step 1. Replace `klaviyo_service_user` with your actual username or service principal name, and prefix schemas with the correct catalog (e.g., `main`).

| Schema | Minimum Required Privileges | Purpose |
| --- | --- | --- |
| `KLAVIYO_TMP` | `ALL PRIVILEGES` **or** the combination of `USE SCHEMA`, `MODIFY`, `SELECT`, and `CREATE TABLE` | Allows Klaviyo to create and manage temporary tables during sync. |
| `KLAVIYO_IMPORT_FROM_DWH` | `USE SCHEMA`, `SELECT` | Allows Klaviyo to read your tables and views. |

```
-- Grant permissions on temporary schema
GRANT ALL PRIVILEGES ON SCHEMA main.KLAVIYO_TMP TO `klaviyo_service_user`;

-- OR, grant granular privileges:
GRANT USE SCHEMA, MODIFY, SELECT, CREATE TABLE ON SCHEMA main.KLAVIYO_TMP TO `klaviyo_service_user`;

-- Grant read-only access to import schema
GRANT USE SCHEMA, SELECT ON SCHEMA main.KLAVIYO_IMPORT_FROM_DWH TO `klaviyo_service_user`;
```

****Best practice:**** Apply the principle of least privilege—grant only what’s required.

---

## 4) Verify Your Setup (Optional)

### 4.1 Confirm the schemas exist

Run in a Databricks SQL notebook or editor:

```
SHOW SCHEMAS IN main;  -- replace 'main' with your catalog if different
```

You should see:

```
klaviyo_import_from_dwh
klaviyo_tmp
```

### 4.2 Test authentication (using your PAT)

Use the Databricks CLI with the same token you plan to provide to Klaviyo:

```
# Set your token and host (example for AWS)
export DATABRICKS_HOST="https://<your-workspace>.cloud.databricks.com"
export DATABRICKS_TOKEN="<your-PAT>"

# Run a simple API call
databricks current-user me
```

**Expected result:** JSON output showing the user or service principal details (e.g., display name, user ID). If you get an HTTP 403 or authentication error, verify the token and host URL.

### 4.3 Check permissions on each schema

```
SHOW GRANTS ON SCHEMA main.klaviyo_tmp;
SHOW GRANTS ON SCHEMA main.klaviyo_import_from_dwh;
```

Confirm that your Klaviyo account appears with the expected privileges (e.g., `USE SCHEMA`, `SELECT`, `MODIFY`, `CREATE TABLE`).

### 4.4 Validate create/read operations

```
-- Test create/drop in KLAVIYO_TMP
USE SCHEMA main.klaviyo_tmp;
CREATE TABLE IF NOT EXISTS test_permissions (id INT);
DROP TABLE test_permissions;

-- Test select in KLAVIYO_IMPORT_FROM_DWH
USE SCHEMA main.klaviyo_import_from_dwh;
SHOW TABLES;
```

****Tips:****

- Run these verification steps using the same identity and PAT that you’ll share with Klaviyo.
- Retain the SQL grant statements and verification output for audit/troubleshooting.
- Rotate the PAT on a regular cadence and after staff changes.

---

## 5) Connect Klaviyo to Databricks

Once Databricks is configured, complete the connection in Klaviyo.

1. In Klaviyo, open the ****left sidebar**** and navigate to ****Advanced > Syncing****.
2. Click ****Create sync****.
3. Select ****Import data from your data warehouse****.
4. Choose ****Databricks**** as your data warehouse.
5. Click ****Connect to Databricks****.

When prompted, provide the following connection details:

| Field | Description | Where to Find It |
| --- | --- | --- |
| ****Hostname**** | The host indicated in the URL of your Databricks workspace. | Found in your browser’s address bar when logged into Databricks:  `https://<your-workspace>.cloud.databricks.com`    Example: `abc-12345678.cloud.databricks.com` |
| ****HTTP Path**** | The HTTP path of the SQL Warehouse to use for queries. | In the Databricks UI:   1. Go to ****SQL Warehouses****. 2. Select the warehouse you plan to use. 3. Copy the ****HTTP Path**** under ****Connection details****.   Example: `/sql/1.0/warehouses/1234abcd5678efgh` |
| ****Catalog**** | The catalog containing your Klaviyo schemas (e.g., `main`). | Verify using:  SHOW CATALOGS; |
| ****Access Token**** | The personal access token (PAT) you created in Step 2. | Store and paste the token securely during setup. |

****After you connect:**** Klaviyo will test the connection and confirm access to your Databricks environment. Once verified, you can configure syncs to import data from the schemas you prepared earlier.

---

**Next step:** After connecting successfully, proceed to create your first sync in Klaviyo and start importing data from Databricks.