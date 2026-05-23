<h1>Connecting Klaviyo and BigQuery (Reverse ETL)</h1>

[Advanced KDP](https://help.klaviyo.com/hc/en-us/articles/17655007276059) is not included in Klaviyo’s standard marketing application, and a subscription is required to access the associated functionality. Head to our [billing guide](https://help.klaviyo.com/hc/en-us/articles/115000976672) to learn about how to purchase this plan.

# Environment Setup and Connection

****Overview:**** Follow these steps to prepare BigQuery for Klaviyo. You’ll create required schemas (in a dataset/project), set up a dedicated service account and key, assign the minimum required privileges, verify the configuration, and connect BigQuery to Klaviyo.

For details on how data warehouse import works in Klaviyo—including schema structure, required tables, and field mappings—see [How Data Warehouse Imports Work in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/40939206649627).

---

## 1) Create Required Schemas / Datasets

In BigQuery, create two datasets in the project you’ll use for Klaviyo.

```
CREATE SCHEMA `KLAVIYO_IMPORT_FROM_DWH`;
CREATE SCHEMA `KLAVIYO_TMP`;
```

- `KLAVIYO_IMPORT_FROM_DWH`: Tables and views created in this dataset will be available for Klaviyo to read/write.
- `KLAVIYO_TMP`: Temporary or staging data used during sync operations.

---

## 2) Create the Klaviyo Service Account and Key

Create a Google service account (e.g. KLAVIYO\_DATA\_TRANSFER\_USER) that Klaviyo will use exclusively for this integration. Download a JSON key for this account and store it securely.

- Go to ****IAM & Admin → Service accounts**** in the GCP Console.
- Create a new service account (or select an existing one dedicated to Klaviyo).
- In the Keys tab, create a new key of type JSON. Keep this key file safe — you’ll need it when configuring the connection in Klaviyo.

---

## 3) Assign Required Permissions

Grant the service account the following roles, scoped to the two datasets you created:

| Dataset | Minimum Required Roles | Description |
| --- | --- | --- |
| `KLAVIYO_TMP` | `BigQuery Data Editor` + `BigQuery Job User` | Allows Klaviyo to create and manage temporary tables, jobs, etc. |
| `KLAVIYO_IMPORT_FROM_DWH` | `BigQuery Data Viewer` + `BigQuery Job User` | Allows Klaviyo to read from your tables. |

```
-- Example commands in GCP CLI (replace placeholders):
gcloud projects add-iam-policy-binding YOUR_PROJECT_ID \
  --member="serviceAccount:KLAVIYO_DATA_TRANSFER_USER@YOUR_PROJECT_ID.iam.gserviceaccount.com" \
  --role="roles/bigquery.dataEditor" \
  --condition=None \
  --dataset="KLAVIYO_TMP"

gcloud projects add-iam-policy-binding YOUR_PROJECT_ID \
  --member="serviceAccount:KLAVIYO_DATA_TRANSFER_USER@YOUR_PROJECT_ID.iam.gserviceaccount.com" \
  --role="roles/bigquery.dataViewer" \
  --condition=None \
  --dataset="KLAVIYO_IMPORT_FROM_DWH"
```

---

## 4) Verify Your Setup (Optional)

### 4.1 Confirm the datasets exist

```
SELECT schema_name
FROM `YOUR_PROJECT_ID.INFORMATION_SCHEMA.SCHEMATA`
WHERE schema_name IN ('KLAVIYO_IMPORT_FROM_DWH','KLAVIYO_TMP');
```

### 4.2 Confirm service account access

Use the service account key to authenticate with the BigQuery CLI or API and run a simple query:

```
bq --project_id=YOUR_PROJECT_ID \
   --dataset_id=KLAVIYO_IMPORT_FROM_DWH \
   query --use_legacy_sql=false \
   'SELECT COUNT(*) FROM `YOUR_PROJECT_ID.KLAVIYO_IMPORT_FROM_DWH.some_table` LIMIT 1'
```

### 4.3 Check permissions on each dataset

```
SELECT *
FROM `YOUR_PROJECT_ID.KLAVIYO_IMPORT_FROM_DWH.INFORMATION_SCHEMA.OBJECT_PRIVILEGES`
WHERE grantee = 'KLAVIYO_DATA_TRANSFER_USER@YOUR_PROJECT_ID.iam.gserviceaccount.com';
```

### 4.4 Optional: Validate create/read operations

```
-- Test create in KLAVIYO_TMP
CREATE TABLE `YOUR_PROJECT_ID.KLAVIYO_TMP.test_permissions` (id INT64);
DROP TABLE `YOUR_PROJECT_ID.KLAVIYO_TMP.test_permissions`;

-- Test select in KLAVIYO_IMPORT_FROM_DWH
SELECT * FROM `YOUR_PROJECT_ID.KLAVIYO_IMPORT_FROM_DWH.some_existing_table` LIMIT 1;
```

****Tip:**** Run these checks using the same service account and key that you will provide to Klaviyo. Keep a copy of the results for auditing.

---

## 5) Connect Klaviyo to BigQuery

Once your BigQuery environment is configured, complete the connection in Klaviyo.

1. In Klaviyo, navigate to ****Advanced → Syncing**** in the left sidebar.
2. Click ****Create sync****.
3. Select ****Import or export data to your data warehouse****.
4. Choose ****BigQuery**** as your data warehouse.
5. Click ****Connect to BigQuery****.

When prompted, provide the following connection configuration details:

| Field | Description | Where to Find It |
| --- | --- | --- |
| ****Project ID**** | Your Google Cloud Project ID. | Found in the GCP console at the top of the project page. |
| ****Dataset**** | The dataset (schema) containing your Klaviyo tables (e.g., `KLAVIYO_IMPORT_FROM_DWH`). | Use the dataset you created in Step 1. Select that dataset when configuring the connection. |
| ****Service Account Key (JSON)**** | The JSON key file you downloaded for the service account. | Upload or paste the contents of the JSON key file you created in Step 2. |

****After you connect:**** Klaviyo will validate the connection, test access to your datasets, and then allow you to configure syncs — for both importing data into Klaviyo and exporting Klaviyo data into BigQuery.

---

**Next step:** After connecting successfully, create your first import or export sync in Klaviyo and begin moving data to or from BigQuery.
